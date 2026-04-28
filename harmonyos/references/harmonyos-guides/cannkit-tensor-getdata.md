---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getdata
title: GetData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > GetData
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4d96788605ecbfe719f9a06dc4208350b8925768d63586ac65eb23bfbae0639d
---

## 函数功能

获取Tensor中的数据。

const uint8\_t\* GetData() const返回的数据不可修改，uint8\_t\* GetData()返回的数据可修改。

## 函数原型

```
1. const uint8_t *GetData() const;
2. uint8_t *GetData();
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| const uint8\_t | Tensor中所存放的数据。 |

## 异常处理

无

## 约束说明

无
