import cognitive_face as CF

KEY = 'a3f85c1deee843b58a33dc6c89a1f1f4'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
result = CF.face.detect(img_url)
print(result)

#Key 1: a3f85c1deee843b58a33dc6c89a1f1f4

#Key 2: f9c6e97e6abb45658069ae9a825c29f1
