import streamlit as st
st.sidebar.title("To-Do list app")
st.sidebar.write("this is a to-do list app created using streamlit")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("📝 To-Do List App")

# Add new task
new_task = st.text_input("Enter a new task")

if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "done": False})

st.write("### Your Tasks")

# Display tasks
for i, task in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([6, 2, 2])

    # Task checkbox
    with col1:
        task["done"] = st.checkbox(task["task"], value=task["done"], key=i)

    # Delete button
    with col2:
        if st.button("Delete", key=f"del{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()

# Clear all tasks
if st.button("Clear All"):
    st.session_state.tasks = []