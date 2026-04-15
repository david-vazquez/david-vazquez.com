---
title: 'AgentAda: Skill-Adaptive Data Analytics for Tailored Insight Discovery'
date: '2025-01-01'
draft: false
authors:
  - Amirhossein Abaskohi
  - Amrutha Varshini Ramesh
  - Shailesh Nanisetty
  - Chirag Goel
  - David Vázquez
  - Christopher Pal
  - Spandana Gella
  - Giuseppe Carenini
  - Issam H Laradji
publication_types:
  - 'paper-conference'
publication: '*Workshop at Association for Computational Linguistics (ACL)*'
abstract: 'We introduce AgentAda, the first LLM-powered analytics agent that can learn and use new analytics skills to extract more specialized insights. Unlike existing methods that require users to manually decide which data analytics method to apply, AgentAda automatically identifies the skill needed from a library of analytical skills to perform the analysis. This also allows AgentAda to use skills that existing LLMs cannot perform out of the box. The library covers a range of methods, including clustering, predictive modeling, and NLP techniques like BERT, which allow AgentAda to handle complex analytics tasks based on what the user needs. AgentAda''s dataset-to-insight extraction strategy consists of three key steps: a (I) question generator to generate queries relevant to user''s goal and persona, a (II) hybrid Retrieval-Augmented Generation (RAG)-based skill matcher to choose the best data analytics skill from the skill library, and a (III) code generator that produces executable code based on the retrieved skill''s documentation to extract key patterns. We also introduce KaggleBench, a benchmark of curated notebooks across diverse domains, to evaluate AgentAda''s performance. We conducted a human evaluation demonstrating that AgentAda provides more insightful analytics than existing tools, with 48.78% of evaluators preferring its analyses, compared to 27.67% for the unskilled agent. We also propose a novel LLM-as-a-judge approach that we show is aligned with human evaluation as a way to automate insights'' quality evaluation at larger scale.'
featured: false

links:
  - name: arXiv
    url: 'https://arxiv.org/pdf/2504.07421'
image:
  focal_point: ''
  preview_only: false
---
