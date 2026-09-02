---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1028
title: Navigation如何实现从0至1渐变出现的跳转动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Navigation如何实现从0至1渐变出现的跳转动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4afad9df4b23b678ab7c6f4b3e53bdec9e12a60ac62a2df4c4721383c9d789c5
---

## 问题现象

使用Navigation作为路由框架，跳转动画采用customNavContentTransition，如何实现跳转动画是从0至1渐变显示整个页面，而不是默认从左到右的动画？

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)组件是路由导航的根视图容器，默认跳转动画为左右方向。
* [customNavContentTransition](../harmonyos-references/ts-basic-components-navigation.md#customnavcontenttransition11)可以自定义进场和退场的Destination页面动画。使用方法可参考[设置可交互转场动画](../harmonyos-references/ts-basic-components-navigation.md#示例3设置可交互转场动画)和[自定义转场动画](../harmonyos-references/ts-basic-components-navigation.md#示例13自定义转场动画)。

## 解决方案

整体实现步骤如下：

1. 定义CustomTransition类管理动画参数：
   * 使用Map结构存储动画回调（customTransitionMap）。
   * 通过registerNavParam注册动画参数（包含start/end/onFinish三个回调及超时时间）。
   * 通过unRegisterNavParam移除已注册参数。
   * 通过getAnimateParam获取指定动画参数。
2. 在页面组件通过aboutToAppear生命周期注册动画回调函数。
   * start：初始化动画参数（如设置初始位移或透明度）。
   * finish：动画结束时的参数，执行动画过渡效果。
   * onFinish：动画结束的回调，重置动画状态或执行清理操作。
3. 在customNavContentTransition中根据页面注册的动画回调创建自定义转场动画协议。

代码实现如下：（以下代码片段请放入同一个文件中运行）

1. 声明动画回调函数接口。

   ```ts
   interface AnimateCallback {
     finish: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
     start: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
     onFinish: ((isPush: boolean, isExit: boolean) => void | undefined) | undefined;
     timeout: (number | undefined) | undefined;
   }
   ```
2. 使用Map结构存储每个页面注册的动画回调。创建单例类CustomTransition管理每个页面动画回调函数的注册和移除。可参考[设置可交互转场动画](../harmonyos-references/ts-basic-components-navigation.md#示例3设置可交互转场动画)中CustomTransition类的实现。

   ```ts
   // 存储每个页面的动画回调函数
   const customTransitionMap: Map<number, AnimateCallback> = new Map();

   // CustomTransition类管理函数的注册和移除
   export class CustomTransition {
     static delegate = new CustomTransition();

     static getInstance() {
       return CustomTransition.delegate;
     }

     // 注册某个页面的动画回调
     registerNavParam(name: number, startCallback: (operation: boolean, isExit: boolean) => void,
       endCallback: (operation: boolean, isExit: boolean) => void,
       onFinish: (operation: boolean, isExit: boolean) => void, timeout: number): void {
       if (customTransitionMap.has(name)) {
         let param = customTransitionMap.get(name);
         if (param !== undefined) {
           param.start = startCallback;
           param.finish = endCallback;
           param.onFinish = onFinish;
           param.timeout = timeout;
           return;
         }
       }
       let params: AnimateCallback = {
         timeout: timeout,
         start: startCallback,
         finish: endCallback,
         onFinish: onFinish,
       };
       customTransitionMap.set(name, params);
     }

     // 移除某个页面的动画回调
     unRegisterNavParam(name: number): void {
       customTransitionMap.delete(name);
     }

     // 获取某个页面的动画回调
     getAnimateParam(name: number): AnimateCallback {
       let result: AnimateCallback = {
         start: customTransitionMap.get(name)?.start,
         finish: customTransitionMap.get(name)?.finish,
         timeout: customTransitionMap.get(name)?.timeout,
         onFinish: customTransitionMap.get(name)?.onFinish
       };
       return result;
     }
   }
   ```
3. 在希望自定义动画的页面中，调用CustomTransition类注册相应的动画回调。如下所示，注册的回调函数中设置了转场位置和透明度。

   ```ts
   @Component
   struct pageOneTmp {
     @Consume('pageInfos') pageInfos: NavPathStack;
     @State x: number = 0;
     @State opacitys: number = 1; // 添加透明度状态
     pageId: number = 0;

     aboutToAppear() {
       this.pageId = this.pageInfos.getAllPathName().length - 1;
       CustomTransition.getInstance().registerNavParam(this.pageId, (isPush: boolean, isExit: boolean) => {
         console.info(`${isPush} ${isExit}`);
         this.x = isExit ? 0 : 300;
         this.opacitys = isExit ? 1 : 0; // 设置初始透明度
       }, (isPush: boolean, isExit: boolean) => {
         console.info(`${isPush} ${isExit}`);
         this.x = isExit ? -300 : 0;
         this.opacitys = isExit ? 0 : 1; // 设置结束透明度
       }, (isPush: boolean, isExit: boolean) => {
         console.info(`${isPush} ${isExit}`);
         this.x = 0;
         this.opacitys = 1; // 重置透明度
       }, 200);
     }

     build() {
       NavDestination() {
         Column() {
           Button('pageTwo', { stateEffect: true, type: ButtonType.Capsule })
             .width('80%')
             .height(40)
             .margin(20)
             .onClick(() => {
               this.pageInfos.pushPathByName('pageTwo', null); //将name指定的NavDestination页面信息入栈，传递的数据为param
             });

         }.width('100%').height('100%');
       }
       .title('pageOne')
       .mode(NavDestinationMode.STANDARD)
       .onBackPressed(() => {
         const popDestinationInfo = this.pageInfos.pop(); // 弹出路由栈栈顶元素
         console.log('pop' + '返回值' + JSON.stringify(popDestinationInfo));
         return true;
       })
       .onDisAppear(() => {
         CustomTransition.getInstance().unRegisterNavParam(this.pageId);
       })
       .translate({ x: 0, y: this.x, z: 0 })
       .opacity(this.opacitys) // 设置透明度属性
       .backgroundColor(Color.White);
     }
   }
   ```

   ```ts
   @Component
   struct PageTwoTemp {
     @Consume('pageInfos') pageInfos: NavPathStack;
     @State x: number = 300;
     @State opacitys: number = 1; // 添加透明度状态
     pageId: number = 0;

     aboutToAppear() {
       this.pageId = this.pageInfos.getAllPathName().length - 1;
       CustomTransition.getInstance().registerNavParam(this.pageId, (isPush: boolean, isExit: boolean) => {
         console.info(`${isPush} ${isExit}`);
         this.x = isExit ? 0 : isPush ? 300 : -300;
         this.opacitys = isExit ? 1 : 0; // 设置初始透明度
       }, (isPush: boolean, isExit: boolean) => {
         console.info(`${isPush} ${isExit}`);
         this.x = isExit ? isPush ? -300 : 300 : 0;
         this.opacitys = isExit ? 0 : 1; // 设置结束透明度
       }, (isPush: boolean, isExit: boolean) => {
         console.info(`${isPush} ${isExit}`);
         this.x = 0;
         this.opacitys = 1; // 重置透明度
       }, 2000);
     }

     build() {
       NavDestination() {
         Column() {
           Text('Page Two').fontSize(50);
         }.width('100%').height('100%');
       }
       .title('pageTwo')
       .onDisAppear(() => {
         CustomTransition.getInstance().unRegisterNavParam(this.pageId);
       })
       .translate({ x: 0, y: 0, z: this.x })
       .opacity(this.opacitys) // 设置透明度属性
       .backgroundColor(Color.White);
     }
   }
   ```
4. 通过Navigation的customNavContentTransition属性设置转场动画。此属性的回调入参包含了进退场Destination页面的信息。通过进退场页面的信息，使用CustomTransition类查询页面对应的动画回调函数，并构建自定义转场动画协议NavigationAnimatedTransition。

   ```ts
   @Entry
   @Component
   struct NavigationPage {
     @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();

     @Builder
     PageMap(name: string) {
       if (name === 'pageOne') {
         pageOneTmp({ pageId: Date.now() });
       } else if (name === 'pageTwo') {
         PageTwoTemp({ pageId: Date.now() });
       }
     }

     aboutToAppear() {
       this.pageInfos.pushPath({ name: 'pageOne' }, false);
       // 使用路由拦截功能
       this.pageInfos.setInterception({
         willShow: (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar,
           operation: NavigationOperation, isAnimated: boolean) => {
           // 如果要返回到主页面，就push名为pageOne的子页面
           if (to == 'navBar') {
             console.info(`${from} ${operation} ${isAnimated}`);
             this.pageInfos.pushPathByName('pageOne', undefined, false);
           }
         }
       });
     }

     build() {
       Navigation(this.pageInfos) {
       }.title('NavIndex').navDestination(this.PageMap)
       .hideNavBar(true)
       .customNavContentTransition((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => {
         if (from.mode === NavDestinationMode.DIALOG || to.mode === NavDestinationMode.DIALOG) {
           return undefined;
         }
         if (from.index === -1 || to.index === -1) {
           return undefined;
         }
         let customAnimation: NavigationAnimatedTransition = {
           timeout: 700,
           transition: (transitionProxy: NavigationTransitionProxy) => {
             // 获取退场页面的动画回调函数
             let fromParam: AnimateCallback = CustomTransition.getInstance()?.getAnimateParam(from.index);
             // 获取进场页面的动画回调函数
             let toParam: AnimateCallback = CustomTransition.getInstance()?.getAnimateParam(to.index);
             if (fromParam.start !== undefined) {
               fromParam.start(operation === NavigationOperation.PUSH, true);
             }
             if (toParam.start !== undefined) {
               toParam.start(operation === NavigationOperation.PUSH, false);
             }
             this.getUIContext().animateTo({
               duration: 1200, onFinish: () => {
                 if (fromParam.onFinish !== undefined) {
                   fromParam.onFinish(operation === NavigationOperation.PUSH, true);
                 }
                 if (toParam.onFinish !== undefined) {
                   toParam.onFinish(operation === NavigationOperation.PUSH, false);
                 }
                 transitionProxy.finishTransition();
               }
             }, () => {
               if (fromParam.finish !== undefined) {
                 fromParam?.finish(operation === NavigationOperation.PUSH, true);
               }
               if (toParam.finish !== undefined) {
                 toParam?.finish(operation === NavigationOperation.PUSH, false);
               }
             });
           }
         };
         return customAnimation;
       });
     }
   }
   ```
