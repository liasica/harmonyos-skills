---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setoriginformat
title: SetOriginFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageFormat > SetOriginFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3cab736cedbf3dcba3a94a981e27dfa238d9396393f81c84df1282fdb36bbbaf
---

## 函数功能

设置原始format。

## 函数原型

```cpp
void SetOriginFormat(const ge::Format origin_format)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| origin\_format | 输入 | 原始format。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
format.SetOriginFormat(ge::Format::FORMAT_NC);
```
