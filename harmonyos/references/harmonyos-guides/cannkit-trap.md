---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-trap
title: Trap
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 调测接口 > Trap
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1a3ec8423103191e3e8321ec58ce5afd57de51ea7e80c9968542678ca4847faf
---

## 函数功能

当软件产生异常后，使用该指令使kernel中止运行。

## 函数原型

```
1. __aicore__ inline void Trap()
```

## 参数说明

无

## 返回值

无

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 注意事项

该接口在kernel需要调试时使用。

## 调用示例

```
1. AscendC::Trap();
```
