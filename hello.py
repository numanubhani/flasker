from flask import Flask, render_template


# creating flask instance

app = Flask(__name__)


# creating a route decorator
@app.route('/')
def index():
    first_name = "code"
    stuff = "This is a text"

    favorite_pizza = ["Pepperoni", "Cheese", "Mashrooms", 41]
    return render_template("index.html", 
                           first_name=first_name,
                           stuff=stuff, 
                           favorite_pizza=favorite_pizza)


# def index():
#     return "Hello World"


@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name = name)


# create custom error pages

# invalid URl

@app.errorhandler(404)
def page_not_found(e):
        return render_template("404.html"), 404

# invalid URl
@app.errorhandler(404)
def page_not_found(e):
        return render_template("404.html"), 404

# Internal Server Error 
@app.errorhandler(500)
def page_not_found(e):
        return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)