# 原书第 21、22 页补充详解：命题 1.2、证明末尾的长公式与短时传播核

[返回命题的原注疏](03-1.3.1.md#p21-short-time-kernel) · [返回证明的原注疏](03-1.3.1.md#p22-momentum-integral) · [返回合订本](chapter-1-commentary.md#p21-short-time-kernel) · [阅读目录](README.md)

对应：§1.3.1，印刷页 21–23（PDF 阅读器页码 44–46），重点为命题 1.2、式 (1.92) 及第 22 页末尾的算符展开。

**第 21 页的命题给出极短时间内从位置 $y$ 到位置 $x$ 的传播振幅；第 22 页最后的长公式，把振幅整理成可以使用振荡高斯积分逐项计算的形式。**证明并未在第 22 页结束，要到第 23 页才回到命题的结果。

原注疏保留了“插入动量、完成平方、得到作用量”的主线；本篇补充微分算符重排、中点势能与余项的联系。

## 一、命题 1.2 想算什么？

定义短时传播核

$$
K_\epsilon(x,y)=\langle x|e^{-i\epsilon H/\hbar}|y\rangle.
$$

$y$ 是初始位置，$x$ 是终点位置，$\epsilon>0$ 是很短的时间间隔。这是传播振幅的核，不是精确位置之间的直接概率。

修正排印问题并恢复 $\hbar$ 后，命题的主要结果为

$$
\boxed{
K_\epsilon(x,y)\simeq
\sqrt{\frac{m}{2\pi i\hbar\epsilon}}
\exp\left[\frac i\hbar\left(
\frac{m(x-y)^2}{2\epsilon}
-\epsilon V\left(\frac{x+y}{2}\right)
\right)\right].
}
$$

这里暂不写精细余项。原书在 $\hbar=1$ 的约定下，还列出指数中的 $O(\epsilon^2)$ 与 $O(\epsilon(x-y)^2)$；这些是短时展开的记号，不能不加条件地当成对所有端点的一致误差估计。

| 部分 | 作用 |
|---|---|
| $\sqrt{m/(2\pi i\hbar\epsilon)}$ | 振荡高斯动量积分产生的前因子 |
| $m(x-y)^2/(2\epsilon)$ | 这一小段的动能作用量 |
| $-\epsilon V((x+y)/2)$ | 中点势能对应的作用量项 |

令平均速度 $v=(x-y)/\epsilon$，则

$$
\frac{m(x-y)^2}{2\epsilon}=\epsilon\frac12mv^2.
$$

所以指数中的主要部分为

$$
\Delta S\simeq\epsilon\left[\frac12mv^2-V\left(\frac{x+y}{2}\right)\right].
$$

即

$$
\boxed{K_\epsilon\simeq\text{前因子}\times e^{i\Delta S/\hbar}.}
$$

这是从算符时间演化走向路径积分的关键一步。平均速度在这里是短时离散表达式里的量，不代表已假定所有量子路径都光滑。

**校记：**原书式 (1.92) 前因子漏了质量因子，速度项把位移多平方了一次。正确主要表达式可与第 23 页证明末尾比较，详见[公式核对附录](formula-checks.md)。

## 二、第 22 页为什么插入动量？

下面与原书一致，暂设 $\hbar=1$。

$$
H=\frac{\hat p^2}{2m}+V(\hat x).
$$

动能在动量基底下最容易处理，所以插入

$$
I=\int dk\,|k\rangle\langle k|.
$$

得到

$$
K_\epsilon(x,y)=\int dk\,
\langle x|e^{-i\epsilon H}|k\rangle\langle k|y\rangle.
$$

利用位置、动量基底之间的傅里叶关系

$$
\langle x|k\rangle=\frac{e^{ikx}}{\sqrt{2\pi}},
\qquad \langle k|y\rangle=\frac{e^{-iky}}{\sqrt{2\pi}},
$$

可写为

$$
K_\epsilon(x,y)=\int\frac{dk}{2\pi}
e^{-iky}e^{-i\epsilon H_x}e^{ikx},
\qquad H_x=-\frac1{2m}\partial_x^2+V(x).
$$

这里 $e^{-i\epsilon H_x}$ 是含微分运算的算符，要对右边的函数起作用，并非普通数值指数。

## 三、为什么反复交换导数与指数的位置？

从乘积求导出发，对测试函数 $f$ 有

$$
\partial_x(e^{ikx}f)=e^{ikx}(ik+\partial_x)f.
$$

因此作为算符关系，

$$
\partial_x e^{ikx}=e^{ikx}(ik+\partial_x).
$$

右边额外的导数表示它还会作用于后续函数；这不是普通指数函数求导公式中凭空多了一项。

将 $e^{ikx}$ 从演化算符右边移到左边，相当于在算符内部作替换

$$
\partial_x\longmapsto\partial_x+ik.
$$

于是，按原书的算符展开理解，

$$
K_\epsilon(x,y)=\int\frac{dk}{2\pi}
e^{ik(x-y)}
e^{-i\epsilon[-(\partial_x+ik)^2/(2m)+V(x)]}\cdot1.
$$

展开平方：

$$
-\frac{(\partial_x+ik)^2}{2m}
=\frac{k^2}{2m}-\frac{ik}{m}\partial_x-\frac1{2m}\partial_x^2.
$$

因此

$$
\boxed{
K_\epsilon(x,y)=\int\frac{dk}{2\pi}
e^{ik(x-y)-i\epsilon k^2/(2m)}e^{-i\epsilon A_k}\cdot1,
}
$$

其中

$$
A_k=-\frac{ik}{m}\partial_x-\frac1{2m}\partial_x^2+V(x).
$$

前面是可直接处理的振荡高斯，后面保留势能和导数修正。此处提出的 $k^2/(2m)$ 对 $x$ 而言是常数，可以与其余算符交换；不能照此直接把一般的动能与势能指数无误差地拆开。

## 四、最后的“乘以 1”为什么重要？

它说明剩下的微分算符最终作用于常数函数 $1$。例如

$$
A_k1=V(x).
$$

但这不表示所有导数项都能删除，因为第二次作用时

$$
\begin{aligned}
A_k^21&=A_kV(x)\\
&=-\frac{ik}{m}V'(x)-\frac1{2m}V''(x)+V(x)^2.
\end{aligned}
$$

导数会作用在第一次产生的 $V(x)$ 上。展开

$$
e^{-i\epsilon A_k}1
=1-i\epsilon A_k1+\frac{(-i\epsilon)^2}{2}A_k^21+\cdots
$$

就会产生势能、势能导数以及它们的组合。这是在保留动能与势能不对易所带来的修正。

## 五、第 22 页最后的长公式整理出了什么？

令 $d=x-y$，完成平方：

$$
ikd-\frac{i\epsilon k^2}{2m}
=-\frac{i\epsilon}{2m}\left(k-\frac{md}{\epsilon}\right)^2
+\frac{imd^2}{2\epsilon}.
$$

再令无量纲积分变量

$$
r=\sqrt{\frac{\epsilon}{2m}}k,
$$

得到与原书末尾相同结构的表达式：

$$
\begin{aligned}
K_\epsilon(x,y)
={}&\sqrt{\frac{2m}{\epsilon}}e^{imd^2/(2\epsilon)}
\int\frac{dr}{2\pi}
e^{-i[r-\sqrt{m/(2\epsilon)}\,d]^2}\\
&\times\sum_{n=0}^{\infty}\frac{(-i\epsilon)^n}{n!}
\left[-i\sqrt{\frac{2}{m\epsilon}}r\partial_x
-\frac{\partial_x^2}{2m}+V(x)\right]^n1.
\end{aligned}
$$

这里用 $r$ 避免与物理动量混淆。原书末尾的平方项与一阶导数项使用相反符号的积分变量；同时令 $r\to-r$，上式即与印出的形式对应，但原书前面文字写出的变量替换符号没有相应调整。

| 部分 | 来源和用途 |
|---|---|
| $\sqrt{2m/\epsilon}$ | 动量变量缩放产生的 Jacobian |
| $e^{imd^2/(2\epsilon)}$ | 完成平方后留下的动能相位 |
| 积分内的振荡高斯 | 使用第 21 页 Lemma 1.2 及相应高斯矩计算 |
| 无穷级数 | 算符指数展开，产生势能修正 |
| 最后的 $1$ | 指定微分算符的作用对象 |

**这条公式是计算中间站，不是新的物理假设。**书中的无穷级数按短时展开使用；不应未经条件检查就把它看作处处收敛、可任意交换积分求和的恒等式。

## 六、势能的中点值怎样出现？

二阶项中的一阶导数贡献为

$$
\frac{(-i\epsilon)^2}{2}\left(-\frac{ik}{m}V'\right)
=\frac{i\epsilon^2k}{2m}V'.
$$

完成平方后，振荡高斯的一阶矩给出 $k$ 的中心值 $md/\epsilon$。这里的“中心”是高斯积分移项的代数说法，不是概率分布的均值；振荡积分可通过加小衰减的方式定义。因此积分后这一项产生

$$
\frac{i\epsilon d}{2}V'(x).
$$

与一阶项组合为

$$
-i\epsilon V(x)+\frac{i\epsilon d}{2}V'(x).
$$

由 Taylor 展开，

$$
V\left(x-\frac d2\right)
=V(x)-\frac d2V'(x)+O(d^2),
\qquad x-\frac d2=\frac{x+y}{2}.
$$

这些项便组成

$$
-i\epsilon V\left(\frac{x+y}{2}\right)
$$

以及相应余项。势能幂次等项也要一起整理；这段计算展示的是中点处一阶修正的来源，不是声称只保留级数的前三项便能在任意端点、任意势能下完成严格证明。

**中点势能不只是“取平均比较自然”的猜测；证明保留的导数修正解释了它为何与该短时展开相容。**这不表示中点是唯一可用的时间切片约定，不同约定需要配套处理误差与算符排序。

## 七、怎样从第 22 页回到命题？

第 23 页接着平移积分变量，用引理

$$
\int_{-\infty}^{\infty}e^{-iaq^2}dq
=\sqrt{\frac{\pi}{ia}},\qquad a>0,
$$

以及相应高斯矩计算。对自由部分，有

$$
\sqrt{\frac{2m}{\epsilon}}
\int\frac{dq}{2\pi}e^{-iq^2}
=\sqrt{\frac{m}{2\pi i\epsilon}}.
$$

所以高斯积分产生前因子，提出的动能相位保留，势能和导数项整理成中点势能指数及余项。恢复 $\hbar$ 后，就是第一节的短时核。

## 八、它与原注疏的关系是什么？

原注疏给出的简化主干为

$$
K_\epsilon(x,y)\simeq\int\frac{dp}{2\pi\hbar}
\exp\left[\frac i\hbar\left(
p(x-y)-\epsilon\frac{p^2}{2m}
-\epsilon V\left(\frac{x+y}{2}\right)\right)\right].
$$

这里写明中点取值；原注疏在该主干积分中将势能简记为 $V$。此式是已经选择并作出短时近似后的表达式，不是把 $e^{-i\epsilon(T+V)/\hbar}$ 直接视为两个可交换的普通指数。

完成平方：

$$
p(x-y)-\frac{\epsilon p^2}{2m}
=-\frac{\epsilon}{2m}\left(p-\frac{m(x-y)}{\epsilon}\right)^2
+\frac{m(x-y)^2}{2\epsilon}.
$$

积分掉第一项，留下的第二项与势能组成 $\Delta S$。两种讲解的侧重点为：

- **原注疏的主线**：插入动量 → 完成平方 → 积分掉动量 → 得到短时作用量。
- **原书第 22 页的展开**：处理算符不对易，解释势能导数修正及中点形式与上述近似的联系。

原注疏没有逐项展开这层算符计算，因此应结合本篇理解两者的对应，不能把简化积分误当作无误差的算符恒等式。

## 九、余项和极限怎样理解？

原书列出的 $O(\epsilon^2)$ 与 $O(\epsilon d^2)$ 提醒我们：该式保留了哪些阶的短时信息；误差还依赖端点距离 $d=x-y$。对于给定的非零 $d$，不能简单地只按 $\epsilon$ 的次数判断所有中间项。

势能的正则性、端点范围、振荡积分的解释与最终极限均需相应条件。特别是 $\epsilon\to0$ 时，传播核趋于 $\delta(x-y)$ 是在作用于波函数的积分意义下理解，而不是普通函数逐点收敛。

本篇解释书中的形式推导与计算主线，不把该短时展开当成对任意势能、任意固定端点的一致误差定理。

[返回命题的原注疏](03-1.3.1.md#p21-short-time-kernel) · [返回证明的原注疏](03-1.3.1.md#p22-momentum-integral) · [返回合订本证明段落](chapter-1-commentary.md#p22-momentum-integral)
