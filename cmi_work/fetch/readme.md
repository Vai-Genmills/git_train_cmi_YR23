

# Marketing Measurement & Data Science Analysis

## Overview
Our marketing analytics journey utilizes **1st-party consumer data** to build predictive models and actionable insights. By analyzing:
- **Purchase history**
- **Demographics**
- **Store/Product affinities**

We create **embeddings** for products and consumers, transforming them into **dense features**. These features feed into supervised propensity models to predict purchase likelihood across 179 product lines.

Through this process, we build:
- **Product relationship insights**
- **Customer personas**

These insights help power recommendation systems and more targeted marketing strategies. Our focus shifts from **demographic-based segments** to **data-driven audience segments** for each brand.

---

## Objective
Our goal is to measure the impact of marketing campaigns by evaluating how targeted marketing influences consumer behavior and calculating the **incremental sales lift** achieved through these campaigns.

---

## Closed-Loop Measurement
The closed-loop measurement process involves:

1. **Data Ingestion**: Collecting and transforming data from multiple sources.
2. **Modeling**: Using machine learning models to predict top consumers for ad targeting.
3. **Ad Campaign Execution**: Tracking responses (impressions, clicks) to ads.
4. **Transaction Tracking**: Monitoring whether consumers made purchases related to the targeted products.

We use a **control group** to form a baseline for measuring **incremental sales lift**, comparing the test (exposed) group against the control group.

---

## Key Stakeholders & Roles

- **Advertiser**: Provides consumer data and media assets for the campaign.
- **Media Agency**: Expands the target audience using lookalike models to identify similar users across the population.
- **Clean Room**: Tracks impressions and clicks through DSP (Demand-Side Platform) feedback.
- **Firn**: Closes the loop by tracking actual purchases and quantifying the effect of targeted ads.

---

## Sections Covered

1. **Media Activation Journey**: Components and timelines for media campaigns.
2. **Key Terms & Glossary**: Definitions of essential marketing and media terms.
3. **Sales Lift Analysis**: Calculation and analysis of sales lift for targeted vs control users.
4. **Clean Room Operations**: Explanation of how DSP feedback is processed.
5. **Weighted Control Allocation**: Method for balancing test and control cohorts.
6. **Technical Execution**: Step-by-step guide for measurement processes.
7. **Audience Optimization**: Learnings from media responses for better targeting.

---

This README provides a comprehensive overview of how **data-driven marketing** is conducted, from segmentation to closed-loop measurement, leveraging cutting-edge tools and models to optimize campaign performance.
