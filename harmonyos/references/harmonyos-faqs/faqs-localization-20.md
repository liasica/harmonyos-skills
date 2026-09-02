---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-20
title: 如何根据系统语言动态切换字体
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 如何根据系统语言动态切换字体
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:db6d0aeaff1fdc399c00387f4c285aabf1403b25ac98fc7b9d41276ee0d3757b
---

## 问题现象

在设置-系统-语言和地区中切换字体以后，能否让应用内字体也跟随切换？比如当系统语言设置成中文时，使用默认字体'HarmonyOS Sans'，当系统语言设置成英文时，使用自定义字体。

## 背景知识

* [系统语言与区域](../harmonyos-guides/i18n-system-language-region.md)：在设置的“语言和地区”中可以切换系统语言。
* [fontFamily](../harmonyos-references/ts-basic-components-text.md#fontfamily)：可以用于设置字体族。
* [registerFont](../harmonyos-references/arkts-apis-uicontext-font.md#registerfont)：在字体管理中注册自定义字体。

## 解决方案

定义状态变量fontFamily并绑定在Text组件上，注册系统语言变化监听，当系统语言变化时修改fontFamily的值，即可实现根据系统语言动态切换字体，实现步骤如下：

1. 注册自定义字体。

   ```ts
   let font: Font = this.getUIContext().getFont();
   font.registerFont({
     familyName: 'customFont', // 注册的字体名称
     familySrc: $rawfile('customFont.ttf') // rawfile目录下的自定义字体文件
   });
   ```
2. 注册系统语言变化监听，在收到监听后根据语言类型进行字体族切换。

   ```ts
   // 通过监听公共事件COMMON_EVENT_LOCALE_CHANGED可以感知系统语言、系统地区或系统区域变化
   let subscriber: commonEventManager.CommonEventSubscriber;
   let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
     events: [commonEventManager.Support.COMMON_EVENT_LOCALE_CHANGED]
   };
   commonEventManager.createSubscriber(subscribeInfo)
     .then((commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
       console.info('CreateSubscriber');
       subscriber = commonEventSubscriber;
       commonEventManager.subscribe(subscriber, (err) => {
         if (err) {
           console.error(`Failed to subscribe common event. error code: ${err.code}, message: ${err.message}.`);
           return;
         }
         let systemLanguage: string = i18n.System.getSystemLanguage(); // systemLanguage为当前系统语言
         if (systemLanguage === 'zh-Hans') {
           this.fontFamily = 'HarmonyOS Sans';
         } else {
           this.fontFamily = 'customFont';
         }
       });
     })
     .catch((err: BusinessError) => {
       console.error(`CreateSubscriber failed, code is ${err.code}, message is ${err.message}`);
     });
   ```

完整示例代码如下：

```ts
import { Font } from '@kit.ArkUI';
import { i18n } from '@kit.LocalizationKit';
import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';

@Entry
@Component
struct ChangeFontFamilyBySystemLanguage {
  @State fontFamily: string = 'HarmonyOS Sans';

  aboutToAppear(): void {
    let font: Font = this.getUIContext().getFont();
    font.registerFont({
      familyName: 'customFont', // 注册的字体名称
      familySrc: $rawfile('customFont.ttf') // rawfile目录下的自定义字体文件
    });
    // 通过监听公共事件COMMON_EVENT_LOCALE_CHANGED可以感知系统语言、系统地区或系统区域变化
    let subscriber: commonEventManager.CommonEventSubscriber;
    let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
      events: [commonEventManager.Support.COMMON_EVENT_LOCALE_CHANGED]
    };
    commonEventManager.createSubscriber(subscribeInfo)
      .then((commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
        console.info('CreateSubscriber');
        subscriber = commonEventSubscriber;
        commonEventManager.subscribe(subscriber, (err) => {
          if (err) {
            console.error(`Failed to subscribe common event. error code: ${err.code}, message: ${err.message}.`);
            return;
          }
          let systemLanguage: string = i18n.System.getSystemLanguage(); // systemLanguage为当前系统语言
          if (systemLanguage === 'zh-Hans') {
            this.fontFamily = 'HarmonyOS Sans';
          } else {
            this.fontFamily = 'customFont';
          }
        });
      })
      .catch((err: BusinessError) => {
        console.error(`CreateSubscriber failed, code is ${err.code}, message is ${err.message}`);
      });
  }

  build() {
    Column() {
      Row() {
        Text('Hello World')
          .fontSize(50)
          .fontFamily(this.fontFamily);
      }.width('100%').justifyContent(FlexAlign.Center);
    };
  }
}
```
