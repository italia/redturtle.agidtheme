Changelog
=========


4.0.0 (unreleased)
------------------

- Cambiata sottolineatura dei link nel testo e nelle tile e portlet di testo
  [pnicolli]


3.3.3 (2019-06-26)
------------------

- Fix relateditems viewlet customization. Now handle empty relations.
  [cekk]
- Fix tiles_page_view condition for text field.
  [cekk]

3.3.2 (2019-06-03)
------------------

- Fix tile collection carousel dots [nzambello]


3.3.1 (2019-03-28)
------------------

- Fix per l'override della tiles_view [pnicolli]
- Fix media query in stili toolbar [pnicolli]


3.3.0 (2019-03-12)
------------------

- Aggiunta email alle opzioni di condivisione [pnicolli]
- Rimosso Google+ dalle opzioni di condivisione [pnicolli]
- Fix search backdrop z-index [nzambello][pnicolli]
- Backport bootstrap 4 container concept [pnicolli]
- Aggiunto rendering server-side delle tiles per utenti anonimi [pnicolli]


3.2.0 (2019-01-28)
------------------

- Sovrascritta label errore portalMessage [nzambello]
- Browserlist: Updated iOS (Safari) version from 6+ to 9+ [nzambello]
- Imported events styles from old plone.app.event resource [nzambello]
- Minor fixes for events [nzambello]


3.1.1 (2019-01-22)
------------------

- Fixed a bug within diazo rules [nzambello]


3.1.0 (2019-01-09)
------------------

- a11y: added role attribute for portal message with diazo [nzambello]
- Fixed contact-info view styles [nzambello]


Compatibility with Plone 5.1.4:

- Updated styles for pagination, improved accessibility and responsiveness [nzambello]
- `plone-logged-in` override is registered only if Plone version is < 5.1.4
  [cekk]


3.0.10 (2018-12-20)
-------------------

- Added publiccode.yml [nzambello]
- a11y: fixed contrast in alerts/messages, WCAG 2 AAA compliant [nzambello]
- Breadcrumbs styles are now less specific in order to allow breadcrumbs viewlet to be moved in another manager
  [pnicolli]


3.0.9 (2018-11-08)
------------------

- Add personal-information link in header viewlet when an user is logged.
  [cekk]


3.0.8 (2018-10-18)
------------------

- Removed target="_blank" from header banner links [nzambello]


3.0.7 (2018-10-11)
------------------

- Added 'big' scale in allowed_sizes, used in leadimage viewlet [fdelia]
- Enhancing styles for default Plone search page [nzambello]


3.0.6 (2018-09-27)
------------------

- Fixed svg mimetypes icons dimensions [nzambello]


3.0.5 (2018-09-20)
------------------

- A11y: added `alt` attribute to `img` in tile collections where missing [nzambello]


3.0.4 (2018-09-13)
------------------

- Added selector for mimetypes icons [nzambello]


3.0.3 (2018-09-13)
------------------

- Fixed selector for mimetypes icons [nzambello]


3.0.2 (2018-09-13)
------------------

- Added selector for mimetypes icons [nzambello]


3.0.1 (2018-09-13)
------------------

