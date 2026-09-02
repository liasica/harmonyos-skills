---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-55
title: 如何通过无感监听实现Navigation根页面的埋点监听
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 如何通过无感监听实现Navigation根页面的埋点监听
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:7909986309918080086a1bc5d50ae54bab11ac5d5d5661cef7a1bae1294c9b16
---

## 问题现象

场景：Navigation组件根页面相比NavDestination更特殊，如何实现对于Navigation根页面的监听操作。

## 背景知识

* [@ohos.arkui.observer(无感监听)](../harmonyos-references/js-apis-arkui-observer.md)：提供UI组件行为变化的无感监听能力。当你需要在数据发生变化时自动更新UI而不需要手动调用更新方法时，如页面生命周期、组件显隐状态、滚动事件等。通过使用@ohos.arkui.observer装饰器标记的状态或属性，当其值发生改变时，所有依赖于它的组件会自动接收到通知并进行相应的更新操作。
* [组件导航(Navigation)](../harmonyos-guides/arkts-navigation-navigation.md)：主要用于实现Navigation页面即NavDestination页面间的跳转，支持在不同Navigation页面间传递参数，提供灵活的跳转栈操作，从而更便捷地实现对不同页面的访问和复用。

## 解决方案

对于[Navigation组件](../harmonyos-references/ts-basic-components-navigation.md)实现路由的方案，实现页面监听时，由于NavDestination组件本身提供了各个生命周期的回调，例如onWillAppear、onWillDisappear、onWillShow、onWillHide等，对于NavDestination子页面的监听操作可以直接通过这些生命周期回调来进行统计。

但[Navigation组件](../harmonyos-references/ts-basic-components-navigation.md)并未提供这些生命周期回调，根页面无法利用这些回调来进行监听；单纯依赖组件本身的生命周期回调如aboutToAppear、aboutToDisappear等，也无法完整监听到根页面状态变化，并且对于一些特殊情况（应用前后台切换等）难以处理，仅依靠生命周期回调难以实现对包含根页面在内的所有页面状态变化的监听。

而无感监听实现能够同时监听router页面状态变化和NavDestination页面的状态变化，且可以同时监听多个[Navigation组件](../harmonyos-references/ts-basic-components-navigation.md)的页面，相比直接利用生命周期回调实现，功能更强大且能够更集中的处理监听逻辑和监听数据的统计。

[Navigation组件](../harmonyos-references/ts-basic-components-navigation.md)所在的根页面不会进入路由栈中，根页面的状态变化不会触发该事件，无法按照NavDestination页面的处理方式进行处理。同时也需要考虑如根页面与其他页面间的跳转、应用前后台切换时导致页面状态变化的特殊情况，因此需要对根页面的监听操作做额外处理。

具体处理如下：

