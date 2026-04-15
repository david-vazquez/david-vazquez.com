---
title: 'Where Are the Masks: Instance Segmentation with Image-Level Supervision'
date: '2019-01-01'
draft: false
authors:
  - Issam H Laradji
  - David Vázquez
  - Mark Schmidt
publication_types:
  - 'paper-conference'
publication: '*British Machine Vision Conference (BMVC)*'
abstract: 'A major obstacle in instance segmentation is that existing methods often need many per-pixel labels in order to be effective. These labels require large human effort and for certain applications, such labels are not readily available. To address this limitation, we propose a novel framework that can effectively train with image-level labels, which are significantly cheaper to acquire. For instance, one can do an internet search for the term ''car'' and obtain many images where a car is present with minimal effort. Our framework consists of two stages: (1) train a classifier to generate pseudo masks for the objects of interest; (2) train a fully supervised Mask R-CNN on these pseudo masks. Our two main contribution are proposing a pipeline that is simple to implement and is amenable to different segmentation methods; and achieves new state-of-the-art results for this problem setup. Our results are based on evaluating our method on PASCAL VOC 2012, a standard dataset for weakly supervised methods, where we demonstrate major performance gains compared to existing methods with respect to mean average precision.'
featured: false

links:
  - type: code
    url: 'https://github.com/ServiceNow/wise_ils'
  - name: arXiv
    url: 'https://arxiv.org/pdf/1907.01430'
image:
  focal_point: ''
  preview_only: false
---
