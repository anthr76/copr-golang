spec = $(topdir)/$(shell basename *.spec)
BASENAME:= $(shell rpmspec -q --srpm --qf "%{name}-%{version}" $(spec))
VERSION:= $(shell rpmspec -q --srpm --qf "%{version}" $(spec))
outdir:= $(topdir)

KUSTOMIZE := $(shell command -v kustomize 2> /dev/null)
GO := $(shell command -v go 2> /dev/null) 

srpm:
ifndef KUSTOMIZE
	dnf install golang-sigs-k8s-kustomize -y
endif
ifndef GO
	dnf install go -y
endif
		wget -O flux2-$(VERSION).tar.gz https://github.com/fluxcd/flux2/archive/refs/tags/v$(VERSION).tar.gz
		tar xf $(BASENAME).tar.gz
		cd $(BASENAME) && go mod vendor
		../generate_bundled_deps $(BASENAME) > bundled.inc
		tar czf $(BASENAME)-vendored-deps.tar.gz $(BASENAME)/vendor
		./$(BASENAME)/manifests/scripts/bundle.sh
		tar czf $(BASENAME)-bundled-manifests.tar.gz $(BASENAME)/cmd/flux/manifests/
		rm -r $(BASENAME)
		rpmbuild -bs --define "_sourcedir $(outdir)" --define "_srcrpmdir $(outdir)" $(spec)

