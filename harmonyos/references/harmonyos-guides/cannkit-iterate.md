---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-iterate
title: Iterate
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 高阶API > 矩阵相乘 > Matmul > Iterate
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:407667cb5d27c9e9c945b592e168f00d04eaefbf8dc610fffe5c855ddd78087a
---

## 功能说明

每调用一次Iterate，会计算出一片baseM \* baseN的C矩阵。接口内部会维护迭代进度，调用一次后会对A、B矩阵首地址进行偏移。默认以先M轴再N轴的迭代顺序，也可以通过调整tiling参数iterateOrder，转换为先N轴再M轴的迭代顺序。

当传入数据未对齐，存在尾块时，会在最后一次迭代输出尾块的计算结果。

## 函数原型

```cpp
template <bool sync = true> __aicore__ inline bool Iterate(bool enPartialSum = false)
```

## 参数说明

**表1** 模板参数说明

| 参数名 | 描述 |
| --- | --- |
| sync | 迭代获取C矩阵分片的过程分为同步和异步两种模式。通过该参数设置同步或者异步模式：同步模式设置为true，异步模式设置为false。默认为同步模式，具体模式的介绍和使用方法请参考[GetTensorC](cannkit-gettensorc.md)。 |

**表2** 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| enPartialSum | 输入 | 是否将矩阵乘的结果累加于现有的CO1数据，默认值false。在L0C累加时，只支持A矩阵和B矩阵相乘的输出C矩阵规格为singleM==baseM &&singleN==baseN。  Kirin9020系列处理器、Kirin9030系列处理器，该参数仅支持配置为false。 |

## 返回值

false：单核上的所有数据全部算完。

true：数据仍在迭代计算中。

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

## 注意事项

无

## 调用示例

```cpp
// 同步模式样例
while (mm.Iterate()) {
    mm.GetTensorC(ubCmatrix);
}
 
// 异步模式样例
mm.template Iterate<false>();
// ...
for (int i = 0; i < singleM/baseM*singleN/baseN; ++i) {
    mm.GetTensorC<false>(ubCmatrix);
}
```
