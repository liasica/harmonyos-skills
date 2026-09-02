---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-804
title: 实现页面级弹出框的功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现页面级弹出框的功能
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:53+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:f895c48648e5f9aa2ca48693d3a14715da30e867ee0904d421cfb4c040a7754e
---

## 问题现象

使用自定义弹窗功能时，在特殊场景下，需要弹窗开启状态下进行页面跳转。用Navigation导航或者router导航在弹窗内跳转到新页面时，会遇到弹窗显示在所有的新入栈的页面上的问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/h5OIfD47SUWWA-MWAGNkbQ/zh-cn_image_0000002665416043.png "点击放大")

## 背景知识

弹窗的定义可参考官方文档：[弹窗概述](../harmonyos-guides/arkts-dialog-overview.md)，常见弹窗实现方式可以分为以下几种：

1. [自定义弹窗（CustomDialog）](../harmonyos-references/ts-methods-custom-dialog-box.md)是一种基础自定义弹窗，通过[CustomDialogController](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)控制。使用弹窗组件时，可自定义弹窗的样式与内容。
2. [@ohos.promptAction（弹窗）](../harmonyos-references/js-apis-promptaction.md)是一种不依赖UI组件的全局自定义弹出框，从API18开始，由于上下文不明确部分接口废弃，建议使用[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中的[getPromptAction](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取当前UI上下文关联的PromptAction对象。并且可以通过配置isModal来实现模态和非模态弹窗。isModal为true时，弹出框为模态弹窗。isModal为false时，弹出框为非模态弹窗。
3. [@ohos.window（窗口）](../harmonyos-references/js-apis-window.md)提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。其中[window.createWindow](../harmonyos-references/arkts-apis-window-f.md#windowcreatewindow9)接口通过[Configuration](../harmonyos-references/arkts-apis-window-i.md#configuration9)参数设置窗口属性。可通过windowType参数设置窗口类型为模态窗口以及子窗口等。
4. 通过[OverlayManager](../harmonyos-references/arkts-apis-uicontext-overlaymanager.md)设置浮层的方式实现弹窗。
5. 通过[NavDestinationMode.DIALOG](../harmonyos-references/ts-basic-components-navdestination.md#navdestinationmode枚举说明11)弹窗类型设置弹窗。此时整个NavDestination无组件占位部分默认透明显示。
6. 创建[模态窗口](../harmonyos-guides/arkts-modal-transition.md)通过[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)等模态窗口属性实现弹窗效果。

路由跳转方式：

1. [Navigation导航](../harmonyos-references/ts-basic-components-navigation.md)是官方推荐路由方式。Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（NavDestination的子组件），首页和非首页通过路由进行切换。
2. [@ohos.router（页面路由）](../harmonyos-references/js-apis-router.md)也是官方的一种路由方式，目前已不再演进，建议使用Navigation导航。

## 问题定位

* @ohos.router（页面路由）：

  出现该问题的根本原因是弹窗不是页面的一个组件或者与页面不是一个显示层级，弹窗显示层级在所有的页面之上。其中自定义弹窗（CustomDialog）、默认模式下的@ohos.promptAction（弹窗）、模态窗口等都是显示在Page页面层级之上。导致在不关闭弹窗的情况下，新打开的页面都在弹窗下面。
* Navigation导航：

  通过Navigation导航跳转时，由于Navigation页面为根页面，与NavDestination页面为父子组件关系，在一个Page内，所以相比较router跳转，当实现弹窗的方式是和Page同级显示时，依旧会显示在NavDestination页面上方。

  例如，将Navigation页面的[mode()](../harmonyos-references/ts-basic-components-navigation.md#mode9)属性参数NavigationMode.Stack改为NavigationMode.Auto，并采用平板展示时，通过@ohos.window（窗口）实现弹窗效果，能直观的复现上述问题。弹窗在NavDestination子页面创建，弹窗显示在根页面之上，也会导致在不关闭弹窗的情况下，新打开的NavDestination页面都在弹窗下面。

## 分析结论

根本原因是弹窗的显示层级在Page页面上，由于不同导航方式实现逻辑不一致，所以不同的导航方式，可以通过不同的窗口实现方式，实现“页面级弹窗”。

## 修改建议

* **方案一**：适用于Navigation导航与@ohos.router（页面路由）两种导航方式。

  可以通过通用属性[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md)，实现半模态弹窗的方式，实现页面级弹窗。需要在[SheetOptions](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)内设置其mode属性为SheetMode.EMBEDDED，表示其为页面级弹出框。以Navigation为例，示例代码如下：

  1. 创建Navigation主页：

     ```ts
     @Entry
     @Component
     struct Index {
       @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();

       build() {
         Navigation(this.pathStack) {
           Column() {
             Button('Navigation页')
               .onClick(() => {
                 this.pathStack.pushPathByName('IndexTwo', null);
               });
           }
           .justifyContent(FlexAlign.Center)
           .width('100%')
           .height('100%');
         }
         .mode(NavigationMode.Auto)
         .width('100%')
         .height('100%');
       }
     }
     ```
  2. 创建需要弹出弹窗的页面，并绑定页面级半模态弹窗：

     ```ts
     @Builder
     export function IndexTwoBuilder() {
       IndexTwo();
     }

     @Component
     struct IndexTwo {
       @State isShow: boolean = false;
       @Consume('pathStack') pathStack: NavPathStack;

       @Builder
       myBuilder() {
         Column() {
           Text('我是半模态弹窗');
           Button('jump')
             .margin({ top: 10 })
             .onClick(() => {
               this.pathStack.pushPathByName('IndexThree', null);
             });
         }
         .margin({ top: 22 })
         .justifyContent(FlexAlign.SpaceEvenly);
       }

       build() {
         NavDestination() {
           Stack() {
             Row() {
               Column() {
                 Button('点击打开弹窗')
                   .onClick(() => {
                     this.isShow = true;
                   });
               }
               .width('100%');
             }
             .height('100%');
           };
         }
         .bindSheet($$this.isShow, this.myBuilder(), {
           height: 400,
           mode: SheetMode.EMBEDDED, // 设置显示层级Navigation导航挂载在NavDestination节点上，若是Router路由挂载在Page节点上。
           backgroundColor: Color.White,
           onWillAppear: () => {
             console.info('BindSheet onWillAppear.');
           },
           onAppear: () => {
             console.info('BindSheet onAppear.');
           },
           onWillDisappear: () => {
             console.info('BindSheet onWillDisappear.');
           },
           onDisappear: () => {
             console.info('BindSheet onDisappear.');
           }
         })
         .title('IndexTwo');
       }
     }
     ```
  3. 创建弹窗内需要跳转的页面：

     ```ts
     @Builder
     export function IndexThreeBuilder() {
       IndexThree();
     }

     @Component
     struct IndexThree {
       @Consume('pathStack') pathStack: NavPathStack;

       build() {
         NavDestination() {
           Column() {
             Text('IndexThree')
               .height('100%');
           }
           .width('100%')
           .height('100%');
         }
         .title('IndexThree');
       }
     }
     ```

     方案一实现效果如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/MAEuEkTfQGaqC475OFmYPg/zh-cn_image_0000002658917109.png "点击放大")
* **方案二**：适用于Navigation导航方式。

  当采用@ohos.router（页面路由）方式跳转NavDestinationMode.DIALOG页面时不适用，会导致弹窗蒙层不透明。

  1. 自定义一个NavDestination组件设置mode为[NavDestinationMode.DIALOG](../harmonyos-references/ts-basic-components-navdestination.md#navdestinationmode枚举说明11)弹窗类型，此时整个NavDestination无组件占位部分默认透明显示。同时进出路由栈不影响下层NavDestination的可见性（onShown、onHidden等生命周期），只会触发onActive、onInactive这两个生命周期。
  2. 定义页面路由，采用push方法将弹窗页面推入路由栈内，由于透明可以看到下一级页面，实现打开弹窗效果。采用pop方法删除路由栈内弹窗页面，实现关闭弹窗效果。

  NavDestinationMode.DIALOG实现自定义弹窗方案，示例代码如下：

  1. 创建Navigation根页面。

     ```ts
     @Entry
     @Component
     struct Index {
       @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();

       build() {
         Navigation(this.pathStack) {
           Column() {
             Button('Navigation页')
               .onClick(() => {
                 this.pathStack.pushPathByName('IndexTwo', null);
               });
           }
           .justifyContent(FlexAlign.Center)
           .width('100%')
           .height('100%');
         }
         .mode(NavigationMode.Auto)
         .width('100%')
         .height('100%');
       }
     }
     ```
  2. 创建IndexTwo子页面，并定义到弹窗页面的路由。

     ```ts
     // 自定义弹窗组件
     @Builder
     export function IndexTwoBuilder() {
       IndexTwo();
     }

     @Component
     export struct IndexTwo {
       @Consume('pathStack') pathStack: NavPathStack;

       build() {
         NavDestination() {
           Row() {
             Column() {
               Button('点击打开弹窗')
                 .onClick(() => {
                   this.pathStack.pushPathByName('CustomDialog', '', false); // 推送弹窗页面
                 });
             }
             .width('100%');
           }
           .height('100%');
         }
         .title('IndexTwo');
       }
     }
     ```
  3. 创建并自定义CustomDialog子页面，并定义到Index3页面的路由。

     ```ts
     @Builder
     export function CustomDialogBuilder() {
       CustomDialog();
     }

     @Component
     export struct CustomDialog {
       @Consume('pathStack') pathStack: NavPathStack;

       build() {
         NavDestination() {
           Stack({ alignContent: Alignment.Center }) {
             Text('') // 弹窗遮罩
               .onClick(() => {
                 this.pathStack.pop(); // 点击遮罩退出该页面，达到关闭弹窗效果
               })
               .width('100%')
               .height('100%')
               .opacity(0) // 遮罩透明度调节
               .backgroundColor(0x000000);
             Column() {
               Text('我是弹窗');
               Button('jump')
                 .onClick(() => {
                   this.pathStack.pushPathByName('IndexThree', ''); // 弹窗内推送IndexThree页面
                 });
             }
             .justifyContent(FlexAlign.SpaceAround)
             .backgroundColor(Color.White)
             .borderRadius(30)
             .height('126vp')
             .width('90%');
           }.height('100%').width('100%');
         }
         .backgroundColor('rgba(0,0,0,0.5)')
         .hideTitleBar(true)
         .mode(NavDestinationMode.DIALOG);
       }
     }
     ```
  4. 创建IndexThree子页面。

     ```ts
     @Builder
     export function IndexThreeBuilder() {
       IndexThree();
     }

     @Component
     struct IndexThree {
       @Consume('pathStack') pathStack: NavPathStack;

       build() {
         NavDestination() {
           Column() {
             Text('IndexThree')
               .height('100%');
           }
           .width('100%')
           .height('100%');
         }
         .title('IndexThree');
       }
     }
     ```

     方案二实现效果如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/WQ0j8Ok2RTu9J7SCw0KfdA/zh-cn_image_0000002635181782.png "点击放大")

     **说明** 

     以上方案均省略了路由配置，Navigation路由表配置方法详见[系统路由表](../harmonyos-guides/arkts-navigation-cross-package.md#系统路由表)。
* **方案三**：适用于Navigation导航与@ohos.router（页面路由）两种导航方式。

  在API15的版本中新提供了[页面级弹出框](../harmonyos-guides/arkts-embedded-dialog.md)参考示例。当弹出框的options入参中设置levelMode属性，值为LevelMode.EMBEDDED时表示开启页面级弹出框能力。该levelMode属性不仅适用于PromptAction弹窗，也适用于CustomDialog弹窗，详见[CustomDialogControllerOptions对象说明](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)。

  + @ohos.router（页面路由）跳转应用示例详情参考官方文档：[页面级弹出框完整示例](../harmonyos-guides/arkts-embedded-dialog.md#完整示例)。
  + Navigation用法参考示例：
  1. 创建Navigation主页：

     ```ts
     @Entry
     @Component
     struct Index {
       @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();

       build() {
         Navigation(this.pathStack) {
           Column() {
             Button('Navigation页')
               .onClick(() => {
                 this.pathStack.pushPathByName('IndexTwo', null);
               });
           }
           .justifyContent(FlexAlign.Center)
           .width('100%')
           .height('100%');
         }
         .mode(NavigationMode.Auto)
         .width('100%')
         .height('100%');
       }
     }
     ```
  2. 创建弹窗需要绑定的页面，并创建弹窗：

     ```ts
     import { LevelMode, ImmersiveMode } from '@kit.ArkUI';

     @Builder
     function customDialogBuilder(pathStack: NavPathStack) {
       Column() {
         Text('我是弹窗');
         Button('jump')
           .onClick(() => {
             // 在弹窗内部进行路由跳转
             pathStack.pushPathByName('IndexThree', null);
           });
       }
       .justifyContent(FlexAlign.SpaceAround)
       .backgroundColor(Color.White)
       .borderRadius(10)
       .height('126vp')
       .width('100%');
     }

     @Builder
     export function IndexTwoBuilder() {
       IndexTwo();
     }

     @Component
     struct IndexTwo {
       private uiContext: UIContext = this.getUIContext();
       @Consume('pathStack') pathStack: NavPathStack;

       @Builder
       customDialogComponent() {
         customDialogBuilder(this.pathStack);
       }

       build() {
         NavDestination() {
           Row() {
             Column() {
               Button('点击打开弹窗')
                 .id('test_text')
                 .onClick(() => {
                   const node: FrameNode | null = this.getUIContext().getFrameNodeById('test_text') || null;
                   this.uiContext.getPromptAction().openCustomDialog({
                     builder: () => {
                       this.customDialogComponent();
                     },
                     levelMode: LevelMode.EMBEDDED, // 启用页面级弹出框
                     levelUniqueId: node?.getUniqueId(), // 设置页面级弹出框所在页面的任意节点ID
                     immersiveMode: ImmersiveMode.EXTEND, // 设置页面级弹出框蒙层的显示模式
                   });
                 });
             }
             .width('100%');
           }
           .height('100%');
         }
         .title('IndexTwo');
       }
     }
     ```
  3. 创建弹窗内跳转的页面：

     ```ts
     @Builder
     export function IndexThreeBuilder() {
       IndexThree();
     }

     @Component
     struct IndexThree {
       @Consume('pathStack') pathStack: NavPathStack;

       build() {
         NavDestination() {
           Column() {
             Text('IndexThree')
               .height('100%');
           }
           .width('100%')
           .height('100%');
         }
         .title('IndexThree');
       }
     }
     ```

     方案三Navigation导航实现效果如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/smuZhQ_OS-mA235q58nq4A/zh-cn_image_0000002658797157.png "点击放大")
* **方案四**：适用于@ohos.router（页面路由）导航方式。

  通过@ohos.window（窗口）创建子窗口的形式创建弹窗：
  1. 修改EntryAbility页面配置。

     ```ts
     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
       windowStage.loadContent('pages/PageA', (err) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         // 全局使用
         AppStorage.setOrCreate('windowStage', windowStage);
         hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
       });
     }
     ```
  2. 主页创建并调用子窗口。

     ```ts
     // PageA.ets页面
     import window from '@ohos.window';
     import { Context } from '@kit.AbilityKit';
     import * as subWin from './subWindow'; // 导入命名路由页面(子窗口)
     import { BusinessError } from '@kit.BasicServicesKit';

     @Entry
     @Component
     struct Index {
       // 全局使用
       @State windowStage: window.WindowStage = AppStorage.get('windowStage') as window.WindowStage;
       @State context: Context = this.getUIContext().getHostContext() as Context;

       build() {
         Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
           Text('这是 page A')
             .fontSize(20)
             .margin({ bottom: 10 });
           Button('点击打开子窗口')
             .onClick(() => {
               this.windowStage.createSubWindow('mySubWindow', (err, windowClass) => {
                 if (err.code) {
                   console.error(`Failed. Cause code: ${err.code}, message: ${err.message}`);
                 }
                 try {
                   windowClass.loadContentByName(subWin.entryName, (err: BusinessError) => {
                     const errCode: number = err.code;
                     if (errCode) {
                       console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
                       return;
                     }
                     console.info('Succeeded in loading the content.');
                     // 设置子窗口左上角坐标
                     windowClass.moveWindowTo(0, 0);
                     // 展示子窗口
                     windowClass.showWindow();
                     // 设置子窗口全屏化布局避让安全区
                     windowClass.setWindowLayoutFullScreen(false);
                     windowClass.setWindowBackgroundColor('#63727272');
                   });
                 } catch (exception) {
                   console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
                 }
                 ;
               });
             });
         }
         .backgroundColor(Color.White)
         .width('100%')
         .height('100%');
       }
     }
     ```
  3. 自定义子窗口布局。

     ```ts
     // subWindow.ets页面
     import { window } from '@kit.ArkUI';

     export const entryName: string = 'subWindow';

     @Entry({ routeName: entryName })
     @Component
     export struct subWindow {
       @StorageProp('pageInfos') pageInfos: NavPathStack = new NavPathStack();

       onBackPress(): boolean | void {
         window.findWindow('mySubWindow').destroyWindow(); // 销毁子窗口
       }

       build() {
         Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
           Stack({ alignContent: Alignment.Center }) {
             Text('') // 弹窗遮罩
               .onClick(() => {
                 window.findWindow('mySubWindow').destroyWindow(); // 销毁子窗口
               })
               .width('100%')
               .height('100%')
               .opacity(0) // 遮罩透明度调节
               .backgroundColor(0x000000);
             Column() {
               Text('我是弹窗');
               Button('jump')
                 .onClick(() => {
                   this.getUIContext().getRouter().pushUrl({
                     url: 'pages/PageB'
                   });
                 });
             }
             .justifyContent(FlexAlign.SpaceAround)
             .backgroundColor(Color.White)
             .borderRadius(30)
             .height('126vp')
             .width('90%');
           }.height('100%').width('100%');
         }
         .width('100%')
         .height('100%');
       }
     }
     ```
  4. 创建跳转测试页面。

     ```ts
     // PageB.ets页面
     @Entry
     @Component
     struct PageB {
       build() {
         Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
           Text('这是 Page B')
             .fontSize(20)
             .margin({ bottom: 10 });
         }
         .backgroundColor(Color.White)
         .width('100%')
         .height('100%')
         .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
       }
     }
     ```

     方案四实现效果如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/MnLRiCwFS8CvTyPG0t2Enw/zh-cn_image_0000002665306201.png "点击放大")

## 常见FAQ

Q：除以上方案外，是否还有其他方式可以实现页面级弹窗？

A：通过组件的通用[zIndex](../harmonyos-references/ts-universal-attributes-z-order.md#zindex)/[visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)属性以及if/else语法控制组件的显隐，模拟实现自定义弹窗效果，但是该方案并不推荐，系统已经封装有各种弹窗，层级、动效都有接口可控制，通过该方式实现弹窗过于复杂且不方便维护。

Q：怎样实现多层弹窗效果？

A：弹窗嵌套即可。可以使用官方弹窗组件CustomDialog嵌套CustomDialog；也可以在CustomDialog官方弹窗内采用本文方案混合使用，遵循谁后打开，谁显示在上层的原则。

Q：设置zIndex属性层级最高的情况下，为什么没效果？

A：zIndex是设置同层组件之间的渲染优先级权重，但不支持跨层比较权重。

Q：Navigation页面中，在弹出框的options入参中设置levelMode属性，页面级弹出框不生效？

A：弹窗层级控制本质上是弹窗所挂载的父节点不同，默认弹窗挂在Root节点下，所以层级最高，页面级弹窗中router路由需要挂载在Page节点下，而Navigation路由需要挂载在NavDestination节点下。所以页面级弹出框只能在NavDestination页面下，设置页面级弹框才会生效，即：在Navigation中嵌套NavDestination，然后在弹出框的options入参中设置levelMode属性，页面级弹出框就会生效。

Q：openCustomDialog的levelMode的属性在API15以下会程序报错。

A：在API15及以上版本中才支持的levelMode属性，当运行在低版本系统（API15以下）时会导致兼容性问题，可能直接触发异常或者存在闪退风险 (不能识别等问题)。
