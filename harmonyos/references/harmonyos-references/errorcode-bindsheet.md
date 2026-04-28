---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bindsheet
title: 半模态错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 半模态错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:04:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:152cda3e36e1bb7b4032cb39865e93a36c7c1c8f7c21b6376d52bb4e90097a32
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 120001 内容节点对应半模态页面错误

PhonePC/2in1TabletTVWearable

**错误信息**

The bindSheetContent is incorrect.

**错误描述**

输入的bindSheetContent错误，系统会产生此错误码。

**可能原因**

输入的bindSheetContent错误。

**处理步骤**

请检查输入的bindSheetContent是否正确。

## 120002 内容节点对应半模态页面已存在

PhonePC/2in1TabletTVWearable

**错误信息**

The bindSheetContent already exists.

**错误描述**

内容节点对应的半模态页面已处于打开状态。

**可能原因**

内容节点对应的半模态页面当前已显示，此时若重复打开，会报此错误码。

**处理步骤**

请检查输入的bindSheetContent是否重复。

## 120003 无法找到内容节点对应的半模态页面

PhonePC/2in1TabletTVWearable

**错误信息**

The bindSheetContent cannot be found.

**错误描述**

内容节点对应的半模态页面未被打开。

**可能原因**

内容节点对应的半模态页面当前未显示，此时若调用关闭或更新半模态页面的接口，会报此错误码。

**处理步骤**

请检查输入的bindSheetContent是否存在。

## 120004 指定的targetId不存在

PhonePC/2in1TabletTVWearable

**错误信息**

The targetId does not exist.

**错误描述**

当无法通过targetId查找到对应的节点时，方法将返回该错误码。

**可能原因**

targetId是无效的，或者其对应的节点已销毁。

**处理步骤**

1. 检查targetId是否非负数；
2. 检查targetId对应的节点是否有效；

## 120005 指定的targetId对应的节点未挂载在节点树上

PhonePC/2in1TabletTVWearable

**错误信息**

The node of targetId is not in the component tree.

**错误描述**

当将半模态页面指定为EMBEDDED模式时，指定的targetId对应的节点未挂载在节点树上时，方法将返回该错误码。

**可能原因**

指定的targetId对应的节点未挂载在节点树上。

**处理步骤**

等待targetId对应的节点挂载上树后，再调用方法；或者将半模态页面指定为OVERLAY模式。

## 120006 指定的targetId对应的节点并不是page节点或NavDestination节点的子节点

PhonePC/2in1TabletTVWearable

**错误信息**

The node of targetId is not a child of the page node or NavDestination node.

**错误描述**

指定的targetId对应的节点并不是page节点或NavDestination节点的子节点时，方法将返回该错误码。

**可能原因**

当将半模态页面指定为EMBEDDED模式时，无法从targetId对应节点的父节点中查找到page节点或NavDestination节点的子节点。

**处理步骤**

更换一个可查找到page节点或NavDestination节点的targetId；或者将半模态页面指定为OVERLAY模式。
