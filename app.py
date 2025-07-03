from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run')
def run_simulation():
    data = []
    leakage_hours = random.sample(range(24), random.randint(1, 2))  # Leak in 1–2 random hours
    overflow_threshold = 55

    for hour in range(24):
        # Random values
        usage = random.randint(10, 60)
        level = random.randint(10, 60)
        grey = random.randint(0, 20) if random.random() > 0.7 else 0
        event = "Normal"

        # Inject leakage
        if hour in leakage_hours:
            usage += random.randint(30, 50)
            event = "Leakage Detected"
        elif level > overflow_threshold:
            event = "Overflow Risk"

        # Format data
        data.append({
            'time': f"{hour:02d}:00",
            'usage': usage,
            'level': level,
            'grey': grey,
            'event': event
        })

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)



