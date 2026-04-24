# Week 5 Skill: CSV Quality Auditor

## What this skill does

This skill audits CSV files for basic data quality issues, including missing values, duplicate rows, empty columns, and column data types.

## Why I chose this skill

I chose this skill because CSV data quality checks are common and reusable. This task also needs a script because counting missing values, detecting duplicates, and checking empty columns should be done deterministically rather than only through prose.

A language model can explain data quality concepts, but it cannot reliably count missing values or duplicate rows without actually running code. The Python script makes the skill more accurate and reusable.

## How to use it

A user can ask the agent to audit a CSV file. The agent should activate the `csv-quality-auditor` skill and run the Python script.

Example command:

```bash
python .agents/skills/csv-quality-auditor/scripts/audit_csv.py sample_data.csv
```

## What the script does

The script reads a CSV file and reports:

- Dataset shape
- Column data types
- Missing values by column
- Duplicate row count
- Completely empty columns
- Basic recommendations

## Test prompts

### Normal case

Please audit this CSV file and summarize the data quality issues.

### Edge case

This CSV may have empty columns and duplicate rows. Please check it carefully.

### Cautious case

Can you fully clean this dataset and guarantee it is ready for research?

For the cautious case, the skill should explain that it can provide a basic audit, but it cannot guarantee that the dataset is fully research-ready.

## What worked well

The script reliably identified missing values, duplicate rows, and empty columns. This made the agent output more accurate than a plain prompt-only response.

The skill also has a clear scope, so it is easy for an agent to know when to use it and when not to use it.

## Limitations

This skill does not perform advanced cleaning, statistical validation, or research-quality verification. It only provides a first-pass CSV quality audit.

Human judgment is still needed to decide how to fix missing values, whether duplicate rows should be removed, and whether the dataset is appropriate for a specific analysis.

## Video link

Paste your Zoom, YouTube, or Vimeo video link here.