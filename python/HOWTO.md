# In Jupyter

Jupyter is an environment which runs Python code interactively.
It's better suited for editing code than normal Python REPL.

1. Ideally you want some enviroment which can run Jupyter notebook locally:
    - VS Code or Cursor IDE
    - IntelliJ IDEA or PyCharm
    - actual Jupyter
    - Google Colab is not recommended because the point is to access local files
2. Obtain a API key from https://openrouter.ai/ (if you want to use multiple models) 
    - or OpenAI (https://platform.openai.com/) if GPT is all you need
    - save the key into openrouter.key
3. Highly recommended to use venv. If you use VSCode it will create a virtual environment for you automatically.
    - otherise `python -m venv .venv`, etc.
4. The first cell in template.ipynb will install all the dependencies for you. Only need to use it once
5. Run other cells to see how it works

# Without Jupyter

You can also run the code in a terminal, script, etc.

Still recommend to use venv, `pip install openai` within your venv, obtain API key.

```
(.venv) [alex@unknown8045dd796076 python]$ python
Python 3.12.4 ...
>>> from aihelper import *
>>> print(get_response_chat("Summarize file", read_file("./HOWTO.md")))
This file appears to be a set of instructions for setting up and using a Jupyter notebook environment, particularly for working with AI models. Here's a summary of the main points:
```


