def build_prompt(data):
    return f"""
You are an expert SEO content writer.

Your goal is to generate a HIGH-QUALITY, HUMAN-LIKE, SEO-OPTIMIZED blog.

PRIMARY KEYWORD: {data['primary']}
SECONDARY KEYWORDS: {", ".join(data['secondary'])}

================ STRUCTURE =================

# Blogy – Best AI Blog Automation Tool in India

## What is {data['primary']}?
Write 50–60 words.
- Clear and direct definition
- Include primary keyword naturally

## Introduction
Write 150–200 words.
- Start engaging (hook)
- Use primary keyword in first paragraph
- Explain context and importance

## Why It Matters
Write 150–200 words.
- Explain why this tool is important
- Mention SEO, automation, and growth

## Key Features

### Core Features
- Write 6 bullet points
- Each bullet should be descriptive (10–15 words)

### Advanced Features
- Write 4 bullet points
- Slightly more advanced capabilities

## Benefits
- Write 6 bullet points
- Focus on outcomes (traffic, efficiency, growth)

## Comparison with Other Tools
Write 200 words.
- Compare Blogy with competitors
- Highlight uniqueness and advantages

## SERP Gap Analysis
Write 150 words.
- Explain what competitors are missing
- Show how Blogy fills that gap

## Internal Linking Suggestions
- Write exactly 3 bullet anchor texts

## FAQs
Write 5 questions and answers.
- Keep answers concise but helpful

## Conclusion
Write 150–200 words.
- Summarize key points
- Reinforce Blogy’s value

## CTA
Write 100 words.
- Strong persuasive call-to-action
- Encourage users to try Blogy

================ RULES =================

- Use proper markdown headings (#, ##, ###)
- DO NOT write plain text headings
- Total word count MUST be 1200+
- Use the primary keyword in EVERY major section (Introduction, Features, Benefits, Conclusion) 
Ensure total usage is 12–15 times naturally across the blog
- Maintain keyword density around 0.8–1.2%
- Use medium-length sentences (10–18 words)
- Break long paragraphs into smaller ones
- Avoid repetition of phrases
- Write like a human expert (NOT robotic)
- Ensure readability score between 40–60
- Keep sentences medium length (10–16 words)
- Avoid very long sentences
- Break large paragraphs into smaller ones

"""