Name:           cambalache
Version:        0.10.3
Release:        1
Summary:        Is a new RAD tool for Gtk 4 and 3 with a clear MVC design
License:        LGPL-2.1-only
URL:            https://gitlab.gnome.org/jpu/cambalache
Source:         https://gitlab.gnome.org/jpu/cambalache/-/archive/%{version}/cambalache-%{version}.tar.bz2
  
BuildRequires:  meson
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3dist(lxml)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libhandy-1)

%description
Cambalache is a new RAD tool for Gtk 4 and 3 with a clear MVC design and data model first philosophy.
This translates to a wide feature coverage with minimal/none 

%package devel
Summary:        Development files for %{name}
Group:          System/Libraries
#Requires:       typelib-1_0-CambalachePrivate-3.0
#Requires:       typelib-1_0-CambalachePrivate-4.0
BuildArch:      noarch

%description devel
Cambalache is a new RAD tool for Gtk 4 and 3 with a clear MVC design and data model first philosophy.
This translates to a wide feature coverage with minimal/none developer intervention for basic support.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
  
#find_lang %{name}

%files    
