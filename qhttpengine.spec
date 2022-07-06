Summary:         Simple and secure HTTP server for Qt
Name:            qhttpengine
Version:         1.0.1
Release:         1%{?dist}
License:         LGPL
URL:             https://github.com/nitroshare/qhttpengine
Source0:         https://github.com/nitroshare/qhttpengine/archive/refs/tags/%{version}.tar.gz

BuildRequires:   cmake
BuildRequires:	 ninja-build
BuildRequires:	 gcc
BuildRequires:	 gcc-c++
BuildRequires:	 qt5-qtbase-devel

Requires:	 qt5-qtbase

%description
Simple and secure HTTP server for Qt

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
/usr/include/qhttpengine/basicauthmiddleware.h
/usr/include/qhttpengine/filesystemhandler.h
/usr/include/qhttpengine/handler.h
/usr/include/qhttpengine/ibytearray.h
/usr/include/qhttpengine/localauthmiddleware.h
/usr/include/qhttpengine/localfile.h
/usr/include/qhttpengine/middleware.h
/usr/include/qhttpengine/parser.h
/usr/include/qhttpengine/proxyhandler.h
/usr/include/qhttpengine/qhttpengine_export.h
/usr/include/qhttpengine/qiodevicecopier.h
/usr/include/qhttpengine/qobjecthandler.h
/usr/include/qhttpengine/range.h
/usr/include/qhttpengine/server.h
/usr/include/qhttpengine/socket.h
/usr/lib/cmake/qhttpengine/qhttpengineConfig-noconfig.cmake
/usr/lib/cmake/qhttpengine/qhttpengineConfig.cmake
/usr/lib/cmake/qhttpengine/qhttpengineConfigVersion.cmake
/usr/lib/libqhttpengine.so
/usr/lib/libqhttpengine.so.1
/usr/lib/libqhttpengine.so.1.0.1
/usr/lib/pkgconfig/qhttpengine.pc
