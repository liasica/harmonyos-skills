---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-648
title: 三维旋转loading动效
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 三维旋转loading动效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:16a9fa31901015a4920d0687b5adc4f0fed07de89b359e6b3a4b24d089ed7adf
---

## 问题现象

如何实现具有三维旋转效果的加载动画界面？

## 背景知识

* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)提供接口来指定由于闭包代码导致的状态变化插入过渡动效。
* [rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)是一种通用属性，可用于设置组件的旋转。

## 解决方案

1. 调用animateTo动画函数，将旋转参数从初始值过渡到目标值并通过设置iterations:-1，实现无限循环。

   ```ts
   this.getUIContext()?.animateTo({
     duration: 2000,
     // 动画播放次数，设置为-1时表示无限次播放
     iterations: -1,
     curve: Curve.Linear
   }, () => {
     this.num = 360;
     this.numZ = 470;
     this.twonum = 450;
     this.twonumZ = 470;
     this.treenum = 480;
     this.treenumZ = 450;
     this.formnum = 610;
     this.formnumZ = 630;
   });
   ```
2. 通过rotate方法设置x/y/z轴旋转分量和旋转中心点(centerX/Y)，实现空间错位效果。

   ```ts
   .rotate({
     x: 50,
     y: 0,
     z: this.numZ,
     angle: this.num,
     centerX: 80,
     centerY: 80,
   });
   ```
3. 完整示例参考如下：

   ```ts
   @Entry
   @Component
   struct RotatingAnimationDemo {
     @State num: number = 0;
     @State numZ: number = 100;
     @State twonum: number = 90;
     @State twonumZ: number = 90;
     @State treenum: number = 180;
     @State treenumZ: number = 90;
     @State formnum: number = 270;
     @State formnumZ: number = 270;

     onDidBuild(): void {
       this.getUIContext()?.animateTo({
         duration: 2000,
         // 动画播放次数，设置为-1时表示无限次播放
         iterations: -1,
         curve: Curve.Linear
       }, () => {
         this.num = 360;
         this.numZ = 470;
         this.twonum = 450;
         this.twonumZ = 470;
         this.treenum = 480;
         this.treenumZ = 450;
         this.formnum = 610;
         this.formnumZ = 630;
       });
     };

     build() {
       Stack() {
         Row() {
         }
         .width(190)
         .height(190)
         .border({ width: { bottom: 8 }, color: 'rgb(255, 141, 249)', style: BorderStyle.Solid })
         .borderRadius(90)
         .rotate({
           x: 50,
           y: 0,
           z: this.numZ,
           angle: this.num,
           centerX: 80,
           centerY: 80,
         });
         Row() {
         }
         .width(190)
         .height(190)
         .border({ width: { bottom: 8 }, color: 'rgb(255, 65, 106)', style: BorderStyle.Solid })
         .borderRadius(90)
         // 设置组件的旋转参数
         .rotate({
           x: 20, // 旋转轴向量x坐标
           y: 50, // 旋转轴向量y坐标
           z: this.twonumZ,
           angle: this.twonum, // 旋转角度
           centerX: 80, // 变换中心点x轴坐标
           centerY: 80,
         });

         Row() {
         }
         .width(190)
         .height(190)
         .border({ width: { bottom: 8 }, color: 'rgb(0, 255, 255)', style: BorderStyle.Solid })
         .borderRadius(90)
         .rotate({
           x: 40,
           y: 150,
           z: this.treenumZ,
           angle: this.treenum,
           centerX: 80,
           centerY: 80,
         });

         Row() {
         }
         .width(190)
         .height(190)
         .border({ width: { bottom: 8 }, color: 'rgb(252, 183, 55)', style: BorderStyle.Solid })
         .borderRadius(90)
         .rotate({
           x: 70,
           y: 0,
           z: this.formnumZ,
           angle: this.formnum,
           centerX: 80,
           centerY: 80,
         });
         Row() {
           Text('loading...')
             .fontColor(Color.White);
         }
       }
       .width('100%')
       .height('100%')
       .backgroundColor('#212121')
     }
   }
   ```

   效果图为：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/_5iN7d2eRaOI5lOG40Utsg/zh-cn_image_0000002628394516.png "点击放大")
