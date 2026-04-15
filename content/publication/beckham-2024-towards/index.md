---
title: 'Towards Good Validation Metrics for Generative Models in Offline Model-Based Optimisation'
date: '2024-01-01'
draft: false
authors:
  - Christopher Beckham
  - Alexandre Piche
  - David Vázquez
  - Christopher Pal
publication_types:
  - 'article-journal'
publication: '*Transactions on Machine Learning Research (TMLR)*'
abstract: 'In model-based optimisation (MBO) we are interested in using machine learning to design candidates that maximise some measure of reward with respect to a black box function called the (ground truth) oracle, which is expensive to compute since it involves executing a real world process. In offline MBO we wish to do so without assuming access to such an oracle during training or validation, with makes evaluation non-straightforward. While an approximation to the ground oracle can be trained and used in place of it during model validation to measure the mean reward over generated candidates, the evaluation is approximate and vulnerable to adversarial examples. Measuring the mean reward of generated candidates over this approximation is one such `validation metric'', whereas we are interested in a more fundamental question which is finding which validation metrics correlate the most with the ground truth. This involves proposing validation metrics and quantifying them over many datasets for which the ground truth is known, for instance simulated environments. This is encapsulated under our proposed evaluation framework which is also designed to measure extrapolation, which is the ultimate goal behind leveraging generative models for MBO. While our evaluation framework is model agnostic we specifically evaluate denoising diffusion models due to their state-of-the-art performance, as well as derive interesting insights such as ranking the most effective validation metrics as well as discussing important hyperparameters.'
featured: false

links:
  - name: arXiv
    url: 'https://arxiv.org/pdf/2211.10747'
---
