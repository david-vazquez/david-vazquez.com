---
title: 'Distilling Specialized Orders for Visual Generation'
date: '2025-01-01'
draft: false
authors:
  - Rishav Pramanik
  - Antoine Poupon
  - Juan A Rodriguez
  - Masih Aminbeidokhti
  - David Vázquez
  - Christopher Pal
  - Zhaozheng Yin
  - Marco Pedersoli
publication_types:
  - 'manuscript'
publication: '*arXiv preprint arXiv:2504.17069*'
abstract: 'Autoregressive patch-based image generation has recently shown competitive results in terms of image quality and scalability. It can also be easily integrated and scaled within Vision-Language models. Nevertheless, autoregressive models require a defined order for patch generation. While a natural order based on the dictation of the words makes sense for text generation, there is no inherent generation order that exists for image generation. Traditionally, a raster-scan order (from top-left to bottom-right) guides autoregressive image generation models. In this paper, we argue that this order is suboptimal, as it fails to respect the causality of the image content: for instance, when conditioned on a visual description of a sunset, an autoregressive model may generate clouds before the sun, even though the color of clouds should depend on the color of the sun and not the inverse. In this work, we show that first by training a model to generate patches in any-given-order, we can infer both the content and the location (order) of each patch during generation. Secondly, we use these extracted orders to finetune the any-given-order model to produce better-quality images. Through our experiments, we show on two datasets that this new generation method produces better images than the traditional raster-scan approach, with similar training costs and no extra annotations.'
featured: false
links:
  - type: pdf
    url: 'https://arxiv.org/pdf/2504.17069'
---
