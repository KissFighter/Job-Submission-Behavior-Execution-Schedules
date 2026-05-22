# Job Submission Behavior & Execution Schedules

This repository presents an HPC / SLURM workload analysis project focused on how users submit jobs, how long those jobs wait in queue, and how resource demand relates to scheduling outcomes. It combines a large-scale preprocessing pipeline for raw SLURM accounting logs, local generation of derived job-level datasets, and notebooks for exploratory and early predictive analysis of submission timing, wait time, runtime, CPU/GPU workloads, and queue behavior.

## Open First

- Open `notebooks/02_job_submission_behavior_analysis.ipynb` first for the main analytical story.
- Open `notebooks/01_build_master_2025.ipynb` if you want to inspect the preprocessing and feature-engineering pipeline that generates the local derived tables.

## Project Overview

The project treats HPC usage data as an end-to-end analysis workflow:

- merge large monthly SLURM accounting logs,
- validate schema and clean missing or inconsistent fields,
- engineer job-level scheduling features such as wait time and runtime,
- build local derived tables for analysis,
- and study how submission timing, requested resources, and workload type relate to scheduling outcomes.

The emphasis is on technically grounded workflow design rather than polished final scientific claims. The repository is meant to show a reproducible analysis pipeline and a clear analytical direction.

## Research Questions

- When do users submit jobs across weekdays and hours of day?
- How are queue wait times distributed, and which jobs wait the longest?
- How do requested CPUs, memory, nodes, and GPUs relate to wait time and execution behavior?
- How do GPU workloads differ from CPU-only workloads?
- Can workload features and submission timing help explain queue behavior?

## Repository Structure

```text
.
├── README.md
├── environment.yml
├── requirements.txt
├── analysis_ready/
│   ├── merge_whole_cluster_usage.py
│   ├── merge_whole_cluster_usage.sh
│   ├── merge_whole_cluster_usage.bat
│   └── peek_merged_data.py
├── notebooks/
│   ├── 01_build_master_2025.ipynb
│   └── 02_job_submission_behavior_analysis.ipynb
├── docs/
│   ├── data_preprocessing_notes.pdf
│   ├── analysis_workflow_notes.pdf
│   ├── project_problem_statement.pdf
│   ├── project_report_midterm.pdf
│   ├── project_slides_midterm.pdf
│   ├── project_report_final.pdf
│   └── project_slides_final.pdf
└── dataset_suitability_report.md
```

### What each part contains

- `analysis_ready/`: scripts for merging and previewing monthly SLURM accounting files before notebook-based processing.
- `notebooks/01_build_master_2025.ipynb`: preprocessing pipeline that validates schema, cleans records, engineers features, and builds local derived job-level outputs.
- `notebooks/02_job_submission_behavior_analysis.ipynb`: main exploratory and modeling notebook covering wait-time behavior, submission timing, resource demand, GPU vs CPU comparisons, and workload-related queue analysis.
- `outputs/`: local generated directory for derived analysis tables. It is intentionally ignored and not tracked in the public repository.
- `docs/`: supporting project materials, including preprocessing notes, workflow notes, reports, and presentation slides.
- `dataset_suitability_report.md`: supporting note on data source selection and dataset scope.

## Reproducibility

This repository is structured so the workflow can be re-run locally without publishing raw cluster data.

1. Create the environment from `environment.yml` or `requirements.txt`.
2. Prepare the merged raw SLURM accounting file locally using the scripts in `analysis_ready/`.
3. Run `notebooks/01_build_master_2025.ipynb` to build the derived 2025 job-level tables locally under `outputs/`.
4. Open `notebooks/02_job_submission_behavior_analysis.ipynb` to inspect exploratory results and queue-related modeling work.

## Public / Private Data Boundary

- Raw cluster data is not stored in this repository.
- Monthly source logs, duplicate raw exports, and private local datasets remain excluded.
- Only code, workflow notes, notebooks, and selected project documents are intended to be public here.
- Derived job-level tables are generated locally and are not committed to the public repository.

## Project Status

Current repository status:

- preprocessing pipeline is in place,
- the preprocessing pipeline can generate derived 2025 job-level tables locally,
- exploratory analysis notebook is available,
- queue and workload modeling is exploratory and still evolving,
- and repository presentation is being refined for clearer public documentation.

## Scope Notes

This repository is not presented as a finished scientific paper. It is a technically grounded project workspace for:

- large-scale preprocessing,
- feature engineering,
- HPC scheduling behavior analysis,
- GPU vs CPU workload comparison,
- and queue / wait-time modeling.

That framing is intentional: the project is strongest as an end-to-end reproducible analysis repo rather than as a polished final report.
