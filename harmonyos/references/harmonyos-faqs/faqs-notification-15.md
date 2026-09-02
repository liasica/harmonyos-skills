---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-15
title: 如何打开横幅通知
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 如何打开横幅通知
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:30+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:f23ea5c44f6ee883a8d2c91d3bb3b3d2405533e8189f72a1b4f490f6bd554138
---

## 问题现象

配置了用户通知服务后，但是横幅通知没有显示，如何配置应用以启用横幅通知。

## 背景知识

当应用中的“允许通知”开关开启时，横幅通知默认关闭（不支持应用配置、用户可手动开启）；SlotType为SOCIAL\_COMMUNICATION和SERVICE\_INFORMATION类型时才会打开横幅通知，参考链接[通知渠道类型说明](../harmonyos-guides/notification-slot.md#通知渠道类型说明)。

## 解决方案

完整流程如下：

1. 可通过[requestEnableNotification](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10)的错误码判断用户是否授权。若返回的错误码为1600004，即为拒绝授权。

   ```ts
   notificationManager.isNotificationEnabled().then((data: boolean) => {
         hilog.info(DOMAIN_NUMBER, TAG, 'isNotificationEnabled success, data: ' + JSON.stringify(data));
         if (!data) {
           notificationManager.requestEnableNotification(this.context).then(() => {
             hilog.info(DOMAIN_NUMBER, TAG, `[ANS] requestEnableNotification success`);
           }).catch((err: BusinessError) => {
             if (1600004 === err.code) {
               hilog.error(DOMAIN_NUMBER, TAG,
                 `[ANS] requestEnableNotification refused, code is ${err.code}, message is ${err.message}`);
             } else {
               hilog.error(DOMAIN_NUMBER, TAG,
                 `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
             }
           });
         }
       }).catch((err: BusinessError) => {
         hilog.error(DOMAIN_NUMBER, TAG, `isNotificationEnabled fail, code is ${err.code}, message is ${err.message}`);
       });
   ```
2. 拉起应用的通知设置界面，引导用户打开横幅通知。

   ```ts
   notificationManager.openNotificationSettings(this.context).then(() => {
         hilog.info(0x0000, 'testTag', `[ANS] openNotificationSettings success`);
       }).catch((err: BusinessError) => {
         hilog.error(0x0000, 'testTag',
           `[ANS] openNotificationSettings failed, code is ${err.code}, message is ${err.message}`);
       });
   ```

   **说明** 

   从HarmonyOS 7.0 beta版本开始，支持通过[notificationManager.getNotificationSetting()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagergetnotificationsetting20)获取当前应用通知设置状态，返回的NotificationSetting中bannerEnabled表示横幅通知开启状态。如未开启横幅通知，可调用[notificationManager.openNotificationSettingsWithResult()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanageropennotificationsettingswithresult)拉起应用通知设置页面，用户完成设置后会返回NotificationSetting，根据bannerEnabled判断是否开启了横幅通知。

   ```ts
   notificationManager.getNotificationSetting().then((data: notificationManager.NotificationSetting) => {
     hilog.info(DOMAIN_NUMBER, TAG, `getNotificationSetting success, data: ${JSON.stringify(data)}`);
     if (!data.bannerEnabled) {
       const context = this.getUIContext().getHostContext();
       if (context) {
         let uiAbilityContext: common.UIAbilityContext = context as common.UIAbilityContext;
         notificationManager.openNotificationSettingsWithResult(uiAbilityContext)
           .then((result: notificationManager.NotificationSetting) => {
             hilog.info(DOMAIN_NUMBER, TAG,
               `[ANS] openNotificationSettingsWithResult success, result: ${JSON.stringify(result)}`);
           }).catch((err: BusinessError) => {
             hilog.error(DOMAIN_NUMBER, TAG,
               `[ANS] openNotificationSettingsWithResult failed, code is ${err.code}, message is ${err.message}`);
           });
       }
     }
   }).catch((err: BusinessError) => {
     hilog.error(DOMAIN_NUMBER, TAG, `getNotificationSetting failed, code is ${err.code}, message is ${err.message}`);
   });
   ```
3. 构造SlotType为SOCIAL\_COMMUNICATION或SERVICE\_INFORMATION类型的NotificationRequest对象，并发布通知。

   ```ts
   let notificationRequest: notificationManager.NotificationRequest = {
         id: 1,
         content: {
           notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT, // 普通文本类型通知
           normal: {
             title: 'test_title',
             text: 'Notification published',
             additionalText: 'test_additionalText',
           },
         },
         // 设置通知渠道类型为社交通信SOCIAL_COMMUNICATION或者SERVICE_INFORMATION
         notificationSlotType: notificationManager.SlotType.SOCIAL_COMMUNICATION,
       };
       notificationManager.publish(notificationRequest, (err: BusinessError) => {
         if (err) {
           hilog.error(DOMAIN_NUMBER, TAG,
             `Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
           return;
         }
         hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in publishing notification.');
       });
   ```

   效果图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/B4PxHER2QyO6WW9K7X-1DQ/zh-cn_image_0000002680319919.png "点击放大")

完整代码如下：

```ts
import { common } from '@kit.AbilityKit';
import { notificationManager } from '@kit.NotificationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '[PublishOperation]';
const DOMAIN_NUMBER: number = 0xFF00;

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  checkNotificationPermission() {
    // Start solution1
    notificationManager.isNotificationEnabled().then((data: boolean) => {
      hilog.info(DOMAIN_NUMBER, TAG, 'isNotificationEnabled success, data: ' + JSON.stringify(data));
      if (!data) {
        notificationManager.requestEnableNotification(this.context).then(() => {
          hilog.info(DOMAIN_NUMBER, TAG, `[ANS] requestEnableNotification success`);
        }).catch((err: BusinessError) => {
          if (1600004 === err.code) {
            hilog.error(DOMAIN_NUMBER, TAG,
              `[ANS] requestEnableNotification refused, code is ${err.code}, message is ${err.message}`);
          } else {
            hilog.error(DOMAIN_NUMBER, TAG,
              `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
          }
        });
      }
    }).catch((err: BusinessError) => {
      hilog.error(DOMAIN_NUMBER, TAG, `isNotificationEnabled fail, code is ${err.code}, message is ${err.message}`);
    });
    // End solution1
  }

  openNotificationSetting() {
    // Start solution2
    notificationManager.openNotificationSettings(this.context).then(() => {
      hilog.info(0x0000, 'testTag', `[ANS] openNotificationSettings success`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag',
        `[ANS] openNotificationSettings failed, code is ${err.code}, message is ${err.message}`);
    });
    // End solution2
  }

  publishNotification() {
    // Start solution3
    let notificationRequest: notificationManager.NotificationRequest = {
      id: 1,
      content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT, // 普通文本类型通知
        normal: {
          title: 'test_title',
          text: 'Notification published',
          additionalText: 'test_additionalText',
        },
      },
      // 设置通知渠道类型为社交通信SOCIAL_COMMUNICATION或者SERVICE_INFORMATION
      notificationSlotType: notificationManager.SlotType.SOCIAL_COMMUNICATION,
    };
    notificationManager.publish(notificationRequest, (err: BusinessError) => {
      if (err) {
        hilog.error(DOMAIN_NUMBER, TAG,
          `Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
        return;
      }
      hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in publishing notification.');
    });
    // End solution3
  }

  aboutToAppear(): void {
    this.checkNotificationPermission();
  }

  build() {
    Column({ space: 10 }) {
      Button('publish')
        .onClick(() => {
          this.publishNotification();
        })
      Button('点击拉起应用设置页面')
        .onClick(() => {
          this.openNotificationSetting();
        })
    }
    .padding({ right: '16px', left: '16px' })
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}
```

## 常见FAQ

Q：APP处于前台时，三方推送通知会横幅展示，如何不进行展示。

A：推送通知扩展消息需要申请场景化消息权益，申请该权益存在限制该场景化消息仅为有商家新订单提醒、商家收款场景的应用开放，其他场景不支持该能力。若您的应用进程在前台，则不弹出通知提醒，您可以在应用进程中获取通知扩展消息内容并自行完成业务处理，具体参考：[发送通知扩展消息](../harmonyos-guides/push-send-extend-noti.md)。

Q：横幅通知上划后，再次调用不会弹出横幅通知，是什么原因？

A：用户有横幅通知的上划动作，从不过于打扰用户的方面考虑，一分钟内不再弹出横幅，但是通知的响铃提示音在此期间是可以正常提示的；一分钟之后，如果有新消息通知的话，才会继续弹出横幅。

Q：应用是否可以主动关闭推送通知扩展消息的横幅通知？

A：在用户同意应用横幅通知情况下，当前应用服务端推送通知扩展消息给应用时，应用无法主动关闭横幅通知。如果应用想实现某些特殊使用场景下，不进行推送，可以将应用状态传递给服务端，服务端过滤掉这些设备，不进行推送。

Q：如何在代码中判断横幅通知是否已开启？

A：从HarmonyOS 7.0 beta版本开始，可调用[notificationManager.getNotificationSetting()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagergetnotificationsetting20)获取当前应用通知设置状态，返回的NotificationSetting中bannerEnabled字段表示横幅通知开启状态。如未开启，可调用[notificationManager.openNotificationSettingsWithResult()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanageropennotificationsettingswithresult)拉起应用通知设置页面，用户完成设置后会返回更新后的NotificationSetting，根据bannerEnabled判断是否已开启横幅通知。
