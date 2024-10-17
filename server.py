''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''

# importing the required mosules
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# initiating the flask app
app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_detection():
    ''' This code receives the text from the HTML interface and
        runs emotion detection over it using emotion_detection()
        function. The output returned shows the emotions and confidence
        scores, as well as dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    dominant_emotion = result['dominant_emotion']

    return f"""For the given statement, the system response is 'anger': {result['anger']},
    'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}.
    The dominant emotion is <b>{dominant_emotion}</b>."""

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="localhost", port=5000)