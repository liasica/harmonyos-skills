---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-676
title: 如何解决防截屏失效问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决防截屏失效问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e55859112e724226bf4c6ee1417beaaf96ec69045fd32983556d6b601dbb5708
---

## 问题现象

应用引入一个三方SDK实现全局防截屏功能，又在登录页面单独设置进入页面开启隐私模式，离开页面取消。离开登录页面后，全局防截屏功能失效。

## 背景知识

* [@ohos.window（窗口）](../harmonyos-references/js-apis-window.md)：窗口提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。
* [setWindowPrivacyMode](../harmonyos-references/arkts-apis-window-window.md#setwindowprivacymode9)：设置窗口是否为隐私模式，使用callback异步回调。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。此接口可用于禁止截屏/录屏的场景。
* 设置窗口禁止截屏可参考[如何实现防截屏功能](faqs-arkui-3.md)。

## 问题定位

防截屏功能是通过设置窗口为隐私模式实现的。防截屏功能失效，需要检查离开登录页面后窗口的隐私模式属性是否生效。

## 分析结论

SDK通过设置主窗口为隐私模式实现防截屏，启动应用时全局可防截屏。进入登录页面后，页面开启隐私模式，离开登录页面后取消隐私模式。离开登录页面时取消隐私模式的操作导致SDK设置的主窗口隐私模式被取消，因此全局防截屏失效。

## 修改建议

在进入登录页面时通过[getWindowProperties()](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9).isPrivacyMode获取当前窗口的隐私模式状态并保存，在离开登录页面时恢复窗口隐私模式状态。示例代码如下：

* module.json5添加隐私窗口权限：

  ```screen
  "requestPermissions": [
    {
      "name": "ohos.permission.PRIVACY_WINDOW",
      "reason": "$string:app_name"
    }
  ],
  ```
* EntryAbility设置主窗口为隐私窗口，实现全局防截屏：

  ```screen
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
      // Main window is created,set main page for this ability
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
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
      });

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
* 由于EntryAbility设置主窗口为隐私窗口，主窗口禁止被截屏：

  ```screen
  @Entry
  @Component
  struct Index {
    private pagePath: NavPathStack = new NavPathStack();

    build() {
      Navigation(this.pagePath) {
        Column() {
          Button('PrivacyWindow')
            .onClick(() => {
              this.pagePath.pushPathByName('PageOne', false);
            });
        };
      }
      .mode(NavigationMode.Stack)
      .hideTitleBar(true)
      .hideToolBar(true);
    }
  }
  ```
* PageOne.ets设置不允许截屏，返回主窗口重置已记录的主窗口状态：

  ```screen
  import { common } from '@kit.AbilityKit';
  import { window } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';

  // 跳转页面入口函数
  @Builder
  export function PageOneBuilder() {
    PageOne();
  }

  // 设置页面隐私窗口状态类
  class windowUtils {
    static setWindowPrivacyModeInPage(context: common.UIAbilityContext, isFlag: boolean) {
      window.getLastWindow(context).then((lastWindow) => {
        lastWindow.setWindowPrivacyMode(isFlag, (err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error(`Failed to set the window to privacy mode. Cause: ${errCode}`);
            return;
          }
          console.info('Succeeded in setting the window to privacy mode.');
        });
      });
    }
  }

  @Entry
  @Component
  struct PageOne {
    pathStack: NavPathStack = new NavPathStack();
    context = this.getUIContext().getHostContext();
    @State windowState: boolean = false;

    @Builder
    pageOne() {
      Column({ space: 10 }) {
        Text('This is PageOne');

        Button('Pop上一页')
          .onClick(() => {
            this.pathStack.pop({ a: 'aaa' });
          });

      };
    }

    build() {
      NavDestination() {
        this.pageOne();
      }
      .title('PageOne')
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
      })
      .onWillShow(() => {
        window.getLastWindow(this.getUIContext().getHostContext()).then(win => {
          console.info(`win.getWindowProperties().isPrivacyMode:${win.getWindowProperties().isPrivacyMode}`);
          // 获取并保存窗口隐私模式状态
          this.windowState = win.getWindowProperties().isPrivacyMode;
        });

        windowUtils.setWindowPrivacyModeInPage(this.getUIContext().getHostContext() as Context as common.UIAbilityContext,
          true);
      })
      .onWillHide(() => {
        // 恢复窗口隐私模式状态
        windowUtils.setWindowPrivacyModeInPage(this.getUIContext().getHostContext() as Context as common.UIAbilityContext,
          this.windowState);
      });
    }
  }
  ```

## 总结

当设置主窗口为隐私模式实现全局防截屏时，无需再在登录页面重复设置页面防截屏。此场景适合在企微等办公软件的通用版中使用，无需针对不同的防截屏策略重复修改工程代码。
