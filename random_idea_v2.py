import random

def generate_python_idea(difficulty):
    easy_ideas = [
        "Create a To-Do List application",
        "Build a simple calculator",
        "Design a password generator",
        "Develop a weather app using an API",
        "Make a basic chatbot",
    ]

    intermediate_ideas = [
        "Implement a file management system",
        "Create a web scraper",
        "Build a URL shortener",
        "Design a quiz game",
        "Develop a budget tracker",
    ]

    advanced_ideas = [
        "Implement a cryptocurrency tracker",
        "Create a program to analyze text sentiment",
        "Develop a simple web server",
        "Design a recipe book application",
        "Build a basic content management system (CMS)",
    ]

    if difficulty == "easy":
        return random.choice(easy_ideas)
    elif difficulty == "intermediate":
        return random.choice(intermediate_ideas)
    elif difficulty == "advanced":
        return random.choice(advanced_ideas)
    else:
        return "Invalid difficulty level. Please choose 'easy', 'intermediate', or 'advanced'."

if __name__ == "__main__":
    print("Choose the difficulty level: 'easy', 'intermediate', or 'advanced'")
    user_choice = input().lower()

    idea = generate_python_idea(user_choice)
    print("\nYour randomly assigned Python project idea is:")
    print(idea)
