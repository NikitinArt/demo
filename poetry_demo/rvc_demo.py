import gradio as gr

def test(audio1, audio2):
    return gr.Audio()

css = """
button {background-color: green; color: white; border-radius: 8px;}
.gradio-container {
    background-color: #FFFFFF !important;
    border-radius: 10px;
    padding: 20px;
}
button:hover {
    background-color: #218838 !important;
}
.feedback {
    background-color: green;
    color: white;
    border-radius: 8px; 
}
"""
# #custom_textarea textarea {
#     background-color: #2E8B57;
#     color: white;
#     border: 2px solid white;
#     padding: 10px;
#     font-size: 16px;
# }
# #custom_textarea textarea::placeholder {
#     color: white;
#     font-size: 14px;
#     opacity: 1;
# }
# .feedback2{
#     background-color: #2E8B57;
#     color: white;
#     border-radius: 8px;
# }

with gr.Blocks(css=css) as demo:
    a = gr.Audio(label="Первое аудио", elem_classes="feedback")
    b = gr.Audio(label="Второе аудио", elem_classes="feedback")
    merge = gr.Button("Объединить")
    out = gr.Audio(label="Результат:", elem_classes="feedback")
    merge.click(fn=test, inputs=[a, b], outputs=out, api_name="rvc_demo")

demo.launch(share=True, show_api=False)