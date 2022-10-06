# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/twpayne/go-xdg
%global goipath         github.com/twpayne/go-xdg/v6
Version:                6.0.0

%gometa -f

%global common_description %{expand:
Package xdg provides support for the XDG Base Directory Specification.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Package xdg provides support for the XDG Base Directory Specification

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

Patch:          0001-update-go-vfs.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%autopatch -p 1

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
