---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1402
title: 如何解决NavDestination切换页面后浏览位置无法保存问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决NavDestination切换页面后浏览位置无法保存问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:896bcb264815d2de2865aa6f43913cfe19a0502547e352ba331041467e7d81fa
---

## 问题现象

在HarmonyOS中，使用NavDestination实现页面跳转至其他页面后，下次进入如何保持跳转前页面的浏览位置？

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)：Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)的子组件）或非首页显示（NavDestination的子组件），首页和非首页通过路由进行切换。
* [@ohos.arkui.observer(无感监听)](../harmonyos-references/js-apis-arkui-observer.md)提供UI组件行为变化的无感监听能力。可以监听Navigation的页面切换事件进行相应操作。
* [Scroll](../harmonyos-references/ts-container-scroll.md)是一种可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* [onDidScroll](../harmonyos-references/ts-container-scroll.md#ondidscroll12)方法在Scroll滚动时触发，可用于在滑动过程中获取Scroll组件的偏移量yOffset。
* [scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)方法可用于让Scroll组件滑动到指定位置。
* [AppStorage](../harmonyos-guides/arkts-appstorage.md)是应用全局的UI状态存储，和应用的进程绑定，只能在UI主线程中使用，无法在子线程中使用、修改。

## 解决方案

* **方案一**：使用路由模式保留页面实例。

  在页面跳转时不要使用[pop](../harmonyos-references/ts-basic-components-navigation.md#pop10)和[clear](../harmonyos-references/ts-basic-components-navigation.md#clear10)等方法，否则NavDestination页面会被回收。可以采用[单例模式MOVE\_TO\_TOP\_SINGLETON](../harmonyos-references/ts-basic-components-navigation.md#launchmode12枚举说明)跳转至指定的页面，该方式会使用栈内已存在的页面实例（即浏览位置不变）。

  由于单例模式是从栈底到栈顶依次查找，当栈内存在多个同名页面实例时，会默认跳转最底层的同名页面实例，所以需确保栈内只存在一个同名实例，否则跳转的页面保留的滚动位置与上一次显示的页面会不一致（显示的是栈底同名实例保留的滚动位置）。

  ```ts
  import { PageOneS1Builder } from './PageOneS1';
  import { PageTwoS1Builder } from './PageTwoS1';

  @Entry
  @Component
  struct Solution1 {
    private pathStack: NavPathStack = new NavPathStack();

    aboutToAppear(): void {
      this.pathStack.pushPath({ name: 'PageOneS1' }); // 推送第一个子页作为首页
    }

    @Builder
    pageMap(name: string) {
      if (name === 'PageOneS1') {
        PageOneS1Builder();
      } else if (name === 'PageTwoS1') {
        PageTwoS1Builder();
      }
    }

    build() {
      Navigation(this.pathStack) {
      }
      .navDestination(this.pageMap)
      .width('100%')
      .height('100%')
      .hideNavBar(true);
    }
  }
  ```

  ```ts
  @Builder
  export function PageOneS1Builder() {
    PageOneS1();
  }

  @Component
  struct PageOneS1 {
    private pathStack: NavPathStack = new NavPathStack();
    private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];

    build() {
      NavDestination() {
        Column({ space: 20 }) {
          Row() {
            Button('跳转页面')
              .margin({ top: 20 })
              .onClick(() => {
                this.pathStack.pushPathByName('PageTwoS1', null, false);
              });
          };

          List({ space: 16 }) {
            ForEach(this.arr, (item: number) => {
              ListItem() {
                Text(item.toString())
                  .width('100%')
                  .height(100)
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .borderRadius(16)
                  .backgroundColor('#F1F3F5');
              }.width('100%');
            }, (item: string) => item);
          }.padding({ left: 12, right: 12 })
          .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
          .alignListItem(ListItemAlign.Center)
          .height('90%');
        };
      }.width('100%').height('100%')
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
      });
    }
  }
  ```

  ```ts
  @Builder
  export function PageTwoS1Builder() {
    PageTwoS1();
  }

  @Component
  struct PageTwoS1 {
    pathStack: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        Column({ space: 20 }) {
          Button('单例跳转')
            .width('30%')
            .margin('20vp')
            .onClick(() => {
              // 或者使用单例模式跳转回其它页面
              this.pathStack.pushPath({ name: 'PageOneS1' }, { launchMode: LaunchMode.MOVE_TO_TOP_SINGLETON });
            });
        }.width('100%').height('100%');
      }
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
      });
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/yXDJAXp3QBGxKf6W-K8Nvw/zh-cn_image_0000002628763134.gif "点击放大")
* **方案二**：手动保存与恢复滚动状态。

  若必须销毁页面，可通过以下步骤实现状态持久化：

  1. 在页面滚动时计算滚动距离并持久化保存。
  2. 在页面返回显示时通过AppStorage获取存储的滚动数据。
  3. 在列表组件中实时更新滚动位置。

     ```ts
     import { PageOneS2Builder } from './PageOneS2';
     import { PageTwoS2Builder } from './PageTwoS2';

     @Entry
     @Component
     struct Solution2 {
       private pathStack: NavPathStack = new NavPathStack();

       aboutToAppear(): void {
         this.pathStack.pushPath({ name: 'PageOneS2' }); // 推送第一个子页作为首页
       }

       @Builder
       pageMap(name: string) {
         if (name === 'PageOneS2') {
           PageOneS2Builder();
         } else if (name === 'PageTwoS2') {
           PageTwoS2Builder();
         }
       }

       build() {
         Navigation(this.pathStack) {
         }
         .navDestination(this.pageMap)
         .width('100%')
         .height('100%')
         .hideNavBar(true);
       }
     }
     ```

     ```ts
     import { uiObserver } from '@kit.ArkUI';

     @Builder
     export function PageOneS2Builder() {
       PageOneS2();
     }

     @Component
     struct PageOneS2 {
       pathStack: NavPathStack = new NavPathStack();
       private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
       @State offsetY: number = 0;
       private scroller: Scroller = new Scroller();

       aboutToAppear() {
         uiObserver.on('navDestinationSwitch', this.getUIContext(), this.callBackFunc);
       }

       callBackFunc = (info: uiObserver.NavDestinationSwitchInfo) => {
         console.info(JSON.stringify(info));
         const offsetY = Number(AppStorage.get('listScrollOffset')); // 获取记录切换的tabs中的index
         this.scroller.scrollTo({
           xOffset: 0,
           yOffset: offsetY,
           animation: { duration: 0, curve: Curve.Ease }
         }); // 由于只能上下移动，所以改变yOffset即可
       };

       build() {
         NavDestination() {
           Column({ space: 20 }) {
             Row() {
               Button('跳转页面')
                 .margin({ top: 20 })
                 .onClick(() => {
                   this.pathStack.pushPathByName('PageTwoS2', null, false);
                 });
             };

             Scroll(this.scroller) {
               List({ space: 16 }) {
                 ForEach(this.arr, (item: number) => {
                   ListItem() {
                     Text(item.toString())
                       .width('100%')
                       .height(100)
                       .fontSize(16)
                       .textAlign(TextAlign.Center)
                       .borderRadius(16)
                       .backgroundColor('#F1F3F5');
                   }.width('100%')
                   .padding({ left: 12, right: 12 });
                 }, (item: string) => item);
               }.alignListItem(ListItemAlign.Center);
             }.height('90%')
             .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
             .onDidScroll((xOffset: number, yOffset: number, scrollState: ScrollState) => {
               console.info(`${xOffset} ${yOffset} ${scrollState}`);
               this.offsetY += yOffset; // 上下滑动，只记录yOffset即可
               AppStorage.setOrCreate('listScrollOffset', this.offsetY); // 持久化存储
             });
           }
           .width('100%')
           .height('100%')
           .padding({ top: 5 });
         }
         .onReady((context: NavDestinationContext) => {
           this.pathStack = context.pathStack;
         });
       }
     }
     ```

     ```ts
     @Builder
     export function PageTwoS2Builder() {
       PageTwoS2();
     }

     @Component
     struct PageTwoS2 {
       pathStack: NavPathStack = new NavPathStack();

       build() {
         NavDestination() {
           Column({ space: 20 }) {
             Button('跳转PageOne')
               .margin('20vp')
               .onClick(() => {
                 this.pathStack.pushPathByName('PageOneS2', null, false);
               });
           }.width('100%').height('100%');
         }
         .onReady((context: NavDestinationContext) => {
           this.pathStack = context.pathStack;
         });
       }
     }
     ```

     效果预览：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/QxVQvMppTOagseb-Lew2lw/zh-cn_image_0000002658962449.gif "点击放大")

## 常见FAQ

Q：NavDestination生命周期执行顺序是什么？

A：执行顺序为onWillAppear-->onReady-->onAppear-->onWillShow，具体可参考[页面生命周期](../harmonyos-guides/arkts-navigation-navdestination.md#页面生命周期)。

Q：Navigation组件中如何实现单例模式？

A：可以参考[使用导航控制器方法](../harmonyos-references/ts-basic-components-navigation.md#示例2使用导航控制器方法)。
