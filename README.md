`ydnassg` is a ~50 SLOC static website generator written in [Flask](https://flask.palletsprojects.com/en/2.2.x/) and made static with [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/).  
Publishing a post is simply a matter of creating a markdown file in `/posts` and adding the required metadata in YAML format, like in the examples, and if you want to know more simply read the whole entire 55 lines!!!

## features:

+ tailwindcss support
+ no config files
+ one click deploy with netlify
+ a lot of [markdown extensions](https://python-markdown.github.io/extensions/)
+ fully static
+ print-friendly pages

[![](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/rcastellotti/ydnassg)


start dev server with: `python3 app.py dev`, build for production using: `python3 app.py build`

For more info check out [this](http://rcastellotti.dev/posts/you-dont-need-a-ssg/) blog post.