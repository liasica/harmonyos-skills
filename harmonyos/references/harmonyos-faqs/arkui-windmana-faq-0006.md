---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-windmana-faq-0006
title: 如何设置窗口或页面透明背景色
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 常见问题 > 如何设置窗口或页面透明背景色
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:28+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:320834097a049d78d562a18598f2295f2296741e9b228181b4cbace14046b6b9
---

**Q：在设计手机软件或应用程序时，需要将某些窗口或页面的背景设置为透明。实现这一效果的方法有哪些？**

**A**：将手机窗口或页面背景设为透明，有以下三种解决方案：

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

  **须知** 

  如若想实现打开一个具有透明背景的子窗口也可使用setWindowBackgroundColor方法实现。

  方案一、方案二示例效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/9ozk_dalTgySl_jpOb4haw/zh-cn_image_0000002801490501.png "点击放大")
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/_heya3O1SjmPZTNF8RfSNQ/zh-cn_image_0000002772253302.png "点击放大")

**Q：如何实现应用页面背景色完全透明的效果？**

**A**：目前在PC和平板的自由多窗模式下应用子窗口可以实现完全透明，其他设备和主窗口不可设置背景色完全透明。实现PC和平板自由多窗模式下完全透明可参考[如何设置PC窗口透明](faqs-computer-9.md)。
