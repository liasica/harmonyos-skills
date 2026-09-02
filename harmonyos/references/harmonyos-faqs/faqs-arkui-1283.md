---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1283
title: 如何解决获取窗口实例时出现延迟的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何解决获取窗口实例时出现延迟的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:88ff9f0d5aae41c114234f993b9a3f0eca18fea6bcda6d93b8020cedf3d4d7ec
---

## 问题现象

如果仅需要在部分页面实现诸如设置隐私模式，窗口旋转等功能，需要先获取到窗口实例，再通过窗口实例去设置隐私模式或窗口旋转等功能。以官网[如何实现防截屏功能](faqs-arkui-3.md)为例，通过方式二在PageOne和PageTwo设置隐私模式，在频繁切换页面时，有时隐私模式会失效，导致该页面可以截屏。

问题代码如下：

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

class WindowUtils {
  static setWindowPrivacyModeInPage(context: common.UIAbilityContext, isFlag: boolean) {
    window.getLastWindow(context).then((lastWindow) => {
    // 通过窗口实例调用setWindowPrivacyMode设置隐私模式
      lastWindow.setWindowPrivacyMode(isFlag, (err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error('Failed to set the window to privacy mode. Cause:' ,`${JSON.stringify(err)}`);
          return;
        }
        console.info('Succeeded in setting the window to privacy mode.');
      });
    });
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
    } else if (name === 'PageTwo') {
      PageTwo();
    }
  }

  build() {
    Navigation(this.pageStack) {
      Column() {
        Button('到PageOne', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageStack.replacePathByName('PageOne', null,
              false);
          });
      };
    }
    .navDestination(this.PagesMap);
  }
}

@Component
struct PageOne {
  @Consume('NavPathStack') pageStack: NavPathStack;

  build() {
    NavDestination() {
      Column() {
        Text('PageOne');
        Button('到PageTwo', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageStack.replacePathByName('PageTwo', null,
              false);
          });
      };
    }
    .title('pageOne')
    .onShown(() => {
      WindowUtils.setWindowPrivacyModeInPage(this.getUIContext().getHostContext() as common.UIAbilityContext, true);
    })
    .onHidden(() => {
      WindowUtils.setWindowPrivacyModeInPage(this.getUIContext().getHostContext() as common.UIAbilityContext, false);
    });
  }
}

@Component
struct PageTwo {
  @Consume('NavPathStack') pageStack: NavPathStack;

  build() {
    NavDestination() {
      Column() {
        Text('PageTwo');
        Button('到PageOne', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageStack.replacePathByName('PageOne', null,
              false);
          });
      };
    }
    .title('pageTwo')
    .onShown(() => {
      WindowUtils.setWindowPrivacyModeInPage(this.getUIContext().getHostContext() as common.UIAbilityContext, true);
    })
    .onHidden(() => {
      WindowUtils.setWindowPrivacyModeInPage(this.getUIContext().getHostContext() as common.UIAbilityContext, false);
    });
  }
}
```

正常情况下，当反复切换页面时，隐私模式应该由开启到关闭再到开启往复循环。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/jsYdR9hZR6S1H7uqm4XY-w/zh-cn_image_0000002669661697.png "点击放大")

但日志中mode出现了连续为1和连续为0情况，说明隐私模式不是从开启到关闭进行循环。

## 背景知识

* [window.getLastWindow](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)通过异步的方式获取最上层窗口。
* [windowStage.getMainWindowSync](../harmonyos-references/arkts-apis-window-windowstage.md#getmainwindowsync9)通过同步的方式获取主窗口对象。
* [AppStorage.setOrCreate](../harmonyos-references/ts-state-management.md#setorcreate10)可以获取到对应的WindowStage实例，并将其存储到AppStorage中。
* [AppStorage.get](../harmonyos-references/ts-state-management.md#get10)可以在页面中获取到AppStorage中的WindowStage实例。

## 问题定位

在设置隐私模式时，需要先获取窗口实例，上述代码中获取窗口实例的方式为window.getLastWindow，这是一个性能消耗较大的异步方法。

## 分析结论

由于getLastWindow底层原因，需要经过查找获取实例，一定程度上会有性能损耗，导致获取窗口实例出现延迟。

## 修改建议

可以通过windowStage.getMainWindowSync的同步方式获取窗口实例。再去设置隐私模式。

```ts
onWindowStageCreate(windowStage: window.WindowStage): void {
  AppStorage.setOrCreate('windowStage', windowStage);
```

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

class WindowUtils {
  static setWindowPrivacyModeInPage(context: common.UIAbilityContext, isFlag: boolean) {
    console.info(`${context}`);
    let windowStage = AppStorage.get('windowStage') as window.WindowStage;
    let windowClass = windowStage.getMainWindowSync();
    windowClass.setWindowPrivacyMode(isFlag, (err: BusinessError) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error('Failed to set the window to privacy mode. Cause:' + JSON.stringify(err));
        return;
      }
      console.info('Succeeded in setting the window to privacy mode.');
    });
  }
}

@Entry
@Component
struct Index {
  @Provide('NavPathStack') pageStack: NavPathStack = new NavPathStack();

  @Builder
  PagesMap(name: string) {
    if (name === 'Index') {
      Index();
    } else if (name === 'PageOne') {
      PageOne();
    } else if (name === 'PageTwo') {
      PageTwo();
    }
  }

  build() {
    Navigation(this.pageStack) {
      Column() {
        Button('到PageOne', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageStack.replacePathByName('PageOne', null,
              false);
          });
      };
    }
    .navDestination(this.PagesMap);
  }
}

@Component
struct PageOne {
  @Consume('NavPathStack') pageStack: NavPathStack;

  build() {
    NavDestination() {
      Column() {
        Text('PageOne');
        Button('到PageTwo', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageStack.replacePathByName('PageTwo', null,
              false);
          });
      };
    }
    .title('pageOne')
    .onShown(() => {
      WindowUtils.setWindowPrivacyModeInPage(this.getUIContext().getHostContext() as common.UIAbilityContext, true);
    })
    .onHidden(() => {
      WindowUtils.setWindowPrivacyModeInPage(this.getUIContext().getHostContext() as common.UIAbilityContext, false);
    });
  }
}

@Component
struct PageTwo {
  @Consume('NavPathStack') pageStack: NavPathStack;

  build() {
    NavDestination() {
      Column() {
        Text('PageTwo');
        Button('到PageOne', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageStack.replacePathByName('PageOne', null,
              false);
          });
      };
    }
    .title('pageTwo')
    .onShown(() => {
      WindowUtils.setWindowPrivacyModeInPage(this.getUIContext().getHostContext() as common.UIAbilityContext, true);
    })
    .onHidden(() => {
      WindowUtils.setWindowPrivacyModeInPage(this.getUIContext().getHostContext() as common.UIAbilityContext, false);
    });
  }
}
```

## 常见FAQ

Q：该方法可以解决哪些问题？

A：需要使用窗口实例的方法都有可能因为getLastWindow的性能损耗出现延迟性问题。例如切换页面后设置的横竖屏切换没有触发，频繁切换页面导致设置的隐私模式或沉浸式效果失效之类的问题。
