---
title:
date: 2026-04-07
type: landing

sections:
  - block: resume-biography
    id: about
    content:
      username: david-vazquez
      text: |
        I study how machines learn to act in the world.
    design:
      css_class: dark
      background:
        color: black
        image:
          filename: bg-hero.jpg
          filters:
            brightness: 0.4
          size: cover
          position: center
          parallax: false

  - block: stats
    content:
      items:
        - statistic: "13K+"
          description: |
            Citations
        - statistic: "140+"
          description: |
            Publications
        - statistic: "4"
          description: |
            Patents
        - statistic: "15+"
          description: |
            Years of Research
    design:
      layout: minimal
      css_class: "bg-gray-100 dark:bg-gray-900"
      spacing:
        padding: [0, 0, 0, 0]

  - block: markdown
    content:
      title: Welcome
      subtitle: ''
      text: |
        I am Research Director at [ServiceNow](https://www.servicenow.com/research/), where I lead the Foundational AI Research (FAR) team working on foundation models, AI agents, RL reasoning, and enterprise reliability (safety and security). I am also Adjunct Professor at [Polytechnique Montréal](https://www.polymtl.ca/) (affiliated with [MILA](https://mila.quebec/)) and the [Universitat Autònoma de Barcelona](https://www.uab.cat/) (affiliated with [CVC](https://www.cvc.uab.es/)). Our team publishes impactful work at top AI venues and releases open-source models, benchmarks, and tools used by the research community worldwide.

        **I am always looking for talented interns and full-time researchers to join my team at ServiceNow, as well as PhD and Master's students at the university.** If you are excited about foundation models, AI agents, or open science, [get in touch](mailto:david.vazquez@mila.quebec).

        <div class="mt-4 flex items-center text-sm font-medium text-primary-500"><a href="/bio/" style="text-decoration:none !important;color:inherit !important">Read full bio<svg class="ml-1 w-4 h-4 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg></a></div>
    design:
      columns: '1'

  - block: collection
    id: news
    content:
      title: Recent News
      subtitle: ''
      count: 5
      filters:
        folders:
          - news
        author: ""
        category: ""
        tag: ""
    design:
      view: date-title-summary
      columns: '1'
---
