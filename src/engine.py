import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_classic.chains import RetrievalQA

class PayoutSentinel:
    def __init__(self, policy_path="data/policies/roku_payout_policy_v4.pdf"):
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

        # Load and Index Policies
        loader = PyPDFLoader(policy_path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)

        self.vectorstore = FAISS.from_documents(docs, self.embeddings)
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever()
        )

    def analyze(self, event):
        query = f"Analyze this failure: {event}. Provide RCA and the exact DynamoDB fix."
        return self.qa_chain.invoke(query)
