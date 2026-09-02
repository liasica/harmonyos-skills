---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-359
title: 在深色模式切换下如何适配状态栏颜色
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 在深色模式切换下如何适配状态栏颜色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:81dbd5319f45649094820ec3723317d089ff93e75b96fb8b8736523ffa8ab8ac
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

   ```json
   // resources/dark/element/color.json
   {
     "color": [
       {
         "name": "status_bar",
         "value": "#000000"
       }
     ]
   }
   ```

   ```json
   // resources/base/element/color.json
   {
     "color": [
       {
         "name": "status_bar",
         "value": "#FFFFFF"
       }
     ]
   }
   ```
2. 缓存窗口对象和当前颜色模式，便于后续使用[setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)接口设置状态栏属性。

   ```ts
   // EntryAbility.ets

   onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
     hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
     // Cache the color mode of the current device
     AppStorage.setOrCreate('currentColorMode', this.context.config.colorMode);
   }

   onWindowStageCreate(windowStage: window.WindowStage): void {
     // Main window is created, set main page for this ability
     hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

     windowStage.loadContent('pages/Index', (err) => {
       if (err.code) {
         hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
         return;
       }
       hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
       let windowClass: window.Window = windowStage.getMainWindowSync(); // Get the main application window
       // 1. Set the window to full screen
       let isLayoutFullScreen = true;
       windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
       // 2. Cache window object
       AppStorage.setOrCreate('windowClass', windowClass);
     });
   }
   ```
3. 颜色模式变更时，更新缓存中的颜色模式。

   ```ts
   // EntryAbility.ets

   // 监听系统配置变更
   onConfigurationUpdate(newConfig: Configuration): void {
     let newColorMode = newConfig.colorMode;
     let currentColorMode = AppStorage.get<ConfigurationConstant.ColorMode>('currentColorMode');
     if (newColorMode === currentColorMode) {
       return;
     }
     // 更新缓存中的颜色模式
     AppStorage.setOrCreate('currentColorMode', newConfig.colorMode);
   }
   ```
4. 页面监听颜色模式，模式变更时更新状态栏字体颜色。

   ```ts
   import { window } from '@kit.ArkUI';
   import { ConfigurationConstant } from '@kit.AbilityKit';

   @Entry
   @Component
   struct SysDarkMode {
     @State message: string = 'page layout';
     @StorageProp('currentColorMode') @Watch('onColorModeChange') currentColorMode: number =
       ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT;

     aboutToAppear(): void {
       this.onColorModeChange();
     }

     onColorModeChange(): void {
       // Get the current application window
       let windowClass = AppStorage.get<window.Window>('windowClass') as window.Window;

       if (this.currentColorMode === ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT) {
         // Currently in light color mode
         //Set the font to black
         windowClass.setWindowSystemBarProperties({
           // Status bar text color
           statusBarContentColor: '#000000'
         });
       } else if (this.currentColorMode === ConfigurationConstant.ColorMode.COLOR_MODE_DARK) {
         // Currently in dark mode
         //Set the font to white
         windowClass.setWindowSystemBarProperties({
           // Status bar text color
           statusBarContentColor: '#FFFFFF'
         });
       } else {
         console.warn("Unsupported color mode")
       }
     }

     build() {
       Column() {
         Row()
           .width('100%')
           .height(100)
           .backgroundColor($r('app.color.status_bar'))
         // page layout
         Text(this.message)
           .fontSize(50)
           .fontColor(Color.Red)
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: {
               anchor: '__container__',
               align: VerticalAlign.Center
             },
             middle: {
               anchor: '__container__',
               align: HorizontalAlign.Center
             }
           })
           .layoutWeight(1)
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
