---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-broadcast-infer
title: BROADCAST_INFER
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > BROADCAST_INFER
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:24f6703dbb650dcaeb76f1931a64be80c9d8944d75e3d7fc5f6400145102668a
---

## 函数功能

提供公共函数宏封装，供算子开发者开发InferShape函数。该函数基于2个输入的shape，设置输出的shape。该宏只是设置shape，未设置dtype。

* 如果2个输入的shape一致，会按输入的shape设置输出shape。
* 如果2个输入的shape不一致，会按照broadcast的策略，取2个输入shape的并集。

  比如输入shape分别为（1,2,3,4）和（3,1,3,4），则该宏会设置算子的输出shape为（3,2,3,4）。

## 函数原型

```
1. BROADCAST_INFER(in1_name, in2_name, out_name)
```

该函数会自动调用如下函数：

```
1. graphStatus BroadCastInfer(const function<vector<int64_t>()> &get_in1_shape,
2. const function<vector<int64_t>()> &get_in2_shape,
3. const function<void(const std::vector<int64_t> &y_shape)> &set_out_shape);
```

## 约束说明

无

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| in1\_name | 输入 | 算子第一个输入。 |
| in2\_name | 输入 | 算子第二个输入。 |
| out\_name | 输入 | 算子输出。 |

## 返回值

执行成功或失败。

## 调用示例

```
1. IMPLEMT_INFERFUNC(RightShift, RightShiftInfer) {
2. DataType type = op.GetInputDesc("x").GetDataType();
3. SET_OUTPUT_TYPE(op, "z", type);
4. return BROADCAST_INFER("x", "y", "z")(op);
5. }
```
