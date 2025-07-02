from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/armstrong/<int:number>", methods=["GET"])
def check_armstrong(number):
    num_str = str(number)
    num_length = len(num_str)
    armstrong_sum = sum(int(digit) ** num_length for digit in num_str)
    return jsonify({"number": number, "is_armstrong": armstrong_sum == number})


if __name__ == "__main__":
    app.run(debug=True)
