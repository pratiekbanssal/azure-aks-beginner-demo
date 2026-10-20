# Version 3: green page plus a bouncing cat (CSS animation only).
import socket                      # lets us read the machine/pod name
from flask import Flask            # Flask = a small Python web framework

app = Flask(__name__)

PAGE = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Hello App - v3</title>
  <style>
    body {{ margin: 0; height: 100vh; display: flex; flex-direction: column;
           align-items: center; justify-content: center;
           font-family: Arial, sans-serif; background: #b2f2bb; }}
    h1   {{ font-size: 3rem; margin: 0; }}
    .ver {{ font-size: 1.5rem; margin-top: 1rem; }}
    .cat {{ font-size: 5rem; margin: 1rem; animation: bounce 1s ease-in-out infinite; }}
    @keyframes bounce {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-25px); }} }}
    .pod {{ position: fixed; bottom: 1rem; color: #777; font-size: 0.9rem; }}
  </style>
</head>
<body>
  <h1>Hello, how are you?</h1>
  <div class="cat">&#128049;</div>
  <div class="ver">Version 3</div>
  <div class="pod">Served by pod: {pod}</div>
</body>
</html>
"""

@app.route("/")
def home():
    # socket.gethostname() returns the pod name when running in Kubernetes
    return PAGE.format(pod=socket.gethostname())

if __name__ == "__main__":
    # 0.0.0.0 = accept traffic from outside the container (required in Docker/AKS)
    app.run(host="0.0.0.0", port=5000)
