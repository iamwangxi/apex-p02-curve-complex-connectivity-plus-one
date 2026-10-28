# 有界交数曲线复形：连通度统一增加一阶

设 $`C_d(S_g)`$ 的顶点为闭连通可定向曲面上本质简单闭曲线的无向同痕类；几何交数至多 $`d`$ 的不同顶点相邻，并取旗复形。对每个 $`g\geq3,d\geq1,k\geq1`$，

```math
d\binom{k}{2}\leq2g-2\quad\Longrightarrow\quad C_d(S_g)\text{ is }k\text{-connected}.
```

同一数值条件下，固定全部原顶点的有限替换定理对每个 $`g\geq2`$ 均成立。因而

```math
\mathrm{conn}\,C_d(S_g)\geq
1+\left\lfloor\frac{\sqrt{1+8(2g-2)/d}-1}{2}\right\rfloor
\qquad(g\geq3).
```

该界比直接交数计数恰好多一阶；固定 $`d`$ 时首项仍为 $`2\sqrt{g/d}`$。所有 $`g\geq2,d\geq1`$ 均单连通。另接受目标论文 Theorem 1.1 的 $`C_1(S_2)`$ 可缩性后，上式也适用于亏格二，新增数值参数仅为 $`k=2,d=1,2`$；结合上述高亏格下界，得到 $`d=1`$ 时所有亏格至少二的 3-连通性。

## 目标论文与范围

目标为 Apex Intelligence 的 [*The Complex of Curves Pairwise Intersecting at Most Once Is Contractible in Genus Two*](https://math.apexin.net/papers/curve-complex-genus-two.pdf)，2026 年 9 月 11 日比赛版本，共 35 页。PDF SHA-256：

`d1eadd01f94e9af17ee9f5fb2ee1b05b326430f37296309fd9417340ea366fd4`

原论文的 Theorem 1.1（印刷第 2 页）证明亏格二可缩；Theorem 1.3（第 2 页）及 Theorem 7.7（第 24 页）证明所有亏格至少二时单连通。本稿给出适用于每个正整数交数上界的连通度加强。

顶点包括全部本质简单闭曲线的无向同痕类，也包括分离曲线；几何实现采用通常弱拓扑。证明保留全部原顶点，允许多次内部 stellar subdivision 后再作重心细分。它不构造整个复形的全局收缩或回缩。

## 阅读顺序

先读[主定理与连通度结论](proof/03-connectivity.md)，再读[所有交数上界的完整证明](proof/06-bounded-intersection.md)。后者包含容量选边、重复颜色圈的同调本质性、逐子面严格下降、有限终止、相对顶点同伦和全部参数边界。

[有限替换](proof/01-finite-replacement.md)另行完整给出邻域、锥载体及直接交数界；[彩虹下降](proof/02-rainbow-descent.md)保留交数一时的专门证明。实际依赖的有限替换论证均在本仓库自足给出。

[一次重心细分的方法界](proof/04-method-cutoff.md)说明填满系统阻碍的确切接口，其平方根首项归属 Anderson–Parlier–Pettet；[覆盖塔命题](proof/05-covering-tower.md)给出完整初始带状图、同调覆盖与总交数下界。另见[文献定位](sources/bibliography.md)、[有限核验范围](checks/README.md)和[复核哈希记录](sources/review-status.md)。

覆盖塔给出 $`n_h=o(g_h)`$ 的填满 1-系统，使任何本质曲线的总交数至少为 $`2^{\lfloor h/2\rfloor}`$。该族的曲线数大于平方根规模，因此不能用来否定只针对 $`n\leq C\sqrt g`$ 的常数成本命题。

## 复跑与校验

需要 Python 3.9 或更新版本，仅用标准库。在仓库根目录运行：

```sh
python3 -B scripts/run_checks.py
```

六组检查均重新计算，并与 `checks/` 中保存的 JSON 逐项比较。程序只输出到标准输出，不写文件；不要使用 `-O`，否则会禁用断言。长彩虹圈程序只加载同目录函数，不执行被加载文件的主程序，也不生成字节码。新增两组核验覆盖加权交点图、容量拟阵选择、实际曲面模型和重复颜色圈的非零同调；使用固定种子，输出不含耗时等浮动字段。

有限计算不能替代无限参数的曲面拓扑、同痕类或相对同伦证明。本稿没有形式化验证。核验包哈希使用：

```sh
shasum -a 256 -c MANIFEST.sha256
```

## 文献归属与审查状态

Harer 的 Lemma 4.3（印刷第 178–179 页）已经使用相近的边界替换及细分同伦方法；最小填满 1-系统的 $`2\sqrt g`$ 首项来自 Anderson–Parlier–Pettet。本稿以容量选边和最高维严格下降加强这类估计；固定交数上界时没有改进渐近首项。尚未完成全球查新或悬赏资格判断。

已复核的证明阶段包括所有正整数交数上界的推广，报告均未发现致命问题、可修补数学问题或表述问题。[复核记录](sources/review-status.md)列出受审稿、复核报告及本仓库证明页的 SHA-256，明确各自范围。亏格二补充仍依赖目标论文的既有可缩性定理，不将本次复核当成该外部定理的独立认证。

## AI 声明

GPT-6.1 Sol 在人类指导下使用 OpenAI Codex 发展证明、执行适用的计算并起草文本；不同的全新上下文会话执行对抗复核。GPT-6 Astra 参与研究方向与投稿范围建议。Claude 对交数一材料贡献了规划、来源核对和编辑。没有人类专家认证本稿。

## 许可

原创文字采用 CC BY 4.0；`scripts/` 代码采用 MIT License。详见 [LICENSE](LICENSE)。外部文献保留各自版权与许可，本仓库不表示 Apex Intelligence 或所引作者认可本稿。
