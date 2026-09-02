---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gmfree
title: GmFree
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 算子调测API > GmFree
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:6d976eff80a3237720752c5bad8d00e59e9064781b67e5c8033d065e9d839084
---

## 函数功能

进行核函数的CPU侧运行验证时，用于释放通过[GmAlloc](cannkit-gmalloc.md)申请的共享内存。

## 函数原型

```cpp
void GmFree(void *ptr)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| ptr | 输入 | 需要释放的共享内存的指针。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 约束说明

传入的指针必须是之前通过GmAlloc申请过的共享内存的指针。

## 调用示例

```cpp
AscendC::GmFree((void*)x);
```
