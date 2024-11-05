from flask import Flask, render_template, request
import google.generativeai as genai

# تكوين مفتاح API
genai.configure(api_key="AIzaSyBgDUjffrnflJi31S6J-EuNa5pKtXUVGrY")
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

def generate_code(description):
    if "code" in description.lower() or "generate code" in description.lower():
        response = model.generate_content(f"Generate Python code for: {description}")
        return response.text
    else:
        return "Please provide a description that includes 'code' or 'generate code'."

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_code = ""
    if request.method == 'POST':
        user_input = request.form['description']
        generated_code = generate_code(user_input)
    return render_template('index.html', code=generated_code)

if __name__ == "__main__":
    app.run(debug=True)
