import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        emotions_res = emotion_detector("I am glad this happened")
        self.assertEqual(emotions_res["dominant_emotion"], "joy")

    def test_anger(self):
        emotions_res = emotion_detector("I am really mad about this")
        self.assertEqual(emotions_res["dominant_emotion"], "anger")

    def test_disgust(self):
        emotions_res = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(emotions_res["dominant_emotion"], "disgust")

    def test_sadness(self):
        emotions_res = emotion_detector("I am so sad about this")
        self.assertEqual(emotions_res["dominant_emotion"], "sadness")

    def test_fear(self):
        emotions_res = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(emotions_res["dominant_emotion"], "fear")

if __name__ == '__main__':
    unittest.main()