---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}
{% assign all_publications = site.publications | sort: "date" | reverse %}
{% assign journal_count = 0 %}
{% assign conference_count = 0 %}
{% for post in all_publications %}
  {% if post.publication_type == "conference" %}
    {% assign conference_count = conference_count | plus: 1 %}
  {% else %}
    {% assign journal_count = journal_count | plus: 1 %}
  {% endif %}
{% endfor %}

<section class="cv-hero">
  <p class="cv-eyebrow">Academic Curriculum Vitae</p>
  <h2>Xin Fang, Ph.D.</h2>
  <p class="cv-hero__role">Assistant Professor of Electrical Engineering · Director, IDEAL Lab · University of South Carolina</p>
  <p class="cv-hero__summary">Power-system researcher and educator developing optimization, dynamics, grid-planning, and cyber-physical modeling methods for reliable, affordable, renewable-rich electricity systems.</p>
  <div class="cv-actions">
    <a class="btn btn--primary" href="{{ '/assets/files/Xin_Fang_CV.pdf' | relative_url }}"><i class="fas fa-file-pdf" aria-hidden="true"></i> Full CV (PDF)</a>
    <a class="btn" href="mailto:fangxin@sc.edu"><i class="fas fa-envelope" aria-hidden="true"></i> Email</a>
    <a class="btn" href="{{ '/publications/' | relative_url }}"><i class="fas fa-book-open" aria-hidden="true"></i> Publications</a>
  </div>
</section>

<div class="cv-stat-grid" aria-label="Academic profile highlights">
  <div class="cv-stat">
    <strong>{{ journal_count }}</strong>
    <span>journal articles</span>
  </div>
  <div class="cv-stat">
    <strong>{{ conference_count }}</strong>
    <span>conference papers</span>
  </div>
  <div class="cv-stat">
    <strong>{{ site.projects | size }}</strong>
    <span>sponsored research projects</span>
  </div>
  <div class="cv-stat">
    <strong>4</strong>
    <span>current Ph.D. researchers</span>
  </div>
</div>

<section class="cv-section">
  <p class="cv-eyebrow">Research Agenda</p>
  <h2>Research Focus</h2>
  <div class="cv-focus-grid">
    <div class="cv-focus cv-focus--markets">
      <h3>Optimization and Markets</h3>
      <p>Electricity-market design, stochastic and robust optimization, dispatch, pricing, and stability-aware economic operation.</p>
    </div>
    <div class="cv-focus cv-focus--dynamics">
      <h3>Dynamics and Stability</h3>
      <p>Frequency response, small-signal stability, grid-forming resources, virtual inertia, and dynamics-informed scheduling.</p>
    </div>
    <div class="cv-focus cv-focus--planning">
      <h3>Grid Planning with Renewables</h3>
      <p>Capacity expansion, transmission planning, resource adequacy, resilience, and renewable integration.</p>
    </div>
    <div class="cv-focus cv-focus--cosim">
      <h3>Cyber-Physical Co-Simulation</h3>
      <p>Transmission-distribution co-simulation, grid digital twins, distributed energy resources, and electric transportation.</p>
    </div>
  </div>
</section>

<div class="cv-two-column">
  <section class="cv-section">
    <p class="cv-eyebrow">Appointments</p>
    <h2>Academic and Professional Experience</h2>
    <ol class="cv-timeline">
      <li>
        <span class="cv-timeline__date">2025-present</span>
        <strong>Assistant Professor</strong>
        <span>University of South Carolina</span>
      </li>
      <li>
        <span class="cv-timeline__date">2022-2025</span>
        <strong>Assistant Professor</strong>
        <span>Mississippi State University</span>
      </li>
      <li>
        <span class="cv-timeline__date">2017-2022</span>
        <strong>Senior Researcher</strong>
        <span>National Renewable Energy Laboratory</span>
      </li>
      <li>
        <span class="cv-timeline__date">2016-2017</span>
        <strong>Power System Engineer</strong>
        <span>GE Grid Solutions</span>
      </li>
    </ol>
  </section>

  <section class="cv-section">
    <p class="cv-eyebrow">Education</p>
    <h2>Degrees</h2>
    <ol class="cv-degree-list">
      <li><strong>Ph.D., Electrical Engineering</strong><span>University of Tennessee, Knoxville · 2016</span></li>
      <li><strong>M.S., Electrical Engineering</strong><span>China Electric Power Research Institute · 2012</span></li>
      <li><strong>B.S., Electrical Engineering</strong><span>Huazhong University of Science and Technology · 2009</span></li>
    </ol>
  </section>
</div>

