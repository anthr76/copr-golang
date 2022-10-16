# Generated by go2rpm 1.8.2
%bcond_without check

# https://github.com/terraform-docs/terraform-docs
%global goipath         github.com/terraform-docs/terraform-docs
Version:                0.16.0

%gometa -f

%global common_description %{expand:
Generate documentation from Terraform modules in various output formats.}

%global golicenses      LICENSE
%global godocs          docs examples CONTRIBUTING.md README.md docs

%global goname  terraform-docs
Name:           %{goname}
Release:        %autorelease
Summary:        Generate documentation from Terraform modules in various output formats

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%gobuild -o %{gobuilddir}/bin/terraform-docs %{goipath}
for cmd in scripts/docs; do
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
%doc docs examples CONTRIBUTING.md README.md docs
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog