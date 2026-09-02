---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-immersive-effect-check
title: "@cross-device-app-dev/immersive-effect-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/immersive-effect-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:31ff2237de3dd4f72cac07a4948d870e539315ae4eb8f081a48918d6c24ba2c2
---

若应用通过[setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)接口设置窗口布局，建议调用[getWindowAvoidArea()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)和[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)获取和动态监听避让区域的变更信息，使页面布局根据避让区域信息进行动态调整。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/immersive-effect-check": "suggestion"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        return;
      }
      let windowClass: window.Window = windowStage.getMainWindowSync(); // Obtain the main window of the application.
      // 1. 设置窗口全屏.
      let isLayoutFullScreen = true;
      windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
        console.info('Succeeded in setting the window layout to full-screen mode.');
      }).catch((err: BusinessError) => {
        console.error('Failed to set the window layout to full-screen mode. Cause:' + JSON.stringify(err));
      });

      // 2. 获取避让区域.
      let type = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR; // Here a navigation bar is used as an example.
      let avoidArea = windowClass.getWindowAvoidArea(type);
      let bottomRectHeight = avoidArea.bottomRect.height; // Obtain the height of the navigation area.
      AppStorage.setOrCreate('bottomRectHeight', bottomRectHeight);
      type = window.AvoidAreaType.TYPE_SYSTEM; // The status bar is used as an example.
      avoidArea = windowClass.getWindowAvoidArea(type);
      let topRectHeight = avoidArea.topRect.height; // Obtain the height of the status bar area.
      AppStorage.setOrCreate('topRectHeight', topRectHeight);
      // 3. Register a listening function to dynamically obtain the data of the avoid area.
      windowClass.on('avoidAreaChange', (data) => {
        if (data.type === window.AvoidAreaType.TYPE_SYSTEM) {
          let topRectHeight = data.area.topRect.height;
          AppStorage.setOrCreate('topRectHeight', topRectHeight);
        } else if (data.type == window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR) {
          let bottomRectHeight = data.area.bottomRect.height;
          AppStorage.setOrCreate('bottomRectHeight', bottomRectHeight);
        }
      });
    });
  }
}
```

## 反例

```screen
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        return;
      }
      let windowClass: window.Window = windowStage.getMainWindowSync(); // Obtain the main window of the application.
      // 只设置窗口全屏.
      let isLayoutFullScreen = true;
      windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
        console.info('Succeeded in setting the window layout to full-screen mode.');
      }).catch((err: BusinessError) => {
        console.error('Failed to set the window layout to full-screen mode. Cause:' + JSON.stringify(err));
      });
    });
  }
}
```

## 规则集

```screen
plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
