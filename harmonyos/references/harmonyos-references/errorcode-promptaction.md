---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-promptaction
title: 弹窗错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 弹窗错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bd2c67445d6749932731a8713d1ceafe1b1e21c0156c886f1b4402b55e3b5af8
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 103301 自定义弹窗内容节点错误

**错误信息**

The ComponentContent is incorrect.

**说明** 

当接口是[openCustomDialog](arkts-apis-uicontext-promptaction.md#opencustomdialog12)、[openCustomDialogWithController](arkts-apis-uicontext-promptaction.md#opencustomdialogwithcontroller18)、[closeCustomDialog](arkts-apis-uicontext-promptaction.md#closecustomdialog12)和[updateCustomDialog](arkts-apis-uicontext-promptaction.md#updatecustomdialog12)时，返回的错误信息为Dialog content error. The ComponentContent is incorrect.

**错误描述**

自定义弹窗内容节点错误，无法渲染显示。

**可能原因**

使用自定义弹窗时，若传入的自定义内容节点为空或其他错误，将无法正常渲染显示。

**处理步骤**

1. 请确认自定义弹窗的内容节点是否存在，可以通过[getFrameNodeById()](arkts-apis-uicontext-uicontext.md#getframenodebyid12)接口查询。
2. 请确认内容节点能够正常渲染显示。

## 103302 内容节点对应自定义弹窗已存在

**错误信息**

The ComponentContent already exists.

**错误描述**

内容节点对应的自定义弹窗当前已处于弹出状态。

**可能原因**

内容节点对应的自定义弹窗已弹出，此时若重复弹出，会报此错误码。

**处理步骤**

请重新初始化一个能够正常渲染显示的内容节点绑定弹窗。

## 103303 无法找到内容节点对应的自定义弹窗

**错误信息**

The ComponentContent cannot be found.

**说明** 

当接口是[closeCustomDialog](arkts-apis-uicontext-promptaction.md#closecustomdialog12)和[updateCustomDialog](arkts-apis-uicontext-promptaction.md#updatecustomdialog12)时，返回的错误信息为Dialog content not found. The ComponentContent cannot be found.

**错误描述**

内容节点对应的自定义弹窗当前未被弹出。

**可能原因**

内容节点对应的自定义弹窗未弹出，此时若调用关闭或更新自定义弹窗的接口，会报此错误码。

**处理步骤**

1. 请确认内容节点对应的自定义弹窗已弹出。
2. 请确认弹出的自定义弹窗的内容节点为当前需要修改或关闭的特定内容节点。

## 103304 指定的targetId不存在

**错误信息**

The targetId does not exist.

**错误描述**

当无法通过targetId查找到对应的节点时，方法将返回该错误码。

**可能原因**

targetId无效，或者对应的节点已销毁。

**处理步骤**

请确认targetId对应的节点是否存在，可以通过[getFrameNodeById()](arkts-apis-uicontext-uicontext.md#getframenodebyid12)接口查询。

## 103305 指定的targetId对应的节点未挂载在组件树上

**错误信息**

The node of targetId is not in the component tree.

**错误描述**

指定的targetId对应的节点未挂载在组件树上时，方法将返回该错误码。

**可能原因**

指定的targetId对应的节点未挂载在组件树上。

**处理步骤**

1. 请确认targetId对应的节点是否存在，可以通过[getFrameNodeById()](arkts-apis-uicontext-uicontext.md#getframenodebyid12)接口查询。
2. 请确认targetId对应的节点已挂载在主组件树上，可以通过内容节点的[isAttached()](js-apis-arkui-framenode.md#isattached12)接口判断是否被挂载到主组件树上。

## 103307 系统弹出窗口导致无法打开浮层

**错误信息**

The overlay cannot be opened due to the system pop-up window.

**错误描述**

由于系统弹出窗口，无法打开浮层。

**可能原因**

当前页面存在系统弹出窗口，拦截浮层的显示。

**处理步骤**

等待用户关闭系统弹出窗口后重新尝试打开浮层。

## 103401 无法找到对应的文本提示框

**错误信息**

Cannot find the toast.

**错误描述**

对应的文本提示框未弹出或已关闭。

**可能原因**

当文本提示框未弹出或已经关闭时，调用关闭文本提示框接口会报此错误码。

**处理步骤**

请确认文本提示框已弹出。
