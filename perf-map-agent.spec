%define rel_ver 0.9.0

Summary: A java agent to generate method mappings to use with the linux `perf` tool
Name: perf-map-agent
Version: %{rel_ver}
Release: 1%{?dist}
License: GPLv2
Group: System/utils
URL: https://github.com/jvm-profiling-tools/perf-map-agent
Source0: perf-map-agent-0.9.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{rel_ver}-%{release}-root
Requires: perf,java
BuildRequires: cmake,make,gcc-c++,java
AutoReqProv: no

%description
perf-map-agent is an agent that supplys dynamic symbol mappings of a Java process
used by the perf.

It consists of a Java agent written C and a small Java bootstrap application which
attaches the agent to a running Java process.

%prep
%setup -q -n perf-map-agent-0.9

%build
cmake .
make

%install
mkdir -p %{buildroot}/opt/%{name}
cp -a bin out %{buildroot}/opt/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/%{name}

%changelog
* Wed Jul 9 2019 Tigran Mkrtchyan <tigran.mkrtchyan@desy.dde>
- Initialize package creation
