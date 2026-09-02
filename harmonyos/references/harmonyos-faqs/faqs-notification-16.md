---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-16
title: 如何发布本地消息到通知中心
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 如何发布本地消息到通知中心
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ed8e7c894268883ccccfbeac294a125ae25c37462c9bae6aee1df2e11d79a19b
---

## 问题现象

1. HarmonyOS有没有类似其他平台的通知中心（NSNotificationCenter）的能力？
2. 如何实现应用本地发送一条消息到通知中心？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/yBSBfi46QryUiTbfMvE38Q/zh-cn_image_0000002658794001.gif "点击放大")

## 背景知识

[Notification Kit（用户通知服务）](../harmonyos-guides/notification-overview.md)为开发者提供本地通知发布通道，开发者可借助Notification Kit将应用产生的通知直接在客户端本地推送给用户，本地通知根据通知类型及发布场景会产生对应的铃声、震动、横幅、锁屏、息屏、通知栏提醒和显示。

## 解决方案

1. HarmonyOS提供了[Notification Kit](../harmonyos-references/notification-api.md)，为开发者提供本地通知发布通道。
2. 本地发送消息到通知中心可以参考如下示例代码：

   ```ts
   import { notificationManager } from '@kit.NotificationKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';
   import { PromptAction } from '@kit.ArkUI';

   const TAG: string = '[PublishOperation]';
   const DOMAIN_NUMBER: number = 0xFF00;

   @Entry
   @Component
   struct NotificationPage {
     uiContext: UIContext = this.getUIContext();
     promptAction: PromptAction = this.uiContext.getPromptAction();

     // 获取用户授权
     requestForNotification() {
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       notificationManager.isNotificationEnabled().then((data: boolean) => {
         console.info(`${DOMAIN_NUMBER}, ${TAG}, isNotificationEnabled success, data: ${data}`);
         if (!data) {
           notificationManager.requestEnableNotification(context).then(() => {
             this.promptAction.openToast({
               message: '请求通知授权成功',
               duration: 2000,
             });
             console.info(`${DOMAIN_NUMBER}, ${TAG}, [ANS] requestEnableNotification success`);
           }).catch((err: BusinessError) => {
             if (1600004 == err.code) {
               this.promptAction.openToast({
                 message: '请求通知授权失败',
                 duration: 2000,
               });
               console.error(`${DOMAIN_NUMBER}, ${TAG},
                 [ANS] requestEnableNotification refused, code is ${err.code}, message is ${err.message}`);
             } else {
               console.error(`${DOMAIN_NUMBER}, ${TAG},
                 [ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
             }
           });
         }
       }).catch((err: BusinessError) => {
         console.error(`${DOMAIN_NUMBER}, ${TAG}, isNotificationEnabled fail, code is ${err.code}, message is ${err.message}`);
       });
     }

     // 构造NotificationRequest对象，发布通知
     notification(title: string, message: string) {
       let notificationRequest: notificationManager.NotificationRequest = {
         id: 1,
         content: {
           notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT, // 普通文本类型通知
           normal: {
             title: title,
             text: message,
             additionalText: 'test_additionalText',
           }
         }
       };
       notificationManager.publish(notificationRequest, (err: BusinessError) => {
         if (err) {
           console.error(`${DOMAIN_NUMBER}, ${TAG}, Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
           this.promptAction.openToast({
             message: '请求通知授权成功',
             duration: 2000,
           });
           return;
         } else {
           console.info(`${DOMAIN_NUMBER}, ${TAG}, Succeeded in publishing notification.`);
           this.promptAction.openToast({
             message: '发布通知成功',
             duration: 2000,
           });
         }
       });
     }

     // 获取二次授权
     openNotification(){
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       notificationManager.isNotificationEnabled().then((data: boolean) => {
         console.info(`${DOMAIN_NUMBER}, ${TAG}, "isNotificationEnabled success, data:${data} `);
         if(!data){
           notificationManager.openNotificationSettings(context).then(() => {
             console.info(`${DOMAIN_NUMBER}, ${TAG}, [ANS] openNotificationSettings success`);
           }).catch((err: BusinessError) => {
             console.error(`${DOMAIN_NUMBER}, ${TAG}, [ANS] openNotificationSettings failed, code is ${err.code}, message is ${err.message}`);
           });
         }
       }).catch((err: BusinessError) => {
         console.error(`${DOMAIN_NUMBER}, ${TAG}, isNotificationEnabled fail, code is ${err.code}, message is ${err.message}`);
       });
     }

     aboutToAppear(): void {
       this.requestForNotification();
       this.openNotification();
     }

     build() {
       Column() {
         Button('发布通知').onClick(() => {
           let title = '这是一个标题';
           let message = '这是一条通知';
           this.notification(title, message);
         });
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center);
     }
   }
   ```

## 常见FAQ

Q：APP退至后台到被挂起的这段时间内，是否仍然可以发起本地通知？

A：APP被退至后台，仍有若干时间才会被系统挂起（不可靠，3-10s）；在被挂起前，APP仍然可以发送本地通知，但依赖这种机制不可靠，建议在被退至后台时就切换到Push kit进行通知的模式。

## 总结

* 注意Notification Kit仅适用于应用处于前台运行时向用户发布通知，当应用转为后台时，本地通知发布通道关闭，开发者需要接入[Push Kit](../harmonyos-guides/push-kit-introduction.md)进行云侧离线通知的发布。
* 在长时任务保活期间，可以在后台使用Notification Kit进行通知。
