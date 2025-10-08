

from transformers import pipeline

# Load a pre-trained summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Example
text = """
Compassion literally means “to suffer together.” Among emotion researchers, it is defined as the feeling that arises when you are confronted with another’s suffering and feel motivated to relieve that suffering.

Compassion is not the same as empathy or altruism, though the concepts are related. While empathy refers more generally to our ability to take the perspective of and feel the emotions of another person, compassion is when those feelings and thoughts include the desire to help. Altruism, in turn, is the kind, selfless behavior often prompted by feelings of compassion, though one can feel compassion without acting on it, and altruism isn’t always motivated by compassion.
"""

# Generating
summary = summarizer(text, max_length=80, min_length=30, do_sample=False)

print("📝 Original Text:\n", text)
print("\n🔍 Summary:\n", summary[0]['summary_text'])
