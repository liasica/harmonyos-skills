---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-359
title: 在深色模式切换下如何适配状态栏颜色
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 在深色模式切换下如何适配状态栏颜色
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f51628961c98e3f2a977ef17df6a515a0135bef31b5988871a900c78b37916cf
---

**问题描述**

在深色模式下，状态栏颜色与背景色对比度不足，导致内容难以辨认。

**解决措施**

1. base/element/color.json中定义浅色模式的状态栏背景色。
2. 在dark/element/color.json中定义深色模式的状态栏背景色。
3. 监听深浅色模式的切换。
4. 监听到颜色切换后，手动使用[setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)设置状态栏字体颜色。

关于深色模式适配，请参考[深色模式适配](../best-practices/bpta-dark-mode-adaptation.md#section128661451172714)。

参考代码如下：

1. 定义深浅色模式下的颜色资源。

   ```
   1. // resources/dark/element/color.json
   2. {
   3. "color": [
   4. {
   5. "name": "status_bar",
   6. "value": "#000000"
   7. }
   8. ]
   9. }
   ```

   ```
   1. // resources/base/element/color.json
   2. {
   3. "color": [
   4. {
   5. "name": "status_bar",
   6. "value": "#FFFFFF"
   7. }
   8. ]
   9. }
   ```
2. 缓存窗口对象和当前颜色模式，便于后续使用[setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)接口设置状态栏属性。

   ```
   1. // EntryAbility.ets

   4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   5. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
   6. // Cache the color mode of the current device
   7. AppStorage.setOrCreate('currentColorMode', this.context.config.colorMode);
   8. }

   11. onWindowStageCreate(windowStage: window.WindowStage): void {
   12. // Main window is created, set main page for this ability
   13. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

   16. windowStage.loadContent('pages/Index', (err) => {
   17. if (err.code) {
   18. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
   19. return;
   20. }
   21. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
   22. let windowClass: window.Window = windowStage.getMainWindowSync(); // Get the main application window
   23. // 1. Set the window to full screen
   24. let isLayoutFullScreen = true;
   25. windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
   26. // 2. Cache window object
   27. AppStorage.setOrCreate('windowClass', windowClass);
   28. });
   29. }
   ```

   [EntryAbilitySystemBarProperties.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilitySystemBarProperties.ets#L28-L56)
3. 颜色模式变更时，更新缓存中的颜色模式。

   ```
   1. // EntryAbility.ets

   3. // 监听系统配置变更
   4. onConfigurationUpdate(newConfig: Configuration): void {
   5. let newColorMode = newConfig.colorMode;
   6. let currentColorMode = AppStorage.get<ConfigurationConstant.ColorMode>('currentColorMode');
   7. if (newColorMode === currentColorMode) {
   8. return;
   9. }
   10. // 更新缓存中的颜色模式
   11. AppStorage.setOrCreate('currentColorMode', newConfig.colorMode);
   12. }
   ```

   [MyAbilityStage.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/MyAbilityStage.ets#L25-L36)
4. 页面监听颜色模式，模式变更时更新状态栏字体颜色。

   ```
   1. import { window } from '@kit.ArkUI';
   2. import { ConfigurationConstant } from '@kit.AbilityKit';

   5. @Entry
   6. @Component
   7. struct SysDarkMode {
   8. @State message: string = 'page layout';
   9. @StorageProp('currentColorMode') @Watch('onColorModeChange') currentColorMode: number =
   10. ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT;

   12. aboutToAppear(): void {
   13. this.onColorModeChange();
   14. }

   16. onColorModeChange(): void {
   17. // Get the current application window
   18. let windowClass = AppStorage.get<window.Window>('windowClass') as window.Window;

   21. if (this.currentColorMode === ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT) {
   22. // Currently in light color mode
   23. //Set the font to black
   24. windowClass.setWindowSystemBarProperties({
   25. // Status bar text color
   26. statusBarContentColor: '#000000'
   27. });
   28. } else if (this.currentColorMode === ConfigurationConstant.ColorMode.COLOR_MODE_DARK) {
   29. // Currently in dark mode
   30. //Set the font to white
   31. windowClass.setWindowSystemBarProperties({
   32. // Status bar text color
   33. statusBarContentColor: '#FFFFFF'
   34. });
   35. } else {
   36. console.warn("Unsupported color mode")
   37. }
   38. }

   40. build() {
   41. Column() {
   42. Row()
   43. .width('100%')
   44. .height(100)
   45. .backgroundColor($r('app.color.status_bar'))
   46. // page layout
   47. Text(this.message)
   48. .fontSize(50)
   49. .fontColor(Color.Red)
   50. .fontWeight(FontWeight.Bold)
   51. .alignRules({
   52. center: {
   53. anchor: '__container__',
   54. align: VerticalAlign.Center
   55. },
   56. middle: {
   57. anchor: '__container__',
   58. align: HorizontalAlign.Center
   59. }
   60. })
   61. .layoutWeight(1)
   62. }
   63. .height('100%')
   64. .width('100%')
   65. }
   66. }
   ```

   [DarkModeSwitchStatusBarColor.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/DarkModeSwitchStatusBarColor.ets#L21-L87)
