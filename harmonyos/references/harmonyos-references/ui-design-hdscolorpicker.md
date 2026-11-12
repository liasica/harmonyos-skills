---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdscolorpicker
title: HdsColorPicker (颜色选择器组件)
breadcrumb: API参考 > 应用框架 > UI Design Kit（UI设计套件） > ArkTS组件 > HdsColorPicker (颜色选择器组件)
category: harmonyos-references
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5b383a87f7af01e919f57e6a5399a9cd8cfd07bee3d4a0a6bf33786e7d2d7e64
---

提供颜色选择与收藏管理功能的组件，支持网格、光谱和滑块三种颜色选择模式。

**起始版本：** 26.0.0

## 导入模块

```typescript
import { HdsColorPicker, HdsColorPickerTabType, HdsColorPickerOptions } from '@kit.UIDesignKit';
```

## 子组件

无

## 属性

不支持[通用属性](ts-component-general-attributes.md)。

## 事件

不支持[通用事件](ts-component-general-events.md)。

## HdsColorPicker

HdsColorPicker({initialColor?: string, onColorSelected: HdsColorSelectedCallback, initialFavoriteColors?: Array<string>, onFavoriteColorsUpdate?: HdsFavoritesUpdateCallback, options?: HdsColorPickerOptions, isColorPickerShow?: boolean, onShowStatusChanged?: HdsColorPickerShowStatusChangeEvent})

定义颜色选择器组件。

**装饰器类型：** @ComponentV2

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 26.0.0

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| initialColor | string | 否 | @Param | 设置颜色选择器的初始颜色，颜色值支持十六进制ARGB标准颜色格式（如'#FFFF0000'）。 默认值：undefined。 |
| onColorSelected | [HdsColorSelectedCallback](ui-design-hdscolorpicker.md#hdscolorselectedcallback) | 是 | @Event | 颜色选择回调，当用户选择颜色时触发。 |
| initialFavoriteColors | Array<string> | 否 | @Param  @Once | 设置颜色选择器的初始收藏颜色列表，颜色值支持十六进制ARGB标准颜色格式（如'#FFFF0000'）。  **说明**：@Once装饰器，仅在组件首次渲染时生效，后续更新不会触发重新渲染。 |
| onFavoriteColorsUpdate | [HdsFavoritesUpdateCallback](ui-design-hdscolorpicker.md#hdsfavoritesupdatecallback) | 否 | @Event | 收藏颜色更新回调，当收藏颜色列表发生变化时触发，最多可收藏并显示72个颜色值。 |
| options | [HdsColorPickerOptions](ui-design-hdscolorpicker.md#hdscolorpickeroptions) | 否 | @Param | 颜色选择器组件选项。 |
| isColorPickerShow | boolean | 否 | @Param | 设置颜色选择器的显示状态。  设置为false时隐藏颜色选择器，设置为true时显示颜色选择器。默认值：false。  **起始版本：** 26.0.1 |
| onShowStatusChanged | [HdsColorPickerShowStatusChangeEvent](ui-design-hdscolorpicker.md#hdscolorpickershowstatuschangeevent) | 否 | @Event | 颜色选择器显示状态变化回调，当颜色选择器的显示状态发生变化时触发。  **起始版本：** 26.0.1 |

## HdsColorPickerOptions

定义颜色选择器的配置选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| circleRadius | number | 否 | 是 | 设置颜色选择器圆形元素的半径，单位：vp。  默认值：12vp  **说明**：  设置的值应为整数，当设置的值小于10时，均默认取值为10。 |
| tabs | [HdsColorPickerTabType](ui-design-hdscolorpicker.md#hdscolorpickertabtype)[] | 否 | 是 | 设置颜色选择器的标签页类型列表。  默认值：[HdsColorPickerTabType.GRID, HdsColorPickerTabType.SPECTRUM, HdsColorPickerTabType.SLIDERS]。 |

## HdsColorPickerTabType

定义颜色选择器的标签页类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GRID | 0 | 网格样式，提供预设颜色网格选择。 |
| SPECTRUM | 1 | 光谱样式，提供色相和饱和度光谱选择。 |
| SLIDERS | 2 | 滑块样式，提供色相、饱和度、明度滑块调节选择。 |

## HdsColorSelectedCallback

type HdsColorSelectedCallback = (selectedColor: string) => void

定义颜色选择回调函数类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectedColor | string | 是 | 用户选择的颜色值，颜色值支持十六进制ARGB标准颜色格式（如'FFFF0000'）。 |

## HdsFavoritesUpdateCallback

type HdsFavoritesUpdateCallback = (favoritesList: Array<string>) => void

定义收藏颜色更新回调函数类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| favoritesList | Array<string> | 是 | 更新后的收藏颜色列表，颜色值支持十六进制ARGB标准颜色格式（如'FFFF0000'）。 |

## HdsColorPickerShowStatusChangeEvent

type HdsColorPickerShowStatusChangeEvent = (isShow: boolean) => void

定义颜色选择器显示状态变化回调函数类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isShow | boolean | 是 | 颜色选择器当前是否显示。true表示颜色选择器已显示，false表示颜色选择器已隐藏。 |

## 示例

HdsColorPicker提供完整的颜色选择与收藏管理功能：

```typescript
import { HdsColorPicker, HdsColorPickerTabType } from '@kit.UIDesignKit';

@Entry
@ComponentV2
struct ColorPickerExample {
  // 当前选中的颜色
  @Local selectedColor: string = '#FF0000';
  // 收藏颜色列表
  @Local favoriteColors: Array<string> = ['#FF0000', '#00FF00', '#0000FF'];
  // 颜色选择器显示状态
  @Local isColorPickerShow: boolean = false;

  build() {
    Column({space: 10}) {
      // 显示当前选中的颜色
      Text('当前选中颜色：' + this.selectedColor)
        .fontSize(16)

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

      // 收藏颜色展示
      Text('收藏颜色：' + this.favoriteColors.join(', '))
        .fontSize(14)

      // HdsColorPicker 组件
      HdsColorPicker({
        initialColor: this.selectedColor,
        initialFavoriteColors: this.favoriteColors,
        isColorPickerShow: this.isColorPickerShow,
        options: {
          circleRadius: 12,
          tabs: [HdsColorPickerTabType.GRID, HdsColorPickerTabType.SPECTRUM, HdsColorPickerTabType.SLIDERS]
        },
        onColorSelected: (color: string) => {
          this.selectedColor = color;
          console.info('选中颜色：' + color);
        },
        onFavoriteColorsUpdate: (favorites: Array<string>) => {
          this.favoriteColors = favorites;
          console.info('收藏颜色更新：' + favorites.join(', '));
        },
        onShowStatusChanged: (isShow: boolean) => {
          this.isColorPickerShow = isShow;
          console.info('颜色选择器显示状态：' + isShow);
        }
      })
        .alignSelf(ItemAlign.Center)

      // 控制颜色选择器显隐的按钮
      Button(this.isColorPickerShow ? '隐藏颜色选择器' : '显示颜色选择器')
        .onClick(() => {
          this.isColorPickerShow = !this.isColorPickerShow;
        })
    }
    .width('100%')
    .height('100%')
    .padding(20)
  }
}
```

## 效果展示

执行上述示例中的代码，进行颜色选择，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/r5rrS0eTQteU4QV8Kj_Gdw/zh-cn_image_0000002786522022.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233241Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5D152F40708C44A06B20CF8E737AA9D7582A373E70DD13B57A11EBB1F3FF48C "点击放大")
