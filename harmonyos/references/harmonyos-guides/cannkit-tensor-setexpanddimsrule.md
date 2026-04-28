---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-setexpanddimsrule
title: SetExpandDimsRule
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > SetExpandDimsRule
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fdc3fa1c8dcf10d40e889c8f729040aada0e9c4a6bd5a99965787745d99f937f
---

## 函数功能

设置Tensor的补维规则。

补维是指在原有shape的基础上，添加一到多个维度。例如原shape[2,2]有两根轴，那么在两根轴中间补两维后的shape为[2,1,1,2]，补维后shape的第0、3根轴被称为原始轴，第1、2根轴被称为补维轴。

通过1和0描述补维规则，1代表当前轴为补维轴，0代表当前轴为原始轴，从左到右依次代表当前shape每根轴的来源，例如：

**表1** 补维规则示例

| 补维规则 | 补维前shape | 补维后shape |
| --- | --- | --- |
| 0110 | [2, 2] | [2, 1, 1, 2] |
| 100 | [2, 3] | [1, 2, 3] |
| 1000 | [2, 3] | 补维规则与补维前shape不匹配，规则指定原始轴有3根，但原始shape只有2根轴，补维报错。 |

## 函数原型

```
1. graphStatus SetExpandDimsRule(const AscendString &expand_dims_rule);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| expand\_dims\_rule | 输入 | 待设置的expand\_dims\_rule补维规则，采用字符串形式表示补维。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 设置成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
