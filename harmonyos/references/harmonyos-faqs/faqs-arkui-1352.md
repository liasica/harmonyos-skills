---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1352
title: 如何实现在多个页面不同位置复用同一个子窗口
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何实现在多个页面不同位置复用同一个子窗口
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6bdbda0173afce44eeaa06fbf3ae4e05d2ed7b4c79979d57be34fd6aa05e6f4e
---

## 问题现象

为了提高子窗口复用性，Index页面和PageA页面复用同一个子窗口。在Index页面中，子窗口位于TabBar边缘的上方；在PageA页面中，子窗口位于当前页面的底部。如何实现该效果？

## 背景知识

HarmonyOS中通过[createSubWindow](../harmonyos-references/arkts-apis-window-windowstage.md#createsubwindow9)方法来创建子窗口，子窗口在创建时，可以通过[moveWindowTo](../harmonyos-references/arkts-apis-window-window.md#movewindowto9-1)方法来确定子窗口的初始位置，此方法用于移动窗口位置，子窗口创建之后即可以使用[window.findWindow](../harmonyos-references/arkts-apis-window-f.md#windowfindwindow9)来查找name所对应的窗口。

## 解决方案

* 将子窗口封装到类里面，任何页面均可以引用此类来调用此子窗口。

  ```screen
  // Until.ets封装的子窗口类
  import { common } from '@kit.AbilityKit';
  import { window } from '@kit.ArkUI';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  export class Loading {
    win: window.Window | undefined = undefined;

    OpenSubWindows(UIContext: UIContext) {
      (UIContext?.getHostContext() as common.UIAbilityContext).windowStage.createSubWindow('FloatPage',
        (err, windowClass) => {
          if (err.code > 0) {
            hilog.error(0x0000, 'testTag', '%{public}s', `failed to create subWindow Cause: ${err.message}`);
            return;
          }
          this.win = windowClass;
          try {
            // 设置子窗口加载页
            windowClass.setUIContent('pages/FloatPage', () => {
              windowClass.setWindowBackgroundColor('#00000000');
            });
            // 设置子窗口左上角坐标
            windowClass.moveWindowTo(0, 2285);
            // 设置子窗口大小
            windowClass.resize(1260, 200);
            // 展示子窗口
            windowClass.showWindow();
          } catch (err) {
            hilog.error(0x0000, 'testTag', '%{public}s', `failed to create subWindow Cause:${err}`);
          }
        });
    }

    CloseSubWindows() {
      this.win?.destroyWindow();
    }
  }

  export default new Loading();
  ```
* 主页面跳转到子页面时，使用window.findWindow方法获取到子窗口，再使用moveWindowTo方法在子页面刚加载时调整子窗口的位置。

  ```screen
  // PageA.ets子页面
  import { window } from '@kit.ArkUI';
  import Loading from './Until';

  @Entry
  @Component
  struct PageA {
    floatWindow: window.Window = window.findWindow('FloatPage');

    aboutToAppear(): void {
      this.floatWindow.moveWindowTo(0, 2500);
    }

    build() {
      Column()
        .width('100%')
        .height('100%')
        .backgroundColor('#5291FF')
        .onClick(() => {
          this.getUIContext().getRouter().back();
          Loading.CloseSubWindows();
        });
    }
  }
  ```
* 切回到主页面时，需要删除子窗口，重新生成子窗口，同时子窗口的位置恢复到默认值。

  ```screen
  // SharedModalAcrossPages.ets主页面
  import Loading from './Until';

  @Entry
  @Component
  struct SharedModalAcrossPages {
    @State currentIndex: number = 0;
    @State selectedIndex: number = 0;
    private controller: TabsController = new TabsController();

    aboutToAppear(): void {
      Loading.OpenSubWindows(this.getUIContext());
    }

    build() {
      Column() {
        Tabs({ barPosition: BarPosition.End, index: this.currentIndex, controller: this.controller }) {
          TabContent() {
            Column()
              .width('100%')
              .height('100%')
              .backgroundColor('#00CB87')
              .onClick(() => {
                Loading.OpenSubWindows(this.getUIContext());
              })
              .onVisibleAreaChange([0.0, 1.0], (isVisible: boolean, currentRatio: number) => {
                if (isVisible && currentRatio >= 1.0) {
                  Loading.OpenSubWindows(this.getUIContext());
                }
                if (!isVisible && currentRatio <= 0.0) {
                  console.info('新闻页隐藏了');
                }
              });
          }.tabBar('内容0');

          TabContent() {
            Column().width('100%').height('100%').backgroundColor('#007DFF');
          }.tabBar('内容1');

          TabContent() {
            Column().width('100%').height('100%').backgroundColor('#FFBF00');
          }.tabBar('内容2');

          TabContent() {
            Column().width('100%').height('100%').backgroundColor('#E67C92');
          }.tabBar('内容3');
        }
        .vertical(false)
        .barMode(BarMode.Fixed)
        .barHeight(56)
        .animationDuration(400)
        .onChange((index: number) => {
          // currentIndex控制TabContent显示页签
          this.currentIndex = index;
          this.selectedIndex = index;
        })
        .onAnimationStart((index: number, targetIndex: number) => {
          if (index === targetIndex) {
            return;
          }
          // selectedIndex控制自定义TabBar内Image和Text颜色切换
          this.selectedIndex = targetIndex;
        })
        .height('100%')
        .backgroundColor('#F1F3F5');
      }.width('100%');
    }
  }
  ```
* 根据需求自定义子窗口页面内容。

  ```screen
  //  FloatPage.ets子窗口页面
  import { common } from '@kit.AbilityKit';
  import Loading from './Until';

  @Entry
  @Component
  struct FloatPage {
    private message: string = '浮窗页面';
    private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

    onBackPress() {
      Loading.CloseSubWindows();
      return true;
    }

    build() {
      Row() {
        Text(this.message)
          .fontSize(15)
          .fontWeight(FontWeight.Bold)
          .margin({ left: '16vp' });
        Button('跳转新页面')
          .onClick(() => {
            const mainR = this.context.windowStage.getMainWindowSync()
              .getUIContext()
              .getRouter();
            mainR.pushUrl({
              url: 'pages/PageA'
            });
          });

        Blank();
        Button('关闭子窗口')
          .onClick(() => {
            Loading.CloseSubWindows();
          })
          .margin({ right: '16vp' });
      }
      .width('100%')
      .height(50)
      .backgroundColor('#FFFFFF');
    }
  }
  ```

## 常见FAQ

Q：在子窗口使用router.pushUrl跳转到其他主窗口时，页面为什么显示在子窗口内？

A：此时焦点在子窗口，需要先获取主窗口router的方法再跳转页面。

Q：子窗口层级高于模态转场，如何避免模态转场被子窗口遮挡？

A：全模态或半模态转场弹出时，关闭子窗口即可。

Q：多个子窗口该如何区别是哪个子窗口？

A：可以根据windowClass.getWindowProperties().name获取子窗口名称去判断。
