Summary:         Simple multicast DNS library for Qt
Name:            qmdnsengine
Version:         0.2.0
Release:         1%{?dist}
License:         LGPL
URL:             https://github.com/nitroshare/qmdnsengine
Source0:         https://github.com/nitroshare/qmdnsengine/archive/refs/tags/%{version}.tar.gz

BuildRequires:   cmake
BuildRequires:	 ninja-build
BuildRequires:	 gcc
BuildRequires:	 gcc-c++
BuildRequires:	 qt5-qtbase-devel

Requires:	 qt5-qtbase

%description
Simple multicast DNS library for Qt

# disable debuginfo, which is useless on binary-only packages
%define debug_package %{nil}

%prep
%setup -q -n %{name}-%{version}

%build
cmake -B build -G Ninja -DCMAKE_INSTALL_PREFIX='/usr' -DBUILD_TESTS=ON
cmake --build build

%install
DESTDIR="%{buildroot}" cmake --install build

%files
/usr/include/qmdnsengine/abstractserver.h
/usr/include/qmdnsengine/bitmap.h
/usr/include/qmdnsengine/browser.h
/usr/include/qmdnsengine/cache.h
/usr/include/qmdnsengine/dns.h
/usr/include/qmdnsengine/hostname.h
/usr/include/qmdnsengine/mdns.h
/usr/include/qmdnsengine/message.h
/usr/include/qmdnsengine/prober.h
/usr/include/qmdnsengine/provider.h
/usr/include/qmdnsengine/qmdnsengine_export.h
/usr/include/qmdnsengine/query.h
/usr/include/qmdnsengine/record.h
/usr/include/qmdnsengine/resolver.h
/usr/include/qmdnsengine/server.h
/usr/include/qmdnsengine/service.h
/usr/lib/cmake/qmdnsengine/qmdnsengineConfig-noconfig.cmake
/usr/lib/cmake/qmdnsengine/qmdnsengineConfig.cmake
/usr/lib/cmake/qmdnsengine/qmdnsengineConfigVersion.cmake
/usr/lib/libqmdnsengine.so.0.2.0
/usr/lib/libqmdnsengine.so
/usr/lib/libqmdnsengine.so.0
