---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-29
title: 分屏模式，不支持分栏显示
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 分屏模式，不支持分栏显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0df0425ac828afaa16be73ac48fd4ace71f66efc105030f8af4f832cb5a43bbb
---

## 问题现象

应用分屏时，不支持分栏显示。

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)：Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（NavDestination的子组件），首页和非首页通过路由进行切换。
* [mode](../harmonyos-references/ts-basic-components-navigation.md#mode9)：Navigation的mode属性可设置导航栏的显示模式，支持单栏（Stack）、分栏（Split）和自适应（Auto）。
* [分栏布局](../best-practices/bpta-multi-device-page-layout.md#section11897247142110)：智能终端设备种类繁多，不同设备的屏幕大小和用户使用习惯不同，开发者可以根据屏幕尺寸断点，灵活使用Navigation组件和SidebarContainer组件来实现不同的分栏效果。
* [显示设备的显示方向](../harmonyos-references/js-apis-display.md#orientation10)：可通过[Display](../harmonyos-references/js-apis-display.md#display)实例获取屏幕的方向。

## 问题定位

1. 查阅平板上全屏时的分栏情况，竖屏时单栏，横屏时双栏。
2. 查阅首页代码中是否使用Navigation组件实现页面的跳转。
3. 查阅Navigation组件的mode属性是否针对断点类型进行适配，例如下面代码。

   ```ts
   Navigation(this.pathInfo) {
     // ...
   }
   .mode(this.currentBreakPoint === 'sm' ? NavigationMode.Stack : this.notesNavMode)
   ```

## 分析结论

应用全屏横向时可以正常分栏，且代码中Navigation的mode属性也有根据断点类型进行适配，那就是分屏时的断点刚好适配的是单栏，所以分屏时才会单栏显示。

## 修改建议

在EntryAbility.ets文件的onWindowStageCreate中获取到window。

```ts
import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

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
    AppStorage.setOrCreate('windowClass', windowStage.getMainWindowSync());
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
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

可以增加Navigation组件的mode属性代码适配逻辑，保证在屏幕横屏时，可以分栏显示。

```ts
import { window } from '@kit.ArkUI';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  windowClass: window.Window | undefined = AppStorage.get('windowClass');
  currentBreakPoint: WidthBreakpoint = this.getUIContext().getWindowWidthBreakpoint();
  currentWindowStatusType: WindowStatusType | undefined = this.windowClass?.getWindowStatus();
  @State currentMode: NavigationMode = NavigationMode.Stack;
  pathInfos: NavPathStack = new NavPathStack();

  setCurrentMode() {
    // 判断屏幕方向，横屏时分栏
    if (display.getDefaultDisplaySync().orientation === display.Orientation.LANDSCAPE ||
      display.getDefaultDisplaySync().orientation === display.Orientation.LANDSCAPE_INVERTED) {
      if (this.currentWindowStatusType === 4) {
        this.currentMode = NavigationMode.Stack;
      } else {
        this.currentMode = NavigationMode.Split;
      }
    } else {
      // 纵向时根据横向断点适配分栏
      this.currentMode = this.currentBreakPoint <= 2 ? NavigationMode.Stack : NavigationMode.Split;
    }
  }

  aboutToAppear(): void {
    this.setCurrentMode();
    this.windowClass?.on('windowSizeChange', () => {
      this.currentBreakPoint = this.getUIContext().getWindowWidthBreakpoint();
      this.setCurrentMode();
    });
    this.windowClass?.on('windowStatusChange', (WindowStatusType) => {
      this.currentWindowStatusType = WindowStatusType;
    });
  }

  build() {
    Navigation(this.pathInfos) {
      Column() {
        Text('测试分屏时，是否可以分栏显示');
      };
    }
    .mode(this.currentMode);
  }
}
```
