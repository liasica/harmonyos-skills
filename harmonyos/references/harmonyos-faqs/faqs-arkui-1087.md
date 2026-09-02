---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1087
title: 实现UI组件跟随bindSheet高度变化
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现UI组件跟随bindSheet高度变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b4b6ef5970a8ae03f5da12e7bd0a3f3ff155ac7ce7bd22c1ac772888d6fe9d7b
---

## 问题现象

屏幕底部有一个按钮，当出现半模态组件时，需要将该按钮向上移动，以避让半模态组件。在半模态组件高度动态变化（非手势触发）的情况下，该按钮应始终与半模态组件保持固定距离，并实现平滑跟随效果。如何实现这一功能？

## 背景知识

* [bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md)：用于实现半模态弹窗功能。通过将该方法绑定到组件上，点击组件后即可显示半模态页面。
* [SheetOptions](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)：bindSheet的配置选项，支持对半模态弹窗进行定制。其中，detentSelection属性可用于动态切换弹窗的高度，onHeightDidChange属性可用于监听弹窗高度的变化。
* [属性动画](../harmonyos-guides/arkts-attribute-animation-apis.md#使用animateto产生属性动画)：通过为属性添加动画，可以让属性值从初始值平滑过渡到目标值，从而实现连续、流畅的动画效果。

## 解决方案

1. 在Text组件上绑定点击事件，用于动态控制半模态弹窗的显示与隐藏。同时，通过按钮的margin属性与属性动画，实现按钮在弹窗出现或隐藏时的平滑跟随效果。
2. 构建一个“切换”按钮，点击该按钮时通过修改SheetOptions中的detentSelection值，动态调整半模态弹窗的高度。同时结合按钮的margin属性与animateTo属性动画，实现按钮随弹窗高度变化的平滑跟随。
3. 通过SheetOptions的onHeightDidChange回调监听半模态弹窗的高度变化，获取手势操作时每一帧的高度值，并据此动态设置按钮的margin，从而实现按钮对弹窗高度变化的实时跟随。

   ```ts
   import { curves, LengthUnit } from '@kit.ArkUI';

   @Entry
   @Component
   export struct BindSheetAnimateDemo {
     private sheetHeights: number[] = [100, 200, 300];
     private index: number = 0;
     @State showSheet: boolean = false;
     @State dataList: string[] = [];
     @State detentSelectionVal: number = 0;
     @State marginVal: number = 0;

     aboutToAppear(): void {
       this.dataList = Array(30).fill(0).map((_value: number, index: number) => String(index));
     }

     @Builder
     demoBuilder() {
       List() {
         ForEach(this.dataList, (item: string) => {
           ListItem() {
             Text(item)
               .fontSize('18fp')
               .height('30vp')
               .margin({ left: 20 })
               .textAlign(TextAlign.Center);
           };
         });
       }
       .width('100%');
     }

     build() {
       Stack() {
         Column() {
           Button('切换')
             .width('90%')
             .height(44)
             .borderRadius(22)
             .onClick(() => {
               if (!this.showSheet) {
                 return;
               }

               this.detentSelectionVal = this.sheetHeights[(++this.index) % 3];
               this.getUIContext()?.animateTo({ curve: curves.springMotion() }, () => {
                 this.marginVal = this.detentSelectionVal;
               });
             })
             .margin({ bottom: 16, top: 50 });
           Button('按钮').width('90%').height(44).borderRadius(22).margin({ bottom: this.marginVal + 16 });
         }.height('100%').width('100%').justifyContent(FlexAlign.End);

         Text('打开半模态页面')
           .fontSize('20fp')
           .fontColor('#000000')
           .textAlign(TextAlign.Center)
           .onClick(() => {
             this.showSheet = !this.showSheet;
             this.detentSelectionVal = this.showSheet ? this.sheetHeights[0] : 0;
             this.getUIContext()?.animateTo({ curve: curves.springMotion() }, () => {
               this.marginVal = this.detentSelectionVal;
             });
           })
           .bindSheet(this.showSheet, this.demoBuilder(), {
             detentSelection: this.detentSelectionVal,
             detents: [100, 200, 300],
             enableOutsideInteractive: true,
             radius: { value: 4, unit: LengthUnit.VP },
             showClose: false,
             mode: SheetMode.EMBEDDED,
             preferType: SheetType.BOTTOM,
             scrollSizeMode: ScrollSizeMode.CONTINUOUS, // 半模态面板在滑动过程中持续更新内容显示区域。
             onHeightDidChange: (height) => {
               // 手动调整半模态高度时，保持跟随
               this.marginVal = this.getUIContext().px2vp(height);
             }
           })
           .width('100%');
       }
       .height('100%')
       .width('100%')
       .alignContent(Alignment.Top);
     }
   }
   ```
