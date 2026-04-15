---
title: 'Flaky Performances When Pretraining on Relational Databases'
date: '2023-01-01'
draft: false
authors:
  - Shengchao Liu
  - David Vázquez
  - Jian Tang
  - Pierre-André Noël
publication_types:
  - 'paper-conference'
publication: '*Conference on Artificial Intelligence (AAAI)*'
abstract: 'We explore the downstream task performances for graph neural network (GNN) self-supervised learning (SSL) methods trained on subgraphs extracted from relational databases (RDBs). Intuitively, this joint use of SSL and GNNs should allow to leverage more of the available data, which could translate to better results. However, we found that naively porting contrastive SSL techniques can cause "negative transfer": linear evaluation on fixed representations from a pretrained model performs worse than on representations from the randomly-initialized model. Based on the conjecture that contrastive SSL conflicts with the message passing layers of the GNN, we propose InfoNode: a contrastive loss aiming to maximize the mutual information between a node''s initial- and final-layer representation. The primary empirical results support our conjecture and the effectiveness of InfoNode.'
featured: false

links:
  - name: arXiv
    url: 'https://arxiv.org/pdf/2211.05213'
---
