import json
import pandas as pd
from .client import Client
from .exceptions import *

class ClientWithAddOns(Client):
    def __init__(self):
        super().__init__()

    def export(self, data_type: str = None, export_type: str = None, lang: str = None, filename: str = None):
        if (data_type is not None and (data_type in ['ideas', 'challenges', 'queries'])) \
        and (export_type is not None and (export_type in ['text', 'json', 'csv'])):
            if lang is not None:
                filename = 'artilipy_export' if filename is None else filename
                data = self.beautifyIdeaCache(lang) if data_type == 'ideas' \
                    else self.beautifyChallengeCache(lang) if data_type == 'challenges' \
                    else self.beautifyDictCache(lang)[0]
                if data_type in ['ideas', 'challenges']:
                    if export_type == 'csv':
                        df = pd.DataFrame(data, columns=[ data_type ])
                        df.to_csv(f'{filename}.csv', index=False)
                    elif export_type == 'text':
                        with open(f'{filename}.txt', mode='w+') as txtfile:
                            for datapiece in data:
                                txtfile.write(datapiece+'\n')
                    else:
                        with open(f'{filename}.json', 'w+') as jsonfile:
                            data_json = [
                                {
                                    'idea': idea,
                                    'index': index
                                } for index, idea in enumerate(data)
                            ]
                            json.dump(data_json, jsonfile)
                else:
                    data_reformed = [[data_piece['word'], data_piece['explanation']] for data_piece in data]
                    if export_type == 'csv':
                        data_pandas = {
                            'word': [data_piece['word'] for data_piece in data],
                            'explanation': [data_piece['explanation'] for data_piece in data]
                        }
                        df = pd.DataFrame(data_pandas, columns=[ "word", "explanation" ])
                        df.to_csv(f'{filename}.csv', index=False, header=True)
                    elif export_type == 'text':
                        with open(f'{filename}.txt', mode='w+') as txtfile:
                            for data_piece in data_reformed:
                                txtfile.write(f'{data_piece[0]}: {data_piece[1]}\n')
                    else:
                        with open(f'{filename}.json', 'w+') as jsonfile:
                            json.dump(data, jsonfile)
            else:
                raise langNotSpecified
        else:
            raise incorrectParams

    def beautifyIdeaCache(self, lang: str = None):
        if lang is not None and lang in ['eng', 'ru']:
            return list(
                map(lambda idea: idea.json()['generated_idea'][lang], self.__dict__['cached_ideas'][0])
            )
        else:
            raise langNotSpecified

    def beautifyChallengeCache(self, lang: str = None):
        if lang is not None and lang in ['eng', 'ru']:
            return list(
                map(lambda idea: idea.json()['generated_challenge'][lang], self.__dict__['cached_challenges'][0])
            )
        else:
            raise langNotSpecified

    def beautifyDictCache(self, lang: str = None):
        existing_cached_languages = list(map(lambda el: el[1], self.__dict__['cached_queries']))
        if lang in existing_cached_languages:
            if lang in ['eng', 'ru']:
                return list(map(lambda el:
                    list(map(
                        lambda query_el: {'word': query_el[0],
                                          'explanation': query_el[1]},
                        el[0].json()['query_results']
                    )), list(
                    filter(lambda query: query[1] == lang, self.__dict__['cached_queries'])
                )))
            else:
                return list(map(
                    lambda el: {
                        list(map(
                            lambda query_el: {'word': query_el[0],
                                              'explanation': query_el[0]},
                            el[0].json()['query_results']
                        ))
                    }, self.__dict__['cached_queries']
                ))
        else:
            raise langIsNotCached
