## artilipy: complete documentation (v. 0.0.1)
---
### Features:
- basic client
- add-on client
---
## Basic client [`artilipy.client.Client()`]
### Attributes:
* endpoints [primary API endpoints]: dict
* cached_ideas [pseudo-cache with the history of generated ideas]: `list`
* cached_challenges [pseudo-cache with the history of generated challenges]: `list`
* cached_queries [pseudo-cache with the history of dictionary queries]: `list`
### Methods:
#### * generate_idea() [get random idea from the generator. The idea is auto-cached in `cached_ideas`] -> (returns) `requests.models.Response`
#### * generate_challenge() [get random challenge from the generator. The challenge is auto-cached in `cached_challenges`] -> `requests.models.Response`
#### * get_patrons() [get list of patrons] -> `requests.models.Response`
#### * get_banner() [get a random banner] -> `requests.models.Response`
#### * dict_query(query, lang) [perform a search query in the dictionary. Query is auto-cached in `cached_queries`] -> `requests.models.Response`
> * query [search query]: str, 
> * lang [search language. 'eng' or 'ru']: str or None (optional)
---
## Add-on client [`artilipy.addons.ClientWithAddOns()`]
This is a subclass of the basic client
### Methods:
#### * beautifyIdeaCache(lang) [get a prettified list of `cached_ideas`] -> `list`
> * lang [search language. 'eng' or 'ru']: str
#### * beautifyChallengeCache(lang) [get a prettified list of `cached_challenges`] -> `list`
> * lang [search language. 'eng' or 'ru']: str
#### * beautifyDictCache(lang) [get a prettified list of `cached_queries`] -> `list`
> * lang [search language. 'eng' or 'ru']: str
