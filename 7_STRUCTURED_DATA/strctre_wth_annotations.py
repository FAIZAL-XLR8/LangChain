from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
load_dotenv()
llm = HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct", task="text-generation")
chat_model = ChatHuggingFace(llm=llm)
#we define a class of typedDict for the specific kind of strcture o/p we need
from typing import TypedDict,Annotated,Literal,Optional
#this is the schema
class structure_format(TypedDict):
    summary:Annotated[str,"The review of the product in 100 lines"]
    sentiment:Annotated[Literal["pos","neg"],"positive or negative "]
    pros: Annotated[Optional[list[str]], "give me the pros of the product"]
    cons : Annotated[Optional[list[str]], "The cons of the product"]

#we defined it
structured_model = chat_model.with_structured_output(structure_format)
response = structured_model.invoke(""" I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don’t use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons:
Bulky and heavy—not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors """)
print(response)
print(response['summary'])
print(response['sentiment'])
