---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-statestyles
title: stateStyles：多态样式
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 组件扩展 > stateStyles：多态样式
category: harmonyos-guides
scraped_at: 2026-09-05T06:13:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:809a084cb534d7166455e941134ca61791396f4110fc2b8c48c5ac98b4e56ccb
---

@Styles仅应用于静态页面的样式复用，stateStyles可以依据组件的内部状态的不同，快速设置不同样式。这就是我们本章要介绍的内容stateStyles（又称为：多态样式）。

**说明** 

多态样式仅支持通用属性。如果多态样式不生效，则该属性可能为组件的私有属性，例如：[fontColor](../harmonyos-references/ts-basic-components-button.md#fontcolor)、[TextInput](../harmonyos-references/ts-basic-components-textinput.md)组件的[backgroundColor](../harmonyos-references/ts-universal-attributes-background.md#backgroundcolor)等。此时，可以通过[attributeModifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置组件属性来解决此问题。

## 概述

stateStyles是属性方法，可以根据UI内部状态来设置样式，类似于css伪类，但语法不同。ArkUI提供以下七种状态：

* focused：获焦态。
* normal：正常态。
* pressed：按压态。
* disabled：不可用态。
* clicked：点击态。
* selected10+：选中态。
* hovered：悬浮态。**起始版本：** 26.0.0

**说明** 

获焦态目前仅支持通过外接键盘的Tab键或方向键触发，不支持在嵌套滚动组件场景下通过按键触发。

## 使用场景

### 基础场景

下面的示例展示了stateStyles最基本的使用场景。Button1处于第一个组件，Button2处于第二个组件。按压时显示为pressed态指定的灰色。使用Tab键走焦，Button1获焦并显示为focused态指定的粉色。当Button2获焦的时候，Button2显示为focused态指定的粉色，Button1失焦显示normal态指定的蓝色。

```typescript
@Entry
@Component
struct StateStylesSample {
  build() {
    Column() {
      Button('Button1')
        .stateStyles({
          focused: {
            .backgroundColor('#ffffeef0')
          },
          pressed: {
            .backgroundColor('#ff707070')
          },
          normal: {
            .backgroundColor('#ff2787d9')
          }
        })
        .margin(20)
      Button('Button2')
        .stateStyles({
          focused: {
            .backgroundColor('#ffffeef0')
          },
          pressed: {
            .backgroundColor('#ff707070')
          },
          normal: {
            .backgroundColor('#ff2787d9')
          }
        })
    }.margin('30%')
  }
}
```

**图1** 获焦态和按压态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/Fw6SG35IRwmibyFQ_MO3uw/zh-cn_image_0000002712403376.gif)

### @Styles和stateStyles联合使用

以下示例通过@Styles指定stateStyles的不同状态。

```typescript
@Entry
@Component
struct MyComponent {
  @Styles normalStyle() {
    .backgroundColor(Color.Gray)
  }

  @Styles pressedStyle() {
    .backgroundColor(Color.Red)
  }
  build() {
    Column() {
      Text('Text1')
        .fontSize(50)
        .fontColor(Color.White)
        .stateStyles({
          normal: this.normalStyle,
          pressed: this.pressedStyle,
        })
    }
  }
}
```

**图2** 正常态和按压态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/KOYKU5jLR7Cj6br5KQUOpw/zh-cn_image_0000002742122327.gif)

### 在stateStyles里使用常规变量和状态变量

stateStyles可以通过this绑定组件内的常规变量和状态变量。

```typescript
@Entry
@Component
struct CompWithInlineStateStyles {
  @State focusedColor: Color = 0xD5D5D5;
  normalColor: Color = 0x004AAF;

  build() {
    Column() {
      Button('clickMe')
        .height(100)
        .width(100)
        .stateStyles({
          normal: {
            .backgroundColor(this.normalColor)
          },
          focused: {
            .backgroundColor(this.focusedColor)
          }
        })
        .onClick(() => {
          this.focusedColor = 0x707070;
        })
        .margin('30%')
    }
  }
}
```

Button默认normal态显示蓝色，第一次按下Tab键让Button获焦显示为focus态的浅灰色，点击事件触发后，再次按下Tab键让Button获焦，focus态变为深灰色。

**图3** 点击改变获焦态样式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/NHjO7fesSzSHGtObnZBUZg/zh-cn_image_0000002712243414.gif)
