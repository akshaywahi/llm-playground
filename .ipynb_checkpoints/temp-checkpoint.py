import google.generativeai as genai
import os

# 1. Configure with your key
genai.configure(api_key="AIzaSyBqe_JdRc5EUcGJfa3JQV3Gv_hIDUDW0u0")

# 2. Call it directly on the genai module
print("Available Embedding Models:")
for m in genai.list_models():
    if 'embedContent' in m.supported_generation_methods:
        print(f" - {m.name}")
