# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
 I chose campus dining reviews at University of Illinois Chicago(UIC). This information is valuable because it provides students with insights into dining options based on actual experiences, rather than solely relying on official menus and descriptions.  
---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | Reddit| This Reddit thread contains student opinions about overall dining hall food quality at UIC, including taste, variety, and consistency. It provides firsthand experiences that reflect general satisfaction and complaints about campus dining.
| https://www.reddit.com/r/uichicago/comments/vpdzh1/how_is_the_dining_hall_food/|
| 2 | Reddit| This post includes student reactions to portion sizes and perceived quality of dining hall meals.|https://www.reddit.com/r/uichicago/comments/1idebe4/i_just_have_to_laugh_uic_dining/ |
| 3 |Reddit |This thread discusses dining hall menus, availability of food options, and student opinions on meal variety. It also includes commentary on how consistent or reliable dining hall offerings are over time.
 | https://www.reddit.com/r/uichicago/comments/1fn1kxn/dining_hall_menu/|
| 4 |Reddit | This Reddit thread explains how UIC’s dining system operates, including meal swipes, dining hall access, and how students use their meal plans in practice.
It provides a practical, student-written explanation of dining logistics.
 |https://www.reddit.com/r/uichicago/comments/ifvi9y/dining_service_stupid_question_how_does_it_work/|
| 5 |Yelp reviews| This Yelp page contains user-generated reviews and ratings for the UIC Student Center West Food Court, including feedback on food quality, pricing, and wait times.
| https://www.yelp.com/biz/uic-student-center-west-food-court-chicago|
| 6 | UIC dining website| This official site provides information on dining halls, meal plans, menus, and operating hours. It serves as a factual reference for campus dining structure and available services.
|https://dining.uic.edu/|
| 7 |UIC website | This page describes the Student Center facilities including dining areas and food court locations.
It provides structural and logistical information about where dining services are located on campus. |https://studentcenters.uic.edu/about/|
| 8 |RestaurantGuru Website |This site aggregates reviews and ratings for the campus food court from multiple users.
It provides summarized opinions and keyword-based insights about food quality and service.
 | https://restaurantguru.com/UIC-Student-Center-West-Food-Court-Chicago|
| 9 | Novacircle Website| This page gives a summarized overview of the food court along with user impressions.
It includes general pros and cons based on visitor experiences and informal reviews.|https://www.novacircle.com/spots/north-america/united-states/illinois/chicago/chicago-il/uic-student-center-west-food-court-8db8f8 |
| 10 | Sodexo website| This page is the official UIC Dining Services homepage, providing an overview of campus dining options, locations, and meal plan information. | https://uicdining.sodexomyway.com/en-us/|

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:** 300 to 600 tokens

**Overlap:** 50 to 100 tokens

**Reasoning:** This size ensures that each segment concentrates on a single complete idea or review. It prevents the fragmentation of student opinions while maintaining manageable chunk sizes to optimize search accuracy across Reddit, Yelp, and official UIC pages.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:** all-MiniLM-L6-v2

**Top-k:** 5

**Production tradeoff reflection:** While more advanced models can better understand meaning, they tend to be more expensive and operate at slower speeds. This model offers a balance of speed and sufficient quality for short student reviews.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 |Which UIC dining location is rated best for food quality? |UIC dining hall is the highest rated for good food quality |
| 2 |What do students say about portion sizes in UIC dining halls? | Reviews mention portions are small or inconsistent depending on the location|
| 3 |What do students say about the variety of food options at UIC dining halls? | Students appreciate having multiple options, but many mention menus becoming repetitive over time. |
| 4 |How does the UIC meal plan system work? |It uses an i-card for all-you-care-to-eat meal swipes, retail meal exchanges, and Flames Fare cash. |
| 5 |What are common complaints about UIC dining? |Complaints center on repetitive menus, bland food quality, and limited weekend hours. |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Some reviews are very short and may not contain enough information for meaningful retrieval.

2. Important information may be split between chunks, causing the retriever to miss part of the context needed to answer a question completely.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->
![Architecture Diagram](images/Screenshot 2026-06-06 192300)
---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:** I will provide Claude with the Documents section, Chunking Strategy section, and the project requirements. I will ask it to generate Python code that loads text files from the data folder, cleans unnecessary formatting, and splits documents into chunks of 300–600 tokens with a 50–100 token overlap. I expect the output to be reusable Python functions for document loading and chunking. I will verify the code by running it on my UIC dining documents and manually inspecting the generated chunks to ensure they preserve complete ideas and maintain source information.

**Milestone 4 — Embedding and retrieval:** I will provide Calude with the Retrieval Approach section, Architecture diagram, and evaluation questions as input. I will ask it to generate code that creates embeddings using the all-MiniLM-L6-v2 model, stores them in ChromaDB, and retrieves the top five most relevant chunks for a query. I expect the output to include embedding generation, vector storage, and retrieval functions. I will verify the implementation by running my evaluation questions and checking whether the retrieved chunks are relevant and contain information needed to answer the queries.

**Milestone 5 — Generation and interface:** I will provide Claude with the Architecture section, Retrieval Approach, and project requirements as input. I will ask it to generate code that connects the retrieval system to a language model through the Groq API and creates a Gradio interface for users to submit questions. I expect the output to include prompt templates, API integration code, and a working interface. I will verify the implementation by testing all evaluation questions, comparing generated answers to the source documents, and ensuring that unsupported questions do not produce information that is not present in the retrieved context.



