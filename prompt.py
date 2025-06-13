import gradio as gr
import openai

def run_prompt(prompt, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

iface = gr.Interface(
    fn=run_prompt,
    inputs=["text", gr.Textbox(label="OpenAI API Key", type="password")],
    outputs="text",
    title="Prompt Engineering Playground"
)

iface.launch()
