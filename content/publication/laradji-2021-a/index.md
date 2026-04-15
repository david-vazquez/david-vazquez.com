---
title: 'A Weakly Supervised Consistency-Based Learning Method for COVID-19 Segmentation in CT Images'
date: '2021-01-01'
draft: false
authors:
  - Issam Laradji
  - Pau Rodriguez
  - Oscar Manas
  - Keegan Lensink
  - Marco Law
  - Lironne Kurzman
  - William Parker
  - David Vázquez
  - Derek Nowrouzezahrai
publication_types:
  - 'paper-conference'
publication: '*Winter Conference on Applications of Computer Vision (WACV)*'
abstract: 'Coronavirus Disease 2019 (COVID-19) has spread aggressively across the world causing an existential health crisis. Thus, having a system that automatically detects COVID-19 in tomography (CT) images can assist in quantifying the severity of the illness. Unfortunately, labelling chest CT scans requires significant domain expertise, time, and effort. We address these labelling challenges by only requiring point annotations, a single pixel for each infected region on a CT image. This labeling scheme allows annotators to label a pixel in a likely infected region, only taking 1-3 seconds, as opposed to 10-15 seconds to segment a region. Conventionally, segmentation models train on point-level annotations using the cross-entropy loss function on these labels. However, these models often suffer from low precision. Thus, we propose a consistency-based (CB) loss function that encourages the output predictions to be consistent with spatial transformations of the input images. The experiments on 3 open-source COVID-19 datasets show that this loss function yields significant improvement over conventional point-level loss functions and almost matches the performance of models trained with full supervision with much less human effort.'
featured: false

links:
  - type: code
    url: 'https://github.com/IssamLaradji/covid19_weak_supervision'
  - type: slides
    url: 'https://www.servicenow.com/research/publication/issam-h.-laradji-a-we-wacv2021/slides.pdf'
  - name: arXiv
    url: 'https://arxiv.org/pdf/2007.02180'
image:
  focal_point: ''
  preview_only: false
---
