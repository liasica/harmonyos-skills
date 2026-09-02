---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-710
title: 如何混用Navigation和router实现路由导航
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何混用Navigation和router实现路由导航
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d617d026652ceb83b139686fe2906ffa8bc15c0e80c848a0ac9b604c8a0d0c3d
---

## 问题现象

如何实现Navigation和router的混用？

## 背景知识

* [router](../harmonyos-references/arkts-apis-uicontext-router.md)：提供通过不同的url访问不同的页面，包括跳转到应用内的指定页面、同应用内的某个页面替换当前页面、返回上一页面或指定的页面等。
* [Navigation](../harmonyos-guides/arkts-navigation-navigation.md)：用于实现Navigation页面（[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)）间的跳转，支持在不同Navigation页面间传递参数，提供灵活的跳转栈操作，从而更便捷地实现对不同页面的访问和复用。Navigation是路由导航的根视图容器，一般作为页面（@Entry）的根容器。

## 解决方案

对于router跳转到的页面需要使用Navigation作为根容器，才能在这个页面跳转到下个NavDestination页面。这是因为router跳转的是page页面，而NavDestination是Navigation的子组件，二者层次不同。以下为Navigation和router混用的三种常见场景。

### 场景一

Navigation页面与router页面间的跳转，如：入口页面->NavPageOne->RouterPageOne->NavPageTwo。该混用场景常见于“全局导航+局部导航”的页面设计，例如首页到隐私模块页面等。

使用router跳转到RouterPageOne，RouterPageOne使用Navigation作为根容器跳转到NavPageTwo，这里RouterPageOne的Navigation和第一个Navigation相互独立，都有各自的路由栈，互不影响。开发者需参考[系统路由表](../harmonyos-guides/arkts-navigation-cross-package.md#系统路由表)配置Navigation路由，配置说明附在本文末尾。

入口页面代码如下：需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

```ts
@Entry
@Component
struct SceneOne {
  pageInfo: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pageInfo) {
      Column() {
        Button('ToNavDestinationOneByNavPathStack', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(24)
          .onClick(() => {
            this.pageInfo.pushPath({ name: 'NavPageOne' });
          });
      };
    }
    .title('NavIndex');
  }
}
```

NavPageOne页面代码如下：

```ts
@Builder
export function PageOneBuilder() {
  NavPageOne();
}

@Component
struct NavPageOne {
  pageInfo: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Text('NavDestinationOne')
        .width('80%')
        .height(50)
        .margin(24);
      Button('ToRouterPage1ByRouter', { stateEffect: true, type: ButtonType.Capsule })
        .width('80%')
        .height(40)
        .margin(10)
        .onClick(() => {
          // 使用router跳转到下一个页面
          this.getUIContext().getRouter().pushUrl({
            url: 'pages/RouterPageOne'
          });
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

需注意router管理@Entry页面之间的跳转（页面级路由栈）。Navigation管理NavDestination组件之间的跳转（组件级路由栈），NavDestination作为Navigation的子组件存在，需搭配Navigation使用。若通过router跳转到一个需要承载NavDestination的页面，该页面（@Entry）必须用Navigation作为容器。

RouterPageOne页面代码如下：需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

```ts
@Entry
@Component
struct RouterPageOne {
  pageInfo: NavPathStack = new NavPathStack();

  build() {
    // 注意：使用NavDestination，会导致无法跳转到指定NavDestination
    // 使用Navigation，可以正常跳转
    Navigation(this.pageInfo) {
      Column() {
        Text('RouterPage1')
          .margin(24);
        Button('ToNavDestination2ByNavPathStack')
          .onClick(() => {
          this.pageInfo.pushPath({ name: 'NavPageTwo' });
        });
      };
    }
    .height('100%')
    .width('100%');
  }
}
```

NavPageTwo页面代码如下：

```ts
@Builder
export function PageTwoBuilder() {
  NavPageTwo();
}

@Component
struct NavPageTwo {
  pageInfo: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Text('NavDestination2')
        .width('80%')
        .height(50)
        .margin(24);
      Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
        .width('80%')
        .height(40)
        .margin(10);
    }
    .height('100%')
    .width('100%');
  }
}
```

| 无法跳转到NavPageTwo | 正常跳转到NavPageTwo |
| --- | --- |
|  |  |
| RouterPageOne使用NavDestination作为根容器。 | RouterPageOne使用Navigation作为根容器。 |

### 场景二

使用router页面作为闪屏页，后续页面跳转由Navigation承载。

使用router跳转到一个Navigation作为根容器的页面，然后清空router路由栈中的页面。

闪屏页代码如下：需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

```ts
@Entry
@Component
struct SceneTwo {
  @State message: string = '闪屏页';

