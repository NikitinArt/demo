import gradio as gr
from gradio_webrtc import WebRTC

def test(a):
    return gr.Image()

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

with gr.Blocks(css=css) as demo:
    image = WebRTC(label="Stream", mode="send-receive", modality="video")
    # conf_threshold = gr.Slider(
    #     label="Порог уверенности",
    #     minimum=0.0,
    #     maximum=1.0,
    #     step=0.05,
    #     value=0.30,
    # )
    image.stream(
        fn=test,
        inputs=[image],
        outputs=[image], time_limit=10
    )

demo.launch(share=True, show_api=False)