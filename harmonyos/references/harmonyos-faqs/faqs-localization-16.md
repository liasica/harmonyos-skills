---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-16
title: 如何定位单独设置APP偏好语言失败的问题
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 如何定位单独设置APP偏好语言失败的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b836dbee1357ef2d496635568317c58e8debc67765583ace5ad21e6d13419e27
---

## 问题现象

单独设置APP偏好语言失败，APP语言必须和系统语言保持一致。

* 预期效果：应用可以根据用户的选择，自行变换应用内的语言。
* 实际效果：应用内语言只能与系统的偏好语言保持一致。

问题代码示例参考如下：

```ts
import I18n from '@ohos.i18n';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  I18n.System.setAppPreferredLanguage('en-Latn-US'); // 设置应用当前的偏好语言为'US'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.setAppPreferredLanguage failed, error code: ${err.code}, message: ${err.message}.`);
}

@Component
@Entry
struct Index {
  build() {
    Column() {
      Text($r('app.string.module_desc'));
    };
  }
}
```

## 背景知识

* [@ohos.i18n(国际化-I18n)](../harmonyos-references/js-apis-i18n.md)：该模块提供系统相关的或者增强的国际化能力，包括区域管理、电话号码处理、日历等。
* [setAppPreferredLanguage](../harmonyos-references/js-apis-i18n.md#setapppreferredlanguage11)：设置应用偏好语言。设置后，应用将优先加载应用偏好语言对应的资源。设置偏好语言为'default'后，应用语言将跟随系统语言，应用冷启动生效。

## 问题定位

1. 排查资源文件中语言信息是否配置正确。
2. 排查切换语言过程中，语言状态status是否正确。

## 分析结论

通过setAppPreferredLanguage接口实现单独设置应用偏好语言。主要实现思路有以下三步：

1. setAppPreferredLanguage接口需要从资源文件中获取语言信息，资源文件中需要提前声明准备提供给用户的不同语言。
2. 在用户界面提供可选语言的下拉框或按钮等交互组件，让用户进行自主选择。
3. 记录用户的选择，并设置进偏好语言中。

## 修改建议

根据上述思路，下文中将以“通过点击按钮，自主切换中英文”进行说明：

1. 在资源文件中添加中/英文的value值。

   默认语言（base文件）以及中文语言（zh\_CN文件）写的是中文，英文语言（en\_US文件）写的是英文。因此在偏好语言为英文时，显示en\_US文件的内容；偏好语言为中文时，显示zh\_CN文件的内容；偏好语言为其他语言时，显示base文件的内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/1XDrbTGBSay6W35vK47mPw/zh-cn_image_0000002628663108.png)

   * base目录中的string.json如下：

     ```json
     {
       "string": [
         {
           "name": "module_desc",
           "value": "模块描述"
         },
         {
           "name": "language_button",
           "value": "改变语言"
         },
         {
           "name": "EntryAbility_desc",
           "value": "description"
         },
         {
           "name": "EntryAbility_label",
           "value": "label"
         }
       ]
     }
     ```
   * en\_US目录中的string.json如下：

     ```json
     {
       "string": [
         {
           "name": "module_desc",
           "value": "module description"
         },
         {
           "name": "language_button",
           "value": "Change Language"
         }
       ]
     }
     ```
   * zh\_CN目录中的string.json如下：

     ```json
     {
       "string": [
         {
           "name": "module_desc",
           "value": "模块描述"
         },
         {
           "name": "language_button",
           "value": "改变语言"
         }
       ]
     }
     ```
2. 点击按钮切换语言。
   * 进入页面后，显示的语言将跟随系统偏好语言进行设置。
   * 设置语言状态status，当系统偏好语言为中文时，status设置为-1，英文时，status设置为1。
   * 因为本例子中仅有中英两种语言，所以点击按钮后status将切换状态。

   ```ts
   import I18n from '@ohos.i18n';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Component
   @Entry
   struct Index {
     // 获取当前系统语言。如果为中文，则设置status为-1；如果为英文，则设置status为1
     status: number = I18n.System.getSystemLanguage() === "zh-Hans" ? -1 : 1;

     build() {
       Column() {
         // 获取应用偏好语言
         Text($r('app.string.module_desc'));
         Button($r('app.string.language_button')).onClick(() => {
           if (this.status === 1) {
             try {
               I18n.System.setAppPreferredLanguage('zh-Hans');
             } catch (error) {
               let err: BusinessError = error as BusinessError;
               console.error(`zh-Hans call System.setAppPreferredLanguage failed, error code: ${err.code}, message: ${err.message}.`);
             }
           } else {
             try {
               I18n.System.setAppPreferredLanguage('en-Latn-US');
             } catch (error) {
               let err: BusinessError = error as BusinessError;
               console.error(`en-Latn-US call System.setAppPreferredLanguage failed, error code: ${err.code}, message: ${err.message}.`);
             }
           }
           this.status = -this.status;
         })
       }
     }
   }
   ```

## 总结

无论是在APP内单独切换语言设置，还是跟随系统语言切换，多语言都需要通过两个步骤：

1. 定义资源文件。
2. 引用资源文件。

另附跟随系统切换语言相关指南：[多语言支持](../harmonyos-references/js-service-widget-multiple-languages.md)。
