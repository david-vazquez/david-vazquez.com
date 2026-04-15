---
title: 'VectorGym: A Multitask Benchmark for SVG Code Generation, Sketching, and Editing'
date: '2026-01-01'
draft: false
authors:
  - Juan Rodriguez
  - Haotian Zhang
  - Abhay Puri
  - Tianyang Zhang
  - Rishav Pramanik
  - Meng Lin
  - Xiaoqing Xie
  - Marco Terral
  - Darsh Kaushik
  - Aly Shariff
  - others
publication_types:
  - 'manuscript'
publication: '*arXiv preprint arXiv:2603.29852*'
abstract: 'We introduce VectorGym, a comprehensive benchmark suite for Scalable Vector Graphics (SVG) that spans generation from text and sketches, complex editing, and visual understanding. VectorGym addresses the lack of realistic, challenging benchmarks aligned with professional design workflows. Our benchmark comprises four tasks with expert human-authored annotations: the novel Sketch2SVG task (VG-Sketch); a new SVG editing dataset (VG-Edit) featuring complex, multi-step edits with higher-order primitives; Text2SVG generation (VG-Text); and SVG captioning (VG-Cap). Unlike prior benchmarks that rely on synthetic edits, VectorGym provides gold-standard human annotations that require semantic understanding and design intent. We also propose a multi-task reinforcement learning approach that jointly optimizes across all four tasks using rendering-based rewards. Our method, built on GRPO with curriculum learning, trains a Qwen3-VL 8B model that achieves state-of-the-art performance among open-source models, surpassing much larger models including Qwen3-VL 235B and matching GPT-4o. We also introduce a VLM-as-a-Judge metric for SVG generation, validated through human correlation studies. Our evaluation of frontier VLMs reveals significant performance gaps, positioning VectorGym as a rigorous framework for advancing visual code generation. VectorGym is publicly available on this http URL.'
featured: false
links:
  - name: arXiv
    url: 'https://arxiv.org/pdf/2603.29852'
---
