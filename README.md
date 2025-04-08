Link Tracker
============================================

This project demonstrates how attackers can gather user data by simply getting someone to click a suspicious link. It's created **strictly for educational purposes** to raise awareness about link-based attacks.

Prerequisites
-------------

-   Python 3 installed on your system

-   Basic understanding of terminal commands

-   An Ngrok account (or any other port-forwarding tool)

Features
--------

When a user clicks the link, the server:

-   Logs their **IP address**

-   Captures **Device & Browser info (User-Agent)**

-   Retrieves **Cookies** (if available)

-   Records the **Referrer** page

-   Fetches **Location details** using the IP address

-   Redirects to a **legit website** so the action goes unnoticed

All captured data is stored in a file called: `victim_logs.txt`

Installation Steps
------------------

1.  **Clone the Repository**

    bash
```
    git clone https://github.com/jagdishtripathy/Link-Tracker.git
    cd Link-Tracker
```
2.  **Install Dependencies**

    Use `pip` to install the required libraries:

    bash
```
    pip install flask requests

```
3.  **Run the Flask Server**

    Launch the application:

    bash
```
    python3 tracker.py

```
4.  **Expose the Local Server**

    Use Ngrok to expose your local server to the internet:

    bash
```
    ngrok http 8080

```
5.  **Test the Link**

    Share the Ngrok URL generated in the terminal to simulate a real-world scenario.

    > ⚠️ Only test this in a legal and ethical environment. Never use it on unsuspecting individuals.

Sample Log Output
-----------------

yaml
```
[2025-04-05 21:07:02]
IP Address: 2401:4900:75fc:9472::45d8:ef8
Location: Delhi, Delhi, India
User-Agent: Mozilla/5.0 (Linux; Android 10; ...)
Cookies: None
Referrer: None
```
----------------------------------------

Disclaimer
----------

This tool is intended **strictly for educational purposes** to show how easily user data can be harvested through malicious links. Do **not** use this tool for unethical or illegal activities.

Always obtain **explicit consent** before testing or demonstrating this tool with others.

Credits
-------

This project was inspired by real-world cybersecurity demonstrations and red team tactics to raise awareness about phishing and link-based attacks.
