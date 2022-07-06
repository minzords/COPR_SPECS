Summary:         LAN file sender application, designed to make transferring files from one device to another extremely simple
Name:            nitroshare
Version:         0.3.4
Release:         1%{?dist}
License:         MIT
URL:             https://github.com/nitroshare/nitroshare-desktop
Source0:         https://github.com/nitroshare/nitroshare-desktop/archive/refs/tags/%{version}.tar.gz
Source1:	 https://raw.githubusercontent.com/archlinux/svntogit-community/packages/nitroshare/trunk/qt-5.11.patch

BuildRequires:   cmake
BuildRequires:	 ninja-build
BuildRequires:	 gcc
BuildRequires:	 gcc-c++
BuildRequires:	 qt5-qtbase-devel
BuildRequires:	 qt5-linguist
BuildRequires:	 qt5-qtsvg-devel
BuildRequires:	 qmdnsengine
BuildRequires:	 qhttpengine

Requires:	 qt5-qtsvg
Requires:	 qmdnsengine
Requires:	 qhttpengine
Requires:	 python3-nautilus

%description
LAN file sender application, designed to make transferring files from one device to another extremely simple

# disable debuginfo, which is useless on binary-only packages
%define debug_package %{nil}

%prep
%setup -q -n %{name}-desktop-%{version}

%build

patch -Np1 -i %{SOURCE1}

# Port filemanager extension to python3
  sed -i 's/from urllib/from urllib.request/
          s/from urlparse/from urllib.parse/' \
    	  src/dist/nitroshare.py.in
  
  cmake -B build -G Ninja -DCMAKE_INSTALL_PREFIX='/usr'
  cmake --build build


%install
DESTDIR="%{buildroot}" cmake --install build

%files
/usr/bin/nitroshare
/usr/bin/nitroshare-send
/usr/share/applications/nitroshare.desktop
/usr/share/caja-python/extensions/nitroshare.py
/usr/share/icons/breeze-dark/apps/22/nitroshare-indicator.svg
/usr/share/icons/breeze/apps/22/nitroshare-indicator.svg
/usr/share/icons/gnome/24x24/apps/nitroshare-indicator.png
/usr/share/icons/hicolor/scalable/apps/nitroshare-indicator.svg
/usr/share/icons/hicolor/scalable/apps/nitroshare.svg
/usr/share/icons/ubuntu-mono-dark/apps/22/nitroshare-indicator.png
/usr/share/icons/ubuntu-mono-dark/apps/24/nitroshare-indicator.svg
/usr/share/icons/ubuntu-mono-light/apps/22/nitroshare-indicator.png
/usr/share/icons/ubuntu-mono-light/apps/24/nitroshare-indicator.svg
/usr/share/kservices5/nitroshare_addtoservicemenu.desktop
/usr/share/man/man1/nitroshare.1.gz
/usr/share/nautilus-python/extensions/nitroshare.py
/usr/share/nemo-python/extensions/nitroshare.py
