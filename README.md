# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->
My system focuses on campus dining reviews at the University of Illinois Chicago (UIC), providing students with honest, experience-based insights that are not available on official university websites. By gathering feedback from sources such as Reddit, Yelp, and other review platforms, it centralizes student opinions on food quality, pricing, portion sizes, and meal plan value in one place.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | r/uichicago, dining hall food quality | Reddit thread | https://www.reddit.com/r/uichicago/comments/vpdzh1/how_is_the_dining_hall_food/ |
| 2 | r/uichicago — portion sizes and reactions | Reddit thread | https://www.reddit.com/r/uichicago/comments/1idebe4/i_just_have_to_laugh_uic_dining/ |
| 3 | r/uichicago, dining hall menu | Reddit thread | https://www.reddit.com/r/uichicago/comments/1fn1kxn/dining_hall_menu/ |
| 4 | r/uichicago, how dining works | Reddit thread | https://www.reddit.com/r/uichicago/comments/ifvi9y/dining_service_stupid_question_how_does_it_work/ |
| 5 | UIC Student Center West Food Court | Yelp reviews | https://www.yelp.com/biz/uic-student-center-west-food-court-chicago |
| 6 | UIC Dining official site | University website | https://dining.uic.edu/ |
| 7 | UIC Student Centers about page | University website | https://studentcenters.uic.edu/about/ |
| 8 | RestaurantGuru, UIC food court | Review aggregator | https://restaurantguru.com/UIC-Student-Center-West-Food-Court-Chicago |
| 9 | Novacircle, UIC food court | Review aggregator | https://www.novacircle.com/spots/north-america/united-states/illinois/chicago/chicago-il/uic-student-center-west-food-court-8db8f8 |
| 10 | Sodexo UIC Dining homepage | Official dining site | https://uicdining.sodexomyway.com/en-us/ |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:** 300 - 600 tokens

**Overlap:** 50 - 100 tokens

**Why these choices fit your documents:** Most source documents are Reddit threads and short reviews, so a chunk size of 300–600 tokens is sufficient to capture complete opinions without breaking them apart. A 50–100 token overlap helps preserve context and ensures important information is retained between chunks.

**Final chunk count:** 64 chunks across 10 source documents

---

## Sample Chunks

**Chunk 1 — Source: reddit3.txt**
> "Reddit r/uichicago Topic: dining hall menu? User: is there any way to check the menu on the dining hall food online? i've gone on the uic food website that details the different restaurants, but when you click the link under the dining hall that is labeled 'menu' the screen displays an error message."
 
**Chunk 2 — Source: reddit3.txt**
> "i've also seen in the dining hall they advertise the ability to check the menu on an app called 'everyday' or something like that, and i downloaded the app and there's no way to do that at all. User: The new app sucks. I dont know why they switched but it's annoying. User: It's https://everyday.dynamify.com/store/21236 I don't know why they haven't fixed the link on the website."
 
**Chunk 3 — Source: reddit4.txt**
> "Reddit r/uichicago Topic: Dining service (stupid) question: how does it work? User: Hi guys! I'm an international student and I know nothing about the dining system at UIC. I just wanted to know how does it work in general. For instance, I would like to do the 15 meals/week plan to go there every day for lunch and dinner."
 
**Chunk 4 — Source: reddit4.txt**
> "Let's say that I did it: where should I go to eat? I've seen a lot of locations on the website (Subway, Starbucks...): do they work all in the same way or is there a specific location to use the meal plan and, for instance, to eat at all the other places I have to use the Flames Fare?"
 
**Chunk 5 — Source: reddit4.txt**
> "So there are 2 main dining halls at UIC: the dining hall at James J. Stukel Towers, and the dining hall at Student Center East. Both of them have menus that can be found online. Note that the menu may vary slightly from what is listed, but there are enough options to find something you like. These are the two locations where you can use your meal plan."


---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:** all-MiniLM-L6-v2 via sentence-transformers

**Production tradeoff reflection:** I chose all-MiniLM-L6-v2 because it is fast, runs locally without an API key, and performs well on short review-style text. For larger-scale deployments, more powerful models could improve retrieval accuracy, while multilingual or fine-tuned models may better support diverse users and domain-specific content.

---
## Retrieval Test Results
 
**Query 1: How does the UIC meal plan system work?**
 
