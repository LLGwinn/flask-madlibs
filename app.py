from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story_lookup

app = Flask(__name__)
app.config['SECRET_KEY'] = 'big_secret'

debug = DebugToolbarExtension(app)


@app.route('/')
def story_dropdown():
    """ Show list of stories to select in dropdown """

    return render_template('home.html', stories=story_lookup.values())

@app.route('/inputs')
def show_prompts():
    """ Show form with story prompts to get user input """

    story_select = request.args['story_select']
    story = story_lookup[story_select]
    prompts = story.prompts
    
    return render_template('inputs.html', 
                           story_select=story_select, 
                           title=story.title,
                           prompts=prompts)

@app.route('/story')
def show_story():
    """ Show selected story based on user input """

    story_select = request.args['story_select']
    story = story_lookup[story_select]
    
    madlib_story = story.generate(request.args)

    return render_template('story.html', title=story.title, madlib_story=madlib_story)

