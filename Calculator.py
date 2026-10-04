import pyto_ui as pui
import math
from wsgiref.simple_server import make_server

# طراحی فوق‌العاده مدرن ماشین حساب با HTML و CSS (دارک مود)
html_content = """
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Advanced Calculator</title>
    <style>
        body {
            background-color: #000000;
            color: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
        .calculator {
            width: 100%;
            max-width: 360px;
            padding: 20px;
        }
        .display {
            width: 100%;
            height: 100px;
            background: transparent;
            border: none;
            color: white;
            text-align: right;
            font-size: 48px;
            font-weight: 300;
            margin-bottom: 20px;
            outline: none;
            box-sizing: border-box;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
        }
        button {
            background-color: #333333;
            color: white;
            border: none;
            border-radius: 50%;
            padding: 20px 0;
            font-size: 22px;
            font-weight: bold;
            cursor: pointer;
            outline: none;
            transition: background-color 0.2s;
            aspect-ratio: 1;
        }
        button:active {
            background-color: #555555;
        }
        button.operator {
            background-color: #ff9f0a;
            color: white;
        }
        button.operator:active {
            background-color: #cc7f08;
        }
        button.special {
            background-color: #a5a5a5;
            color: black;
            font-size: 18px;
        }
        button.special:active {
            background-color: #8e8e8e;
        }
        button.sci {
            background-color: #212124;
            color: #ff9f0a;
            font-size: 16px;
            border-radius: 16px;
        }
    </style>
</head>
<body>

<div class="calculator">
    <input type="text" class="display" id="display" readonly value="0">
    <div class="grid">
        <!-- ردیف توابع مهندسی -->
        <button class="sci" onclick="press('sin(')">sin</button>
        <button class="sci" onclick="press('cos(')">cos</button>
        <button class="sci" onclick="press('tan(')">tan</button>
        <button class="sci" onclick="press('sqrt(')">√</button>
        
        <button class="sci" onclick="press('log(')">log</button>
        <button class="sci" onclick="press('Math.PI')">π</button>
        <button class="sci" onclick="press('**')">^</button>
        <button class="sci" onclick="press('(')">(</button>

        <!-- دکمه‌های اصلی -->
        <button class="special" onclick="clearDisplay()">C</button>
        <button class="special" onclick="backspace()">Del</button>
        <button class="special" onclick="press(')')">)</button>
        <button class="operator" onclick="press('/')">/</button>

        <button onclick="press('7')">7</button>
        <button onclick="press('8')">8</button>
        <button onclick="press('9')">9</button>
        <button class="operator" onclick="press('*')">×</button>

        <button onclick="press('4')">4</button>
        <button onclick="press('5')">5</button>
        <button onclick="press('6')">6</button>
        <button class="operator" onclick="press('-')">-</button>

        <button onclick="press('1')">1</button>
        <button onclick="press('2')">2</button>
        <button onclick="press('3')">3</button>
        <button class="operator" onclick="press('+')">+</button>

        <button onclick="press('0')" style="grid-column: span 1;">0</button>
        <button onclick="press('.')">.</button>
        <button class="operator" style="grid-column: span 2; border-radius: 30px;" onclick="calculate()">=</button>
    </div>
</div>

<script>
    let display = document.getElementById('display');
    let expression = "";

    function press(num) {
        if (display.value === "0" || display.value === "Error") {
            expression = "";
        }
        expression += num;
        display.value = expression.replace('Math.PI', 'π').replace('**', '^');
    }

    function clearDisplay() {
        expression = "";
        display.value = "0";
    }

    function backspace() {
        expression = expression.slice(0, -1);
        display.value = expression || "0";
    }

    function calculate() {
        try {
            // شبیه‌سازی توابع ریاضی برای محاسبه متنی
            let sin = Math.sin, cos = Math.cos, tan = Math.tan, sqrt = Math.sqrt, log = Math.log10;
            let result = eval(expression);
            display.value = Number(result.toFixed(6)); // رند کردن تا ۶ رقم اعشار
            expression = String(result);
        } catch (e) {
            display.value = "Error";
            expression = "";
        }
    }
</script>

</body>
</html>
"""

# اجرای یک مرورگر داخلی (Web View) شیک در محیط Pyto آیفون
view = pui.WebView()
view.load_html(html_content)
pui.show_view(view)