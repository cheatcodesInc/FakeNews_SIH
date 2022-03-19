import requests

API_URL = "https://api-inference.huggingface.co/models/chinhon/fake_tweet_detect"
headers = {"Authorization": f"Bearer {'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'}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def factcheck(input):
    output = query({"inputs": input,})
    try:
      false_score = output[0][0].get('score')
    except:
      return 'Timed Out. Please try again.'
    if(false_score>=0.6):
      return "Fake"
    elif(false_score<=0.4):
      return "Not fake"
    else:
      return "Undetermined"