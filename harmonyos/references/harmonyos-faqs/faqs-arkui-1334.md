---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1334
title: List自适应高度
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > List自适应高度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bc36138ae0c068e79d229d6c0c5f62ec1cd735ac3f8c50cf6f8a4fb460752cdd
---

## 问题现象

1. List如何根据其中ListItem的高度，进行高度的自适应？
2. 页面包含三个纵向排列的子组件，中间的List组件需要实现动态高度：当列表项较少时，List与父容器高度自适应内容；当列表项充满父容器时，List自动占满剩余空间并启用滚动。请问如何实现这种动态布局效果？

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)是用于展示动态数据集合的核心组件，支持滚动、动态更新等特性。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)事件在组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。可以使用该组件获取组件的高度。
* [constraintSize](../harmonyos-references/ts-universal-attributes-size.md#constraintsize)设置约束尺寸，组件布局时，进行尺寸范围限制。

## 解决方案

1. 通过给ListItem添加onAreaChange事件，通过回调获取每个ListItem组件的高度，通过对比将最大值赋值给List组件的height属性：

   ```ts
   @Entry
   @Component
   struct listDemoFirst {
     private arr: string[] = ['这是一段文本', '这是一段文本这是一段文本',
       '这是一段文本这是一段文本这是一段文本这是一段文本这是一段文本这是一段文本这是一段文本这是一段文本这是一段文本这是一段文本',
       '3', '4',
       '这是一段文本这是一段文本', '这是一段文本', '这是一段文本', '这是一段文本', '这是一段文本这是一段文本这是一段文本'];
     @State sizeValue: number = 0;

     build() {
       Row() {
         List() {
           ForEach(this.arr, (item: string) => {
             ListItem() {
               Row() {
                 Text(item)
                   .width('40%')
                   .height('auto')
                   .fontSize(16)
                   .textAlign(TextAlign.Center)
                   .borderRadius(10)
                   .backgroundColor('#FFFFFF')
               }
               .padding({top: 8, left: 16, right: 16})
               .width('100%')
               .justifyContent(FlexAlign.Center)
               .alignItems(VerticalAlign.Center)
               .onAreaChange((oldValue: Area, newValue: Area) => {
                 if (Number(newValue.height) > Number(this.sizeValue)) {
                   this.sizeValue = Number(newValue.height);
                 }
               })
             }
           }, (item: string) => item)
         }
         .scrollBar(BarState.Auto)
         .backgroundColor('#F1F3F5')
         .width('100%')
         .height(this.sizeValue)
       }
       .width('100%')
       .height('100%')
       .padding({ top: 5 })
       .justifyContent(FlexAlign.Center)
       .alignItems(VerticalAlign.Center)
     }
   }
   ```

   效果预览：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/wB60kjzRQyOCv8kSWrlrrw/zh-cn_image_0000002628600018.png "点击放大")
2. 在父容器高度受限的场景下，可通过List组件的constraintSize接口中的[ConstraintSizeOptions](../harmonyos-references/ts-types.md#constraintsizeoptions)属性设置maxHeight参数控制最大高度，实现动态伸缩布局。

   ```ts
   @Entry
   @Component
   struct Index {
     @State itemHeight: number = 200;

     build() {
       Column() {
         Column() {
           Text('内容1')
             .padding({top: 16, bottom: 8})
           Button('改变ListItem2高度').onClick(() => {
             this.itemHeight = this.itemHeight === 200 ? 900 : 200;
           })
         }
         .width('100%')
         .height(100)
         .backgroundColor('#F1F3F5')

         List() {
           ListItem() {
             Text('ListItem1')
               .padding({top: 16})
           }
           .width('100%')

           ListItem() {
             Text('ListItem2')
           }
           .height(this.itemHeight)
           .width('100%')
         }
         .constraintSize({ maxHeight: 'calc(100% - 200vp)' })

         Column() {
           Text('内容2')
             .padding({top: 16})
         }
         .width('100%').
         height(100).
         backgroundColor('#F1F3F5')
       }
       .width('100%')
       .height('100%')
     }
   }
   ```

   效果预览：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/2IXyqgVSRYSLNDecfyFHQg/zh-cn_image_0000002628759924.png "点击放大")

## 常见FAQ

Q：在问题现象2中若无法确定其他子组件的高度，maxHeight该如何确定需要减去的高度？

A：可以使用onAreaChange获取其他子组件的高度。

Q：List组件如何自适应高度？

A：List组件嵌套在Scroll下可以实现自适应高度效果，List组件本身不设置固定高度，它会根据内容实际高度展示。
