from src.model_loader import generate_summary

sample_text = """
Artificial intelligence (AI) is intelligence demonstrated by machines, 
in contrast to the natural intelligence displayed by humans and animals.
"""

summary = generate_summary(sample_text)
print("Summary:", summary)