---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-904
title: Tab组件内Navigation跳转，TabBar导航栏隐藏失败如何解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Tab组件内Navigation跳转，TabBar导航栏隐藏失败如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a75634448705614125e6e29145b5bf25d685f61665728e8438c971b5b5f2bf47
---

## 问题现象

在“我的”页面点击“跳转设置页”按钮跳转到设置页面，底部的TabBar导航栏仍然存在。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/XN0I7Qu9RWeKUJGfYj8PxQ/zh-cn_image_0000002658918977.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/Q3EdubCPQ76R5XOWPuo6yQ/zh-cn_image_0000002628399756.png "点击放大")

主页面有“首页”、“我的”两个Tab页面，部分代码如下：

```ts
@Entry
@Component
struct TabsNavPage {
  build() {
    Tabs() {
      TabContent() {
        MinePage()
      }
      .tabBar(BottomTabBarStyle.of($r('sys.media.ohos_app_icon'), '我的'))

      TabContent() {
        Text('首页')
      }
      .tabBar(BottomTabBarStyle.of($r('sys.media.ohos_app_icon'), '首页'))
    }
    .barPosition(BarPosition.End)
  }
}

@Component
struct MinePage {
  @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();

  @Builder
  PagesMap(name: string) {
    if (name === 'Settings') {
      Settings();
    }
  }

  build() {
    Navigation(this.pathStack) {
      Row(){
        Column() {
          Button('跳转设置页')
            .onClick(() => {
              this.pathStack.pushPathByName('Settings', null);
            })
        }
      }
    }
    .hideTitleBar(true)
    .navDestination(this.PagesMap)
  }
}

@Component
struct Settings {
  @Consume('pathStack') pathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Button('返回')
        .onClick(() => {
          this.pathStack.pop();
        });
    }.title('设置')
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/un0ap7csQJCKg7_JS0p0uQ/zh-cn_image_0000002658799025.png "点击放大")

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)的子组件），首页和非首页通过路由进行切换。
* [@Provide装饰器和@Consume装饰器](../harmonyos-guides/arkts-provide-and-consume.md)：应用于与后代组件的双向数据同步、状态数据在多个层级之间传递的场景。

## 解决方案

问题现象中是用Tab组件包裹Navigation组件，跳转Navigation子组件并不会影响到外层的Tab组件。

将Navigation组件作为根容器包括Tab组件，为保证子组件都共享一个NavPathStack实例，可以使用@Provide和@Consume装饰器将导航控制器对象[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)传递给Tabs内的子组件使用。

```typescript
@Entry
@Component
struct TabsNavPage {
  // 使用@Provide将路由栈对象传递给TabContent内的组件
  @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();

  @Builder
  PagesMap(name: string) {
    if (name === 'Settings') {
      Settings();
    }
  }

  build() {
    // 使用Navigation包裹Tabs，Tabs子页使用同一个路由栈对象
    Navigation(this.pathStack) {
      Tabs() {
        TabContent() {
          MinePage();
        }
        .tabBar(BottomTabBarStyle.of($r('sys.media.ohos_app_icon'), '我的'))

        TabContent() {
          Text('首页').fontColor('40fp');
        }
        .tabBar(BottomTabBarStyle.of($r('sys.media.ohos_app_icon'), '首页'))
      }
      .barPosition(BarPosition.End);
    }
    .hideTitleBar(true)
    .navDestination(this.PagesMap)
  }
}

@Component
struct MinePage {
  // 获取Navigation的路由栈对象
  @Consume('pathStack') pathStack: NavPathStack;

  build() {
    Column() {
      Button('跳转设置页')
        .onClick(() => {
          this.pathStack.pushPathByName('Settings', null);
        });
    };
  }
}

@Component
struct Settings {
  @Consume('pathStack') pathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Button('返回')
        .onClick(() => {
          this.pathStack.pop();
        });
    }.title('设置')
  }
}
```
