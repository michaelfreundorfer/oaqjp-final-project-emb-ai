import requests

def emotion_detector(text_to_analzye: str):
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload_dict = { 'raw_document': { 'text': text_to_analzye } }
    r = requests.post('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict', json=payload_dict, headers=headers)