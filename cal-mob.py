
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

 font-family: Arial, sans-serif;background: linear-gradient(135deg, #eef2f7, #d9e2ec); 
 margin: 0;  
}<p id="subtotal"></p>
<p id="taxAmount"></p>
<p id="result" class="total-result"></p>
h1 {
    text-align: center;
}
.calculator-card {
    background: white;
    width: 90%;
    max-width: 420px;
    margin: 40px auto;
    padding: 30px 30px 35px;
    box-sizing: border-box;
    border-radius: 18px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
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
    border-radius: 10px;
    border: none;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.18);
    cursor: pointer;
 transition: transform 0.15s, box-shadow 0.15s;   
}

#result {
text-align: center;
    fobutton:active {
    transform: translateY(2px);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
}
    font-size: 22px;
    font-weight: bold;
    color: #2E7D32;
}
.result-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 10px 15px;
    margin: 10px auto 0;
    max-width: 300px;
}
#subtotal,
#taxAmount {
    text-align: center;
    font-size: 18px;
    margin: 10px;
}
.bottom-buttons {
    display: flex;
    justify-content: center;
    gap: 15px;
}

.bottom-buttons button {
    margin: 5px 0 20px 0;
}
.clear-button {
    background-color: #1976D2;
}
.exit-button {
    background-color: #D32F2F;
}
@media (max-width: 600px) {
    h1 {
        font-size: 28px;
    }

    input {
        width: 85%;
        box-sizing: border-box;
        border: 1px solid #cbd5e1;
        border: 1px solid #cbd5e1;
        border-radius: 10px;
        outline: none;
    }
input:focus {
    border-color: #2E7D32;
    box-shadow: 0 0 0 3px rgba(46, 125, 50, 0.12);
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
<div class="calculator-card">
<h1>🧮 Price Calculator</h1>
<label>Enter Price:</label>
<input type="number" id="price">
<label>Tax Rate (%):</label>
<input type="number" id="tax" value="13">
<button onclick="calculate()">Calculate</button>
<div class="bottom-buttons">
<button class="clear-button" onclick="clearCalculator()">Clear</button>
<button class="exit-button" onclick="exitCalculator()">Exit</button>
</div>

<div class="result-box">
<p id="subtotal"></p>
<p id="taxAmount"></p>
<p id="result"></p>
</div>
<script>
function exitCalculator() {
    document.querySelector(".calculator-card").innerHTML =
        "<h1>Calculator Closed</h1><p style='text-align:center;'>You can now close this app.</p>";
}
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
if (isNaN(price) || isNaN(tax)) {
    document.getElementById("subtotal").innerText = "";
    document.getElementById("taxAmount").innerText = "";
    document.getElementById("result").innerText = "Please enter a valid price.";
    return;
}
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
