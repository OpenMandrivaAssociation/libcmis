%define api 0.6
%define major 6
%define oldlibname %mklibname cmis 0.5 5
%define oldlibcmis_c %mklibname cmis-c 0.5 5
%define libname %mklibname cmis
%define libcmis_c %mklibname cmis-c
%define devname %mklibname -d cmis

Summary:	A C++ client library for the CMIS interface
Name:		libcmis
Version:	0.6.2
Release:	2
Group:		System/Libraries
License:	GPLv2+ or LGPLv2+ or MPLv1.1
Url:		https://github.com/tdf/libcmis/
Source0:	https://github.com/tdf/libcmis/releases/download/v%{version}/libcmis-%{version}.tar.gz
BuildRequires:	docbook2x
BuildRequires:	boost-devel >= 1.73.0-0
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
%rename %{oldlibname}

%description -n %{libname}
LibCMIS is a C++ client library for the CMIS interface. This allows C++
applications to connect to any ECM behaving as a CMIS server like
Alfresco, Nuxeo for the open source ones.

%package -n %{libcmis_c}
Summary:	Text categorization library
Group:		System/Libraries
%rename %{oldlibcmis_c}

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
%autosetup -p1

%build
%configure \
	--disable-tests \
	--disable-werror \
	--with-man=no

%make_build

%install
%make_install

%files tools
%{_bindir}/cmis-client

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}*

%files -n %{libcmis_c}
%{_libdir}/%{name}-c-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING.GPL COPYING.LGPL COPYING.MPL NEWS
%{_includedir}/%{name}-%{api}
%{_includedir}/%{name}-c-%{api}
%{_libdir}/%{name}-%{api}.so
%{_libdir}/%{name}-c-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/pkgconfig/%{name}-c-%{api}.pc
