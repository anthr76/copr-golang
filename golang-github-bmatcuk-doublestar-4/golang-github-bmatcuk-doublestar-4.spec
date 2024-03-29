# Generated by go2rpm 1.8.2
%bcond_without check
%global debug_package %{nil}

# https://github.com/bmatcuk/doublestar
%global goipath         github.com/bmatcuk/doublestar/v4
Version:                4.2.0

%gometa -f

%global common_description %{expand:
Implements support for double star (**) matches in golang's path.Match and
filepath.Glob.}

%global golicenses      LICENSE
%global godocs          examples README.md UPGRADING.md

Name:           %{goname}
Release:        %{autorelease}
Summary:        Implements support for double star (**) matches in golang's path.Match and filepath.Glob

License:        MIT
URL:            %{gourl}
Source:        %{gosource}

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
%autochangelog
