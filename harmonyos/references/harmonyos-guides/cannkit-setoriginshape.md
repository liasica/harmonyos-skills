---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setoriginshape
title: SetOriginShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > SetOriginShape
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:60d90c674510e32cb9848000616fc5b4e413667f11e058be4168b08eb985eafe
---

## 函数功能

向TensorDesc中设置Tensor的原始Shape。

该Shape是指原始网络模型的Shape。

## 函数原型

```cpp
void SetOriginShape(const Shape &originShape);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| originShape | 输入 | 向TensorDesc设置原始的originShape对象。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
