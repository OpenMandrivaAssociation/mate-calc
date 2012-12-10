Summary:	MATE desktop calculator
Name:		mate-calc
Version:	1.4.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
Patch0:		mate-calc-1.4.0-rosa-yyscan_t.patch

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(mate-doc-utils)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libxml-2.0)

%description
mate-calc is a desktop calculator.
It has Basic, Financial and Scientific modes. Internally it uses multiple
precision arithmetic to produce results to a high degree of accuracy.

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--with-gtk=2.0

%make

%install
%makeinstall_std
desktop-file-edit --remove-category=MATE --add-category=X-MATE %{buildroot}%{_datadir}/applications/mate-calc.desktop

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README NEWS AUTHORS 
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.mate.mate-calc.gschema.xml
%{_mandir}/man1/*
# mate help file
%{_datadir}/mate/help



%changelog
* Tue Jun 05 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 802502
- imported package mate-calc

