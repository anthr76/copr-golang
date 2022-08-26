# kubecolor.spec
# Generated by go2rpm 1.6.0
%bcond_without check

# https://github.com/hidetatz/kubecolor
%global goipath         github.com/hidetatz/kubecolor
%global commit          828af61cd8a55c052fb42c755d734c856a775af2

%gometa

%global goname kubecolor

%global common_description %{expand:
Colorizes kubectl output.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p -b 3
Summary:        Colorizes kubectl output

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

Requires: kubernetes-client

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

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

