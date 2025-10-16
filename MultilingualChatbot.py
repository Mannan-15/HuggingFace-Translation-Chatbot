from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

class smt :
    def __init__(self) :
        self.translator = pipeline('translation', model = 'facebook/m2m100_418M')
        self.language_codes = {
            'English' : "en",
            "Japanese" : "ja",
            "French" : "fr",
            "Chinese" : "zh",
            "Russian" : "ru",
            "Spanish" : "es",
            "German" : "de",
            "Arabic" : "ar"
        }
        
    def translate(self, text, source_lang, target_lang) :
        src_code = self.language_codes.get(source_lang, source_lang)
        tgt_code = self.language_codes.get(target_lang, target_lang)
        result = self.translator(text, src_lang = src_code, tgt_lang = tgt_code)
        return result[0]['translation_text']

translator = smt()

support_responses = {
    "greeting" : "Hello! How can I help you today?",
    "product" : "Our product comes with a 30-day warranty. What specific information do you need?",
    "pricing" : "Our pricing starts at $69 per month. Would you like to know about our different plans?",
    "contact" : "You can reach our support team at support@example.com or call us at 6969.",
    "default" : "Could you please rephrase your question?"
}

@app.route('/')
def home() :
    return render_template('mlt.html')

@app.route('/chat', methods = ['POST'])

def chat() :
    data = request.json
    user_msg = data['message']
    user_lang = data.get('language', 'English')

    response_key = 'default'
    for key in support_responses :
        if key in user_msg.lower() :
            response_key = key
            break

    response = support_responses[response_key]

    if user_lang != 'English' :
        response = translator.translate(response, 'English', user_lang)

    return jsonify({'response' : response})

if __name__ == '__main__' :
    app.run(debug = True)