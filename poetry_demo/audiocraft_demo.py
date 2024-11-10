import gradio as gr

def test(text):
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
    text = gr.TextArea(label="Текст:", placeholder="Напиши что-нибудь!", elem_classes="feedback", elem_id="custom_textarea")
    merge = gr.Button("Получить аудиофайл")
    out = gr.Audio(label="Результат:", elem_classes="feedback")
    merge.click(fn=test, inputs=text, outputs=out, api_name="audiocraft_demo")

demo.launch(share=True, show_api=False)