# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [4.0.1b]

### Added

- option to point to local reference files to the genome viewer pileup.js. Documented in `docs.admin-guide.server`

## [4.0.0]

### WARNING ###

This is a major version update and will require that the backend of pre releases is updated.
Run commands:

```
$scout update genes
$scout update hpo
```

- Created a Clinvar submission tool, to speed up Clinvar submission of SNVs and SVs
- Added an analysis report page (html and PDF format) containing phenotype, gene panels and variants that are relevant to solve a case.

### Fixed

- Adapts clinvar parsing to new format
- Fixed problem in `scout update user` when the user object had no roles
- Makes pileup.js use online genome resources when viewing alignments. Now any instance of Scout can make use of this functionality.
- Fix ensembl link for structural variants
- Works even when cases does not have `'madeline_info'`
- Parses Polyphen in correct way again

### Added

- Filter for spidex scores
- All HPO terms are now added and fetched from the correct source (https://github.com/obophenotype/human-phenotype-ontology/blob/master/hp.obo)
- New command `scout update hpo`
- New command `scout update genes` will fetch all the latest information about genes and update them
- Load **all** variants found on chromosome **MT**
- Adds choice in cases overview do show as many cases as user like

### Removed

- All source files for HPO information, this is instead fetched directly from source
- All source files for gene information, this is instead fetched directly from source

## [3.0.0]
### Fixed
- hide pedigree panel unless it exists

## [1.5.1] - 2016-07-27
### Fixed
- look for both ".bam.bai" and ".bai" extensions

## [1.4.0] - 2016-03-22
### Added
- support for local frequency through loqusdb
- bunch of other stuff

## [1.3.0] - 2016-02-19
### Fixed
- Update query-phenomizer and add username/password

### Changed
- Update the way a case is checked for rerun-status

### Added
- Add new button to mark a case as "checked"
- Link to clinical variants _without_ 1000G annotation

## [1.2.2] - 2016-02-18
### Fixed
- avoid filtering out variants lacking ExAC and 1000G annotations

## [1.1.3] - 2015-10-01
### Fixed
- persist (clinical) filter when clicking load more
- fix #154 by robustly setting clinical filter func. terms

## [1.1.2] - 2015-09-07
### Fixed
- avoid replacing coverage report with none
- update SO terms, refactored

## [1.1.1] - 2015-08-20
### Fixed
- fetch case based on collaborator status (not owner)

## [1.1.0] - 2015-05-29
### Added
- link(s) to SNPedia based on RS-numbers
- new Jinja filter to "humanize" decimal numbers
- show gene panels in variant view
- new Jinja filter for decoding URL encoding
- add indicator to variants in list that have comments
- add variant number threshold and rank score threshold to load function
- add event methods to mongo adapter
- add tests for models
- show badge "old" if comment was written for a previous analysis

### Changed
- show cDNA change in transcript summary unless variant is exonic
- moved compounds table further up the page
- show dates for case uploads in ISO format
- moved variant comments higher up on page
- updated documentation for pages
- read in coverage report as blob in database and serve directly
- change ``OmimPhenotype`` to ``PhenotypeTerm``
- reorganize models sub-package
- move events (and comments) to separate collection
- only display prev/next links for the research list
- include variant type in breadcrumbs e.g. "Clinical variants"

### Removed
- drop dependency on moment.js

### Fixed
- show the same level of detail for all frequencies on all pages
- properly decode URL encoded symbols in amino acid/cDNA change strings
- fixed issue with wipe permissions in MongoDB
- include default gene lists in "variants" link in breadcrumbs

## [1.0.2] - 2015-05-20
### Changed
- update case fetching function

### Fixed
- handle multiple cases with same id

## [1.0.1] - 2015-04-28
### Fixed
- Fix building URL parameters in cases list Vue component

## [1.0.0] - 2015-04-12
Codename: Sara Lund

![Release 1.0](artwork/releases/release-1-0.jpg)

### Added
- Add email logging for unexpected errors
- New command line tool for deleting case

### Changed
- Much improved logging overall
- Updated documentation/usage guide
- Removed non-working IGV link

### Fixed
- Show sample display name in GT call
- Various small bug fixes
- Make it easier to hover over popups

## [0.0.2-rc1] - 2015-03-04
### Added
- add protein table for each variant
- add many more external links
- add coverage reports as PDFs

### Changed
- incorporate user feedback updates
- big refactor of load scripts

## [0.0.2-rc2] - 2015-03-04
### Changes
- add gene table with gene description
- reorganize inheritance models box

### Fixed
- avoid overwriting gene list on "research" load
- fix various bugs in external links

## [0.0.2-rc3] - 2015-03-05
### Added
- Activity log feed to variant view
- Adds protein change strings to ODM and Sanger email

### Changed
- Extract activity log component to macro

### Fixes
- Make Ensembl transcript links use archive website
