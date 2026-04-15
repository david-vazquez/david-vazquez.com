---
title: 'Improving HOG with Image Segmentation: Application to Human Detection'
date: '2012-01-01'
draft: false
authors:
  - Yainuvis Socarrás
  - David Vázquez
  - Antonio M López
  - David Gerónimo
  - Theo Gevers
publication_types:
  - 'paper-conference'
publication: '*International Conference on Advanced Concepts for Intelligent Vision Systems (ACIVS)*'
abstract: 'In this paper we improve the histogram of oriented gradients (HOG), a core descriptor of state-of-the-art object detection, by the use of higher-level information coming from image segmentation. The idea is to re-weight the descriptor while computing it without increasing its size. The benefits of the proposal are two-fold: (i) to improve the performance of the detector by enriching the descriptor information and (ii) take advantage of the information of image segmentation, which in fact is likely to be used in other stages of the detection system such as candidate generation or refinement. We test our technique in the INRIA person dataset, which was originally developed to test HOG, embedding it in a human detection system. The well-known segmentation method, mean-shift (from smaller to larger super-pixels), and different methods to re-weight the original descriptor (constant, region-luminance, color or texture-dependent) has been evaluated. We achieve performance improvements of 4.47% in detection rate through the use of differences of color between contour pixel neighborhoods as re-weighting function.'
featured: false

links:
  - type: pdf
    url: 'http://refbase.cvc.uab.es/files/SLV2012a.pdf'
---
