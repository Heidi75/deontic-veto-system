
import streamlit as st
import pandas as pd

st.set_page_config(page_title="HPLM Truth Engine", page_icon="🛡️")

st.title("🛡️ HPLM 'Truth Engine' Demo")
st.subheader("ENEG-OEPM Financial Audit Interface")

# --- LAYER 1: NEURAL INTAKE ---
st.sidebar.header("Control Panel")
user_amount = st.sidebar.number_input("Transaction Amount ($)", value=25000, step=1000)
user_dest = st.sidebar.selectbox("Destination Jurisdiction", ["US", "UK", "RU", "IR", "MX"])
threshold = st.sidebar.slider("Risk Threshold ($)", 5000, 50000, 20000)

st.info("**Layer 1 (NIL):** Ingesting unstructured payment narrative...")

# --- LAYER 4 & 5: SYMBOLIC ARENA & VETO GATE ---
# The logic that protects the moat
high_risk = ["RU", "IR"]
is_violation = (user_amount > threshold) and (user_dest in high_risk)

st.divider()
if is_violation:
    st.error(f"## LAYER 5: VETOED")
    st.warning(f"Policy Violation: {user_dest} transfer of ${user_amount} exceeds ${threshold} limit.")
else:
    st.success(f"## LAYER 5: DEPLOYED")
    st.balloons()

# --- LAYER 6: TRACEBACK & AUDIT ---
with st.expander("🔍 View Layer 6: Forensic Audit Trail"):
    audit_data = {
        "HPLM Layer": ["1: Intake", "4: Symbolic Arena", "5: Deontic Veto Gate"],
        "Process": ["Neural Intake (NIL)", "Dimensional Analysis", "Constraint Satisfaction"],
        "Result": ["Success", "Violation Detected" if is_violation else "Passed", "REFUSAL" if is_violation else "CLEARED"]
    }
    st.table(pd.DataFrame(audit_data))
