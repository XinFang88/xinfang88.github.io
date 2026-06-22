---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my full publication record on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% assign chronological_numbered_publications = site.publications | sort: "date" %}
{% assign chronological_publications = site.publications | sort: "date" | reverse %}
{% assign publication_count = chronological_publications | size %}
{% capture optimization_titles %}Stable Relay Learning Optimization Approach for Fast Power System Production Cost Minimization Simulation|On the Decomposition of Locational Marginal Hydrogen Pricing−Part II: Solution Approach and Numerical Results|Addressing Wind Power Forecast Errors in Day-Ahead Pricing With Energy Storage Systems: A Distributionally Robust Joint Chance-Constrained Approach|Implications of electricity and gas price coupling in US New England region|DLMP of Competitive Markets in Active Distribution Networks: Models, Solutions, Applications, and Visions|How Can Probabilistic Solar Power Forecasts Be Used to Lower Costs and Improve Reliability in Power Spot Markets? A Review and Application to Flexiramp Requirements|State-of-the-art short-term electricity market operation with solar generation: A review|Two-stage stochastic optimization frameworks to aid in decision-making under uncertainty for variable resource generators participating in a sequential energy market|Redesigning capacity market to include flexibility via ramp constraints in high-renewable penetrated system|Practical Operations of Energy Storage Providing Ancillary Services: From Day-Ahead to Real-Time|Analytical Model of Day-ahead and Real-time Price Correlation in Strategic Wind Power Offering|A clustering-based scenario generation framework for power market simulation with wind integration|Deliverable Flexible Ramping Products Considering Spatiotemporal Correlation of Wind Generation and Demand Uncertainties|Linear Approximation Line Pack Model for Integrated Electricity and Natural Gas Systems OPF|Analysis of Wind Ramping Product Formulations in a Ramp-constrained Power Grid|Distributionally-robust chance constrained and interval optimization for integrated electricity and natural gas systems optimal power flow with wind uncertainties|Multi-Stage Stochastic Programming to Joint Economic Dispatch for Energy and Reserve With Uncertain Renewable Energy|Adjustable and distributionally robust chance-constrained economic dispatch considering wind power uncertainty|Decentralized wind uncertainty management: Alternating direction method of multipliers based distributionally-robust chance constrained optimal power flow|Introducing Uncertainty Components in Locational Marginal Prices for Pricing Wind Power and Load Uncertainties|Capacity Market Model Considering Flexible Resource Requirements|Potential of Wind Power to Provide Flexible Ramping Products and Operating Reserve|Mean-Variance Optimization-Based Energy Storage Scheduling Considering Day-Ahead and Real-Time LMP Uncertainties|Modelling wind power spatial-temporal correlation in multi-interval optimal power flow: A sparse correlation matrix approach|Bilevel Arbitrage Potential Evaluation for Grid-Scale Energy Storage Considering Wind Power and LMP Smoothing Effect|Hybrid component and configuration model for combined-cycle units in unit commitment problem|Multi-dimensional assessment of the developing situation of provincial electricity market considering the external economic factors|Evaluation of LMP Intervals Considering Wind Uncertainty|Day-ahead coordinated operation of utility-scale electricity and natural gas networks considering demand response based virtual power plants|Strategic CBDR bidding considering FTR and wind power|Strategic scheduling of energy storage for load serving entities in locational marginal pricing market|Coupon-Based Demand Response Considering Wind Power Uncertainty: A Strategic Bidding Model for Load Serving Entities|An approach to assess the responsive residential demand to financial incentives|The impact of FTR on LSE's strategic bidding considering coupon based demand response{% endcapture %}
{% capture dynamics_titles %}Holistic Stability Region Evaluation of Low Inertia Power System Frequency Response|Enhancing Island Power Systems Operational Flexibility with Hybrid Power Plants|Inertia Estimation for Stability-Constrained Economic Dispatch of IBR Penetrated Grid|Analytical Small-signal Stability Analysis of Low-Inertia Power System Frequency Response Considering Secondary Frequency Regulation|Multi-Timescale Hydro Modeling with Integrated Hydrological Conditions: Flexibility Analysis and Its Impact on Grid Stability|Virtual Inertia Synthesis and Control: Informative and Relevant|Dynamics-incorporated Modeling Framework for Stability Constrained Scheduling Under High-penetration of Renewable Energy|Multi-timescale optimal operation framework for integrated economic and reliability analysis of hybrid power plants|Power Sharing-Based Framework for Allocating Automatic Generation Control in Distributed Energy Resources|Multi-Timescale Modeling Framework of Hybrid Power Plants Providing Secondary Frequency Regulation|Frequency Security-Constrained Unit Commitment with Fast Frequency Support of DFIG-Based Wind Power Plants|Electric Vehicles Charging Time Constrained Deliverable Provision of Secondary Frequency Regulation|A unified analytical method to quantify three types of fast frequency response from inverter-based resources|Developing Frequency Stability Constraint for Unit Commitment Problem Considering High Penetration of Renewables|Battery degradation modeling in hybrid power plants: An island system unit commitment study|Impact of Transportation Electrification on the System's Dynamic Frequency Response|Manage Real-Time Power Imbalance With Renewable Energy: Fast Generation Dispatch or Adaptive Frequency Regulation?|On Thermal Dynamics Embedded Static Voltage Stability Margin|A comparison of machine learning methods for frequency nadir estimation in power systems|Secondary Frequency Regulation from Variable Generation Through Uncertainty Decomposition: An Economic and Reliability Perspective|Real-Time Dispatch With Secondary Frequency Regulation: A Pathway to Consider Intra-Interval Fluctuations|Providing Ancillary Services with Photovoltaic Generation in Multi-Timescale Grid Operation|Application of battery-supercapacitor energy storage system for smoothing wind power output: An optimal coordinated control strategy{% endcapture %}
{% capture planning_titles %}Frequency Stability Constrained Capacity Expansion Planning through Virtual Inertia and Droop Capacities Allocation of IBRs|Energy Equity-Aware Load Shedding Optimization Methodology|DC Near-area Voltage Stability Constrained Renewable Energy Integration for Regional Power Grids|Frequency Nadir Constrained Unit Commitment for High Renewable Penetration Island Power Systems|Distributed PV Hosting Capacity Evaluation Considering Equitable PV Accommodation|A Medium-/Low-Voltage Joint State Estimator Through Linear Uncertainty Propagation|Effective Parallelism for Equation and Jacobian Evaluation in Large-Scale Power Flow Calculation|Available Transfer Capability Calculations Considering Demand Response|Available transfer capability evaluation in a deregulated electricity market considering correlated wind power|Mitigate overestimation of voltage stability margin by coupled single-port circuit models|System Load Margin Evaluation using Mixed-Integer Conic Optimization|Distribution Network Reconfiguration with Aggregated Electric Vehicle Charging Strategy|Reactive power planning under high penetration of wind energy using Benders decomposition|Probabilistic available transfer capability evaluation for power systems including high penetration of wind power|Reactive power planning considering high penetration of wind energy|Capacity Credit Evaluation of Photovoltaic Generation Based on System Reserve Capacity|The Probabilistic Production Simulation for Mixed Wind-Hydro-Thermal Power System and the Sensitivity Analysis for the Indices of Abandoned Wind{% endcapture %}
{% capture cosim_titles %}Sumo x PyPSA: Interactive Web Demo of Real-Time Urban Power-Traffic Co-Simulation with Vehicle-to-Grid|Distributed Optimization and Control for Autonomous Distributed Energy Resource Power Dispatch and Frequency Regulation Considering Communication Failures|Co-Simulation of PSS/E, OpenDSS, and PSCAD for Power Systems Stability Analysis With Inverter-Based Resources|Distributed Automatic Generation Control Considering DPV Using T&D Dynamic Co-Simulation|Demonstrating the transient system impact of cyber-physical events through scalable transmission and distribution (T&D) co-simulation|Transmission-distribution dynamic co-simulation of electric vehicles providing grid frequency response|Cyber-Physical Event Emulation-Based Transmission-and-Distribution Co-simulation for Situational Awareness of Grid Anomalies (SAGA)|Impact of DER Communication Delay in AGC: Cyber-Physical Dynamic Simulation|Transmission-and-Distribution Dynamic Co-Simulation Framework for Distributed Energy Resource Frequency Response|Load altering attack-tolerant defense strategy for load frequency control system|A Framework of Residential Demand Aggregation With Financial Incentives{% endcapture %}

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
  #publication-option-focus:checked ~ #publication-view-focus,
  #publication-option-type:checked ~ #publication-view-type {
    display: block;
  }

  #publication-option-chronological:checked ~ .publication-view-toggle label[for="publication-option-chronological"],
  #publication-option-focus:checked ~ .publication-view-toggle label[for="publication-option-focus"],
  #publication-option-type:checked ~ .publication-view-toggle label[for="publication-option-type"] {
    background-color: #3b5f88;
    color: #fff;
  }
