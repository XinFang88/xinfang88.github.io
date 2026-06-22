---
layout: archive
title: "Journal Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my full publication record on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% assign chronological_publications = site.publications | sort: "date" | reverse %}
{% capture optimization_titles %}Addressing Wind Power Forecast Errors in Day-Ahead Pricing With Energy Storage Systems: A Distributionally Robust Joint Chance-Constrained Approach|Stable Relay Learning Optimization Approach for Fast Power System Production Cost Minimization Simulation|On the Decomposition of Locational Marginal Hydrogen Pricing−Part II: Solution Approach and Numerical Results|Implications of electricity and gas price coupling in US New England region|DLMP of Competitive Markets in Active Distribution Networks: Models, Solutions, Applications, and Visions|How Can Probabilistic Solar Power Forecasts Be Used to Lower Costs and Improve Reliability in Power Spot Markets? A Review and Application to Flexiramp Requirements|Two-stage stochastic optimization frameworks to aid in decision-making under uncertainty for variable resource generators participating in a sequential energy market|Redesigning capacity market to include flexibility via ramp constraints in high-renewable penetrated system|State-of-the-art short-term electricity market operation with solar generation: A review|A clustering-based scenario generation framework for power market simulation with wind integration|Analytical Model of Day-ahead and Real-time Price Correlation in Strategic Wind Power Offering|Multi-Stage Stochastic Programming to Joint Economic Dispatch for Energy and Reserve With Uncertain Renewable Energy|Distributionally-robust chance constrained and interval optimization for integrated electricity and natural gas systems optimal power flow with wind uncertainties|Decentralized wind uncertainty management: Alternating direction method of multipliers based distributionally-robust chance constrained optimal power flow|Adjustable and distributionally robust chance-constrained economic dispatch considering wind power uncertainty|Coupon-Based Demand Response Considering Wind Power Uncertainty: A Strategic Bidding Model for Load Serving Entities|Introducing Uncertainty Components in Locational Marginal Prices for Pricing Wind Power and Load Uncertainties|Mean-Variance Optimization-Based Energy Storage Scheduling Considering Day-Ahead and Real-Time LMP Uncertainties|Bilevel Arbitrage Potential Evaluation for Grid-Scale Energy Storage Considering Wind Power and LMP Smoothing Effect|Strategic CBDR bidding considering FTR and wind power|Strategic scheduling of energy storage for load serving entities in locational marginal pricing market|Evaluation of LMP Intervals Considering Wind Uncertainty|Day-ahead coordinated operation of utility-scale electricity and natural gas networks considering demand response based virtual power plants|Hybrid component and configuration model for combined-cycle units in unit commitment problem|Deliverable Flexible Ramping Products Considering Spatiotemporal Correlation of Wind Generation and Demand Uncertainties|Modelling wind power spatial-temporal correlation in multi-interval optimal power flow: A sparse correlation matrix approach{% endcapture %}
{% capture dynamics_titles %}Analytical Small-signal Stability Analysis of Low-Inertia Power System Frequency Response Considering Secondary Frequency Regulation|Multi-Timescale Modeling Framework of Hybrid Power Plants Providing Secondary Frequency Regulation|Frequency Security-Constrained Unit Commitment with Fast Frequency Support of DFIG-Based Wind Power Plants|Dynamics-incorporated Modeling Framework for Stability Constrained Scheduling Under High-penetration of Renewable Energy|Manage Real-Time Power Imbalance With Renewable Energy: Fast Generation Dispatch or Adaptive Frequency Regulation?|Secondary Frequency Regulation from Variable Generation Through Uncertainty Decomposition: An Economic and Reliability Perspective|Real-Time Dispatch With Secondary Frequency Regulation: A Pathway to Consider Intra-Interval Fluctuations|On Thermal Dynamics Embedded Static Voltage Stability Margin|Virtual Inertia Synthesis and Control: Informative and Relevant|Electric Vehicles Charging Time Constrained Deliverable Provision of Secondary Frequency Regulation{% endcapture %}
{% capture planning_titles %}Frequency Nadir Constrained Unit Commitment for High Renewable Penetration Island Power Systems|DC Near-area Voltage Stability Constrained Renewable Energy Integration for Regional Power Grids|Reactive power planning under high penetration of wind energy using Benders decomposition|Available transfer capability evaluation in a deregulated electricity market considering correlated wind power|Energy Equity-Aware Load Shedding Optimization Methodology|Effective Parallelism for Equation and Jacobian Evaluation in Large-Scale Power Flow Calculation{% endcapture %}
{% capture cosim_titles %}Transmission-and-Distribution Dynamic Co-Simulation Framework for Distributed Energy Resource Frequency Response|Demonstrating the transient system impact of cyber-physical events through scalable transmission and distribution (T&D) co-simulation|Distributed Optimization and Control for Autonomous Distributed Energy Resource Power Dispatch and Frequency Regulation Considering Communication Failures|Load altering attack-tolerant defense strategy for load frequency control system|A Framework of Residential Demand Aggregation With Financial Incentives{% endcapture %}

