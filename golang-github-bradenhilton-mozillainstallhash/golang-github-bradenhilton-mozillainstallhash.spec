# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/bradenhilton/mozillainstallhash
%global goipath         github.com/bradenhilton/mozillainstallhash
Version:                1.0.0

%gometa

%global common_description %{expand:
Go package which generates the hash used to differentiate between installs of
Mozilla software.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go package which generates the hash used to differentiate between installs of Mozilla software

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
* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 1.0.0-1
- Initial package
