import gradio as gr

def test(video):
    return "Hello World!!"

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
    video = gr.Video(label="Выберите видео", elem_classes="feedback")
    greet_btn = gr.Button("Конвертировать")
    desc = gr.Textbox(label="Описание:", elem_classes="feedback")
    greet_btn.click(fn=test, inputs=video, outputs=desc, api_name="video-desc_demo")

demo.launch(share=True, show_api=False)