---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1480
title: promptAction.showToast在后台不显示
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > promptAction.showToast在后台不显示
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8b2a661c6bdf22842c50631375076ca046f5a5eccb1c17add6a724a534c1e20a
---

## 问题现象

APP进入后台时，希望能弹出Toast提示用户进入后台，但是Toast不显示。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/nhgU333oQryD5zhxSOzeNg/zh-cn_image_0000002658845071.png "点击放大")

## 背景知识

* [Toast](../harmonyos-guides/arkts-create-toast.md)：即时反馈（Toast）是一种临时性的消息提示框，用于向用户显示简短的操作反馈或状态信息。它通常在屏幕的底部或顶部短暂弹出，随后在一段时间后自动消失。即时反馈的主要目的是提供简洁、不打扰的信息反馈，避免干扰用户当前的操作流程。
* [Notification Kit](../harmonyos-guides/notification-overview.md)：Notification Kit（用户通知服务）为开发者提供本地通知发布通道，开发者可借助Notification Kit将应用产生的通知直接在客户端本地推送给用户，本地通知根据通知类型及发布场景会产生对应的铃声、震动、横幅、锁屏、息屏、通知栏提醒和显示。

## 解决方案

为了安全考虑，例如Toast恶意遮挡其他页面，Toast只能显示在当前的UI实例中，应用退出后，不会单独显示在桌面上。若是想在应用退出到后台时继续提醒用户，可以使用横幅通知功能。

* 在EntryAbility.ets文件中增加以下代码，在程序退至后台时会触发[onBackground](../harmonyos-guides/uiability-lifecycle.md#onbackground)回调，在此回调中弹出横幅提醒用户。

  ```ts
  import { notificationManager } from '@kit.NotificationKit';
  ```

  ```ts
  // 通知方法
  publishNotification() {
    let notificationRequest:
      // 描述通知的请求
      notificationManager.NotificationRequest = {
      // 通知ID
      id: 1,
      // 通知内容
      content: {
        notificationContentType:
        // 普通文本类型通知
        notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
        // 基本类型通知内容
        normal: {
          title: '应用名称',
          text: '应用在后台运行'
        },
      },
      notificationSlotType: notificationManager.SlotType.SOCIAL_COMMUNICATION,
    };
    // 发布通知
    notificationManager.publish(notificationRequest).then(() => {
      console.info('publish success');
    }).catch((err: Error) => {
      console.error(`publish failed,message is ${err}`);
    });
  }

  onBackground(): void {
    this.publishNotification();
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
  ```
* 应用页面按照正常业务逻辑写即可，以hello world工程为例。Index.ets：

  ```ts
  @Entry
  @Component
  struct Index {
    @State message: string = 'Hello World';

    build() {
      RelativeContainer() {
        Text(this.message)
          .id('HelloWorld')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            this.message = 'Welcome';
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

**说明** 

运行上述示例需要在通知设置里开启此应用通知开关。也可通过代码拉起弹窗请求用户授权，实现详细请参考[业务流程](../harmonyos-guides/notification-overview.md#业务流程)和[请求通知授权](../harmonyos-guides/notification-enable.md)

## 常见FAQ

Q：横幅通知可以提醒用户APP进入后台，是否有其他方案来实现？

A：可以使用[SoundPool](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#soundpool)播放自定义的提示音来提醒用户。这可以让用户听到明显的音频提示，知道应用已经转到后台。具体开发步骤及注意事项可以参考：[使用SoundPool播放短音频](../harmonyos-guides/using-soundpool-for-playback.md)。

## 总结

* Toast不支持在应用退至后台后，仍发送提示框消息。
* 退至后台时，消息可以通过Notification Kit在客户端本地推送给用户。
* 若应用退到后台或进程终止后，仍希望有一些提醒用户的定时类通知，可以使用[Background Tasks Kit](../harmonyos-guides/background-task-overview.md)进行消息创建。
* 远程推送消息至本地请使用[Push Kit](../harmonyos-guides/push-kit-introduction.md)。
