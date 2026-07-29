from flask import Flask, jsonify, render_template, request
import time

app = Flask(__name__)

# Application start time
start_time = time.time()

# Metrics
request_count = 0
last_response_time = 0


@app.before_request
def before_request():
    request.start_time = time.perf_counter()


@app.after_request
def after_request(response):
    global request_count
    global last_response_time

    request_count += 1
    last_response_time = round(
        (time.perf_counter() - request.start_time) * 1000, 2
    )

    return response


@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "message": "Application is healthy",
        "uptime_seconds": round(time.time() - start_time, 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "version": "1.0.0"
    }), 200


@app.route("/metrics")
def metrics():
    return jsonify({
        "status": "UP",
        "requests": request_count,
        "response_time_ms": last_response_time,
        "uptime_seconds": round(time.time() - start_time, 2)
    })


@app.route("/api/info")
def api_info():
    return jsonify({
        "application": "Ghaymah SRE API",
        "language": "Python",
        "framework": "Flask",
        "version": "1.0.0",
        "author": "Moustafa Medhat"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
