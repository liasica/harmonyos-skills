---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setstorageformat
title: SetStorageFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageFormat > SetStorageFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:63ff5e661de35b599d65fb0d1f52578347f0575ac226c38be502252f6c1d98e6
---

## 函数功能

设置运行时format。

## 函数原型

```cpp
void SetStorageFormat(const ge::Format storage_format)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| storage\_format | 输入 | 运行时format。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
format.SetStorageFormat(ge::Format::FORMAT_NC);
```
