---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1165
title: 子窗口无法拖动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 子窗口无法拖动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-07-07
content_hash: sha256:8d24546fb5d3d6e32bc334abf925d22821a14f71da65e638dfa6354a05170996
---

## 问题现象

通过createSubWindow创建了一个子窗口来实现悬浮窗，设置了拖动事件，但是不生效。

## 背景知识

* 可以使用滑动手势[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)拖动子窗口，在[onActionUpdate](../harmonyos-references/ts-basic-gestures-pangesture.md#onactionupdate)中获取触摸点的位置信息，并更新子窗口的位置。
* [setFollowParentWindowLayoutEnabled](../harmonyos-references/arkts-apis-window-window.md#setfollowparentwindowlayoutenabled17)设置子窗口或模态窗口（即WindowType为TYPE\_DIALOG的窗口）的布局信息（position和size）是否跟随主窗口。一般适用于主窗口和子窗口同时存在，当主窗口移动时，子窗口需要跟随移动的场景。

## 问题定位

设置子窗口背景发现子窗口大小是整个屏幕，使用resize也没用，发现创建子窗口后setFollowParentWindowLayoutEnabled为true，导致子窗口的布局信息与主窗口完全一致并保持（主窗口的大小为整个屏幕）。当子窗口调用该接口后，再调用moveTo、resize等修改布局信息的接口将不生效，当再次调用setFollowParentWindowLayoutEnabled接口并传入false时，效果将不再持续。

## 分析结论

setFollowParentWindowLayoutEnabled为true，导致子窗口的布局信息与主窗口完全一致并保持，所以无法单独拖动子窗口，除非拖动主窗口使子窗口跟随移动。

## 修改建议

1. 不使用setFollowParentWindowLayoutEnabled接口时，通过滑动手势PanGesture能正常拖动子窗口。

   ```ts
   this.windowStage.createSubWindow('SubWindow', async (err: BusinessError, data: window.Window | null) => {
     if (err.code !== 0 || !data) {
       console.error(`Failed to create the subwindow. Code: ${err.code}, message: ${err.message}`);
       return;
     }
     const win = data;
     try {
       // 1. 设置大小
       await win.resize(this.uiContext.vp2px(100), this.uiContext.vp2px(100));
       await win.setUIContent('pages/SubWindow');
       // 2. 设置透明背景，避免遮挡
       await win.setWindowBackgroundColor('#50FF00');
       // 3. 显示窗口
       await win.showWindow();
       await win.setWindowTouchable(true);
       await win.setWindowFocusable(false);
     } catch (subErr) {
       console.error('子窗口操作失败: ' + subErr.message);
     }
   });
   ```
2. 设置setFollowParentWindowLayoutEnabled接口为true时，无法通过滑动手势PanGesture单独拖动子窗口，但可以拖动主窗口使子窗口跟随移动。

   ```ts
   this.windowStage.createSubWindow('SubWindowTwo', async (err: BusinessError, data: window.Window | null) => {
     if (err.code !== 0 || !data) {
       console.error(`Failed to create the subwindow. Code: ${err.code}, message: ${err.message}`);
       return;
     }
     const win = data;
     await win.setFollowParentWindowLayoutEnabled(true);
     try {
       // 1. 设置大小
       await win.resize(this.uiContext.vp2px(100), this.uiContext.vp2px(100));
       await win.setUIContent('pages/SubWindowTwo');
       // 2. 设置透明背景，
       await win.setWindowBackgroundColor('#8050ff00');
       // 3. 显示窗口
       await win.showWindow();
       // 4. 设置不可触摸，防止子窗口阻挡主窗口的拖动的手势
       await win.setWindowTouchable(false);
       await win.setWindowFocusable(false);
     } catch (subErr) {
       console.error('子窗口操作失败: ' + subErr.message);
     }
   });
   ```

完整示例代码如下：

* EntryAbility.ets：通过AppStorage存储windowStage等相关实例以便后续使用。

  ```ts
  import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { window } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';

  const DOMAIN = 0x0000;

  export default class EntryAbility extends UIAbility {
    onCreate(): void {
      try {
        this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
      } catch (err) {
        hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
      }
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
    }

    onDestroy(): void {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
    }

    onWindowStageCreate(windowStage: window.WindowStage): void {
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

      windowStage.loadContent('pages/DragSubWindow', (err) => {
        if (err.code) {
          hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
          return;
        }
        AppStorage.setOrCreate('uiContext', windowStage.getMainWindowSync()
          .getUIContext());
        AppStorage.setOrCreate('windowStage', windowStage);
        AppStorage.setOrCreate('mainWindowId', windowStage.getMainWindowSync()
          .getWindowProperties()
          .id);
        // 默认浅色系统
        this.context.getApplicationContext()
          .setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT);
        let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
        // 1. 设置窗口全屏
        let isLayoutFullScreen = true;
        windowClass.setWindowLayoutFullScreen(isLayoutFullScreen)
          .then(() => {
            hilog.info(0x0000, 'testTag', '%{public}s', 'Succeeded in setting the window layout to full-screen mode.');
          })
          .catch((err: BusinessError) => {
            hilog.error(0x0000, 'testTag', '%{public}s', `Failed to set the window layout to full-screen mode.
            Cause: ${JSON.stringify(err)}`);
          });
        // 2. 获取布局避让遮挡的区域
        let type = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR; // 以导航条避让为例
        let avoidArea = windowClass.getWindowAvoidArea(type);
        let bottomRectHeight = avoidArea.bottomRect.height; // 获取到导航条区域的高度
        AppStorage.setOrCreate('bottomRectHeight', bottomRectHeight);

        type = window.AvoidAreaType.TYPE_SYSTEM; // 以状态栏避让为例
        avoidArea = windowClass.getWindowAvoidArea(type);
        let topRectHeight = avoidArea.topRect.height; // 获取状态栏区域高度
        AppStorage.setOrCreate('topRectHeight', topRectHeight);
        hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
      });
    }

    onWindowStageDestroy(): void {
      // Main window is destroyed, release UI related resources
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
    }

    onForeground(): void {
      // Ability has brought to foreground
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
    }

    onBackground(): void {
      // Ability has back to background
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
    }
  };
  ```
* 首页：DragSubWindow.ets。

  ```ts
  import { BusinessError } from '@kit.BasicServicesKit';
  import { window } from '@kit.ArkUI';

  @Entry
  @Component
  struct DragSubWindow {
    windowStage: window.WindowStage = AppStorage.get('windowStage') as window.WindowStage;
    uiContext = this.getUIContext();

    createSubWindow() {
      this.windowStage.createSubWindow('SubWindow', async (err: BusinessError, data: window.Window | null) => {
        if (err.code !== 0 || !data) {
          console.error(`Failed to create the subwindow. Code: ${err.code}, message: ${err.message}`);
          return;
        }
        const win = data;
        try {
          // 1. 设置大小
          await win.resize(this.uiContext.vp2px(100), this.uiContext.vp2px(100));
          await win.setUIContent('pages/SubWindow');
          // 2. 设置透明背景，避免遮挡
          await win.setWindowBackgroundColor('#50FF00');
          // 3. 显示窗口
          await win.showWindow();
          await win.setWindowTouchable(true);
          await win.setWindowFocusable(false);
        } catch (subErr) {
          console.error('子窗口操作失败: ' + subErr.message);
        }
      });
    }

    createSubWindowTwo() {
      this.windowStage.createSubWindow('SubWindowTwo', async (err: BusinessError, data: window.Window | null) => {
        if (err.code !== 0 || !data) {
          console.error(`Failed to create the subwindow. Code: ${err.code}, message: ${err.message}`);
          return;
        }
        const win = data;
        await win.setFollowParentWindowLayoutEnabled(true);
        try {
          // 1. 设置大小
          await win.resize(this.uiContext.vp2px(100), this.uiContext.vp2px(100));
          await win.setUIContent('pages/SubWindowTwo');
          // 2. 设置透明背景，
          await win.setWindowBackgroundColor('#8050ff00');
          // 3. 显示窗口
          await win.showWindow();
          // 4. 设置不可触摸，防止子窗口阻挡主窗口的拖动的手势
          await win.setWindowTouchable(false);
          await win.setWindowFocusable(false);
        } catch (subErr) {
          console.error('子窗口操作失败: ' + subErr.message);
        }
      });
    }

    build() {
      Column({ space: 50 }) {
        Button('创建一个可拖动的子窗口')
          .fontSize(16)
          .onClick(() => {
            this.createSubWindow();
          });
        Button('创建一个布局信息跟随主窗口的子窗口')
          .fontSize(16)
          .onClick(() => {
            this.createSubWindowTwo();
          });
      }
      .width('100%')
      .height('100%')
      .padding({
        left: 16,
        right: 16
      })
      .justifyContent(FlexAlign.Center);
    }
  }
  ```
* 子页面一：SubWindow.ets，使用滑动手势PanGesture拖动子窗口，在onActionUpdate中获取触摸点的位置信息，并更新子窗口的位置。

  ```ts
  import { display, window } from '@kit.ArkUI';

  export interface Position {
    x: number,
    y: number
  }

  @Entry
  @Component
  struct SubWindow {
    @State subWindow: window.Window = window.findWindow('SubWindow');
    @State windowPosition: Position = { x: 0, y: 0 };
    uiContext: UIContext = AppStorage.get('uiContext') as UIContext;

    dragToMove(event: GestureEvent, window: window.Window, windowPosition: Position): void {
      let bottomRectHeight = AppStorage.get('bottomRectHeight') as number;
      let topRectHeight = AppStorage.get('topRectHeight') as number;
      let bottomY =
        display.getDefaultDisplaySync().height - bottomRectHeight - this.uiContext.vp2px(100);
      windowPosition.x += event.offsetX;
      if (windowPosition.y > topRectHeight && windowPosition.y < bottomY) {
        windowPosition.y += event.offsetY;
      } else if (windowPosition.y <= topRectHeight && event.offsetY > 0) {
        windowPosition.y += event.offsetY;
      } else if (windowPosition.y >= bottomY && event.offsetY < 0) {
        windowPosition.y += event.offsetY;
      }
      window.moveWindowTo(windowPosition.x, windowPosition.y);
    }

    build() {
      Column() {
        Text('SubWindow')
          .fontSize(14);
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .gesture(
        PanGesture()// 发生拖拽时，获取到触摸点的位置，并将位置信息传递给windowPosition
          .onActionUpdate((event: GestureEvent) => {
            this.dragToMove(event, this.subWindow, this.windowPosition);
          })
      );
    }
  }
  ```
* 子页面二：SubWindowTwo.ets。

  ```ts
  @Entry
  @Component
  struct SubWindow {
    build() {
      Column() {
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center);
    }
  }
  ```
* module.json5文件，deviceTypes添加“2in1”。

  ```json
  {
    "module": {
      "name": "entry",
      "type": "entry",
      "description": "$string:module_desc",
      "mainElement": "EntryAbility",
      "deviceTypes": [
        "phone",
        "2in1"
      ],
      "deliveryWithInstall": true,
      "installationFree": false,
      "pages": "$profile:main_pages",
      "abilities": [
        {
          "name": "EntryAbility",
          "srcEntry": "./ets/entryability/EntryAbility.ets",
          "description": "$string:EntryAbility_desc",
          "icon": "$media:layered_image",
          "label": "$string:EntryAbility_label",
          "startWindowIcon": "$media:startIcon",
          "startWindowBackground": "$color:start_window_background",
          "exported": true,
          "skills": [
            {
              "entities": [
                "entity.system.home"
              ],
              "actions": [
                "ohos.want.action.home"
              ]
            }
          ]
        }
      ],
      "extensionAbilities": [
        {
          "name": "EntryBackupAbility",
          "srcEntry": "./ets/entrybackupability/EntryBackupAbility.ets",
          "type": "backup",
          "exported": false,
          "metadata": [
            {
              "name": "ohos.extension.backup",
              "resource": "$profile:backup_config"
            }
          ],
        }
      ]
    }
  }
  ```

## 常见FAQ

Q：createSubWindow创建子窗口时，是否可以添加进入动画？

A：子窗口显示隐藏的方法不支持动画效果。
