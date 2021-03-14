from flask import Flask, request, render_template
from stories import Story

app=Flask(__name__)

@app.route('/')
def home():
    """makes homepage"""
    return render_template("home.html")

@app.route("/story")
def adlib():
    """gets info from form and populates it in webpage"""
    place = request.args.get("place")
    noun = request.args.get("noun")
    verb = request.args.get("verb")
    adjective =request.args.get("adjective")
    plural_noun =request.args.get("plural_noun")
    story_words = [place,noun,verb,adjective,plural_noun]
    story = f"Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."
    filled_story = Story(story_words,story)

    return render_template("story.html",place=place,noun=noun,
    verb=verb,adjective=adjective, plural_noun=plural_noun,filled_story=filled_story.generate(request.args))
