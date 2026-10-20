---
layout: archive
title: "Code"
permalink: /code/
author_profile: true
---

<p class="code-intro">Open-source implementations accompanying IDEAL Lab publications. These repositories make research methods easier to inspect, reproduce, and extend.</p>

{% assign code_projects = site.code | sort: "date" | reverse %}

<div class="code-list">
  {% for project in code_projects %}
    <article class="code-card">
      <div class="code-card__body">
        <p class="code-card__eyebrow">{{ project.category | default: "Research software" }}</p>
        <h2>{{ project.title }}</h2>
        <p class="code-card__meta">{{ project.authors }} · <em>{{ project.venue }}</em> · {{ project.date | date: "%Y" }}</p>
        <p>{{ project.description }}</p>
      </div>
      <div class="code-card__actions">
        <a class="btn btn--primary" href="{{ project.repositoryurl }}"><i class="fab fa-github" aria-hidden="true"></i> View code</a>
        {% if project.paperurl %}
          <a class="btn btn--inverse" href="{{ project.paperurl }}"><i class="fas fa-book-open" aria-hidden="true"></i> View paper</a>
        {% endif %}
      </div>
    </article>
  {% endfor %}
</div>
