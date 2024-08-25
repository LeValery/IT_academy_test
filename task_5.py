# -*- coding: utf-8 -*-


def distr_by_word_count(search_queries):
    word_count = [len(search_querie.split()) for search_querie in search_queries]
    word_count.sort()

    for cnt in set(word_count):
        perc = word_count.count(cnt)/len(word_count)*100
        inflectional_suffix = 'о' if cnt%20==1 else 'а' if cnt%20 in (2, 3, 4) else ''
        print(f'{cnt} слов{inflectional_suffix}: {perc:.0f}%')

    
"""
search_queries = ["watch new movies",
"coffee near me", "how to find the determinant", "python",
"data science jobs in UK", "courses for data science",
"taxi", "google", "yandex", "bing",
"foreign exchange rates USD/BYN",
"Netflix movies watch online free",
"Statistics courses online from top universities"]

distr_by_word_count(search_queries)
"""
