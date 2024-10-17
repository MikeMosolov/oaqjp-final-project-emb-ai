import json
import operator
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = json_obj, headers = header)
    string_response = response.text
    formatted_response = json.loads(string_response)
    first_key = formatted_response['emotionPredictions']
    # print(first_key)
    
    anger_score = first_key[0]["emotion"]['anger']
    disgust_score = first_key[0]["emotion"]['disgust']
    fear_score = first_key[0]["emotion"]['fear']
    joy_score = first_key[0]["emotion"]['joy']
    sadness_score = first_key[0]["emotion"]['sadness']
    
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }

    dominant_emotion = max(result.items(), key=operator.itemgetter(1))[0]

    if dominant_emotion:
        result.update(
            {'anger': anger_score, 
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            })

    # json_obj = json.dumps(result)
    return result
    
    
