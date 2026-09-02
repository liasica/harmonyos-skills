---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdata
title: GetData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > GetData
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:a3121dc74eaa82f8300b95d53a021c72d20e8f4f876e3fdd533b54b88bc2f7db
---

## 函数功能

获取Tensor的数据地址。

## 函数原型

```cpp
template<class T>  const T *GetData() const
template<class T>  T *GetData()
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| T | 输入 | 数据类型。 |

## 返回值

数据地址。

## 约束说明

无

## 调用示例

```cpp
Tensor tensor{{{8, 3, 224, 224}, {16, 3, 224, 224}}, // shape
              {ge::FORMAT_ND, ge::FORMAT_FRACTAL_NZ, {}}, // format
              kFollowing, // placement
              ge::DT_FLOAT16, // dt
              nullptr};
auto addr = tensor.GetData<int64_t>();
```
