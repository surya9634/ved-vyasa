import streamlit as st
from main_app_course import create_course_structure  # Import from main_app_course

# Custom CSS for a hacker and futuristic theme
custom_css = """
<style>
body {
    background-color: #000;
    color: #00ff00;
    font-family: 'Courier New', Courier, monospace;
}

.stButton>button {
    background-color: #00ff00;
    color: #000;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.stButton>button:hover {
    background-color: #00cc00;
}

.stTextInput>div>div>input {
    background-color: #000;
    color: #00ff00;
    border: 1px solid #00ff00;
    padding: 10px;
    font-size: 16px;
}

.stMarkdown {
    color: #00ff00;
}

.stSpinner>div>div {
    border-top-color: #00ff00;
}

.stSuccess {
    color: #00ff00;
}

.stError {
    color: #ff0000;
}

.stWarning {
    color: #ffff00;
}
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

def main():
    st.title("Course Creator")

    # Input field for the topic
    topic = st.text_input("Enter a topic to create a course:")

    if st.button("Create Course"):
        if topic:
            # Show a loading spinner while the course is being generated
            with st.spinner("Generating course..."):
                course_content = create_course_structure(topic)

            if not course_content or "error" in course_content:
                st.error(f"Error: {course_content.get('error', 'Failed to generate course content.')}")
            else:
                st.success(f"Course created for topic: {topic}")
                st.write("**Course Outline:**")
                st.write(course_content.get("course_outline", ""))

                st.write("**Lessons:**")
                for lesson in course_content.get("lessons", []):
                    st.write(f"- {lesson}")

                st.write("**Quizzes:**")
                for quiz in course_content.get("quizzes", []):
                    st.write(f"- {quiz}")
        else:
            st.warning("Please enter a topic to create a course.")

if __name__ == "__main__":
    main()