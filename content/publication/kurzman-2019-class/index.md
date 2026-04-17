---
title: 'Class-Based Styling: Real-Time Localized Style Transfer with Semantic Segmentation'
date: '2019-01-01'
draft: false
authors:
  - Lironne Kurzman
  - David Vázquez
  - Issam Laradji
publication_types:
  - 'paper-workshop'
publication: '*Workshop at International Conference on Computer Vision (ICCV)*'
abstract: 'We propose a Class-Based Styling method (CBS) that can map different styles for different object classes in real-time. CBS achieves real-time performance by carrying out two steps simultaneously. While a semantic segmentation method is used to obtain the mask of each object class in a video frame, a styling method is used to style that frame globally. Then an object class can be styled by combining the segmentation mask and the styled image. The user can also select multiple styles so that different object classes can have different styles in a single frame. For semantic segmentation, we leverage DABNet that achieves high accuracy, yet only has 0.76 million parameters and runs at 104 FPS. For the style transfer step, we use a popular real-time method proposed by Johnson et al. [7]. We evaluated CBS on a video of the CityScapes dataset and observed high-quality localized style transfer results for different object classes and real-time performance.'
featured: false

links:
  - type: code
    url: 'https://github.com/IssamLaradji/CBStyling'
  - name: arXiv
    url: 'https://arxiv.org/pdf/1908.11525'
image:
  focal_point: ''
  preview_only: false
---
