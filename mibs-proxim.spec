Summary:	MIBs for Proxim Networking Hardware
Summary(pl):	MIB-y dla sprzêtu sieciowego Proxim
Name:		net-snmp-mibs-proxim
Version:	2.2.5
Release:	1
License:	Unknown
Group:		Applications/System
Source0:	http://keygen.proxim.com/support/tsunami/mp11/tmp225/MIBs.zip
# Source0-md5:	9d1a3a8d0e18d1cddb5287b3e9bcd279
BuildRequires:	unzip
Requires:	net-snmp-mibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIBs for Proxim Networking Hardware.

%description -l pl
MIB-y dla sprzêtu sieciowego Proxim.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/snmp/mibs

for file in *.mib; do
	b=$(basename "$file" .mib)
	install "$file" $RPM_BUILD_ROOT%{_datadir}/snmp/mibs/mib-${b}.txt
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/snmp/mibs/*.*
