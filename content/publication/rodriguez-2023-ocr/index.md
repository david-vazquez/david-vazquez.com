---
title: 'OCR-VQGAN: Taming Text-within-Image Generation'
date: '2023-01-01'
draft: false
authors:
  - Juan A Rodriguez
  - David Vázquez
  - Issam Laradji
  - Marco Pedersoli
  - Pau Rodriguez
publication_types:
  - 'paper-conference'
publication: '*Winter Conference on Applications of Computer Vision (WACV)*'
abstract: 'Synthetic image generation has recently experienced significant improvements in domains such as natural image or art generation. However, the problem of figure and diagram generation remains unexplored. A challenging aspect of generating figures and diagrams is effectively rendering readable texts within the images. To alleviate this problem, we present OCR-VQGAN, an image encoder and decoder that leverages OCR pre-trained features to optimize a text perceptual loss, encouraging the architecture to preserve high fidelity text and diagram structure. To explore our approach, we introduce the Paper2Fig100k dataset, with over 100k images of figures and texts from research papers. The figures show architecture diagrams and methodologies of articles available at arXiv.org from fields like artificial intelligence and computer vision. Figures usually include text and discrete objects, e.g., boxes in a diagram, with lines and arrows that connect them. We demonstrate the superiority of our method by conducting several experiments on the task of figure reconstruction. Additionally, we explore the qualitative and quantitative impact of weighting different perceptual metrics in the overall loss function.'
featured: false

links:
  - type: code
    url: 'https://github.com/joanrod/ocr-vqgan'
  - name: arXiv
    url: 'https://arxiv.org/pdf/2210.11248'
image:
  focal_point: ''
  preview_only: false
---
