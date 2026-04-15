---
title: 'BigCharts-R1: Enhanced Chart Reasoning with Visual Reinforcement Finetuning'
date: '2025-01-01'
draft: false
authors:
  - Ahmed Masry
  - Abhay Puri
  - Masoud Hashemi
  - Juan A Rodriguez
  - Megh Thakkar
  - Khyati Mahajan
  - Vikas Yadav
  - Sathwik Tejaswi Madhusudhan
  - Alexandre Piché
  - Dzmitry Bahdanau
  - others
publication_types:
  - 'paper-conference'
publication: '*Conference on Language Modeling (COLM)*'
abstract: 'Charts are essential to data analysis, transforming raw data into clear visual representations that support human decision-making. Although current vision-language models (VLMs) have made significant progress, they continue to struggle with chart comprehension due to training on datasets that lack diversity and real-world authenticity, or on automatically extracted underlying data tables of charts, which can contain numerous estimation errors. Furthermore, existing models only rely on supervised fine-tuning using these low-quality datasets, severely limiting their effectiveness. To address these issues, we first propose BigCharts, a dataset creation pipeline that generates visually diverse chart images by conditioning the rendering process on real-world charts sourced from multiple online platforms. Unlike purely synthetic datasets, BigCharts incorporates real-world data, ensuring authenticity and visual diversity, while still retaining accurate underlying data due to our proposed replotting process. Additionally, we introduce a comprehensive training framework that integrates supervised fine-tuning with Group Relative Policy Optimization (GRPO)-based reinforcement learning. By introducing novel reward signals specifically designed for chart reasoning, our approach enhances model robustness and generalization across diverse chart styles and domains, resulting in a state-of-the-art chart reasoning model, BigCharts-R1. Extensive experiments demonstrate that our models surpass existing methods on multiple chart question-answering benchmarks compared to even larger open-source and closed-source models.'
featured: false

links:
  - type: 'video'
    url: 'https://www.youtube.com/watch?v=vN_KsGTzh4E'
  - type: 'pdf'
    url: 'https://arxiv.org/pdf/2508.09804'
---
