# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/muesli/combinator
%global goipath         github.com/muesli/combinator
Version:                0.3.0

%gometa

%global common_description %{expand:
Generates a slice of all possible value combinations for any given struct and a
set of its potential member values.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Generates a slice of all possible value combinations for any given struct and a set of its potential member values

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

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 0.3.0-1
- Initial package
