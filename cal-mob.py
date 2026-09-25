
import webbrowser
from flask import Flask
app = Flask(__name__)
@app.route("/manifest.json")
def manifest():
    return app.send_static_file("manifest.json")
@app.route("/service-worker.js")
def service_worker():
    return app.send_static_file("service-worker.js")
@app.route("/")
def home():
    return """
<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
<link rel="manifest" href="/manifest.json">
<style>
body {
    background-color: #F5F5F5;
 font-family: Arial, sans-serif; 
 margin: 0;  
}
h1 {
    text-align: center;
}
label {
    display: block;
    text-align: center;
    margin-top: 15px;
    font-weight: bold;
}
input {
    display: block;
    width: 80%;
    max-width: 300px;
    margin: 5px auto;
    padding: 12px;
    font-size: 18px;
    text-align: center;
}
button {
    display: block;
    margin: 20px auto;
    padding: 12px 25px;
    font-size: 16px;
    font-weight: bold;
 background-color: #2E7D32;
    color: white;
    border-radius: 6px;
  border: none;  
}
#result {
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}
#subtotal,
#taxAmount {
    text-align: center;
    font-size: 18px;
    margin: 10px;
}
.clear-button {
    background-color: #1976D2;
}@media (max-width: 600px) {
    h1 {
        font-size: 28px;
    }

    input {
        width: 85%;
        box-sizing: border-box;
    }

    button {
        width: 70%;
        max-width: 250px;
    }
}
.exit-button {
    background-color: #D32F2F;
}
</style> 
<h1>Price Calculator</h1>
<label>Enter Price:</label>
<input type="number" id="price">
<label>Tax Rate (%):</label>
<input type="number" id="tax" value="13">
<button onclick="calculate()">Calculate</button>
<button class="clear-button" onclick="clearCalculator()">Clear</button>


<p id="subtotal"></p>
<p id="taxAmount"></p>
<p id="result"></p>
<script>
function clearCalculator() {
document.getElementById("price").value = "";
document.getElementById("tax").value = "13";
document.getElementById("result").innerText = "";
document.getElementById("subtotal").innerText = "";
document.getElementById("taxAmount").innerText = "";
}
function calculate() {
let price = parseFloat(document.getElementById("price").value);
let tax = parseFloat(document.getElementById("tax").value) / 100;
let total = price + (price * tax);
let taxAmount = price * tax;
document.getElementById("subtotal").innerText = "Subtotal: $" + price.toFixed(2);
document.getElementById("taxAmount").innerText = "Tax: $" + taxAmount.toFixed(2);
document.getElementById("result").innerText = "Total: $" + total.toFixed(2);
}
if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/service-worker.js");
}
</script>
"""
import ctypes
from ctypes import wintypes
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
