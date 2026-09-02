---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-notification-h
title: notification.h
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > C API > 头文件 > notification.h
category: harmonyos-references
scraped_at: 2026-09-02T15:03:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1008174edb581b874042b3fc37987ac3847364cff801d475702bf1beddac1ad1
---

## 概述

定义通知服务API接口。

**引用文件：** <NotificationKit/notification.h>

**库：** libohnotification.so

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 13

**相关模块：** [NOTIFICATION](capi-notification.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [bool OH\_Notification\_IsNotificationEnabled(void)](capi-notification-h.md#oh_notification_isnotificationenabled) | 查询当前应用通知使能状态。 |

## 函数说明

### OH\_Notification\_IsNotificationEnabled()

```c
bool OH_Notification_IsNotificationEnabled(void)
```

**描述**

查询当前应用通知使能状态。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true - 表示当前应用已使能通知。  false - 表示当前应用未使能通知。 |
