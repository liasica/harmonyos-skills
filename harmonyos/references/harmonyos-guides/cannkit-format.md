---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-format
title: Format
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 原型注册与管理 > OpParamDef > Format
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5d4082534969b71758b080d1fecf44931029e49585eaeebe294b4b988592a812
---

## 函数功能

定义算子参数数据格式。

## 函数原型

```cpp
OpParamDef &Format(std::vector<ge::Format> formats);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| formats | 输入 | 算子参数数据格式，ge::Format请参考[Format](cannkit-ge-format.md)。 |

## 返回值

[OpParamDef](cannkit-paramtype.md)算子定义。

## 约束说明

无
