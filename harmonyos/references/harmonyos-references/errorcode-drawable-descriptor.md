---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-drawable-descriptor
title: DrawableDescriptor错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > DrawableDescriptor错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f0b156c249a247f13770a01626717b2cfd71498704e219398fa8aea458201856
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)。

## 111001 资源加载失败

**错误信息**

resource loading failed.

**错误描述**

该错误码在资源加载失败时被触发。

**可能原因**

路径不存在，资源不存在或者文件已损坏。

**处理步骤**

检查资源是否存在或文件是否损坏。

## 111002 资源已释放

**错误信息**

The native memory referenced by the drawableDescriptor has been released.

**错误描述**

该错误码在DrawableDescriptor引用的native内存已被释放时被触发。当调用[release](js-apis-arkui-drawabledescriptor.md#release)方法释放资源后，再调用[getPixelMap](js-apis-arkui-drawabledescriptor.md#getpixelmap)、[getForeground](js-apis-arkui-drawabledescriptor.md#getforeground)、[getBackground](js-apis-arkui-drawabledescriptor.md#getbackground)、[getMask](js-apis-arkui-drawabledescriptor.md#getmask)、[loadSync](js-apis-arkui-drawabledescriptor.md#loadsync21)、[load](js-apis-arkui-drawabledescriptor.md#load21)等接口时会触发此错误。

**可能原因**

在调用[release](js-apis-arkui-drawabledescriptor.md#release)释放DrawableDescriptor资源后，继续调用该对象的其他接口。

**处理步骤**

1. 在调用getPixelMap等接口前，通过[isReleased](js-apis-arkui-drawabledescriptor.md#isreleased)检查对象是否已释放。
2. 避免在[release](js-apis-arkui-drawabledescriptor.md#release)后继续使用该DrawableDescriptor对象。
