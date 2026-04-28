---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-preferred-language
title: 应用偏好语言
breadcrumb: 指南 > 应用框架 > Localization Kit（本地化开发服务） > 应用国际化 > 语言与用户偏好 > 应用偏好语言
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6c705a813bad1b053d2d2a3d5cecb92e94d7427e2afbb355f9fb49fbbcb58357
---

## 功能介绍

对于多语言用户，通常会将系统语言设置为一种语言（如中文），将特定应用的语言设置为另一种语言（如英语）。应用界面加载资源时，显示应用设置的语言。开发过程中，设置应用国际化特性区域为偏好语言，确保应用界面的国际化特性和加载的资源一致。当前，应用仅支持设置一种语言。

## 开发步骤

接口具体使用方法和说明请参考[getAppPreferredLanguage](../harmonyos-references/js-apis-i18n.md#getapppreferredlanguage9)的API文档。示例代码如下：

1. 导入模块。

   ```
   1. import { i18n } from '@kit.LocalizationKit';
   2. import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   ```

   [LanguagePreferenceSetting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/LanguagePreferenceSetting.ets#L18-L21)
2. 使用场景。

* 需要获取应用偏好语言。

  ```
  1. let appPreferredLanguage = i18n.System.getAppPreferredLanguage(); // 获取应用偏好语言
  ```

  [LanguagePreferenceSetting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/LanguagePreferenceSetting.ets#L68-L70)
* 设置应用偏好语言。将应用偏好语言设置为目标语言后，应用界面会切换为目标语言。这仅影响应用本身，不影响系统语言设置。

  ```
  1. try {
  2. i18n.System.setAppPreferredLanguage('zh-Hans'); // 设置应用偏好语言为zh-Hans
  3. } catch (error) {
  4. let err: BusinessError = error as BusinessError;
  5. console.error(`call System.setAppPreferredLanguage failed, error code: ${err.code}, message: ${err.message}.`);
  6. }
  ```

  [LanguagePreferenceSetting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/LanguagePreferenceSetting.ets#L59-L66)
* 清除应用偏好语言。将应用偏好语言设置为“default”后，该应用的界面会跟随系统语言变化，该特性将在应用重新启动后生效。

  ```
  1. try {
  2. i18n.System.setAppPreferredLanguage('default'); // 清除应用偏好语言
  3. } catch (error) {
  4. let err: BusinessError = error as BusinessError;
  5. console.error(`call System.setAppPreferredLanguage failed, error code: ${err.code}, message: ${err.message}.`);
  6. }
  ```

  [LanguagePreferenceSetting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/LanguagePreferenceSetting.ets#L72-L80)
