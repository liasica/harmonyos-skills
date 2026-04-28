---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-error-code
title: ArkTS 错误码
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > ArkTS 组件 > ArkTS 错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:09:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3bd6ffdf5e8cd9039244d1f1a9e102d782395ca764be8092f081f9be37c69890
---

说明

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](errorcode-universal.md)。

## 1001202001 代表对端取消流程

PhonePC/2in1TabletTV

**错误信息**

对端取消。

**错误描述**

跨设备互通接口被调用端取消。

**可能原因**

拉起对端应用后对端取消。

**处理步骤**

通过正确的跨设备互通使用流程进行功能测试。

## 1001202002 代表协同框架内部出现错误

PhonePC/2in1TabletTV

**错误信息**

协同框架内部出现错误。

**错误描述**

跨设备互通接口被调用端取消。

**可能原因**

拉起应用后取消。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1001202003 代表本端取消流程

PhonePC/2in1TabletTV

**错误信息**

本端取消。

**错误描述**

跨设备互通接口调用侧取消。

**可能原因**

拉起对端应用后本端取消。

**处理步骤**

通过正确的使用跨设备互通流程进行功能测试。

## 1001202004 代表跨设备互通能力开始

PhonePC/2in1TabletTV

**错误信息**

跨设备互通能力已经拉起。

**错误描述**

跨设备互通能力已经拉起。

**可能原因**

跨设备互通能力已经拉起。

**处理步骤**

属于正常状态code，正常处理即可。

## 1001202005 代表图片全部回传结束

PhonePC/2in1TabletTV

**错误信息**

图片全部回传完毕。

**错误描述**

图片全部回传完毕。

**可能原因**

所有图片已经回传完毕。

**处理步骤**

属于正常状态code，代表所有图片已经回传完毕。

## 1001202006 代表回传文件名称

PhonePC/2in1TabletTV

**错误信息**

回传文件名称。

**错误描述**

回传文件名称。

**可能原因**

本次回传的信息为文件名称。

**处理步骤**

属于正常状态code，代表本次回传的信息为文件名称。

## 1001202007 代表传入的自定义图片张数小于等于0

**错误信息**

传入的自定义图片张数小于等于0。

**错误描述**

传入的自定义图片张数小于等于0。

**可能原因**

使用[createCollaborationServiceMenuItems](servicecollaboration-collaborationservice.md#createcollaborationservicemenuitems-1)传入的自定义图片张数canReceiveNumber小于等于0。

**处理步骤**

使用[createCollaborationServiceMenuItems](servicecollaboration-collaborationservice.md#createcollaborationservicemenuitems-1)时，自定义图片张数canReceiveNumber请传入1到50的值。

## 1001202015 代表视频回传成功

PhonePC/2in1TabletTV

**错误信息**

视频全部回传成功。

**错误描述**

视频全部回传成功。

**可能原因**

视频已经全部回传成功。

**处理步骤**

属于正常状态code，代表本次视频全部回传成功。

## 1001202016 代表回传视频名称

PhonePC/2in1TabletTV

**错误信息**

回传视频名称。

**错误描述**

回传视频名称。

**可能原因**

回传视频名称。

**处理步骤**

属于正常状态code，代表本次回传视频名称。
