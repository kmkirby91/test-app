import streamlit as st
import pandas as pd
import time
from datetime import datetime

# Initialize session state variables
if "start_time" not in st.session_state:
    st.session_state["start_time"] = None
if "elapsed_time" not in st.session_state:
    st.session_state["elapsed_time"] = 0
if "is_running" not in st.session_state:
    st.session_state["is_running"] = False
if "preview_data" not in st.session_state:
    st.session_state["preview_data"] = {
        "Option 1": "",
        "Option 2": "",
        "Option 3": "",
        "Free Text": "",
    }
if "data" not in st.session_state:
    st.session_state.data = []
if "categories" not in st.session_state:
    st.session_state["categories"] = {"Category 1": [], "Category 2": [], "Category 3": []}
if "kanban_board" not in st.session_state:
    st.session_state["kanban_board"] = {
        "Clinical": [],
        "Research": [],
        "Teaching": [],
        "Outreach": [],
        "Other": [],
    }

# Stopwatch Functions
def toggle_stopwatch():
    """Start or stop the stopwatch."""
    if not st.session_state["is_running"]:
        st.session_state["start_time"] = time.time()
        st.session_state["is_running"] = True
    else:
        st.session_state["elapsed_time"] += time.time() - st.session_state["start_time"]
        st.session_state["start_time"] = None
        st.session_state["is_running"] = False

def reset_stopwatch():
    """Reset the stopwatch."""
    st.session_state["start_time"] = None
    st.session_state["elapsed_time"] = 0
    st.session_state["is_running"] = False

def update_preview_data(option_1, option_2, option_3, free_text):
    """Update the preview data for the stopwatch."""
    st.session_state["preview_data"] = {
        "Option 1": option_1,
        "Option 2": option_2,
        "Option 3": option_3,
        "Free Text": free_text,
    }

def log_entry():
    """Log the current preview and elapsed time with a timestamp."""
    if st.session_state["is_running"]:
        elapsed_time = time.time() - st.session_state["start_time"] + st.session_state["elapsed_time"]
    else:
        elapsed_time = st.session_state["elapsed_time"]
    entry = {
        "Date Added": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Add timestamp
        "Option 1": st.session_state["preview_data"]["Option 1"],
        "Option 2": st.session_state["preview_data"]["Option 2"],
        "Option 3": st.session_state["preview_data"]["Option 3"],
        "Free Text": st.session_state["preview_data"]["Free Text"],
        "Elapsed Time": round(elapsed_time, 2),
    }
    st.session_state.data.append(entry)

# Category Functions
def add_to_category(category_key, text_input_key):
    """Add an input value to a specific category and sort alphabetically."""
    value = st.session_state.get(text_input_key, "").strip()
    if value:
        st.session_state["categories"][category_key].append(value)
        st.session_state["categories"][category_key].sort()  # Sort alphabetically
        st.session_state[text_input_key] = ""  # Clear input field

def get_padded_categories():
    """Ensure all category columns are of equal length by padding with empty strings."""
    max_length = max(len(col) for col in st.session_state["categories"].values())
    padded_categories = {
        key: col + [""] * (max_length - len(col)) for key, col in st.session_state["categories"].items()
    }
    return padded_categories

# Kanban Board Functions
def add_to_kanban_list(column, text_input_key):
    """Add a new task to a Kanban column."""
    task = st.session_state.get(text_input_key, "").strip()
    if task:
        st.session_state["kanban_board"][column].append({"task": task, "completed": False})
        st.session_state[text_input_key] = ""  # Clear input field

def toggle_task_completion(column, index):
    """Toggle the completion status of a task."""
    st.session_state["kanban_board"][column][index]["completed"] = not st.session_state["kanban_board"][column][index]["completed"]

def delete_task(column, index):
    """Delete a task from a Kanban column."""
    st.session_state["kanban_board"][column].pop(index)

