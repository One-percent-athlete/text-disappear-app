
from flask import Flask, render_template, request
import threading

app = Flask(__name__)

# Global variable to store the text content
text_buffer = ""
# Timer object to trigger text deletion
timer = None

def delete_text():
  global text_buffer, timer
  # Simulate a delay (replace with actual logic for user inactivity)
  import time
  time.sleep(1)  # Replace 5 with desired delay in seconds for deletion
  text_buffer = ""
  timer = None  # Cancel the timer

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/update", methods=["POST"])
def update_text():
  global text_buffer, timer
  # Get the new text content from the request form
  new_text = request.form["text"]
  text_buffer = new_text

  # Cancel any existing timer
  if timer:
    timer.cancel()

  # Create a new timer to delete text after inactivity
  timer = threading.Timer(1, delete_text)  # Replace 5 with desired delay
  timer.start()

  return ""  # No content to return for update route

if __name__ == "__main__":
  app.run(debug=True)