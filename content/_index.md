---
title: ''
date: 2026-04-07
type: landing

design:
  spacing: "6rem"

sections:
  - block: resume-biography
    id: about
    content:
      title: ''
      username: david-vazquez

  - block: collection
    id: news
    content:
      title: Recent News
      subtitle: ''
      text: ''
      page_type: news
      count: 5
      offset: 0
      order: desc
    design:
      view: date-title-summary

  - block: collection
    id: projects
    content:
      title: Research
      subtitle: Current and past projects
      text: ''
      filters:
        folders:
          - project
      sort_by: 'Date'
      sort_ascending: false
    design:
      view: article-grid

  - block: collection
    id: publications
    content:
      title: Selected Publications
      subtitle: '[Full list on Google Scholar](https://scholar.google.ca/citations?user=1jHvtfsAAAAJ)'
      text: ''
      filters:
        folders:
          - publication
      count: 20
      sort_by: 'Date'
      sort_ascending: false
    design:
      view: citation

  - block: markdown
    id: team
    content:
      title: Team
      subtitle: Current members and alumni
      text: |
        See the [full team page]({{< ref "/team" >}}) for current PhD interns, thesis students, and alumni placements.

        **Alumni highlights:** Meta AI, Google, Apple, NUS, UC Berkeley, NVIDIA, MIT, and founders of QuiverAI, Tensoreye, SeaX AI, and Theker.

  - block: markdown
    id: teaching
    content:
      title: Teaching
      text: |
        **Adjunct Professor, Polytechnique Montréal** (2025 to Present)
        Co supervising doctoral students in multimodal AI and AI agents.

        **Adjunct Professor, UAB** (2017 to Present)
        Teaching graduate courses in the Master's in Computer Vision and AI.

        See the [full teaching page]({{< ref "/teaching" >}}) for course history and program development.

  - block: markdown
    id: service
    content:
      title: Academic Service
      text: |
        **Board Memberships:**
        ELLIS Member (2019 to Present) · NSERC TAC Reviewer (2025 to Present) · QueerTech Inclusive Tech Advisory Board (2025 to Present)

        **Workshop Organization:**
        GoodData at AAAI 2025 · L3D-IVU at CVPR 2022 to 2023 · CLVision at CVPR 2020 to 2023 · GroundedML at ICLR 2022 · TASK-CV at ICCV/ECCV 2014 to 2021 · WAD at CVPR 2018 to 2021

        **Area Chair / Reviewer:**
        NeurIPS · ICLR · ICML · CVPR · ECCV · ICCV · ACL · TMLR

  - block: contact-info
    id: contact
    content:
      title: Contact
      subtitle: ''
      email: david.vazquez@mila.quebec
      address:
        lines:
          - Montreal, Quebec, Canada
      social:
        - icon: hero/academic-cap
          url: 'https://scholar.google.ca/citations?user=1jHvtfsAAAAJ'
        - icon: brands/linkedin
          url: 'https://www.linkedin.com/in/dvazquezcvc/'
        - icon: brands/x-twitter
          url: 'https://x.com/dvazquezcv'
---
