Summary:	X.org input driver for Elographics touchscreen devices
Summary(pl):	Sterownik wej¶ciowy X.org dla ekranów dotykowych Elographics
Name:		xorg-driver-input-elographics
Version:	1.1.0
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-elographics-%{version}.tar.bz2
# Source0-md5:	ecb2bf1f800d4f5f4c295f2a0e6b1de7
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Elographics touchscreen devices. E271-2210 and
E271-2200 devices are supported. E281-2310 and compatible devices are
supported with some features unavailable.

%description -l pl
Sterownik wej¶ciowy X.org dla ekranów dotykowych Elographics.
Obs³ugiwane s± urz±dzenia E271-2210 i E271-2200, natomiast E281-2381 i
kompatybilne s± obs³ugiwane bez niektórych mo¿liwo¶ci.

%prep
%setup -q -n xf86-input-elographics-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/input/elographics_drv.so
%{_mandir}/man4/elographics.4*
