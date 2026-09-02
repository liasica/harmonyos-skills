---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storageshape-operatorb
title: operator!=
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageShape > operator!=
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e386c7b408f16bc0d6ddeb349961ee1e4fbe052b9f70be3c16850c2b72c75959
---

## 函数功能

判断shape是否不相等。

## 函数原型

```cpp
bool operator!=(const StorageShape &other) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| other | 输入 | 另一个shape。 |

## 返回值

true：不相等。

false：相等。

## 约束说明

无

## 调用示例

```cpp
StorageShape shape0({3, 256, 256}, {256, 256, 3});
StorageShape shape1({3, 256, 256}, {3, 256, 256});
bool is_diff_shape = shape0 != shape1; // true
```