| Rank | Source | Distance | Preview |
|------|--------|----------|---------|
| 1 | reddit4.txt | 0.5222 | "Reddit r/uichicago Topic: Dining service (stupid) question: how does it work? User: Hi guys! I'm an international student and I know nothing about the dining system at UIC..." |
| 2 | Website.1.txt | 0.7093 | "UIC Dining Services Overview — UIC Dining Services provides a variety of dining options for students, faculty, and staff across campus. Dining Services Include: Dining Halls, Retail Dining Locations..." |
| 3 | Website5.txt | 0.7683 | "Additional Services: UIC Dining supports catering, food trucks, Grubhub ordering, nutrition education, special dietary accommodations, and campus dining events..." |
 
---
 
**Query 2: What are common complaints about UIC dining?**
 
| Rank | Source | Distance | Preview |
|------|--------|----------|---------|
| 1 | reddit4.txt | 0.8004 | "Reddit r/uichicago Topic: Dining service (stupid) question: how does it work? User: Hi guys! I'm an international student and I know nothing about the dining system at UIC..." |
| 2 | Website3.txt | 0.8407 | "Review: UIC west Student union — dining options like Subway, pizza, salad, sandwich, smoothie. Review: Huge variety of places..." |
| 3 | Website4.txt | 0.8480 | "Here, you'll see different kinds of food like Vietnamese, Chinese, pizza, and burgers. It's a favorite quick meal spot in the Medical District area..." |
---
 
**Query 3: What do students say about portion sizes in UIC dining halls?**
 
| Rank | Source | Distance | Preview |
|------|--------|----------|---------|
| 1 | Website.1.txt | 0.8399 | "UIC Dining Services Overview — UIC Dining Services provides a variety of dining options for students, faculty, and staff across campus..." |
| 2 | Website5.txt | 0.8422 | "Additional Services: UIC Dining supports catering, food trucks, Grubhub ordering, nutrition education, special dietary accommodations..." |
| 3 | reddit4.txt | 0.8605 | "So there are 2 main dining halls at UIC: the dining hall at James J. Stukel Towers, and the dining hall at Student Center East. Both of them have menus that can be found online..." |

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:** You are a helpful assistant that answers questions about UIC campus dining.
Answer the question using ONLY the information provided in the context below.
If the context does not contain enough information to answer the question, say:
"I don't have enough information on that in my documents."
Do NOT use any outside knowledge. Always cite which source document(s) your answer came from.

**How source attribution is surfaced in the response:** The system tracks source filenames for all retrieved chunks and includes them in the context provided to the model. These filenames are used for citation within responses and are also collected separately by the application, allowing the interface to display a dedicated list of sources in a "Retrieved from" section below each answer.

---
## Example System Responses
 
**Response 1 — In scope:**
 
> **Question:** How does the UIC meal plan system work?
>
> **Answer:** The UIC meal plan system works by granting students access to campus dining halls and other dining services through the purchase of meal plans (source: Website.1.txt). A "meal swipe" refers to the swipes used to enter the dining halls (source: Website.1.txt). Students can purchase meal plans, such as the 15 meals/week plan, to use at the dining halls (source: reddit4.txt). The meal plans can be used at the two main dining halls, located at James J. Stukel towers and Student Center east, which have menus available online (source: reddit4.txt). Additionally, students can use their meal plans at other dining locations and can manage their dining experience through mobile applications, such as viewing menus and nutrition information (source: Website5.txt, Website.1.txt).
>
> **Retrieved from:** reddit4.txt, Website.1.txt, Website5.txt
---
 
**Response 2 — In scope:**
 
> **Question:** What do students say about the variety of food options at UIC dining halls?
>
> **Answer:** According to the sources, students have expressed positive opinions about the variety of food options at UIC dining halls. One user on Reddit (source: reddit4.txt) mentioned that "there are enough options to find something you like" at the two main dining halls. Additionally, a review on Website3.txt stated that there is a "Huge variety of places to eat" and another review mentioned that the "Food is wonderful". However, one review also noted that the prices are too high for the quality of the food (source: Website3.txt).
>
> **Retrieved from:** Website4.txt, Website5.txt, reddit4.txt, Website3.txt
 
---
 
**Response 3 — Out of scope (refusal):**
 
> **Question:** Which UIC dining location is rated best for food quality?
>
> **Answer:** I don't have enough information on that in my documents.
>
> **Retrieved from:** Website4.txt, reddit4.txt, Website3.txt



