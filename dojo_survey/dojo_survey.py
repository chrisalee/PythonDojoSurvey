from flask import Flask, render_template, request  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)
# The "@" decorator associates this route with the function immediately following
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
    print('*'*40)
    print(request.form)
    your_name_from_form = request.form['your_name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comment_from_form = request.form['comment']
    return render_template("show.html", your_name_on_template=your_name_from_form,location_on_template=location_from_form,language_on_template=language_from_form,
    comment_on_template=comment_from_form)


if __name__ == "__main__":
    app.run(debug=True)
