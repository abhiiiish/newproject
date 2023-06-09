from flask import Flask, render_template, request
import openai
import os
app = Flask(__name__)


openai.api_key =  os.environ.get("OPENAI_API_KEY")# Replace with your OpenAI API key
model_engine = "text-davinci-002" # Replace with the desired GPT model

def generate_description(prompt):
    prompt = f"Describe {prompt}."
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.5,
    )
    description = response.choices[0].text.strip()
    return description

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        company_name = request.form['company_name']
        establishment = request.form['establishment']
        services = request.form['services']
        location = request.form['location']
        prompt = f"Generate description for  Business name {company_name} , which Establish in year {establishment}. Their specialization  are {services} and  located in {location}. And also decribe service in brief."
        description = generate_description(prompt)
        return render_template('index.html', description=description)
    else:
        return render_template('index.html')
    

if __name__ == '__main__':
   from waitress import serve
   serve(app, host="0.0.0.0", port=8080)



