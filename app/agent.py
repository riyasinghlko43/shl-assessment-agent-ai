from app.retrieval import search_assessments


def generate_response(messages):

    user_message = messages[-1]["content"]

    print(f"\nUser Message: {user_message}")

    # vague query handling
    if len(user_message.split()) < 4:

        return {
            "reply": "Please provide more details about the role, skills, or experience level.",
            "recommendations": [],
            "end_of_conversation": False
        }

    # off-topic handling
    blocked_topics = [
        "salary",
        "legal",
        "lawsuit",
        "politics"
    ]

    for topic in blocked_topics:

        if topic in user_message.lower():

            return {
                "reply": "Sorry, I can only help with SHL assessment recommendations.",
                "recommendations": [],
                "end_of_conversation": False
            }

    # retrieve recommendations
    recommendations = search_assessments(user_message)

    return {
        "reply": f"I found {len(recommendations)} SHL assessments that match your requirements.",
        "recommendations": recommendations,
        "end_of_conversation": False
    }