PACKAGE = jebudo-fonts
VERSION = 0.1.0

srcdir = src
builddir = build
scriptsdir = scripts
distdir = dist
testsdir = tests

PYTHON = python
XGRIDFIT = xgridfit
GENERATECMD = $(PYTHON) $(scriptsdir)/generate.py

SFD := $(wildcard $(srcdir)/*.sfd)
TTF := $(patsubst $(srcdir)/%.sfd, $(builddir)/%.ttf, $(SFD))

TTFDIST := jebudo-ttf-$(VERSION)
TTFDISTFILE = $(TTFDIST).tar.bz2
EXTRA_TTF = LICENSE README

TESTS := $(wildcard $(testsdir)/test-*.py)


.PHONY: all build clean dist test merge-hinting

all: build

build: $(TTF)

dist: $(distdir)/$(TTFDISTFILE)

test:
	@for S in $(SFD); do for T in $(TESTS); do \
	  echo $$T $$S; $(PYTHON) $$T $$S || exit 1; done done

$(builddir)/%.ttf: $(srcdir)/%.sfd
	@install -d $(dir $@)
	$(GENERATECMD) $< $@

merge-hinting:
	@for S in $(SFD); do \
	  xgf=`dirname $$S`/hintings/`basename $$S | sed -e 's/sfd$$/xgf/'`; \
	  tmp=`dirname $$S`/hintings/`basename $$S`.new.sfd; \
	  echo "$$S: merging hintings..."; \
	  $(XGRIDFIT) -m -f -i $$S -o $$tmp $$xgf && mv $$tmp $$S; \
	done

$(distdir)/$(TTFDISTFILE): build
	@install -d $(distdir)/$(TTFDIST)
	for T in $(TTF); do install -m644 $$T $(distdir)/$(TTFDIST)/; done
	install -m644 $(EXTRA_TTF) $(distdir)/$(TTFDIST)/
	(cd $(distdir); tar jcvf $(TTFDISTFILE) $(TTFDIST))

clean:
	rm -f -r $(builddir)
	rm -f -r $(distdir)