- Updated styles for new tiles management UI (https://github.com/RedTurtle/redturtle.tiles.management/pull/12) [nzambello]
- Added login button in header banner viewlet shown if an option in controlpanel is selected [nzambello]
- Used <h2> for tile titles and extended those styles for h2 [nzambello]
- Changed styles for leadimage [nzambello]
- Added social icons for footer [nzambello]


3.0.0 (2018-08-06)
------------------

BREAKING CHANGES:

- Changed package name from redturtle.agidtheme to design.plone.theme to adhere to the standards of github.com/italia [nzambello]
    - Removed old upgrade steps
    - Removed old profiles

Other changes:

- Fix uninstall step [cekk]
- Update of the "font_size_base" variable [fdelia]
- Added an override of plone-logged-in js resource to fix toolbar pattern [nzambello]


2.2.2 (2018-07-05)
------------------

- Improved translation for header social viewlet
  [eikichi18]


2.2.1 (2018-07-03)
------------------

- Improved translation for share button on social_viewlet
  [eikichi18]
- Fix missing title formatting for linkedin social share links
  [cekk]
- Changed menù behavior for mobile devices. It's now positioned off canvas on the right. [pnicolli]


2.2.0 (2018-06-14)
------------------

- Styles for empty tile collections [nzambello]
- Fix flexbox styles for header [nzambello]
- Added multilingual viewlet [nzambello]
- Separated header in two viewlets: portal_header (default) and header_banner [nzambello]


2.1.4 (2018-05-31)
------------------

- Updated default profile name [pnicolli]
- Styles for table of contents [nzambello]


2.1.3 (2018-05-29)
------------------

- Fix pagination styles [nzambello]


2.1.2 (2018-05-28)
------------------

- Fix tile collection flexbox dimensions [nzambello]
- Fix bootstrap import (missing modules found) [nzambello]
- Fix comments styles in tile collections [nzambello]
- Styles for table of contents [nzambello]
- Fix user pic in comments [nzambello]


2.1.1 (2018-05-10)
------------------

- Remove unused defaults in controlpanel
  [cekk]


2.1.0 (2018-04-26)
------------------

- Fix tags for icons (for compatibility) [nzambello]
- Fixes for icons (separated js called with an event) [nzambello]
- Don't show header viewlet if settings aren't set. Now default settings are set
  at install-time.
  [cekk]
- Added comments styles from barceloneta [nzambello]
- Moved icons to a separated bundle [nzambello]
- Minor fixes for icons and js events [nzambello]


2.0.0 (2018-03-15)
------------------

Docs on this release: `docs`__.

BREAKING CHANGES:

- Moved JS resources to theme/ folder [nzambello]
- Migrated icons and styles to FontAwesome 5 (import via JS, added its classes to templates) [nzambello]
- Added prettier and made it run on the code [nzambello]

Minor changes:

- Updated package.json to reflect current addon version [pnicolli]
- Fixed collection tile renderers layers, they won't show up when this theme is not installed anymore [pnicolli]
- Evitato lo scroll della pagina quando il menu o la ricerca sono aperti [nzambello]
- Cambiato selettore per il tile manager per l'uso senza pattern [nzambello]
- Fix nell'ordine degli elementi nel controlpanel [nzambello]
- Documentate meglio alcune viste per le tile collections [nzambello]
- Cambiato metodo di scaling di plone.app.imaging da scale() a tag() [nzambello]
- Cambiate le occorrenze del font-weight 700 a 600 (è quello di cui si fa l'import nel font) [nzambello]


__ https://github.com/PloneGov-IT/redturtle.agidtheme/blob/master/docs/migrationTo2.rst

1.1.7 (2018-02-07)
------------------

- Fix list-style rules to allow an override [nzambello]


1.1.6 (2018-02-07)
------------------

- Fix list-style rules to allow an override [nzambello]
- Removed useless flex in header which had issues with Safari on iOS [nzambello]
- Fix show_more in sights-collection view [nzambello]


1.1.5 (2018-02-02)
------------------

- Fixed backend searchbox [pnicolli]
- Added clearfix for static tile bg [nzambello]
- Fix gallery collection icon [nzambello]
- 'senza-titolo' CSS class applied to any tile [nzambello]
- Changed grunt-postcss sourcemap settings [nzambello]


1.1.4 (2018-01-25)
------------------

- Added title border to navigation static tile [nzambello]
- Added icon for newsletter [nzambello]
- Removed collapse button for tiles from templates, styles and js [nzambello]
- Removed tiles_page_view for folder [fdelia]
- Changed newshome miniature [nzambello]


1.1.3 (2018-01-18)
------------------

- Fix problem with mobile menu wrongly dependent on social container
  This could fix also problem with close menu button: javascript in
  rer.agidtheme.base seems to work properly
  [lucabel]
- Aggiunti stili per tile statica "menu navigazione" [nzambello]


1.1.2 (2018-01-12)
------------------

- Fix upgrade-step
  [cekk]

1.1.1 (2018-01-12)
------------------

- Improve follow us links: now is a list field with more flexibility
  [cekk]


1.1.0 (2018-01-12)
------------------

- Fix sights_renderer template
  [cekk]
- Add customizable social links in header viewlet
  [cekk]


1.0.9 (2018-01-11)
------------------

- Minor fix for responsive styles [nzambello]
- Fix plone styles for site setup portlets list [nzambello]
- Updated ellipsed [nzambello]
- Fix list in collective.tiles.advancedstatic.css_styles [fdelia]


1.0.8 (2018-01-05)
------------------

- Divided css and js resources and bundles for themes overriding


1.0.7 (2017-12-29)
------------------

- Added skiplinks [nzambello]
- Fix big photo tile container styles [nzambello]
- Added License and references to new repo [nzambello]


1.0.6 (2017-12-21)
------------------

- Fix redturtleagidtheme_rules.xml per inserire anche i tag <style> [cekk]
- Fixed menu styles to avoid affecting possible submenus [pnicolli]
- Refactored tiles page stiles to be more flexible about the number of columns [pnicolli]
- Removed h1 from logo viewlet [pnicolli]
- Stili carousel [nzambello]
- Stili gallery [nzambello]
- Renamed aree-tematiche to aree-tematiche-collection to prevent conflicts with site contents ids [nzambello]
- Removed ellipsed from public resources [pnicolli]
- Info in README [nzambello]
- Removed unused landing-aree-tematiche view [nzambello]
- Three columns pages collection tile [nzambello]
- Fix stili tile sfondo scuro/chiaro [nzambello]
- Fix JS compile rules in registry [nzambello]
- Moved theme styles to resource registry [nzambello]


1.0.5 (2017-10-25)
------------------

- Corretti stili collezioni e tile [nzambello]
- Aggiunta icona Instagram [nzambello]
- Aggiunti alcuni fix responsive [fdelia]
- Aggiornato ellipsed [nzambello]


1.0.4 (2017-10-04)
------------------

- Corrette indicazioni accessibilita' [nzambello]


1.0.3 (2017-10-03)
------------------

- Aggiornamento ellipsed per problemi di compatibilita' [nzambello]
- Aggiunta vista per collezione video [nzambello]
- Aggiunta vista per collezione gallery (folders) [nzambello]
- Aggiunti stili responsive per header (+ ricerca e menu) [nzambello]
- Aggiunte indicazioni accessibilita [nzambello]


1.0.2 (2017-09-28)
------------------

- Aggiunte indicazioni per accessibilita' bottone chiusura menu [nzambello]
- Fix posizione date collezione news [nzambello]


1.0.1 (2017-09-18)
------------------

- Fix import di ellipsed nel bundle [nzambello]
- Aggiornamento versioni npm [nzambello]
- Stili tiles testo statico con classe CSS e non entry nel menu a tendina [nzambello]
- Icona chiusura modale plone piÃ¹ visibile [nzambello]


1.0.0 (2017-09-14)
------------------

- fix backend css url in diazo rules
  [mamico]
- Initial release.
  [RedTurtle]
