---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setnodename
title: SetNodeName
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ComputeNodeInfo > SetNodeName
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1e58a7cfe0aafc50b8f24bfc46a67377a79bdbdc174ea5b719ecbf97530ab7a1
---

## 函数功能

设置该ComputeNodeInfo对应的算子的名称。

## 函数原型

```cpp
void SetNodeName(const ge::char_t *node_name)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| node\_name | 输入 | 算子的名称。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
compute_node_info->SetNodeName("Conv2d");
```