{% assign optimization_titles = optimization_titles | split: "|" %}
{% assign dynamics_titles = dynamics_titles | split: "|" %}
{% assign planning_titles = planning_titles | split: "|" %}
{% assign cosim_titles = cosim_titles | split: "|" %}

<style>
  .publication-view-radio {
    position: absolute;
    width: 1px;
    height: 1px;
    overflow: hidden;
    opacity: 0;
  }

  .publication-switcher .publication-view {
    display: none;
  }

  #publication-option-chronological:checked ~ #publication-view-chronological,
  #publication-option-focus:checked ~ #publication-view-focus {
    display: block;
  }

  #publication-option-chronological:checked ~ .publication-view-toggle label[for="publication-option-chronological"],
  #publication-option-focus:checked ~ .publication-view-toggle label[for="publication-option-focus"] {
    background-color: #3b5f88;
    color: #fff;
  }
</style>

<div class="publication-switcher">
<input class="publication-view-radio" type="radio" name="publication-view-option" id="publication-option-chronological" checked>
<input class="publication-view-radio" type="radio" name="publication-view-option" id="publication-option-focus">

<div class="publication-view-toggle" aria-label="Publication list view">
  <label class="btn" for="publication-option-chronological">Chronological</label>
  <label class="btn" for="publication-option-focus">By Research Focus</label>
</div>

<section id="publication-view-chronological" class="publication-view publication-view--chronological">
  <h2>Chronological</h2>
  <ol class="publication-numbered-list">
    {% for post in chronological_publications %}
      <li>
        {% include publication-list-item.html post=post %}
      </li>
    {% endfor %}
  </ol>
</section>

<section id="publication-view-focus" class="publication-view publication-view--focus">
  <h2>By Research Focus</h2>
  {% assign focus_number = 0 %}
  <div class="publication-cluster-list">
    <section class="publication-cluster">
      <div class="publication-cluster__summary">
        <p class="publication-cluster__eyebrow">Cluster 1</p>
        <h3>Optimization and Markets</h3>
        <p>Optimization, electricity-market design, day-ahead and real-time operation, renewable uncertainty, and pricing methods for clean-energy systems.</p>
      </div>
      <ol class="publication-numbered-list publication-focus-list">
        {% for publication_title in optimization_titles %}
          {% assign post = site.publications | where: "title", publication_title | first %}
          {% if post %}
            {% assign focus_number = focus_number | plus: 1 %}
            <li value="{{ focus_number }}">
              {% include publication-list-item.html post=post %}
            </li>
          {% endif %}
        {% endfor %}
      </ol>
    </section>

    <section class="publication-cluster">
      <div class="publication-cluster__summary">
        <p class="publication-cluster__eyebrow">Cluster 2</p>
        <h3>Dynamics and Stability</h3>
        <p>Frequency response, small-signal stability, fast frequency support, hybrid power plants, and inverter-based resource dynamics.</p>
      </div>
      <ol class="publication-numbered-list publication-focus-list">
        {% for publication_title in dynamics_titles %}
          {% assign post = site.publications | where: "title", publication_title | first %}
          {% if post %}
            {% assign focus_number = focus_number | plus: 1 %}
            <li value="{{ focus_number }}">
              {% include publication-list-item.html post=post %}
            </li>
          {% endif %}
        {% endfor %}
      </ol>
    </section>

    <section class="publication-cluster">
      <div class="publication-cluster__summary">
        <p class="publication-cluster__eyebrow">Cluster 3</p>
        <h3>Grid Planning with Renewables</h3>
        <p>Capacity expansion, transmission planning, resource adequacy, voltage stability, renewable integration, and scalable grid-computation methods.</p>
      </div>
      <ol class="publication-numbered-list publication-focus-list">
        {% for publication_title in planning_titles %}
          {% assign post = site.publications | where: "title", publication_title | first %}
          {% if post %}
            {% assign focus_number = focus_number | plus: 1 %}
            <li value="{{ focus_number }}">
              {% include publication-list-item.html post=post %}
            </li>
          {% endif %}
        {% endfor %}
      </ol>
    </section>

    <section class="publication-cluster">
      <div class="publication-cluster__summary">
        <p class="publication-cluster__eyebrow">Cluster 4</p>
        <h3>Cyber-Physical Co-Simulation</h3>
        <p>Transmission-and-distribution co-simulation, distributed energy resource integration, communication-aware control, and scalable grid digital twins.</p>
      </div>
      <ol class="publication-numbered-list publication-focus-list">
        {% for publication_title in cosim_titles %}
          {% assign post = site.publications | where: "title", publication_title | first %}
          {% if post %}
            {% assign focus_number = focus_number | plus: 1 %}
            <li value="{{ focus_number }}">
              {% include publication-list-item.html post=post %}
            </li>
          {% endif %}
        {% endfor %}
      </ol>
    </section>
  </div>
</section>
</div>
