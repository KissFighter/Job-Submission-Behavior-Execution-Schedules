# 数据集适配性评估报告（Job Submission Behavior & Execution Schedules）

- 评估时间：2026-02-16
- 评估范围：`/Volumes/Store/427/iccp-cluster-usage-analysis-selected`
- 评估方法：全部采用流式读取（`awk`/`sed`/`wc`/`unzip -p`），未将大文件一次性读入内存。

## 1. 你的分析目标

你当前要做的是：

1. `Job Submission Behavior`（作业提交行为）
2. `Execution Schedules`（执行时序/调度时序）

因此关键字段应至少覆盖：
- 用户与队列维度：`User`, `Account`, `Partition`, `QOS`, `State`
- 时间维度：`Submit`, `Eligible`, `Start`, `End`, `ElapsedRaw`
- 资源请求维度：`ReqCPUS`, `ReqMem`, `ReqNodes`, `AllocCPUS`, `AllocTRES`

---

## 2. Folder 级数据清单

### 2.1 根目录

路径：`/Volumes/Store/427/iccp-cluster-usage-analysis-selected`

- `slurm_all_jobs_jan15_oct2_2025.zip`（184MB，压缩包，preliminary）
- `statclass/`（12个按月 txt）
- `whole-cluster-usage/`（12个按月 txt + `2025_seff/`）

### 2.2 `statclass/`

- 文件：`jan25.txt` 到 `dec25.txt`（12个）
- 总行数：`6,123,202`（含各文件表头）
- 结论：与 `whole-cluster-usage/` 同名月文件逐字节一致（12/12 identical）

### 2.3 `whole-cluster-usage/`

- 文件：`jan25.txt` 到 `dec25.txt`（12个）
- 总行数：`6,123,202`（含各文件表头）
- 附带子目录：`2025_seff/`

### 2.4 `whole-cluster-usage/2025_seff/`

- 文件：`seff_jan.txt, seff_feb.txt, ..., seff_sep.txt, seff_nov.txt, seff_dec.txt`
- 缺失：`seff_oct.txt`（不存在）
- 总行数：`38,586,024`
- 说明：为半结构化文本（key-value 段落），不是固定列式表

### 2.5 全量文件清单（逐文件）

```text
/Volumes/Store/427/iccp-cluster-usage-analysis-selected/
  .DS_Store
  slurm_all_jobs_jan15_oct2_2025.zip
  statclass/
    apr25.txt
    aug25.txt
    dec25.txt
    feb25.txt
    jan25.txt
    jul25.txt
    jun25.txt
    mar25.txt
    may25.txt
    nov25.txt
    oct25.txt
    sep25.txt
  whole-cluster-usage/
    apr25.txt
    aug25.txt
    dec25.txt
    feb25.txt
    jan25.txt
    jul25.txt
    jun25.txt
    mar25.txt
    may25.txt
    nov25.txt
    oct25.txt
    sep25.txt
    2025_seff/
      .DS_Store
      seff_apr.txt
      seff_aug.txt
      seff_dec.txt
      seff_feb.txt
      seff_jan.txt
      seff_jul.txt
      seff_jun.txt
      seff_mar.txt
      seff_may.txt
      seff_nov.txt
      seff_sep.txt
```

---

## 3. 字段清单（完整）

## 3.1 `whole-cluster-usage/*.txt` 与 `statclass/*.txt`（120字段）

