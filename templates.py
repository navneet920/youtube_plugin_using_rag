import os
import logging
from pathlib import Path

logging.basicConfig(format='[%(asctime)s]: %(message)s', level=logging.INFO)

list_of_files = [
    # rag
    "rag/__init__.py",
    "rag/pipeline.py",

    # indexing
    "rag/indexing/__init__.py",
    "rag/indexing/loader.py",
    "rag/indexing/chunking.py",
    "rag/indexing/embedding.py",
    "rag/indexing/vector_store.py",

    # retrieval
    "rag/retrieval/__init__.py",
    "rag/retrieval/retriever.py",
    "rag/retrieval/reranker.py",

    # augmentation
    "rag/augmentation/__init__.py",
    "rag/augmentation/prompt_builder.py",

    # generation
    "rag/generation/__init__.py",
    "rag/generation/llm.py",
    "rag/generation/response_parser.py",

    # evaluation
    "rag/evaluation/__init__.py",
    "rag/evaluation/metrics.py",

    # models
    "models/__init__.py",
    "models/embedding_model.py",
    "models/llm_model.py",
    "models/model_config.py",

    # data
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/embeddings/.gitkeep",

    # vector db
    "vector_db/faiss_index/.gitkeep",

    # services
    "services/__init__.py",
    "services/rag_service.py",
    "services/transcript_service.py",

    # utils
    "utils/__init__.py",
    "utils/logger.py",
    "utils/helpers.py",
    "utils/text_cleaner.py",


    # tests
    "tests/__init__.py",
    "tests/test_retriever.py",
    "tests/test_pipeline.py",

    # root files
    ".env",
    "requirements.txt",
    "README.md",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")