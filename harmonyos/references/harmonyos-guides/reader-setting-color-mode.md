---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-setting-color-mode
title: 适配深、浅色模式
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > 书籍内容排版 > 修改阅读设置 > 适配深、浅色模式
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9ec69ecbc8863ce1a75809b60d140b6b2f76bd90b0925c1d4863ad0aeb371b49
---

当应用需要根据设备的深、浅色模式变化动态切换主题时，开发者可通过UIAbility的onConfigurationUpdate回调判断模式的变化，然后设置模式对应的字体颜色及背景色。

## 接口说明

适配深、浅色主题主要涉及1个接口，具体介绍如下表所示。

| 接口名 | 描述 |
| --- | --- |
| [setPageConfig](../harmonyos-references/reader-read-core.md#setpageconfig)(pageConfig: ReaderSetting): void | 设置或者修改页面排版属性。 |

## 开发准备

在适配深、浅色主题之前，请先确保已经“[构建阅读器](reader-read-page.md)”。

## 开发步骤

1. 监听UIAbility的onConfigurationUpdate回调，并通过应用级变量的状态管理[AppStorage](arkts-appstorage.md)保存当前colorMode值。

   ```typescript
   import { Configuration, UIAbility } from '@kit.AbilityKit';

   export default class EntryAbility extends UIAbility {

     onConfigurationUpdate(newConfig: Configuration): void {
       AppStorage.setOrCreate('colorMode', newConfig.colorMode);
     }
   }
   ```
2. 阅读页通过[@StorageLink](arkts-appstorage.md#storagelink)装饰器监听colorMode字段的变化。如果颜色变化，则触发对应主题色的变更。

   ```typescript
   import { ConfigurationConstant } from '@kit.AbilityKit';

   @StorageLink('colorMode') @Watch('colorModeChange') colorMode: ConfigurationConstant.ColorMode =
     ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET;

   /**
    * 系统深色模式变化，可以重新设置主题
    */
   colorModeChange() {
     if (this.colorMode === ConfigurationConstant.ColorMode.COLOR_MODE_DARK) {
       this.readerSetting.nightMode = true;
       this.readerSetting.fontColor = '#ffffff';
       this.readerSetting.themeColor = '#202224';
     } else {
       this.readerSetting.nightMode = false;
       this.readerSetting.fontColor = '#000000';
       this.readerSetting.themeColor = '#FFFFFF';
     }
     this.readerComponentController.setPageConfig(this.readerSetting);
   }
   ```
