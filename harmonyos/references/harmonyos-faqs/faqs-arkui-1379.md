---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1379
title: Navigation路由导航更新全局变量时机
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Navigation路由导航更新全局变量时机
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:53457cbf8426d3fa649fc757ae41a48f328cb917959d7e95cd1bbd7fd9974cf1
---

## 问题现象

使用Navigation组件进行页面导航，现有一个页面A和一个全局变量globalData。在页面A中调用replacePathByName方法跳转到页面B。开发者在页面A的aboutToDisappear（销毁时执行）生命周期回调中初始化globalData，并在页面B的aboutToAppear（初始化实例时执行）回调中尝试获取globalData。结果发现，在页面B中获取到的globalData是未初始化的状态。这表明页面生命周期的执行顺序与预期不符。

## 背景知识

* 组件导航（[Navigation](../harmonyos-guides/arkts-navigation-navigation.md)）主要用于实现页面间以及组件内部的跳转。它支持在不同组件间传递参数，并提供了灵活的页面栈操作（如入栈、出栈、替换），方便页面访问和复用。
* [replacePathByName](../harmonyos-references/ts-basic-components-navigation.md#replacepathbyname11)该API用于替换Navigation路由栈的当前页面。其核心流程是：先将目标页面B入栈，然后退出（销毁）当前页面A。这种设计主要是为了防止在页面切换过程中出现空白页面。

## 解决方案

replacePathByName的执行顺序是：先让目标页面B入栈并准备显示，然后再销毁当前页面A。因此，在页面跳转(A -> B)过程中，生命周期的实际触发顺序是：

1. B页面的aboutToAppear。
2. A页面的aboutToDisappear。

   **关键点**：这意味着页面B的构建(aboutToAppear)发生在页面A销毁(aboutToDisappear)之前。

数据变量处理建议：

1. 页面级数据：通常无需特殊处理。当从页面A跳转到页面B时，页面A的数据变量会在其aboutToDisappear后被销毁，不会影响B页面的数据。这是预期行为。
2. 全局数据（globalData问题）：

   **问题根源**：由于页面B的aboutToAppear在页面A的aboutToDisappear之前执行，在页面B中访问globalData时，页面A中初始化globalData的代码(aboutToDisappear)尚未执行。

   **处理建议**：不要在页面A的aboutToDisappear中初始化页面B需要的全局数据。应在触发跳转（调用replacePathByName）之前就完成globalData的初始化。可以通过自定义的路由管理单例，在执行任何路由替换操作之前，统一完成所需全局数据的更新和准备。

示例代码如下：

Index.ets封装路由组件，更新全局数据：

```ts
//封装路由组件
export class routerModule {
  static stack: NavPathStack;
  static instance: routerModule;

  static init(stack: NavPathStack) {
    routerModule.stack = stack;
  }

  static getInstance() {
    if (!routerModule.instance) {
      routerModule.instance = new routerModule();
    }
    return routerModule.instance;
  }

  replacePathByName(routeName: string) {
    // 清除全局数据再跳转
    AppStorage.setOrCreate('globalData', 1);
    routerModule.stack.replacePathByName(routeName, '');
  }
}

@Entry
@Component
struct NavigationIndex {
  pageInfos: NavPathStack = new NavPathStack();

  aboutToAppear() {
    routerModule.init(this.pageInfos);
  }

  build() {
    Stack() {
      Navigation(this.pageInfos) {
        Column() {
          Button('To PageA', { stateEffect: true, type: ButtonType.Capsule })
            .width('80%')
            .height(40)
            .margin(20)
            .onClick(() => {
              this.pageInfos.pushPath({ name: 'pageA' });
            });
        };
      }.title('NavIndex');

    };
  }
}
```

PageA.ets触发路由跳转（调用replacePathByName）：

```ts
import { routerModule } from './Index';

@Builder
export function PageABuilder() {
  PageA();
}

@Component
export struct PageA {
  pageInfo: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Button('replacePathByName', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            routerModule.getInstance().replacePathByName('pageB');
          });

      }.width('100%').height(300);
    }
    .width('100%')
    .title('pageA')
    .onBackPressed(() => {
      this.pageInfo.pop();
      return true;
    }).onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    });
  }
}
```

PageB.ets查看数据更新：

```ts
@Builder
export function PageBBuilder() {
  PageB();
}

@Component
export struct PageB {
  pageInfo: NavPathStack = new NavPathStack();
  @State globalData: number | undefined = 0;

  aboutToAppear(): void {
    this.globalData = AppStorage.get('globalData');
  }

  build() {
    NavDestination() {
      Column() {
        Text("数据更新后的值：" + this.globalData)
          .width(200);
      }.width('100%').height(300);
    }
    .width('100%')
    .title('pageB')
    .onBackPressed(() => {
      this.pageInfo.pop();
      return true;
    }).onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    });
  }
}
```

在src/main目录下的[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下：

```json
{
  "routerMap": [
    {
      "name": "pageA",
      "pageSourceFile": "src/main/ets/pages/PageA.ets",
      "buildFunction": "PageABuilder",
      "data": {
        "description": "this is pageA"
      }
    },
    {
      "name": "pageB",
      "pageSourceFile": "src/main/ets/pages/PageB.ets",
      "buildFunction": "PageBBuilder",
      "data": {
        "description": "this is pageB"
      }
    }
  ]
}
```
