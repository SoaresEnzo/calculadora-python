from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")


@app.route("/", methods=["GET", "POST"])
def home():
    if(request.method == "GET"):
        return render_template("index.html")
    else:
        if(request.form["num1"] != "" and request.form["num2"] != ""):
            num1 = int(request.form["num1"])
            num2 = int(request.form["num2"])
            opc = request.form["opc"]

            if(opc == "soma"):
                return {
                    "resultado": str(num1+num2)
                }
            elif(opc == "subt"):
                return {
                    "resultado": str(num1-num2)
                }
            elif(opc == "mult"):
                return {
                    "resultado": str(num1*num2)
                }
            elif(opc == "divi"):
                return {
                    "resultado": str(num1//num2)
                }
            else:
                return "Insira uma opção válida"

        else:
            return "Insira valores válidos"


@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")


@app.errorhandler(405)
def not_found(error):
    return "Uso de verbo errado"

# i:47:00


app.run(port=8000, debug=True)
