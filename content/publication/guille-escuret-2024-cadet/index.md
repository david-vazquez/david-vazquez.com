---
title: 'CADet: Fully Self-Supervised Out-of-Distribution Detection with Contrastive Learning'
date: '2024-01-01'
draft: false
authors:
  - Charles Guille-Escuret
  - Pau Rodriguez
  - David Vázquez
  - Ioannis Mitliagkas
  - Joao Monteiro
publication_types:
  - 'paper-conference'
publication: '*Advances in Neural Information Processing Systems (NeurIPS)*'
abstract: 'Handling out-of-distribution (OOD) samples has become a major stake in the real-world deployment of machine learning systems. This work explores the application of self-supervised contrastive learning to the simultaneous detection of two types of OOD samples: unseen classes and adversarial perturbations. Since in practice the distribution of such samples is not known in advance, we do not assume access to OOD examples. We first show that similarity functions trained with contrastive learning can be leveraged with the maximum mean discrepancy (MMD) two-sample test to verify whether two independent sets of samples are drawn from the same distribution. Inspired by this approach, we introduce CADet (Contrastive Anomaly Detection), a method based on contrastive transformations to perform anomaly detection on single samples. CADet compares favorably to adversarial detection methods to detect adversarially perturbed samples on ImageNet. Simultaneously, it achieves comparable performance to unseen label detection methods on two challenging benchmarks: ImageNet-O and iNaturalist. CADet is fully self-supervised and requires neither labels for in-distribution samples nor access to OOD examples.'
featured: false

links:
  - name: arXiv
    url: 'https://arxiv.org/pdf/2210.01742'
---
