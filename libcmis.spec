%define api	0.5
%define major	5
%define libname %mklibname cmis %{api} %{major}
%define libcmis_c %mklibname cmis-c %{api} %{major}
%define devname %mklibname -d cmis

Summary:	A C++ client library for the CMIS interface
Name:		libcmis
Version:	0.5.0
Release:	15
Group:		System/Libraries
License:	GPLv2+ or LGPLv2+ or MPLv1.1
Url:		http://sourceforge.net/projects/libcmis/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch1:		0001-fix-boost-configuration-with-gcc-5.patch

BuildRequires:	docbook2x
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	autoconf

%description
LibCMIS is a C++ client library for the CMIS interface. This allows C++
applications to connect to any ECM behaving as a CMIS server like
Alfresco, Nuxeo for the open source ones.

%package -n %{libname}
Summary:	Text categorization library
Group:		System/Libraries

%description -n %{libname}
LibCMIS is a C++ client library for the CMIS interface. This allows C++
applications to connect to any ECM behaving as a CMIS server like
Alfresco, Nuxeo for the open source ones.

%package -n %{libcmis_c}
Summary:	Text categorization library
Group:		System/Libraries

%description -n %{libcmis_c}
This package contains a shared library for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libcmis_c} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:	Command line tool to access CMIS
Group:		Publishing

%description tools
The %{name}-tools package contains a tool for accessing CMIS from the
command line.

%prep
%setup -q
%apply_patches
sed -i -e 's/docbook-to-man/db2x_docbook2man/' configure
autoreconf -fiv

%build
export CC=gcc
export CXX=g++
%configure \
	--disable-tests \
	--disable-werror \
	--with-man=no

%make

%install
%makeinstall_std

%files tools
%{_bindir}/cmis-client
%{_mandir}/manx/cmis-client.xml.*

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}*

%files -n %{libcmis_c}
%{_libdir}/%{name}-c-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING.GPL COPYING.LGPL COPYING.MPL README
%{_includedir}/%{name}-%{api}
%{_includedir}/%{name}-c-%{api}
%{_libdir}/%{name}-%{api}.so
%{_libdir}/%{name}-c-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/pkgconfig/%{name}-c-%{api}.pc

