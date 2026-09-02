---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-761
title: NavPathStack如何在自己封装的公共类中使用
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > NavPathStack如何在自己封装的公共类中使用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4ba3f5881e5758903e21b9d0a1d2a0484e4923e2de446766f25d08b79bdae0a7
---

## 问题现象

NavPathStack能在子组件中使用或者自己封装的公共类中使用吗，如何使用？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/bDEWbxwXT624J4Li6sTtOQ/zh-cn_image_0000002628395798.gif "点击放大")

## 背景知识

* [AppStorage](../harmonyos-guides/arkts-appstorage.md)：应用全局的UI状态存储。
* [Navigation](../harmonyos-references/ts-basic-components-navigation.md#navigation-1)：Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)的子组件），首页和非首页通过路由进行切换。

## 解决方案

1. 新增PublicUtils文件并定义跳转页面的公共方法。

   ```screen
   export class Tmp {
     pushPath(name: string) {
       (AppStorage.get('pathStack') as NavPathStack).pushPath({ name: name });
     }
   }
   ```
2. 将NavPathStack缓存起来。

   ```screen
   // Index.ets
   import { Tmp } from './PublicUtils';

   @Entry
   @Component
   struct Index {
     // 创建一个页面栈对象并传入Navigation
     private pathStack: NavPathStack = new NavPathStack();
     private InfoTmp: Tmp = new Tmp();

     aboutToAppear(): void {
       // 存储pathStack
       AppStorage.setOrCreate('pathStack', this.pathStack);
     }

     build() {
       Navigation(this.pathStack) {
         Button('click')
           .onClick(() => {
             // 调用pushPath方法并跳转到对应页面
             this.InfoTmp.pushPath('PageOne');
           });
       }
       .title('Main');
     }
   }
   ```
3. PageOne页面：

   ```screen
   @Builder
   export function PageOneBuilder() {
     PageOne();
   }

   @Component
   export struct PageOne {
     build() {
       NavDestination() {
         Button('setInteractive');
       }
       .width('100%')
       .height('100%');
     }
   }
   ```
4. 在src/main目录下的工程配置文件module.json5中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例参考如下：

   ```screen
   {
     "routerMap": [
       {
         "name": "PageOne",
         "pageSourceFile": "src/main/ets/pages/PageOne.ets",
         "buildFunction": "PageOneBuilder"
       }
     ]
   }
   ```
