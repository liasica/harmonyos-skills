---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gmfree
title: GmFree
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 算子调测API > GmFree
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ced4175972e604ac75291be0891c3a7ae0e05d1dec694ce582a3f516be0bf934
---

## 函数功能

进行核函数的CPU侧运行验证时，用于释放通过[GmAlloc](cannkit-gmalloc.md)申请的共享内存。

## 函数原型

```
1. void GmFree(void *ptr)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| ptr | 输入 | 需要释放的共享内存的指针。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 约束说明

传入的指针必须是之前通过GmAlloc申请过的共享内存的指针。

## 调用示例

```
1. AscendC::GmFree((void*)x);
```
