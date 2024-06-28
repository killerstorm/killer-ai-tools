from openai import OpenAI
import os

with open('openrouter.key', 'r') as f:
    api_key = f.read().replace('\n', '')

client = OpenAI(
    ## if you want to use openrouter, uncomment the following line
    base_url="https://openrouter.ai/api/v1",
    ## if you want to use openai, uncomment the following line
    #base_url="https://api.openai.com/v1",
    api_key=api_key
)

# generatlly prompt is instruction 
# and content is the context
# but you also can add instructions to content, 
# particularly it makes sense if you have a lot of context

def get_response_chat(prompt, content):
    response = client.chat.completions.create(
        model="anthropic/claude-3.5-sonnet", # this is the best model, 200k context
        # List of models: https://openrouter.ai/docs/models
        # Some highlights:
        # google/gemini-flash-1.5 - fast, cheap, 2.8M token context
        # google/gemini-pro-1.5 - like flash but smarter
        # openai/gpt-4-turbo - best understanding of formatting, instruction following, but is a bit lazy
        # openai/gpt-4o - like 4-turbo but faster and more eager, but less exact
        # 
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content}
        ]
    )
    return response.choices[0].message.content

# Helper functions which read file(s) into strings

def read_file(name):
    with open(name, 'r') as f:
        return f.read()

def read_files(directory, extensions):
    res = ""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                res += "//// BEGIN FILE " + file + "\n"
                with open(file_path, 'r') as infile:
                    res += infile.read()
                res += "//// END FILE " + file + "\n"
    return res