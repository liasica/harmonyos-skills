---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-939
title: 实现跨页面的同步旋转图片动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现跨页面的同步旋转图片动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:51ac0b2783f6653d35775fe366c612d7f8894c4685744cb854cb63d7c75e85e9
---

## 问题现象

如何在两个页面中实现Image组件的旋转动画同步，通过共享全局状态触发动画更新？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/GV0bX8TyQ8uKOQxPifnE_Q/zh-cn_image_0000002658920411.gif "点击放大")

## 背景知识

* [AppStorage](../harmonyos-guides/arkts-appstorage.md)是应用级全局UI状态存储容器，由UI框架在应用启动时创建，用于存储运行内存中的UI状态数据。
* [Image](../harmonyos-references/ts-basic-components-image.md)是UI框架中用于渲染图片的核心组件，支持多种格式和动态加载能力，[rotate](../harmonyos-references/js-apis-sendableimage.md#rotate)是其配套的修饰符属性，通过指定旋转角度对图片进行旋转变形，支持动态绑定状态值。

## 解决方案

通过AppStorage全局状态管理实现两个页面中Image组件旋转动画的同步，具体如下：

1. 通过AppStorage共享startFlag状态：页面1通过AppStorage.set()修改状态；页面2通过AppStorage.get()读取状态。
2. 使用@StorageProp('startFlag')装饰器绑定startFlag状态，当startFlag变化时，触发change()方法动态更新旋转角度和动画时长，从而控制Image的旋转动画。

   ```screen
   // PageOne
   @Entry
   @Component
   struct Index {
     @StorageProp('startFlag') @Watch('change') startFlag: boolean = false;
     @State rotateValue: number = 0;
     @State ifStop: number = -1;
     @State duration: number = 4000;

     change() {
       console.info(`startFlag: ${this.startFlag}`);
       if (this.startFlag) {
         this.duration = 4000;
         this.rotateValue = 360;
       } else {
         this.rotateValue = 0;
       }
     }

     build() {
       Column({ space: 30 }) {
         Button('点击')
           .onClick(() => {
             this.getUIContext().getRouter().pushUrl({
               url: 'pages/Index2',
               params: {
                 flag: '1',
               }
             });
           });

         // 此处'app.media.startIcon'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
         Image($r('app.media.startIcon'))
           .width(200)
           .aspectRatio(1)
           .borderRadius(100)
           .rotate({
             angle: this.rotateValue
           })
           .animation({
             duration: this.duration,
             iterations: -1, // 动画重复次数
             curve: Curve.Linear,
             delay: 1, // 延迟时间
             playMode: PlayMode.Normal
           });

         Button('旋转').onClick(() => {
           this.duration = 4000;
           this.rotateValue = 360;
           AppStorage.set('startFlag', true);
         });

         Button('停止').onClick(() => {
           this.duration = 0;
           this.rotateValue = 0;
           AppStorage.set('startFlag', false);
         });
       }
       .justifyContent(FlexAlign.Center)
       .height('100%')
       .width('100%');
     }
   }
   ```

   ```screen
   // PageTwo
   @Entry
   @Component
   struct Index2 {
     @State rotateValue: number = 0;
     @State duration: number = 4000;
     @State pauseFlag: boolean = false;

     onPageShow(): void {
       const startFlag = AppStorage.get('startFlag') as boolean;
       console.info(`页面二：startFlag: ${startFlag}`);
       if (startFlag) {
         this.duration = 4000;
         this.rotateValue = 360;
       } else {
         this.duration = 0;
         this.rotateValue = 0;
       }
     }

     build() {
       Column({ space: 30 }) {
         // 此处'app.media.startIcon'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
         Image($r('app.media.startIcon'))
           .width(200)
           .aspectRatio(1)
           .borderRadius(100)
           .rotate({
             angle: this.rotateValue
           })
           .animation({
             duration: this.duration,
             iterations: -1, // 动画重复次数
             curve: Curve.Linear,
             delay: 1, // 延迟时间
             playMode: PlayMode.Normal
           });

         Button('旋转').onClick(() => {
           this.duration = 4000;
           this.rotateValue = 360;
           AppStorage.set('startFlag', true);
         });

         Button('停止').onClick(() => {
           this.duration = 0;
           this.rotateValue = 0;
           AppStorage.set('startFlag', false);
         });

         Button('返回').onClick(() => {
           this.getUIContext().getRouter().back({
             url: 'pages/Index',
             params: this.pauseFlag
           });
         });
       }
       .justifyContent(FlexAlign.Center)
       .height('100%')
       .width('100%');
     }
   }
   ```

   ```screen
   {
     "src": [
       "pages/Index",
       "pages/Index2"
     ]
   }
   ```
