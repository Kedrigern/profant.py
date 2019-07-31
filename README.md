# profant.py

Přepiš webu [profant.eu](https://www.profant.eu) z původního [Jekyllu](https://jekyllrb.com/) do [Lektoru](https://www.getlektor.com/).

Jekyll je nejspíše nejrozšířenější generátor statických stránek. Nese sebou však těžké břímě minulosti v podobě některých principů (velmi rozvolněný datový model) a komplikovanosti rozšiřování. Též je napsán v Ruby, což není můj oblíbený jazyk. Velmi často se setkávám s balíčky, které mají dependency hell apod.

Lektor je nový a moderní projekt napsaný v Pythonu 3. Poučil se z chyb předchozích projektů. Připravoval ho jeden z autorů Flasku.

## Roadmap

- [X] **základní struktura**: menu, statické stránky (bez plného obsahy)
  - [X] hlavní menu
  - [X] statické stránky (bez plného obsahu)
- [X] **blog post**: (neobsahuje migrace starého obsahy)
  - [X] struktura článku se všemi metadaty apod.
  - [X] perex ve výpisu, [plugin](https://github.com/Andrew-Shay/lektor-read-full-post)
  - [X] obrázek ve výpisu
- [ ] **styly a skripty**:
  - [ ] [Webpack 4](https://www.getlektor.com/docs/guides/webpack/) (návod je však pro starší verze webpack)
  - [ ] [Foundation 6](https://foundation.zurb.com/)
  - [ ] Custom styly / SASS ([tutorial pro webpack](https://dev.to/pixelgoo/how-to-configure-webpack-from-scratch-for-a-basic-website-46a5))
  - [ ] Javascript
  - [ ] Aktualizace stylů (stažení nových verzí)
- [ ] **statické stránky**: doladění obsahu
- [ ] **migrace blog postů**
  - [ ] Texty
  - [ ] Přílohy
- [ ] **RSS/Atom**
- [ ] **seo**:
  - [ ] ulrs (same or permanent redirect)
  - [ ] sitemap
  - [ ] keywords
  - [ ] twitter sharing
  - [ ] FB sharing
- [ ] **travis**: CI, deployemnt
