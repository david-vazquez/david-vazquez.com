---
title: 'Domain Adaptation of Deformable Part-Based Models'
date: '2014-01-01'
draft: false
authors:
  - Jiaolong Xu
  - Sebastian Ramos
  - David Vázquez
  - Antonio M López
publication_types:
  - 'article-journal'
publication: '*IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)*'
abstract: 'The accuracy of object classifiers can significantly drop when the training data (source domain) and the application scenario (target domain) have inherent differences. Therefore, adapting the classifiers to the scenario in which they must operate is of paramount importance. We present novel domain adaptation (DA) methods for object detection. As proof of concept, we focus on adapting the state-of-the-art deformable part-based model (DPM) for pedestrian detection. We introduce an adaptive structural SVM (A-SSVM) that adapts a pre-learned classifier between different domains. By taking into account the inherent structure in feature space (e.g., the parts in a DPM), we propose a structure-aware A-SSVM (SA-SSVM). Neither A-SSVM nor SA-SSVM needs to revisit the source-domain training data to perform the adaptation. Rather, a low number of target-domain training examples (e.g., pedestrians) are used. To address the scenario where there are no target-domain annotated samples, we propose a self-adaptive DPM based on a self-paced learning (SPL) strategy and a Gaussian Process Regression (GPR). Two types of adaptation tasks are assessed: from both synthetic pedestrians and general persons (PASCAL VOC) to pedestrians imaged from an on-board camera. Results show that our proposals avoid accuracy drops as high as 15 points when comparing adapted and non-adapted detectors.'
featured: false

links:
  - type: pdf
    url: 'http://refbase.cvc.uab.es/files/XRV2014b.pdf'
---
