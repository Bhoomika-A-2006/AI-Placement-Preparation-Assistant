
import streamlit as st
from html import escape
from generator import generate_interview



# -------------------- PAGE CONFIGURATION --------------------

st.set_page_config(
    page_title="AI Placement Preparation Assistant",
    page_icon="🎯",
    layout="wide"
)


# -------------------- DARK NAVY BLUE THEME --------------------

st.markdown("""
<style>

/* Main Background */
.stApp,
[data-testid="stMain"],
[data-testid="stAppViewContainer"] {
    background-color: #14213D !important;
    color: #E2E8F0 !important;
}

/* Keep Streamlit Header and Toolbar */
[data-testid="stHeader"] {
    background-color: transparent !important;
}

/* Main Content Text */
[data-testid="stMain"] h1,
[data-testid="stMain"] h2,
[data-testid="stMain"] h3,
[data-testid="stMain"] h4,
[data-testid="stMain"] p,
[data-testid="stMain"] li,
[data-testid="stMain"] label {
    color: #E2E8F0 !important;
}

/* Main Title */
.main-title {
    color: white !important;
    font-size: 34px;
    font-weight: 750;
    margin-bottom: 4px;
}

/* Subtitle */
.subtitle {
    color: #CBD5E1 !important;
    font-size: 16px;
    margin-bottom: 24px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #0B1730 !important;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* Buttons */
.stButton > button,
.stDownloadButton > button {
    background-color: #2563EB !important;
    color: white !important;
    border: none !important;
    border-radius: 8px;
    font-weight: 600;
    min-height: 40px;
}

/* Button Hover */
.stButton > button:hover,
.stDownloadButton > button:hover {
    background-color: #1D4ED8 !important;
}

/* Input Fields */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #1E3A5F !important;
    color: white !important;
    border: 1px solid #334E73 !important;
}

/* Select Boxes */
[data-baseweb="select"] {
    background-color: #1E3A5F !important;
    color: white !important;
}

/* Dropdown Menu */
[data-baseweb="popover"],
[data-baseweb="menu"] {
    background-color: #1E3A5F !important;
    color: white !important;
}

/* Question Expanders */
[data-testid="stExpander"] {
    background-color: #1E3A5F !important;
    border: 1px solid #334E73 !important;
    border-radius: 10px;
}

[data-testid="stExpander"] * {
    color: white !important;
}

/* Information Boxes */
[data-testid="stAlert"] {
    background-color: #1E3A5F !important;
    color: white !important;
}

/* Interview overview cards */
.overview-card {
    background: linear-gradient(145deg, #203F66, #1B3557);
    border: 1px solid #3B5B80;
    border-radius: 13px;
    padding: 18px 20px;
    min-height: 126px;
    height: 100%;
    box-sizing: border-box;
}

.overview-label {
    color: #C7D8EA;
    font-size: 0.92rem;
    font-weight: 600;
    margin-bottom: 12px;
}

.overview-value {
    color: #FFFFFF;
    font-size: clamp(1.35rem, 2vw, 2rem);
    font-weight: 700;
    line-height: 1.2;
    overflow-wrap: anywhere;
    word-break: normal;
}

.overview-meta {
    color: #A9BBD0;
    font-size: 0.84rem;
    margin-top: 8px;
}

/* Interview question category cards */
.category-card {
    background: #1B3557;
    border: 1px solid #355579;
    border-radius: 12px;
    padding: 16px;
    min-height: 112px;
    height: 100%;
    box-sizing: border-box;
}

.category-title {
    color: #F1F5F9;
    font-size: 0.98rem;
    font-weight: 650;
    margin-bottom: 13px;
    overflow-wrap: anywhere;
}

.category-track {
    width: 100%;
    height: 9px;
    background: #405875;
    border-radius: 999px;
    overflow: hidden;
    margin-bottom: 10px;
}

.category-fill {
    height: 100%;
    background: linear-gradient(90deg, #38BDF8, #3B82F6);
    border-radius: 999px;
}

.category-count {
    color: #B8C7D9;
    font-size: 0.84rem;
}

/* Section headings and spacing */
.section-heading {
    color: #F8FAFC;
    font-size: 1.65rem;
    font-weight: 750;
    margin: 8px 0 18px 0;
}

.section-subheading {
    color: #DCE7F3;
    font-size: 1.05rem;
    font-weight: 650;
    margin: 4px 0 14px 0;
}


/* Tables */
[data-testid="stTable"],
[data-testid="stDataFrame"] {
    background-color: #1E3A5F !important;
}

/* Code Blocks */
[data-testid="stCode"] {
    background-color: #0B1730 !important;
}

/* Links */
[data-testid="stMain"] a {
    color: #93C5FD !important;
}

/* Page Spacing */
.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Dividers */
hr {
    border-color: #334E73 !important;
}

/* Keep Default Streamlit Toolbar Visible */
[data-testid="stToolbar"] {
    visibility: visible !important;
}

</style>
""", unsafe_allow_html=True)


# -------------------- SESSION STATE --------------------

if "result" not in st.session_state:
    st.session_state.result = None

if "generation_time" not in st.session_state:
    st.session_state.generation_time = None

if "generated_settings" not in st.session_state:
    st.session_state.generated_settings = {}


# -------------------- SIDEBAR --------------------

