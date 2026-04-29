---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gmalloc
title: GmAlloc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 算子调测API > GmAlloc
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:73cbdf3fbce31ce1ae447b99fc3e1df8138bf82c33b5eca7dee166499d7b5b45
---

## 函数功能

进行核函数的CPU侧运行验证时，用于创建共享内存：在/tmp目录下创建一个共享文件，并返回该文件的映射指针。

## 函数原型

```
1. void *GmAlloc(size_t size)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| size | 输入 | 开发者想要申请的共享内存大小。 |

## 返回值

返回一个void\*指针，该指针表示该共享内存空间的首地址。

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 约束说明

该接口在系统的/tmp目录下生成临时文件，故需要磁盘空间足够才可以正常生成共享内存。

## 调用示例

```
1. constexpr int32_t len = 8 * 32 * 1024 * 8;
2. half* x = (half*) GmAlloc(len*sizeof(half));
```
