import os
from crewai import Agent, Crew, Process, Task

# Ensure OpenAI API key is read from the environment variable
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(
        "OPENAI_API_KEY environment variable is not set. Please set it before running the script."
    )


def main():
    # Ask the user for a city
    city = input("Enter a city to plan a trip for: ").strip()

    if not city:
        print("No city provided. Exiting.")
        return

    # 1. Define the Travel Planner Agent
    travel_planner = Agent(
        role="Expert Travel Guide and Local Explorer",
        goal="Provide top-tier, tailored travel recommendations for cities around the world.",
        backstory=(
            "You are a seasoned travel enthusiast who has spent over a decade exploring hidden "
            "gems, cultural highlights, and iconic spots across major global cities. Your specialty "
            "is crafting bite-sized, memorable itineraries that give visitors a authentic feel for a city."
        ),
        verbose=True,
    )

    # 2. Define the Travel Planning Task
    travel_task = Task(
        description=(
            f"Identify and describe exactly 3 must-visit places in {city}. For each place, include "
            "its name, a short explanation of why it is worth visiting, and a quick practical tip for travelers."
        ),
        expected_output=(
            "A bulleted list featuring exactly 3 locations. Each entry must have:\n"
            "1. Place Name\n"
            "2. Overview (2-3 sentences)\n"
            "3. Travel Tip"
        ),
        agent=travel_planner,
    )

    # 3. Assemble the Crew
    crew = Crew(
        agents=[travel_planner],
        tasks=[travel_task],
        process=Process.sequential,
        verbose=True,
    )

    # 4. Run the Crew and Print the Result
    print(f"\n--- Running Travel Planner Crew for: {city} ---\n")
    result = crew.kickoff()

    print("\n================ FINAL RESULT ================\n")
    print(result)


if __name__ == "__main__":
    main()