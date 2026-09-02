---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getaddr
title: GetAddr
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > GetAddr
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:869d8e5c409541a4c0c638866e7de5a21241a02a060790a1bf4ea72a28755205
---

## 函数功能

获取Tensor的数据地址。

## 函数原型

```cpp
const void *GetAddr() const
void *GetAddr()
```

## 参数说明

无

## 返回值

返回数据地址。

## 约束说明

无

## 调用示例

```cpp
Tensor tensor{{{8, 3, 224, 224}, {16, 3, 224, 224}}, // shape
              {ge::FORMAT_ND, ge::FORMAT_FRACTAL_NZ, {}}, // format
              kFollowing, // placement
              ge::DT_FLOAT16, // dt
              nullptr};
auto addr = tensor.GetAddr();
```
