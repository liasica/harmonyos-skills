---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1090
title: 如何监听页面切换
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何监听页面切换
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:4749b43c2433867e32c9c8b2101eb163c3f51fc4c50a5397e280243078ef6713
---

## 问题现象

场景一：如何监听Navigation根页面的显示与隐藏状态？

场景二：如何监听NavDestination组件的显示和隐藏状态？

场景三：如何实现页面埋点监听？

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)：路由导航的根视图容器。
* [NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)：子页面的根容器，用于显示Navigation的内容区。
* [onNavBarStateChange](../harmonyos-references/ts-basic-components-navigation.md#onnavbarstatechange9)：导航页显示状态切换时触发该回调。
* [uiObserver.on('navDestinationUpdate')](../harmonyos-references/js-apis-arkui-observer.md#uiobserveronnavdestinationupdate)：监听NavDestination组件的状态变化。
* [uiObserver.on('navDestinationSwitch')](../harmonyos-references/js-apis-arkui-observer.md#uiobserveronnavdestinationswitch12)：监听Navigation的页面切换事件。
* [onShown](../harmonyos-references/ts-basic-components-navdestination.md#onshown10)：当该NavDestination页面显示时触发此回调。
* [onHidden](../harmonyos-references/ts-basic-components-navdestination.md#onhidden10)：当该NavDestination页面隐藏时触发此回调。
* [onActive](../harmonyos-references/ts-basic-components-navdestination.md#onactive17)：NavDestination处于激活态（处于栈顶可操作，且上层无特殊组件遮挡）时，触发该回调。
* [@Watch装饰器](../harmonyos-guides/arkts-watch.md)：用于对状态变量的监听。

## 解决方案

实现方案如下：

| **应用场景** | **实现方案** | **实现效果** | **方案对比** |
| --- | --- | --- | --- |
| **场景一：监听Navigation根页面的显隐状态。** | **方案一：使用uiObserver.on('navDestinationSwitch')实现监听。** | 可监听所有页面的切换事件（包括前进/后退）。 | 适用于全局监听的场景。 |
| **方案二：使用onNavBarStateChange实现监听。** | 监听导航栏的显隐状态变化。 | 仅能监听导航栏状态，无法获取具体页面切换的详细信息。 |
| **方案三：使用@Watch监听路由栈大小。** | 通过装饰器实现NavPathStack的自动监听，可获取路由栈的当前状态。 | 必须确保NavPathStack的引用正确传递到监听组件中。 |
| **场景二：监听NavDestination的显隐状态。** | **方案一：通过页面生命周期实现监听。** | 可精确监听单个页面的显隐状态。 | 仅能监听当前页面的生命周期，无法感知其他页面的切换状态。 |
| **方案二：使用uiObserver.on('navDestinationUpdate')实现监听。** | 可监听所有NavDestination的切换事件。 | 适用于全局监听的场景。 |
| **场景三：实现页面埋点监听。** | **方案：通过无感监听实现。** | 实现对页面访问次数及页面访问时间的监听统计。 | / |

* **场景一：监听Navigation根页面的显隐状态。**
  + **方案一：使用uiObserver.on('navDestinationSwitch')实现监听。**

    当页面切换时触发，可获取切换前后的页面信息[NavDestinationSwitchInfo](../harmonyos-references/js-apis-arkui-observer.md#navdestinationswitchinfo12)，当[NavDestinationSwitchInfo](../harmonyos-references/js-apis-arkui-observer.md#navdestinationswitchinfo12)的to的值为'navBar'时，表示返回到根页面。参考代码如下所示：

    ```ts
    import { uiObserver } from '@kit.ArkUI';

    @Entry
    @Component
    struct SceneOneDestinationSwitch {
      pageInfos: NavPathStack = new NavPathStack();

      @Builder
      pageMap(name: string) {
        if (name === 'PageTwo') {
          DestinationSwitchPageTwo();
        } else if (name === 'PageThree') {
          DestinationSwitchPageThree();
        }
      }

      aboutToAppear(): void {
        uiObserver.on('navDestinationSwitch', this.getUIContext(), (info: uiObserver.NavDestinationSwitchInfo) => {
          // 当返回到根页面
          if (info.to === 'navBar') {
            console.info(`Succeeded in Navigation show.`);
          } else {
            console.info(`Succeeded in Navigation hide.`);
          }
        });
      }

      // 移除监听
      aboutToDisappear(): void {
        uiObserver.off('navDestinationSwitch', this.getUIContext());
      }

      build() {
        Navigation(this.pageInfos) {
          Button('PageOne跳转到PageTwo')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pushPathByName('PageTwo', null, false);
            });
        }
        .hideNavBar(false)
        .navDestination(this.pageMap);
      }
    }

    @Component
    struct DestinationSwitchPageTwo {
      pageInfos: NavPathStack = new NavPathStack();

      build() {
        NavDestination() {
          Button('PageTwo跳转PageThree')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pushPathByName('PageThree', null, false);
            });
          Button('PageTwo返回PageOne')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pop();
            });
        }
        .hideTitleBar(true)
        .onReady((context: NavDestinationContext) => {
          this.pageInfos = context.pathStack;
        });
      }
    }

    @Component
    struct DestinationSwitchPageThree {
      pageInfos: NavPathStack = new NavPathStack();

      build() {
        NavDestination() {
          Button('PageThree返回PageTwo')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pop();
            });
          Button('PageThree返回首页')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.clear();
            });
        }
        .hideTitleBar(true)
        .onReady((context: NavDestinationContext) => {
          this.pageInfos = context.pathStack;
        });
      }
    }
    ```
  + **方案二：使用onNavBarStateChange实现监听。**

    当导航栏的显隐状态发生变化时触发，isVisible参数为true表示导航栏显示，false表示隐藏。参考代码如下所示：

    ```ts
    @Entry
    @Component
    struct SceneOneNavBarStateChange {
      pageInfos: NavPathStack = new NavPathStack();

      @Builder
      pageMap(name: string) {
        if (name === 'PageTwo') {
          NavBarStateChangePageTwo();
        } else if (name === 'PageThree') {
          NavBarStateChangePageThree();
        }
      }

      build() {
        Navigation(this.pageInfos) {
          Button('PageOne跳转到PageTwo')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pushPathByName('PageTwo', null, false);
            });
        }
        .hideNavBar(false)
        .navDestination(this.pageMap)
        .onNavBarStateChange((isVisible: boolean) => {
          // isVisible为true时表示显示
          if (isVisible) {
            console.info(`Succeeded in Navigation show.`);
          } else {
            console.info(`Succeeded in Navigation hide.`);
          }
        });
      }
    }

    @Component
    struct NavBarStateChangePageTwo {
      pageInfos: NavPathStack = new NavPathStack();

      build() {
        NavDestination() {
          Button('PageTwo跳转PageThree')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pushPathByName('PageThree', null, false);
            });
          Button('PageTwo返回PageOne')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pop();
            });
        }
        .hideTitleBar(true)
        .onReady((context: NavDestinationContext) => {
          this.pageInfos = context.pathStack;
        });
      }
    }

    @Component
    struct NavBarStateChangePageThree {
      pageInfos: NavPathStack = new NavPathStack();

      build() {
        NavDestination() {
          Button('PageThree返回PageTwo')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pop();
            });
          Button('PageThree返回首页')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.clear();
            });
        }
        .hideTitleBar(true)
        .onReady((context: NavDestinationContext) => {
          this.pageInfos = context.pathStack;
        });
      }
    }
    ```
  + **方案三：使用@Watch监听路由栈大小。**

    使用@Provide提供全局共享的pageSize状态变量，使用@Watch装饰器监听pageSize，在每次执行跳转操作时，将路由栈的大小赋值pageSize，并触发监听回调方法pathInfoChange()，pageSize的值为0时，表示返回到根页面。参考代码如下所示：

    ```ts
    @Entry
    @Component
    struct SceneOneWatch {
      pageInfos: NavPathStack = new NavPathStack();
      @Provide @Watch('pathInfoChange') pageSize: number = -1;

      // pageSize变化时触发该方法
      pathInfoChange() {
        if (this.pageInfos.size() === 0) {
          console.info(`Succeeded in Navigation show.`);
        } else {
          console.info(`Succeeded in Navigation hide.`);
        }
      }

      @Builder
      pageMap(name: string) {
        if (name === 'PageTwo') {
          WatchPageTwo();
        } else if (name === 'PageThree') {
          WatchPageThree();
        }
      }

      aboutToAppear(): void {
        this.pathInfoChange();
      }

      build() {
        Navigation(this.pageInfos) {
          Button('PageOne跳转到PageTwo')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pushPathByName('PageTwo', null, false);
              // 路由栈的大小赋值pageSize
              this.pageSize = this.pageInfos.size();
            });
        }
        .hideNavBar(false)
        .navDestination(this.pageMap);
      }
    }

    @Component
    struct WatchPageTwo {
      pageInfos: NavPathStack = new NavPathStack();
      @Consume pageSize: number = -1;

      build() {
        NavDestination() {
          Button('PageTwo跳转PageThree')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pushPathByName('PageThree', null, false);
              this.pageSize = this.pageInfos.size();
            });
          Button('PageTwo返回PageOne')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pop();
              this.pageSize = this.pageInfos.size();
            });
        }
        .hideTitleBar(true)
        .onReady((context: NavDestinationContext) => {
          this.pageInfos = context.pathStack;
        });
      }
    }

    @Component
    struct WatchPageThree {
      pageInfos: NavPathStack = new NavPathStack();
      @Consume pageSize: number = -1;

      build() {
        NavDestination() {
          Button('PageThree返回PageTwo')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pop();
              this.pageSize = this.pageInfos.size();
            });
          Button('PageThree返回首页')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.clear();
              this.pageSize = this.pageInfos.size();
            });
        }
        .hideTitleBar(true)
        .onReady((context: NavDestinationContext) => {
          this.pageInfos = context.pathStack;
        });
      }
    }
    ```
* **场景二：监听NavDestination的显隐状态。**
  + **方案一：通过页面生命周期实现监听。**

    监听NavDestination组件的显示与隐藏状态，可通过NavDestination组件的onShown事件和onHidden事件监听。除了onShown和onHidden事件，也可使用其它事件组合进行更多元化的监听，具体事件可以参考[页面生命周期](../harmonyos-guides/arkts-navigation-navdestination.md#页面生命周期)。示例可参考[NavDestination生命周期时序](../harmonyos-references/ts-basic-components-navigation.md#示例8navdestination生命周期时序)和[NavDestination的onActive与onInActive生命周期](../harmonyos-references/ts-basic-components-navdestination.md#示例5navdestination的onactive与oninactive生命周期)。
  + **方案二：使用uiObserver.on('navDestinationUpdate')实现监听。**

    当页面切换时会触发，监听NavDestination组件的状态变化并返回组件信息[NavDestinationInfo](../harmonyos-references/js-apis-arkui-observer.md#navdestinationinfo)，通过[NavDestinationInfo](../harmonyos-references/js-apis-arkui-observer.md#navdestinationinfo)的name和state监听指定NavDestination组件的显隐状态。参考代码如下所示：

    ```ts
    import { uiObserver } from '@kit.ArkUI';

    @Entry
    @Component
    struct SceneTwoDestinationUpdate {
      pageInfos: NavPathStack = new NavPathStack();

      @Builder
      pageMap(name: string) {
        if (name === 'PageOne') {
          DestinationUpdatePageOne();
        } else if (name === 'PageTwo') {
          DestinationUpdatePageTwo();
        } else if (name === 'PageThree') {
          DestinationUpdatePageThree();
        }
      }

      aboutToAppear(): void {
        uiObserver.on('navDestinationUpdate', (info: NavDestinationInfo) => {
          // 监听目标页面的显隐状态
          if (info.name === 'PageOne' && info.state === 0) {
            console.info(`Succeeded in navDestinationOne show.`);
          } else if (info.name === 'PageOne' && info.state === 1) {
            console.info(`Succeeded in navDestinationOne hide.`);
          }
        });
      }

      // 移除监听
      aboutToDisappear(): void {
        uiObserver.off('navDestinationUpdate');
      }

      build() {
        Navigation(this.pageInfos)
          .navDestination(this.pageMap)
          .hideNavBar(true)
          .onAppear(() => {
            this.pageInfos.pushPathByName('PageOne', null, false);
          });
      }
    }

    @Component
    struct DestinationUpdatePageOne {
      pageInfos: NavPathStack = new NavPathStack();

      build() {
        NavDestination() {
          Button('PageOne跳转PageTwo')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pushPathByName('PageTwo', null, false);
            });
        }
        .hideTitleBar(true)
        .onReady((context: NavDestinationContext) => {
          this.pageInfos = context.pathStack;
        });
      }
    }

    @Component
    struct DestinationUpdatePageTwo {
      pageInfos: NavPathStack = new NavPathStack();

      build() {
        NavDestination() {
          Button('PageTwo跳转PageThree')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pushPathByName('PageThree', null, false);
            });
          Button('PageTwo返回PageOne')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pop();
            });
        }
        .hideTitleBar(true)
        .onReady((context: NavDestinationContext) => {
          this.pageInfos = context.pathStack;
        });
      }
    }

    @Component
    struct DestinationUpdatePageThree {
      pageInfos: NavPathStack = new NavPathStack();

      build() {
        NavDestination() {
          Button('PageThree返回PageTwo')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pop();
            });
          Button('PageThree返回首页')
            .margin({ top: 16 })
            .fontSize(16)
            .padding(4)
            .onClick(() => {
              this.pageInfos.pushPathByName('PageOne', null, false);
            });
        }
        .hideTitleBar(true)
        .onReady((context: NavDestinationContext) => {
          this.pageInfos = context.pathStack;
        });
      }
    }
    ```
* **场景三：实现页面埋点监听。**
  + **方案：通过无感监听实现。**

    通过[@ohos.arkui.observer](../harmonyos-references/js-apis-arkui-observer.md)监听页面切换navDestinationSwitch、页面更新navDestinationUpdate、router页面状态变化routerPageUpdate三个事件。示例参考[页面埋点监听](../architecture-guides/page_tracing_point-0000002283641138.md)。
