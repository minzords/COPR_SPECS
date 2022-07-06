Summary:         Lecture de l'actualité & célébrité.
Name:            qpresse
Version:         1.0
Release:         1%{?dist}
License:         BSD
URL:             https://minzord.ca
Source0:         https://miroir.minzord.ca/%{name}.tar.xz

BuildRequires:   gcc
BuildRequires:   make
BuildRequires:	 qt5-qtbase-devel
BuildRequires:   qt5-qtwebengine-devel

Requires:        qt5-qtbase
Requires:        qt5-qtwebengine

%description
Lecture de l'actualité & célébrité. (Quebec)

# disable debuginfo, which is useless on binary-only packages
%define debug_package %{nil}

%prep
%setup -q -n %{name}

%build
qmake-qt5 -makefile QPresse.pro
%make_build


%install
install -D -t %{buildroot}%{_bindir} QPresse
install -Dm644 -t %{buildroot}%{_datadir}/pixmaps QPresse.png
install -Dm644 -t %{buildroot}%{_datadir}/applications QPresse.desktop


%files
%{_bindir}/QPresse
%{_datadir}/pixmaps/QPresse.png
%{_datadir}/applications/QPresse.desktop
