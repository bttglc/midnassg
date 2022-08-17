from flask import Flask, render_template
from os import listdir
import markdown
import json
from flask_frozen import Freezer
import sys
from datetime import datetime
import yaml

app = Flask(__name__)
freezer = Freezer(app)


def getMetadata(static_post):
    with open(f"posts/{static_post}") as f:
        heading = f.read().split("---")[1]
        out = yaml.load(heading, Loader=yaml.FullLoader)
        out["slug"] = static_post[:-3]
        return out


@app.route("/")
def index():
    posts = []
    for post in listdir("posts"):
        post = getMetadata(post)
        if post["draft"] is False:
            posts.append(post)
    posts = sorted(
        posts, key=lambda d: datetime.strptime(d["date"], "%d/%m/%Y"), reverse=True
    )
    return render_template("index.html", posts=posts)


@app.route("/posts/<path:path>/")
def posts(path):
    f = open(f"./posts/{path}.md", "r")
    htmlmarkdown = markdown.Markdown(
        extensions=["fenced_code", "codehilite", "meta", "footnotes", "toc", "tables"]
    )
    post = htmlmarkdown.convert(f.read())
    return render_template("post.html", post=post, meta=htmlmarkdown.Meta)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    if sys.argv[1] == "dev":
        app.run(debug=True, host="0.0.0.0")
    elif sys.argv[1] == "prod":
        freezer.freeze()
