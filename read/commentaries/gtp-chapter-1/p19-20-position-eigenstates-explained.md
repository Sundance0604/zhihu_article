# 原书第 19、20 页补充详解：带时间标签的位置本征态

[返回第 19 页原注疏](03-1.3.1.md#p19-position-eigenstates) · [返回第 20 页原注疏](03-1.3.1.md#p20-propagator) · [返回合订本对应段落](chapter-1-commentary.md#p19-position-eigenstates) · [阅读目录](README.md)

对应：§1.3.1 Path integral quantization，印刷页 19–20（PDF 阅读器页码 42–43），重点为式 (1.80)–(1.87)。

## 一、式 (1.81) 到底说了什么？

原书第 19 页写道

$$
\boxed{\hat x(t_f)|x_f,t_f\rangle=x_f|x_f,t_f\rangle.}
$$

括号中是 $t_f$，表示最终时刻；下标 $f$ 表示 final，不是一个函数 $f$。

**作者用这个本征值方程定义 $|x_f,t_f\rangle$：它是“在时刻 $t_f$，位置测量值确定为 $x_f$”的理想位置本征态。**这个公式不是对任意状态都成立。

位置取连续值，精确位置态属于广义本征态，不能像普通波包一样归一化。这里先把它作为连续基底使用；实际位置概率需要结合波函数，对有宽度的区间积分。

## 二、先不考虑时间：它就是熟悉的本征值方程

线性代数中的本征值方程是

$$
A\mathbf v=\lambda\mathbf v.
$$

矩阵作用于一个特殊向量，结果只把该向量乘以一个数。位置算符的情形对应为

$$
\underbrace{\hat x}_{\text{位置算符}}
\underbrace{|x_f\rangle}_{\text{位置本征态}}
=\underbrace{x_f}_{\text{位置本征值}}
\underbrace{|x_f\rangle}_{\text{同一个态}}.
$$

物理意义是：对这个理想状态测量位置，结果确定为 $x_f$。**位置算符作用不是把粒子移动一下；等式描述的是算符与其本征态之间的关系。**

对于一般状态 $|\psi\rangle$，通常不能写 $\hat x|\psi\rangle=x_f|\psi\rangle$，因为它的位置一般不确定。

## 三、为什么位置算符和本征态带时间标签？

第 19 页采用 Heisenberg 绘景。为区分记号，这里恢复下标 $H$；原书在该处省略了绘景下标。

设 $H$ 不随时间变化，以 $0$ 为参考时刻，定义

$$
U(t)=e^{-iHt/\hbar}.
$$

Heisenberg 绘景的位置算符为

$$
\boxed{\hat x_H(t)=U(t)^\dagger\hat xU(t).}
$$

不同时间的位置测量，分别由 $\hat x_H(t_i)$ 和 $\hat x_H(t_f)$ 描述。作者把后者对应本征值 $x_f$ 的本征态记作 $|x_f,t_f\rangle$，因此它按定义满足

$$
\hat x_H(t_f)|x_f,t_f\rangle=x_f|x_f,t_f\rangle.
$$

两个标签有不同作用：$x_f$ 标记位置测量值，$t_f$ 标记讨论的是哪个时刻的位置算符。

## 四、第 20 页怎样把它与不带时间的位置态联系起来？

从参考位置算符的本征态出发：

$$
\hat x|x_f\rangle=x_f|x_f\rangle.
$$

选取相容的本征态相位约定，令

$$
\boxed{|x_f,t_f\rangle=U(t_f)^\dagger|x_f\rangle
=e^{iHt_f/\hbar}|x_f\rangle.}
$$

直接验证，下面的 $U$ 均取在 $t_f$：

$$
\begin{aligned}
\hat x_H(t_f)|x_f,t_f\rangle
&=(U^\dagger\hat xU)(U^\dagger|x_f\rangle)\\
&=U^\dagger\hat x\underbrace{UU^\dagger}_{I}|x_f\rangle\\
&=U^\dagger\hat x|x_f\rangle\\
&=U^\dagger x_f|x_f\rangle\\
&=x_f|x_f,t_f\rangle.
\end{aligned}
$$

因此这里用的是一个线性代数事实：

$$
\boxed{
A|v\rangle=\lambda|v\rangle
\quad\Longrightarrow\quad
(U^\dagger AU)(U^\dagger|v\rangle)
=\lambda(U^\dagger|v\rangle).
}
$$

**算符做酉变换时，本征向量相应变换，本征值保持不变。**本征值方程本身不能固定本征向量的整体相位；上面的等式选定了后续计算统一采用的约定。

## 五、它不是把一个位置态向前演化得到的状态

在 Schrödinger 绘景中，初始状态的正向时间演化写成

$$
|\psi_S(t)\rangle=U(t)|\psi_S(0)\rangle.
$$

但这里的位置基底写成

$$
|x_f,t_f\rangle=U(t_f)^\dagger|x_f\rangle.
$$

方向相反，因为我们在构造**时刻 $t_f$ 的位置算符的本征基底**，而不是求某个初始位置态运动后的状态。原书第 19 页脚注特别提醒了这个区别。

| 对象 | 表达式 | 作用 |
|---|---|---|
| Schrödinger 绘景中的演化状态 | $U(t)|\psi_S(0)\rangle$ | 描述指定初始状态的时间演化 |
| Heisenberg 绘景中的位置本征基底 | $U(t)^\dagger|x\rangle$ | 给出 $\hat x_H(t)$ 对应本征值 $x$ 的基底态 |

Heisenberg 绘景中物理状态向量保持固定，并不妨碍随时间改变的测量算符拥有随时间改变的本征基底。这里的时间标签属于后者。

一个粒子起初位置确定，并不意味着它后来位置仍然确定；实际准备的局域波包可以随时间扩散。不能把本征基底的时间标签理解成一条确定的粒子轨迹。

## 六、为什么要引入这些记号？

作者要计算初始位置 $x_i$ 到最终位置 $x_f$ 的跃迁振幅：

$$
K(x_f,t_f;x_i,t_i)=\langle x_f,t_f|x_i,t_i\rangle.
$$

由前面的关系，

$$
|x_i,t_i\rangle=U(t_i)^\dagger|x_i\rangle,
\qquad
\langle x_f,t_f|=\langle x_f|U(t_f).
$$

因此

$$
\begin{aligned}
\langle x_f,t_f|x_i,t_i\rangle
&=\langle x_f|U(t_f)U(t_i)^\dagger|x_i\rangle\\
&=\boxed{\langle x_f|e^{-iH(t_f-t_i)/\hbar}|x_i\rangle.}
\end{aligned}
$$

最后一步用了时间无关的 $H$；原书设 $\hbar=1$，所以指数中省略了它。

- 左边是不同时刻的位置本征态之间的重叠。
- 右边是从初始位置态出发，经过时间演化，再提取终点位置分量。

它们描述同一个传播核。对于实际的初始波函数，后来的波函数由

$$
\psi_f(x_f)=\int dx_i\,K(x_f,t_f;x_i,t_i)\psi_i(x_i)
$$

给出。核本身不能直接当成精确位置测量的概率；还需与初始波函数结合，并对终点区间积分模平方。

## 七、回读时抓住的区别

1. $\hat x_H(t_f)|x_f,t_f\rangle=x_f|x_f,t_f\rangle$ 是位置本征态的定义，不是任意状态的性质。
2. 时间标签说明测量算符的时刻，不是断言粒子沿着确定轨迹运动。
3. $U^\dagger|x\rangle$ 构造 Heisenberg 位置基底，$U|\psi\rangle$ 描述 Schrödinger 状态演化，二者用途不同。
4. 第 20 页借助酉变换把这些记号转成传播核，为后面的时间切片和路径积分作准备。

[返回第 19 页原注疏](03-1.3.1.md#p19-position-eigenstates) · [返回第 20 页原注疏](03-1.3.1.md#p20-propagator) · [返回合订本第 20 页](chapter-1-commentary.md#p20-propagator)
