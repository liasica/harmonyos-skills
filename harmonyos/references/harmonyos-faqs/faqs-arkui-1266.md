---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1266
title: 深色模式适配及持久化实现方式
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 深色模式适配及持久化实现方式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a0366c1ad3061715698a121470d5b1b7dacefd047cab966c27431a22844e9942
---

## 问题现象

调用ApplicationContext.setColorMode(ConfigurationConstant.ColorMode.COLOR\_MODE\_DARK)将应用配色方案设为深色模式后，仅运行期间有效。退出应用重新进入后，设置丢失，深色模式失效。如何实现设置深色模式后，下次进入应用能保留配置？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/Yk1EH_sDRHmKplbawTCwtw/zh-cn_image_0000002628756010.gif "点击放大")

## 背景知识

* 深色模式适配属于应用最常见的功能，通过[ApplicationContext.setColorMode](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextsetcolormode11)自定义应用的颜色模式，官网案例参考：[深色模式适配](../best-practices/bpta-dark-mode-adaptation.md)。该案例内有详细说明如何实现深浅色模式适配以及，如何取消或跟随系统的深浅色切换。其中深浅色模式监听参考：[深浅色监听](../harmonyos-guides/reader-setting-color-mode.md)。
* [首选项模块（Preferences）](../harmonyos-references/js-apis-data-preferences.md#preferences)可以提供Key-Value键值型数据的处理接口，实现对轻量级数据的查询、修改和持久化功能。

## 解决方案

ApplicationContext.setColorMode属性本身并不支持数据持久化，可以采用用户首选项的数据持久化方式实现配置储存，然后在进入应用时读取用户首选项内容重新配置上一次退出软件时设置的深浅色模式。

* 第一步：在pages目录下创建PreferencesUtil.ets页面，在其中添加Preferences对象。用户首选项实现指南详见[通过用户首选项实现数据持久化](../harmonyos-guides/data-persistence-by-preferences.md)。

  ```screen
  import { preferences } from '@kit.ArkData';

  export class PreferencesUtil {
    preference?: preferences.Preferences;

    getColorModel(context: Context) {
      this.preference = preferences.getPreferencesSync(context, { name: 'Color' });
    }

    saveColorModel(current: string) {
      this.preference?.putSync('colorModel', current);
      this.preference?.flush();
    }

    getChangeColorModel() {
      let current: string = 'COLOR_MODE_LIGHT';
      current = this.preference?.getSync('colorModel', 0) as string;
      return current;
    }
  }

  let preferenceUtilsObject: PreferencesUtil = new PreferencesUtil();

  export default preferenceUtilsObject;
  ```

* **第二步**：在pages目录下的Index.ets页面设置深浅色模式切换，并保存在用户首选项内。

  ```screen
  import { ConfigurationConstant } from '@kit.AbilityKit';
  import preferenceUtilsObject from './PreferencesUtil';

  @Entry
  @Component
  struct DarkModePage {
    build() {
      Column({ space: 20 }) {
        Button('切换深色模式')
          .onClick(() => {
            this.getUIContext()
              .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
            preferenceUtilsObject.saveColorModel('COLOR_MODE_DARK');
          });
        Button('切换浅色模式')
          .onClick(() => {
            this.getUIContext()
              .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT);
            preferenceUtilsObject.saveColorModel('COLOR_MODE_LIGHT');
          });
        Button('跟随系统')
          .onClick(() => {
            this.getUIContext()
              .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
            preferenceUtilsObject.saveColorModel('COLOR_MODE_NOT_SET');
          });
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%');
    }
  }
  ```
* **第三步**：修改EntryAbility页面的onWindowStageCreate函数，在应用启动时获取储存的用户首选项，并设置应用深浅色模式。

  ```screen
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', () => {
      preferenceUtilsObject.getColorModel(this.context);
      let colorModel: string = preferenceUtilsObject.getChangeColorModel();
      if (colorModel === 'COLOR_MODE_DARK') {
        this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
      } else if (colorModel === 'COLOR_MODE_LIGHT') {
        this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT);
      } else {
        this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
      }
    });
  }
  ```

## 常见FAQ

Q：如何在代码中获取当前系统的深浅色模式状态？

A：在AbilityStage的onCreate()生命周期中获取APP当前的颜色模式：

```screen
onCreate(): void {
  try {
    this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    console.info( 'colorMode', this.context.config.colorMode); // 获取当前APP的颜色模式
  } catch (err) {
    hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
  }
  hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
}
```
