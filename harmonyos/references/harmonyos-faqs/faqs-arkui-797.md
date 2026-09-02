---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-797
title: 在子窗口中使用Navigation进行多页面跳转
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 在子窗口中使用Navigation进行多页面跳转
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-07-02
content_hash: sha256:911eada7b1078e53a7d25b8780fb55be572aaded33126cb96072880dbd8c45ff
---

## 问题现象

如何在子窗口中使用Navigation实现多页面跳转的功能？

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（NavDestination的子组件），首页和非首页通过路由进行切换。
* HarmonyOS提供的窗口模块用于在同一块物理屏幕上，提供多个应用界面显示、交互的机制。开发者可以按需创建[应用子窗口](../harmonyos-guides/subwindow-guide.md)，如弹窗等，并对其进行属性设置等操作。
* 无法在自定义弹窗中进行多页面跳转，推荐使用子窗口进行操作。

## 解决方案

1. 在UIAbility中的onWindowStageCreate方法中添加在如下代码，以实现窗口的全局存储。

   ```ts
   AppStorage.setAndLink('windowStage', windowStage);
   ```
2. 创建主页面，在该页面中实现createSubWindow方法，用以创建子窗口，设置子窗口的位置，大小及相关属性，并加载对应的页面。

   ```ts
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   let windowStage_: window.WindowStage | undefined = undefined;
   let sub_windowClass: window.Window | undefined = undefined;

   @Entry
   @Component
   struct Index {
     private createSubWindow() {
       windowStage_ = AppStorage.get('windowStage'); // 获取windowStage

       if (windowStage_ == null) {
         console.error('Failed to create the subwindow. Cause: windowStage_ is null');
       } else {
         windowStage_.createSubWindow('mySubWindow', (err: BusinessError, data) => { // 创建应用子窗口
           let errCode: number = err.code;
           if (errCode) {
             console.error('Failed to create the subwindow. Cause: ' + JSON.stringify(err));
             return;
           }
           sub_windowClass = data;
           if (!sub_windowClass) {
             console.error('sub_windowClass is null');
             return;
           }
           console.info('Succeeded in creating the subwindow. Data: ' + JSON.stringify(data));
           sub_windowClass.moveWindowTo(300, 300, (err: BusinessError) => { // 子窗口创建成功后，设置子窗口的位置、大小及相关属性等
             let errCode: number = err.code;
             if (errCode) {
               console.error('Failed to move the window. Cause:' + JSON.stringify(err));
               return;
             }
             console.info('Succeeded in moving the window.');
           });
           sub_windowClass.resize(700, 700, (err: BusinessError) => {
             let errCode: number = err.code;
             if (errCode) {
               console.error('Failed to change the window size. Cause:' + JSON.stringify(err));
               return;
             }
             console.info('Succeeded in changing the window size.');
           });
           sub_windowClass.setUIContent('pages/SubWindow', (err: BusinessError) => { // 为子窗口加载对应的目标页面。
             let errCode: number = err.code;
             if (errCode) {
               console.error('Failed to load the content. Cause:' + JSON.stringify(err));
               return;
             }
             console.info('Succeeded in loading the content.');
             if (!sub_windowClass) {
               console.error('sub_windowClass is null');
               return;
             }
             sub_windowClass.showWindow((err: BusinessError) => { // 显示子窗口
               let errCode: number = err.code;
               if (errCode) {
                 console.error('Failed to show the window. Cause: ' + JSON.stringify(err));
                 return;
               }
               console.info('Succeeded in showing the window.');
             });
           });
         });
       }
     }

     private destroySubWindow() {
       if (!sub_windowClass) {
         console.error('sub_windowClass is null');
         return;
       }
       sub_windowClass.destroyWindow((err: BusinessError) => { // 销毁子窗口
         let errCode: number = err.code;
         if (errCode) {
           console.error('Failed to destroy the window. Cause: ' + JSON.stringify(err));
           return;
         }
         console.info('Succeeded in destroying the window.');
       });
     }

     build() {
       Row() {
         Column() {
           Button() {
             Text('创建子窗口')
               .fontSize(20)
               .fontWeight(FontWeight.Normal)
           }.width(110).height(50)
           .onClick(() => {
             this.createSubWindow();
           })
           .position({
             top: 50,
             left: 50
           })

           Button() {
             Text('销毁子窗口')
               .fontSize(20)
               .fontWeight(FontWeight.Normal)
           }.width(110).height(50)
           .onClick(() => {
             this.destroySubWindow();
           })
           .position({
             top: 120,
             left: 50
           })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
3. 使用Navigation创建子窗口的主页面及其子页面。

   ```ts
   @Entry
   @ComponentV2
   struct SubWindow {
     pageInfos: NavPathStack = new NavPathStack();
     isUseInterception: boolean = false;

     build() {
       Navigation(this.pageInfos) {
         Column() {
           Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
             .width('80%')
             .height(40)
             .margin(20)
             .onClick(() => {
               this.pageInfos.pushPath({ name: 'pageOne' });
             })
         }
       }.title('子窗口页面')
       .borderWidth(2)
     }
   }
   ```

   ```ts
   class TmpClass {
     count: number = 10;
   }

   @Builder
   export function PageOneBuilder() {
     PageOne()
   }

   @ComponentV2
   export struct PageOne {
     pageInfos: NavPathStack = new NavPathStack();

     build() {
       NavDestination() {
         Column() {
           Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
             .width('80%')
             .height(40)
             .margin(20)
             .onClick(() => {
               let tmp = new TmpClass();
               this.pageInfos.pushPathByName('pageTwo', tmp);
             })
         }.width('100%').height('100%')
       }.title('pageOne')
       .onReady((context: NavDestinationContext) => {
         this.pageInfos = context.pathStack;
       })
     }
   }
   ```
