---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1276
title: Navigation在分栏模式下，如何给右侧空白部分设置默认页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Navigation在分栏模式下，如何给右侧空白部分设置默认页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e42fdd15f5d11576f292a3159d19a7b330ec63774f5e5adac005ce3ef18d997c
---

## 问题现象

Navigation在Split模式下，未点击左侧导航栏时，右侧子页显示区显示为空白。当未进行页面路由推送时，如何给右侧的空白部分设置默认展示页面？

## 背景知识

* [Navigation组件](../harmonyos-references/ts-basic-components-navigation.md)的分栏模式由[mode属性](../harmonyos-references/ts-basic-components-navigation.md#mode9)控制，包括单栏（Stack）、分栏（Split）和自适应（Auto）三个属性。该属性默认为Auto模式，在该模式下会自动监听屏幕属性，当为折叠屏或平板时，默认分栏显示，在折叠状态或普通手机时可为单栏显示。
* [splitPlaceholder](../harmonyos-references/ts-basic-components-navigation.md#splitplaceholder20)：在API20下，Navigation双栏模式支持设置右侧页面显示默认占位页，占位页仅作为UI展示页，不可获焦和响应事件。

## 解决方案

* **方案一：push方法推送默认页面。**
  1. 编写默认页面，并重写[onBackPressed](../harmonyos-references/ts-basic-components-navdestination.md#onbackpressed10)返回，当在该页面返回时直接退出软件。
  2. Navigation主页执行aboutToAppear，将默认页面加入页面栈进行默认显示。

     ```ts
     import { window } from '@kit.ArkUI';

     @Entry
     @Component
     struct NavigationExample {
       @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
       private arr: number[] = [1, 2, 3];

       aboutToAppear(): void {
         this.pageInfos.pushPath({ name: 'DefaultPage' });
       }

       @Builder
       PageMap(name: string) {
         if (name === 'NavDestinationTitle1') {
           pageOneTmp();
         } else if (name === 'NavDestinationTitle2') {
           pageTwoTmp();
         } else if (name === 'NavDestinationTitle3') {
           pageThreeTmp();
         } else if (name === 'DefaultPage') {
           DefaultPage();
         }
       }

       build() {
         Column() {
           Navigation(this.pageInfos) {
             TextInput({ placeholder: 'search...' })
               .width('90%')
               .height(40)
               .backgroundColor('#FFFFFF');
             List({ space: 12 }) {
               ForEach(this.arr, (item: number) => {
                 ListItem() {
                   Text('Page' + item)
                     .width('100%')
                     .height(72)
                     .backgroundColor('#FFFFFF')
                     .borderRadius(24)
                     .fontSize(16)
                     .fontWeight(500)
                     .textAlign(TextAlign.Center)
                     .onClick(() => {
                       this.pageInfos.pushPath({ name: 'NavDestinationTitle' + item });
                     });
                 };
               }, (item: number) => item.toString());
             }
             .width('90%')
             .margin({ top: 12 });
           }
           .title('主标题')
           .mode(NavigationMode.Split)
           .navDestination(this.PageMap);
         }
         .height('100%')
         .width('100%')
         .background('#F1F3F5');
       }
     }

     // PageOne页面
     @Component
     export struct pageOneTmp {
       @Consume('pageInfos') pageInfos: NavPathStack;

       build() {
         NavDestination() {
           Column() {
             Text('NavDestinationContent1');
           }.width('100%').height('100%').justifyContent(FlexAlign.Center);
         }.title('NavDestinationTitle1');
       }
     }

     // PageTwo页面
     @Component
     export struct pageTwoTmp {
       @Consume('pageInfos') pageInfos: NavPathStack;

       build() {
         NavDestination() {
           Column() {
             Text('NavDestinationContent2');
           }.width('100%').height('100%').justifyContent(FlexAlign.Center);
         }.title('NavDestinationTitle2');
       }
     }

     // PageThree页面
     @Component
     export struct pageThreeTmp {
       @Consume('pageInfos') pageInfos: NavPathStack;

       build() {
         NavDestination() {
           Column() {
             Text('NavDestinationContent3');
           }.width('100%').height('100%').justifyContent(FlexAlign.Center);
         }.title('NavDestinationTitle3');
       }
     }
     @Component
     export struct DefaultPage {
       @Consume('pageInfos') pageInfos: NavPathStack;

       build() {
         NavDestination() {
           Column() {
             Text('DefaultPage');
           }.width('100%').height('100%').justifyContent(FlexAlign.Center);
         }.title('DefaultPage')
         .onBackPressed(() => {
           // 返回true表示自定义返回，能避免返回空白页面。返回false则表示系统默认返回，会返回空白页面。
           try {
             // 需要导入window
             window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
               const errCode: number = err.code;
               if (errCode) {
                 console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
                 return;
               }
               win.minimize((err) => {
                 const errCode: number = err.code;
                 if (errCode) {
                   console.error(`Failed to minimize the window. Cause code: ${err.code}, message: ${err.message}`);
                   return;
                 }
                 console.info('Succeeded in minimizing the window.');
               });
             });
           } catch (exception) {
             console.error(`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}`);
           }
           return true;
         });
       }
     }
     ```

     实现效果如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/4r9fWdc1TRWKEo1z7sbb9Q/zh-cn_image_0000002658955337.png "点击放大")
* **方案二：采用API20中的splitPlaceholder属性。**

  详情参考：[示例14](../harmonyos-references/ts-basic-components-navigation.md#示例14设置navigation双栏模式)。

## 常见FAQ

Q：API20以下，当采用Auto模式时，如何判断是否需要推送默认显示页面？

A：可以通过以下方式在aboutToAppear中判断是否需要推送默认页面：

1. 通过设备信息@ohos.deviceInfo接口获取设备的[deviceType](../harmonyos-references/js-apis-device-info.md#常量)类型。
2. 通过屏幕属性@ohos.display的[isFoldable方法](../harmonyos-references/js-apis-display.md#displayisfoldable10)返回当前设备是否可折叠的结果。

## 总结

实现默认展示页面的方式为，创建一个默认页面，在创建主页时自动推送该默认页面即可，其他关联实现方式参照常见FAQ实现即可。
