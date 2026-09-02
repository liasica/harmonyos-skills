---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-682
title: 如何实现应用级别的全局置顶弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现应用级别的全局置顶弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e0ff3d97742f7e9498637bd1ec56ee67f29025b953297c6e6c7dfd8c1a6f27d0
---

## 问题现象

如何实现应用级别的全局置顶弹窗？要求切换页面弹窗不消失，一直显示在页面之上。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/PdyOVrauTVCjPXBNVsOVGg/zh-cn_image_0000002658914065.png "点击放大")

## 背景知识

* [Navigation](../harmonyos-guides/arkts-navigation-navigation.md)主要用于实现页面间以及组件内部的页面跳转，支持在不同组件间传递跳转参数，提供灵活的跳转栈操作，从而更便捷地实现对不同页面的访问和复用。
* [CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)是自定义弹出框，可用于广告、中奖、警告、软件更新等与用户交互响应操作。开发者可以通过CustomDialogController类显示自定义弹出框。

## 解决方案

使用CustomDialog，设置isModal:false隐藏遮罩效果，可以实现页面上未被弹窗覆盖的区域仍可交互，不影响用户的其他操作，同时使用Navigation实现页面跳转，由于弹窗是独立组件，不受页面栈影响，因此弹窗会一直显示在页面最上层。

1. Index.ets页面。

   ```ts
   @Builder
   export function MainPageBuilder() {
     Index();
   }

   @CustomDialog
   export struct TestDialogController {
     controller?: CustomDialogController;
     cancel: () => void = () => {
     };
     confirm: () => void = () => {
     };

     build() {
       Column() {
         Text('温馨提示')
           .margin({ top: 16 })
           .fontSize(20)
           .fontWeight(FontWeight.Bold);
         Text('在今年的诸多春节销金窟中，炒货荣登刺客榜首。消费者反映，手剥松子等常见坚果单价突破百元，单次采购花费达数百元，社交媒体热议“炒货自由”难实现')
           .fontSize(16)
           .margin({ top: 16, left: 24, right: 24 });
         Button('知道了')
           .margin({ top: 8, bottom: 16 })
           .onClick(() => {
             if (this.controller != undefined) {
               this.controller.close();
             }
           });
       }
       .width('90%')
       .backgroundColor('#F1F3F5')
       .borderRadius(20);
     }
   }

   @Entry
   @Component
   struct Index {
     pageInfos: NavPathStack = new NavPathStack();
     dialogController: CustomDialogController | null = new CustomDialogController({
       builder: TestDialogController(),
       alignment: DialogAlignment.Center,
       customStyle: true,
       autoCancel: false, // 是否允许点击遮障层退出
       isModal: false, // 是否有蒙层
       width: '80%',
       height: 200,
       cornerRadius: 20,
     });

     onPageShow(): void {
       this.dialogController?.open();
     }

     build() {
       Navigation(this.pageInfos) {
         Row({ space: 20 }) {
           Button('打开弹窗')
             .fontSize(16)
             .backgroundColor('#0A59F7')
             .onClick(() => {
               this.dialogController?.open();
             });
           Button('页面跳转')
             .fontSize(16)
             .backgroundColor('#0A59F7')
             .onClick(() => {
               this.pageInfos.pushPathByName('routerPage', null);
             });
         }
         .margin({ top: 15 });
       }
       .backgroundColor(Color.White);
     }
   }
   ```
2. 路由跳转页面RouterPage.ets。

   ```ts
   @Builder
   export function RouterPageBuilder() {
     RouterPage();
   }

   @Entry
   @Component
   struct RouterPage {
     @State message: string = '点击这里可交互';

     build() {
       NavDestination() {
         Row() {
           Text(this.message)
             .fontSize(16)
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               this.message = '值已修改';
             });
         }
       }
       .backgroundColor(Color.White);
     }
   }
   ```
3. 在工程配置文件module.json5中配置{"routerMap": "$profile:router\_map"}，并在“src/main/resources/base/profile”路径下创建配置文件router\_map.json。

   ```html
   {
     "routerMap": [
       {
         "name": "Index",
         "pageSourceFile": "src/main/ets/pages/Index.ets",
         "buildFunction": "MainPageBuilder",
         "data": {
           "description": "This is mainPage"
         }
       },
       {
         "name": "routerPage",
         "pageSourceFile": "src/main/ets/pages/RouterPage.ets",
         "buildFunction": "RouterPageBuilder",
         "data": {
           "description": "This is RouterPage"
         }
       }
     ]
   }
   ```
