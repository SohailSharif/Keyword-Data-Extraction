"""Server for Take Home"""

import logging
import logging.config

import flask
import markupsafe
import mistune
from flask import Flask
from include.errors import APIError
from werkzeug.exceptions import HTTPException

logging.config.fileConfig("logging.conf")

app = Flask(__name__)

# Import handlers or any other modules that require
# app to be initialized here, to prevent circular
# dependencies.
import handlers.api

app.register_blueprint(handlers.api.api)

# "main" is more reliable than __name__ (which is "__main__")
logger = logging.getLogger("main")


# Register error handler
@app.errorhandler(Exception)
def handle_error(e):
    if isinstance(e, APIError):
        response = {"error": e.message}
        response["metadata"] = e.metadata if e.metadata else {}
        response["metadata"]["class"] = e.__class__.__name__

        if e.reason:
            response["reason"] = e.reason

        return response, e.STATUS_CODE, e.headers

    if isinstance(e, HTTPException):
        response = {"error": e.description}

        return response, e.code

    logger.exception(e)

    return {"error": "Server error"}, 500


@app.route("/")
def about():
    """One-page introduction to Secure Scaffold.

    This renders Markdown to HTML on-the-fly, trusting the Markdown content
    can be used to generate <a> tags. Do not do this on production sites!
    """
    logger.info("about invoked")

    # The Anchors renderer trusts the headers in the Markdown file.
    with open("../README.md") as fh:
        m = mistune.create_markdown(renderer=Anchors())
        readme = m(fh.read())
        readme = markupsafe.Markup(readme)

    context = {
        "page_title": "Secure Scaffold",
        "readme": readme,
    }

    return flask.render_template("about.html", **context)


class Anchors(mistune.HTMLRenderer):
    """Adds id attributes to <h*> elements.

    This is not safe if you cannot trust the Markdown content.
    """

    def header(self, text, level, raw=None):
        name = self.choose_name(text)
        class_ = f"title is-{level}"

        return f'<h{level} id="{name}" class="{class_}">{text}</h{level}>'

    def choose_name(self, text):
        text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore")
        text = re.sub(r"[^\w\s-]", "", text.decode("ascii")).strip().lower()
        text = re.sub(r"[-\s]+", "-", text)

        return text


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
