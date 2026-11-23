# 《Geometry, Topology and Physics》第一章章句集注

底本：Mikio Nakahara，Geometry, Topology and Physics，Second Edition，2003，Chapter 1 “Quantum Physics”。

从你现有笔记停止之后的 **1.2.4 Wavefunction** 开始，按原书次序覆盖到 **1.10.2** 和章末 **Problem 1.1**。对应印刷页 13 下部至 66，PDF 阅读器页码 36 至 89，共涉及 54 个原书页面。已有笔记未覆盖或改写。

## 底本保存与读法

每个小节采用“原书该页完整影印块 → 该页句读与集注”的结构。解释按原段落和公式推进，补出物理动机、隐含前提、数学推导与适用范围。

**完整原文以影印图片保存在 Markdown 正文中。**本地 PDF 的公式文字提取存在上下标错位、特殊字形乱码，故不把自动提取结果当作校订后的原文。正文、公式、图示、练习和脚注均随原页保留；同页跨小节时沿标题切开，原文不删改。原文图片可放大，中文注疏及重排公式可编辑、检索。

这不是可逐字编辑的英文转录本。短引句用于定位句读，不能替代上方完整底本；新增解释不冒充原文。发现原式不一致时另列“校记”，不修改影印。校记依据所提供版本的代入、量纲、低维算例及前后文检查，不冒充出版社官方勘误。

以你的高中物理背景为起点，补充大学物理概念；数学解释利用你已学的分析、线性代数、常微分方程与凸优化。遇到物理公设会说明其地位，不把它伪装成仅凭数学就能推导的结论。

## 连续阅读

[打开完整合订 Markdown](chapter-1-commentary.md)。

合订本与分小节版本内容相同，共用 assets 文件夹。移动、备份时需同时保留图片；只复制 Markdown 不会带走原文。下列分册适合按节阅读，避免一次加载全部原页。

| 原书小节 | 注疏 | 印刷页 |
|---|---|---|
| 1.2.4 | [Wavefunction：波函数](01-1.2.4.md) | 13–17 |
| 1.2.5 | [Harmonic oscillator：谐振子的算符量子化](02-1.2.5.md) | 17–19 |
| 1.3.1 | [Path integral quantization：玻色粒子的路径积分](03-1.3.1.md) | 19–26 |
| 1.3.2 | [Imaginary time and partition function：虚时间与配分函数](04-1.3.2.md) | 26–28 |
| 1.3.3 | [Time-ordered product and generating functional：编时乘积与生成泛函](05-1.3.3.md) | 28–31 |
| 1.4.1 | [Transition amplitude：谐振子的传播振幅](06-1.4.1.md) | 31–35 |
| 1.4.2 | [Partition function：谐振子的配分函数与谱行列式](07-1.4.2.md) | 35–38 |
| 1.5.1 | [Fermionic harmonic oscillator：费米谐振子](08-1.5.1.md) | 38–40 |
| 1.5.2 | [Calculus of Grassmann numbers：Grassmann 数与分次](09-1.5.2.md) | 40–41 |
| 1.5.3 | [Differentiation：Grassmann 微分](10-1.5.3.md) | 41 |
| 1.5.4 | [Integration：Berezin 积分与换元](11-1.5.4.md) | 42–43 |
| 1.5.5 | [Delta-function：Grassmann δ 函数](12-1.5.5.md) | 43 |
| 1.5.6 | [Gaussian integral：费米高斯积分与 Pfaffian](13-1.5.6.md) | 44–45 |
| 1.5.7 | [Functional derivative：Grassmann 泛函微分](14-1.5.7.md) | 45 |
| 1.5.8 | [Complex conjugation：Grassmann 共轭](15-1.5.8.md) | 45 |
| 1.5.9 | [Coherent states and completeness relation：费米相干态与完备关系](16-1.5.9.md) | 46–47 |
| 1.5.10 | [Partition function of a fermionic oscillator：费米配分函数与反周期条件](17-1.5.10.md) | 47–51 |
| 1.6.1 | [Free scalar field：自由标量场](18-1.6.1.md) | 51–53 |
| 1.6.2 | [Interacting scalar field：相互作用、关联函数与有效作用量](19-1.6.2.md) | 54–55 |
| 1.7 | [Quantization of a Dirac field：Dirac 场的量子化](20-1.7.md) | 55–56 |
| 1.8.1 | [Abelian gauge theories：电磁场与阿贝尔规范理论](21-1.8.1.md) | 56–58 |
| 1.8.2 | [Non-Abelian gauge theories：非阿贝尔规范理论](22-1.8.2.md) | 58–59 |
| 1.8.3 | [Higgs fields：Higgs 场与质量](23-1.8.3.md) | 60 |
| 1.9.1 | [Dirac monopole：Dirac 磁单极子](24-1.9.1.md) | 60–61 |
| 1.9.2 | [The Wu-Yang monopole：Wu–Yang 拼接](25-1.9.2.md) | 62 |
| 1.9.3 | [Charge quantization：电荷量子化](26-1.9.3.md) | 62–63 |
| 1.10.1 | [Introduction：瞬子与拓扑扇区](27-1.10.1.md) | 63–64 |
| 1.10.2 | [The (anti-)self-dual solution：自对偶解与作用量下界](28-1.10.2.md) | 64–65 |
| Problems | [Problems：Derrick 缩放论证](29-Problems.md) | 66 |

## 符号与约定

原文常设 $\hbar=c=1$。解释量纲、经典尺度及电荷量子化时，注中有时恢复这些常数。$\beta=1/(k_BT)$；恢复 $\hbar$ 后，热欧氏时间长度为 $\hbar\beta$。

$Z(\beta)$ 是热迹，$Z[J]$ 通常是含源生成泛函；后者是否已除以 $Z[0]$ 要另看说明。磁荷 $g$ 与 Yang–Mills 耦合不是同一种物理参数。Lorentz/Euclidean 度规、Hermitian/反 Hermitian 生成元也不能混用；需要另选一致约定时，注中会明确列出。

“句读”说明原句和原公式的实际意思；“疏”补推导与前提；“集注”将段落放回物理问题和后续数学结构；“校记”说明此版本可直接核验的不一致或约定缺失。

## 读完一段如何检查理解

先读原文，再读紧接的注释，动手补几行关键计算。随后用自己的话回答：正在解释什么现象或计算什么量？新增数学对象解决了什么困难？哪些前提改变后，公式便不能照用？

本章反复串联的关系是：复振幅与干涉；演化核与路径积分；二次型与模式涨落；费米交换符号与奇代数；局部规范基准与联络；非零通量与全球拼接；拓扑整数与作用量下界。细节可以分次消化，每次回读都应能说明这些联系。

## 核验记录

[校读索引](editorial-notes.md) 汇总公式与约定问题，正文中有相应说明。[底本范围记录](source-manifest.json) 记录源文件、哈希、每个影印块所属页与切片范围，供完整性检查。

本次范围从 1.2.4 开始，不包含更早已学部分的重新注疏，也不冒充从第一章开头开始的全章转录。原笔记在本次写作前后保持一致。
