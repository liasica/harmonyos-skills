---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setnodetype
title: SetNodeType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ComputeNodeInfo > SetNodeType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c0078c9b2484b2f6150f0f0ac28e09f4f8724950e51572835f2c519837aa7c37
---

## 函数功能

设置算子的类型。

## 函数原型

```cpp
void SetNodeType(const ge::char_t *node_type)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| node\_type | 输入 | 算子的类型。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
compute_node_info.SetNodeType("Const");
```
