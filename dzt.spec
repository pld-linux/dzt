Summary:	Yet Another Tabbed GNOME Terminal
Summary:	Jeszcze jeden GNOME Terminal z zak³adkami
Name:		dzt
Version:	1.1.1
Release:	3
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	3472795fc9914924a56c155048581fdd
Patch0:		%{name}-config.patch
Patch1:		%{name}-desktop.patch
URL:		http://dzt.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
dzt is a YATGT (Yet Another Tabbed GNOME Terminal). It is a
multi-tabbed/paged terminal which is simple, configurable, and quick
to use.

Install dzt if you want a simple, quick, clean, and stable YATGT.

%description -l pl
dzt jest JJGTZ (Jeszcze Jeden GNOME Terminal z Zak³adkami). Jest to
wielozak³adkowy terminal, który jest prosty, konfigurowalny i szybki w
u¿yciu.

Zainstaluj dzt je¶li potrzebujesz prostego, szybkiego, pozbawionego
udziwnieñ oraz stabilnego JJGTZ.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
rm -f macros/Makefile.am
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_desktopdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
