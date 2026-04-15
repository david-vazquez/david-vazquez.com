---
title: 'Incremental Domain Adaptation of Deformable Part-Based Models'
date: '2014-01-01'
draft: false
authors:
  - Jiaolong Xu
  - Sebastian Ramos
  - David Vázquez
  - Antonio M López
publication_types:
  - 'paper-conference'
publication: '*British Machine Vision Conference (BMVC)*'
abstract: 'Nowadays, classifiers play a core role in many computer vision tasks. The underlying assumption for learning classifiers is that the training set and the deployment environment (testing) follow the same probability distribution regarding the features used by the classifiers. However, in practice, there are different reasons that can break this constancy assumption. Accordingly, reusing existing classifiers by adapting them from the previous training environment (source domain) to the new testing one (target domain) is an approach with increasing acceptance in the computer vision community. In this paper we focus on the domain adaptation of deformable part-based models (DPMs) for object detection. In particular, we focus on a relatively unexplored scenario, i.e., on-line/incremental domain adaptation for object detection assuming weak-labeling. Therefore, our algorithm is ready to improve existing source-oriented DPM-based detectors as soon as a little amount of labeled target-domain training data is available, and keeps improving as more of such data arrives in a continuous fashion. For achieving this, we follow a multiple instance learning (MIL) paradigm that operates in an incremental per-image basis. As proof of concept, we address the challenging scenario of adapting a DPM-based pedestrian detector trained with synthetic pedestrians to operate in real-world scenarios. The obtained results show that our incremental adaptive models obtain equally good accuracy results as the batch learned models, while being more flexible for handling continuously arriving target-domain data.'
featured: false

links:
  - type: pdf
    url: 'http://sebastian-ramos.net/wp-content/uploads/2015/02/bmvc14.pdf'
---
