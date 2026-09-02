---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-user-preferences
title: 用户偏好
breadcrumb: 指南 > 应用框架 > Localization Kit（本地化开发服务） > 应用国际化 > 语言与用户偏好 > 用户偏好
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7419f03ccacbef1523c1be7eadb56747b61ae3d75fe163065c301eb9e985ae5e
---

## 使用场景

除区域设置和应用偏好语言设置外，系统还可以设置用户偏好，当前支持本地数字和时制两种偏好。用户偏好设置会保存到系统区域及应用偏好语言中，最终体现在用户界面的国际化特性上。

## 开发步骤

接口具体使用方法和说明请参考[System](../harmonyos-references/js-apis-i18n.md#system9)的API接口文档。

1. 导入模块。

   ```typescript
   import { i18n } from '@kit.LocalizationKit';
   import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   ```
2. 使用场景。

* 获取用户偏好。

  ```typescript
  // 判断系统当前是否使用本地数字
  let usingLocalDigit: boolean = i18n.System.getUsingLocalDigit();

  // 判断系统当前是否使用24小时制
  let is24HourClock: boolean = i18n.System.is24HourClock();

  // 通过监听公共事件COMMON_EVENT_TIME_CHANGED可以感知系统时制变化
  let timeSubscriber: commonEventManager.CommonEventSubscriber; // 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
  let timeSubscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
    events: [commonEventManager.Support.COMMON_EVENT_TIME_CHANGED]
  };
  // 创建订阅者
  commonEventManager.createSubscriber(timeSubscribeInfo)
    .then((commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
      console.info('CreateSubscriber');
      timeSubscriber = commonEventSubscriber;
      commonEventManager.subscribe(timeSubscriber, (err, data) => {
        if (err) {
          console.error(`Failed to subscribe common event. error code: ${err.code}, message: ${err.message}.`);
          return;
        }
        // 用于区分系统时间和系统时制变化
        if (data.data != undefined && data.data == '24HourChange') {
          console.info('The subscribed event has occurred.'); // 系统时制变化时执行
        }
      })
    })
    .catch((err: BusinessError) => {
      console.error(`CreateSubscriber failed, code is ${err.code}, message is ${err.message}`);
    });
  ```
