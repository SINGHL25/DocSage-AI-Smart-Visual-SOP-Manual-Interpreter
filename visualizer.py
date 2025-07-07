import streamlit as st
import graphviz

def visualize_doc_structure(text):
    st.subheader("📊 Document Structure")

    lines = text.split("\n")
    dot = graphviz.Digraph()

    section_counter = 0
    for line in lines:
        if len(line.strip()) == 0:
            continue
        if line.strip().endswith(":") or line.strip().isdigit():
            section_counter += 1
            dot.node(f"sec{section_counter}", line.strip())

    if section_counter == 0:
        st.info("No structured headings detected. Displaying full text.")
    else:
        for i in range(1, section_counter):
            dot.edge(f"sec{i}", f"sec{i+1}")
        st.graphviz_chart(dot)

