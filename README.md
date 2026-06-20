# AI Sales Assistant

An AI-powered sales assistant that combines Retrieval-Augmented Generation (RAG), AI Agents, semantic search, and intelligent tool usage to automate product discovery, customer support, and sales interactions.

## Overview

AI Sales Assistant helps users discover products, resolve customer queries, and receive intelligent recommendations through natural language conversations.
The system leverages embeddings, pgvector-based retrieval, AI agent workflows, memory, planning, and tool integrations to provide accurate and context-aware responses.

## Features

- Product Search and Recommendations
- Customer Support Automation
- Retrieval-Augmented Generation (RAG)
- Semantic Search using Embeddings
- pgvector-based Knowledge Retrieval
- AI Agent Workflows
- Conversation Memory
- Multi-Step Query Resolution
- Intelligent Planning and Decision Making
- External Tool Integration
- API and Database Connectivity

---

## Architecture

```text
User Query
    │
    ▼
AI Agent
    │
    ▼
Memory & Context
    │
    ▼
Planner
    │
    ▼
Tool Selection
 ┌─────────────┬──────────────┬──────────────┐
 ▼             ▼              ▼
Product      Customer      Database
Search       Support       Retrieval
 Tool          Tool           Tool
 └─────────────┴──────────────┘
               │
               ▼
        pgvector Retrieval
               │
               ▼
      Relevant Product Data
               │
               ▼
         Gemini LLM
               │
               ▼
         Final Response
```

## Tech Stack

### Programming Language
- Python

### Backend
- Flask
- REST APIs

### AI & LLM
- Gemini API
- Generative AI
- AI Agents
- Prompt Engineering
- Multi-Step Reasoning

### Retrieval
- Retrieval-Augmented Generation (RAG)
- Embeddings
- Semantic Search
- Vector Retrieval

### Database
- PostgreSQL
- pgvector

### Tools & Integrations
- External APIs
- Tool Calling
- MCP-inspired Tool Interfaces

---

## Project Workflow

1. User submits a product or support query.
2. AI Agent analyzes the user intent.
3. Planner determines required actions.
4. Agent selects appropriate tools.
5. Relevant product and knowledge-base information is retrieved using embeddings and pgvector.
6. Retrieved context is combined with user intent.
7. Gemini generates a context-aware response.
8. Memory stores conversation history for future interactions.
9. Final response is returned to the user.

---

## Sample Queries

### Product Search

```text
Suggest the best laptop under ₹80,000.
```

### Product Comparison

```text
Compare iPhone 15 and Samsung S24.
```

### Customer Support

```text
What is the warranty policy for this product?
```

### Recommendation

```text
Recommend a gaming laptop for machine learning projects.
```

---

## Key Concepts Implemented

- AI Agents
- Retrieval-Augmented Generation (RAG)
- Embeddings
- Semantic Search
- Vector Databases
- pgvector
- Tool Calling
- Memory Management
- Multi-Step Planning
- Intelligent Automation

---

## Challenges Addressed

- Understanding user intent accurately.
- Retrieving relevant product information efficiently.
- Maintaining conversational context.
- Supporting complex multi-step queries.
- Reducing hallucinations using retrieval-based grounding.
- Integrating multiple external tools and data sources.

---

## Future Enhancements

- Multi-Agent Collaboration
- Voice-Based Interaction
- Personalized Recommendations
- Real-Time Inventory Integration
- Order Tracking Agent
- Cloud Deployment on AWS
- Advanced Analytics Dashboard
- Fine-Tuned Domain-Specific Models

---

## Installation

```bash
git clone https://github.com/pujitha-mule/AI_Sales_Assistant.git

cd AI_Sales_Assistant

pip install -r requirements.txt
```

## Run Application

```bash
python app.py
```

---

## Resume Highlights

- Built an AI-powered sales assistant for product search, customer support, and sales inquiries.
- Implemented RAG with embeddings and pgvector for product and knowledge-base retrieval.
- Developed AI agent workflows for memory, planning, and multi-step query resolution.
- Integrated tool interfaces enabling AI agents to interact with APIs, databases, and enterprise services.

---

## Author

**Pujitha Mule**

Generative AI | AI Agents | Intelligent Applications

GitHub: https://github.com/pujitha-mule
