Name:           shortwave
Version:        3.0.0
Release:        1%{?dist}
Summary:        Find and listen to internet radio stations

License:       	GPL3
URL:            https://gitlab.gnome.org/World/Shortwave
Source0:        https://gitlab.gnome.org/World/Shortwave/-/archive/%{version}/Shortwave-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:	rust
BuildRequires:	cargo
BuildRequires:	libshumate-devel
BuildRequires:	libadwaita-devel
BuildRequires:  gstreamer1-devel
BuildRequires:	pkgconfig(gstreamer-audio-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(glib-2.0)

Requires:       gtk4
Requires:       gstreamer1
Requires:       libshumate
Requires:       libadwaita
Requires:	glib2

%description
Find and listen to internet radio stations


%prep
%setup -q -n Shortwave-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
/usr/bin/shortwave
/usr/lib/debug/usr/bin/shortwave-3.0.0-1.fc36.x86_64.debug
/usr/share/applications/de.haeckerfelix.Shortwave.desktop
/usr/share/dbus-1/services/de.haeckerfelix.Shortwave.service
/usr/share/glib-2.0/schemas/de.haeckerfelix.Shortwave.gschema.xml
/usr/share/icons/hicolor/scalable/apps/de.haeckerfelix.Shortwave.svg
/usr/share/icons/hicolor/symbolic/apps/de.haeckerfelix.Shortwave-symbolic.svg
/usr/share/locale/ca/LC_MESSAGES/shortwave.mo
/usr/share/locale/cs/LC_MESSAGES/shortwave.mo
/usr/share/locale/da/LC_MESSAGES/shortwave.mo
/usr/share/locale/de/LC_MESSAGES/shortwave.mo
/usr/share/locale/el/LC_MESSAGES/shortwave.mo
/usr/share/locale/en_GB/LC_MESSAGES/shortwave.mo
/usr/share/locale/es/LC_MESSAGES/shortwave.mo
/usr/share/locale/eu/LC_MESSAGES/shortwave.mo
/usr/share/locale/fi/LC_MESSAGES/shortwave.mo
/usr/share/locale/fr/LC_MESSAGES/shortwave.mo
/usr/share/locale/gl/LC_MESSAGES/shortwave.mo
/usr/share/locale/he/LC_MESSAGES/shortwave.mo
/usr/share/locale/hr/LC_MESSAGES/shortwave.mo
/usr/share/locale/hu/LC_MESSAGES/shortwave.mo
/usr/share/locale/id/LC_MESSAGES/shortwave.mo
/usr/share/locale/it/LC_MESSAGES/shortwave.mo
/usr/share/locale/nl/LC_MESSAGES/shortwave.mo
/usr/share/locale/oc/LC_MESSAGES/shortwave.mo
/usr/share/locale/pl/LC_MESSAGES/shortwave.mo
/usr/share/locale/pt/LC_MESSAGES/shortwave.mo
/usr/share/locale/pt_BR/LC_MESSAGES/shortwave.mo
/usr/share/locale/ro/LC_MESSAGES/shortwave.mo
/usr/share/locale/ru/LC_MESSAGES/shortwave.mo
/usr/share/locale/sk/LC_MESSAGES/shortwave.mo
/usr/share/locale/sl/LC_MESSAGES/shortwave.mo
/usr/share/locale/sr/LC_MESSAGES/shortwave.mo
/usr/share/locale/sv/LC_MESSAGES/shortwave.mo
/usr/share/locale/tr/LC_MESSAGES/shortwave.mo
/usr/share/locale/uk/LC_MESSAGES/shortwave.mo
/usr/share/locale/vi/LC_MESSAGES/shortwave.mo
/usr/share/locale/zh_CN/LC_MESSAGES/shortwave.mo
/usr/share/metainfo/de.haeckerfelix.Shortwave.metainfo.xml
/usr/share/shortwave/de.haeckerfelix.Shortwave.gresource
