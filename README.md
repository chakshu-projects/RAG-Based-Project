# RAG-Based-Project

## 1) Introduction 
This project implements a Retrieval-Augmented Generation (RAG) system that answers user questions based on educational video content. Instead of generating answers only from a language model's knowledge, the system first retrieves the most relevant information from video transcripts using semantic embeddings and then generates a contextual answer using a Large Language Model (LLM).

## 2) Technology Used
  -  Python
  -  FFmpeg
  -  OpenAI Whisper (Large-v2)
  -  BGE-M3 Embedding Model
  -  Ollama
  -  Llama 3.2
  -  Pandas
  -  NumPy
  -  Scikit-learn
  -  Joblib
  -  JSON

## 3) Raw Information(Dataset)  
### a. Video File
The videos explain HTML fundamentals including concepts, syntax, tags, and practical examples.The complete video content is converted into searchable text so users can ask natural language questions related to the course.

### b. Context of Video
The videos explain HTML fundamentals including concepts, syntax, tags, and practical examples.The complete video content is converted into searchable text so users can ask natural language questions related to the course.

### c. How to Download
  -  Download the HTML tutorial videos.
  -  Save the videos inside the tutorials/ folder.
  -  Execute the FFmpeg conversion script.
  -  Audio files are generated inside the audios/ folder.
  -  The audio is transcribed into JSON transcripts using Whisper.
  -  Embeddings are generated and stored for semantic retrieval.

## 4) Workflow  
### a. Flow Diagram
Tutorial Videos  
       │  
       ▼  
FFmpeg Conversion  
(Video → Audio)  
       │  
       ▼  
Whisper Model  
(Audio → Text)  
       │  
       ▼  
Transcript Chunking  
(JSON File)  
       │  
       ▼  
BGE-M3 Embeddings  
       │  
       ▼  
Store Embeddings  
(Joblib DataFrame)  
       │  
       ▼  
User Question  
       │  
       ▼  
Generate Query Embedding  
       │  
       ▼  
Cosine Similarity Search  
       │  
       ▼  
Top Relevant Chunks  
       │  
       ▼  
Llama 3.2  
       │  
       ▼  
Final Answer with Video Timestamp  

### b. Collecting Data / Videos
Educational HTML tutorial videos are collected and stored in the tutorials/ directory. These videos serve as the primary knowledge source for the RAG system.

### c. Converting video into audio 
FFmpeg is used to extract audio from every video automatically. Each video is converted into MP3 format so that it can be processed by the Whisper speech recognition model.

### d. Audio into Text 
The Whisper Large-v2 model transcribes each audio file into English text while preserving timestamp information.

### e. Text to Embeddings
Every transcript chunk is converted into dense vector embeddings using the BGE-M3 embedding model running through Ollama.

### f. Saving into Joblib/Pickle
All transcript chunks along with their embeddings are stored inside a Pandas DataFrame.The DataFrame is serialized using Joblib for fast loading during inference.

### g. Parsing / Reading Embeddings with Prompt  
During execution:
  -  The saved Joblib file is loaded.
  -  The user's question is converted into an embedding.
  -  Cosine similarity is calculated between the query embedding and every transcript embedding.
  -  The top five most relevant transcript chunks are selected.
  -  These chunks are inserted into a custom prompt for the Llama 3.2 model.

## 5) Exceution and Results  
### a. Coding with Blocks
#### i. FFmpeg Block
This module automatically converts all tutorial videos into MP3 audio files using FFmpeg.  
Purpose:
  -  Video preprocessing
  -  Audio extraction
  -  Batch conversion

#### ii. Whisper Block
This module loads the Whisper Large-v2 model and converts audio into timestamped text.  
Functions performed:
  -  Speech Recognition
  -  Translation
  -  Transcript Generation
  -  JSON Export

#### iii.Embeddings Block
This module sends transcript chunks to the BGE-M3 embedding model using Ollama.  
Functions:
  -  Generate semantic embeddings
  -  Assign unique chunk IDs
  -  Save embeddings into a DataFrame
  -  Export using Joblib

### b. Output  
The system successfully:
  -  Converts videos into searchable knowledge.
  -  Retrieves semantically relevant transcript chunks.
  -  Generates accurate answers using Llama 3.2.
  -  Provides the exact video name and timestamp where the concept is explained.
  -  Restricts responses to course-related questions only.

### c. Website Link 
Libraries and Models Used:
  -  Ollama: https://ollama.com/
  -  Whisper: https://github.com/openai/whisper
  -  FFmpeg: https://www.ffmpeg.org/
  -  Joblib: https://joblib.readthedocs.io/en/stable/
  -  BGE-M3 Model: https://huggingface.co/BAAI/bge-m3
  
## 6) Conclusion  
This project successfully demonstrates the implementation of a Retrieval-Augmented Generation (RAG) system for educational video question answering. By integrating FFmpeg, Whisper, BGE-M3 embeddings, cosine similarity, and the Llama 3.2 language model, the system retrieves relevant transcript information before generating responses. This approach improves answer accuracy while allowing users to locate the exact video and timestamp where a topic is explained.
