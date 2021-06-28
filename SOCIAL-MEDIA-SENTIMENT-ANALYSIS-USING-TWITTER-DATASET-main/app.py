import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))
loaded_vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
loaded_model = pickle.load(open('classification.model', 'rb'))
@app.route('/')
def home():
    return render_template('FrontPagecc.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # tfidf = TfidfVectorizer(max_features=10000, ngram_range=(1, 2))
    s = [(x) for x in request.form.values()]
    # vec = tfidf.transform(int_features)
    # final_features = np.array(int_features).reshape(1, -1)
    print(s)



    # load the model


    # make a prediction
    # x=(loaded_model.predict(loaded_vectorizer.transform(["i hate you"])))
    # prediction = model.predict(s)
    #
    output = ((s[0][-1]))
    # print(type(output))
    if output=="⠀":

        return render_template('ok.html')
    else:
        return render_template('notok.html')
    #


if __name__ == "__main__":
    app.run(debug=True)