</style>

<div class="publication-switcher">
<input class="publication-view-radio" type="radio" name="publication-view-option" id="publication-option-chronological" checked>
<input class="publication-view-radio" type="radio" name="publication-view-option" id="publication-option-focus">
<input class="publication-view-radio" type="radio" name="publication-view-option" id="publication-option-type">

<div class="publication-view-toggle" aria-label="Publication list view">
  <label class="btn" for="publication-option-chronological">Chronological</label>
  <label class="btn" for="publication-option-focus">By Research Focus</label>
  <label class="btn" for="publication-option-type">By Publication Type</label>
</div>

<section id="publication-view-chronological" class="publication-view publication-view--chronological">
  <ol class="publication-numbered-list" reversed start="{{ publication_count }}">
    {% for post in chronological_publications %}
      <li>
        {% include publication-list-item.html post=post %}
      </li>
    {% endfor %}
  </ol>
</section>

<section id="publication-view-focus" class="publication-view publication-view--focus">
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
            {% assign publication_number = 0 %}
            {% for numbered_post in chronological_numbered_publications %}
              {% if numbered_post.title == post.title %}
                {% assign publication_number = forloop.index %}
              {% endif %}
            {% endfor %}
            <li value="{{ publication_number }}">
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
            {% assign publication_number = 0 %}
            {% for numbered_post in chronological_numbered_publications %}
              {% if numbered_post.title == post.title %}
                {% assign publication_number = forloop.index %}
              {% endif %}
            {% endfor %}
            <li value="{{ publication_number }}">
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
            {% assign publication_number = 0 %}
            {% for numbered_post in chronological_numbered_publications %}
              {% if numbered_post.title == post.title %}
                {% assign publication_number = forloop.index %}
              {% endif %}
            {% endfor %}
            <li value="{{ publication_number }}">
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
            {% assign publication_number = 0 %}
            {% for numbered_post in chronological_numbered_publications %}
              {% if numbered_post.title == post.title %}
                {% assign publication_number = forloop.index %}
              {% endif %}
            {% endfor %}
            <li value="{{ publication_number }}">
              {% include publication-list-item.html post=post %}
            </li>
          {% endif %}
        {% endfor %}
      </ol>
    </section>
  </div>
