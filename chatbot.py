'''
A Simple Tkinter interfae for chatGTP
'''
# improt Tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext   # for text box 
from tkinter import filedialog     # for open file dialog

import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

# Find the starting directory
START_DIR = os.getcwd()

#----------------------------------  Procedures  ----------------------------------#

# This helper function will make it easier to use prompts and look at the generated outputs:
def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    try:

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature, # this is the degree of randomness of the model's output
        )
    except Exception as e:
        # Produce error box
        tk.messagebox.showerror(title="Error", message=e)
        return None
    
    return response.choices[0].message["content"]


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

# Define a function for the generate button
def generate():
    # Get the prompt text
    prompt = promptText.get(1.0, tk.END)

    response_text = get_completion(prompt)
    chatGPT_response.insert(tk.END, f"AI:\n{response_text}\n\n")


# Define a function for the clear current conversation
def clear_prompt_and_response():
    # Clear the promt box and the response box
    if promptText is not None:
        promptText.delete(1.0, tk.END)

    if chatGPT_response is not None:
        chatGPT_response.delete(1.0, tk.END)

#----------------------------------   Setup Tkinter  ----------------------------------#

# Create instance
root = tk.Tk()
root.title("ChatGPT")
#root.resizable(0,0) # disable resizing the GUI
root.geometry("515x690")
root.iconbitmap("01 Nenebiker.ico")


#----------------------------------   Menus  ----------------------------------#

# Add menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Settings")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)


#----------------------------------   Add response box  ----------------------------------#


# Add response scrolled text box
chatGPT_response = scrolledtext.ScrolledText(root, width=59, height=20, wrap=tk.WORD)
chatGPT_response.grid(column=0, row=0, sticky='WE', padx=10, pady=10, columnspan=2)

# Default message
chatGPT_response.insert(tk.END, f"AI: Hello, I am ChatGPT, your friendly chatbot.\n\n")

#----------------------------------   User interactions  ----------------------------------#

# Add a scrolled text box for user input
promptText = scrolledtext.ScrolledText(root, width=59, height=15, wrap=tk.WORD)
promptText.grid(column=0, row=1, sticky='WE', padx=10, pady=10, columnspan=2)


# Adding a Button call generate passing the prompt entered by the user
action = ttk.Button(root, text="Generate", command=lambda: generate())
action.grid(column=0, row=2, padx=10, pady=10)

# Adding a Button to clear the response box
action = ttk.Button(root, text="Clear", command=lambda: clear_prompt_and_response())
action.grid(column=1, row=2, padx=10, pady=10)


#----------------------------------   Main Loop  ----------------------------------#

# Start the GUI
root.mainloop()
