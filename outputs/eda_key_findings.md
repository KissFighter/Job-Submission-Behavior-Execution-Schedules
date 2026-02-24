# EDA Key Findings (Job-Level, 2025)

- Jobs are most frequently submitted on **Tuesday** (16.09%), and peak submission hour is **15** (6.26%).
- Median wait time is **0.42 h**, p90 is **13.01 h**, p95 is **31.13 h**.
- For COMPLETED jobs, median runtime is **0.02 h**, p90 is **1.06 h**.
- GPU jobs account for **6.36%** of jobs.
- Wait decomposition: Submit->Eligible median **0.00 h**, Eligible->Start median **0.20 h**; dominant segment: **Eligible->Start (QueueWait)**.
- GPU vs non-GPU median wait: **0.09 h** vs **0.44 h** (ratio: **0.20x**).

## Saved figures
- `/private/tmp/Job-Submission-Behavior-Execution-Schedules-fresh/outputs/figures/03_state_distribution.png`
- `/private/tmp/Job-Submission-Behavior-Execution-Schedules-fresh/outputs/figures/04_submission_weekday_proportion.png`
- `/private/tmp/Job-Submission-Behavior-Execution-Schedules-fresh/outputs/figures/05_submission_hour_proportion.png`
- `/private/tmp/Job-Submission-Behavior-Execution-Schedules-fresh/outputs/figures/06_partition_top10.png`
- `/private/tmp/Job-Submission-Behavior-Execution-Schedules-fresh/outputs/figures/07_qos_top10.png`
- `/private/tmp/Job-Submission-Behavior-Execution-Schedules-fresh/outputs/figures/08_reqcpus_distribution.png`
- `/private/tmp/Job-Submission-Behavior-Execution-Schedules-fresh/outputs/figures/09_reqmem_distribution_log.png`
- `/private/tmp/Job-Submission-Behavior-Execution-Schedules-fresh/outputs/figures/10_wait_time_distribution.png`
- `/private/tmp/Job-Submission-Behavior-Execution-Schedules-fresh/outputs/figures/11_wait_time_ecdf.png`
- `/private/tmp/Job-Submission-Behavior-Execution-Schedules-fresh/outputs/figures/12_runtime_distribution_completed.png`
- `/private/tmp/Job-Submission-Behavior-Execution-Schedules-fresh/outputs/figures/13_hold_vs_queuewait_boxplot.png`
- `/private/tmp/Job-Submission-Behavior-Execution-Schedules-fresh/outputs/figures/14_gpu_vs_nongpu_wait.png`
- `/private/tmp/Job-Submission-Behavior-Execution-Schedules-fresh/outputs/figures/16_partition_effect_wait.png`