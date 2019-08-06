# profant.py

Přepiš webu [profant.eu](https://www.profant.eu) z původního [Jekyllu](https://jekyllrb.com/) do [Lektoru](https://www.getlektor.com/).

Jekyll je nejspíše nejrozšířenější generátor statických stránek. Nese sebou však těžké břímě minulosti v podobě některých principů (velmi rozvolněný datový model) a komplikovanosti rozšiřování. Též je napsán v Ruby, což není můj oblíbený jazyk. Velmi často se setkávám s balíčky, které mají dependency hell apod.

Lektor je nový a moderní projekt napsaný v Pythonu 3. Poučil se z chyb předchozích projektů. Připravoval ho jeden z autorů Flasku.

## Run

`lektor server -f webpack`

## Roadmap

- [X] **základní struktura**: menu, statické stránky (bez plného obsahy)
  - [X] hlavní menu
  - [X] statické stránky (bez plného obsahu)
- [ ] **blog post**: (neobsahuje migrace starého obsahy)
  - [X] struktura článku se všemi metadaty apod.
  - [X] perex ve výpisu, [plugin](https://github.com/Andrew-Shay/lektor-read-full-post)
  - [X] obrázek ve výpisu
  - [ ] [kategorie](https://www.getlektor.com/docs/guides/categories/)
- [ ] **styly a skripty**:
  - [X] [Webpack 4](https://www.getlektor.com/docs/guides/webpack/) (návod je však pro starší verze webpack)
  - [X] [Foundation 6](https://foundation.zurb.com/)
  - [X] Custom styly / SASS ([tutorial pro webpack](https://dev.to/pixelgoo/how-to-configure-webpack-from-scratch-for-a-basic-website-46a5))
  - [ ] Javascript
  - [X] Aktualizace stylů (stažení nových verzí)
- [ ] **statické stránky**: doladění obsahu
  - [ ] formát datumu
- [ ] **migrace blog postů**
  - [ ] Texty
  - [ ] Přílohy
- [ ] **RSS/Atom**
- [ ] **seo**:
  - [ ] urls (same or permanent redirect), [question in discusion](https://www.getlektor.com/docs/guides/blog/)
  - [ ] [sitemap](https://www.getlektor.com/docs/guides/sitemap/)
  - [ ] meta keywords
  - [ ] twitter sharing
  - [ ] FB sharing
- [ ] **Disqus**: [plugin](https://www.getlektor.com/plugins/lektor-disqus-comments/)
- [ ] **travis**: CI, deployemnt
- [ ] **custom plugin**: [návod](https://www.getlektor.com/docs/plugins/dev/)
