# Generated by go2rpm 1.6.0
%bcond_without check

# https://github.com/twpayne/chezmoi
%global goipath         github.com/twpayne/chezmoi
Version:                2.21.1

%global goname chezmoi

%gometa

%global common_description %{expand:
Manage your dotfiles across multiple diverse machines, securely.}

%global golicenses      LICENSE assets/chezmoi.io/docs/license.md\\\
                        assets/chezmoi.io/docs/reference/commands/license.md\\\
                        pkg/cmd/licensecmd.go
%global godocs          README.md docs

Name:           %{goname}
Release:        %autorelease -b 2
Summary:        Manage your dotfiles across multiple diverse machines, securely

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        %{name}-%{version}-vendored-deps.tar.gz
Source2:        bundled.inc

%include        %SOURCE2

%description
%{common_description}

%gopkg

%prep
%autosetup
tar -xf %SOURCE1 --strip-components=1
%goprep -e -k

%build
export LDFLAGS="-X main.version=%{version}  \
                -X main.date=$(date -d "@${SOURCE_DATE_EPOCH}" +%Y-%m-%d)"
%gobuild -o %{gobuilddir}/bin/chezmoi %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

install -Dpm 0644 completions/%{name}-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 0644 completions/%{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dpm 0644 completions/%{name}.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE assets/chezmoi.io/docs/license.md
%license assets/chezmoi.io/docs/reference/commands/license.md
%license pkg/cmd/licensecmd.go
%doc README.md assets/chezmoi.io/docs
%{_bindir}/*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}


%gopkgfiles

%changelog
%autochangelog
