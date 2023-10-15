# FACILITIES-
Repositář pro projekt na ZS 2023/2024
# ZADÁNÍ
FACILITIES (2 studenti) Rout, Stacha

  Entity (FacilityGQLModel, FacilityTypeGQLModel)
  
  Entity (FacilityEventGQLModel, FacilityEventStateTypeGQLModel)
  
  Resolver FacilityBy3Letters
  
  Modely v databázi pomocí SQLAlchemy, API endpoint typu GraphQL s pomocí knihovny Strawberry.
  
  Přístup k databázi řešte důsledně přes AioDataloder, resp. (https://github.com/hrbolek/uoishelpers/blob/main/uoishelpers/dataloaders.py).
  
  Zabezpečte kompletní CRUD operace nad entitami ExternalIdModel, ExternalIdTypeModel, ExternalIdCategoryModel
  
  CUD operace jako návratový typ nejméně se třemi prvky id, msg a „entityresult“ (pojmenujte adekvátně podle dotčené entity), vhodné přidat možnost nadřízené entity, 
  speciálně   pro operaci D.
  
  Řešte autorizaci operací (permission classes).
  
  Kompletní CRUD dotazy na GQL v souboru externalids_queries.json (dictionary), jméno klíče nechť vhodně identifikuje operaci, hodnota je dictionary s klíči query (obsahuje       parametrický dotaz) nebo mutation (obsahuje parametrické mutation) a variables (obsahuje dictionary jako testovací hodnoty).
  
  Kompletní popisy API v kódu (description u GQLModelů) a popisy DB vrstvy (comment u DBModelů).
  
  Zabezpečte více jak 90% code test coverage (standard pytest).


# SPOLEČNÉ PODMÍNKY

SQL Alchemy pro SQL databázi

Všechny entity v DB budou mít položky createdby (kdo vytvořil), changedby (kdo změnil), created (kdy vytvořeno), lastchange (😊)

Strawberry pro GQL endpoint, federativní API, extenze neovlivňují primární definici, jsou definovány v samostatných třídách,

Všechny vektorové atributy mají volitelné skip, limit a where parametry (snad se podaří řešiteli úkolu 19 vytvořit podpůrný produkt 😊).

Přístup k DB striktně přes AIODataLoader (optimalizace přístupu k DB) (Všechny operace zprostředkované dataloadery).

Přístup k dataloaderům inicializován v kontextu, použijte cached property.

Vlastní repository na github.com

Není možné odstraňovat existující tabulky či atributy

Je možné přidat další tabulky či atributy po konzultaci

Alespoň 90 % test code coverage (pytest)

DB modely v samostatných souborech a ty ve společném adresáři (aka Python package)

GQL modely s queries a mutations v samostatných souborech a ty ve společném adresáři (aka Python package), doplnit modelem query a modelem mutation, 100% description

_queries.json - kompletní CRUD dotazy (příklady) na GQL v souboru json (dictionary), jméno klíče nechť vhodně identifikuje operaci, hodnota je dictionary s klíči query (obsahuje parametrický dotaz) nebo mutation (obsahuje parametrické mutation) a variables (obsahuje dictionary jako testovací hodnoty)

# Časový harmonogram:

9.10.2023 zveřejnění harmonogramu prací na projektu (z pohledu programátora), určení repository url (nebo alespoň root např. https://github.com/hrbolek)

16.10.2023 projektový den, Prezentace porozumění projektu, jeho struktura, deskripce entit („live dokumentace v GQL API – Voyager / GraphiQL“)

27.11.2023 projektový den, Prezentace alespoň RU operací

15.1.2024 projektový den, Alfa verze

21.1.2024 uzavření projektu

22.1.2024 počátek zkouškového období,

?.3.2024 konec zkouškového období.

# Rozvrh práce z pohledu programátorů 

9.10.2023 - Seznámení s knihovnamy, tvorba githubu, ujasnění zadání

16.10.2023 - Sepsání prvních entit(jen testovacích), zprovoznění nějaké R operace

27.11.2023 - Entity (FacilityGQLModel, FacilityTypeGQLModel, FacilityEventGQLModel, FacilityEventStateTypeGQLModel), Resolver FacilityBy3Letters, RU nad ExternalIdModel, ExternalIdTypeModel, ExternalIdCategoryModel

15.1.2024 - Kompletní CRUD na požadovanými entitami, autorizace operací, CRUD dotazy na GQL v souboru externalids_queries.json, popisy API v kódu (description u GQLModelů) a popisy DB vrstvy (comment u DBModelů), 90%  test coverage

# Hodnocení:

Absolvování jednoho projektového dne (součástí je commit na github ne starší než 1 týden) 5 b (x3, tj. 15 b), pod omluvě lze nahradit individuálně

Příběh (na githubu) 5 b (součástí příběhu je časová posloupnost commitů, definice problémů k vyřešení)

Řádné komentáře v kódu (včetně description u GQLModelů, strawberry fieldsa a comment u DBModelů) 5 b

Vygenerovaná dokumentace 5 b

Prokázaná funkčnost jako samostatný kontejner 5 b

Prokázaná funkčnost jako prvek docker-compose (s odkazem na samostatný kontejner z docker hubu) 5 b

Vytvoření docker containeru, publikace na Docker hub 5 b

Kompletní CRUD 5 b

_json 5 b

Obhajoba 60 b, každý student předvede „dopracovaný“ SQL a GQL model (bez ohledu na týmovou práci)

Lze získat až 120 bodů. Předmětem projdete, pokud budete mít více než 50 bodů, hodnocení „A“ získáte za 90 bodů a více

# Doporučené zdroje:

https://github.com/hrbolek/_uois

https://graphql.org/

https://docs.docker.com/compose/
