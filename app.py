from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store temporary values (in-memory for demo purposes)
state = {
    "num1": "",
    "num2": "",
    "operator": "",
    "result": ""
}

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        btn = request.form.get("btn")

        # Clear everything
        if btn == "C":
            state["num1"] = ""
            state["num2"] = ""
            state["operator"] = ""
            state["result"] = ""

        # Calculate result
        elif btn == "=":
            try:
                n1 = float(state["num1"])
                n2 = float(state["num2"])
                op = state["operator"]

                if op == "+":
                    result = n1 + n2
                elif op == "-":
                    result = n1 - n2
                elif op == "*":
                    result = n1 * n2
                elif op == "/":
                    result = "Error" if n2 == 0 else n1 / n2
                else:
                    result = "Invalid"

                state["result"] = str(result)
                state["num1"] = state["result"]
                state["num2"] = ""
                state["operator"] = ""
            except:
                state["result"] = "Error"

        # Operator clicked
        elif btn in "+-*/":
            if state["num1"]:  # only allow setting operator if num1 exists
                state["operator"] = btn

        # Number clicked
        elif btn.isdigit() or btn == ".":
            if state["operator"]:
                state["num2"] += btn
                state["result"] = state["num2"]
            else:
                state["num1"] += btn
                state["result"] = state["num1"]

    return render_template("index.html", result=state["result"])

if __name__ == "__main__":
    app.run(debug=True)

