Summary:         A stock, currency and cryptocurrency tracker
Name:            bitstower-markets
Version:         0.5.4
Release:         1%{?dist}
License:         LGPL
URL:             https://github.com/bitstower/markets
Source0:         https://github.com/bitstower/markets/archive/refs/tags/%{version}.tar.gz

BuildRequires:   meson
BuildRequires:   ninja-build
BuildRequires:	 cmake
BuildRequires:   vala
BuildRequires:   gtk3-devel
BuildRequires:	 libappstream-glib-devel
BuildRequires:   libhandy-devel
BuildRequires:	 libhandy1
BuildRequires:	 libsoup-devel
BuildRequires:	 libgee-devel
BuildRequires:	 json-glib-devel
BuildRequires:	 glib2-devel


Requires:        gtk3
Requires:        libgee
Requires:        libsoup
Requires:        libhandy
Requires:        json-glib
Requires:        glib2
Requires:	 libhandy1

%description
A stock, currency and cryptocurrency tracker

# disable debuginfo, which is useless on binary-only packages
%define debug_package %{nil}

%prep
%setup -q -n markets-%{version}

%build
meson build --prefix=/usr
cd build
ninja

%install
cd build
DESTDIR=%{buildroot} ninja install

%post
glib-compile-schemas /usr/share/glib-2.0/schemas


%files
/usr/bin/bitstower-markets
/usr/share/appdata/com.bitstower.Markets.appdata.xml
/usr/share/applications/com.bitstower.Markets.desktop
/usr/share/glib-2.0/schemas/com.bitstower.Markets.gschema.xml
/usr/share/icons/hicolor/scalable/apps/com.bitstower.Markets.svg
/usr/share/icons/hicolor/symbolic/apps/com.bitstower.Markets-symbolic.svg
/usr/share/locale/en/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/es/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/fr/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/hr/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/nb_NO/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/nl/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/pl/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/ru/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/sk/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/sv/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/cs/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/de/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/eu/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/gl/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/id/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/it/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/ja/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/pt_BR/LC_MESSAGES/com.bitstower.Markets.mo
/usr/share/locale/tr/LC_MESSAGES/com.bitstower.Markets.mo
