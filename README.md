# profant.py

Přepiš webu [profant.eu](https://www.profant.eu) z původního [Jekyllu](https://jekyllrb.com/) do [Lektoru](https://www.getlektor.com/).

Jekyll je nejspíše nejrozšířenější generátor statických stránek. Nese sebou však těžké břímě minulosti v podobě některých principů (velmi rozvolněný datový model) a komplikovanosti rozšiřování. Též je napsán v Ruby, což není můj oblíbený jazyk. Velmi často se setkávám s balíčky, které mají dependency hell apod.

Lektor je nový a moderní projekt napsaný v Pythonu. Poučil se z chyb předchozích projektů.

## Roadmap

- [X] **základní struktura**: menu, statické stránky (bez plného obsahy)
  - [X] menu
  - [X] statické stránky (bez plného obsahu)
- [ ] **blog post**: (neobsahuje migrace starého obsahy)
  - [X] struktura článku se všemi metadaty apod.
  - [ ] perex ve výpisu, [plugin](https://github.com/Andrew-Shay/lektor-read-full-post)
  - [ ] obrázek ve výpisu
- [ ] **styly a skripty**:
  - [ ] [Foundation](https://foundation.zurb.com/)
  - [ ] Custom styly
  - [ ] Javascript
  - [ ] Verzování stylů
- [ ] **statické stránky**: obsah
- [ ] **migrace blog postů**
  - [ ] Texty
  - [ ] Přílohy
- [ ] **RSS/Atom**
- [ ] **seo**:
  - [ ] sitemap
  - [ ] keywords
  - [ ] twitter sharing
  - [ ] FB sharing
- [ ] **travis**: CI, deployemnt
