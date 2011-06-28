Summary:	X.org input driver for Elographics touchscreen devices
Summary(pl.UTF-8):	Sterownik wejściowy X.org dla ekranów dotykowych Elographics
Name:		xorg-driver-input-elographics
Version:	1.3.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-elographics-%{version}.tar.bz2
# Source0-md5:	9c6616048cd589d6e8540c1d397f64ab
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 1.2
BuildRequires:	xorg-xserver-server-devel >= 1.10.0
BuildRequires:  rpmbuild(macros) >= 1.389
%{?requires_xorg_xserver_xinput}
Requires:	xorg-xserver-server >= 1.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Elographics touchscreen devices. E271-2210 and
E271-2200 devices are supported. E281-2310 and compatible devices are
supported with some features unavailable.

%description -l pl.UTF-8
Sterownik wejściowy X.org dla ekranów dotykowych Elographics.
Obsługiwane są urządzenia E271-2210 i E271-2200, natomiast E281-2381 i
kompatybilne są obsługiwane bez niektórych możliwości.

%prep
%setup -q -n xf86-input-elographics-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/input/elographics_drv.so
%{_mandir}/man4/elographics.4*
