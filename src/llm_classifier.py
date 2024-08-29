"""
This module interacts with an LLM API to create labels using predefined tasks.
"""

import pandas as pd
import google.generativeai as genai

DATA_PATH = "https://raw.githubusercontent.com/mickaeltemporao/workshop-ai-augmented-data/main/data/raw/us_pols_20.csv"
MODEL = "gemini-1.5-flash"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(MODEL)

response = model.generate_content("Peux-tu m'écrire une histoire fantastique en 5 phrases?")
print(response.text)


def run_task(task, content):
    model=genai.GenerativeModel(
      model_name="gemini-pro",
      system_instruction=task
    )
    response = model.generate_content(
        content,
        generation_config=genai.types.GenerationConfig(
            candidate_count=1,
            stop_sequences=['x'],
            max_output_tokens=10,
            temperature=0.7,
        )
    )
    output = response.text
    return output


def make_content(obs):
    return f"""Account name: {obs.name}
Account description: {obs['description']}
"""


def find_file():
    try:
        tmp_df = pd.read_csv(OUTPUT_FILE_PATH, index_col='username')
        print("Resuming from previous file.")
    except FileNotFoundError:
        df = pd.read_csv(DATA_PATH)
        df = df.dropna(subset=['username', 'description']).set_index('username')
        df['description'].to_csv(OUTPUT_FILE_PATH)
        tmp_df = df[['description']].copy()
        print("New output filed created!")
    return tmp_df


def main():

    for task in src.tasks.task_main:
        print(f"Starting {task}")
        newcol = f'task_{task}'

        if newcol not in tmp_df.columns:
            tmp_df[newcol] = "NONE"

        for i, j in tmp_df.iterrows():
            if tmp_df.loc[j.name, newcol] != "NONE":
                continue
            print(f"Running task for {j.name}")
            task_output = run_task(
                src.tasks.task_main[task],
                make_content(j)
            )

            tmp_df.loc[j.name, newcol] = task_output

            tmp_df.to_csv(OUTPUT_FILE_PATH)
            print("Filed Saved")

