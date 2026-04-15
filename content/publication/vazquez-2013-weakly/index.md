---
title: 'Weakly Supervised Automatic Annotation of Pedestrian Bounding Boxes'
date: '2013-01-01'
draft: false
authors:
  - David Vázquez
  - Jiaolong Xu
  - Sebastian Ramos
  - Antonio Lopez
  - Daniel Ponsa
publication_types:
  - 'paper-conference'
publication: '*Workshop at Computer Vision and Pattern Recognition (CVPR)*'
abstract: 'Among the components of a pedestrian detector, its trained pedestrian classifier is crucial for achieving the desired performance. The initial task of the training process consists in collecting samples of pedestrians and background, which involves tiresome manual annotation of pedestrian bounding boxes (BBs). Thus, recent works have assessed the use of automatically collected samples from photo-realistic virtual worlds. However, learning from virtual-world samples and testing in real-world images may suffer the dataset shift problem. Accordingly, in this paper we assess an strategy to collect samples from the real world and retrain with them, thus avoiding the dataset shift, but in such a way that no BBs of real-world pedestrians have to be provided. In particular, we train a pedestrian classifier based on virtual-world samples (no human annotation required). Then, using such a classifier we collect pedestrian samples from real-world images by detection. After, a human oracle rejects the false detections efficiently (weak annotation). Finally, a new classifier is trained with the accepted detections. We show that this classifier is competitive with respect to the counterpart trained with samples collected by manually annotating hundreds of pedestrian BBs.'
featured: false

links:
  - type: pdf
    url: 'http://refbase.cvc.uab.es/files/vxr2013a.pdf'
---
