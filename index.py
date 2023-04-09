from flask import Flask, render_template, request
import openai
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY' # Replace with your secret key

openai.api_key =  os.environ.get("OPENAI_API_KEY")# Replace with your OpenAI API key
model_engine = "text-davinci-002" # Replace with the desired GPT model

def generate_description(prompt):
    prompt = f"Describe {prompt}."
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    description = response.choices[0].text.strip()
    return description

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        prompt = request.form['input']
        description = generate_description(prompt)
        return render_template('index.html', description=description)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


