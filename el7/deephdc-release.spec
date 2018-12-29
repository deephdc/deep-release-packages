Name: deephdc-release
Version: 1.0.0
Release: 1%{?dist}
Summary: DEEP-1 (Genesis) Release
License: Apache Software License
Source: %{name}-%{version}.src.tgz
Vendor: DEEP-HybridDataCloud
Group: System Environment/Libraries
BuildArch: noarch
Requires: yum-protectbase
Requires: yum-priorities
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
#BuildRoot: %{_tmppath}/%{name}-%{version}-build


%description
DDEEP-HybridDataCloud repository files

%prep
%setup -q

%build
#Nothing to build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf ${buildroot}

%post
if [ -f /etc/yum/pluginconf.d/priorities.conf ]; then grep -q -e "check_obsoletes" /etc/yum/pluginconf.d/priorities.conf || sed -i -e "/^\[main\]/{G;s/$/\# added by the deephdc-release package\\ncheck_obsoletes = 1/;}" /etc/yum/pluginconf.d/priorities.conf; fi

%postun
if [ "$1" = "0" ]; then grep -q -e "deephdc-release" /etc/yum/pluginconf.d/priorities.conf && sed -i '/deephdc-release/d;/check_obsoletes/d' /etc/yum/pluginconf.d/priorities.conf; fi

%files
%defattr(-,root,root,-)

/etc/deephdc-release
/etc/pki/rpm-gpg/RPM-GPG-KEY-indigodc
/etc/yum.repos.d/deep-1-base.repo
/etc/yum.repos.d/deep-1-third-party.repo
/etc/yum.repos.d/deep-1-updates.repo

%changelog
* Thu Nov 01 2018 Cristina Duma <aiftim@infn.it>
- first release
