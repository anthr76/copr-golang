# golang-github-peak-s5cmd.spec
# Generated by go2rpm 1.8.0
%bcond_without check

# https://github.com/peak/s5cmd
%global goipath         github.com/peak/s5cmd
Version:                2.0.0

# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
# ---
# New Fedora packages should use %%gometa -f, which makes the package
# ExclusiveArch to %%golang_arches_future and thus excludes the package from
# %%ix86. If the new package is needed as a dependency for another pacage,
# please consider removing that package from %%ix86 in the same way, instead of
# building more go packages for i686. If your package is not a leaf package,
# you'll need to coordinate the removal of the package's dependents first.
# ---
# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
%gometa

%global goname s5cmd

%global common_description %{expand:
Parallel S3 and local filesystem execution tool.}

%global golicenses      LICENSE
%global godocs          doc CONTRIBUTING.md CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Parallel S3 and local filesystem execution tool

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

Patch:          001-remove-vendor-test.patch

%description %{common_description}

%gopkg

%prep
%goprep
# Remove vendored go within upstream's SCM
rm -rf vendor/
# Assums vendored go build
%autopatch -p 1

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/s5cmd %{goipath}

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
%doc doc CONTRIBUTING.md CHANGELOG.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog

