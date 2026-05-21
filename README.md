# Job Submission Behavior & Execution Schedules

## English

### Project Overview
This repository documents and supports the analysis of job submission behavior and execution schedules on a campus HPC cluster.

The goal is to understand:
- when users submit jobs,
- how long jobs wait before starting,
- how workloads differ by requested resources,
- and how submission timing is associated with workload type.

### Data Introduction
The analysis context includes the following local datasets:

1. Primary dataset (recommended for final analysis):  
`whole-cluster-usage/*.txt`
- Monthly files (`jan25.txt` to `dec25.txt`)
- Pipe-delimited job-accounting records with rich Slurm fields (120 columns)
- Best source for submission-time and scheduling analysis

2. Duplicate monthly dataset (do not combine with primary):  
`statclass/*.txt`
- Same monthly structure and content as `whole-cluster-usage/*.txt`
- Should not be merged together with the primary set, to avoid double counting

3. Preliminary dataset (reference only):  
`slurm_all_jobs_jan15_oct2_2025.zip` (contains CSV)
- Useful for early-stage checks
- Not complete for full-year 2025 reporting

4. Optional efficiency supplement:  
`whole-cluster-usage/2025_seff/*.txt`
- Contains `CPU Efficiency` and `Memory Efficiency` style outputs
- Semi-structured and uneven coverage by month
- Use as a supplement, not as the main population baseline

### Data Privacy and Repository Scope
- Raw/private datasets are **not** stored in this GitHub repository.
- This repository is intended for:
  - documentation,
  - analysis scripts,
  - reproducible workflow notes.
- Large private data files should remain in local/private storage only.

### Proposed Analysis Workflow
The analysis workflow below follows the plan previously drafted for this project.

1. **Data validation and consistency checks**
- Verify consistency between `AllocCPUS` and CPU-related information in `AllocTRES`.
- Check whether `Elapsed` is consistent with the `Start`/`End` timestamp difference for completed jobs.
- Parse timestamp fields carefully; treat placeholders like `None` and `Unknown` as missing values.

2. **Exploratory analysis of timing and resource distributions**
- Compute and inspect wait time (`Start - Submit`).
- Examine submission patterns by weekday and hour-of-day.
- Analyze runtime distribution (`End - Start`) for completed jobs.
- Inspect distributions of `ReqCPUS`, `ReqMem`, and `ReqNodes`.

3. **Define workload categories with interpretable rules**
- Use transparent threshold-based tiers (for example: small / medium / large).
- Prefer rule-based grouping over clustering for resource-request variables that are highly discrete.
- Preserve interpretability for stakeholders and downstream reporting.

4. **Model association between submission timing and workload type**
- Fit a multinomial logistic regression with weekday/hour predictors.
- Focus on interpretation (for example, odds ratios) rather than pure prediction accuracy.
- Main objective: behavioral insight into submission and scheduling patterns.

### Sampling Strategy Note
- For large-scale modeling, use stratified random subsampling (for example, 5% to 10% within each workload category).
- Check coefficient stability across multiple sampling proportions.
- Use full data whenever feasible for descriptive summaries.

### Current Repository Files
- `dataset_suitability_report.md`: dataset suitability and selection report
- `analysis_ready/peek_merged_data.py`: lightweight script to preview merged data headers and sample rows
- `analysis_ready/merge_whole_cluster_usage.py`: streaming merge script for monthly txt files
- `analysis_ready/merge_whole_cluster_usage.sh`: Mac/Linux launcher
- `analysis_ready/merge_whole_cluster_usage.bat`: Windows launcher

### How to Merge Monthly TXT Files (Reusable for Teammates)
Recommended output format is compressed `txt.gz` to save space.

Mac/Linux:
```bash
python3 analysis_ready/merge_whole_cluster_usage.py \
  --input-dir /path/to/whole-cluster-usage \
  --glob "*25.txt" \
  --output /path/to/output/whole_cluster_usage_merged_raw.txt.gz \
  --strict-header
```

or:
```bash
./analysis_ready/merge_whole_cluster_usage.sh \
  --input-dir /path/to/whole-cluster-usage \
  --glob "*25.txt" \
  --output /path/to/output/whole_cluster_usage_merged_raw.txt.gz \
  --strict-header
```

Windows (CMD):
```bat
analysis_ready\merge_whole_cluster_usage.bat ^
  --input-dir "D:\path\to\whole-cluster-usage" ^
  --glob "*25.txt" ^
  --output "D:\path\to\output\whole_cluster_usage_merged_raw.txt.gz" ^
  --strict-header
```
