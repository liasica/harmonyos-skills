---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-servicecollaboration
title: 错误码
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > 错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bc7ccac41714a2adfe34f4cc9424491fdc17fa492c8117ac325512e392e310f6
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](errorcode-universal.md)。

## 1001202001 代表对端取消流程

**错误信息**

The peer end cancels the operation.

**错误描述**

跨设备互通接口被调用端取消。

**可能原因**

拉起对端应用后对端取消。

**处理步骤**

通过正确的跨设备互通使用流程进行功能测试。

## 1001202002 代表协同框架内部出现错误

**错误信息**

An error occurred within the collaborative framework.

**错误描述**

协同框架内部出现错误。

**可能原因**

拉起应用后取消。

**处理步骤**

请尝试重新点击设备列表使用跨设备互通能力，如多次尝试无果仍有此问题请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1001202003 代表本端取消流程

**错误信息**

The local end cancels the operation.

**错误描述**

跨设备互通接口调用侧取消。

**可能原因**

拉起对端应用后本端取消。

**处理步骤**

通过正确的使用跨设备互通流程进行功能测试。

## 1001202004 代表跨设备互通能力开始

**错误信息**

The device interconnectivity has been established.

**错误描述**

跨设备互通能力已经拉起。

**可能原因**

跨设备互通能力已经拉起。

**处理步骤**

属于正常状态code，正常处理即可。

## 1001202005 代表图片全部回传结束

**错误信息**

All images have been successfully sent back.

**错误描述**

图片全部回传完毕。

**可能原因**

所有图片已经回传完毕。

**处理步骤**

属于正常状态code，代表所有图片已经回传完毕。

## 1001202006 正在回传多个图片

**错误信息**

Multiple images are being sent back.

**错误描述**

正在回传多个图片。

**可能原因**

正在回传多个图片。

**处理步骤**

属于正常状态code，代表正在回传多个图片。

## 1001202007 代表传入的自定义图片张数小于等于0

**错误信息**

The number of input custom images is less than or equal to 0.

**错误描述**

传入的自定义图片张数小于等于0。

**可能原因**

使用[createCollaborationServiceMenuItems](servicecollaboration-collaborationservice.md#createcollaborationservicemenuitems-1)传入的自定义图片张数canReceiveNumber小于等于0。

**处理步骤**

使用[createCollaborationServiceMenuItems](servicecollaboration-collaborationservice.md#createcollaborationservicemenuitems-1)时，自定义图片张数canReceiveNumber请传入1到50的值。

## 1001202015 代表视频回传成功

**错误信息**

All videos have been successfully sent back.

**错误描述**

视频全部回传成功。

**可能原因**

视频已经全部回传成功。

**处理步骤**

属于正常状态code，代表本次视频全部回传成功。

## 1001202016 正在回传多个视频

**错误信息**

Multiple videos are being sent back.

**错误描述**

正在回传多个视频。

**可能原因**

正在回传多个视频。

**处理步骤**

属于正常状态code，代表正在回传多个视频。

## 1001202017 内存不足视频回传失败

**错误信息**

Out of memory, video send back failed.

**错误描述**

内存不足视频回传失败。

**可能原因**

内存不足视频回传失败。

**处理步骤**

代表内存不足视频回传失败，请进行开发者内存分析后修复代码逻辑。

## 1028501001 IPC通信异常

**错误信息**

IPC communication exception.

**错误描述**

IPC通信异常。

**可能原因**

系统侧进程出现过异常。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1028501002 参数错误

**错误信息**

Invalid parameter.

**错误描述**

参数错误。

**可能原因**

接口入参传入非法值。

**处理步骤**

检查出现异常的接口方法的入参传入是否正确。
