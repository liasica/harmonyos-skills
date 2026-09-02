---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-reset
title: Reset
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TBufPool > Reset
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:7c472bb24574b31302cc8479ba9845da4688888a680e95b52bced0de63989557
---

## 功能说明

完成TbufPool资源的释放与eventId等变量的初始化操作。

## 函数原型

```cpp
__aicore__ inline void Reset()
```

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

切换TBufPool资源池时调用该接口，调用后对应资源池及资源池分配的Buffer不能继续使用。

## 返回值

无

## 调用示例

参考[InitBufPool](cannkit-initbufpool.md)。
