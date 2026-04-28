---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-user-preferences
title: 用户偏好
breadcrumb: 指南 > 应用框架 > Localization Kit（本地化开发服务） > 应用国际化 > 语言与用户偏好 > 用户偏好
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0d5d149769ce76a15eba6d89d729770a51b69b8e7a0b9e7fefd29836fae21ec9
---

## 使用场景

除区域设置和应用偏好语言设置外，系统还可以设置用户偏好，当前支持本地数字和时制两种偏好。用户偏好设置会保存到系统区域及应用偏好语言中，最终体现在用户界面的国际化特性上。

## 开发步骤

接口具体使用方法和说明请参考[System](../harmonyos-references/js-apis-i18n.md#system9)的API接口文档。

1. 导入模块。

   ```
   1. import { i18n } from '@kit.LocalizationKit';
   2. import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   ```

   [LanguagePreferenceSetting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/LanguagePreferenceSetting.ets#L18-L21)
2. 使用场景。

* 获取用户偏好。

  ```
  1. // 判断系统当前是否使用本地数字
  2. let usingLocalDigit: boolean = i18n.System.getUsingLocalDigit();

  4. // 判断系统当前是否使用24小时制
  5. let is24HourClock: boolean = i18n.System.is24HourClock();

  7. // 通过监听公共事件COMMON_EVENT_TIME_CHANGED可以感知系统时制变化
  8. let timeSubscriber: commonEventManager.CommonEventSubscriber; // 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
  9. let timeSubscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  10. events: [commonEventManager.Support.COMMON_EVENT_TIME_CHANGED]
  11. };
  12. // 创建订阅者
  13. commonEventManager.createSubscriber(timeSubscribeInfo)
  14. .then((commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
  15. console.info('CreateSubscriber');
  16. timeSubscriber = commonEventSubscriber;
  17. commonEventManager.subscribe(timeSubscriber, (err, data) => {
  18. if (err) {
  19. console.error(`Failed to subscribe common event. error code: ${err.code}, message: ${err.message}.`);
  20. return;
  21. }
  22. // 用于区分系统时间和系统时制变化
  23. if (data.data != undefined && data.data == '24HourChange') {
  24. console.info('The subscribed event has occurred.'); // 系统时制变化时执行
  25. }
  26. })
  27. })
  28. .catch((err: BusinessError) => {
  29. console.error(`CreateSubscriber failed, code is ${err.code}, message is ${err.message}`);
  30. });
  ```

  [LanguagePreferenceSetting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/LanguagePreferenceSetting.ets#L82-L113)
