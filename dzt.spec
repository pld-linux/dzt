Summary:	Yet Another Tabbed GNOME Terminal
Summary:	Jeszcze jeden GNOME Terminal z zak³adkami
Name:		dzt
Version:	1.0.0
Release:	1
License:	GPL
Group:		X11/Applications
URL:		http://dzt.sourceforge.net/
Source0:	http://telia.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gnome-libs-devel

%description
dzt is a YATGT (Yet Another Tabbed GNOME Terminal). It is a
multi-tabbed/paged terminal which is simple, configurable, and quick
to use.

Install dzt if you want a simple, quick, clean, and stable YATGT

%description -l pl
dzt jest JJGTZ (Jeszcze Jeden GNOME Terminal z Zak³adkami). Jest to
wielozak³adkowy terminal, który jest prosty, konfigurowalny i szybki
w u¿yciu.

Zainstaluj dzt je¶li potrzebujsz prostego, szybkiego, pozbawionego
udziwnieñ oraz stablinego JJGTZ.

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
aclocal -I %{_aclocaldir}/gnome
autoconf
rm -f macros/Makefile.am
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Terminals
install dzt.desktop $RPM_BUILD_ROOT%{_applnkdir}/Terminals


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc README AUTHORS ChangeLog
%{_datadir}/gnome/help/dzt/*
%{_applnkdir}/Terminals/*
