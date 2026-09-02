---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-preferred-language
title: 应用偏好语言
breadcrumb: 指南 > 应用框架 > Localization Kit（本地化开发服务） > 应用国际化 > 语言与用户偏好 > 应用偏好语言
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a7cda6bb1c4dade3e24a4f36e3ae04353b3ea16484dd0ae10d2a533303577b5b
---

## 功能介绍

对于多语言用户，通常会将系统语言设置为一种语言（如中文），将特定应用的语言设置为另一种语言（如英语）。应用界面加载资源时，显示应用设置的语言。开发过程中，设置应用国际化特性区域为偏好语言，确保应用界面的国际化特性和加载的资源一致。当前，应用仅支持设置一种语言。

## 开发步骤

接口具体使用方法和说明请参考[getAppPreferredLanguage](../harmonyos-references/js-apis-i18n.md#getapppreferredlanguage9)的API文档。示例代码如下：

1. 导入模块。

   ```typescript
   import { i18n } from '@kit.LocalizationKit';
   import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   ```
2. 使用场景。

* 需要获取应用偏好语言。

  ```typescript
  let appPreferredLanguage = i18n.System.getAppPreferredLanguage(); // 获取应用偏好语言
  ```
* 设置应用偏好语言。将应用偏好语言设置为目标语言后，应用界面会切换为目标语言。这仅影响应用本身，不影响系统语言设置。

  ```typescript
  try {
    i18n.System.setAppPreferredLanguage('zh-Hans'); // 设置应用偏好语言为zh-Hans
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`call System.setAppPreferredLanguage failed, error code: ${err.code}, message: ${err.message}.`);
  }
  ```
* 清除应用偏好语言。将应用偏好语言设置为“default”后，该应用的界面会跟随系统语言变化，该特性将在应用重新启动后生效。

  ```typescript
  try {
    i18n.System.setAppPreferredLanguage('default'); // 清除应用偏好语言
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`call System.setAppPreferredLanguage failed, error code: ${err.code}, message: ${err.message}.`);
  }
  ```
