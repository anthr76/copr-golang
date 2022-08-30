# Generated by go2rpm 1.8.0
%bcond_without check

# https://github.com/sachaos/viddy
%global goipath         github.com/sachaos/viddy
%global goname          viddy
Version:                0.3.6

%gometa

%global common_description %{expand:
👀 A modern watch command. Time machine and pager etc.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        A modern watch command. Time machine and pager etc

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/viddy %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog