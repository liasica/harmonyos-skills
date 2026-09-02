---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setsubgraphbuilder
title: SetSubgraphBuilder
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > SetSubgraphBuilder
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:018ae5c13717768bd94c381f200a74524719545c33dce4207277fa4cd2b69415
---

## 函数功能

设置指定子图构建的函数对象。

## 函数原型

```cpp
void SetSubgraphBuilder(const char_t *ir_name, uint32_t index, const SubgraphBuilder &builder);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| ir\_name | 输入 | 子图名称。 |
| index | 输入 | 动态个数子图场景（子图数量不固定），标识子图的序号。 |
| builder | 输入 | 子图构建的函数对象。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
