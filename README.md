# profant.py

Přepiš webu [profant.eu](https://www.profant.eu) z původního [Jekyllu](https://jekyllrb.com/) do [Lektoru](https://www.getlektor.com/).

Jekyll je nejspíše nejrozšířenější generátor statických stránek. Nese sebou však těžké břímě minulosti v podobě některých principů (velmi rozvolněný datový model) a komplikovanosti rozšiřování. Též je napsán v Ruby, což není můj oblíbený jazyk. Velmi často se setkávám s balíčky, které mají dependency hell apod.

Lektor je nový a moderní projekt napsaný v Pythonu 3. Poučil se z chyb předchozích projektů. Připravoval ho jeden z autorů Flasku.

## Run

`lektor server -f webpack`

## Roadmap

- [X] **základní struktura**: menu, statické stránky (bez plného obsahy)
  - [X] hlavní menu: [4a7a4ba](https://github.com/Kedrigern/profant.py/commit/4a7a4ba9995e3f261b53059277711c318a02472f)
  - [X] statické stránky (bez plného obsahu)
- [X] **blog post**: (neobsahuje migrace starého obsahy)
  - [X] struktura článku se všemi metadaty apod.
  - [X] perex ve výpisu, [plugin](https://github.com/Andrew-Shay/lektor-read-full-post)
  - [X] obrázek ve výpisu
  - [X] [kategorie](https://www.getlektor.com/docs/guides/categories/) [a72f43e](https://github.com/Kedrigern/profant.py/commit/a72f43e613a6b02d02e48596fa2b162ced645e85)
- [X] **styly a skripty**: [4380f8a](https://github.com/Kedrigern/profant.py/commit/4380f8a152233da8a92db825f5edd513e01f7aaa)
  - [X] [Webpack 4](https://www.getlektor.com/docs/guides/webpack/) (návod je však pro starší verze webpack): cc88fd164cc56f047dad8c75a22bac26fdd1dadf
  - [X] [Foundation 6](https://foundation.zurb.com/) 
  - [X] Custom styly / SASS ([tutorial pro webpack](https://dev.to/pixelgoo/how-to-configure-webpack-from-scratch-for-a-basic-website-46a5))
  - [X] Javascript: [tutorial](https://github.com/pelamfi/zurb-foundation-scss-webpack-example)
  - [X] Aktualizace stylů (stažení nových verzí)
- [X] **statické stránky**: doladění obsahu
  - [X] formát datumu
- [ ] **migrace blog postů**
  - [ ] Texty
  - [ ] Přílohy
- [X] **RSS/Atom**: [návod](https://www.getlektor.com/plugins/lektor-atom/): [0b6228c](https://github.com/Kedrigern/profant.py/commit/0b6228cc31d9a8eca101dc4bc9618a021de43408)
- [ ] **seo**:
  - [ ] urls (same or permanent redirect), [question in discusion](https://www.getlektor.com/docs/guides/blog/), [stack overflow](https://stackoverflow.com/questions/44972297/changing-the-url-structure-of-lektor-for-blog-posts-to-be-in-the-parent-director)
  - [X] [sitemap](https://www.getlektor.com/docs/guides/sitemap/): [ac73c41](https://github.com/Kedrigern/profant.py/commit/ac73c41d5564b44d5464145a93848eee314e4e12)
  - [ ] meta keywords
  - [ ] twitter sharing
  - [ ] FB sharing
- [ ] **Disqus**: [plugin](https://www.getlektor.com/plugins/lektor-disqus-comments/)
- [ ] **travis**: CI, deployemnt: [tutorial](https://www.getlektor.com/docs/deployment/travisci/)
- [ ] **custom plugin**: [návod](https://www.getlektor.com/docs/plugins/dev/)
