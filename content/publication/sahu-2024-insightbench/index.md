---
title: 'InsightBench: Evaluating Business Analytics Agents through Multi-Step Insight Generation'
date: '2024-01-01'
draft: false
publishDate: '2026-04-08T13:35:27.412232Z'
authors:
- Gaurav Sahu
- Abhay Puri
- Juan Rodriguez
- Amirhossein Abaskohi
- Mohammad Chegini
- Alexandre Drouin
- Perouz Taslakian
- Valentina Zantedeschi
- Alexandre Lacoste
- David Vázquez
- ' others'
publication_types:
- '1'
abstract: 'Data analytics is essential for extracting valuable insights from data that can assist organizations in making effective decisions. We introduce InsightBench, a benchmark dataset with three key features. First, it consists of 100 datasets representing diverse business use cases such as finance and incident management, each accompanied by a carefully curated set of insights planted in the datasets. Second, unlike existing benchmarks focusing on answering single queries, InsightBench evaluates agents based on their ability to perform end-to-end data analytics, including formulating questions, interpreting answers, and generating a summary of insights and actionable steps. Third, we conducted comprehensive quality assurance to ensure that each dataset in the benchmark had clear goals and included relevant and meaningful questions and analysis. Furthermore, we implement a two-way evaluation mechanism using LLaMA-3 as an effective, open-source evaluator to assess agents'' ability to extract insights. We also propose AgentPoirot, our baseline data analysis agent capable of performing end-to-end data analytics. Our evaluation on InsightBench shows that AgentPoirot outperforms existing approaches (such as Pandas Agent) that focus on resolving single queries. We also compare the performance of open- and closed-source LLMs and various evaluation strategies. Overall, this benchmark serves as a testbed to motivate further development in comprehensive automated data analytics.'
featured: false
publication: '*International Conference on Learning Representations (ICLR)*'

links:
  - type: code
    url: 'https://github.com/ServiceNow/insight-bench'
  - name: arXiv
    url: 'https://arxiv.org/pdf/2407.06423'
---

