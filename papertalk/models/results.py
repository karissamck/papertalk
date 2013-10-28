__author__ = 'karissamckelvey'
from papertalk.models.article import Article

def get_known_articles(articles):
    """
    Return the known articles from an article result query
    """
    res = []
    for article in articles:
        try:
            a = Article.lookup({"title" : article["title"], "year": article["year"]})
        except:
            a = article

        res.append(a)
    return res

def get_or_insert_articles(search_results):
    res = []
    for sr in search_results:
        try:
            a = Article.lookup({'canonical_title': sr['canonical_title']})

        except:
            a = Article()
            a.update(sr)
            a.save()

        res.append(a)

    return res