```text
1  Account
2  AdminComment
3  AllocCPUS
4  AllocNodes
5  AllocTRES
6  AssocID
7  AveCPU
8  AveCPUFreq
9  AveDiskRead
10 AveDiskWrite
11 AvePages
12 AveRSS
13 AveVMSize
14 BlockID
15 Cluster
16 Comment
17 Constraints
18 ConsumedEnergy
19 ConsumedEnergyRaw
20 Container
21 CPUTime
22 CPUTimeRAW
23 DBIndex
24 DerivedExitCode
25 Elapsed
26 ElapsedRaw
27 Eligible
28 End
29 ExitCode
30 Extra
31 FailedNode
32 Flags
33 GID
34 Group
35 JobID
36 JobIDRaw
37 JobName
38 Layout
39 Licenses
40 MaxDiskRead
41 MaxDiskReadNode
42 MaxDiskReadTask
43 MaxDiskWrite
44 MaxDiskWriteNode
45 MaxDiskWriteTask
46 MaxPages
47 MaxPagesNode
48 MaxPagesTask
49 MaxRSS
50 MaxRSSNode
51 MaxRSSTask
52 MaxVMSize
53 MaxVMSizeNode
54 MaxVMSizeTask
55 McsLabel
56 MinCPU
57 MinCPUNode
58 MinCPUTask
59 NCPUS
60 NNodes
61 NodeList
62 NTasks
63 Partition
64 Planned
65 PlannedCPU
66 PlannedCPURAW
67 Priority
68 QOS
69 QOSRAW
70 QOSREQ
71 Reason
72 ReqCPUFreq
73 ReqCPUFreqGov
74 ReqCPUFreqMax
75 ReqCPUFreqMin
76 ReqCPUS
77 ReqMem
78 ReqNodes
79 ReqTRES
80 Reservation
81 ReservationId
82 ReqReservation
83 Restarts
84 SegmentSize
85 SLUID
86 Start
87 State
88 StdErr
89 StdIn
90 StdOut
91 Submit
92 SubmitLine
93 Suspended
94 SystemComment
95 SystemCPU
96 Timelimit
97 TimelimitRaw
98 TotalCPU
99 TRESUsageInAve
100 TRESUsageInMax
101 TRESUsageInMaxNode
102 TRESUsageInMaxTask
103 TRESUsageInMin
104 TRESUsageInMinNode
105 TRESUsageInMinTask
106 TRESUsageInTot
107 TRESUsageOutAve
108 TRESUsageOutMax
109 TRESUsageOutMaxNode
110 TRESUsageOutMaxTask
111 TRESUsageOutMin
112 TRESUsageOutMinNode
113 TRESUsageOutMinTask
114 TRESUsageOutTot
115 UID
116 User
117 UserCPU
118 WCKey
119 WCKeyID
120 WorkDir
```

### 3.2 `slurm_all_jobs_jan15_oct2_2025.zip` 内 CSV（19字段）

```text
1  JobID
2  JobIDRaw
3  JobName
4  Partition
5  Account
6  AllocCPUS
7  State
8  ExitCode
9  Start
10 End
11 Elapsed
12 AllocNodes
13 AllocTRES
14 ReqMem
15 ReqCPUS
16 ReqNodes
17 Submit
18 User
19 Group
```

### 3.3 `2025_seff/*.txt`（半结构化 key）

在全量 seff 中出现频率较高的字段键：

- `Job ID`
- `Array Job ID`（仅数组作业）
- `Cluster`
- `User/Group`
- `State`
- `Cores` 或 `Nodes + Cores per node`
- `CPU Utilized`
- `CPU Efficiency`
- `Job Wall-clock time`
- `Memory Utilized`
- `Memory Efficiency`

说明：`seff` 不保证固定列结构，字段会随作业类型变化。

---

## 4. 质量、覆盖率与结构稳定性

### 4.1 `statclass` 与 `whole-cluster-usage` 重复性

- 12个月文件逐月比较结果：`identical`
- 结论：两套月度文件是重复副本，不能同时并入主分析（会重复计数）

### 4.2 `whole-cluster-usage` 结构稳定性（按数据行）

- 总数据行（去掉12个表头）：`6,123,190`
- `NF==120` 的规范行：`6,101,853`
- 非120列行：`21,337`（`0.3485%`）

推荐在清洗时保留条件：`NF==120`。

### 4.3 `whole-cluster-usage` 关键字段可用性（基于 `NF==120`）

- 总行数：`6,101,853`
- `Submit` 缺失：`0`（100%可用）
- `Start` 缺失或Unknown：`45,460`（`0.75%`）
- `End` 缺失或Unknown：`49,060`（`0.80%`）
- `ElapsedRaw` 为0或缺失：`788,040`（`12.91%`）
- 可计算 `Submit->Start` 等待时长：`6,056,393`（`99.25%`）
- 可计算 `Start->End` 运行时长：`6,052,793`（`99.20%`）
- `COMPLETED` 且 `Start/End` 完整：`4,659,021/4,659,021`（`100%`）

### 4.4 时间覆盖（`whole-cluster-usage`, `NF==120`）

- `Submit` 最小值：`2022-03-19T02:23:33`
- `Submit` 最大值：`2025-12-30T23:58:39`
- `Submit` 在2025年的记录：`6,059,084`

与 preliminary 窗口对比：
- `2025-01-15` 到 `2025-10-02`：`4,727,989`（占2025记录 `78.03%`）
- `2025-10-03` 到 `2025-12-31`：`1,324,927`（占2025记录 `21.87%`）
- `2025-01-01` 到 `2025-01-14`：`6,168`

含义：只用 preliminary 会漏掉约 `22%` 的2025记录（主要是10月后与年末数据）。

### 4.5 月度规模与 `seff` 覆盖率

