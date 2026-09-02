---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-19
title: 如何判断应用启动是来自于Notification Kit拉起的
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 如何判断应用启动是来自于Notification Kit拉起的
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a965fdb1b5e997d549d5e20cb7c4c2f0cd198b8f17b17d52c9bc002988c04831
---

## 问题现象

希望在无需特殊设置uri的情况下，能够判断出这次启动是来自Notification Kit拉起的。

## 背景知识

* [LaunchParam](../harmonyos-references/js-apis-app-ability-abilityconstant.md#launchparam)：启动参数，主要包括Ability启动原因以及上次退出原因。
* [Params](../harmonyos-references/js-apis-app-ability-wantconstant.md#params):[Want.parameters](../harmonyos-references/js-apis-app-ability-want.md#want)字段常用的系统预置关键字。开发者可以通过这些预置关键字设置或获取应用跳转等场景中额外携带的参数信息。

## 解决方案

通过[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)处理通知跳转事件时，可使用[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)的[LaunchParam.launchReasonMessage](../harmonyos-references/js-apis-app-ability-abilityconstant.md#launchparam)字段是否为'ReasonMessage\_Notification'判断。

```ts
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  try {
    this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
  } catch (err) {
    hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
  }
  hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');

  if (launchParam.launchReasonMessage === 'ReasonMessage_Notification') {
    // 识别为被通知拉起
    console.info('被拉起原因：通知');
  }
}

onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  if (launchParam.launchReasonMessage === 'ReasonMessage_Notification') {
    // 识别为被通知拉起
    console.info('被拉起原因：通知');
  }
}
```

完整示例参考如下：

EntryAbility:

```ts
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');

    if (launchParam.launchReasonMessage === 'ReasonMessage_Notification') {
      // 识别为被通知拉起
      console.info('被拉起原因：通知');
    }
  }

  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    if (launchParam.launchReasonMessage === 'ReasonMessage_Notification') {
      // 识别为被通知拉起
      console.info('被拉起原因：通知');
    }
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

Index:

```ts
import { notificationManager } from '@kit.NotificationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common, wantAgent, WantAgent } from '@kit.AbilityKit';

const TAG: string = '[PublishOperation]';
const DOMAIN_NUMBER: number = 0xFF00;

@Entry
@Component
struct Index {
  private notificationId: number = 1;

  aboutToAppear() {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
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
      hilog.error(DOMAIN_NUMBER, TAG,
        `isNotificationEnabled fail, code is ${err.code}, message is ${err.message}`);
    });
  }

  async publishWantNotification(): Promise<void> {
    let wantAgentObj: WantAgent;
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      wants: [
        {
          bundleName: 'com.example.notificationtest', // 自己项目的包名
          abilityName: 'EntryAbility',
          parameters: {
            targetPage: 'Index' // 添加目标页面参数
          }
        }
      ],
      actionType: wantAgent.OperationType.START_ABILITY,
      requestCode: 0,
      wantAgentFlags: [wantAgent.WantAgentFlags.CONSTANT_FLAG]
    };
    wantAgent.getWantAgent(wantAgentInfo, (err: BusinessError, data: WantAgent) => {
      if (err) {
        hilog.error(DOMAIN_NUMBER, TAG, `Failed to get want agent. Code is ${err.code}, message is ${err.message}`);
        return;
      }
      hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in getting want agent.');
      wantAgentObj = data;

      // 构造NotificationRequest对象
      let notificationRequest: notificationManager.NotificationRequest = {
        id: this.notificationId,
        notificationSlotType: notificationManager.SlotType.SOCIAL_COMMUNICATION,
        content: {
          notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
          normal: {
            title: '新消息提醒',
            text: '您有一条消息',
            additionalText: '点击查看详情',
          },
        },
        wantAgent: wantAgentObj,
      };
      notificationManager.publish(notificationRequest, (err: BusinessError) => {
        if (err) {
          console.error(`NotificationPage err, code is：${err.code}, message is ${err.message}`);
          return;
        }
        console.info(`NotificationPage data success`);
        this.notificationId++;
      });
    });
  }

  build() {
    RelativeContainer() {
      Text('发送意图通知')
        .id('sendWantNotification')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.publishWantNotification();
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
