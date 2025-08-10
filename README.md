![Build](https://github.com/abs-hasan/ab-testing-search-ranking-impact/actions/workflows/ci.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.10%20|%203.11-blue)
![Last commit](https://img.shields.io/github/last-commit/abs-hasan/ab-testing-search-ranking-impact)
![Issues](https://img.shields.io/github/issues/abs-hasan/ab-testing-search-ranking-impact)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)



# 📊 A/B Testing : Search Ranking Impact

**🚀 Did a new search ranking system increase user bookings?**  
This project investigates that question through a full A/B testing workflow — from sanity checks to deep segment analysis.

---

## 🧠 Project Summary

In this analysis, we simulate a real-world scenario where an online travel agency is testing a new **search algorithm (variant)** against the current one (control). The goal is to evaluate **conversion uplift**, **booking speed**, and **performance across user segments**.

We analyze 17,000+ user sessions using Python, applying statistical techniques to determine whether the new experience positively impacts key business metrics.

---

## 🎯 Business Objective

- ✅ Increase **booking conversions**
- ✅ Reduce **time to booking**
- ✅ Identify **which user segments benefit most**

The leadership team needs statistically sound evidence to decide whether to **roll out the new ranking algorithm**.

---

## 📁 Dataset Overview

The dataset consists of two files:

- `sessions_data.csv`: Contains session-level browsing and booking behavior
- `users_data.csv`: Contains user type (`guest` vs `logged_in`) and experiment group assignment (`control` or `variant`)

---

## 🧪 A/B Testing Structure

| Metric Type        | Metric                     | Test Used              | Significance Level |
|--------------------|----------------------------|------------------------|---------------------|
| Sanity Check       | Sample Ratio Mismatch (SRM)| Chi-square test        | α = 0.01            |
| Primary Metric     | Conversion Rate            | Chi-square test        | α = 0.1             |
| Guardrail Metric   | Time to Booking            | Mann-Whitney U test    | α = 0.1             |
| Segment Analysis   | Conversion by User Segment | Grouped Mean Comparison| -                   |

---

## ✅ Key Findings

### 1⃣ Sanity Check (SRM)
- ✅ **Passed**: Users were **evenly split** between control and variant.
- **p-value = 0.6658**, Chi-squared = 0.19

> Ensures random assignment wasn't biased and experiment setup was valid.

---

### 2⃣ Primary Metric: Conversion Rate

| Group     | Conversion Rate |
|-----------|------------------|
| Control   | 15.92%           |
| Variant   | 18.19%           |
| **Lift**  | **+14.22%**      |
| **p-value** | **0.0002**     |

- ✅ Statistically significant improvement
- ✅ Business-impactful effect size
- 🧬 90% Confidence Interval for Lift: [+1.26%, +3.27%]

> 💡 **Recommendation:** Roll out the new search algorithm. The variant significantly increased bookings.

---

### 3⃣ Guardrail Metric: Time to Booking

| Group     | Avg Time to Book |
|-----------|------------------|
| Control   | ~X mins (simulated) |
| Variant   | ~0.79% faster     |
| **p-value** | 0.3699 (not significant) |

> ⛔ The variant didn’t make booking significantly faster — but it also didn’t make it worse.

---

### 4⃣ Segment Deep-Dive

| Segment        | Control Conversion | Variant Conversion |
|----------------|--------------------|---------------------|
| Casual Users   | 16.14%             | **17.72%**          |
| Engaged Users  | 15.82%             | **18.42%**          |

- ✅ **Both user types** saw improvement
- 📈 Larger lift for **Engaged Users**

---

## 💠 Tools & Techniques Used

- **Python** (Pandas, NumPy, Seaborn, Matplotlib)
- **Statistical Tests**: Chi-square, Mann-Whitney U, Confidence Intervals
- **Data Merging, Cleaning, Aggregation**
- **Segmented Visualizations** (Engagement segments, conversion rate distributions)

---

## 🧾 Conclusion & Recommendation

The new search experience **significantly increased conversion rates** across all user types without negatively affecting time to booking. There is **strong statistical evidence** to support a **company-wide rollout** of the new algorithm.

> 📢 **Final Verdict**: ✅ Roll out the new search ranking system!

---

## 📌 How This Adds Value

✅ Real-world scenario  
✅ Full experimentation flow  
✅ Business-driven insights  
✅ Visual + statistical interpretation  
✅ Storytelling ready for stakeholders

---

## 📂 Project Files

- `notebook.ipynb`: Full analysis
- `segmented_conversion_rate.png`: Visualization of conversions by user segment
- `AB_testing_report.pdf`: Original problem statement and reference

