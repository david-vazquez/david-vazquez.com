---
title: 'Improving Generalization in Task-Oriented Dialogues with Workflows and Action Plans'
date: '2023-01-01'
draft: false
authors:
  - Stefania Raimondo
  - Christopher Pal
  - Xiaotian Liu
  - David Vázquez
  - Hector Palacios
publication_types:
  - 'paper-conference'
publication: '*Conference on Empirical Methods in Natural Language Processing (EMNLP)*'
abstract: 'Task-oriented dialogue is difficult in part because it involves understanding user intent, collecting information from the user, executing API calls, and generating helpful and fluent responses. However, for complex tasks one must also correctly do all of these things over multiple steps, and in a specific order. While large pre-trained language models can be fine-tuned end-to-end to create multi-step task-oriented dialogue agents that generate fluent text, our experiments confirm that this approach alone cannot reliably perform new multi-step tasks that are unseen during training. To address these limitations, we augment the dialogue contexts given to text2text transformers with known valid workflow names and action plans. Action plans consist of sequences of actions required to accomplish a task, and are encoded as simple sequences of keywords (e.g. verify-identity, pull-up-account, reset-password, etc.). We perform extensive experiments on the Action-Based Conversations Dataset (ABCD) with T5-small, base and large models, and show that such models: a) are able to more readily generalize to unseen workflows by following the provided plan, and b) are able to generalize to executing unseen actions if they are provided in the plan. In contrast, models are unable to fully accomplish new multi-step tasks when they are not provided action plan information, even when given new valid workflow names.'
featured: false

links:
  - name: arXiv
    url: 'https://arxiv.org/pdf/2306.01729'
---
