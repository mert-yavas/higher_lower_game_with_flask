from flask import Flask
import random

# Create a Flask application instance
app = Flask(__name__)

# Generate a random number between 0 and 9
random_number = random.randint(0, 9)


# Decorator function to make the returned text bold
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    
    return wrapper


# Route for the home page
@app.route("/")
@make_bold
def home():
    # Display a message prompting the user to guess a number between 0 and 9
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="Numbers ranging from 0-9">'


# Route for handling guesses from the user
@app.route("/<int:guess>")
def webpages(guess):
    if guess > random_number:
        # If the guess is too high, return a message in purple text and a GIF
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif guess < random_number:
        # If the guess is too low, return a message in red text and a GIF
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        # If the guess is correct, return a message in green text and a GIF
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
