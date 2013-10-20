from flask import render_template, request
from papertalk import papertalk, mongo
from papertalk.utils.utils import jsonify
from papertalk.models.sites import Scholar, Mendeley

@papertalk.route('/article/<int:id>')
def article(id):
    context = {}
    context["article"] = mongo.db.find_one({"_id" : id})
    return render_template('article.html', **context)


@papertalk.route("/article/search", methods=["POST"])
def article_search():
    """
    Parses the article from a given search string.
    This could be a title (most likely); or an author
    """
    text = request.form.get("query", "")
    print text

    articles = Scholar.search(text=text)
    articles += Mendeley.search(text=text)

    return jsonify({"articles" : articles})


@papertalk.route('/article/url', methods=["POST"])
def add_article():
    """
    Scrapes the url and returns a new article
    """
    site = request.form.get("site")
    url = request.form.get("url")

    print site
    print url

    article = {
        "scholar" : Scholar.scrape(url),
        "mendeley" : Mendeley.scrape(url)
    }[site]

    return jsonify(article)


