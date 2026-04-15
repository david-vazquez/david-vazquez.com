---
title: 'Slanted Stixels: A Way to Represent Steep Streets'
date: '2019-01-01'
draft: false
authors:
  - Daniel Hernandez-Juarez
  - Lukas Schneider
  - Pau Cebrian
  - Antonio Espinosa
  - David Vázquez
  - Antonio M López
  - Uwe Franke
  - Marc Pollefeys
  - Juan C Moure
publication_types:
  - 'article-journal'
publication: '*International Journal of Computer Vision (IJCV)*'
abstract: 'This work presents and evaluates a novel compact scene representation based on Stixels that infers geometric and semantic information. Our approach overcomes the previous rather restrictive geometric assumptions for Stixels by introducing a novel depth model to account for non-flat roads and slanted objects. Both semantic and depth cues are used jointly to infer the scene representation in a sound global energy minimization formulation. Furthermore, a novel approximation scheme is introduced in order to significantly reduce the computational complexity of the Stixel algorithm, and then achieve real-time computation capabilities. The idea is to first perform an over-segmentation of the image, discarding the unlikely Stixel cuts, and apply the algorithm only on the remaining Stixel cuts. This work presents a novel over-segmentation strategy based on a Fully Convolutional Network (FCN), which outperforms an approach based on using local extrema of the disparity map. We evaluate the proposed methods in terms of semantic and geometric accuracy as well as run-time on four publicly available benchmark datasets. Our approach maintains accuracy on flat road scene datasets while improving substantially on a novel non-flat road dataset.'
featured: false

links:
  - type: code
    url: 'https://github.com/dhernandez0/stixels'
  - name: arXiv
    url: 'https://arxiv.org/pdf/1910.01466'
image:
  focal_point: ''
  preview_only: false
---
