---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-969
title: 如何监听应用进入多任务
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何监听应用进入多任务
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:00660eb155dcc2eb42d8f1434e9c4e7c3dd602e7be4799de66c6f9e5c831261d
---

## 问题现象

应用开发中一些场景（比如切屏）需要监听是否进入多任务界面，如何监听应用进入多任务呢？

## 背景知识

* [on('windowStageEvent')](../harmonyos-references/arkts-apis-window-windowstage.md#onwindowstageevent9)：开启WindowStage生命周期变化的监听。
* [WindowStageEventType](../harmonyos-references/arkts-apis-window-e.md#windowstageeventtype9)：WindowStage生命周期状态枚举。
* [@Watch](../harmonyos-guides/arkts-watch.md)应用于对状态变量的监听。如果开发者需要关注某个状态变量的值是否改变，可以使用@Watch为状态变量设置回调函数。

## 解决方案

当上划应用时，会触发WindowStageEventType.PAUSED，松开时会触发WindowStageEventType.RESUMED。可以通过状态变量来记录是否触发PAUSED，并通过@Watch监听状态变量变化来处理不同业务逻辑。示例代码如下：

* EntryAbility.ets：onWindowStageCreate中进行生命周期监听，并记录是否触发PAUSED（isPaused）。

  ```ts
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    try {
      this.context.windowStage.on('windowStageEvent', (data) => {
        let stageEventType: window.WindowStageEventType = data;
        switch (stageEventType) {
          case window.WindowStageEventType.RESUMED: // 前台可交互状态，如从多任务界面返回应用
            console.info(`windowStage resumed. false`);
            AppStorage.setOrCreate('isPaused', false);
            break;
          case window.WindowStageEventType.PAUSED: // 前台不可交互状态，如进入多任务界面
            console.info(`windowStage paused. true`);
            AppStorage.setOrCreate('isPaused', true);
            break;
          default:
            break;
        }
      });
    } catch (exception) {
      console.error(`Failed to enable the listener for window stage event changes. Cause: ${JSON.stringify(exception)}`);
    }
    console.info(`Ability onWindowStageCreate`);

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
  }
  ```
* Index.ets：监听isPaused状态变量变化，处理不同业务逻辑。

  ```ts
  import { common } from '@kit.AbilityKit';

  @Entry
  @Component
  struct Index {
    @State message: string = 'Hello World';
    context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    @Watch('onChange') @StorageLink('isPaused') isPaused: boolean | undefined = AppStorage.get('isPaused');

    onChange() {
      if (this.isPaused) {
        this.message = 'Paused';
      } else {
        this.message = 'Resume';
      }
    }

    build() {
      RelativeContainer() {
        Text(this.message)
          .id('Page2HelloWorld')
          .fontSize(50)
          .fontColor(Color.Black)
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          });
      };
    }
  }
  ```

## 常见FAQ

Q：应用冷启动之后是否会触发WindowStageEventType.RESUMED？

A：由于应用冷启动不属于应用恢复到前台可交互状态，因此不会触发WindowStageEventType.RESUMED。应用冷启动之后会触发WindowStageEventType.SHOWN，可通过监听此状态实现相关业务逻辑。
