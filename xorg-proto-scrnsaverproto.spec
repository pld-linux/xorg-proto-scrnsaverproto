Summary:	ScrnSaver extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia ScrnSaver
Name:		xorg-proto-scrnsaverproto
Version:	1.2.2
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/scrnsaverproto-%{version}.tar.bz2
# Source0-md5:	edd8a73775e8ece1d69515dd17767bfb
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
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
%doc COPYING ChangeLog README specs/saver.html
%{_includedir}/X11/extensions/saver*.h
%{_pkgconfigdir}/scrnsaverproto.pc
