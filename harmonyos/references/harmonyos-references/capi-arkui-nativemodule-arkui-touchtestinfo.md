---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-touchtestinfo
title: ArkUI_TouchTestInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_TouchTestInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:04:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bbfe50d3f1d5e9ca44639fcb5b6a2bab2552f65d28a03eb6f9296963a6f7236b
---

```
1. typedef struct ArkUI_TouchTestInfo ArkUI_TouchTestInfo
```

## 概述

PhonePC/2in1TabletTVWearable

定义触摸测试信息。

当用户通过[registerNodeEvent](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)注册了[NODE\_ON\_CHILD\_TOUCH\_TEST](capi-native-node-h.md#arkui_nodeeventtype)事件时，才能接收到此事件。触摸测试信息包含触摸测试策略、命中测试过程中需要作用的子组件ID和触摸测试信息项的列表。

**起始版本：** 22

**相关模块：** [ArkUI\_EventModule](capi-arkui-eventmodule.md)

**所在头文件：** [ui\_input\_event.h](capi-ui-input-event-h.md)