with st.sidebar:

    st.markdown("# 🎯 Placement Assistant")
    st.caption("Technical Interview Preparation")

    st.divider()

    st.markdown("### Interview Settings")

    job_role = st.selectbox(
        "Job Role",
        [
            "Python Developer",
            "Java Developer",
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Analyst",
            "Data Scientist",
            "GenAI Engineer",
            "Backend Developer"
        ]
    )

    experience_level = st.selectbox(
        "Experience Level",
        [
            "Fresher",
            "0-1 Years",
            "1-3 Years",
            "3-5 Years"
        ]
    )

    difficulty = st.select_slider(
        "Difficulty",
        options=["Easy", "Medium", "Hard"],
        value="Medium"
    )

    num_questions = st.slider(
        "Number of Questions",
        min_value=3,
        max_value=15,
        value=5
    )

    st.divider()

    generate_button = st.button(
        "🚀 Generate Questions",
        type="primary",
        use_container_width=True
    )

    clear_button = st.button(
        "Clear Results",
        use_container_width=True
    )

    st.divider()



# -------------------- MAIN HEADER --------------------

st.markdown(
    '<div class="main-title">AI Placement Preparation Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Prepare for technical interviews with personalized questions, '
    'clear explanations and practical examples.'
    '</div>',
    unsafe_allow_html=True
)


# -------------------- GENERATE QUESTIONS --------------------

if generate_button:

    with st.spinner("Preparing your interview questions..."):

        try:
            result = generate_interview(
                job_role,
                experience_level,
                difficulty,
                num_questions
            )

            if not result or not result.questions:
                st.error(
                    "No questions were generated. Please try again."
                )

            else:
                st.session_state.result = result


                st.session_state.generated_settings = {
                    "difficulty": difficulty,
                    "num_questions": num_questions
                }

                st.success(
                    "Your interview questions are ready!"
                )

        except Exception as error:
            st.error(
                f"Question generation failed: {error}"
            )


# -------------------- CLEAR RESULTS --------------------

if clear_button:

    st.session_state.result = None
    st.session_state.generation_time = None
    st.session_state.generated_settings = {}

    st.rerun()


# -------------------- DISPLAY RESULTS --------------------

if st.session_state.result:

    result = st.session_state.result
    questions = result.questions

    saved_difficulty = st.session_state.generated_settings.get(
        "difficulty",
        difficulty
    )

    st.markdown(
        '<div class="section-heading">📊 Interview Overview</div>',
        unsafe_allow_html=True
    )

    # Custom cards prevent long job-role names from being cut off.
    overview_items = [
        ("Job Role", result.job_role),
        ("Experience", result.experience_level),
        ("Questions", str(len(questions))),
        ("Difficulty", saved_difficulty),
    ]

    overview_columns = st.columns(4, gap="medium")

    for column, (label, value) in zip(overview_columns, overview_items):
        with column:
            st.markdown(
                f"""
                <div class="overview-card">
                    <div class="overview-label">{escape(str(label))}</div>
                    <div class="overview-value">{escape(str(value))}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.divider()

    st.markdown(
        '<div class="section-heading">📝 Interview Questions</div>',
        unsafe_allow_html=True
    )

    # -------------------- QUESTION CATEGORIES --------------------

    question_types = {}

    for question in questions:

        question_type = question.question_type

        question_types[question_type] = (
            question_types.get(question_type, 0) + 1
        )

    if question_types:

        st.markdown(
            '<div class="section-subheading">Question Categories</div>',
            unsafe_allow_html=True
        )

        category_columns = st.columns(
            min(len(question_types), 4),
            gap="medium"
        )

        for index, (question_type, count) in enumerate(
            question_types.items()
        ):

            percentage = (count / len(questions)) * 100

            with category_columns[index % len(category_columns)]:
                st.markdown(
                    f"""
                    <div class="category-card">
                        <div class="category-title">{escape(str(question_type))}</div>
                        <div class="category-track">
                            <div class="category-fill"
                                 style="width: {percentage:.1f}%;">
                            </div>
                        </div>
                        <div class="category-count">
                            {count} question(s)
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.divider()

    # -------------------- DISPLAY QUESTIONS AND ANSWERS --------------------

    for index, question in enumerate(questions, start=1):

        difficulty_icons = {
            "Easy": "🟢",
            "Medium": "🟡",
            "Hard": "🔴"
        }

        difficulty_icon = difficulty_icons.get(
            question.difficulty,
            "🔵"
        )

        with st.expander(
            f"Q{index}. {question.question}"
        ):

            left, right = st.columns(2)

            with left:
                st.caption(
                    f"📌 Type: {question.question_type}"
                )

            with right:
                st.caption(
                    f"{difficulty_icon} Difficulty: "
                    f"{question.difficulty}"
                )

            st.markdown("#### Model Answer")
            st.markdown(question.model_answer)

            st.markdown("#### 💡 Simple Explanation")
            st.info(question.explanation)

            st.markdown("#### 💻 Practical Example")
            st.markdown(question.practical_example)

            st.markdown("#### 🔑 Important Keywords")

            keywords = question.keywords or []

            st.markdown(
                " · ".join(f"`{word}`" for word in keywords)
            )

            st.markdown("#### 🎤 Follow-up Question")
            st.warning(question.follow_up)

    # -------------------- DOWNLOAD RESULTS --------------------

    st.divider()

    markdown_content = (
        f"# AI Placement Preparation\n\n"
        f"**Job Role:** {result.job_role}\n\n"
        f"**Experience:** {result.experience_level}\n\n"
        f"**Difficulty:** {saved_difficulty}\n\n"

    )

    for index, question in enumerate(questions, start=1):

        markdown_content += f"""
---

## Q{index}. {question.question}

**Question Type:** {question.question_type}

**Difficulty:** {question.difficulty}

### Model Answer

{question.model_answer}

### Simple Explanation

{question.explanation}

### Practical Example

{question.practical_example}

### Important Keywords

{", ".join(question.keywords or [])}

### Follow-up Question

{question.follow_up}

"""

