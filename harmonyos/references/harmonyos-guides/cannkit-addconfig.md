---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-addconfig
title: AddConfig
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 原型注册与管理 > OpAICoreDef > AddConfig
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cae3d2d86eaa53f541d0d95195d8d89afc20bf981b4f72891b16285bc1254e20
---

## 函数功能

注册算子支持的AI处理器型号信息。

## 函数原型

```
1. void AddConfig(const char *soc);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| soc | 输入 | 支持AI处理器型号。 |

## 返回值

无

## 约束说明

支持Kirin9020系列处理器

KirinX90系列处理器
