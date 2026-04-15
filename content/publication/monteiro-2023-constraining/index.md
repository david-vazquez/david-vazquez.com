---
title: Constraining Representations Yields Models That Know What They Don't Know
date: '2023-01-01'
draft: false
publishDate: '2026-04-08T13:35:27.785461Z'
authors:
- João Monteiro
- Pau Rodríguez
- Pierre-André Noël
- Issam H. Laradji
- David Vázquez
publication_types:
- '1'
abstract: 'A well-known failure mode of neural networks is that they may confidently return erroneous predictions. Such unsafe behaviour is particularly frequent when the use case slightly differs from the training context, and/or in the presence of an adversary. This work presents a novel direction to address these issues in a broad, general manner: imposing class-aware constraints on a model''s internal activation patterns. Specifically, we assign to each class a unique, fixed, randomly-generated binary vector - hereafter called class code - and train the model so that its cross-depths activation patterns predict the appropriate class code according to the input sample''s class. The resulting predictors are dubbed total activation classifiers (TAC), and TACs may either be trained from scratch, or used with negligible cost as a thin add-on on top of a frozen, pre-trained neural network. The distance between a TAC''s activation pattern and the closest valid code acts as an additional confidence score, besides the default unTAC''ed prediction head''s. In the add-on case, the original neural network''s inference head is completely unaffected (so its accuracy remains the same) but we now have the option to use TAC''s own confidence and prediction when determining which course of action to take in an hypothetical production workflow. In particular, we show that TAC strictly improves the value derived from models allowed to reject/defer. We provide further empirical evidence that TAC works well on multiple types of architectures and data modalities and that it is at least as good as state-of-the-art alternative confidence scores derived from existing models.'
featured: false
publication: '*International Conference on Learning Representations (ICLR)*'

links:
  - type: code
    url: 'https://github.com/ServiceNow/tac'
  - type: slides
    url: 'https://www.servicenow.com/research/publication/joao-monteiro-cons-iclr2023/slides.pptx'
  - type: 'video'
    url: 'https://iclr.cc/virtual/2023/poster/11420'
  - type: 'pdf'
    url: 'https://arxiv.org/pdf/2208.14488'
image:
  focal_point: ''
  preview_only: false
---

