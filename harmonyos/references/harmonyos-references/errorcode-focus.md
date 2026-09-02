---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-focus
title: 焦点错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 焦点错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b0695de28e72df4dd631be261870093301a413c1046d44d2654960ffd24a3a4a
---

**说明** 

焦点错误码用于说明节点获取焦点失败时的常见问题及处理方向，帮助开发者定位焦点异常并采取相应措施。以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 150001 节点无法获得焦点

**错误信息**

the component cannot be focused.

**错误描述**

当前节点无法获得焦点。该错误码为string类型。

**可能原因**

节点默认无法获焦、开发者将节点的focusable属性设置为false等，具体获焦能力请参见[组件获焦能力说明](../harmonyos-guides/arkts-common-events-focus-event.md#组件获焦能力说明)。

**处理步骤**

检查当前节点是否支持获焦，以及是否将focusable设置为true。

## 150002 祖先节点无法获得焦点

**错误信息**

This component has an unfocusable ancestor.

**错误描述**

当前节点对应的祖先节点中存在无法获焦节点。该错误码为string类型。

**可能原因**

祖先节点默认无法获焦、开发者将节点的focusable属性设置为false等，具体获焦能力请参见[组件获焦能力说明](../harmonyos-guides/arkts-common-events-focus-event.md#组件获焦能力说明)。

**处理步骤**

检查祖先节点是否支持获焦，以及是否将focusable设置为true。

## 150003 节点不存在

**错误信息**

the component is not on tree or does not exist.

**错误描述**

传入的id指向不存在或未挂树的节点。该错误码为string类型。

**可能原因**

* 传入的id不存在或指向错误节点，或者id对应的节点已被销毁。
* 对不具有获得焦点能力的组件请求焦点。具体组件可查询[组件获焦能力说明](../harmonyos-guides/arkts-common-events-focus-event.md#组件获焦能力说明)。

**处理步骤**

使用正确的id或节点，并确保节点已挂树、可见且具有获焦能力。
