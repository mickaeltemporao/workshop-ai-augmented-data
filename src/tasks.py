def make_task(task_text):
    return f"""
        You are an unbiased US politics expert.
        You will be provided with a Twitter account name and description.
        Your task is to classify the account into one of the following numbered categories:
        {task_text}
        For each of these categories, I have provided a short description to help you with your choice. 
        Your output consists only of the number of the selected category, that is the number before the description provided.
    """


task_main = {
    "ideology": make_task(
        """
        1. Left wing accounts are those that express political views and opinions or include content that focuses on issues of income equality, environmental protection, social justice, open borders, progressive policies to promote minority representation;
        2. Centre accounts are those that express political views that mix or combine left and right opinion and content such that one opinion or type of content does not dominate;
        3. Right wing accounts are those that express political views and opinions or include content that focuses on issues of economic liberalism, less state intervention in citizens lives, lower taxes, controlling borders and immigration);
        4. Non-partisan accounts are those that typically do not express political views or contain any political content;
        """
    ),
    "age": make_task(
        """
        1. 18-24 Early adulthood, references to college, social media trends, youth culture.
        2. 25-34: Early career stage, potential references to career growth, early family life, pop culture.
        3. 35-44: Mid-career, family-oriented topics, more established professional references.
        4. 45-54: Experienced career stage, references to leadership roles, mature pop culture.
        5. 55-64: Pre-retirement stage, discussions about retirement, long-term career, older family dynamics.
        6. 65+: Retirement, senior living, nostalgia, grandparenting.
        0. Unclassifiable/Insufficient Information.
        """
    ),
    "gender": make_task(
        """
        1. Male: Masculine language, traditional male-dominated interests or references.
        2. Female: Feminine language, topics or references more common among women.
        3. Non-binary/Genderqueer: Non-gendered language, a mix of traditionally male and female references.
        0. Unclassifiable/Insufficient Information.
        """
    ),
    "education": make_task(
        """
        1. High School or Lower: Basic language use, common knowledge, fewer technical terms.
        2. Some College/Technical School: Intermediate language, some industry-specific terms or references.
        3. Undergraduate Degree: Advanced language, references to undergraduate-level education.
        4. Graduate Degree (Master’s, PhD): Complex language, use of specialized terminology, advanced concepts.
        5. Professional Certifications: Industry-specific jargon, focus on certification-related content.
        0. Unclassifiable/Insufficient Information.
        """
    ),
}