<section class="cv-section">
  <p class="cv-eyebrow">Research Leadership</p>
  <h2>Sponsored Projects</h2>
  <p class="cv-section__intro">PI and Co-PI contributions span NSF, DOE, NREL, and INL programs in cybertraining, grid stability, digital twins, HVDC education, and renewable integration.</p>
  <div class="cv-project-list">
    {% assign research_projects = site.projects | sort: "date" | reverse %}
    {% for post in research_projects %}
      <article class="cv-project">
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p><strong>{{ post.role }}</strong> · {{ post.Sponsor }}</p>
        <p>{{ post.Funding }}</p>
      </article>
    {% endfor %}
  </div>
</section>

<section class="cv-section">
  <p class="cv-eyebrow">Mentoring</p>
  <h2>Advising and Student Development</h2>
  <div class="cv-advisee-grid">
    <div>
      <h3>Yuxin Deng</h3>
      <p>Ph.D. researcher in power-system optimization, planning, stability analysis, and renewable integration.</p>
    </div>
    <div>
      <h3>Prasant Basnet</h3>
      <p>Ph.D. researcher in IBR-aware capacity expansion, dynamics, and cyber-physical power-system modeling; NREL intern.</p>
    </div>
    <div>
      <h3>Bishal Rijal</h3>
      <p>Ph.D. researcher in distribution planning, transformer replacement, renewable integration, and system strength; INL intern.</p>
    </div>
    <div>
      <h3>Adarsha Chalise</h3>
      <p>Ph.D. researcher in island power systems, energy-storage sizing, flexible operation, and reliability.</p>
    </div>
  </div>
</section>

<section class="cv-section">
  <p class="cv-eyebrow">Teaching Portfolio</p>
  <h2>Courses Taught</h2>
  <div class="cv-teaching-grid">
    <div><strong>ELCT 221</strong><span>Circuits II · Spring and Fall 2026</span></div>
    <div><strong>ELCT 451</strong><span>Power System Design and Analysis · Fall 2025</span></div>
    <div><strong>ECE 5990</strong><span>Power Systems Economics · Spring 2025</span></div>
    <div><strong>ECE 4613/6613</strong><span>Power Transmission Systems · Fall 2023 and 2024</span></div>
    <div><strong>ECE 4633/6633</strong><span>Power Distribution Systems · Spring 2023</span></div>
    <div><strong>ECE 3643</strong><span>Electronic Circuits I · Fall 2022</span></div>
  </div>
</section>

<div class="cv-two-column">
  <section class="cv-section">
    <p class="cv-eyebrow">Recognition</p>
    <h2>Selected Awards and Honors</h2>
    <ul class="cv-honor-list">
      <li><strong>Best Paper Award</strong>, IEEE Open Access Journal of Power and Energy, 2025</li>
      <li><strong>IEEE PES PSOPE Technical Committee Prize Paper Award</strong>, 2024</li>
      <li><strong>Outstanding Associate Editor</strong>, IEEE Transactions on Power Systems, 2023</li>
      <li><strong>Outstanding Associate Editor</strong>, IEEE Transactions on Sustainable Energy, 2022</li>
      <li><strong>Best Journal Paper Award</strong>, Journal of Modern Power Systems and Clean Energy, 2019</li>
      <li><strong>Best Conference Paper</strong>, IEEE PES General Meeting, 2018</li>
      <li><strong>Chancellor's Citation Award for Extraordinary Professional Promise</strong>, University of Tennessee, 2016</li>
    </ul>
  </section>

  <section class="cv-section">
    <p class="cv-eyebrow">Professional Leadership</p>
    <h2>Editorial and IEEE Service</h2>
    <ul class="cv-service-list">
      <li>Vice Chair, IEEE PSOPE Bulk Power System Planning Subcommittee</li>
      <li>Associate Editor, IEEE Transactions on Sustainable Energy</li>
      <li>Associate Editor, IEEE Transactions on Power Systems</li>
      <li>Associate Editor, Energy Internet</li>
      <li>Associate Editor, Energy Conversion and Economics</li>
      <li>Associate Editor, Journal of Modern Power Systems and Clean Energy</li>
    </ul>
  </section>
</div>

<section class="cv-section cv-section--publications">
  <p class="cv-eyebrow">Scholarship</p>
  <h2>Selected Journal Publications</h2>
  <ol class="publication-numbered-list cv-publication-list">
    {% assign selected_journal_count = 0 %}
    {% for post in all_publications %}
      {% if post.publication_type != "conference" and selected_journal_count < 8 %}
        {% assign selected_journal_count = selected_journal_count | plus: 1 %}
        <li>{% include publication-list-item.html post=post %}</li>
      {% endif %}
    {% endfor %}
  </ol>
  <div class="cv-actions">
    <a class="btn btn--primary" href="{{ '/publications/' | relative_url }}">Browse all publications</a>
    <a class="btn" href="{{ '/assets/files/Xin_Fang_CV.pdf' | relative_url }}">Full publication list in PDF</a>
  </div>
</section>
