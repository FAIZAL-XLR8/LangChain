from langchain_huggingface import HuggingFacePipeline
from dotenv import load_dotenv
load_dotenv()
import os
os.environ['HF_HOME'] = 'D:/huggingface_cache'
chatmodel = HuggingFacePipeline.from_model_id(
    model_id = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs= dict(
    max_new_tokens = 100,
    temperature = 0.5,
    do_sample=True
    )

)
chatmodel.invoke("Who is Naruto Uzumaki!")