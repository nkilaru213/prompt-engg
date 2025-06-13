import gradio as gr
import requests

def call_backend(prompt):
    response = requests.post(
        "http://localhost:8000/ask",
        json={"question": prompt}
    )
    return response.json()["answer"]

iface = gr.Interface(fn=call_backend, inputs="text", outputs="text", title="Gradio + FastAPI")
iface.launch()
