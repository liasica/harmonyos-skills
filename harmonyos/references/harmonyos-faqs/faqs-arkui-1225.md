---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1225
title: 权限申请弹窗与自定义弹窗冲突问题及解决方案
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 权限申请弹窗与自定义弹窗冲突问题及解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:42d54a7d7e64366a5e79dab1049a4dbc9bdd3cbadc8c8cfa49ad4811699c70f0
---

## 问题现象

首次打开APP时，通知权限申请弹窗与自定义弹窗冲突，只弹出了通知权限申请弹窗，而自定义弹窗未弹出。问题代码如下：

```ts
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { notificationManager } from '@kit.NotificationKit';

@CustomDialog
struct CustomDialogExample {
  controller: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample({}),
  })

  build() {
    Column() {
      Text('我是内容')
        .fontSize(20)
    }.height(60).justifyContent(FlexAlign.Center)
  }
}

@Entry
@Component
struct Index {
  private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample(),
  })

  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const DOMAIN_NUMBER: number = 0xFF00;
    const TAG: string = '[PublishOperation]';
    notificationManager.isNotificationEnabled().then((data: boolean) => {
      hilog.info(DOMAIN_NUMBER, TAG, `isNotificationEnabled success, data: ${data}`);
      if(!data){
        notificationManager.requestEnableNotification(context).then(() => {
          this.dialogController.open()
          hilog.info(DOMAIN_NUMBER, TAG, `[ANS] requestEnableNotification success`);
        }).catch((err : BusinessError) => {
          if(1600004 == err.code){
            hilog.error(DOMAIN_NUMBER, TAG, `[ANS] requestEnableNotification refused, code is ${err.code}, message is ${err.message}`);
          } else {
            hilog.error(DOMAIN_NUMBER, TAG, `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
          }
        });
      }
    }).catch((err : BusinessError) => {
      hilog.error(DOMAIN_NUMBER, TAG, `isNotificationEnabled fail, code is ${err.code}, message is ${err.message}`);
    });
  }

  build() {
    RelativeContainer() {
      Text('Hello World')
        .fontSize($r('app.float.page_text_font_size'))
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        });
    }
    .height('100%')
    .width('100%')
  }
}
```

问题效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/2fhCOoUzTQ29jz_AmreSZw/zh-cn_image_0000002628594026.png "点击放大")

## 背景知识

[CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)用于创建自定义弹窗，允许用户灵活地设置弹窗的样式，布局和交互行为。[NotificationManager模块](../harmonyos-references/js-apis-notificationmanager.md)提供通知管理的能力，在发布通知前需调用[requestEnableNotification()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10-1)方法，让用户选择是否允许发送通知。

## 解决方案

由于系统级弹窗的模态化窗口级别较高，不可与CustomDialog或openCustomDialog同时弹出，因此禁止直接弹出子窗口或其他弹窗，必须按照先后顺序展示。

若使用了系统级别弹窗，不能在requestEnableNotification接口回调中进行调用CustomDialog或openCustomDialog，打开自定义弹窗的代码需要在requestEnableNotification回调结束后调用。代码修复如下：

```ts
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { notificationManager } from '@kit.NotificationKit';

@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;

  build() {
    Column() {
      Text('这是自定义弹窗')
        .fontSize(30)
        .height(100);
      Button('点我关闭弹窗')
        .onClick(() => {
          if (this.controller != undefined) {
            this.controller.close();
          }
        })
        .margin(20);
    };
  }
}

@Entry
@Component
struct Index {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample(),
    backgroundColor: Color.White,
    backgroundBlurStyle: BlurStyle.Thin,

  });

  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const DOMAIN_NUMBER: number = 0xFF00;
    const TAG: string = '[PublishOperation]';
    notificationManager.isNotificationEnabled().then((data: boolean) => {
      hilog.info(DOMAIN_NUMBER, TAG, `isNotificationEnabled success, data: ${data}`);
      if (!data) {
        notificationManager.requestEnableNotification(context).then(() => {
          hilog.info(DOMAIN_NUMBER, TAG, `[ANS] requestEnableNotification success`);
        }).catch((err: BusinessError) => {
          if (1600004 == err.code) {
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
    // 系统通知授权后，弹窗
    this.dialogController.open();
  }

  build() {
    RelativeContainer() {
      Text('Hello World')
        .fontSize($r('app.float.page_text_font_size'))
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/8HZRfdYUSRyOKV7JsQL52w/zh-cn_image_0000002628753922.png "点击放大")

## 常见FAQ

Q：点击Web内组件同时弹出alert弹窗和系统弹窗，拉起alert弹窗时，Web进程会阻塞等待应用回复如何规避？

A：可以给[AlertDialog](../harmonyos-references/ts-methods-alert-dialog-box.md#alertdialogparam对象说明)设置LevelMode属性（弹窗显示层级模式），设置[LevelMode](../harmonyos-references/js-apis-promptaction.md#levelmode15)：LevelMode.EMBEDDED，会将分享弹窗和alert弹窗都显示出来，也不会卡死。
