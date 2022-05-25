# Generated by go2rpm 1.6.0
%bcond_with check
%global debug_package %{nil}

# https://github.com/go-git/go-billy
%global goipath         github.com/go-git/go-billy
Version:                5.3.1

%gometa

%global common_description %{expand:
The missing interface filesystem abstraction for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        The missing interface filesystem abstraction for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

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
* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 5.3.1-2
- Disable checks

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 5.3.1-1
- Initial package