</section>
<section id="publication-view-type" class="publication-view publication-view--type">
  <div class="publication-cluster-list">
    <section class="publication-cluster">
      <div class="publication-cluster__summary">
        <h3>Journal Papers</h3>
      </div>
      <ol class="publication-numbered-list publication-focus-list">
        {% for post in chronological_publications %}
          {% if post.publication_type != "conference" %}
            {% assign publication_number = 0 %}
            {% for numbered_post in chronological_numbered_publications %}
              {% if numbered_post.title == post.title %}
                {% assign publication_number = forloop.index %}
              {% endif %}
            {% endfor %}
            <li value="{{ publication_number }}">
              {% include publication-list-item.html post=post %}
            </li>
          {% endif %}
        {% endfor %}
      </ol>
    </section>

    <section class="publication-cluster">
      <div class="publication-cluster__summary">
        <h3>Conference Papers</h3>
      </div>
      <ol class="publication-numbered-list publication-focus-list">
        {% for post in chronological_publications %}
          {% if post.publication_type == "conference" %}
            {% assign publication_number = 0 %}
            {% for numbered_post in chronological_numbered_publications %}
              {% if numbered_post.title == post.title %}
                {% assign publication_number = forloop.index %}
              {% endif %}
            {% endfor %}
            <li value="{{ publication_number }}">
              {% include publication-list-item.html post=post %}
            </li>
          {% endif %}
        {% endfor %}
      </ol>
    </section>
  </div>
</section>

</div>
