import google.generativeai as genai
import tkinter as tk
from tkinter import ttk
import os

# Set up Gemini API credentials
API_KEY = "AIzaSyDX-tnVxg-5elUvlh2vL6H65fjCyMzsLW4"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

def translate_text(text, source_language, target_language):
    """Translates text using Gemini API."""
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Translate the following '{source_language}' text to '{target_language}': {text}"

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

def on_translate_click():
    """Handles translation when the button is clicked."""
    text = text_input.get()
    source_language = source_lang_input.get()
    target_language = target_lang_input.get()

    if text and source_language and target_language:
        translated_text = translate_text(text, source_language, target_language)
        result_label.config(text=translated_text)
    else:
        result_label.config(text="Please fill in all fields.")

# Create the user interface
app = tk.Tk()
app.title("Multilingual Translation Tool")
app.geometry("400x200")

# UI Components
ttk.Label(app, text="Text:").grid(column=0, row=0, padx=10, pady=5)
text_input = ttk.Entry(app, width=40)
text_input.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(app, text="Source Language:").grid(column=0, row=1, padx=10, pady=5)
source_lang_input = ttk.Entry(app, width=20)
source_lang_input.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(app, text="Target Language:").grid(column=0, row=2, padx=10, pady=5)
target_lang_input = ttk.Entry(app, width=20)
target_lang_input.grid(column=1, row=2, padx=10, pady=5)

translate_button = ttk.Button(app, text="Translate", command=on_translate_click)
translate_button.grid(column=1, row=3, padx=10, pady=10)

result_label = ttk.Label(app, text="", wraplength=350)
result_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

app.mainloop()