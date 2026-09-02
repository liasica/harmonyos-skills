---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-trap
title: Trap
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 调测接口 > Trap
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:16b7c78c16f131e1edba75dd913d85a8a0ef5db7244e92c1442008d7dc8733da
---

## 函数功能

当软件产生异常后，使用该指令终止kernel运行。

## 函数原型

```cpp
__aicore__ inline void Trap()
```

## 参数说明

无

## 返回值

无

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

该接口在kernel需要调试时使用。

## 调用示例

```cpp
AscendC::Trap();
```
