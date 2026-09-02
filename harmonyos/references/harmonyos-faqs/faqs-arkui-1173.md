---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1173
title: 如何实现图标垃圾桶
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现图标垃圾桶
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dd05360dd48cc69eff4df1ffa5e6dd519078c709108114e8636357801690aff3
---

## 问题现象

如何实现存在一个垃圾桶区域，将指定图标拖入后可将图标删除。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/ZprjzDu-RvSHSJW6gGpr2g/zh-cn_image_0000002658929095.png "点击放大")

## 背景知识

* [拖拽事件](../harmonyos-references/ts-universal-events-drag-drop.md)：拖拽事件是指在用户界面中，当用户拖动某个对象（如文件、控件或元素）时触发的一系列事件。这些事件允许开发者自定义拖拽行为，实现诸如拖放、调整位置等功能。其中绑定onDrop事件的组件可作为拖拽操作的释放目标。当在本组件范围内停止拖放行为时，将触发回调。
* [visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)：控制组件的显示或隐藏。当未设置visibility时，组件默认为显示。

## 解决方案

想要实现预期效果，可分为两步：

1. 图标拖拽效果：Image组件自带可拖拽属性，想要实现拖拽效果，需要在Image组件开始被拖动时，将原始位置的组件隐藏，且拖拽结束时如果未进入垃圾桶区域，则让图标回归原位，可通过设置visibility属性实现。若图标被拖入垃圾桶，则通过改变if内boolean值不再展示图标。

   ```ts
   if (this.ifNeed) {
     // $r('app.media.startIcon')需要替换为开发者所需的图片资源文件
     Image($r('app.media.startIcon'))
       .width(100)
       .height(100)
       .draggable(true)
       .visibility(this.imgState)
       .onDragStart(() => {
         this.imgState = Visibility.Hidden;
       })
       .onDragEnd(() => {
         this.imgState = Visibility.Visible;
       });
   }
   ```
2. 拖入垃圾桶删除图标：需要实现图标拖入指定区域后，将原处的图标删除。可以使用onDrop事件实现，图标拖入后则触发修改是否展示图标的boolean值，使图标不再展示。

   ```ts
   Column()
     .margin({ left: 15 })
     .backgroundColor('#F1F3F5')
     .borderRadius(8)
     // 图标拖入后将boolean值修改，不再展示图标
     .onDrop(() => {
       this.ifNeed = false;
     })
   ```
3. 完整示例参考如下：

   ```ts
   @Entry
   @Component
   struct DropExample {
     @State ifNeed: boolean = true;
     @State imgState: Visibility = Visibility.Visible;

     build() {
       Row() {
         Column() {
           if (this.ifNeed) {
             // $r('app.media.startIcon')需要替换为开发者所需的图片资源文件
             Image($r('app.media.startIcon'))
               .width(100)
               .height(100)
               .draggable(true)
               .visibility(this.imgState)
               .onDragStart(() => {
                 this.imgState = Visibility.Hidden;
               })
               .onDragEnd(() => {
                 this.imgState = Visibility.Visible;
               });
           }
         }.width('45%')
         .height('100%');

         Column() {
           Text('垃圾桶区域')
             .fontSize(20)
             .width(180)
             .height(40)
             .textAlign(TextAlign.Center)
             .margin(10);
           Column()
             .margin({ left: 15 })
             .backgroundColor('#F1F3F5')
             .borderRadius(8)
             // 图标拖入后将boolean值修改，不再展示图标
             .onDrop(() => {
               this.ifNeed = false;
             })
             .width(150)
             .height(150);
         }.width('45%')
         .height('100%')
         .margin({ left: '5%' });
       }
       .height('100%');
     }
   }
   ```
