---
name: csv-quality-auditor
description: Audits CSV files for missing values, duplicate rows, empty columns, and basic data quality issues. Use when the user asks to inspect, validate, or summarize the quality of a CSV dataset.
---

# CSV Quality Auditor

## When to use this skill

Use this skill when the user provides a CSV file and asks to inspect, audit, validate, or summarize data quality issues.

This skill is especially useful when the user wants to understand whether a CSV file has common quality problems before analysis.

## When not to use this skill

Do not use this skill for advanced statistical modeling, machine learning, deep data cleaning, or guaranteeing that a dataset is fully research-ready.

Do not use this skill when the user only wants general advice and does not provide a CSV file or file path.

## Expected inputs

The expected input is a CSV file path provided by the user.

Example:

```bash
sample_data.csv
