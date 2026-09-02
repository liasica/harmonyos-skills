---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-end
title: End
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 高阶API > 矩阵相乘 > Matmul > End
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:12bc4a6d051948408c89b44130b98232feb05d53b574428227d507a946cfe80f
---

## 功能说明

单核内Matmul矩阵相乘计算结束后必须调用一次End函数。

## 函数原型

```cpp
__aicore__ inline void End()
```

## 参数说明

无

## 返回值

无

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

## 注意事项

无

## 调用示例

```cpp
mm.IterateAll(gm_c);
mm.End();
```
