Summary:	MIBs for Proxim Networking Hardware
Summary(pl.UTF-8):	MIB-y dla sprzętu sieciowego Proxim
Name:		mibs-proxim
Version:	2.2.5
Release:	1
License:	Unknown
Group:		Applications/System
Source0:	http://keygen.proxim.com/support/tsunami/mp11/tmp225/MIBs.zip
# Source0-md5:	9d1a3a8d0e18d1cddb5287b3e9bcd279
BuildRequires:	unzip
Requires:	mibs-dirs
Obsoletes:	net-snmp-mibs-proxim
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		mibdir	%{_datadir}/mibs

%description
MIBs for Proxim Networking Hardware.

%description -l pl.UTF-8
MIB-y dla sprzętu sieciowego Proxim.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{mibdir}
cp -a *.mib $RPM_BUILD_ROOT%{mibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{mibdir}/*
