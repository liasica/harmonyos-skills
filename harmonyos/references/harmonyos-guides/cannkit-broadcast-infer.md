---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-broadcast-infer
title: BROADCAST_INFER
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > BROADCAST_INFER
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:835962e322906e8e45d528b305e2c9e60ead20161bddbd16a69fff2d72f31125
---

## 函数功能

提供公共函数宏封装，供算子开发者开发InferShape函数。该函数基于2个输入的shape，设置输出的shape。该宏只是设置shape，未设置dtype。

* 如果2个输入的shape一致，会按输入的shape设置输出shape。
* 如果2个输入的shape不一致，会按照broadcast的策略，取2个输入shape的并集。

  比如输入shape分别为（1,2,3,4）和（3,1,3,4），则该宏会设置算子的输出shape为（3,2,3,4）。

## 函数原型

```cpp
BROADCAST_INFER(in1_name, in2_name, out_name)
```

该函数会自动调用如下函数：

```cpp
graphStatus BroadCastInfer(const function<vector<int64_t>()> &get_in1_shape,
                           const function<vector<int64_t>()> &get_in2_shape,
                           const function<void(const std::vector<int64_t> &y_shape)> &set_out_shape);
```

## 约束说明

无

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| in1\_name | 输入 | 算子第一个输入。 |
| in2\_name | 输入 | 算子第二个输入。 |
| out\_name | 输出 | 算子输出。 |

## 返回值

执行成功或失败。

## 调用示例

```cpp
IMPLEMT_INFERFUNC(RightShift, RightShiftInfer) {
  DataType type = op.GetInputDesc("x").GetDataType();
  SET_OUTPUT_TYPE(op, "z", type);
  return BROADCAST_INFER("x", "y", "z")(op);
}
```
