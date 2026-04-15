---
title: '3D Perception with Slanted Stixels on GPU'
date: '2021-01-01'
draft: false
authors:
  - Daniel Hernandez-Juarez
  - Antonio Espinosa
  - David Vázquez
  - Antonio M. Lopez
  - Juan C. Moure
publication_types:
  - 'article-journal'
publication: '*IEEE Transactions on Parallel and Distributed Systems (TPDS)*'
abstract: 'This article presents a GPU-accelerated software design of the recently proposed model of Slanted Stixels, which represents the geometric and semantic information of a scene in a compact and accurate way. We reformulate the measurement depth model to reduce the computational complexity of the algorithm, relying on the confidence of the depth estimation and the identification of invalid values to handle outliers. The proposed massively parallel scheme and data layout for the irregular computation pattern that corresponds to a Dynamic Programming paradigm is described and carefully analyzed in performance terms. Performance is shown to scale gracefully on current generation embedded GPUs. We assess the proposed methods in terms of semantic and geometric accuracy as well as run-time performance on three publicly available benchmark datasets. Our approach achieves real-time performance with high accuracy for 2048 x 1024 image sizes and 4 x 4 Stixel resolution on the low-power embedded GPU of an NVIDIA Tegra Xavier.'
featured: false

links:
  - type: code
    url: 'https://github.com/dhernandez0/stixels'
  - type: pdf
    url: 'https://ieeexplore.ieee.org/abstract/document/9382880'
---
