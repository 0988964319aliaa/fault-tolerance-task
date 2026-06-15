import streamlit as st

st.title("Fault Tolerance Load Balancer")

# إعداد السيرفرات وحالتها
if 'servers' not in st.session_state:
    st.session_state.servers = {"Server 1": True, "Server 2": True, "Server 3": True}
    st.session_state.logs = []

# التحكم في حالة السيرفر (Up/Down)
st.subheader("إدارة السيرفرات:")
col1, col2, col3 = st.columns(3)
with col1: st.session_state.servers["Server 1"] = st.checkbox("Server 1 (Active)", value=True)
with col2: st.session_state.servers["Server 2"] = st.checkbox("Server 2 (Active)", value=True)
with col3: st.session_state.servers["Server 3"] = st.checkbox("Server 3 (Active)", value=True)

# منطق التوزيع مع مراعاة السيرفرات المتاحة فقط
if st.button("إرسال طلب"):
    active_servers = [s for s, active in st.session_state.servers.items() if active]
    
    if not active_servers:
        st.error("خطأ: لا توجد سيرفرات متاحة!")
    else:
        # اختيار سيرفر متاح
        import random
        target = random.choice(active_servers)
        st.session_state.logs.append(f"تم توجيه الطلب إلى: {target}")

# عرض النتائج
st.subheader("سجل العمليات:")
for log in reversed(st.session_state.logs):
    st.write(log)