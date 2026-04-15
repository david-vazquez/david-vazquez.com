---
title: 'Learning Data Augmentation with Online Bilevel Optimization for Image Classification'
date: '2021-01-01'
draft: false
authors:
  - Saypraseuth Mounsaveng
  - Issam Laradji
  - Ismail Ben Ayed
  - David Vázquez
  - Marco Pedersoli
publication_types:
  - 'paper-conference'
publication: '*Winter Conference on Applications of Computer Vision (WACV)*'
abstract: 'Data augmentation is a key practice in machine learning for improving generalization performance. However, finding the best data augmentation hyperparameters requires domain knowledge or a computationally demanding search. We address this issue by proposing an efficient approach to automatically train a network that learns an effective distribution of transformations to improve its generalization. Using bilevel optimization, we directly optimize the data augmentation parameters using a validation set. This framework can be used as a general solution to learn the optimal data augmentation jointly with an end task model like a classifier. Results show that our joint training method produces an image classification accuracy that is comparable to or better than carefully hand-crafted data augmentation. Yet, it does not need an expensive external validation loop on the data augmentation hyperparameters.'
featured: false

links:
  - type: code
    url: 'https://github.com/ServiceNow/bilevel_augment'
  - name: arXiv
    url: 'https://arxiv.org/pdf/2006.14699'
---
