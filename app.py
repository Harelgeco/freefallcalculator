from flask import Flask, jsonify, render_template
import time

app = Flask(__name__)
start_time = None  # משתנה גלובלי לשמירת זמן התחלה

@app.route('/')
def home():
    return render_template('index.html')  # פה מפנים לדף index.html

@app.route('/start', methods=['GET'])
def start_timer():
    global start_time
    start_time = time.time()  # שמירת זמן ההתחלה
    return jsonify({"message": "measure started"})

@app.route('/stop', methods=['GET'])
def stop_timer():
    global start_time
    if start_time is None:
        return jsonify({"error": "measure didn't start"}), 400

    elapsed_time = time.time() - start_time  # חישוב הזמן שעבר
    height = 4.9 * (elapsed_time ** 2)  # חישוב גובה נפילה חופשית

    start_time = None  # איפוס המדידה
    return jsonify({"elapsed_time": round(elapsed_time, 2), "height": round(height, 2)})

if __name__ == '__main__':
    app.run(debug=True)
