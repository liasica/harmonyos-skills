---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-snapshot
title: 截图错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:04:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fcef2a3c1c7f01412204587f24fa3d5d3019a33f62cd3c95d6430f5148c47bcc
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 160001 图像加载错误

PhonePC/2in1TabletTVWearable

**错误信息**

An image component in builder is not ready for taking a snapshot. The check for the ready state is required when the checkImageStatus option is enabled.

**错误描述**

图像加载错误。

**可能原因**

在进行截图操作前，若Image组件解码检查失败或节点图像加载失败。此时，调用截图接口，将可能触发相应的错误码。

**处理步骤**

设置相应截图接口的delay延时参数，以确保图像加载成功。

## 160002 截图超时

PhonePC/2in1TabletTVWearable

**错误信息**

Timeout.

**错误描述**

图像加载超时。

**可能原因**

系统任务未执行。

**处理步骤**

改用当前截图接口对应的异步接口。

## 160003 截图选项不支持的色彩空间或动态范围模式

PhonePC/2in1TabletTVWearable

**错误信息**

Unsupported color space or dynamic range mode in snapshot options.

**错误描述**

截图选项中设置了不支持的色彩空间或动态范围模式。

**可能原因**

截图选项中设置的色彩空间或动态范围模式值不在支持范围内。

**处理步骤**

修改截图选项中设置的色彩空间或动态范围模式值为支持范围内的值。

## 160004 离屏节点截图不支持色彩空间或动态范围模式的isAuto参数设置为true

PhonePC/2in1TabletTVWearable

**错误信息**

isAuto(true) is not supported for offscreen node snapshots.

**错误描述**

对离屏节点截图时，色彩空间或动态范围模式的isAuto参数被设置为true。

**可能原因**

对离屏节点截图时，不支持截图选项中的色彩空间或动态范围模式的isAuto参数设置为true。

**处理步骤**

将截图选项中色彩空间或动态范围模式的isAuto参数设置为false。
