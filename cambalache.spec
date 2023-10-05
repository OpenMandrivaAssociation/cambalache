Name:           cambalache
Version:        0.16.0
Release:        1
Summary:        Is a new RAD tool for Gtk 4 and 3 with a clear MVC design
License:        LGPL-2.1-only
URL:            https://gitlab.gnome.org/jpu/cambalache
Source:         https://gitlab.gnome.org/jpu/cambalache/-/archive/%{version}/cambalache-%{version}.tar.bz2

BuildRequires:  appstream-util  
BuildRequires:  meson
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3dist(pygobject)
BuildRequires:  python3dist(lxml)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  %{_lib}harfbuzz-gir-devel

%description
Cambalache is a new RAD tool for Gtk 4 and 3 with a clear MVC design and data model first philosophy.
This translates to a wide feature coverage with minimal/none 

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
  
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/cambalache
%{python_sitelib}/cambalache/
%{_libdir}/girepository-1.0/CambalachePrivate-3.0.typelib
%{_libdir}/girepository-1.0/CambalachePrivate-4.0.typelib
%{_libdir}/libcambalacheprivate-*.so
%{_datadir}/applications/ar.xjuan.Cambalache.desktop
%{_datadir}/cambalache/
%{_datadir}/gir-1.0/CambalachePrivate-3.0.gir
%{_datadir}/gir-1.0/CambalachePrivate-4.0.gir
%{_datadir}/glib-2.0/schemas/ar.xjuan.Cambalache.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/ar.xjuan.Cambalache.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/ar.xjuan.Cambalache.mime.svg
%{_datadir}/icons/hicolor/symbolic/apps/ar.xjuan.Cambalache-symbolic.svg
%{_datadir}/metainfo/ar.xjuan.Cambalache.metainfo.xml
%{_datadir}/mime/packages/ar.xjuan.Cambalache.mime.xml

