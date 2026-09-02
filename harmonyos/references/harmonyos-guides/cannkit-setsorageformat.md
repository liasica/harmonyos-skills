---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setsorageformat
title: SetStorageFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > SetStorageFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b0bd2f3ebd9db90538f3cc4fb25a9bd058ba03de07635bb5a066fc1bc4efb7dd
---

## 函数功能

设置运行时Tensor的format。

## 函数原型

```cpp
void SetStorageFormat(const ge::Format storage_format)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| storage\_format | 输入 | 运行时format。  关于ge::Format类型的定义，请参见[Format](cannkit-ge-format.md)。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
Tensor t = {{}, {}, {}, {}, nullptr};
t.SetOriginFormat(ge::FORMAT_NHWC);
t.SetStorageFormat(ge::FORMAT_NC1HWC0);
auto fmt = t.GetStorageFormat(); // ge::FORMAT_NC1HWC0
```
