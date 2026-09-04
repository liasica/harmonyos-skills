---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-pipebarrier
title: PipeBarrier(ISASI)
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > 核内同步 > PipeBarrier(ISASI)
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e32d25850a8a5aa00b2eda1e5db17cdd218c6ad2608f39b57be4b3abb49a8452
---

## 功能说明

阻塞相同流水，具有数据依赖的相同流水之间需要插入此同步。

## 函数原型

```cpp
template <pipe_t pipe>
__aicore__ inline void PipeBarrier()
```

## 参数说明

**表1** 模板参数说明

| 参数名 | 描述 |
| --- | --- |
| pipe | 模板参数，表示阻塞的流水类别。  支持的流水参考表2。  如果不关注流水类别，希望阻塞所有流水，可以传入PIPE\_ALL。 |

**表2** 指令流水类型和相关说明

| 流水类型 | 含义 |
| --- | --- |
| PIPE\_S | 标量流水线，使用Tensor GetValue函数时为此流水 |
| PIPE\_V | 矢量计算流水及L0C->UB数据搬运流水 |
| PIPE\_M | 矩阵计算流水 |
| PIPE\_MTE1 | L1->L0A、L1->L0B数据搬运流水 |
| PIPE\_MTE2 | GM->L1、GM->L0A、GM->L0B、GM->UB数据搬运流水 |
| PIPE\_MTE3 | UB->GM、UB->L1数据搬运流水 |
| PIPE\_FIX | L0C->GM、L0C->L1数据搬运流水。 |

## 返回值

无

## 支持的型号

KirinX90系列处理器

## 注意事项

无

## 约束说明

Scalar流水之间的同步由硬件自动保证，调用PipeBarrier<PIPE\_S>()会引发硬件错误。

## 调用示例

如下示例，Mul指令的输入dst0Local是Add指令的输出，两个矢量运算指令产生依赖，需要插入PipeBarrier保证两条指令的执行顺序。

注：仅作为示例参考，开启自动同步的情况下，编译器自动插入PIPE\_V同步，无需开发者手动插入。

**图1** Mul指令和Add指令是串行关系，必须等待Add指令执行完成后，才能执行Mul指令。

![](https://media:401788444116621952)

```cpp
AscendC::LocalTensor<half> src0Local;
AscendC::LocalTensor<half> src1Local;
AscendC::LocalTensor<half> src2Local;
AscendC::LocalTensor<half> dst0Local;
AscendC::LocalTensor<half> dst1Local;

AscendC::Add(dst0Local, src0Local, src1Local, 512);
AscendC::PipeBarrier<PIPE_V>();
AscendC::Mul(dst1Local, dst0Local, src2Local, 512);
```