---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | Which UIC dining location is rated best for food quality? | UIC dining hall is highest rated | "I don't have enough information on that in my documents." | Off-target | Inaccurate |
| 2 | What do students say about portion sizes in UIC dining halls? | Portions are small or inconsistent | "I don't have enough information on that in my documents." | Off-target | Inaccurate |
| 3 | What do students say about the variety of food options at UIC dining halls? | Students appreciate variety but menus get repetitive | Students noted a huge variety of places to eat and wonderful food, but prices are high for the quality; enough options to find something you like (source: Website3.txt, reddit4.txt) | Relevant | Partially accurate |
| 4 | How does the UIC meal plan system work? | Meal swipes, i-card, all-you-care-to-eat, Flames Fare | Explained meal swipes, 15 meals/week plan, two main dining halls at Stukel Towers and Student Center East, Everyday App for menus (source: Website1.txt, reddit4.txt) | Relevant | Accurate |
| 5 | What are common complaints about UIC dining? | Repetitive menus, bland food, limited weekend hours | High prices for food quality; mixed opinions on food quality and service (source: Website3.txt, Website4.txt) | Partially relevant | Partially accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:** "Which UIC dining location is rated best for food quality?" and "What do students say about portion sizes in UIC dining halls?"

**What the system returned:** "I don't have enough information on that in my documents." for both questions.

**Root cause (tied to a specific pipeline stage):** The failure likely occurred during the chunking and retrieval stages. Reviews discussing dining locations and portion sizes may have been split across multiple chunks, causing important context to be separated. Since all-MiniLM-L6-v2 generates embeddings at the chunk level, fragments without explicit references to portions or locations were less likely to match the query. This reduced their retrieval ranking, even if the full review was relevant.

**What you would change to fix it:** Retrieval could be improved by increasing chunk size so each embedding captures more context. Adding more reviews for specific dining locations would provide better coverage of user queries.

---
## Query Interface
 
The interface is built with Gradio and runs locally at http://localhost:7860.
 
**Input:**
- *Your question*: a text box where the user types a free-form question about UIC campus dining
**Output:**
- *Answer*: displays the LLM's grounded response with source filenames cited inline
- *Retrieved from*: lists the source documents that were retrieved to generate the answer

**Sample interaction transcript:**
  
> **Input:** How does the UIC meal plan system work?

> **Output:** The UIC meal plan system works by granting students access to campus dining halls and other dining services through the purchase of meal plans (source: Website.1.txt). A "meal swipe" refers to the swipes used to enter the dining halls (source: Website.1.txt). Students can purchase meal plans, such as the 15 meals/week plan, to use at the dining halls (source: reddit4.txt). The meal plans can be used at the two main dining halls, located at James J. Stukel towers and Student Center east, which have menus available online (source: reddit4.txt). Additionally, students can use their meal plans at other dining locations and can manage their dining experience through mobile applications, such as viewing menus and nutrition information (source: Website5.txt, Website.1.txt).
>
> **Retrieved from:** reddit4.txt, Website.1.txt, Website5.txt

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:** The Retrieval Approach section in planning.md made implementation easier by defining the embedding model and retrieval settings upfront. Choosing all-MiniLM-L6-v2 and top-k=5 before coding reduced decision-making during development. It also provided a clear specification for generating retrieval code with minimal revisions.


**One way your implementation diverged from the spec, and why:** Although the specification targeted chunk sizes of 300–600 tokens, the final chunks were often smaller because the source documents consisted mainly of short Reddit posts and review snippets. Keeping these chunks separate preserved individual opinions and context.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:* I provided the Retrieval Approach section from planning.md, my pipeline diagram, and the structure of chunks.json. I specifically asked the AI to implement the embedding stage using SentenceTransformer to store embeddings in ChromaDB with source metadata, and create a retrieval function that returned the top-k chunks with distance scores.
- *What it produced:* A embed_and_retrieve.py script that loaded chunks, embedded them with all-MiniLM-L6-v2, stored them in ChromaDB, and ran all 5 evaluation queries with distance scores and chunk previews.
- *What I changed or overrode:* The initial script caused a DuplicateIDError because multiple source files used the same sequential chunk IDs starting from 0. To fix this, document IDs were made unique by combining the source filename with the chunk ID. For example, a chunk ID was changed to a format like `reddit4.txt_0`.

**Instance 2**

- *What I gave the AI:* The implementation was guided by the `retrieval.py` code, the Architecture section of planning.md, and the requirement that all responses be grounded in retrieved documents.
- *What it produced:* query.py with a system prompt enforcing grounded generation and app.py with a Gradio interface showing answer and source fields.
- *What I changed or overrode:* The generated code initially used `client` for both the Groq API and ChromaDB objects, creating a naming conflict. I resolved this by renaming the Groq object to `groq_client`. I also replaced `load_dotenv(dotenv_path=...)` with `load_dotenv()` after finding that the path-based version was not correctly locating the `.env` file on my system.

