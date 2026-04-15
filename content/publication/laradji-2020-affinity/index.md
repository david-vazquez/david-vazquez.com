---
title: 'Affinity LCFCN: Learning to Segment Fish with Weak Supervision'
date: '2020-01-01'
draft: false
authors:
  - Issam Laradji
  - Alzayat Saleh
  - Pau Rodriguez
  - Derek Nowrouzezahrai
  - Mostafa Rahimi Azghadi
  - David Vázquez
publication_types:
  - 'article-journal'
publication: '*Nature Scientific Reports*'
abstract: 'Aquaculture industries rely on the availability of accurate fish body measurements, e.g., length, width and mass. Manual methods that rely on physical tools like rulers are time and labour intensive. Leading automatic approaches rely on fully-supervised segmentation models to acquire these measurements but these require collecting per-pixel labels -- also time consuming and laborious: i.e., it can take up to two minutes per fish to generate accurate segmentation labels, almost always requiring at least some manual intervention. We propose an automatic segmentation model efficiently trained on images labeled with only point-level supervision, where each fish is annotated with a single click. This labeling process requires significantly less manual intervention, averaging roughly one second per fish. Our approach uses a fully convolutional neural network with one branch that outputs per-pixel scores and another that outputs an affinity matrix. We aggregate these two outputs using a random walk to obtain the final, refined per-pixel segmentation output. We train the entire model end-to-end with an LCFCN loss, resulting in our A-LCFCN method. We validate our model on the DeepFish dataset, which contains many fish habitats from the north-eastern Australian region. Our experimental results confirm that A-LCFCN outperforms a fully-supervised segmentation model at fixed annotation budget. Moreover, we show that A-LCFCN achieves better segmentation results than LCFCN and a standard baseline.'
featured: false

links:
  - type: code
    url: 'https://github.com/IssamLaradji/affinity_lcfcn'
  - name: arXiv
    url: 'https://arxiv.org/pdf/2011.03149'
---
