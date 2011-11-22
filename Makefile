PACKAGE = jebudo-fonts
VERSION = 0.1.0

srcdir = src
builddir = build
scriptsdir = scripts
distdir = dist
testsdir = tests

PYTHON = python

SFD := $(wildcard $(srcdir)/*.sfd)
TTF := $(patsubst $(srcdir)/%.sfd, $(builddir)/%.ttf, $(SFD))

TTFDIST := jebudo-ttf-$(VERSION)
TTFDISTFILE = $(TTFDIST).tar.bz2
EXTRA_TTF = LICENSE README

GENERATECMD = $(PYTHON) $(scriptsdir)/generate.py

TESTS := $(wildcard $(testsdir)/test-*.py)


.PHONY: all build clean dist test

all: build

build: $(TTF)

dist: $(distdir)/$(TTFDISTFILE)

test:
	@for S in $(SFD); do for T in $(TESTS); do \
	  echo $$T $$S; $(PYTHON) $$T $$S || exit 1; done done

$(builddir)/%.ttf: $(srcdir)/%.sfd
	@install -d $(dir $@)
	$(GENERATECMD) $< $@

$(distdir)/$(TTFDISTFILE): build
	@install -d $(distdir)/$(TTFDIST)
	for T in $(TTF); do install -m644 $$T $(distdir)/$(TTFDIST)/; done
	install -m644 $(EXTRA_TTF) $(distdir)/$(TTFDIST)/
	(cd $(distdir); tar jcvf $(TTFDISTFILE) $(TTFDIST))

clean:
	rm -f -r $(builddir)
	rm -f -r $(distdir)
