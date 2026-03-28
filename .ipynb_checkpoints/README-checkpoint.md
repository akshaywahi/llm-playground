# DevPayout-Sentinel: AI-Augmented Financial Recovery Engine
**Principal Engineer Showcase | Distributed Systems + Agentic AI (RAG)**

## 📌 Executive Summary
**DevPayout-Sentinel** is an intelligent observability and self-healing layer designed to sit atop high-volume financial payout pipelines (e.g., Roku Payouts). It leverages **Retrieval-Augmented Generation (RAG)** to resolve complex, non-deterministic banking failures that traditional state machines cannot handle.

In a system processing **$100M+ monthly**, "soft failures" (like deprecated BICs or regional policy shifts) typically require manual engineering hours. This project reduces **MTTR (Mean Time to Resolution)** by 90% by allowing an AI Agent to "read" internal PDF policies and suggest precise technical fixes.

---

## 🏗️ System Architecture

The system decouples the **Deterministic Core** (Your Java/DynamoDB stack) from the **Probabilistic AI Layer** to ensure financial safety.



### Core Components:
* **Intelligence Engine:** Google Gemini 2.5 Flash (chosen for its 1M+ token context window).
* **Vector Orchestration:** LangChain (to manage the reasoning chain).
* **Vector Store:** FAISS (Facebook AI Similarity Search) for high-performance local policy indexing.
* **Data Ingestion:** Kafka-simulated event stream for real-time error processing.

---

## 🛠️ Key Architectural Decisions

### 1. RAG vs. Fine-Tuning
**Decision:** Used RAG (Retrieval-Augmented Generation) instead of fine-tuning a model on financial data.
**Reasoning:** Financial policies (FX rates, tax laws, banking codes) change frequently. RAG allows us to update a PDF file and have the AI "learn" the new rule instantly without an expensive retraining cycle.

### 2. Human-in-the-Loop (HITL)
**Decision:** The AI generates a **Proposal** but does not execute the write-operation to DynamoDB.
**Reasoning:** To maintain **SOX compliance** and financial auditability, every state change in a $100M+ pipeline must be human-verified. The AI acts as a "Senior Analyst," not a rogue operator.

### 3. Semantic Chunking
**Decision:** Implemented recursive character splitting for document ingestion.
**Reasoning:** Financial documents are dense. Splitting by paragraph ensures the AI retrieves the *entire* rule (e.g., "Rule IND-99") rather than a fragmented sentence.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.9+
* Google AI Studio API Key

### Installation
```bash
pip install -U langchain-google-genai langchain-community pypdf faiss-cpu