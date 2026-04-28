---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setoriginformat
title: SetOriginFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageFormat > SetOriginFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d4df10ae24eef6095dbf03d6aa8107d7a2f84abc5f348c4c34d938147c4568a9
---

## 函数功能

设置原始format。

## 函数原型

```
1. void SetOriginFormat(const ge::Format origin_format)
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

```
1. ExpandDimsType dim_type("1100");
2. StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
3. format.SetOriginFormat(ge::Format::FORMAT_NC);
```
