%define  lib_name_orig libalsa
%define  api 0.2
%define  major 2
%define  lib_name %mklibname cmis %api %major
%define  develname %mklibname -d cmis

Name: libcmis
Version: 0.2.3
Release: %mkrel 3
Summary: A C++ client library for the CMIS interface
Group: System/Libraries
License: GPL+ or LGPLv2+ or MPLv1.1
URL: http://sourceforge.net/projects/libcmis/
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires: boost-devel
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
BuildRequires: docbook2x

%description
LibCMIS is a C++ client library for the CMIS interface. This allows C++
applications to connect to any ECM behaving as a CMIS server like
Alfresco, Nuxeo for the open source ones.

#--------------------------------------------------------------------

%package -n %lib_name
Summary: Text categorization library
Group:   System/Libraries
Obsoletes: %{_lib}cmis2 < %{version}-%{release}

%description -n %lib_name
LibCMIS is a C++ client library for the CMIS interface. This allows C++
applications to connect to any ECM behaving as a CMIS server like
Alfresco, Nuxeo for the open source ones.

%files -n %lib_name
%doc AUTHORS COPYING.GPL COPYING.LGPL COPYING.MPL README
%{_libdir}/%{name}-%{api}.so.%{major}*

#--------------------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/Other
Requires: %lib_name = %version-%release
Obsoletes: %{name}-devel < %version-%release
Provides: %{name}-devel = %version-%release

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -n %{develname}
%{_includedir}/%{name}-%{api}
%{_libdir}/%{name}-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc

#--------------------------------------------------------------------

%package tools
Summary: Command line tool to access CMIS
Group:    Publishing

%description tools
The %{name}-tools package contains a tool for accessing CMIS from the
command line.

%files tools
%{_bindir}/cmis-client
%{_mandir}/manx/cmis-client.xml.*

#--------------------------------------------------------------------

%prep
%setup -q
sed -i -e 's/docbook-to-man/db2x_docbook2man/' configure

%build
%configure2_5x --disable-static --disable-tests --disable-werror --with-man=no
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make


%install
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/*.la


%changelog

* Tue Jul 31 2012 fwang <fwang> 0.2.3-3.mga3
+ Revision: 276497
- rebuild for new boost

* Sun Jul 15 2012 fwang <fwang> 0.2.3-2.mga3
+ Revision: 270983
- update lib package policy

* Thu Jul 05 2012 dmorgan <dmorgan> 0.2.3-1.mga3
+ Revision: 267991
- New version

* Tue May 29 2012 ovitters <ovitters> 0.1.0-2.mga3
+ Revision: 249431
- rebuild due to new boost

  + dmorgan <dmorgan>
    - imported package libcmis

