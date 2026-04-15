---
title: 'XC-Cache: Cross-Attending to Cached Context for Efficient LLM Inference'
date: '2024-01-01'
draft: false
authors:
  - João Monteiro
  - Étienne Marcotte
  - Pierre-André Noël
  - Valentina Zantedeschi
  - David Vázquez
  - Nicolas Chapados
  - Christopher Pal
  - Perouz Taslakian
publication_types:
  - 'paper-conference'
publication: '*Advances in Neural Information Processing Systems (NeurIPS)*'
abstract: 'In-context learning approaches typically leverage prompting to condition decoder-only language model generation on reference information. Just-in-time processing of a context is inefficient due to the quadratic cost of self-attention operations, and caching is desirable. However, caching transformer states can easily require almost as much space as the model parameters. When the right context isn''t known in advance, caching ICL can be challenging. This work addresses these limitations by introducing models that, inspired by the encoder-decoder architecture, use cross-attention to condition generation on reference text without the prompt. More precisely, we leverage pre-trained decoder-only models and only train a small number of added layers. We use Question-Answering (QA) as a testbed to evaluate the ability of our models to perform conditional generation and observe that they outperform ICL, are comparable to fine-tuned prompted LLMs, and drastically reduce the space footprint relative to standard KV caching by two orders of magnitude.'
featured: false

links:
  - type: code
    url: 'https://github.com/ServiceNow/xc-cache'
  - name: arXiv
    url: 'https://arxiv.org/pdf/2404.15420'
image:
  focal_point: ''
  preview_only: false
---
