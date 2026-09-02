---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-3
title: 如何实现防截屏功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何实现防截屏功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f5aadd474749e6482bfb76e27d216007042a814cd85fa439efff158fed9d609e
---

设置窗口隐私模式，禁止截屏或录屏。此接口适用于禁止截屏/录屏的场景。

方式一：进入页面开启隐私模式，离开页面取消，具体可参考以下步骤：

首先，在 module.json5 文件中声明需要使用 ohos.permission.PRIVACY\_WINDOW 权限。

```json
"requestPermissions": [
  {
    "name": "ohos.permission.PRIVACY_WINDOW"
  }
],
```

通过导航栏显示状态切换触发 onNavBarStateChange回调。进入页面时，isVisible 为 true，调用setWindowPrivacyMode 设置窗口为隐私模式。离开页面时，isVisible 为 false，设置窗口为非隐私模式。参考示例代码如下：

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

class WindowUtils {
  static setWindowPrivacyModeInPage(context: common.UIAbilityContext, isFlag: boolean) {
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setWindowPrivacyMode(isFlag, (err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error('Failed to set the window to privacy mode. Cause:' + JSON.stringify(err));
          return;
        }
        console.info('Succeeded in setting the window to privacy mode.');
      });
    })
  }
}

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  @Provide('NavPathStack') pageStack: NavPathStack = new NavPathStack();
  context = this.getUIContext();

  @Builder
  PagesMap(name: string) {
    if (name === 'Index') {
      Index();
    } else if (name === 'PageOne') {
      PageOne();
    }
  }

  build() {
    Navigation(this.pageStack) {
      Column() {
        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageStack.pushPath({ name: 'PageOne' }) // Push the page info of specified NavDestination into the stack
          })
      }
    }
    .navDestination(this.PagesMap)
    .onNavBarStateChange((isVisible: boolean) => {
      // Callback triggered when navigation bar display state changes
      console.info('------>isVisible：' + isVisible)
      WindowUtils.setWindowPrivacyModeInPage(this.context.getHostContext() as common.UIAbilityContext, isVisible);
    })
  }
}

@Component
struct PageOne {
  @Consume('NavPathStack') pageStack: NavPathStack;

  build() {
    NavDestination() {
      Column() {
        Text('PageOne')
      }
    }
    .title('pageOne')
    .onBackPressed(() => {
      const popDestinationInfo = this.pageStack.pop(); // Pop the top element from the navigation stack
      return true;
    })
  }
}
```

方式二：设置主窗口为隐私模式，参考以下步骤：

在module.json5文件中声明需要使用的ohos.permission.PRIVACY\_WINDOW权限。

```json
"requestPermissions": [
  {
    "name": "ohos.permission.PRIVACY_WINDOW"
  }
],
```

在EntryAbility.ets文件的onWindowStageCreate回调中设置主窗口为隐私模式，具体可参考示例代码：

```typescript
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    // Get the main window
    windowStage.getMainWindow((err: BusinessError, data) => {
      let errCode: number = err.code;
      if (errCode) {
        console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
        return;
      }
      let windowClass: window.Window = data;
      console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
      // Set the window privacy mode
      let isPrivacyMode: boolean = true;
      try {
        windowClass.setWindowPrivacyMode(isPrivacyMode, (err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error('Failed to set the window to privacy mode. Cause:' + JSON.stringify(err));
            return;
          }
          console.info('Succeeded in setting the window to privacy mode.');
        });
      } catch (exception) {
        console.error('Failed to set the window to privacy mode. Cause:' + JSON.stringify(exception));
      }
    })
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

**参考链接**

[setWindowPrivacyMode](../harmonyos-references/arkts-apis-window-window.md#setwindowprivacymode9)、[onNavBarStateChange](../harmonyos-references/ts-basic-components-navigation.md#onnavbarstatechange9)
