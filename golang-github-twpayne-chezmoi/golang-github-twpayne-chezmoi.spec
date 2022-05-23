# Generated by go2rpm 1.6.0
%bcond_without check

# https://github.com/twpayne/chezmoi
%global goipath         github.com/twpayne/chezmoi
Version:                2.16.0

%gometa

%global common_description %{expand:
Manage your dotfiles across multiple diverse machines, securely.}

%global golicenses      LICENSE assets/chezmoi.io/docs/license.md\\\
                        assets/chezmoi.io/docs/reference/commands/license.md\\\
                        pkg/cmd/licensecmd.go
%global godocs          README.md docs

Name:           %{goname}
Release:        1%{?dist}
Summary:        Manage your dotfiles across multiple diverse machines, securely

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/chezmoi %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE assets/chezmoi.io/docs/license.md
%license assets/chezmoi.io/docs/reference/commands/license.md
%license pkg/cmd/licensecmd.go
%doc README.md docs
%{_bindir}/*

%gopkgfiles

%changelog
* Sun May 22 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 2.16.0-1
- Initial package
