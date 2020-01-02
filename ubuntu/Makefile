name=deephdc-release
prefix=/

# needed dirs
debbuild_dir=$(shell pwd)/debbuild
deb_version=2.0.0
deb_age=1
here=$(shell pwd)

.PHONY: clean install deb

all: deb

####################################################################
# Install
####################################################################

install:
	@echo installing ...
	@mkdir -p $(prefix)/etc
	@mkdir -p $(prefix)/etc/apt
	@mkdir -p $(prefix)/etc/apt/sources.list.d
	@mkdir -p $(prefix)/etc/apt/preferences.d
	@install -m 0644 etc/deep-hdc-release $(prefix)/etc
	@install -m 0644 etc/apt/sources.list.d/deep-2.list $(prefix)/etc/apt/sources.list.d
	@install -m 0644 etc/apt/preferences.d/deep-2 $(prefix)/etc/apt/preferences.d

###########################################################$(DESTDIR)#########
# Build Distribution
####################################################################

DISTFILES=etc debian

srcdist:
	mkdir -p $(here)/$(name)-$(deb_version)
	@cp -a $(DISTFILES) $(here)/$(name)-$(deb_version)
	cd $(here) && tar cvz --exclude='*.github*' -f $(name)_$(deb_version).orig.tar.gz $(name)-$(deb_version)/*
	@rm -rf $(name)-$(deb_version)

prepare-debbuilddir: srcdist
	@mkdir -p $(debbuild_dir)
	@cp $(name)_$(deb_version).orig.tar.gz $(debbuild_dir)/$(name)_$(deb_version).orig.tar.gz
	@cd $(debbuild_dir) && tar xzvf $(name)_$(deb_version).orig.tar.gz
	@echo "done"

deb-src: prepare-debbuilddir
	ls -l $(debbuild_dir)
	cd $(debbuild_dir)
	strace dpkg-source -b $(name)-$(deb_version)

deb: deb-src
	cd $(debbuild_dir)/$(name)-$(deb_version) && debuild -us -uc

clean:
	@rm -rf $(name)_$(deb_version).orig.tar.gz $(debbuild_dir)
