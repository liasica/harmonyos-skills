---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-cancel
title: 取消通知
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 取消通知
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fd53c7ea811a5799ad5f61aba787fe25e8334acc3f6b00d2aea5eadf00247286
---

用户点击通知并拉起应用到前台时，应用可以取消某条通知、部分通知或所有通知。

用户点击桌面图标拉起应用到前台时，用户查看后的应用内消息，应用可以选择取消这些已查看消息的通知。

例如：

场景1：用户收到某个好友的IM消息，点击通知进入应用查看消息后，应用可以取消相关通知提醒。

场景2：用户收到某个好友的IM消息，从桌面图标进入应用查看消息后，应用可以取消相关通知提醒。

## 接口说明

通知取消接口如下。接口详情参见[@ohos.notificationManager (NotificationManager模块)](../harmonyos-references/js-apis-notificationmanager.md)。

| **接口名** | **描述** |
| --- | --- |
| cancel(id: number, callback: AsyncCallback<void>): void | 取消指定的通知。 |
| cancelAll(callback: AsyncCallback<void>): void | 取消所有该应用发布的通知。 |

## 开发步骤

本文以取消文本类型通知为例进行说明，其他类型通知取消操作与此类似。

1. 导入模块。

   ```typescript
   import { notificationManager } from '@kit.NotificationKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const TAG: string = '[PublishOperation]';
   const DOMAIN_NUMBER: number = 0xFF00;
   ```
2. 发布通知。

   参考[发布文本类型通知](text-notification.md)。
3. 取消通知。

   ```typescript
   // 当拉起应用到前台，查看消息后，调用该接口取消通知。
   notificationManager.cancel(1, (err: BusinessError) => {
     if (err) {
       hilog.error(DOMAIN_NUMBER, TAG,
         `Failed to cancel notification. Code is ${err.code}, message is ${err.message}`);
       return;
     }
     hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in canceling notification.');
   });
   ```
