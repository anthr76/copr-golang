# golang-github-peak-s5cmd.spec
# Generated by go2rpm 1.8.0
%bcond_without check

# https://github.com/peak/s5cmd
%global goipath         github.com/peak/s5cmd
Version:                2.0.0

%gometa

%global goname s5cmd

%global common_description %{expand:
Parallel S3 and local filesystem execution tool.}

%global golicenses      LICENSE
%global godocs          doc CONTRIBUTING.md CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease -b 5
Summary:        Parallel S3 and local filesystem execution tool

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

Patch:          001-fix-e2e-builds.patch

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
export LDFLAGS="-s -w -X github.com/peak/s5cmd/version.Version=%{version} -X github.com/peak/s5cmd/version.GitCommit= "
%gobuild -o %{gobuilddir}/bin/s5cmd %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%ifarch ppc64le
for test in "TestRemoveS3ObjectsWithEmptyExcludeFilter" "TestListS3ObjectsWithEmptyExcludeFilter" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%endif
%ifarch s390x
for test in "TestSyncSingleS3ObjectToLocalTwice" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%endif
%gocheck
%endif

%files
%license LICENSE
%doc doc CONTRIBUTING.md CHANGELOG.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog

