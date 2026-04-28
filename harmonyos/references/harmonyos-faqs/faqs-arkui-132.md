---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-132
title: 如何获取与设置屏幕亮度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何获取与设置屏幕亮度
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:35+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:542ec9d57f47f71a6ef4a0cf94cafbb1103441b65e40dc43911dff706f3cf597
---

获取与设置屏幕亮度可以通过如下两种方式：

**1、通过使用settings实现屏幕亮度的获取与设置。**

1. 通过使用[settings.getValueSync()](../harmonyos-references/js-apis-settings.md#settingsgetvaluesync10)方法可获取屏幕亮度，传入应用上下文与数据项的名称（屏幕亮度为settings.display.SCREEN\_BRIGHTNESS\_STATUS），以及默认值，即可获取当前屏幕亮度，获取值范围为0-255。

   ```
   1. Button('获取屏幕亮度')
   2. .width(328)
   3. .margin({
   4. top: 16,
   5. bottom:16
   6. })
   7. .onClick(() => {
   8. // Get screen brightness through the getValueSync() method.
   9. this.settingsBrightness = settings.getValueSync(this.context, settings.display.SCREEN_BRIGHTNESS_STATUS, '10');
   10. })
   ```

   [ScreenBrightness.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ScreenBrightness.ets#L41-L50)
2. 通过使用[settings.setValue()](../harmonyos-references/js-apis-settings.md#settingssetvalue10-1)方法可设置屏幕亮度，传入应用上下文与数据项的名称（屏幕亮度为settings.display.SCREEN\_BRIGHTNESS\_STATUS），以及设置值，即可设置当前屏幕亮度。需要注意的是，settings.setValue()方法仅系统应用可用。

**2、通过使用[window模块](../harmonyos-references/js-apis-window.md)实现屏幕亮度的获取与设置。**

1. 在EntryAbility.ets的onWindowStageCreate方法中设置一个AppStorage，保存window实例。

   ```
   1. onWindowStageCreate(windowStage: window.WindowStage): void {
   2. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
   3. let windowClass = windowStage.getMainWindowSync();
   4. AppStorage.setOrCreate('windowClass',windowClass);
   5. // ...
   6. }
   ```

   [EntryAbilityScreenBrightness.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityScreenBrightness.ets#L36-L49)
2. 通过window实例的[getWindowProperties()](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)获取窗口属性，其中包括屏幕亮度的信息。

   ```
   1. Button('获取屏幕亮度')
   2. .width(328)
   3. .margin({
   4. top: 16,
   5. bottom:16
   6. })
   7. .onClick(() => {
   8. try {
   9. // By retrieving window properties using getWindowProperties(), the screen brightness can be obtained.
   10. let properties = this.windowClass?.getWindowProperties();
   11. this.windowBrightness = properties?.brightness ?? -1;
   12. } catch (exception) {
   13. hilog.error(0x0000, TAG,
   14. `Failed to obtain the window properties. Cause code: ${exception.code}, message: ${exception.message}`);
   15. }
   16. })
   ```

   [ScreenBrightness.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ScreenBrightness.ets#L71-L86)

   说明

   屏幕亮度。该参数为浮点数，可设置的亮度范围为[0.0, 1.0]，其取1.0时表示最大亮度值。如果窗口没有设置亮度值，表示亮度跟随系统，此时获取到的亮度值为-1。
3. 通过window实例提供的[setWindowBrightness()](../harmonyos-references/arkts-apis-window-window.md#setwindowbrightness9)方法，即可设置屏幕亮度。

   ```
   1. Button('设置屏幕亮度')
   2. .width(328)
   3. .onClick(() => {
   4. try {
   5. this.windowBrightness = Math.random() * (1.0 - 0.0) + 0.0;
   6. if (this.windowBrightness < 0 || this.windowBrightness > 1) {
   7. hilog.error(0x0000, TAG, `WindowBrightness is not within the valid range`);
   8. return;
   9. }
   10. this.windowClass?.setWindowBrightness(this.windowBrightness, (err: BusinessError) => {
   11. const errCode: number = err.code;
   12. if (errCode) {
   13. hilog.error(0x0000, TAG,
   14. `Failed to set the brightness. Cause code: ${err.code}, message: ${err.message}`);
   15. return;
   16. }
   17. hilog.info(0x0000, TAG, 'Succeeded in setting the brightness.');
   18. });
   19. } catch (exception) {
   20. hilog.error(0x0000, TAG,
   21. `Failed to set the brightness. Cause code: ${exception.code}, message: ${exception.message}`);
   22. }
   23. })
   ```

   [ScreenBrightness.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ScreenBrightness.ets#L89-L111)

   说明

   该接口设置的屏幕亮度仅在应用内生效，不影响系统本身屏幕亮度。

**参考链接**

[@ohos.settings (设置数据项名称)](../harmonyos-references/js-apis-settings.md)
