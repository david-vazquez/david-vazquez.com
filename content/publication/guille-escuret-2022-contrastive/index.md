---
title: 'Contrastive Self-Supervision Defines General-Purpose Similarity Functions'
date: '2022-01-01'
draft: false
authors:
  - Charles Guille-Escuret
  - Pau Rodrı́guez
  - David Vázquez
  - Ioannis Mitliagkas
  - João Monteiro
publication_types:
  - 'paper-workshop'
publication: '*Workshop at Advances in Neural Information Processing Systems (NeurIPS)*'
abstract: 'Handling out-of-distribution (OOD) and adversarial inputs has become a major stake in the real-world deployment of machine learning systems. In this work, we explore the use of maximum mean discrepancy (MMD) two-sample test in conjunction with self-supervised contrastive learning to verify whether two sets of samples have been drawn from a same distribution. In particular, we find that the similarity functions defined on top of models trained with contrastive learning lead to high testing power on different types of distributional shifts. Our approach is able to differentiate CIFAR10 from CIFAR10.1 with much higher probability and using less samples than previous methods. Moreover, when trained on ImageNet, our approach shows great efficiency in detecting both adversarial attacks and OOD data on challenging benchmarks, using only 3 to 20 samples.'
featured: false

links:
  - type: pdf
    url: 'https://sslneurips22.github.io/paper_pdfs/paper_38.pdf'
---
