---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-touchtestinfo
title: ArkUI_TouchTestInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_TouchTestInfo
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:481d19dfce6df9f72686aac3f9a268a67c933c74674924d599250d16504e6811
---

```
typedef struct ArkUI_TouchTestInfo ArkUI_TouchTestInfo
```

## 概述

定义触摸测试信息，用于在命中测试过程中获取触摸测试策略、参与命中测试的子组件ID及触摸测试信息项列表，适用于需要在子组件触摸事件中获取命中测试详细信息以自定义命中测试逻辑、优化触摸事件分发与响应的场景。

当用户通过[registerNodeEvent](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)注册了[NODE\_ON\_CHILD\_TOUCH\_TEST](capi-native-node-h.md#arkui_nodeeventtype)事件时，才能接收到此事件。触摸测试信息包含触摸测试策略、命中测试过程中需要参与命中测试的子组件ID和触摸测试信息项的列表。

**起始版本：** 22

**相关模块：** [ArkUI\_EventModule](capi-arkui-eventmodule.md)

**所在头文件：** [ui\_input\_event.h](capi-ui-input-event-h.md)
