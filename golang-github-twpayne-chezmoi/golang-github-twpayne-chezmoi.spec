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
Release:        4%{?dist}
Summary:        Manage your dotfiles across multiple diverse machines, securely

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(filippo.io/age)
BuildRequires:  golang(filippo.io/age/armor)
BuildRequires:  golang(github.com/bmatcuk/doublestar)
BuildRequires:  golang(github.com/bradenhilton/mozillainstallhash)
BuildRequires:  golang(github.com/charmbracelet/glamour)
BuildRequires:  golang(github.com/coreos/go-semver/semver)
BuildRequires:  golang(github.com/go-git/go-git)
BuildRequires:  golang(github.com/go-git/go-git/plumbing)
BuildRequires:  golang(github.com/go-git/go-git/plumbing/filemode)
BuildRequires:  golang(github.com/go-git/go-git/plumbing/format/diff)
BuildRequires:  golang(github.com/go-git/go-git/plumbing/transport)
BuildRequires:  golang(github.com/go-git/go-git/plumbing/transport/http)
BuildRequires:  golang(github.com/google/go-github/github)
BuildRequires:  golang(github.com/google/gops/agent)
BuildRequires:  golang(github.com/google/renameio)
BuildRequires:  golang(github.com/google/renameio/maybe)
BuildRequires:  golang(github.com/gregjones/httpcache)
BuildRequires:  golang(github.com/gregjones/httpcache/diskcache)
BuildRequires:  golang(github.com/Masterminds/sprig/v3)
BuildRequires:  golang(github.com/mitchellh/mapstructure)
BuildRequires:  golang(github.com/pelletier/go-toml/v2)
BuildRequires:  golang(github.com/rs/zerolog)
BuildRequires:  golang(github.com/rs/zerolog/log)
BuildRequires:  golang(github.com/sergi/go-diff/diffmatchpatch)
BuildRequires:  golang(github.com/spf13/afero)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/viper)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/twpayne/go-pinentry)
BuildRequires:  golang(github.com/twpayne/go-shell)
BuildRequires:  golang(github.com/twpayne/go-vfs)
BuildRequires:  golang(github.com/twpayne/go-vfs/vfst)
BuildRequires:  golang(github.com/twpayne/go-xdg)
BuildRequires:  golang(github.com/ulikunitz/xz)
BuildRequires:  golang(github.com/zalando/go-keyring)
BuildRequires:  golang(go.etcd.io/bbolt)
BuildRequires:  golang(go.uber.org/multierr)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/term)
BuildRequires:  golang(gopkg.in/yaml.v3)
BuildRequires:  golang(howett.net/plist)
BuildRequires:  golang(mvdan.cc/sh/v3/expand)
BuildRequires:  golang(mvdan.cc/sh/v3/syntax)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/muesli/combinator)
BuildRequires:  golang(github.com/rs/zerolog/pkgerrors)
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

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
* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 2.16.0-4
- Fix go-github dependency

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 2.16.0-3
- Correct some go dependencies

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 2.16.0-2
- Add manual BuildRequires

* Sun May 22 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 2.16.0-1
- Initial package
