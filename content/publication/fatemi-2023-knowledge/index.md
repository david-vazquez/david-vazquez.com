---
title: 'Knowledge Hypergraph Embedding Meets Relational Algebra'
date: '2023-01-01'
draft: false
authors:
  - Bahare Fatemi
  - Perouz Taslakian
  - David Vázquez
  - David Poole
publication_types:
  - 'article-journal'
publication: '*Journal of Machine Learning Research (JMLR)*'
abstract: 'Embedding-based methods for reasoning in knowledge hypergraphs learn a representation for each entity and relation. Current methods do not capture the procedural rules underlying the relations in the graph. We propose a simple embedding-based model called ReAlE that performs link prediction in knowledge hypergraphs (generalized knowledge graphs) and can represent high-level abstractions in terms of relational algebra operations. We show theoretically that ReAlE is fully expressive and provide proofs and empirical evidence that it can represent a large subset of the primitive relational algebra operations, namely renaming, projection, set union, selection, and set difference. We also verify experimentally that ReAlE outperforms state-of-the-art models in knowledge hypergraph completion, and in representing each of these primitive relational algebra operations. For the latter experiment, we generate a synthetic knowledge hypergraph, for which we design an algorithm based on the Erdos-Renyi model for generating random graphs.'
featured: false

links:
  - type: code
    url: 'https://github.com/baharefatemi/ReAlE'
  - name: arXiv
    url: 'https://arxiv.org/pdf/2102.09557'
---
