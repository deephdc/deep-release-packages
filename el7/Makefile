NAME= $(shell grep Name: *.spec | sed 's/^[^:]*:[^a-zA-Z]*//' )
VERSION= $(shell grep Version: *.spec | sed 's/^[^:]*:[^0-9]*//' )
RELEASE= $(shell grep Release: *.spec |cut -d"%" -f1 |sed 's/^[^:]*:[^0-9]*//')
build=$(shell pwd)/build
DATE=$(shell date "+%a, %d %b %Y %T %z")
dist=$(shell rpm --eval '%dist' | sed 's/%dist/.el6/')

default: 
	@echo "Nothing to do"

install:
	@echo installing ...
	@mkdir -p $(prefix)/etc
	@mkdir -p $(prefix)/etc/yum.repos.d
	@mkdir -p $(prefix)/etc/pki
	@mkdir -p $(prefix)/etc/pki/rpm-gpg
	@install -m 0644 etc/deep-hdc-release $(prefix)/etc
	@install -m 0644 etc/yum.repos.d/deep-1-base.repo $(prefix)/etc/yum.repos.d
	@install -m 0644 etc/yum.repos.d/deep-1-updates.repo $(prefix)/etc/yum.repos.d
	@install -m 0644 etc/yum.repos.d/deep-1-third-party.repo $(prefix)/etc/yum.repos.d
	@install -m 0644 etc/pki/rpm-gpg/RPM-GPG-KEY-indigodc $(prefix)/etc/pki/rpm-gpg

dist:
	@mkdir -p  $(build)/$(NAME)-$(VERSION)/
	rsync -HaS --exclude ".git" --exclude "$(build)" * $(build)/$(NAME)-$(VERSION)/
	cd $(build); tar --gzip -cf $(NAME)-$(VERSION).src.tgz $(NAME)-$(VERSION)/; cd -

sources: dist
	cp $(build)/$(NAME)-$(VERSION).src.tgz .

prepare: dist
	@mkdir -p  $(build)/RPMS/noarch
	@mkdir -p  $(build)/SRPMS/
	@mkdir -p  $(build)/SPECS/
	@mkdir -p  $(build)/SOURCES/
	@mkdir -p  $(build)/BUILD/
	cp $(build)/$(NAME)-$(VERSION).src.tgz $(build)/SOURCES

srpm: prepare
	@rpmbuild -bs --define="dist ${dist}" --define='_topdir ${build}' $(NAME).spec 

rpm: srpm
	@rpmbuild --rebuild  --define="dist ${dist}" --define='_topdir ${build} ' $(build)/SRPMS/$(NAME)-$(VERSION)-$(RELEASE)${dist}.src.rpm 

clean:
	rm -f *~ $(NAME)-$(VERSION).src.tgz
	rm -rf $(build)

.PHONY: dist srpm rpm sources clean
