---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-color-picker-favorites
title: 颜色选择与收藏管理
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 颜色选择与收藏管理
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:58+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:6127fe6803e4342d3b0fa89f171b6184ef095ec60540df5efb5b81e8d2624ba4
---

## 场景介绍

从26.0.0版本开始，新增支持颜色选择与收藏管理功能。

[HdsColorPicker (颜色选择器组件)](../harmonyos-references/ui-design-hdscolorpicker.md)支持完整的颜色选择与收藏管理功能。当应用开发者需要为用户提供颜色选择、主题配置、画笔颜色设置等功能时，可以通过HdsColorPicker组件实现。该组件提供三种颜色选择模式：

* **网格模式（GRID）**：提供预设颜色网格，方便用户快速选择常用颜色。
* **光谱模式（SPECTRUM）**：提供色相和饱和度光谱，支持精细的颜色调节。
* **滑块模式（SLIDERS）**：提供HSB滑块，支持通过色相、饱和度、明度三个维度精确调节颜色。

同时，组件支持颜色收藏功能，用户可以将常用颜色添加到收藏列表，方便后续快速选择。

## 约束条件

[HdsColorPicker](../harmonyos-references/ui-design-hdscolorpicker.md#hdscolorpicker)支持设备：Phone、Tablet，取色能力受手写笔Pen Kit的[全局取色能力](pen-image-feature-picker.md)约束。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { HdsColorPicker, HdsColorPickerTabType } from '@kit.UIDesignKit';
   ```
2. 创建页面组件，定义状态变量用于存储当前选中颜色和收藏颜色列表。在build方法中创建HdsColorPicker组件，设置初始颜色和收藏颜色，并监听颜色选择和收藏更新事件。

   ```typescript
    @Entry
    @ComponentV2
    struct ColorPickerExample {
      // 当前选中的颜色
      @Local selectedColor: string = '#FFFF0000';
      // 收藏颜色列表
      @Local favoriteColors: Array<string> = ['#FFFF0000', '#FF00FF00', '#FF0000FF'];

      build() {
        Column() {
          // 显示当前选中的颜色
          Text('当前选中颜色: ' + this.selectedColor)
            .fontSize(16)
            .margin({ bottom: 10 })

          // 颜色预览区域
          Row() {
            Column()
              .width(100)
              .height(100)
              .backgroundColor(this.selectedColor)
              .borderRadius(12)
          }
          .width('100%')
          .justifyContent(FlexAlign.Center)
          .margin({ bottom: 20 })

          // 收藏颜色展示
          Text('收藏颜色: ' + this.favoriteColors.join(', '))
            .fontSize(14)
            .margin({ bottom: 10 })

          // HdsColorPicker 组件
          HdsColorPicker({
            initialColor: this.selectedColor,
            initialFavoriteColors: this.favoriteColors,
            options: {
              circleRadius: 12,
              tabs: [HdsColorPickerTabType.GRID, HdsColorPickerTabType.SPECTRUM, HdsColorPickerTabType.SLIDERS]
            },
            onColorSelected: (color: string) => {
              this.selectedColor = color;
              console.info('选中颜色: ' + color);
            },
            onFavoriteColorsUpdate: (favorites: Array<string>) => {
              this.favoriteColors = favorites;
              console.info('收藏颜色更新: ' + favorites.join(', '));
            }
          })
            .width('100%')
            .height(500)
        }
        .width('100%')
        .height('100%')
        .padding(20)
      }
    }
   ```
3. （可选）通过[HdsColorPickerOptions](../harmonyos-references/ui-design-hdscolorpicker.md#hdscolorpickeroptions)可以配置自定义颜色选择器选项。

   示例：仅显示网格和滑块两种模式

   ```typescript
   options: {
     circleRadius: 16,
     tabs: [HdsColorPickerTabType.GRID, HdsColorPickerTabType.SLIDERS]
   }
   ```
