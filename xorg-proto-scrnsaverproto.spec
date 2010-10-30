Summary:	ScrnSaver extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia ScrnSaver
Name:		xorg-proto-scrnsaverproto
Version:	1.2.1
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/scrnsaverproto-%{version}.tar.bz2
# Source0-md5:	6af0f2e3369f5f74e69345e214f5fd0d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xmlto >= 0.0.20
BuildRequires:	xorg-sgml-doctools >= 1.5
BuildRequires:	xorg-util-util-macros >= 1.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ScrnSaver extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia ScrnSaver.

%package devel
Summary:	ScrnSaver extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia ScrnSaver
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
ScrnSaver extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia ScrnSaver.

%prep
%setup -q -n scrnsaverproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README specs/*.{html,css}
%{_includedir}/X11/extensions/saver*.h
%{_pkgconfigdir}/scrnsaverproto.pc
