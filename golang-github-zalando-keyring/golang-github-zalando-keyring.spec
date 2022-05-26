# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/zalando/go-keyring
%global goipath         github.com/zalando/go-keyring
Version:                0.2.1

%gometa

%global common_description %{expand:
Cross-platform keyring interface for Go.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md SECURITY.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Cross-platform keyring interface for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  dbus-x11
BuildRequires:  gnome-keyring
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Thu May 26 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 0.2.1-5
- Revise tests BuildRequires

* Thu May 26 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 0.2.1-4
- Change dbus test dependency

* Thu May 26 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 0.2.1-3
- Fix dbus package name

* Thu May 26 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 0.2.1-2
- Add dbus to BuildRequires

* Thu May 26 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 0.2.1-1
- Initial package
