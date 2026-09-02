---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-12
title: 打开应用弹出的通知授权弹窗来不及点就消失了
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 打开应用弹出的通知授权弹窗来不及点就消失了
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d241155113edabe7a7c5626645ce050c5a3fc4a22b7b56a78a11c7893b88b557
---

## 问题现象

下载应用后首次打开，会弹出通知授权弹窗，但是还没来得及点击“允许”或“不允许”，弹窗就自动消失了。

## 背景知识

* [notificationManager.requestEnableNotification](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10-1)：应用需要获取用户授权才能发送通知。在通知发布前调用该接口，可以拉起通知授权弹窗，让用户选择是否允许发送通知。
* [层级页面](../harmonyos-guides/arkts-common-events-focus-event.md#基础概念)：层级页面是焦点框架中特定容器组件的统称，涵盖Page、Dialog、SheetPage、ModalPage、Menu、Popup、NavBar、NavDestination等。在一个应用程序中，任何时候都至少存在一个层级页面组件，并且该组件会持有当前焦点。当该层级页面关闭或不再可见时，焦点会自动转移到下一个可用的层级页面组件上，确保用户交互的连贯性和一致性。

## 问题定位

1. 首先排查调用通知授权弹窗接口时机是否正确。

   requestEnableNotification应当在应用界面加载完成后（即调用loadContent成功），方可调用该接口。通过搜索"onCreate"、"onWindowStageCreate"、"onForeground"、"loadContent"、"requestEnableNotification"关键词查看日志，发现调用通知授权弹窗是在loadContent之后调用的。

   ```txt
   11-14 17:00:36.335 16418 16418 I A00000/com.hm.example/testTag: Ability onCreate
   11-14 17:00:36.347 16418 16418 I A00000/com.hm.example/testTag: Ability onWindowStageCreate
   11-14 17:00:36.348 16418 16418 I C04200/com.hm.example/JsWindowStage: (87)LoadContent: [NAPI]
   11-14 17:00:36.353 16418 16418 I A00000/com.hm.example/testTag: Ability onForeground
   11-14 17:00:36.414 16418 16418 I C01203/com.hm.example/Ans: [napi_enable_notification.cpp(NapiRequestEnableNotification:255)]
   ```
2. 然后可以从组件获取焦点和失去焦点的思路继续排查弹窗自动关闭的原因。

   通过搜索"Focus"、"ModalPage"关键词查看日志，发现通知授权弹窗"ModalPage/11"是在应用启动页"page/2"之后请求焦点并获取焦点的，这一点可以从"page/2 lost focus"和"Request focus on focus view: ModalPage/11"可以看出。

   然后从"Request focus on focus view: page/13"看出紧接着页面"page/13"也发起了请求焦点并获取焦点，导致了"ModalPage/11 close"、"ModalPage/11 lost focus"。

   ```txt
   11-14 17:00:36.395 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Focus view: page/2 show
   11-14 17:00:36.406 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Request focus on focus view: page/2.
   11-14 17:00:36.406 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Focus view has no default focus.
   11-14 17:00:36.421 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Focus view: ModalPage/11 show
   11-14 17:00:36.421 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Focus view: page/2 lost focus
   11-14 17:00:36.421 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Request focus on focus view: ModalPage/11.
   11-14 17:00:36.421 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Focus view has no default focus.
   11-14 17:00:37.296 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Focus view: ModalPage/11 close
   11-14 17:00:37.296 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Focus view: ModalPage/11 lost focus
   11-14 17:00:37.330 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Focus view: page/2 hide
   11-14 17:00:37.330 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Focus view: page/2 lost focus
   11-14 17:00:37.331 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Focus view: page/13 show
   11-14 17:00:37.331 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Focus view: page/2 hide
   11-14 17:00:37.331 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Focus view: page/2 lost focus
   11-14 17:00:37.331 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Focus view: page/2 close
   11-14 17:00:37.331 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Focus view: page/2 lost focus
   11-14 17:00:37.333 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Request focus on focus view: page/13.
   11-14 17:00:37.333 16418 16418 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Focus view has no default focus.
   ```
3. 尝试基于这个思路进行问题复现，发现页面跳转确实会让授权弹窗失去焦点并自动消失。

   ```ts
   // EntryAbility.ets
   onWindowStageCreate(windowStage: window.WindowStage): void {
     windowStage.loadContent('pages/PageOne', (err) => {
       if (err.code) {
         console.error(`Failed to load the content, code is ${err.code}.`);
         return;
       }
       // 拉起通知授权弹窗
       notificationManager.requestEnableNotification(this.context).then(() => {
         console.info('requestEnableNotification success');
       }).catch((err: BusinessError) => {
         console.error(`requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
       });
       console.info('Succeeded in loading the content.');
     });
   }

   // PageOne.ets
   aboutToAppear() {
     setTimeout(() => {
       router.pushUrl({ url: 'pages/PageTwo' });
     }, 500)
   }
   ```

## 分析结论

由于在应用启动到跳转到首页的过程中，申请通知授权弹窗时机和页面跳转产生冲突，页面多次跳转使出现的弹窗因失去焦点而消失关闭，导致了弹窗出现后很快自动消失的问题。

## 修改建议

* 如果应用在启动后会涉及多个页面的自动跳转，建议不要在onWindowStageCreate中拉起通知授权弹窗，而是在最后一个不会再继续往下跳转的页面中拉起弹窗。
* 或者在loadContent加载的页面中，调用requestEnableNotification接口，然后在回调返回结果中控制是否授权的页面跳转逻辑。

```ts
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { notificationManager } from '@kit.NotificationKit';

@Entry
@Component
struct PageOne {
  @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

  aboutToAppear() {
    // 拉起通知授权弹窗
    notificationManager.requestEnableNotification(this.context).then(() => {
      console.info('requestEnableNotification success');
      this.pageInfos.pushPathByName('PageTwo', null);
    }).catch((err: BusinessError) => {
      console.error(`requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
    });
  }

  @Builder
  pageMap(name: string) {
    if (name === 'PageTwo') {
      PageTwo();
    }
  }

  build() {
    Column() {
      Navigation(this.pageInfos) {
        Text('PageOne')
          .fontSize(30)
          .margin(30);
      }
      .navDestination(this.pageMap);
    }.width('100%');
  }
}

@Component
struct PageTwo {
  @Consume('pageInfos') pageInfos: NavPathStack;

  build() {
    Column() {
      NavDestination() {
        Text('PageTwo')
          .fontSize(30)
          .margin(30);
      };
    }.width('100%');
  }
}
```
