from langchain_core.prompts import PromptTemplate
user_template = PromptTemplate(
    template="""
Tell me about anime character {name}
    """,
    input_variables=['name'],
    validate_template=True
)
# query_prompt = user_template.invoke({'' : "", }) --> this is giving values to templarte
user_template.save('template.json')