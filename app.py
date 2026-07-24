from flask import Flask, render_template, request
import math
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/math", methods=["POST"])
def calculate():

    try:
        operation = request.form["operation"]
        num1 = float(request.form["num1"])

        # Square root only needs one number
        if operation == "sqrt":
            num2 = 0
        else:
            num2 = float(request.form["num2"])

        operations = {
            "add": ("Addition", num1 + num2),
            "subtract": ("Subtraction", num1 - num2),
            "multiply": ("Multiplication", num1 * num2),
            "divide": ("Division", num1 / num2 if num2 != 0 else "Cannot divide by zero"),
            "power": ("Power", num1 ** num2),
            "mod": ("Modulus", num1 % num2),
            "log": ("Logarithm", math.log(num1, num2)),
            "sqrt": ("Square Root", math.sqrt(num1))
        }

        operation_name, answer = operations[operation]

        return render_template(
            "result.html",
            operation=operation_name,
            num1=num1,
            num2="" if operation == "sqrt" else num2,
            result=answer
        )

    except Exception as e:
        return render_template(
            "result.html",
            operation="Error",
            num1="-",
            num2="-",
            result=str(e)
        )


def get_local_ip():
    """
    Returns the local IPv4 address of this computer.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


if __name__ == "__main__":

    local_ip = get_local_ip()

    print("\n" + "=" * 55)
    print("🚀 Engineering Calculator is Running...")
    print("=" * 55)
    print(f"💻 Localhost : http://127.0.0.1:5000")
    print(f"🌐 Local IP  : http://{local_ip}:5000")
    print("=" * 55)
    print("📱 Open the Local IP on any device connected")
    print("   to the same Wi-Fi/LAN network.")
    print("=" * 55 + "\n")

    app.run(host="0.0.0.0", port=5000, debug=True)