| 月份 | whole 行数（含表头） | whole 规范行（NF=120） | seff Job 块数 | seff覆盖率(对whole) |
|---|---:|---:|---:|---:|
| jan | 6,965 | 6,964 | 2,048 | 29.41% |
| feb | 510,111 | 506,336 | 459,254 | 90.70% |
| mar | 547,510 | 543,120 | 488,328 | 89.91% |
| apr | 706,818 | 705,279 | 93,648 | 13.28% |
| may | 478,996 | 478,485 | 405,919 | 84.83% |
| jun | 810,016 | 809,638 | 140,505 | 17.35% |
| jul | 528,301 | 528,049 | 429,424 | 81.32% |
| aug | 615,722 | 615,649 | 122,821 | 19.95% |
| sep | 537,289 | 536,839 | 101,682 | 18.94% |
| oct | 557,249 | 554,168 | 0 | 0.00% |
| nov | 471,201 | 468,238 | 375,789 | 80.26% |
| dec | 353,024 | 349,088 | 301,728 | 86.43% |
| **总计** | **6,123,202** | **6,101,853** | **2,921,146** | **47.87%** |

结论：`seff` 覆盖非常不均匀，且缺 10 月文件，不适合作主数据。

### 4.6 preliminary zip 特征（`NF==19`）

- 总行数：`15,227,183`
- `JobIDRaw` 为纯数字（更接近“主作业”）：`5,128,840`（`33.68%`）
- `JobIDRaw` 非纯数字（大量 step 记录，如 `.batch` 等）：`10,098,343`（`66.32%`）
- `User` 缺失：`10,098,343`（`66.32%`，与 step 行基本重合）
- `Submit` 范围：`2022-03-19T02:23:33` 到 `2025-10-02T23:59:52`

2025月度（zip）可见 10 月仅到 10/02：

- 2025-01: 541,569
- 2025-02: 1,593,992
- 2025-03: 1,719,753
- 2025-04: 2,106,391
- 2025-05: 1,526,097
- 2025-06: 2,411,209
- 2025-07: 1,603,034
- 2025-08: 1,859,215
- 2025-09: 1,734,690
- 2025-10: 89,263（仅前2天）

结论：zip 在“完整性 + 主作业纯度”上不适合做最终主分析。

---

## 5. 针对你的目标的适配性评估

| 数据集 | 对 Submission Behavior | 对 Execution Schedules | 风险 | 结论 |
|---|---|---|---|---|
| `whole-cluster-usage/*.txt` | 强（用户/队列/状态/提交时间齐全） | 强（`Submit/Start/End/ElapsedRaw`可算） | 少量非120列脏行需过滤 | **主数据集（推荐）** |
| `statclass/*.txt` | 与上相同 | 与上相同 | 与上完全重复 | 不单独使用 |
| `2025_seff/*.txt` | 弱（缺提交时刻等关键行为字段） | 中（有效率指标） | 覆盖不完整，结构不固定，缺10月 | 仅补充特征 |
| `slurm_all_jobs_jan15_oct2_2025.zip` | 中（字段少，step噪声大） | 中（有起止时刻但非全年） | 仅到10/02，66% step行 | 仅作preliminary对照 |

---

## 6. 最终数据选择建议（可直接执行）

### 6.1 主分析数据（最终）

使用：`/Volumes/Store/427/iccp-cluster-usage-analysis-selected/whole-cluster-usage/*.txt`

清洗规则建议：
1. 跳过每个文件表头（`FNR==1`）
2. 仅保留 `NF==120`
3. 分析2025时保留 `substr(Submit,1,4)=="2025"`
4. 时间分桶以 `Submit` 推导（不要用文件名推导月份）
5. 如果跨文件合并做全局统计，按 `JobIDRaw` 去重或按 `Submit` 月归属，避免跨月重复累积

### 6.2 补充数据（可选）

使用：`/Volumes/Store/427/iccp-cluster-usage-analysis-selected/whole-cluster-usage/2025_seff/*.txt`

- 仅在需要 `CPU Efficiency` / `Memory Efficiency` 时按 `Job ID` 左连接
- 只用于“已匹配样本”的附加分析，不作为总体基数

### 6.3 不建议作为最终主集

- `statclass/*.txt`（因为重复）
- `slurm_all_jobs_jan15_oct2_2025.zip`（因为 preliminary + 10月后缺失 + step占比高）

---

## 7. 一句话结论

对于 `Job Submission Behavior & Execution Schedules`，最合适的数据是：

- **主表：** `whole-cluster-usage/*.txt`（过滤 `NF==120`）
- **补充：** `2025_seff/*.txt`（只补效率特征）
- **排除：** `statclass/*.txt`（重复副本）与 preliminary zip（非全年最终版）
