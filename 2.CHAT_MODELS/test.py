import requests

model_id = "google/gemma-2-2b-it"
resp = requests.get(f"https://huggingface.co/api/models/{model_id}?expand[]=inferenceProviderMapping")
data = resp.json()
print(data.get("inferenceProviderMapping"))
#this was to check a model existing!