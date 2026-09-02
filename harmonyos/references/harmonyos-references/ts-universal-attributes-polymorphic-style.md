---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-polymorphic-style
title: 多态样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 多态样式
category: harmonyos-references
scraped_at: 2026-09-02T15:00:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0b3bab1844b72d2ff7a059285bdcce398d3ef59f085da99bf6f78f57d482efa9
---

设置组件在不同状态下的样式，适用于需要根据各种交互状态动态切换组件样式的场景，帮助开发者统一管理组件状态样式。

**说明** 

* 从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 从API version 11开始支持另一种写法[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)，可根据开发者需要动态设置属性。
* 多态样式仅支持[通用属性](ts-component-general-attributes.md)。如果多态样式不生效，则该属性可能为组件的私有属性，例如：fontColor、[TextInput](ts-basic-components-textinput.md)组件的[backgroundColor](ts-universal-attributes-background.md#backgroundcolor18)等。此时，可以通过attributeModifier动态设置组件属性来解决此问题。
* 当前多态样式实现依赖于组件自定义节点的刷新机制。因Builder不具备独立的自定义父节点，无法直接触发刷新，致使多态样式无法直接在Builder中生效。解决方法是将多态样式封装至自定义组件内部，再将此组件置于@Builder中，以此来间接实现多态样式。示例代码可参考[示例3（设置Builder多态样式）](ts-universal-attributes-polymorphic-style.md#示例3设置builder多态样式)。
* 多态样式的焦点态只有在[焦点激活态](../harmonyos-guides/arkts-common-events-focus-event.md#基础概念)开启时生效。
* 如果组件同时处于多种状态，并且分别在各自的状态里设置了相同属性，那么最终生效样式由开发者设置顺序决定，后设置的样式生效。

## stateStyles

stateStyles(value: StateStyles): T

设置组件不同状态的样式。

**说明** 

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [StateStyles](ts-universal-attributes-polymorphic-style.md#statestyles-1) | 是 | 设置组件不同状态的样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## StateStyles

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| normal | any | 否 | 是 | 组件无状态时的样式。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| pressed | any | 否 | 是 | 组件按下状态的样式。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| disabled | any | 否 | 是 | 组件禁用状态的样式。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| focused | any | 否 | 是 | 组件获焦状态的样式。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| clicked | any | 否 | 是 | 组件点击状态的样式。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| selected10+ | object | 否 | 是 | 组件选中状态的样式。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| hovered | object | 否 | 是 | 组件悬浮状态的样式。  **起始版本：** 26.0.0  **卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |

**selected选中状态说明**

* 当前多态样式的选中状态样式依赖组件选中属性值，可以使用[点击事件](ts-universal-events-click.md)修改属性值，或使用属性自带[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定功能。
* 当前支持selected的组件及其参数/属性值：

  | 组件 | 支持的参数/属性 | 起始API版本 |
  | --- | --- | --- |
  | [Checkbox](ts-basic-components-checkbox.md) | select | 10 |
  | [CheckboxGroup](ts-basic-components-checkboxgroup.md) | selectAll | 10 |
  | [Radio](ts-basic-components-radio.md) | checked | 10 |
  | [Toggle](ts-basic-components-toggle.md) | isOn | 10 |
  | [ListItem](ts-container-listitem.md) | selected | 10 |
  | [GridItem](ts-container-griditem.md) | selected | 10 |
  | [MenuItem](ts-basic-components-menuitem.md) | selected | 10 |

**pressed和clicked状态说明**

* 当clicked和pressed同时在一个组件上使用时，只有后注册的状态才能生效。

## 示例

### 示例1（设置Text多态样式）

该示例展示了[stateStyles](ts-universal-attributes-polymorphic-style.md#statestyles)设置状态为hovered、pressed和disabled时Text组件的样式变化。

从API版本26.0.0开始，[stateStyles](ts-universal-attributes-polymorphic-style.md#statestyles)新增hovered属性。

```ts
// xxx.ets
@Entry
@Component
struct StyleExample {
  @State isEnable: boolean = true

  @Styles
  hoveredStyles(): void {
    .backgroundColor('#12db70')
    .borderRadius(10)
    .borderStyle(BorderStyle.Dashed)
    .borderWidth(2)
    .borderColor('#33000000')
    .width(120)
    .height(30)
    .opacity(1)
  }

  @Styles
  pressedStyles(): void {
    .backgroundColor('#ED6F21')
    .borderRadius(10)
    .borderStyle(BorderStyle.Dashed)
    .borderWidth(2)
    .borderColor('#33000000')
    .width(120)
    .height(30)
    .opacity(1)
  }

  @Styles
  disabledStyles(): void {
    .backgroundColor('#E5E5E5')
    .borderRadius(10)
    .borderStyle(BorderStyle.Solid)
    .borderWidth(2)
    .borderColor('#2a4c1919')
    .width(90)
    .height(25)
    .opacity(1)
  }

  @Styles
  normalStyles(): void {
    .backgroundColor('#0A59F7')
    .borderRadius(10)
    .borderStyle(BorderStyle.Solid)
    .borderWidth(2)
    .borderColor('#33000000')
    .width(100)
    .height(25)
    .opacity(1)
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
      Text('normal')
        .fontSize(14)
        .fontColor(Color.White)
        .opacity(0.5)
        // stateStyles设置组件无状态时的样式
        .stateStyles({
          normal: this.normalStyles,
        })
        .margin({ bottom: 20 })
        .textAlign(TextAlign.Center)
      Text('hovered')
        .backgroundColor('#0A59F7')
        .borderRadius(20)
        .borderStyle(BorderStyle.Dotted)
        .borderWidth(2)
        .borderColor(Color.Red)
        .width(100)
        .height(25)
        .opacity(1)
        .fontSize(14)
        .fontColor(Color.White)
        // stateStyles设置组件鼠标悬浮状态时的样式
        .stateStyles({
          hovered: this.hoveredStyles,
        })
        .margin({ bottom: 20 })
        .textAlign(TextAlign.Center)
      Text('pressed')
        .backgroundColor('#0A59F7')
        .borderRadius(20)
        .borderStyle(BorderStyle.Dotted)
        .borderWidth(2)
        .borderColor(Color.Red)
        .width(100)
        .height(25)
        .opacity(1)
        .fontSize(14)
        .fontColor(Color.White)
        // stateStyles设置组件按下状态时的样式
        .stateStyles({
          pressed: this.pressedStyles,
        })
        .margin({ bottom: 20 })
        .textAlign(TextAlign.Center)
      Text(this.isEnable ? 'effective' : 'disabled')
        .backgroundColor('#0A59F7')
        .borderRadius(20)
        .borderStyle(BorderStyle.Solid)
        .borderWidth(2)
        .borderColor(Color.Gray)
        .width(100)
        .height(25)
        .opacity(1)
        .fontSize(14)
        .fontColor(Color.White)
        .enabled(this.isEnable)
        // stateStyles设置组件禁用状态时的样式
        .stateStyles({
          disabled: this.disabledStyles,
        })
        .textAlign(TextAlign.Center)
      Text('control disabled')
        .onClick(() => {
          this.isEnable = !this.isEnable;
          console.info(`${this.isEnable}`);
        })
    }
    .width(350).height(300)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/9gKM52z0QsKl3z-5oTxY5w/zh-cn_image_0000002736314787.gif)

### 示例2（设置Radio多态样式）

该示例展示了状态为selected时Radio组件的样式变化。

```ts
// xxx.ets
@Entry
@Component
struct Index {
  @State isRadio1Selected: boolean = false
  @State isRadio2Selected: boolean = false

  @Styles
  normalStyles(): void {
    .backgroundColor('#E5E5E1')
  }

  @Styles
  selectStyles(): void {
    .backgroundColor('#ED6F21')
    .borderWidth(2)
  }

  build() {
    Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Column() {
        Text('Radio1')
          .fontSize(25)
        Radio({ value: 'Radio1', group: 'radioGroup1' })
          .checked(this.isRadio1Selected)
          .height(50)
          .width(50)
          .borderWidth(0)
          .borderRadius(30)
          .onClick(() => {
            this.isRadio1Selected = !this.isRadio1Selected;
          })
          .stateStyles({
            normal: this.normalStyles,
            selected: this.selectStyles,
          })
      }
      .margin(30)

      Column() {
        Text('Radio2')
          .fontSize(25)
        Radio({ value: 'Radio2', group: 'radioGroup2' })
          .checked($$this.isRadio2Selected)
          .height(50)
          .width(50)
          .borderWidth(0)
          .borderRadius(30)
          .stateStyles({
            normal: this.normalStyles,
            selected: this.selectStyles,
          })
      }
      .margin(30)
    }.padding({ top: 30 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/HK1I45XOR-SoaHEBmdynLA/zh-cn_image_0000002706675746.gif)

### 示例3（设置Builder多态样式）

该示例展示了状态为pressed时@Builder中自定义组件的样式变化。

```ts
import { ComponentContent } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Component
struct Child {
  build() {
    Row()
      .zIndex(10)
      .width(200)
      .height(200)
      .stateStyles({
        normal: {
          .backgroundColor(Color.Blue)
        },
        pressed: {
          .backgroundColor(Color.Black)
        }
      })
  }
}

@Builder
function buildText() {
  Child()
}

@Entry
@Component
struct Index {
  private contentNode: ComponentContent<Object> =
    new ComponentContent(this.getUIContext(), wrapBuilder(buildText));

  build() {
    Column() {
      Button().margin({ top: 200 }).onClick(() => {
        this.getUIContext()
          .getPromptAction()
          .openCustomDialog(this.contentNode)
          .then(() => {
            console.info('OpenCustomDialog complete.');
          })
          .catch((error: BusinessError) => {
            let message = error.message;
            let code = error.code;
            console.error(`OpenCustomDialog args error code is ${code}, message is ${message}`);
          });
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/P9Nm7Yq9TguAe0cgWl1PBg/zh-cn_image_0000002736434831.gif)
