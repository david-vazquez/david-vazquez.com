---
title: 'Expecting the Unexpected: Towards Broad Out-of-Distribution Detection'
date: '2023-01-01'
draft: false
authors:
  - Charles Guille-Escuret
  - Pierre-André Noël
  - Ioannis Mitliagkas
  - David Vázquez
  - Joao Monteiro
publication_types:
  - 'paper-conference'
publication: '*Advances in Neural Information Processing Systems (NeurIPS)*'
abstract: 'Improving the reliability of deployed machine learning systems often involves developing methods to detect out-of-distribution (OOD) inputs. However, existing research often narrowly focuses on samples from classes that are absent from the training set, neglecting other types of plausible distribution shifts. This limitation reduces the applicability of these methods in real-world scenarios, where systems encounter a wide variety of anomalous inputs. In this study, we categorize five distinct types of distribution shifts and critically evaluate the performance of recent OOD detection methods on each of them. We publicly release our benchmark under the name BROAD (Benchmarking Resilience Over Anomaly Diversity). Our findings reveal that while these methods excel in detecting unknown classes, their performance is inconsistent when encountering other types of distribution shifts. In other words, they only reliably detect unexpected inputs that they have been specifically designed to expect. As a first step toward broad OOD detection, we learn a generative model of existing detection scores with a Gaussian mixture. By doing so, we present an ensemble approach that offers a more consistent and comprehensive solution for broad OOD detection, demonstrating superior performance compared to existing methods. Our code to download BROAD and reproduce our experiments is publicly available.'
featured: false

links:
  - type: code
    url: 'https://github.com/ServiceNow/broad'
  - name: arXiv
    url: 'https://arxiv.org/pdf/2308.11480'
image:
  focal_point: ''
  preview_only: false
---
