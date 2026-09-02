---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-setoriginformat
title: SetOriginFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > SetOriginFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1c6a73e6a8f65d00c9a8d2e10870bfe3101112ee170ef0e09c5fe7f8d63e5317
---

## 函数功能

设置Tensor的原始format。

## 函数原型

```cpp
void SetOriginFormat(const ge::Format origin_format)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| origin\_format | 输入 | 原始format。  关于ge::Format类型的定义，请参见[Format](cannkit-ge-format.md)。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
Tensor t = {{}, {}, {}, {}, nullptr};
t.SetOriginFormat(ge::FORMAT_NHWC);
t.SetStorageFormat(ge::FORMAT_NC1HWC0);
auto fmt = t.GetOriginFormat(); // ge::FORMAT_NHWC
```
