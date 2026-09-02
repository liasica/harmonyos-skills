---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-956
title: 如何实现连续点击小圆点的动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现连续点击小圆点的动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:08d4b0db97b432ed2f42f386d0e8009a066bf29dded93c6a165696d0999c536e
---

## 问题现象

在页面上根据手指点击动态增加小圆点，1秒后自动淡出，要求可以连续点击，后面的点击不会影响前面点击的小圆点动画，这种功能需要如何实现？效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/gAU_PGU9Q3yz5VcTEQ__uw/zh-cn_image_0000002628561176.png "点击放大")

## 背景知识

* 通过动画属性改变引起UI上产生的连续视觉效果，即为[属性动画](../harmonyos-guides/arkts-attribute-animation-apis.md)。属性动画是最基础易懂的动画，ArkUI提供三种属性动画接口[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)、[animation](../harmonyos-references/ts-animatorproperty.md)和[keyframeAnimateTo](../harmonyos-references/ts-keyframeanimateto.md)驱动组件属性按照动画曲线等动画参数进行连续的变化，产生属性动画。
* [opacity](../harmonyos-references/ts-universal-attributes-opacity.md#opacity)是HarmonyOS提供的一种通用属性，用于设置组件的不透明度。

## 解决方案

1. 点击事件获取坐标：在屏幕上点击时，通过事件对象获取点击位置相对于屏幕的坐标。

   ```ts
   .onClick((e) => {
     this.indexArray[this.index].top = e.y;
     this.indexArray[this.index].left = e.x;
     this.display(this.indexArray[this.index]);
     this.index = this.index + 1 >= 20 ? 0 : this.index + 1;
   });
   ```
2. 循环渲染小圆点：使用ForEach循环渲染数组或Map中记录的小圆点，每个小圆点根据其位置信息进行定位。

   ```ts
   ForEach(this.indexArray, (test: Test) => {
     Dot({ test: test });
   }, (test: Test, index: number) => {
     return test.top + ':' + test.left + ':' + index;
   });
   ```
3. 定时删除小圆点：在创建小圆点时，设置一个定时器，在指定时间后移除该小圆点的记录。

   ```ts
   hide(test: Test) {
     this.getUIContext().animateTo({ duration: 1000 }, () => {
       test.is = false;
     });
   }
   ```

   完整示例参考如下：

   ```ts
   @Entry
   @Component
   struct ClickDotPage {
     @State indexArray: Test[] = [];
     @State index: number = 0;

     display(test: Test) {
       this.getUIContext().animateTo({ duration: 1000 }, () => {
         test.is = true;
       });
       setTimeout(() => {
         this.hide(test);
       }, 1000);
     }

     hide(test: Test) {
       this.getUIContext().animateTo({ duration: 1000 }, () => {
         test.is = false;
       });
     }

     aboutToAppear(): void {
       // 初始化数据
       for (let i = 0; i < 20; i++) {
         this.indexArray.push(new Test(0, 0));
       }
     }

     build() {
       Stack() {
         // 在Stack组件中循环渲染数组或Map中记录的小圆点，每个小圆点根据其位置信息进行定位
         ForEach(this.indexArray, (test: Test) => {
           Dot({ test: test });
         }, (test: Test, index: number) => {
           return test.top + ':' + test.left + ':' + index;
         });
       }.width('100%')
       .height('100%')
       .alignContent(Alignment.TopStart)
       // 点击事件获取坐标
       .onClick((e) => {
         this.indexArray[this.index].top = e.y;
         this.indexArray[this.index].left = e.x;
         this.display(this.indexArray[this.index]);
         this.index = this.index + 1 >= 20 ? 0 : this.index + 1;
       });

     }
   }

   @Component
   struct Dot {
     @ObjectLink test: Test;
     private w: number = 30;

     build() {
       if (this.test.is) {
         Row()
           .width(this.w)
           .height(this.w)
           .borderRadius(this.w)
           .backgroundColor(Color.Blue)
           .margin({ left: this.test.left, top: this.test.top })
           .transition({
             opacity: 0
           });
       }
     }
   }

   @Observed
   class Test {
     top: number;
     left: number;
     is: boolean = false;

     constructor(top: number, left: number) {
       this.top = top;
       this.left = left;
     }
   }
   ```
