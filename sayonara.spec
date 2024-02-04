%define _disable_ld_no_undefined 1

Summary:	A lightweight Qt Audio player
Name:		sayonara
Version:	1.9.0
Release:	1
License:	GPLv3+
Group:		Sound
Url:		http://sayonara-player.com
Source0:	https://gitlab.com/luciocarreras/sayonara-player/-/archive/%{version}-stable1/sayonara-player-%{version}-stable1.tar.bz2
BuildRequires:	cmake
BuildRequires:  qmake5
BuildRequires:	qt5-linguist-tools
#BuildRequires:	qt5-tools
BuildRequires:  qt5-qttools
BuildRequires:	pkgconfig(gstreamer-app-1.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(zlib)
Requires:	qt5-database-plugin-sqlite

%description
Sayonara is a small, clear, not yet platform-independent music player.
Low CPU usage, low memory consumption and no long loading times are only
three benefits of this player. Sayonara should be easy and intuitive to
use and therefore it should be able to compete with the most popular
music players.

%files
%doc MANUAL README.md
%{_bindir}/%{name}
%{_bindir}/sayonara-ctl
%{_bindir}/sayonara-query
%{_datadir}/%{name}/
%{_datadir}/applications/com.sayonara-player.Sayonara.desktop
%{_iconsdir}/hicolor/*x*/apps/sayonara.png
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/sayonara-ctl.1.*
%{_mandir}/man1/sayonara-query.1.*
%{_datadir}/metainfo/sayonara.appdata.xml

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-player-%{version}-stable1

%build
#cd src
%cmake
%make_build

%install
#cd src
%make_install -C build

# remove menu dir, because it's not necessary
rm -rf %{buildroot}%{_datadir}/menu

