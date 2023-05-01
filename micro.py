from flask import Flask, request, jsonify
import requests
import re
app = Flask(__name__)
@app.route('/count-words', methods=['POST'])
def count_words():
    website_url = request.json['url']
    response = requests.get(website_url)
    words = re.findall('\w+', response.text.lower())
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    return jsonify(word_counts)
if __name__ == '__main__':
    app.run()
