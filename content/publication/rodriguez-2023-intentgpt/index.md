---
title: 'IntentGPT: Few-Shot Intent Discovery with Large Language Models'
date: '2023-01-01'
draft: false
authors:
  - Juan A Rodriguez
  - Nicholas Botzer
  - David Vázquez
  - Christopher Pal
  - Marco Pedersoli
  - Issam H Laradji
publication_types:
  - 'paper-conference'
publication: '*Workshop at International Conference on Learning Representations (ICLR)*'
abstract: 'In today''s digitally driven world, dialogue systems play a pivotal role in enhancing user interactions, from customer service to virtual assistants. In these dialogues, it is important to identify user''s goals automatically to resolve their needs promptly. This has necessitated the integration of models that perform Intent Detection. However, users'' intents are diverse and dynamic, making it challenging to maintain a fixed set of predefined intents. As a result, a more practical approach is to develop a model capable of identifying new intents as they emerge. We address the challenge of Intent Discovery, an area that has drawn significant attention in recent research efforts. Existing methods need to train on a substantial amount of data for correctly identifying new intents, demanding significant human effort. To overcome this, we introduce IntentGPT, a novel training-free method that effectively prompts Large Language Models (LLMs) such as GPT-4 to discover new intents with minimal labeled data. IntentGPT comprises an In-Context Prompt Generator which generates informative prompts for In-Context Learning, an Intent Predictor for classifying and discovering user intents from utterances, and a Semantic Few-Shot Sampler that selects relevant few-shot examples and a set of known intents to be injected into the prompt. Our experiments show that IntentGPT outperforms previous methods that require extensive domain-specific data and fine-tuning, in popular benchmarks, including CLINC and BANKING, among others.'
featured: false

links:
  - type: code
    url: 'https://github.com/joanrod/IntentGPT'
  - name: arXiv
    url: 'https://arxiv.org/pdf/2411.10670'
---
