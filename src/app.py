"""
app.py
Gradio interface for UIC Dining RAG system.
Run with: python app.py
Then open: http://localhost:7860
"""

import gradio as gr
from query import ask


def handle_query(question: str):
    if not question.strip():
        return "Please enter a question.", ""

    result = ask(question)
    answer = result["answer"]
    sources = "\n".join(f"• {s}" for s in result["sources"])
    return answer, sources


with gr.Blocks(title="UIC Dining Guide") as demo:
    gr.Markdown("## UIC Dining Guide\nAsk anything about UIC campus dining based on real student reviews.")

    inp = gr.Textbox(
        label="Your question",
        placeholder="e.g. What do students say about portion sizes?",
        lines=2,
    )
    btn = gr.Button("Ask", variant="primary")

    answer_box = gr.Textbox(label="Answer", lines=8, interactive=False)
    sources_box = gr.Textbox(label="Retrieved from", lines=4, interactive=False)

    btn.click(handle_query, inputs=inp, outputs=[answer_box, sources_box])
    inp.submit(handle_query, inputs=inp, outputs=[answer_box, sources_box])

demo.launch()