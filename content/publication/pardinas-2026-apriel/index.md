---
title: 'Apriel-1.5-OpenReasoner: RL Post-Training for General-Purpose and Efficient Reasoning'
date: '2026-01-01'
draft: false
authors:
  - Rafael Pardinas
  - Ehsan Kamalloo
  - David Vázquez
  - Alexandre Drouin
publication_types:
  - 'manuscript'
publication: '*arXiv preprint arXiv:2604.02007*'
abstract: 'Building general-purpose reasoning models using reinforcement learning with verifiable rewards (RLVR) across diverse domains has been widely adopted by frontier open-weight models. However, their training recipes and domain mixtures are often not disclosed. Joint optimization across domains poses significant challenges: domains vary widely in rollout length, problem difficulty and sample efficiency. Further, models with long chain-of-thought traces increase inference cost and latency, making efficiency critical for practical deployment. We present Apriel-1.5-OpenReasoner, trained with a fully reproducible multi-domain RL post-training recipe on Apriel-Base, a 15B-parameter open-weight LLM, across five domains using public datasets: mathematics, code generation, instruction following, logical puzzles and function calling. We introduce an adaptive domain sampling mechanism that preserves target domain ratios despite heterogeneous rollout dynamics, and a difficulty-aware extension of the standard length penalty that, with no additional training overhead, encourages longer reasoning for difficult problems and shorter traces for easy ones. Trained with a strict 16K-token output budget, Apriel-1.5-OpenReasoner generalizes to 32K tokens at inference and improves over Apriel-Base on AIME 2025, GPQA, MMLU-Pro, and LiveCodeBench while producing 30-50% shorter reasoning traces. It matches strong open-weight models of similar size at lower token cost, thereby pushing the Pareto frontier of accuracy versus token budget.'
featured: false
links:
  - type: code
    url: 'https://github.com/ServiceNow/apriel'
  - name: arXiv
    url: 'https://arxiv.org/pdf/2604.02007'
---
