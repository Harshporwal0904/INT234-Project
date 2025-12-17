import pandas as pd

# Load dataset
df = pd.read_csv('clean_dataset.csv')

# ---- STEP 1: Rename columns (clean + professional names) ----
rename_map = {
    "How often do you use AI tools (ChatGPT, Gemini, Copilot, etc.)?": "AI_Usage_Freq",
    "For what task do you mostly use AI?": "AI_Task_Type",
    "How confident are you in understanding how AI tools work?": "AI_Confidence",
    "How willing are you to adopt new AI tools in the future?": "Willingness_To_Adopt",
    "How much time do you think AI saves you daily?": "Time_Saved_Daily",
    "How useful do you find AI in improving your learning or productivity?": "AI_Usefulness",
    "Do you feel comfortable relying on AI-generated recommendations?": "Comfort_Using_AI",
    "How often do you rely on AI when you get stuck instead of thinking on your own first?": "Rely_On_AI",
    "If AI tools were unavailable for a day, how difficult would your work/studies become?": "Difficulty_Without_AI",
    "Do you feel dependent on AI for completing academic tasks?": "Feeling_Dependent",
    "How frequently do you double-check AI-generated answers?": "Trust_Accuracy",
    "How much do you trust the accuracy of AI-generated content?": "Trust_Accuracy_AI",
    "Do you believe AI may reduce your problem-solving or critical-thinking skills over time?": "Thinks_AI_Reduces_Skills"
}

df = df.rename(columns=rename_map)

# ---- STEP 2: Remove leakage columns ----
leak_cols = [
    "Rely_On_AI",
    "Feeling_Dependent",
    "Difficulty_Without_AI"
]

df = df.drop(columns=leak_cols)

# ---- STEP 3: Save ONE final cleaned dataset ----
output_path = "final_clean_dataset.csv"
df.to_csv(output_path, index=False)

output_path
