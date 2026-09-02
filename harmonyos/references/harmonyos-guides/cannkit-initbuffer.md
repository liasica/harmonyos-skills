---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-initbuffer
title: InitBuffer
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TBufPool > InitBuffer
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:884a852bde88832c7a4bc4cadf92ceb4dcacb34a22b92be077b243d0633780c6
---

## 功能说明

调用TBufPool::InitBuffer接口为TQue/TBuf进行内存分配。

## 函数原型

```cpp
template <class T> __aicore__ inline bool InitBuffer(T& que, uint8_t num, uint32_t len);
template <TPosition pos> __aicore__ inline bool InitBuffer(TBuf<pos>& buf, uint32_t len);
```

## 参数说明

**表1** InitBuffer(T& que, uint8\_t num, uint32\_t len) 原型定义参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| que | 输入 | 需要分配内存的TQue对象。 |
| num | 输入 | 分配内存块的个数。 |
| len | 输入 | 每个内存块的大小，单位为Byte，非32Bytes对齐会自动向上补齐至32Bytes对齐。 |

**表2** InitBuffer(TBuf<pos>& buf, uint32\_t len)原型定义参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| buf | 输入 | 需要分配内存的TBuf对象。 |
| len | 输入 | 为TBuf分配的内存大小，单位为Byte，非32Bytes对齐会自动向上补齐至32Bytes对齐。 |

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

声明TBufPool时，可以通过bufIDSize指定可分配Buffer的最大数量，默认上限为4，最大为16。TQue或TBuf的物理内存需要和TBufPool一致。

## 返回值

无

## 调用示例

参考[InitBufPool](cannkit-initbufpool.md)。
