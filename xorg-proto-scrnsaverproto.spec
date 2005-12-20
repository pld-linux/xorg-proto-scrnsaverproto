Summary:	ScrnSaver protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u ScrnSaver i pomocnicze
Name:		xorg-proto-scrnsaverproto
Version:	1.0.2
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC4/proto/scrnsaverproto-%{version}.tar.bz2
# Source0-md5:	f5687667b79e8eade58c8d51a889f0b7
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ScrnSaver protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u ScrnSaver i pomocnicze.

%package devel
Summary:	ScrnSaver protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u ScrnSaver i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
ScrnSaver protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u ScrnSaver i pomocnicze.

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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/scrnsaverproto.pc
