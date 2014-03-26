%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE desktop calculator
Name:		mate-calc
Version:	1.8.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
#Patch0:		mate-calc-1.4.0-rosa-yyscan_t.patch

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	mate-common
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libxml-2.0)

%description
mate-calc is a desktop calculator.
It has Basic, Financial and Scientific modes. Internally it uses multiple
precision arithmetic to produce results to a high degree of accuracy.

%prep
%setup -q
%apply_patches
NOCONFIGURE=yes ./autogen.sh

%build
%configure2_5x \
	--with-gtk=2.0

%make

%install
%makeinstall_std
desktop-file-edit --remove-category=MATE --add-category=X-MATE %{buildroot}%{_datadir}/applications/mate-calc.desktop

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc README NEWS AUTHORS 
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.mate.calc.gschema.xml
%{_mandir}/man1/*

