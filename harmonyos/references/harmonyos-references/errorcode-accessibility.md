---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility
title: 无障碍子系统错误码
breadcrumb: API参考 > 应用框架 > Accessibility Kit（无障碍服务） > 错误码 > 无障碍子系统错误码
category: harmonyos-references
scraped_at: 2026-04-28T07:59:07+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:98169510b4aa04de8d90b4b0535517ac65af0cd9f31289252be0eee87a79a03f
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 9300003 不具备执行该操作的无障碍权限

PhonePC/2in1TabletWearable

**错误信息**

No accessibility permission to perform the operation.

**错误描述**

当应用执行了用户在启用无障碍扩展应用时没有开启的辅助操作时，方法将返回该错误码。

**可能原因**

该错误码表示应用不具备该操作的无障碍权限，可能原因是应用执行了用户在启用无障碍扩展应用时没有开启的辅助操作。

**处理步骤**

1. 尝试向用户提示请求执行无障碍辅助操作的必要性，并获取用户授权。
2. 重新启用无障碍扩展应用，并开启所需的辅助操作。

## 9300004 属性不存在

PhonePC/2in1TabletWearable

**错误信息**

This property does not exist.

**错误描述**

当输入无障碍节点元素中不存在的属性时，方法将返回该错误码。

**可能原因**

该错误码表示输入了无效的无障碍节点元素的属性，即无障碍节点元素中不存在该属性。

**处理步骤**

检查无障碍节点元素中是否存在该属性。

## 9300005 不支持该操作

PhonePC/2in1TabletWearable

**错误信息**

This action is not supported.

**错误描述**

当应用执行无障碍节点元素不支持的操作时，方法将返回该错误码。

**可能原因**

该错误码表示执行了无障碍节点元素不支持的操作。

**处理步骤**

确认该无障碍节点元素支持的操作列表中是否包含该操作。
