from flask import Flask, render_template_string

app = Flask(__name__)

# หน้าตาเว็บเครื่องคิดเลขแบบง่ายด้วย Python/Flask
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>Casio Calculator Python</title>
    <style>
        body { font-family: Arial, sans-serif; background: #e0e0e0; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .calculator { background: #222; padding: 20px; border-radius: 10px; width: 300px; color: white; text-align: center; }
        h2 { font-size: 16px; margin-bottom: 10px; color: #ff9800; }
        input { width: 90%; padding: 10px; font-size: 18px; margin-bottom: 10px; text-align: right; }
        button { padding: 10px 15px; font-size: 16px; margin: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="calculator">
        <h2>Casio Calc (Python Backend)</h2>
        <form method="POST">
            <input type="text" name="expression" value="{{ expression }}" placeholder="เช่น 5+5">
            <br>
            <button type="submit">คำนวณ</button>
        </form>
        <h3>ผลลัพธ์: {{ result }}</h3>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    from flask import request
    expression = ""
    result = "0"
    if request.method == 'POST':
        expression = request.form.get('expression', '')
        try:
            # ป้องกันความปลอดภัยเบื้องต้น อนุญาตเฉพาะตัวเลขและเครื่องคำนวณพื้นฐาน
            allowed_chars = set("0123456789+-*/.() ")
            if all(c in allowed_chars for c in expression):
                result = str(eval(expression))
            else:
                result = "Error (Invalid chars)"
        except Exception:
            result = "Error"
    return render_template_string(HTML_TEMPLATE, expression=expression, result=result)

if __name__ == '__main__':
    app.run(debug=True)
