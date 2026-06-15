import streamlit as st
import random

st.title("Fault Tolerance Load Balancer")

# إعداد السيرفرات
if 'servers' not in st.session_state:
    st.session_state.servers = {"Server 1": True, "Server 2": True, "Server 3": True}
    st.session_state.logs = []

# إدارة الواجهة (Checkboxes)
st.subheader("إدارة السيرفرات:")
col1, col2, col3 = st.columns(3)
with col1: st.session_state.servers["Server 1"] = st.checkbox("Server 1 (Active)", value=st.session_state.servers["Server 1"])
with col2: st.session_state.servers["Server 2"] = st.checkbox("Server 2 (Active)", value=st.session_state.servers["Server 2"])
with col3: st.session_state.servers["Server 3"] = st.checkbox("Server 3 (Active)", value=st.session_state.servers["Server 3"])

# منطق التوزيع الذكي
if st.button("إرسال طلب"):
    # هنا نحدد المتاح فقط لحظة الضغط
    active_servers = [name for name, active in st.session_state.servers.items() if active]
    
    if not active_servers:
        st.error("خطأ: لا توجد سيرفرات متاحة!")
    else:
        # يختار فقط من القائمة التي فيها True
        target = random.choice(active_servers)
        st.session_state.logs.append(f"تم توجيه الطلب إلى: {target}")

# عرض السجل
st.subheader("سجل العمليات:")
for log in reversed(st.session_state.logs):
    st.write(log)
