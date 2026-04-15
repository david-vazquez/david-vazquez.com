---
title: 'Learning to Remove Rain in Traffic Surveillance by using Synthetic Data'
date: '2018-01-01'
draft: false
authors:
  - Chris H Bahnsen
  - David Vázquez
  - Antonio M López
  - Thomas B Moeslund
publication_types:
  - 'paper-conference'
publication: '*International Conference on Computer Vision Theory and Applications (VISIGRAPP)*'
abstract: 'Rainfall is a problem in automated traffic surveillance. Rain streaks occlude the road users and degrade the overall visibility which in turn decrease object detection performance. One way of alleviating this is by artificially removing the rain from the images. This requires knowledge of corresponding rainy and rain-free images. Such images are often produced by overlaying synthetic rain on top of rain-free images. However, this method fails to incorporate the fact that rain fall in the entire three-dimensional volume of the scene. To overcome this, we introduce training data from the SYNTHIA virtual world that models rain streaks in the entirety of a scene. We train a conditional Generative Adversarial Network for rain removal and apply it on traffic surveillance images from SYNTHIA and the AAU RainSnow datasets. To measure the applicability of the rain-removed images in a traffic surveillance context, we run the YOLOv2 object detection algorithm on the original and rain-removed frames. The results on SYNTHIA show an 8% increase in detection accuracy compared to the original rain image. Interestingly, we find that high PSNR or SSIM scores do not imply good object detection performance.'
featured: false

links:
  - type: pdf
    url: 'https://pdfs.semanticscholar.org/1be8/da309476229f4f866e25e638c0fc0ec3ede4.pdf?_ga=2.17507902.60659343.1584314114-1624787374.1584198436'
---
