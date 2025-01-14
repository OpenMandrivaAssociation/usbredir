%define oname usbredir

%define major_parser 1
%define libname_parser %mklibname usbredirparser %{major_parser}
%define develname_parser %mklibname usbredirparser -d

%define major_host 1
%define libname_host %mklibname usbredirhost %{major_host}
%define develname_host %mklibname usbredirhost -d

Name:		usbredir
Version:	0.12.0
Release:	2
License:	GPL-2.0+ ; LGPL-2.1+
Summary:	A protocol for redirection USB traffic
URL:		https://spice-space.org/download/usbredir/
Group:		System/Libraries
Source0:	http://spice-space.org/download/usbredir/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libusb-1.0) => 1.0.9
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  meson

%description
usbredir is a protocol for redirection USB traffic from a single USB device,
to a different (virtual) machine then the one to which the USB device is
attached. See usb-redirection-protocol.txt for the description / definition
of this protocol.

# ---------------------------------------------------------------------------

%package -n %{libname_host}
Summary:	A protocol for redirection USB traffic
Group:		System/Libraries

%description -n %{libname_host}
usbredir is a protocol for redirection USB traffic from a single USB device,
to a different (virtual) machine then the one to which the USB device is
attached. See usb-redirection-protocol.txt for the description / definition
of this protocol.

%package -n %{develname_host}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname_host} = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description -n %{develname_host}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

# ---------------------------------------------------------------------------

%package -n %{libname_parser}
Summary:	A protocol for redirection USB traffic
Group:		System/Libraries

%description -n %{libname_parser}
usbredir is a protocol for redirection USB traffic from a single USB device,
to a different (virtual) machine then the one to which the USB device is
attached. See usb-redirection-protocol.txt for the description / definition
of this protocol.

%package -n %{develname_parser}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname_parser} = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description -n %{develname_parser}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

# ---------------------------------------------------------------------------

%package devel
Summary:	A protocol for redirection USB traffic - Development files
Group:		Development/C
Requires:	%{libname_host} = %{version}-%{release}
Requires:	%{libname_parser} = %{version}-%{release}

%description devel
usbredir is a protocol for redirection USB traffic from a single USB device,
to a different (virtual) machine then the one to which the USB device is
attached. See usb-redirection-protocol.txt for the description / definition
of this protocol.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%doc ChangeLog.md README.md COPYING
%{_sbindir}/usbredirserver
%{_bindir}/usbredirect
%{_mandir}/man1/usbredirserver.1.*
%{_mandir}/man1/usbredirect.1.*

%files -n %{libname_host}
%{_libdir}/libusbredirhost.so.%{major_host}*

%files -n %{develname_host}
%{_includedir}/usbredirhost.h
%{_libdir}/libusbredirhost.so
%{_libdir}/pkgconfig/libusbredirhost.pc

%files -n %{libname_parser}
%{_libdir}/libusbredirparser.so.%{major_parser}*

%files -n %{develname_parser}
%{_includedir}/usbredirparser.h
%{_libdir}/libusbredirparser.so
%{_libdir}/pkgconfig/libusbredirparser-0.5.pc

%files devel
%{_includedir}/usbredirproto.h
%{_includedir}/usbredirfilter.h
