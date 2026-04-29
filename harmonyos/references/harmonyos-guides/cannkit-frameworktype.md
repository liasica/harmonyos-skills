---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-frameworktype
title: FrameworkType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > FrameworkType
category: harmonyos-guides
scraped_at: 2026-04-29T13:42:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a61795237712b0d34f8666ac211a1084390163e4df9c28c9f160fece46e30396
---

## 函数功能

设置原始模型的框架类型。

## 函数原型

```
1. OpRegistrationData &FrameworkType(const domi::FrameworkType &fmk_type)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| fmk\_type | 输入 | 框架类型。  - CAFFE  - TENSORFLOW  - ONNX  FrameworkType枚举值的如下：CAFFE、MINDSPORE、TENSORFLOW、ANDROID\_NN、ONNX、FRAMEWORK\_RESERVED。 |