1. 监听routerPageUpdate事件，即调用[uiObserver.on('routerPageUpdate')](../harmonyos-references/js-apis-arkui-observer.md#uiobserveronrouterpageupdate)，根页面初始化以及应用触发前后台切换时，实际会触发routerPageUpdate事件，为保证能够监听根页面初次访问时的状态变化，以及应用前后台切换时的状态变化，需要额外监听routerPageUpdate事件：

   ```ts
   this.uiObserver.on('routerPageUpdate', (info: uiObserver.RouterPageInfo) => {
     // 非当前Navigation页面过滤，避免干扰
     if (info.name !== 'pages/Index') {
       return;
     }
     if (info.state === uiObserver.RouterPageState.ABOUT_TO_APPEAR) {
       // 根页初次加载时会触发该状态，可在此记录首页访问次数等数据
       let accessCount = AppStorage.get<number>('rootCount') ?? 0;
       accessCount++;
       AppStorage.setOrCreate('rootCount', accessCount);
     }
     if (info.state === uiObserver.RouterPageState.ABOUT_TO_DISAPPEAR) {
       // 页面销毁时触发，可在此重置状态
       this.startTime = 0;
     }
     // 处理页面前后台切换，这里需要注意当应用前后台切换时，无论当前展示的页面是否为根页，首页都会触发一次routerPageUpdate事件
     if (info.state === uiObserver.RouterPageState.ON_PAGE_SHOW && this.isTop) {
       // 应用从后台切换至前台时，首页触发一次该状态，此时需要根据根页是否为最上层展示页面来做进一步处理，这里通过isTop变量记录首页是否在最上层
       this.startTime = Date.now();
     }
     if (info.state === uiObserver.RouterPageState.ON_PAGE_HIDE && this.isTop) {
       // 应用从前台切换至后台时，首页触发一次该状态，此时同样需要根据根页是否为最上层展示页面来做进一步处理
       let duration = Date.now() - this.startTime;
       AppStorage.setOrCreate('rootTime', Math.round((duration + this.preTime)/1000));
       this.preTime += duration;
     }
   });
   ```

2. 注册页面切换事件监听，即调用[uiObserver.on('navDestinationSwitch')](../harmonyos-references/js-apis-arkui-observer.md#uiobserveronnavdestinationswitch12)，监听navDestinationSwitch事件是为了正常处理根页面与其他页面间的跳转，当根页面跳转至其他子页面或者其他子页面返回到根页面时并不会触发routerPageUpdate事件，只能依靠navDestinationSwitch页面切换事件进行处理：

   ```ts
   this.uiObserver.on('navDestinationSwitch', (info: uiObserver.NavDestinationSwitchInfo) => {
     if (info.from === 'navBar') {
       // 这里代表从根页面跳转至其他页面，根页面将被隐藏，可以在此处标记根页面是否被隐藏，方便后续处理
       this.isTop = false;
       let duration = this.startTime === 0 ? 0 : Date.now() - this.startTime;
       AppStorage.setOrCreate('rootTime', Math.round((duration + this.preTime) / 1000));
       this.preTime += duration;
     }
     if (info.to === 'navBar') {
       // 回到根页面，根页面将重新展示
       this.isTop = true;
       this.startTime = Date.now();
     }
   });
   ```
3. 对于事件监听注册的位置，由于需要在根页面加载前注册，建议放在EntryAbility-onWindowStageCreate回调中注册，在windowStage.loadContent的回调中可获取到主窗口对象及其对应的UIContext，然后通过UIContext获取UIObserver对象即可；

   注销事件监听时，在监听事件不再使用时及时注销，释放系统资源即可，在不考虑Navigation嵌套的情况下，可以在onWindowStageDestroy回调中注销事件监听，具体位置可根据实际情况调整。

完整代码：

```ts
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { uiObserver, UIObserver, window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  uiObserver?: UIObserver;
  startTime: number = 0;
  preTime: number = 0;
  isTop: boolean = true;

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', `Ability onCreate ${want.abilityName} ${launchParam.launchReasonMessage}`);
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
      let uiContext = windowStage.getMainWindowSync().getUIContext();
      // 这里保存uiObserver对象，方便后续注销订阅时使用
      this.uiObserver = uiContext.getUIObserver();
      this.uiObserver.on('navDestinationSwitch', (info: uiObserver.NavDestinationSwitchInfo) => {
        if (info.from === 'navBar') {
          // 这里代表从根页面跳转至其他页面，根页面将被隐藏，可以在此处标记根页面是否被隐藏，方便后续处理
          this.isTop = false;
          let duration = this.startTime === 0 ? 0 : Date.now() - this.startTime;
          AppStorage.setOrCreate('rootTime', Math.round((duration + this.preTime) / 1000));
          this.preTime += duration;
        }
        if (info.to === 'navBar') {
          // 回到根页面，根页面将重新展示
          this.isTop = true;
          this.startTime = Date.now();
        }
      });
      this.uiObserver.on('routerPageUpdate', (info: uiObserver.RouterPageInfo) => {
        // 非当前Navigation页面过滤，避免干扰
        if (info.name !== 'pages/Index') {
          return;
        }
        if (info.state === uiObserver.RouterPageState.ABOUT_TO_APPEAR) {
          // 根页初次加载时会触发该状态，可在此记录首页访问次数等数据
          let accessCount = AppStorage.get<number>('rootCount') ?? 0;
          accessCount++;
          AppStorage.setOrCreate('rootCount', accessCount);
        }
        if (info.state === uiObserver.RouterPageState.ABOUT_TO_DISAPPEAR) {
          // 页面销毁时触发，可在此重置状态
          this.startTime = 0;
        }
        // 处理页面前后台切换，这里需要注意当应用前后台切换时，无论当前展示的页面是否为根页，首页都会触发一次routerPageUpdate事件
        if (info.state === uiObserver.RouterPageState.ON_PAGE_SHOW && this.isTop) {
          // 应用从后台切换至前台时，首页触发一次该状态，此时需要根据根页是否为最上层展示页面来做进一步处理，这里通过isTop变量记录首页是否在最上层
          this.startTime = Date.now();
        }
        if (info.state === uiObserver.RouterPageState.ON_PAGE_HIDE && this.isTop) {
          // 应用从前台切换至后台时，首页触发一次该状态，此时同样需要根据根页是否为最上层展示页面来做进一步处理
          let duration = Date.now() - this.startTime;
          AppStorage.setOrCreate('rootTime', Math.round((duration + this.preTime)/1000));
          this.preTime += duration;
        }
      });
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
    this.uiObserver?.off('navDestinationSwitch');
    this.uiObserver?.off('routerPageUpdate');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

```ts
@Entry
@Component
struct Index {
  @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();
  @State timeText: string = '00 : 00 : 00';
  @StorageProp('rootTime') rootTime: number = 0;
  @StorageProp('rootCount') rootCount: number = 0;
  hours: number = 0;
  minutes: number = 0;
  seconds: number = 0;
  timeId: number = -1;

  aboutToAppear() {
    this.timeId = setInterval(() => {
      this.countTime();
    }, 1000);
  }

  aboutToDisappear(): void {
    clearInterval(this.timeId);
  }

  build() {
    Navigation(this.pathStack) {
      Column({space: 20}) {
        Text(this.timeText)
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
        Column({ space: 16 }) {
          Button('第一页', { type: ButtonType.Capsule })
            .width('50%')
            .height(40)
            .onClick(() => {
              this.pathStack.pushPath({ name: 'PageOne' });
            })
          Button('第二页', { type: ButtonType.Capsule })
            .width('50%')
            .height(40)
            .onClick(() => {
              this.pathStack.pushPath({ name: 'PageTwo' });
            })
          Button('第三页', { type: ButtonType.Capsule })
            .width('50%')
            .height(40)
            .onClick(() => {
              this.pathStack.pushPath({ name: 'PageThree' });
            })
        }.width('100%')

        Column({ space: 10 }) {
          Text() {
            Span('首页访问次数：')
            Span(this.rootCount.toString())
            Span('次')
          }.fontSize(18)
          Text() {
            Span('首页访问时长：')
            Span(this.rootTime.toString())
            Span(' s')
          }.fontSize(18)
        }.width('100%')
      }.width('100%')
      .height('100%')
      .justifyContent(FlexAlign.SpaceEvenly)
    }.hideToolBar(true)
    .id('IndexNavigation')
  }

  /**
   * 计算时间
   */
  countTime() {
    this.seconds++;
    if (this.seconds >= 60) {
      this.minutes++;
      this.seconds = 0;
    }
    if (this.minutes >= 60) {
      this.hours++;
      this.minutes = 0;
    }
    this.timeText = this.formatTime();
  }

  formatTime() {
    return `${this.getTwoMoreDigitStyle(this.hours)} : ${this.getTwoMoreDigitStyle(this.minutes)} : ${this.getTwoMoreDigitStyle(this.seconds)}`;
  }

  getTwoMoreDigitStyle(num: number) {
    if (num < 10) {
      return `0${num}`;
    } else {
      return num.toString();
    }
  }
}
```

## 常见FAQ

Q：实现页面相关的无感监听事件有哪些。

A：监听页面切换事件('navDestinationSwitch')、监听页面状态变化事件('navDestinationUpdate')、监听router中page页面的状态变化事件('routerPageUpdate')。

Q：如果需要上报监听到的数据，如何实现。

A：可参考[最佳实践-应用埋点](../best-practices/bpta-application-track-practice.md)。
