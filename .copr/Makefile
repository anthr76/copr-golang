# Bundler Makefile

spec:= $(topdir)/$(shell basename *.spec)
BASENAME:= $(shell rpmspec -q --srpm --qf "%{name}-%{version}" $(spec))
NAME:= $(shell rpmspec -q --srpm --qf "%{name}" $(spec))
VERSION:= $(shell rpmspec -q --srpm --qf "%{version}" $(spec))
outdir:= $(topdir)

# Check deps
KUSTOMIZE := $(shell command -v kustomize 2> /dev/null)
GO := $(shell command -v go 2> /dev/null)

srpm:
ifndef GO
	dnf install go -y
endif
ifeq ($(spec),flux2/flux2.spec)
	make -f .copr/Makefile flux outdir=$(outdir) spec=$(spec)
endif
	tar xf $(outdir)/$(BASENAME).tar.gz -C $(outdir)
	cd $(outdir)/$(BASENAME) && go mod vendor
	./generate_bundled_deps $(outdir)/$(BASENAME) > $(outdir)/bundled.inc
	cd $(outdir) && tar czf $(BASENAME)-vendored-deps.tar.gz $(BASENAME)/vendor
	rm -r $(outdir)/$(BASENAME)
	rpmbuild -bs --define "_sourcedir $(outdir)" --define "_srcrpmdir $(outdir)" $(spec)

flux:
ifndef KUSTOMIZE
	dnf install go -y
endif
	wget -O $(outdir)/flux2-$(VERSION).tar.gz https://github.com/fluxcd/flux2/archive/refs/tags/v$(VERSION).tar.gz
	make -f .copr/Makefile flux-manifests outdir=$(outdir) spec=$(spec)

flux-manifests:
	tar xf $(outdir)/$(BASENAME).tar.gz -C $(outdir)
	$(outdir)/$(BASENAME)/manifests/scripts/bundle.sh
	cd $(outdir) && tar czf $(BASENAME)-bundled-manifests.tar.gz $(BASENAME)/cmd/flux/manifests

