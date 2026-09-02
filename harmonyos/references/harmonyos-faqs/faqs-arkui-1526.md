---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1526
title: 如何设置窗口或页面透明背景色
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何设置窗口或页面透明背景色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:b3ae43283866a0b5239155b7f3c0ea106f13518e2ea6e7385f9f0711b3d80122
---

## 问题现象

在设计手机软件或应用程序时，需要将某些窗口或页面的背景设置为透明。实现这一效果的方法有哪些？

## 背景知识

* [setWindowBackgroundColor](../harmonyos-references/arkts-apis-window-window.md#setwindowbackgroundcolor9)用于设置窗口的背景色，可传入带有透明度的颜色值。
* [getMainWindow](../harmonyos-references/arkts-apis-window-windowstage.md#getmainwindow9)：获取该WindowStage实例下的主窗口，使用callback异步回调。
* [window.getLastWindow](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)：获取当前应用内最上层的子窗口，若无应用子窗口，则返回应用主窗口，使用callback异步回调。
* [NavDestinationMode](../harmonyos-references/ts-basic-components-navdestination.md#navdestinationmode枚举说明11)：将NavDestination类型设置为DIALOG时，默认透明，进出页面栈不影响下层NavDestination的生命周期。

## 解决方案

将手机窗口或页面背景设为透明，有以下三种解决方案：

* 方案一：在EntryAbility.ets页面在windowStage.getMainWindow()方法中通过setWindowBackgroundColor设置其背景色即可。

  ```ts
  import { UIAbility } from '@kit.AbilityKit';
  import { window } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';

  export default class EntryAbility extends UIAbility {
    onDestroy(): void {
    }

    onWindowStageCreate(windowStage: window.WindowStage): void {
      // Main window is created, set main page for this ability
      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          return;
        }
        windowStage.getMainWindow(async (err: BusinessError, data) => {
          // 设置窗口背景色
          if (err) {
          }
          data.setWindowBackgroundColor('#00000000');

        });
      });
    }

    onWindowStageDestroy(): void {
      // Main window is destroyed, release UI related resources
    }

    onForeground(): void {
      // Ability has brought to foreground
    }

    onBackground(): void {
      // Ability has back to background
    }
  };
  ```
* 方案二：在目标页面onPageShow()中先通过window.getLastWindow()方法获取窗口再使用setWindowBackgroundColor设置其背景色实现。

  ```ts
  import { window } from '@kit.ArkUI';

  @Entry
  @Component
  struct Index {
    private message: string = 'Hello World';
    uiContext = this.getUIContext();

    // 在onPageShow()生命周期中设置窗口背景颜色
    onPageShow(): void {
      window.getLastWindow(this.uiContext?.getHostContext(), (err, data) => {
        data.setWindowBackgroundColor('#00000000');
      });
    }

    build() {
      RelativeContainer() {
        Text(this.message)
          .id('Page2HelloWorld')
          .fontSize(50)
          .fontColor(Color.White)
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          });
      };
    }
  }
  ```

  注：如若想实现打开一个具有透明背景的子窗口也可使用setWindowBackgroundColor方法实现。

  方案一、方案二示例效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/YTu5pnC5Qbeu9yGdxu5lNQ/zh-cn_image_0000002675345105.png "点击放大")
* 方案三：如果页面使用了NavDestination，将其模式设置为DIALOG可实现背景透明的效果。

  ```ts
  import { SymbolGlyphModifier } from '@kit.ArkUI';

  @Component
  struct MyPageTwo {
    private listScroller: Scroller = new Scroller();
    private arr: number[] = [];

    aboutToAppear(): void {
      for (let i = 0; i < 5; i++) {
        this.arr.push(i);
      }
    }

    build() {
      NavDestination() {
        List({ scroller: this.listScroller }) {

        }
        .width('100%');
      }
      .backgroundColor('rgba(200,200,200,0.4)')
      // 设置NavDestination的模式为DIALOG模式。
      .mode(NavDestinationMode.DIALOG)
      .title('PageTwo', { backgroundColor: 'rgba(10, 89, 247, 0.1)', barStyle: BarStyle.STACK })
      .toolbarConfiguration([
        {
          value: 'item1',
          symbolIcon: new SymbolGlyphModifier($r('sys.symbol.phone_badge_star'))
        }
      ],
        { backgroundColor: 'rgba(10, 89, 247, 0.1)', barStyle: BarStyle.STACK })
      // 绑定可滚动容器组件
      .bindToScrollable([this.listScroller]);
    }
  }

  @Entry
  @Component
  struct Index {
    private stack: NavPathStack = new NavPathStack();

    @Builder
    MyPageMap(name: string) {
      if (name === 'myPageTwo') {
        MyPageTwo();
      }
    }

    build() {
      Navigation(this.stack) {
        RelativeContainer() {
          Button('push PageTwo')
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })

            .onClick(() => {
              this.stack.pushPath({ name: 'myPageTwo' });
            });
        }
        .height('40%');

      }
      .width('100%')
      .height('100%')
      .mode(NavigationMode.Stack)
      .title({ main: 'MainTitle', sub: 'subTitle' })
      .navDestination(this.MyPageMap)
      .backgroundColor('rgba(241, 243, 245, 1.00)');
    }
  }
  ```

  方案三示例效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/ZyYfSrUnS5m4o_HJcELuHA/zh-cn_image_0000002645185340.png "点击放大")

## 总结

方案一、二都是使用[setWindowBackgroundColor](../harmonyos-references/arkts-apis-window-window.md#setwindowbackgroundcolor9)方法实现，但具体应用场景不同。请参考如下表格：

| 方案 | 适用场景 |
| --- | --- |
| 方案一 | 将所有页面背景色设置为透明效果，由于安全因素，全屏时表现为高斯模糊效果，应用上滑到设备右上角进入悬浮窗时，可表现为完全透明 |
| 方案二 | 将指定页面背景设置为透明效果，由于安全因素，全屏时表现为高斯模糊效果，对应页面上滑到设备右上角进入悬浮窗时，可表现为完全透明 |
| 方案三 | 使用NavDestination进行页面管理，将页面设置为透明效果 |

## 常见FAQ

Q：如何实现应用页面背景色完全透明的效果？

A：目前在PC和平板的自由多窗模式下应用子窗口可以实现完全透明，其他设备和主窗口不可设置背景色完全透明。实现PC和平板自由多窗模式下完全透明可参考[如何设置PC窗口透明](faqs-computer-9.md)。
