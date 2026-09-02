---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1077
title: 如何实现HAP和HAR/HSP页面跳转
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现HAP和HAR/HSP页面跳转
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:74575ad0d6a4c501925a2614713a817b82d0c8bbae24683a308fd8ee004086d4
---

## 问题现象

HAP页面如何跳转到HAR/HSP页面，HAR/HSP页面如何跳转到HAP页面。

## 背景知识

[Navigation](../harmonyos-references/ts-basic-components-navigation.md)：路由导航的根视图容器，管理[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)子页面的路由栈。

[Router](../harmonyos-references/arkts-apis-uicontext-router.md)：通过不同的url访问不同的页面。

HAR和HSP的使用：[HAR的使用](../harmonyos-guides/har-package.md#使用)、[HSP的使用](../harmonyos-guides/in-app-hsp.md#使用)。

## 解决方案

跳转示例：HAP模块Index页面（Router跳转）->HSP模块HspIndexPage页面（Navigation跳转）->HSP模块HspPage页面（Navigation跳转）->HAR模块HarPage页面（Router跳转）->HAP模块Index页面。

1. HAP模块Index页面->HSP模块HspIndexPage页面，使用Router实现。
   * 方式一：通过命名路由的方式实现跨包跳转。可参考[跨包路由](../harmonyos-guides/arkts-router-to-navigation.md#跨包路由)。
   * 方式二：使用@bundle协议指定目标模块的包名、模块名和页面路径。格式规则：@bundle:包名（bundleName）/模块名（moduleName）/路径/页面所在的文件名(不加.ets后缀)。参考示例如下所示：

     ```ts
     this.getUIContext().getRouter().pushUrl({
       url: '@bundle:com.example.navigationsystemtable/hsp/ets/pages/Index' // url格式为'@bundle:包名（bundleName）/模块名（moduleName）/路径/页面所在的文件名(不加.ets后缀)'
     });
     ```
2. HSP模块HspIndexPage页面->HSP模块HspPage页面->HAR模块HarPage页面，推荐使用Navigation实现。
   1. 在对应的模块内oh-package.json5文件中配置依赖，参考示例如下所示：

      ```json
      "dependencies": {
        "har": "file:../har",
        "hsp": "file:../hsp"
      }
      ```
   2. 在HSP和HAR模块内的配置系统路由表：详情可参考[系统路由表](../harmonyos-guides/arkts-navigation-cross-package.md#系统路由表)。
   3. 构建HspIndexPage、HspPage、HarPage页面，并在对应模块内的Index.ets文件中导出。参考示例如下所示：

      HSP模块内Index.ets文件：

      ```ts
      export { Index } from './src/main/ets/pages/Index';

      export { HspPageBuilder, HspPage } from './src/main/ets/pages/HspPage';
      ```

      HAR模块内Index.ets文件：

      ```ts
      export { HarPage } from './src/main/ets/components/HarPage';
      ```
   4. 通过pushPathByName等方法跳转页面：

      ```ts
      this.pageInfos.pushPathByName('HspPage', null, false);
      ```

      除系统路由表外，可通过Navigation动态路由实现，开发者可参考[Navigation动态路由](https://gitcode.com/HarmonyOS-Cases/cases/tree/master/test/performance/dynamicRouter/)。
3. HAR模块HarPage页面->HAP模块Index页面，entry内模块路由跳转：pages/页面所在的文件名（不加.ets后缀），参考示例如下所示：

   ```ts
   // (无需@bundle前缀）
   this.getUIContext().getRouter().pushUrl({ url: 'pages/Index' });
   ```

完整代码如下所示：

HAP模块：oh-package.json5文件配置如上，Index页面代码如下所示。

```ts
// import引入HSP模块内跳转目标页面
import 'hsp/src/main/ets/pages/Index';

@Entry
@Component
struct Index {
  pageInfos: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pageInfos) {
      Column({ space: 16 }) {
        Button('跳转到hspIndexPage页面（方法一）')
          .onClick(() => {
            this.getUIContext().getRouter().pushNamedRoute({ name: 'HspIndexPage' });
          });
        Button('跳转到hspIndexPage页面（方法二）')
          .onClick(() => {
            this.getUIContext().getRouter().pushUrl({
              url: '@bundle:com.example.navigationsystemtable/hsp/ets/pages/Index' // url格式为'@bundle:包名（bundleName）/模块名（moduleName）/路径/页面所在的文件名(不加.ets后缀)'
            });
          });
        Button('跳转到HspPage页面')
          .onClick(() => {
            this.pageInfos.pushPathByName('HspPage', null, false);
          });
      }
      .width('100%')
      .height('100%');
    }
    .width('100%')
    .height('100%')
    .hideBackButton(true)
    .title('hap页面')
    .titleMode(NavigationTitleMode.Mini);
  }
}
```

HSP模块：Index.ets文件如上配置。HspIndexPage页面代码如下：

```ts
// 命名路由页面的名字
@Entry({ routeName: 'HspIndexPage' })
@Component
export struct Index {
  pageInfos: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pageInfos) {
      Column({ space: 16 }) {
        Button('跳转到HspPage页面')
          .onClick(() => {
            this.pageInfos.pushPathByName('HspPage', null, false);
          });
      }
      .width('100%')
      .height('100%');
    }
    .width('100%')
    .height('100%')
    .hideBackButton(true)
    .title('hspIndexPage页面')
    .titleMode(NavigationTitleMode.Mini);
  }
}
```

HspPage页面代码如下：

```ts
@Builder
export function HspPageBuilder() {
  HspPage();
}

@Component
export struct HspPage {
  pageInfos: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column({ space: 16 }) {
        Button('跳转har页面')
          .onClick(() => {
            this.pageInfos.pushPathByName('HarPage', null, false);
          });
      }
      .width('100%')
      .height('100%');
    }
    .width('100%')
    .height('100%')
    .title('hsp页面')
    .hideBackButton(true)
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    });
  }
}
```

系统路由表配置如下：

```json
{
  "routerMap": [
    {
      "name": "HspPage",
      "pageSourceFile": "src/main/ets/pages/HspPage.ets",
      "buildFunction": "HspPageBuilder",
      "data": {
        "description": "this is harPage,"
      }
    }
  ]
}
```

HAR模块：Index.ets文件如上配置。HarPage页面代码如下所示。

```ts
@Builder
export function harPageBuilder() {
  HarPage();
}

@Component
export struct HarPage {
  pageInfos: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column({ space: 16 }) {
        Button('跳转到hap页面')
          .onClick(() => {
            // (无需@bundle前缀）
            this.getUIContext().getRouter().pushUrl({ url: 'pages/Index' });
          });
      }
      .width('100%')
      .height('100%');
    }
    .width('100%')
    .height('100%')
    .title('har页面')
    .hideBackButton(true)
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    });
  }
}
```

系统路由表配置如下：

```json
{
  "routerMap": [
    {
      "name": "HarPage",
      "pageSourceFile": "src/main/ets/components/HarPage.ets",
      "buildFunction": "harPageBuilder",
      "data": {
        "description": "this is harPage,"
      }
    }
  ]
}
```

## 常见FAQ

Q：HAR模块中能否支持Page页面？

A：HAR模块支持Page页面，但不支持在配置文件module.json5中声明pages页面，通过[命名路由](../harmonyos-guides/arkts-router-to-navigation.md#跨包路由)的方式跳转，详见[HAR和HSP支持page](faqs-package-structure-15.md)和[HAP/HAR/HSP使用场景](faqs-package-structure-73.md)。

## 总结

HAP和HAR/HSP页面跳转相关问题如下表所示：

|  | 实现方案 | 特点 | 适用场景 |
| --- | --- | --- | --- |
| Router | 方式一：通过命名路由的方式实现跨包跳转。 | 基于页面装饰器@Entry({routeName:'PageName'})声明路由名称。 | 模块内简单页面跳转、小型应用或原型开发。 |
| 方式二：使用@bundle协议指定目标模块的包名、模块名和页面路径。 | 通过@bundle:包名/模块路径格式指定目标资源。 | 动态化场景（按需加载远程模块）、跨包跳转（如主应用跳子模块）。 |
| Navigation | 方式一：系统路由表 | 将路由表方案下沉到系统中管理。 | 复杂应用统一路由管理、多团队协作开发（各模块独立配置路由表）。 |
| 方式二：动态路由 | 使用动态Import，按需加载页面 | 彻底解耦的模块化架构、跨HSP/HAR的无依赖跳转。 |
