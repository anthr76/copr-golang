# Generated by go2rpm 1.6.0
%bcond_without check

# https://github.com/siderolabs/talos
%global goipath         github.com/siderolabs/talos
Version:                1.1.2

%gometa

%global common_description %{expand:
Talos Linux is a modern Linux distribution built for Kubernetes.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md ADOPTERS.md CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Talos Linux is a modern Linux distribution built for Kubernetes

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep
rm -r docs website

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CONTRIBUTING.md ADOPTERS.md CHANGELOG.md README.md 
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog