import requests
import json

def emotion_detector(text_to_analzye: str):
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload_dict = { 'raw_document': { 'text': text_to_analzye } }
    r = requests.post('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict', json=payload_dict, headers=headers)
    r_json = json.loads(r.text)
    anger_score = r_json["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = r_json["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = r_json["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = r_json["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = r_json["emotionPredictions"][0]["emotion"]["sadness"]

    emotions_dict = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }

    max_key = max(emotions_dict, key=emotions_dict.get)
    emotions_dict["dominant_emotion"] = max_key
    return emotions_dict