---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-windmana-faq-0006
title: 手机应用页面透明背景设置问题排查
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 常见问题 > 手机应用页面透明背景设置问题排查
category: harmonyos-faqs
scraped_at: 2026-11-27T10:50:42+08:00
doc_updated_at: 2026-11-26
content_hash: sha256:fa32ad6798b23fbfa49ec579e70e85ea4309501931c678982a158d798735f221
---

**Q：在设计手机软件或应用程序时，需要将某些窗口或页面的背景设置为透明。实现这一效果的方法有哪些？**

**A：**将手机窗口或页面背景设为透明，有以下三种解决方案：

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

  **说明** 

  如若想实现打开一个具有透明背景的子窗口也可使用setWindowBackgroundColor方法实现。

  方案一、方案二示例效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/KvIHJSV-TZumNxYd7XIo3w/zh-cn_image_0000002796034236.png?HW-CC-KV=V1&HW-CC-Date=20261127T025042Z&HW-CC-Expire=31536000000&HW-CC-Sign=0AADB45C77C2E916A7C3EDA15056CB24A9E1C44010E7767D8CB1B7A052FB1C63 "点击放大")
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/RxlqOh0LSxm6pCTFXEpf_A/zh-cn_image_0000002824674261.png?HW-CC-KV=V1&HW-CC-Date=20261127T025042Z&HW-CC-Expire=31536000000&HW-CC-Sign=87178D3B711D3FB33B7C00F0002A9C0A451E8C0B3F6BB5B86CA8E02C78F541AA "点击放大")

**Q：如何实现应用页面背景色完全透明的效果？**

**A：**目前在PC和平板的自由多窗模式下应用子窗口可以实现完全透明，其他设备和主窗口不可设置背景色完全透明。

**Q：使用setWindowBackgroundColor设置窗口背景色后，仅在手机和平板设备上生效，请问如何设置PC窗口的背景色？**

**A：**由于PC窗口存在标题栏，因此设置PC窗口透明背景色需要setWindowBackgroundColor与setWindowContainerColor搭配使用，setWindowContainerColor设置标题栏透明，setWindowBackgroundColor设置内容区域背景色透明，方可实现整个PC窗口透明效果。示例代码如下：

* 在module.json5中配置权限。

  ```json
  "requestPermissions": [
    {
      'name': "ohos.permission.SET_WINDOW_TRANSPARENT"
    }
  ],
  ```
* 给PC窗口设置透明色（'#00000000'）。

  ```ts
  import { window } from '@kit.ArkUI';

  @Entry
  @Component
  struct Index {
    private message: string = 'Hello World';
    uiContext = this.getUIContext();

    // 在aboutToAppear()生命周期中设置PC窗口背景颜色
    aboutToAppear(): void {
      window.getLastWindow(this.uiContext?.getHostContext(), (err, data) => {
        try {
          data.setWindowBackgroundColor('#00000000');
          data.setWindowContainerColor('#00000000', '#FF000000');
        } catch (exception) {
          console.error(`Failed to set the background color. Cause code: ${exception.code}, message: ${exception.message}`);
        }
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
