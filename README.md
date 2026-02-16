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

---

## 中文

### 项目概述
本仓库用于支持和记录校园集群（HPC）中作业提交行为（Job Submission Behavior）与执行调度时序（Execution Schedules）的分析工作。

核心目标包括：
- 用户在什么时间提交作业；
- 作业从提交到开始执行的等待特征；
- 不同资源请求规模的作业结构；
- 提交时间与作业类型之间的关联关系。

### 数据介绍
当前分析涉及以下本地数据集：

1. 主数据集（最终分析推荐）：  
`whole-cluster-usage/*.txt`
- 按月文件（`jan25.txt` 到 `dec25.txt`）
- `|` 分隔的 Slurm 作业记录，字段较完整（120列）
- 最适合用于提交行为与调度时序分析

2. 重复月度数据集（不要与主表同时合并）：  
`statclass/*.txt`
- 与 `whole-cluster-usage/*.txt` 在结构与内容上重复
- 若同时使用会造成重复计数

3. Preliminary 数据（仅参考）：  
`slurm_all_jobs_jan15_oct2_2025.zip`（内含 CSV）
- 可用于早期探索
- 不适合作为 2025 全年最终结论的数据底座

4. 可选补充数据（效率指标）：  
`whole-cluster-usage/2025_seff/*.txt`
- 包含 `CPU Efficiency`、`Memory Efficiency` 等信息
- 结构为半结构化文本，且各月覆盖不均匀
- 建议仅作补充，不作为总体样本基数

### 数据隐私与仓库边界
- 原始/私有数据 **不上传** 到本 GitHub 仓库。
- 本仓库仅用于存放：
  - 文档，
  - 分析脚本，
  - 可复现流程说明。
- 大体量私有数据文件应保留在本地或私有存储中。

### 后续分析流程（按既定方案）
以下流程沿用你此前制定的分析计划结构。

1. **数据校验与一致性检查**
- 检查 `AllocCPUS` 与 `AllocTRES` 中 CPU 信息是否一致。
- 对已完成作业，核对 `Elapsed` 与 `Start/End` 差值是否一致。
- 时间字段统一解析，并将 `None`、`Unknown` 等占位值视为缺失值。

2. **时序与资源分布的探索性分析**
- 计算并分析等待时间（`Start - Submit`）分布。
- 按星期与小时分析作业提交模式。
- 对已完成作业分析运行时长（`End - Start`）分布。
- 查看 `ReqCPUS`、`ReqMem`、`ReqNodes` 的分布特征。

3. **基于可解释规则定义工作负载类别**
- 使用阈值规则定义 small / medium / large 等类别。
- 对高度离散、阶梯型资源请求变量，优先采用规则分组而非聚类。
- 保持结果可解释、可沟通。

4. **建模提交时段与工作负载类型的关联**
- 使用星期/小时作为解释变量，建立多项 Logit（multinomial logistic regression）模型。
- 重点解释系数（如 odds ratio），而非单纯追求预测精度。
- 核心目标是行为洞察与调度理解。

### 采样策略说明
- 在模型阶段可采用分层随机抽样（例如各工作负载层内抽取 5%~10%）。
- 对不同采样比例进行稳健性检查（比较系数稳定性）。
- 描述统计部分在计算可承受时尽量使用全量数据。

### 当前仓库文件
- `dataset_suitability_report.md`：数据集适配性与选型报告
- `analysis_ready/peek_merged_data.py`：轻量预览脚本（查看表头与前几行样本）
- `analysis_ready/merge_whole_cluster_usage.py`：按月 txt 流式合并脚本
- `analysis_ready/merge_whole_cluster_usage.sh`：Mac/Linux 启动脚本
- `analysis_ready/merge_whole_cluster_usage.bat`：Windows 启动脚本

### 如何合并月度 TXT（可直接给同学复用）
建议输出为压缩的 `txt.gz`，节省空间。

Mac/Linux：
```bash
python3 analysis_ready/merge_whole_cluster_usage.py \
  --input-dir /path/to/whole-cluster-usage \
  --glob "*25.txt" \
  --output /path/to/output/whole_cluster_usage_merged_raw.txt.gz \
  --strict-header
```

或者：
```bash
./analysis_ready/merge_whole_cluster_usage.sh \
  --input-dir /path/to/whole-cluster-usage \
  --glob "*25.txt" \
  --output /path/to/output/whole_cluster_usage_merged_raw.txt.gz \
  --strict-header
```

Windows（CMD）：
```bat
analysis_ready\merge_whole_cluster_usage.bat ^
  --input-dir "D:\path\to\whole-cluster-usage" ^
  --glob "*25.txt" ^
  --output "D:\path\to\output\whole_cluster_usage_merged_raw.txt.gz" ^
  --strict-header
```
