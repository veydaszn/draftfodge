def generate_draft(topic: str, tone: str) -> str:
    return f"""
Title: {topic}

Introduction:
This article discusses {topic} in a {tone} tone.

Main Points:
1. Definition and background of {topic}
2. Importance and real-world applications
3. Key challenges and solutions
4. Future outlook

Conclusion:
{topic} continues to be relevant and impactful in today's world.
"""
