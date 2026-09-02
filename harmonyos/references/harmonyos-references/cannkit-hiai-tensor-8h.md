---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-hiai-tensor-8h
title: hiai_tensor.h
breadcrumb: API参考 > AI > CANN Kit（CANN异构计算框架服务） > C API > 头文件和结构体 > 头文件 > hiai_tensor.h
category: harmonyos-references
scraped_at: 2026-09-02T15:03:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:99ae7788bd9268de17a21c566b56f1a02cf00688a3f764dc647129f00179bfc9
---

## 概述

模型推理时使用的输入输出内存相关的辅助接口。

通过以下接口，可以关联AippParam到tensor中，也可计算图片格式需要申请的tensor内存大小。

**引用文件：** <CANNKit/hiai\_tensor.h>

**库：** libhiai\_foundation.so

**系统能力：** SystemCapability.AI.HiAIFoundation

**起始版本：** 4.1.0(11)

**相关模块：** [CANN](cannkit.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| size\_t [HMS\_HiAITensor\_GetSizeWithImageFormat](cannkit.md#hms_hiaitensor_getsizewithimageformat) (NN\_TensorDesc \*desc, [HiAI\_ImageFormat](cannkit.md#hiai_imageformat) format) | 根据NN\_TensorDesc和HiAI\_ImageFormat计算申请tensor的大小。 |
| OH\_NN\_ReturnCode [HMS\_HiAITensor\_SetAippParams](cannkit.md#hms_hiaitensor_setaippparams) (NN\_Tensor \*tensor, [HiAI\_AippParam](cannkit.md#hiai_aippparam) \*aippParams[], size\_t aippNum) | 给NN\_Tensor设置AippParams。 |
