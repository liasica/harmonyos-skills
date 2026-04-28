---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-error-code
title: ArkTS API错误码
breadcrumb: API参考 > 应用框架 > UI Design Kit（UI设计套件） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:06:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5c9b578fc677d489bf004c48941feeae180567787555b94829e4eae115736c08
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 1012600001 并发任务忙碌

PhonePC/2in1TabletTV

**错误信息**

Task is busy.

**错误描述**

并发任务忙碌。

**可能原因**

上一个并发任务还没结束。

**处理步骤**

1. 检查 [hdsDrawable.getHdsLayeredIcons](ui-design-hdsdrawable.md#hdsdrawablegethdslayeredicons)， [hdsDrawable.getHdsIcons](ui-design-hdsdrawable.md#hdsdrawablegethdsicons)的调用是否在对应返回结果后再执行，或者使用单次处理的API接口进行处理。
2. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1012600002 资源大小超过规格限制

PhonePC/2in1TabletTV

**错误信息**

Resource size error. The ttf resource out of size.

Resource size error. The json resource out of size.

**错误描述**

资源大小超过规格限制。

**可能原因**

用户传入的资源大小超过规格限制的大小，限制用户最多自定义10个图标。

**处理步骤**

裁剪接口传入的自定义Symbol图标个数以及配套动效参数个数。

## 1012600003 资源解析失败

PhonePC/2in1TabletTV

**错误信息**

Resource error. Parse the ttf resource failed.

Resource error. Parse the json resource failed.

**错误描述**

资源解析失败。

**可能原因**

用户传入的资源内容有误。

**处理步骤**

1. 请检查传入的图标资源是否正确。
2. 请检查传入的动效参数资源是否正确。
