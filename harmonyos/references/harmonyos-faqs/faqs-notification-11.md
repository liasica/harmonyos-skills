---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-11
title: 通知消息的角标信息显示不正确
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 通知消息的角标信息显示不正确
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f5fe274d7a311c82c1aa1209904872f01d7d0873482f097e2ffdce1186990c5c
---

## 问题现象

角标消息的数字不会随新增消息或阅读通知进行增减。

## 背景知识

* [通知角标](../harmonyos-guides/notification-badge.md)：针对未读的通知，系统提供了角标设置接口，将未读通知个数显示在桌面图标的右上角角标上。通知增加时，角标上显示的未读通知个数需要增加。通知被查看后，角标上显示的未读通知个数需要减少，没有未读通知时，不显示角标。
* 增加角标数，支持如下两种方法：
  + 发布通知时，在[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md#notificationrequest-1)的badgeNumber字段里携带，桌面收到通知后，在原角标数上累加、呈现。
  + 调用接口[setBadgeNumber](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagersetbadgenumber10)设置，桌面按设置的角标数呈现。
* 减少角标数，目前仅支持通过setBadgeNumber()设置。
* [请求通知权限](../harmonyos-guides/notification-enable.md)：应用需要获取用户授权才能发送通知。在通知发布前调用[requestEnableNotification()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10-1)方法，弹窗让用户选择是否允许发送通知，后续再次调用requestEnableNotification()方法时，则不再弹窗。
* 关键日志：badgeNumber，角标通知数量。

  | 日志 | 说明 |
  | --- | --- |
  | badgeNumber | 角标通知数量 |
  | requestEnableNotification错误码 | 1600004，拒绝授权 |

## 问题定位

* 查看Hilog日志判断应用是否已申请通知权限和具备角标权限，通过关键词“Ans”过滤日志：

  ```txt
  02-10 19:09:48.901   52431-65135   C01203/com.example.harmonyos/Ans  cc.tomato...r.huawei  I     setBadge number:12
  02-10 19:09:48.901   3716-60153    C01203/com.ohos.sceneboard/Ans  com.ohos.sceneboard   I     BadgeChanged bundle:com.example.harmonyos,uid:20020206,badgeNum:12
  02-10 19:09:48.902   3716-15393    C01203/com.ohos.sceneboard/Ans  com.ohos.sceneboard   I     BadgeChanged bundle:com.example.harmonyos,uid:20020206,badgeNum:12
  02-10 19:09:48.902   54255-64318   C01203/commonUI/Ans             commonUI              I     BadgeChanged bundle:com.example.harmonyos,uid:20020206,badgeNum:12
  02-10 19:09:48.904   54255-65138   C01203/commonUI/Ans             commonUI              I     get badgeEnabled bundle:com.example.harmonyos,uid:20020206,code:0,enabled:0
  02-10 19:09:48.904   54255-65139   C01203/commonUI/Ans             commonUI              I     isSmartReminder code=0,status=2
  02-10 19:09:48.904   54255-64951   C01203/commonUI/Ans             commonUI              I     isNotificationEnabled bundle:com.example.harmonyos,uid:20020206,code=0,allowed=1
  ```

  1. “get badgeEnabled bundle:com.example.xxx,uid:xxx,code:0,enabled:0”，enabled值为桌面角标权限开关，0表示桌面角标权限未打开，1表示桌面角标权限已打开；
  2. “isNotificationEnabled bundle:com.example.xxx,uid:xxx,code=0,allowed=1”，allowed值为通知权限开关，1表示允许通知，0表示不允许通知。
* 查看Hilog日志badgeNumber关键字，如果不存在对应关键字或者badgeNumber不会跟随消息数量增加减少，判断应用消息角标通知功能未实现或实现逻辑异常。

## 分析结论

* 应用未申请请求通知权限，参考修改建议一修改。
* 应用消息角标通知功能未实现或实现逻辑异常，参考修改建议二修改。

## 修改建议

* 修改建议一：使用[notificationManager.requestEnableNotification()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10-1)申请请求通知权限。在用户拒绝的情况可以使用[notificationManager.openNotificationSettings](../harmonyos-references/js-apis-notificationmanager.md#notificationmanageropennotificationsettings13)拉起通知管理半模态弹窗，向用户再次申请通知授权。
* 修改建议二：使用[notificationManager.setBadgeNumber()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagersetbadgenumber10-1)方法实现消息角标数修改功能。

  示例代码如下：

  ```ts
  import { notificationManager } from '@kit.NotificationKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { common } from '@kit.AbilityKit';

  const TAG: string = '[PublishOperation]';
  const DOMAIN_NUMBER: number = 0xFF00;

  @Entry
  @Component
  struct Index {
    badgeNumber = 10;

    // step1:申请通知权限
    aboutToAppear(): void {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      notificationManager.isNotificationEnabled().then((data: boolean) => {
        hilog.info(DOMAIN_NUMBER, TAG, "isNotificationEnabled success, data: " + JSON.stringify(data));
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
    }

    build() {
      Column({ space: 20 }) {
        // step2-1:增加消息数
        Button('增加一条消息')
          .type(ButtonType.ROUNDED_RECTANGLE)
          .width(300)
          .backgroundColor('#0a59f7')
          .onClick(() => {
            try {
              let setBadgeNumberCallback = (err: BusinessError): void => {
                if (err) {
                  hilog.error(DOMAIN_NUMBER, TAG,
                    `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
                  return;
                }
              };
              this.badgeNumber += 1;
              notificationManager.setBadgeNumber(this.badgeNumber, setBadgeNumberCallback);
            } catch (err) {
            }
          });

        // step2-1:减少消息数
        Button('减少一条消息')
          .width(300)
          .type(ButtonType.ROUNDED_RECTANGLE)
          .backgroundColor('#0a59f7')
          .onClick(() => {
            console.info(`Succeeded in clicking the 'Back' button.`);
            try {
              let setBadgeNumberCallback = (err: BusinessError): void => {
                if (err) {
                  hilog.error(DOMAIN_NUMBER, TAG,
                    `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
                  return;
                }
              };
              this.badgeNumber = this.badgeNumber - 1;
              notificationManager.setBadgeNumber(this.badgeNumber, setBadgeNumberCallback);
            } catch (err) {
            }
          });
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center);
    }
  }
  ```
