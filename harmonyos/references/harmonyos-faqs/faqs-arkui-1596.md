---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1596
title: 如何判断当前是否处于自由多窗及监听自由多窗切换
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何判断当前是否处于自由多窗及监听自由多窗切换
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c62a40285d54e7e3a9c2e8f6c3480877fab76a07c0636d54edbbd940045b3809
---

## 问题现象

* **场景一**：非自由多窗模式下打开应用窗口后切换到自由多窗模式，界面底部导航栏和页面状态栏会出现留白。
* **场景二**：自由多窗下打开应用窗口，关闭自由多窗，此时界面底部导航栏和顶部状态栏有重叠。

## 背景知识

* [自由多窗模式](../best-practices/bpta-multi-device-window-mode.md#section151195853214)：自由多窗是一种多窗口显示模式，它允许用户在同一时间、同一屏幕上同时运行多个应用窗口。开发者可以使用"window\_pcmode\_switch\_status"字段结合[settings.registerKeyObserver()](../harmonyos-references/js-apis-settings.md#settingsregisterkeyobserver11)接口和[settings.getValue()](../harmonyos-references/js-apis-settings.md#settingsgetvalue10)接口来获取并监听当前是否切换至自由多窗模式。
* [isInFreeWindowMode](../harmonyos-references/arkts-apis-window-window.md#isinfreewindowmode22)：查询当前窗口是否为自由窗口模式，该接口支持API22及以上版本。
* [on('freeWindowModeChange')](../harmonyos-references/arkts-apis-window-window.md#onfreewindowmodechange22)：开启自由窗口模式变化事件的监听，该接口支持API22及以上版本。
* [padding](../harmonyos-references/ts-universal-attributes-size.md#padding)：设置组件的内边距属性。

## 问题定位

* 排查应用中是否调用了settings.registerKeyObserver()接口和settings.getValue()接口来获取并监听当前是否切换至自由多窗模式。
* 排查应用是否实现了沉浸式布局以及根组件中是否设置padding属性用于动态设置状态栏和底部导航栏避让区域。
* 排查应用是否在监听自由多窗切换模式中动态设置状态栏和底部导航栏避让区域。

## 分析结论

* 应用未调用settings.registerKeyObserver()和settings.getValue()接口来监听自由多窗模式切换状态。
* 应用虽然使用了沉浸式窗口布局，但未在根组件设置padding属性来处理状态栏和导航栏的避让。
* 应用中使用了沉浸式效果窗口全屏布局方案，根组件也设置padding属性用于动态设置状态栏和底部导航栏避让区域。但是没有在settings.registerKeyObserver()接口和settings.getValue()接口的回调中判断当前是否开启自由多窗模式来动态设置状态栏和底部导航栏避让区域。

## 修改建议

* **方案一**：使用"window\_pcmode\_switch\_status"字段结合settings.registerKeyObserver()接口和settings.getValue()接口来获取并监听当前是否切换至自由多窗模式。当应用开启自由多窗模式时，将根组件设置的padding属性值清空，防止因为开启沉浸式模式界面底部导航栏和页面状态栏有留白。当应用关闭自由多窗模式时，开启沉浸式模式并且根组件动态设置padding属性值用于动态设置状态栏和底部导航栏避让区域，完整示例参考如下：

  ```ts
  import { settings } from '@kit.BasicServicesKit';
  import { window } from '@kit.ArkUI';

  @Entry
  @Component
  struct TabsExample {
    private controller: TabsController = new TabsController();
    @StorageProp('bottomRectHeight')
    bottomRectHeight: number = 0;
    @StorageProp('topRectHeight')
    topRectHeight: number = 0;
    private context = this.getUIContext().getHostContext();

    aboutToAppear(): void {
      //初次获取当前的状态
      this.getMode();
      // 监听当前是否切换至自由多窗模式
      settings.registerKeyObserver(this.context, 'window_pcmode_switch_status', settings.domainName.USER_PROPERTY,
        () => {
          this.getMode();
        });
    }

    getMode() {
      settings.getValue(this.context, 'window_pcmode_switch_status', settings.domainName.USER_PROPERTY)
        .then((data) => {
          if (data) {
            this.setFullScreen(false);
            this.topRectHeight = 0;
            this.bottomRectHeight = 0;
          } else {
            this.setFullScreen(true);
            this.setSafeTop();
            this.setSafeBottom();
          }
        });
    }

    // 动态设置窗口全屏
    setFullScreen(value: boolean) {
      window.getLastWindow(this.context).then(currentWindow => {
        currentWindow.setWindowLayoutFullScreen(value);
      });
    };

    // 设置顶部状态栏避让
    setSafeTop() {
      window.getLastWindow(this.context).then(windowClass => {
        let topType = window.AvoidAreaType.TYPE_SYSTEM;
        let statusBarArea = windowClass.getWindowAvoidArea(topType);
        this.topRectHeight = statusBarArea.topRect.height;
      });
    }

    // 设置底部导航栏避让
    setSafeBottom() {
      window.getLastWindow(this.context).then(windowClass => {
        let bottomType = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR;
        let bottomArea = windowClass.getWindowAvoidArea(bottomType);
        this.bottomRectHeight = bottomArea.bottomRect.height;
      });
    }

    build() {
      Column() {
        Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
          TabContent() {
            Column() {
            }.width('100%').height('100%').backgroundColor('#F1F3F5');
          }.tabBar(BottomTabBarStyle.of($r('sys.media.AI_search'), 'Tab1'));

          TabContent() {
            Column().width('100%').height('100%').backgroundColor('#F1F3F5');
          }.tabBar(BottomTabBarStyle.of($r('sys.media.AI_phone'), 'Tab2'));

          TabContent() {
            Column().width('100%').height('100%').backgroundColor('#F1F3F5');
          }.tabBar(BottomTabBarStyle.of($r('sys.media.AI_play'), 'Tab3'));

          TabContent() {
            Column().width('100%').height('100%').backgroundColor('#F1F3F5');
          }.tabBar(BottomTabBarStyle.of($r('sys.media.AI_playing'), 'Tab4'));
        }
        .width('100%')
        .height('100%')
        .backgroundColor('#F1F3F5')
        // top数值与状态栏区域高度保持一致；bottom数值与导航区域高度保持一致
        .padding({
          top: this.getUIContext().px2vp(this.topRectHeight),
          bottom: this.getUIContext().px2vp(this.bottomRectHeight)
        });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
* **方案二**：通过isInFreeWindowMode和on('freeWindowModeChange')来获取并监听当前是否切换至自由多窗模式，当应用开启自由多窗模式时，将根组件设置的padding属性值清空，防止因为开启沉浸式模式界面底部导航栏和页面状态栏有留白。当应用关闭自由多窗模式时，开启沉浸式模式并且根组件动态设置padding属性值用于动态设置状态栏和底部导航栏避让区域，完整示例参考如下：

  ```ts
  import { window } from '@kit.ArkUI';

  @Entry
  @Component
  struct Page {
    private controller: TabsController = new TabsController();
    @StorageProp('bottomRectHeight')
    bottomRectHeight: number = 0;
    @StorageProp('topRectHeight')
    topRectHeight: number = 0;
    private context = this.getUIContext().getHostContext();

    aboutToAppear(): void {
      // 监听当前是否切换至自由多窗模式
      window.getLastWindow(this.context, (err: BusinessError, data) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        let isInFreeWindowMode: boolean = data.isInFreeWindowMode();
        this.configUIWithFreeWindowMode(isInFreeWindowMode);
        data.on('freeWindowModeChange', callback);

      });
      const callback = (isInFreeWindowMode: boolean) => {
        this.configUIWithFreeWindowMode(isInFreeWindowMode);
      };
    }

    configUIWithFreeWindowMode(isFreeWindowMode: boolean) {
      if (isFreeWindowMode) {
        this.setFullScreen(false);
        this.topRectHeight = 0;
        this.bottomRectHeight = 0;
      } else {
        this.setFullScreen(true);
        this.setSafeTop();
        this.setSafeBottom();
      }
    }

    // 动态设置窗口全屏
    setFullScreen(value: boolean) {
      window.getLastWindow(this.context).then(currentWindow => {
        currentWindow.setWindowLayoutFullScreen(value);
      });
    };

    // 设置顶部状态栏避让
    setSafeTop() {
      window.getLastWindow(this.context).then(windowClass => {
        let topType = window.AvoidAreaType.TYPE_SYSTEM;
        let statusBarArea = windowClass.getWindowAvoidArea(topType);
        this.topRectHeight = statusBarArea.topRect.height;
      });
    }

    // 设置底部导航栏避让
    setSafeBottom() {
      window.getLastWindow(this.context).then(windowClass => {
        let bottomType = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR;
        let bottomArea = windowClass.getWindowAvoidArea(bottomType);
        this.bottomRectHeight = bottomArea.bottomRect.height;
      });
    }

    build() {
      Column() {
        Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
          TabContent() {
            Column() {
            }.width('100%').height('100%').backgroundColor('#F1F3F5');
          }.tabBar(BottomTabBarStyle.of($r('sys.media.AI_search'), 'Tab1'));

          TabContent() {
            Column().width('100%').height('100%').backgroundColor('#F1F3F5');
          }.tabBar(BottomTabBarStyle.of($r('sys.media.AI_phone'), 'Tab2'));

          TabContent() {
            Column().width('100%').height('100%').backgroundColor('#F1F3F5');
          }.tabBar(BottomTabBarStyle.of($r('sys.media.AI_play'), 'Tab3'));

          TabContent() {
            Column().width('100%').height('100%').backgroundColor('#F1F3F5');
          }.tabBar(BottomTabBarStyle.of($r('sys.media.AI_playing'), 'Tab4'));
        }
        .width('100%')
        .height('100%')
        .backgroundColor('#F1F3F5')
        // top数值与状态栏区域高度保持一致；bottom数值与导航区域高度保持一致
        .padding({
          top: this.getUIContext().px2vp(this.topRectHeight),
          bottom: this.getUIContext().px2vp(this.bottomRectHeight)
        });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