# Pages
def stopwatch_page():
    """Render the Stopwatch page."""
    st.title("Stopwatch")

    # Get the dynamic options for each dropdown
    categories = get_padded_categories()
    option_1_values = [val for val in categories["Category 1"] if val.strip()]
    option_2_values = [val for val in categories["Category 2"] if val.strip()]
    option_3_values = [val for val in categories["Category 3"] if val.strip()]

    col1, col2, col3 = st.columns(3)
    with col1:
        option_1 = st.selectbox("Select Option 1", option_1_values)
    with col2:
        option_2 = st.selectbox("Select Option 2", option_2_values)
    with col3:
        option_3 = st.selectbox("Select Option 3", option_3_values)

    free_text = st.text_area("Enter your text here")

    st.write("### Stopwatch")

    button_label = "Stop" if st.session_state["is_running"] else "Start"
    if st.button(button_label):
        toggle_stopwatch()

    st.button("Reset Stopwatch", on_click=reset_stopwatch)
    st.button(
        "Update Preview",
        on_click=update_preview_data,
        args=(option_1, option_2, option_3, free_text),
    )
    st.button("Log Entry", on_click=log_entry)

    if st.session_state["is_running"]:
        elapsed_time = time.time() - st.session_state["start_time"] + st.session_state["elapsed_time"]
    else:
        elapsed_time = st.session_state["elapsed_time"]

    st.write(f"Elapsed Time: **{elapsed_time:.2f} seconds**")

    st.write("#### Stopwatch Preview")
    preview_df = pd.DataFrame([st.session_state["preview_data"]])
    st.table(preview_df)

    st.write("### Recent Logs")
    if st.session_state.data:
        recent_logs = pd.DataFrame(st.session_state.data).tail(5)
        st.table(recent_logs)
    else:
        st.write("No logs yet.")

def log_page():
    """Render the Log page."""
    st.title("Log of Events")
    if st.session_state.data:
        df = pd.DataFrame(st.session_state.data)
        st.table(df)
    else:
        st.write("No logs yet.")

def categories_page():
    """Render the Categories page."""
    st.title("Categories")

    # Input boxes for each category with Enter key functionality
    col1, col2, col3 = st.columns(3)

    with col1:
        st.text_input(
            "Add to Category 1",
            key="category_1_input",
            on_change=add_to_category,
            args=("Category 1", "category_1_input"),
        )

    with col2:
        st.text_input(
            "Add to Category 2",
            key="category_2_input",
            on_change=add_to_category,
            args=("Category 2", "category_2_input"),
        )

    with col3:
        st.text_input(
            "Add to Category 3",
            key="category_3_input",
            on_change=add_to_category,
            args=("Category 3", "category_3_input"),
        )

    # Display the updated table
    st.write("### Current Categories (Alphabetically Sorted)")
    padded_categories = get_padded_categories()
    categories_df = pd.DataFrame(padded_categories)
    st.table(categories_df)

def kanban_board_page():
    """Render the Kanban-style board with nested tasks and checkboxes."""
    st.title("Kanban Board")

    # Display and manage each column
    for column in ["Clinical", "Research", "Teaching", "Outreach", "Other"]:
        with st.expander(column):
            # Add task to the column
            task_input_key = f"{column}_input"
            st.text_input(
                f"Add task to {column}",
                key=task_input_key,
                on_change=add_to_kanban_list,
                args=(column, task_input_key),
            )

            # Display tasks in the column
            for index, task_data in enumerate(st.session_state["kanban_board"][column]):
                task = task_data["task"]
                completed = task_data["completed"]

                # Create a row for each task with a checkbox and delete button
                col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
                with col1:
                    if st.checkbox(
                        "Mark Complete",
                        value=completed,
                        key=f"{column}_{index}_checkbox",
                        label_visibility="hidden",
                    ):
                        toggle_task_completion(column, index)
                with col2:
                    task_text = f"~~{task}~~" if completed else task
                    st.markdown(f"- {task_text}")
                with col3:
                    if st.button("🗑", key=f"{column}_{index}_delete"):
                        delete_task(column, index)

# Main Function
def main():
    """Main function to display pages."""
    page = st.sidebar.selectbox("Navigate", ["Stopwatch", "Log", "Categories", "Kanban Board"])

    if page == "Stopwatch":
        stopwatch_page()
    elif page == "Log":
        log_page()
    elif page == "Categories":
        categories_page()
    elif page == "Kanban Board":
        kanban_board_page()

main()
