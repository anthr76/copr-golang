# Generated by go2rpm 1.8.0
%bcond_without check

# https://github.com/google/gnostic
%global goipath         github.com/google/gnostic
Version:                0.6.9

%gometa

%global common_description %{expand:
A compiler for APIs described by the OpenAPI Specification with plugins for
code generation and other API support tasks.}

%global golicenses     LICENSE
%global godocs          examples CONTRIBUTING.md README.md\\\
                        cmd/disco/README.md cmd/petstore-builder/README.md\\\
                        examples cmd/protoc-gen-jsonschema/README.md examples\\\
                        cmd/protoc-gen-openapi/README.md cmd/report-\\\
                        messages/README.md cmd/report/README.md\\\
                        cmd/vocabulary-operations/README.md\\\
                        compiler/README.md discovery/README.md\\\
                        extensions/README.md generate-gnostic/README.md\\\
                        jsonschema/README.md jsonwriter/README.md\\\
                        linters/README.md linters/go/gnostic-lint-\\\
                        descriptions/README.md linters/go/gnostic-lint-\\\
                        paths/README.md linters/node/gnostic-lint-\\\
                        operations/README.md linters/node/gnostic-lint-\\\
                        responses/README.md openapiv2/README.md\\\
                        openapiv3/README.md openapiv3/schema-\\\
                        generator/3.0.0.md openapiv3/schema-\\\
                        generator/3.0.1.md openapiv3/schema-\\\
                        generator/3.0.2.md openapiv3/schema-\\\
                        generator/3.1.0.md openapiv3/schema-\\\
                        generator/README.md plugins/README.md\\\
                        plugins/gnostic-analyze/README.md plugins/gnostic-\\\
                        complexity/README.md plugins/gnostic-\\\
                        summary/README.md printer/README.md surface/README.md\\\
                        tools/README.md
%global godevelheader   %{expand:
Obsoletes:              golang-github-googleapis-gnostic < 0.5.3-9
}

Name:           %{goname}
Release:        %autorelease
Summary:        A compiler for APIs described by the OpenAPI Specification with plugins for code generation and other API support tasks

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg
%prep
%goprep
 

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%gobuild -o %{gobuilddir}/bin/gnostic %{goipath}
for cmd in plugins/gnostic-process-plugin-response linters/go/gnostic-lint-paths plugins/gnostic-linter linters/go/gnostic-lint-descriptions tools/format-schema plugins/gnostic-analyze generate-gnostic plugins/gnostic-analyze/summarize plugins/gnostic-complexity plugins/gnostic-vocabulary tools/j2y2j plugins/gnostic-plugin-request plugins/gnostic-summary jsonschema openapiv3/schema-generator; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
 
%if %{with check}
%check
# Needs network
%gocheck -d . \
         -d apps/protoc-gen-openapi	\
         -d generate-gnostic \
         -d compiler \
         -d extensions \
         -d plugins \
         -d plugins/gnostic-complexity \
         -d plugins/gnostic-vocabulary
%endif
 
%files
%license LICENSE
%doc examples CONTRIBUTING.md README.md cmd/disco/README.md
%doc cmd/petstore-builder/README.md examples cmd/protoc-gen-jsonschema/README.md
%doc examples cmd/protoc-gen-openapi/README.md cmd/report-messages/README.md
%doc cmd/report/README.md cmd/vocabulary-operations/README.md compiler/README.md
%doc discovery/README.md extensions/README.md generate-gnostic/README.md
%doc jsonschema/README.md jsonwriter/README.md linters/README.md
%doc linters/go/gnostic-lint-descriptions/README.md
%doc linters/go/gnostic-lint-paths/README.md
%doc linters/node/gnostic-lint-operations/README.md
%doc linters/node/gnostic-lint-responses/README.md openapiv2/README.md
%doc openapiv3/README.md openapiv3/schema-generator/3.0.0.md
%doc openapiv3/schema-generator/3.0.1.md openapiv3/schema-generator/3.0.2.md
%doc openapiv3/schema-generator/3.1.0.md openapiv3/schema-generator/README.md
%doc plugins/README.md plugins/gnostic-analyze/README.md
%doc plugins/gnostic-complexity/README.md plugins/gnostic-summary/README.md
%doc printer/README.md surface/README.md tools/README.md
%{_bindir}/*
 
%gopkgfiles

%changelog
%autochangelog
