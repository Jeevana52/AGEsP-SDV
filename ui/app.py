import streamlit as st
import sys, os
sys.path.append(os.path.abspath(".."))
from orchestrator.workflow import run_pipeline
st.set_page_config(page_title="AGEsP-SDV", layout="wide")
st.title(" Agentic Service for Software-Defined Vehicle (SDV)")
st.caption(" Multi-agent AI dashboard")

req = st.text_area("Enter SDV Feature Requirement", height=100,
    placeholder="e.g. Implement adaptive cruise control...")

if st.button("Run Pipeline", type="primary"):
    if not req.strip():
        st.warning("Please enter a requirement.")
    else:
        with st.spinner("Running pipeline..."):
            result = run_pipeline(req)
        t1,t2,t3,t4,t5 = st.tabs(["Planner","Requirement","Service Design","Generated","Critic"])
        with t1: st.json(result.get("planner",{}))
        with t2: st.json(result.get("requirement",{}))
        with t3: st.json(result.get("service_design",{}))
        with t4: st.code(result.get("generated_code",""), language="python")
        with t5: st.json(result.get("critic",{}))