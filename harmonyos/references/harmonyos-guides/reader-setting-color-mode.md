---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-setting-color-mode
title: 适配深、浅色模式
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > 书籍内容排版 > 修改阅读设置 > 适配深、浅色模式
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:24d08ea34a8b33073494d37e759d5c9583dcf43f52f111bf3ca2931388fbc771
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

   ```
   1. import { Configuration, UIAbility } from '@kit.AbilityKit';

   3. export default class EntryAbility extends UIAbility {

   5. onConfigurationUpdate(newConfig: Configuration): void {
   6. AppStorage.setOrCreate('colorMode', newConfig.colorMode);
   7. }
   8. }
   ```
2. 阅读页通过[@StorageLink](arkts-appstorage.md#storagelink)装饰器监听colorMode字段的变化。如果颜色变化，则触发对应主题色的变更。

   ```
   1. import { ConfigurationConstant } from '@kit.AbilityKit';

   3. @StorageLink('colorMode') @Watch('colorModeChange') colorMode: ConfigurationConstant.ColorMode =
   4. ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET;

   6. /**
   7. * 系统深色模式变化，可以重新设置主题
   8. */
   9. colorModeChange() {
   10. if (this.colorMode === ConfigurationConstant.ColorMode.COLOR_MODE_DARK) {
   11. this.readerSetting.nightMode = true;
   12. this.readerSetting.fontColor = '#ffffff';
   13. this.readerSetting.themeColor = '#202224';
   14. } else {
   15. this.readerSetting.nightMode = false;
   16. this.readerSetting.fontColor = '#000000';
   17. this.readerSetting.themeColor = '#FFFFFF';
   18. }
   19. this.readerComponentController.setPageConfig(this.readerSetting);
   20. }
   ```
