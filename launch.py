import gradio as gr
import openai

def run_prompt(prompt, key):
    openai.api_key = key
    res = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return res.choices[0].text.strip()

iface = gr.Interface(fn=run_prompt,
                     inputs=["textbox", "textbox"],
                     outputs="textbox",
                     title="Prompt Playground")

iface.launch()
