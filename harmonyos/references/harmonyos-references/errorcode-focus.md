---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-focus
title: 焦点错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 焦点错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:04:52+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:cf8e0f33b89368f2ce1367d3cc5239a2efdcb51a5ac4cc1facab1b10b75bb98c
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 150001 节点无法获得焦点

PhonePC/2in1TabletTVWearable

**错误信息**

the component cannot be focused.

**错误描述**

当前节点无法获得焦点。

**可能原因**

节点默认无法获焦、开发者通过focusable等属性方法设置等。

**处理步骤**

检查当前节点是否支持获焦、是否设置focusable为true。

## 150002 祖先节点无法获得焦点

PhonePC/2in1TabletTVWearable

**错误信息**

This component has an unfocusable ancestor.

**错误描述**

当前节点对应的祖先节点中存在无法获焦节点。

**可能原因**

祖先节点默认无法获焦、开发者通过focusable等属性方法设置等。

**处理步骤**

检查祖先节点是否支持获焦、是否设置focusable为true。

## 150003 节点不存在

PhonePC/2in1TabletTVWearable

**错误信息**

the component is not on tree or does not exist.

**错误描述**

传入的id指向不存在、未挂树或者不可见节点。

**可能原因**

* 传入id错误、节点已经被销毁等。
* 对不具有获焦能力的组件请求焦点。具体组件可查询[组件获焦能力说明](../harmonyos-guides/arkts-common-events-focus-event.md#组件获焦能力说明)。

**处理步骤**

使用正确的id或节点。
