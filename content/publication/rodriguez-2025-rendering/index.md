---
title: 'Rendering-Aware Reinforcement Learning for Vector Graphics Generation'
date: '2025-01-01'
draft: false
authors:
  - Juan A Rodriguez
  - Haotian Zhang
  - Abhay Puri
  - Aarash Feizi
  - Rishav Pramanik
  - Pascal Wichmann
  - Arnab Mondal
  - Mohammad Reza Samsami
  - Rabiul Awal
  - Perouz Taslakian
  - others
publication_types:
  - 'paper-conference'
publication: '*Advances in Neural Information Processing Systems (NeurIPS)*'
abstract: 'Scalable Vector Graphics (SVG) offer a powerful format for representing visual designs as interpretable code. Recent advances in vision-language models (VLMs) have enabled high-quality SVG generation by framing the problem as a code generation task and leveraging large-scale pretraining. VLMs are particularly suitable for this task as they capture both global semantics and fine-grained visual patterns, while transferring knowledge across vision, natural language, and code domains. However, existing VLM approaches often struggle to produce faithful and efficient SVGs because they never observe the rendered images during training. Although differentiable rendering for autoregressive SVG code generation remains unavailable, rendered outputs can still be compared to original inputs, enabling evaluative feedback suitable for reinforcement learning (RL). In this work, we introduce RLVG, a reinforcement learning approach for SVG generation with autoregressive VLMs. Given an input image, the model generates SVG rollouts that are rendered and compared to the original image to compute a reward. This visual fidelity feedback guides the model toward producing more accurate, efficient, and semantically coherent SVGs. RLVG significantly outperforms supervised fine-tuning, addressing common failure modes and enabling precise, high-quality SVG generation with strong structural understanding and generalization.'
featured: false

links:
  - name: arXiv
    url: 'https://arxiv.org/pdf/2505.20793'
image:
  focal_point: ''
  preview_only: false
---
