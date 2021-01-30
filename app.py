from flask import Flask, request, jsonify
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

output = {}

def sentiment(sentence):
    nltk.download('vader_lexicon') # has all list of good or bad words
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(sentence)['compound'] # compound gets sentiment of whole sentence
    if(score > 0):
        return "Positive"
    else:
        return "Negative"

@app.route('/',methods=['GET','POST'])

# define route
# GET : passed data firectly in url e.g http://127.0.0.1:5000/q="Good Day"
# Post: data is passed encryptedly not in url

def sentimentRequest():
    if request.method =='POST':
        sentence = request.form['q']
    else:
        sentence = request.args.get('q')

    sent = sentiment(sentence)
    output['sentiment'] = sent
    return jsonify(output)

# run appli as server
if __name__ == '__main__':
    app.run