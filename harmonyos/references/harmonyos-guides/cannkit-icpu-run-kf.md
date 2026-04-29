---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-icpu-run-kf
title: ICPU_RUN_KF
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 算子调测API > ICPU_RUN_KF
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:86d22e323629fe0d1a73032fb3f08096f9c70b0d4739b4c88604e648b3a35ab7
---

## 函数功能

进行核函数的CPU侧运行验证时，CPU调测总入口，完成CPU侧的算子程序调用。

## 函数原型

```
1. #define ICPU_RUN_KF(func, blkdim, ...)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| func | 输入 | 算子的kernel函数指针。 |
| blkdim | 输入 | 算子的核心数，corenum。 |
| ... | 输入 | 所有的入参和出参，依次填入。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 约束说明

除了func、blkdim以外，其他的变量都必须是通过GmAlloc分配的共享内存的指针，传入的参数的数量和顺序都必须和kernel保持一致。

## 调用示例

```
1. ICPU_RUN_KF(sort_kernel0, coreNum, (uint8_t*)x, (uint8_t*)y);
```