  aboutToAppear(): void {
    setTimeout(() => {
      this.getUIContext().getRouter().replaceUrl({ url: 'pages/NavigationPage' });
    }, 2000);
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

首页代码如下：需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

```ts
@Entry
@Component
struct NavIndex {
  pageInfo: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pageInfo) {
      Column() {
        Button('ToNavDestinationOneByNavPathStack', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfo.pushPath({ name: 'pageOne' });
          });
      };
    }.title('NavIndex');
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/igQZ6C1OT3mhoCBwQtS2IQ/zh-cn_image_0000002658914219.png "点击放大")

### 场景三

Navigation页面与router页面间的跳转为：入口页面->PageOne->pageTwo->RouterPage->PageThree。

该混用场景常见于使用的三方SDK布局为router导航，且根容器不是Navigation。可以使用router的单例模式（[页面跳转](../harmonyos-guides/arkts-routing.md#页面跳转)的场景三）拉起Navigation首页，通过路由监听或者传参等方式控制Navigation首页跳转PageThree。

入口页面代码如下：需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

```ts
@Entry
@Component
struct SceneThree {
  pageInfos: NavPathStack = new NavPathStack();
  isUseInterception: boolean = false;

  onPageShow(): void {
    let rouNam: number | undefined = AppStorage.get('router');
    if (rouNam === 1) {
      this.getUIContext().getRouter().clear(); // 清除掉历史页面router
      this.pageInfos.pushDestination({ name: 'pageThree' }, false);
    }
  }

  build() {
    Stack() {
      Navigation(this.pageInfos) {
        Button('pageOne', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'pageOne' });
          });
      }
      .title('NavIndex')
      .titleMode(NavigationTitleMode.Mini);
    };
  }
}
```

PageOne页面代码如下：

```ts
@Builder
export function PageOneBuilder() {
  PageOne();
}

@Component
export struct PageOne {
  pageInfos: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Button('pageTwo', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'pageTwo' });
          });
      }
      .width('100%')
      .height('100%');
    }
    .title('pageOne')
    .onBackPressed(() => {
      this.pageInfos.pop();
      return true;
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .customTransition(null);
  }
}
```

pageTwo页：

```ts
@Builder
export function PageTwoBuilder() {
  PageTwo();
}

@Component
export struct PageTwo {
  pathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Button('routerSDK客服页', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.getUIContext().getRouter().pushUrl({ url: 'pages/RouterPage' }, (err) => {
              if (err) {
                console.error(`Failed to pushUrl, code is ${err.code}, message is ${err.message}`);
                return;
              }
              console.info('Succeeded in pushUrl.');
            });
          });
        Button('pageThree', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.pushDestination({ name: 'pageThree' });
          });

        Button('pop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pathStack.pop();
          });
      }
      .width('100%')
      .height('100%');
    }
    .title('pageTwo')
    .backgroundColor('#FFFFFF')
    .onBackPressed(() => {
      this.pathStack.pop();
      return true;
    })
    .onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack;
    })
    .customTransition(null);
  }
}
```

RouterPage页面代码如下：需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)：

```ts
import { router } from '@kit.ArkUI';

@Entry
@Component
struct RouterPage {
  build() {
    Column() {
      Text('客服页');
      Button('router首页+拉起page3', { stateEffect: true, type: ButtonType.Capsule })
        .width('80%')
        .height(40)
        .margin(20)
        .onClick(() => {
          AppStorage.setOrCreate('router', 1);
          this.getUIContext().getRouter().pushUrl({ url: 'pages/SceneThree' }, router.RouterMode.Single, (err) => {
            if (err) {
              console.error(`Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
              return;
            }
            console.info('Invoke pushUrl succeeded.');
          });
        });
    };
  }
}
```

PageThree页面代码如下：

```ts
@Builder
export function PageThreeBuilder() {
  PageThree();
}

@Component
export struct PageThree {
  pathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Button('pop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            AppStorage.delete('router');
            this.pathStack.pop();
          });
      }
      .width('100%')
      .height('100%');
    }
    .title('pageThree')
    .onBackPressed(() => {
      let rouNam: number | undefined = AppStorage.get('router');
      // 消除返回重影
      setTimeout(() => {
        this.pathStack?.pop();
      }, rouNam === 1 ? 500 : 0);
      if (rouNam === 1) {
        this.getUIContext().getRouter().clear(); // 清除掉历史页面router
        AppStorage.delete('router');
      }
      return true;
    })
    .onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack;
    });
  }
}
```

上述场景的Navigation页面需进行路由配置，在src/main目录下的工程配置文件module.json5中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json文件。router\_map.json文件内容如下：

```json
{
  "routerMap": [
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    },
    {
      "name": "pageTwo",
      "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
      "buildFunction": "PageTwoBuilder"
    },
    {
      "name": "pageThree",
      "pageSourceFile": "src/main/ets/pages/PageThree.ets",
      "buildFunction": "PageThreeBuilder"
    },
    {
      "name": "NavPageOne",
      "pageSourceFile": "src/main/ets/pages/SceneOne.ets",
      "buildFunction": "PageOneBuilder"
    },
    {
      "name": "NavPageTwo",
      "pageSourceFile": "src/main/ets/pages/SceneOne.ets",
      "buildFunction": "PageTwoBuilder"
    }
  ]
}
```

resources/base/profile/main\_pages.json配置如下：

```json
{
  "src": [
    "pages/SceneThree",
    "pages/RouterPageOne",
    "pages/SceneTwo",
    "pages/NavigationPage",
    "pages/SceneOne",
    "pages/RouterPage"
  ]
}
```

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/pc-a1h_oR5KUEX0a2uu2EA/zh-cn_image_0000002628395004.png "点击放大")

## 总结

推荐单独使用Navigation组件导航，不建议混用。若涉及混合使用Navigation和router应注意以下关键点：

1. router页面需以Navigation为根容器。
2. 避免路由栈冲突：Navigation通过NavPathStack管理自身路由栈，router有独立的路由栈机制。混合跳转时（如：NavDestination -> RouterPage），需显式清空router栈中不需要的页面（如闪屏页）。
3. 跳转方向需符合层级：router仅支持跳转到用@Entry的页面，无法通过router直接从NavDestination跳转到另一个NavDestination，需要经过@Entry页面中转。
