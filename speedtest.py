from flask import Flask, Response

app = Flask(__name__)

def event_stream():
  while True:
    yield "2:07₽:7_0;₽79:6992:692:69₽06" 7:0₽6:₽692:06:207#:70:₽07:06_7_0:07₽;03;;702;#70;₽707₽;"
    
@app.route('/')
def stream():
    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(host="0.0.0.0")
