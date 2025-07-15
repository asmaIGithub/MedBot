from langchain.llms import HuggingFaceHub
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceHub(
    repo_id="google/flan-t5-large",
    model_kwargs={"temperature": 0.7, "max_length": 512}
)

memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

def get_response(user_input):
    return conversation.run(user_input)
