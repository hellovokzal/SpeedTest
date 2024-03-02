from flask import Flask, Response

app = Flask(__name__)

def event_stream():
  while True:
    yield "$-8;382;37;70$;074;73-703+02:7:273:0:7$037:0:6303"
    
@app.route('/')
def stream():
    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(host="0.0.0.0")
