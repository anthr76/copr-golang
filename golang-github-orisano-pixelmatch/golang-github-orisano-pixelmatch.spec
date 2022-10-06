# golang-github-orisano-pixelmatch.spec
# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/orisano/pixelmatch
%global goipath         github.com/orisano/pixelmatch
%global commit          fb0b55479cde89fd42234927a9e27786d459dd89

%gometa -f

%global common_description %{expand:
Mapbox/pixelmatch ports for go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Mapbox/pixelmatch ports for go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep
# Binary is not known to be useful.
# Open a RHBZ if it's needed
rm -r cmd/pixelmatch

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

