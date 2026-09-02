---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-19
title: 应用界面如何显示系统语言之外的语言
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 应用界面如何显示系统语言之外的语言
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c5eb3c70ef62b7252d08e027cd712e951a881bbc2dd3c5b5bb3a8def607749be
---

## 问题现象

系统设置中语言支持简体中文、繁体中文、英文、维吾尔文、藏文、俄文等语言，应用如何显示系统预置语言之外的其他语言？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/SqGDWQbXS_uxDkZKcLPgqg/zh-cn_image_0000002659062373.png "点击放大")

## 背景知识

* [getOverrideConfiguration](../harmonyos-references/js-apis-resource-manager.md#getoverrideconfiguration12)：获取差异化资源的配置。
* [getOverrideResourceManager](../harmonyos-references/js-apis-resource-manager.md#getoverrideresourcemanager12)：获取可以加载差异化资源的资源管理对象。
* [getStringSync](../harmonyos-references/js-apis-resource-manager.md#getstringsync9)：获取指定资源ID对应的字符串。

## 解决方案

应用可以通过在resources目录下添加[限定词目录](../harmonyos-guides/resource-categories-and-access.md#限定词目录与设备状态的匹配规则)，如日语ja\_JP、德语de\_DE，增加不同语言资源文件后，在应用运行时，通过[指定资源配置方式](../harmonyos-guides/resource-categories-and-access.md#获取指定配置的资源)，让应用展示不同国家语言。

参考示例：

* entry/src/main/resources/zh\_CN/element/string.json示例：

  ```json
  {
    "string": [
      {
        "name": "language",
        "value": "这是中文"
      }
    ]
  }
  ```
* entry/src/main/resources/ja\_JP/element/string.json示例：

  ```json
  {
    "string": [
      {
        "name": "language",
        "value": "これは日本語です"
      }
    ]
  }
  ```
* entry/src/main/resources/en\_US/element/string.json示例：

  ```json
  {
    "string": [
      {
        "name": "language",
        "value": "This is English"
      }
    ]
  }
  ```

在Index.ets中，分别获取三种语言的资源并显示在文本框中，运行设备当前系统语言为中文，示例代码：

```ts
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State englishString: string = '';
  @State jpString: string = '';

  getString(): string {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let resMgr = context.resourceManager;
    let resId = $r('app.string.language').id;
    // 获取符合当前系统语言地区、颜色模式、分辨率等配置的资源
    let currentLanguageString = resMgr.getStringSync(resId);
    // 获取符合当前系统颜色模式、分辨率等配置的英文资源
    let overrideConfig = resMgr.getOverrideConfiguration();
    overrideConfig.locale = 'en_US'; // 指定资源的语言为英语，地区为美国
    let overrideResMgr = resMgr.getOverrideResourceManager(overrideConfig);
    this.englishString = overrideResMgr.getStringSync(resId);
    // 获取符合当前系统颜色模式、分辨率等配置的日文资源
    overrideConfig.locale = 'ja_JP'; // 指定资源的语言为日文，地区为日本
    overrideResMgr.updateOverrideConfiguration(overrideConfig); // 等效于resMgr.updateOverrideConfiguration(overrideConfig)
    this.jpString = overrideResMgr.getStringSync(resId);
    return currentLanguageString;
  }

  build() {
    Row() {
      Column() {
        Text(this.getString())
          .fontSize(45)
          .fontWeight(FontWeight.Bold)
          .margin({ top: 10 });
        Text(this.englishString)
          .fontSize(45)
          .fontWeight(FontWeight.Bold)
          .margin({ top: 10 });
        Text(this.jpString)
          .fontSize(45)
          .fontWeight(FontWeight.Bold)
          .margin({ top: 10 });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```
