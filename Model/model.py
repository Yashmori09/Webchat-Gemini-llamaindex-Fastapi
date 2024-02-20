import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.embeddings import HuggingFaceEmbeddings
from llama_index.core import ServiceContext
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.embeddings.huggingface_optimum import OptimumEmbedding
from llama_index.core import Settings
from huggingface_hub import hf_hub_download

class Model:
    def __init__(self):
        pass

    def load_model(self):
        load_dotenv()
        GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
        print("staring")
        llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY, convert_system_message_to_human=True)
        print("llm loaded")
        model_name = "thenlper/gte-large"
        
        embed_model = HuggingFaceEmbeddings(
            model_name=model_name
            )
        print("emb loaded")
        documents = SimpleDirectoryReader(r"D:\website-chatbot-gemini-fastapi\artifacts",recursive=True).load_data()
        
        print("doc loaded")
        Settings.llm = None
        Settings.embed_model = embed_model
        Settings.chunk_size = 512
        Settings.chunk_overlap = 64
        print("settings loaded")
        service_context = ServiceContext.from_defaults(
                chunk_size=512, chunk_overlap=64,
                llm=llm,
                embed_model=embed_model
        )
        print("service context done")
        index = VectorStoreIndex.from_documents(documents, service_context=service_context)
        print("index done")
        query_engine = index.as_query_engine()
        print("query engine done")
        print("response done")
        return query_engine
    
    def get_answer(self, question,query_engine):
        response = query_engine.query(question)
        return response

if __name__ == "__main__":
    model = Model()
    #print("Loading model...")
    
    query_engine = model.load_model()
    response=model.get_answer("who Raghu in thinkbyte team?",query_engine)
    print("Query engine:", response)
