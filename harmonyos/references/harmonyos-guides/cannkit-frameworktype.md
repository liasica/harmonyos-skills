---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-frameworktype
title: FrameworkType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > FrameworkType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:fb9c5c3700454d509578d9f5bc458ef487fee453181bcb38abc943659ebb8f70
---

## 函数功能

设置原始模型的框架类型。

## 函数原型

```cpp
OpRegistrationData &FrameworkType(const domi::FrameworkType &fmk_type)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| fmk\_type | 输入 | 框架类型。  - CAFFE  - TENSORFLOW  - ONNX  FrameworkType枚举值如下：CAFFE、MINDSPORE、TENSORFLOW、ANDROID\_NN、ONNX、FRAMEWORK\_RESERVED。 |
