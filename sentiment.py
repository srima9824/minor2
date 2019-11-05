import six
import os
from google.cloud import language
from google.cloud.language import types
from google.cloud.language import enums
from google.cloud import language_v1
api_key= "AIzaSyAv-jbvsteT5h6lvU7Kae-8hmPWzDNVuWI"
file = open("review.txt", "r")
l1= file.readlines()
print(l1)

def sample_analyze_sentiment(content,sco):
    client = language_v1.LanguageServiceClient()
    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {'type': type_, 'content': content}
    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment
    sco.append(sentiment.score)
    sco.append(sentiment.magnitude)
    print('Score: {}'.format(sentiment.score))
    print('Magnitude: {}'.format(sentiment.magnitude))
    return sco

v=[]
for i in l1:
    sample_analyze_sentiment(i, v)