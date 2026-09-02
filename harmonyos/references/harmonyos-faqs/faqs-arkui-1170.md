---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1170
title: 如何实现在NavDestination子页面中动态调整公共组件的样式
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现在NavDestination子页面中动态调整公共组件的样式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:75e20e6d80ad55a20fbd0eb6bc2827fa2ed262bc7a6cfb10601c2b4f8ca4f73d
---

## 问题现象

在NavDestination子页面中抽离出公共组件，如何动态调整公共组件的样式？比如，在NavDestination的A子页面中，组件使用红色背景色，而在B子页面中，组件使用蓝色背景色。

## 背景知识

* [组件导航（Navigation）](../harmonyos-guides/arkts-navigation-navigation.md)主要用于实现Navigation页面（NavDestination）间的跳转，支持在不同Navigation页面间传递参数，提供灵活的跳转栈操作，从而更便捷地实现对不同页面的访问和复用。
* 自定义组件提供[queryNavDestinationInfo](../harmonyos-references/ts-custom-component-api.md#querynavdestinationinfo)方法，可以在NavDestination内部查询到当前所属页面的信息，返回值为[NavDestinationInfo](../harmonyos-references/js-apis-arkui-observer.md#navdestinationinfo)，若查询不到则返回undefined。

## 解决方案

整体上来看，首先需要使用Navigation组件构建路由导航的根视图容器，然后使用NavDestination构建子页面。在子页面中，将公共组件抽离，并利用queryNavDestinationInfo方法查询组件所属的页面，进行动态调整。

1. 使用Navigation组件构建路由导航的根视图容器。

   ```ts
   // 根容器
   Navigation(this.navPathStack) {
     Button('跳转第一个页面').onClick(() => {
       this.navPathStack.pushPath({
         name: 'one'
       });
     });
     Button('跳转第二个页面').onClick(() => {
       this.navPathStack.pushPath({
         name: 'two'
       });
     });
   }.navDestination(this.myDestination);
   ```
2. 使用NavDestination构建子页面。

   ```ts
   @Component
   struct One {
     @Consume('navPathStack') navPathStack: NavPathStack;

     build() {
       NavDestination() {
         Text('第一个页面');
         Common();
       };
     }
   }

   @Component
   struct Two {
     @Consume('navPathStack') navPathStack: NavPathStack;

     build() {
       NavDestination() {
         Text('第二个页面');
         Common();
       };
     }
   }
   ```
3. 抽离公共组件，利用queryNavDestinationInfo方法查询组件所属的页面，进行动态调整。

   ```ts
   // 公共组件
   @Component
   struct Common {
     navDesInfo: uiObserver.NavDestinationInfo | undefined;

     aboutToAppear(): void {
       this.navDesInfo = this.queryNavDestinationInfo();
     }

     build() {
       Column() {
         Text('这里是公共的组件');
         Text("所属页面Name: " + this.navDesInfo?.name);
       }.width(200)
       .height(200)
       .border({
         width: 5
       })
       // 根据NavDestinationInfo动态调整样式
       .backgroundColor(this.navDesInfo?.name == 'one' ? Color.Blue : Color.Red);
     }
   }
   ```

完整示例参考如下：

```ts
import { uiObserver } from '@kit.ArkUI';

@Component
@Entry
struct DynamicallyAdjustPublicComponents {
  @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack();

  @Builder
  myDestination(name: string) {
    if (name == 'one') {
      One();
    } else if (name == 'two') {
      Two();
    }
  }

  build() {
    // 根容器
    Navigation(this.navPathStack) {
      Button('跳转第一个页面').onClick(() => {
        this.navPathStack.pushPath({
          name: 'one'
        });
      });
      Button('跳转第二个页面').onClick(() => {
        this.navPathStack.pushPath({
          name: 'two'
        });
      });
    }.navDestination(this.myDestination);

  }
}

@Component
struct One {
  @Consume('navPathStack') navPathStack: NavPathStack;

  build() {
    NavDestination() {
      Text('第一个页面');
      Common();
    };
  }
}

@Component
struct Two {
  @Consume('navPathStack') navPathStack: NavPathStack;

  build() {
    NavDestination() {
      Text('第二个页面');
      Common();
    };
  }
}

// 公共组件
@Component
struct Common {
  navDesInfo: uiObserver.NavDestinationInfo | undefined;

  aboutToAppear(): void {
    this.navDesInfo = this.queryNavDestinationInfo();
  }

  build() {
    Column() {
      Text('这里是公共的组件');
      Text("所属页面Name: " + this.navDesInfo?.name);
    }.width(200)
    .height(200)
    .border({
      width: 5
    })
    // 根据NavDestinationInfo动态调整样式
    .backgroundColor(this.navDesInfo?.name == 'one' ? Color.Blue : Color.Red);
  }
}
```
