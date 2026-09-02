---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-132
title: 如何获取与设置屏幕亮度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > 如何获取与设置屏幕亮度
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d2465b5f0173abc4b589175ff1455e0c56c8b76e450952528bf856ce804e1283
---

获取与设置屏幕亮度可以通过如下两种方式：

**1、通过使用settings实现屏幕亮度的获取与设置。**

1. 通过使用[settings.getValueSync()](../harmonyos-references/js-apis-settings.md#settingsgetvaluesync10)方法可获取屏幕亮度，传入应用上下文与数据项的名称（屏幕亮度为settings.display.SCREEN\_BRIGHTNESS\_STATUS），以及默认值，即可获取当前屏幕亮度，获取值范围为0-255。

   ```ts
   Button('获取屏幕亮度')
     .width(328)
     .margin({
       top: 16,
       bottom:16
     })
     .onClick(() => {
       // Get screen brightness through the getValueSync() method.
       this.settingsBrightness = settings.getValueSync(this.context, settings.display.SCREEN_BRIGHTNESS_STATUS, '10');
     })
   ```
2. 通过使用[settings.setValue()](../harmonyos-references/js-apis-settings.md#settingssetvalue10-1)方法可设置屏幕亮度，传入应用上下文与数据项的名称（屏幕亮度为settings.display.SCREEN\_BRIGHTNESS\_STATUS），以及设置值，即可设置当前屏幕亮度。需要注意的是，settings.setValue()方法仅系统应用可用。

**2、通过使用[window模块](../harmonyos-references/js-apis-window.md)实现屏幕亮度的获取与设置。**

1. 在EntryAbility.ets的onWindowStageCreate方法中设置一个AppStorage，保存window实例。

   ```ts
   onWindowStageCreate(windowStage: window.WindowStage): void {
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
     let windowClass = windowStage.getMainWindowSync();
     AppStorage.setOrCreate('windowClass',windowClass);
     // ...
   }
   ```
2. 通过window实例的[getWindowProperties()](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)获取窗口属性，其中包括屏幕亮度的信息。

   ```ts
   Button('获取屏幕亮度')
     .width(328)
     .margin({
       top: 16,
       bottom:16
     })
     .onClick(() => {
       try {
         // By retrieving window properties using getWindowProperties(), the screen brightness can be obtained.
         let properties = this.windowClass?.getWindowProperties();
         this.windowBrightness = properties?.brightness ?? -1;
       } catch (exception) {
         hilog.error(0x0000, TAG,
           `Failed to obtain the window properties. Cause code: ${exception.code}, message: ${exception.message}`);
       }
     })
   ```

   **说明** 

   屏幕亮度。该参数为浮点数，可设置的亮度范围为[0.0, 1.0]，其取1.0时表示最大亮度值。如果窗口没有设置亮度值，表示亮度跟随系统，此时获取到的亮度值为-1。
3. 通过window实例提供的[setWindowBrightness()](../harmonyos-references/arkts-apis-window-window.md#setwindowbrightness9)方法，即可设置屏幕亮度。

   ```typescript
   Button('设置屏幕亮度')
     .width(328)
     .onClick(() => {
       try {
         this.windowBrightness = Math.random() * (1.0 - 0.0) + 0.0;
         if (this.windowBrightness < 0 || this.windowBrightness > 1) {
           hilog.error(0x0000, TAG, `WindowBrightness is not within the valid range`);
           return;
         }
         this.windowClass?.setWindowBrightness(this.windowBrightness, (err: BusinessError) => {
           const errCode: number = err.code;
           if (errCode) {
             hilog.error(0x0000, TAG,
               `Failed to set the brightness. Cause code: ${err.code}, message: ${err.message}`);
             return;
           }
           hilog.info(0x0000, TAG, 'Succeeded in setting the brightness.');
         });
       } catch (exception) {
         hilog.error(0x0000, TAG,
           `Failed to set the brightness. Cause code: ${exception.code}, message: ${exception.message}`);
       }
     })
   ```

   **说明** 

   该接口设置的屏幕亮度仅在应用内生效，不影响系统本身屏幕亮度。

**参考链接**

[@ohos.settings (设置数据项名称)](../harmonyos-references/js-apis-settings.md)
