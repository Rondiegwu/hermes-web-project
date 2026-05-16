from flask import Flask, render_template
import threading
from hermes_core import run_automation_cycle

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>RS Plus Tooth Powder</h1><p>Our AI 'Hermes' is currently generating daily health tips!</p>"

def start_hermes():
    # This runs Hermes in the background so the website doesn't freeze
    run_automation_cycle()

if __name__ == "__main__":
    # Start the automation thread
    threading.Thread(target=start_hermes).start()
    app.run(host='0.0.0.0', port=10000)
