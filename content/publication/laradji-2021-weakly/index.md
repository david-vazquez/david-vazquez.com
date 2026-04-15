---
title: 'Weakly Supervised Underwater Fish Segmentation using Affinity LCFCN'
date: '2021-01-01'
draft: false
authors:
  - Issam H Laradji
  - Alzayat Saleh
  - Pau Rodriguez
  - Derek Nowrouzezahrai
  - Mostafa Rahimi Azghadi
  - David Vázquez
publication_types:
  - 'article-journal'
publication: '*Nature Scientific Reports*'
abstract: 'Estimating fish body measurements like length, width, and mass has potential applications in marine and aquaculture productivity. The paper proposes a segmentation model requiring only point-level supervision (single click per fish, ~1 second per fish) rather than per-pixel labels (up to 2 minutes per fish). The method uses a fully convolutional neural network with two branches: one outputs per-pixel scores, another outputs an affinity matrix. These are combined using random walk refinement and trained end-to-end with LCFCN loss, termed Affinity-LCFCN (A-LCFCN). Experiments on the DeepFish dataset show A-LCFCN outperforms fully-supervised models at fixed annotation budgets and achieves better results than standard baselines.'
featured: false

links:
  - type: pdf
    url: 'https://www.nature.com/articles/s41598-021-96610-2'
---
