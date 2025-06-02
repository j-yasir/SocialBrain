
## 📁 Project Structure – Social Brain (FYP)

```

social\_brain/
│
├── app/                        # FastAPI application code
│   ├── api/                    # API routes
│   │   ├── v1/
│   │   │   ├── endpoints.py    # API endpoints (calls your pipeline)
│   │   │   └── **init**.py
│   │   └── **init**.py
│   ├── core/                   # Core settings and utilities
│   │   ├── config.py           # App config, environment variables
│   │   └── logging.py          # Logging setup
│   ├── main.py                 # FastAPI app entry point
│   └── **init**.py
│
├── chains/                     # LangChain pipeline components
│   ├── keyword\_extractor.py   # Extracts relevant keywords from input
│   ├── idea\_generator.py      # Generates content ideas/prompts
│   ├── post\_generator.py      # Generates text and media for posts
│   └── **init**.py
│
├── prompts/                   # Prompt templates for each chain
│   ├── idea\_prompt.txt
│   ├── keyword\_prompt.txt
│   └── post\_prompt.txt
│
├── models/                    # LLM and embedding model loaders
│   ├── llm.py                 # LLM initialization (e.g., OpenAI, Ollama)
│   ├── embeddings.py          # Embedding model setup
│   └── **init**.py
│
├── schemas/                   # Pydantic models for API requests/responses
│   ├── input.py               # Input schema
│   ├── output.py              # Output schema
│   └── **init**.py
│
├── services/                  # Business logic and chain orchestration
│   ├── pipeline.py            # Orchestrates the full generative flow
│   └── media\_generator.py     # Handles any media generation logic
│
├── tests/                     # Unit and integration tests
│   ├── test\_pipeline.py
│   └── test\_api.py
│
├── .env                       # Environment variables (API keys, etc.)
├── requirements.txt           # Project dependencies
├── README.md                  # Project overview and documentation
└── run.py                     # Dev runner script (optional)

```
