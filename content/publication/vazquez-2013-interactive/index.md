---
title: 'Interactive Training of Human Detectors'
date: '2013-01-01'
draft: false
authors:
  - David Vázquez
  - Antonio M López
  - Daniel Ponsa
  - David Gerónimo
publication_types:
  - 'paper-conference'
publication: '*International Conference on Multimodal Interaction (ICMI)*'
abstract: 'Image based human detection remains as a challenging problem. Most promising detectors rely on classifiers trained with labelled samples. However, labelling is a manual labor intensive step. To overcome this problem we propose to collect images of pedestrians from a virtual city, i.e., with automatic labels, and train a pedestrian detector with them, which works fine when such virtual-world data are similar to testing one, i.e., real-world pedestrians in urban areas. When testing data is acquired in different conditions than training one, e.g., human detection in personal photo albums, dataset shift appears. In previous work, we cast this problem as one of domain adaptation and solve it with an active learning procedure. In this work, we focus on the same problem but evaluating a different set of faster to compute features, i.e., Haar, EOH and their combination. In particular, we train a classifier with virtual-world data, using such features and Real AdaBoost as learning machine. This classifier is applied to real-world training images. Then, a human oracle interactively corrects the wrong detections, i.e., few miss detections are manually annotated and some false ones are pointed out too. A low amount of manual annotation is fixed as restriction. Real- and virtual-world difficult samples are combined within what we call cool world and we retrain the classifier with this data. Our experiments show that this adapted classifier is equivalent to the one trained with only real-world data but requiring 90% less manual annotations.'
featured: false

links:
  - type: pdf
    url: 'https://refbase.cvc.uab.es/files/vlp2012c.pdf'
---
