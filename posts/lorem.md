---
title: Sample Post
date: 12/01/2012
draft: False
---

[TOC]

# h1 Heading

## h2 Heading

### h3 Heading

#### h4 Heading

##### h5 Heading

###### h6 Heading


## Text styling

| input                   | output                |
| ----------------------- | --------------------- |
| `**This is bold text**` | **This is bold text** |
| `_This is italic text_` | _This is italic text_ |


## Blockquotes

> Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse suscipit nemo velit dignissimos deserunt, aliquid vitae architecto itaque dicta quidem. Natus voluptate atque minima temporibus eaque itaque repellendus voluptatum possimus?

## Lists

Unordered

- Create a list by starting a line with `+`, `-`, or `*`
- Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    - Ac tristique libero volutpat at
    * Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit

Ordered

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa

## Code

Inline `code`

Syntax highlighting

```python3
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
```

## Tables

| Option | Description                                                               |
| ------ | ------------------------------------------------------------------------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default.    |
| ext    | extension to be used for dest files.                                      |

Right aligned columns

| Option |                                                               Description |
| -----: | ------------------------------------------------------------------------: |
|   data | path to data files to supply the data that will be passed into templates. |
| engine |    engine to be used for processing templates. Handlebars is the default. |
|    ext |                                      extension to be used for dest files. |

## Links

[link text](http://dev.nodeca.com)

## Horizontal Rules

---

## Images

![Stormtroopocat](/static/img/sample.png)


Footnote 1 link[^first].

To know more about other features consult [python-markdown](https://python-markdown.github.io/)'s website


[^first]: Footnotes **can have markup**
