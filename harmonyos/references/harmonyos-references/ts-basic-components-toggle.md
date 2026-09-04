---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle
title: Toggle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > Toggle
category: harmonyos-references
scraped_at: 2026-09-05T06:17:13+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:a0c7508a6018ab2b7d98695901b0dbe77d1e70a7e3bb6f606fca5a18ce37f541
---

组件提供勾选框样式、状态按钮样式和开关样式，适用于需要快速切换状态或进行单选确认的场景，能够有效提升交互体验与界面的直观性。

**说明** 

* 该组件从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 从API版本26.0.0开始，Toggle组件支持系统材质效果。Toggle组件使用通用系统材质属性[systemMaterial](ts-universal-attributes-image-effect.md#systemmaterial)时，不同[ToggleType](ts-basic-components-toggle.md#toggletype枚举说明)类型的效果不同：

  + ToggleType.Checkbox：当前未适配系统材质效果，设置系统材质不会出现系统材质相关的动效和视觉效果。
  + ToggleType.Switch：传入材质参数时，使用组件内部预设的视觉参数，传入的材质参数仅作为开启系统材质的开关标记，不影响实际视觉效果。主要影响Toggle的滑块大小、滑块样式、阴影等视觉属性。开启系统材质后，滑块会出现默认白色的点光源效果；设置[switchPointColor](ts-basic-components-toggle.md#switchpointcolor)后，点光源颜色跟随switchPointColor的设置。传入undefined时，系统材质不生效，表现为原先的Toggle样式。
  + ToggleType.Button：设置系统材质的效果与[Button](ts-basic-components-button.md)组件设置系统材质的效果相同，主要影响背景颜色、边框、阴影等视觉属性。

## 子组件

仅当ToggleType设置为Button时，可包含子组件。

## 接口

Toggle(options: ToggleOptions)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToggleOptions](ts-basic-components-toggle.md#toggleoptions18对象说明) | 是 | Toggle组件的配置选项，用于配置开关的样式类型和初始状态。 |

## ToggleOptions18+对象说明

Toggle组件的配置信息。

**说明** 

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type8+ | [ToggleType](ts-basic-components-toggle.md#toggletype枚举说明) | 否 | 否 | 开关的样式。  默认值：ToggleType.Switch  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isOn8+ | boolean | 否 | 是 | 开关是否打开。  true：打开；false：关闭。  默认值：false  该属性支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  该属性支持[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## ToggleType枚举说明

Toggle的样式。

**说明** 

Toggle的样式继承对应组件样式的默认值，且不支持设置。例如，如果ToggleType为Button，则该组件样式继承[ButtonType](ts-basic-components-button.md#buttontype枚举说明)的默认值。由于Button.type从API version 18开始，默认类型从胶囊型变更为圆角矩形，胶囊型按钮不支持设置[borderRadius](ts-universal-attributes-border.md#borderradius)，此时使用Toggle组件设置borderRadius也不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Checkbox | 0 | 提供勾选框样式。  **说明：**  API version 11开始，Checkbox默认样式由圆角方形变为圆形。  [通用属性margin](ts-universal-attributes-size.md#margin)的默认值为：  {  top: '14px',  right: '14px',  bottom: '14px',  left: '14px'  }。  默认尺寸为：  {width:'20vp', height:'20vp'}。 |
| Switch | 1 | 提供开关样式。  **说明：**  [通用属性margin](ts-universal-attributes-size.md#margin)的默认值为：  {  top: '6px',  right: '14px',  bottom: '6px',  left: '14px'  }。  默认尺寸为：  {width:'36vp', height:'20vp'}。 |
| Button | 2 | 提供状态按钮样式。如子组件设置文本，文本内容将显示在按钮内。默认高度为28vp，宽度无默认值。 |

## 属性

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### selectedColor

selectedColor(value: ResourceColor)

设置组件在打开状态下的背景颜色。

**说明** 

设置systemMaterial系统材质时对背景色的影响，请参考组件开篇说明。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 组件打开状态的背景颜色。  默认值：  当ToggleType为Switch时，默认值为$r('sys.color.ohos\_id\_color\_emphasize')。  当ToggleType为Checkbox时，默认值为$r('sys.color.ohos\_id\_color\_emphasize')。  当ToggleType为Button时，默认值为$r('sys.color.ohos\_id\_color\_emphasize')混合$r('sys.float.ohos\_id\_alpha\_highlight\_bg')的透明度。 |

### switchPointColor

switchPointColor(color: ResourceColor)

设置Switch类型的圆形滑块颜色。仅当type为ToggleType.Switch生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 是 | Switch类型的圆形滑块颜色。  默认值：$r('sys.color.ohos\_id\_color\_foreground\_contrary')  **说明：**  同时设置了[systemMaterial](ts-universal-attributes-image-effect.md#systemmaterial)系统材质时，滑块会出现默认白色的点光源效果，设置此属性后点光源颜色跟随此属性的设置。 |

### switchStyle12+

switchStyle(value: SwitchStyle)

设置Switch类型的样式。仅当type为ToggleType.Switch生效。

**说明** 

与systemMaterial系统材质同时设置时，请参考组件开篇说明及通用系统材质属性文档。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SwitchStyle](ts-basic-components-toggle.md#switchstyle12对象说明) | 是 | Switch样式风格。 |

### contentModifier12+

contentModifier(modifier: ContentModifier<ToggleConfiguration>)

定制Toggle内容区的方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](ts-universal-attributes-content-modifier.md#contentmodifiert)<[ToggleConfiguration](ts-basic-components-toggle.md#toggleconfiguration12对象说明)> | 是 | 在Toggle组件上，定制内容区的方法。  modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。 |

## SwitchStyle12+对象说明

Switch类型的样式。

**说明** 

与systemMaterial系统材质同时设置时，请参考组件开篇说明及通用系统材质属性文档。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pointRadius | number | [Resource](ts-types.md#resource) | 否 | 是 | 设置Switch类型的圆形滑块半径，单位为vp。  **说明：**  不支持百分比，设定值小于0时按照默认算法设置，设定值大于等于0时按照设定值设置。  未设定此属性时，圆形滑块半径根据默认算法设置。  默认算法：（组件高度（单位：vp） / 2） - （2vp \* 组件高度（单位：vp） / 20vp）。 |
| unselectedColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置Switch类型关闭状态的背景颜色。  默认值：深色和浅色模式下均为0x337F7F7F。从API version 20开始，如果开启了[优化深浅色模式切换开销](../harmonyos-guides/ui-dark-light-color-adaptation.md#优化深浅色模式切换开销)能力，浅色模式下默认值为0x19000000，表现效果为10%透明度的黑色；深色模式下默认值为0x19FFFFFF，表现效果为10%透明度的白色。 |
| pointColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置Switch类型的圆形滑块颜色。  默认值：$r('sys.color.ohos\_id\_color\_foreground\_contrary') |
| trackBorderRadius | number | [Resource](ts-types.md#resource) | 否 | 是 | 设置Switch类型的滑轨的圆角，单位为vp。  **说明：**  不支持百分比，设定值小于0时按照默认算法设置，设定值大于组件高度一半时按照组件高度一半设置，其他场合按照设定值设置。  未设定此属性时，滑轨圆角根据默认算法设置。  默认算法：组件高度（单位：vp） / 2。 |

## 事件

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onChange

onChange(callback: (isOn: boolean) => void)

开关状态切换时触发该事件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isOn | boolean | 是 | 开关的状态。  true：状态从关切换为开；false：状态从开切换为关。 |

## ToggleConfiguration12+对象说明

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](ts-universal-attributes-content-modifier.md#commonconfigurationt)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isOn | boolean | 否 | 否 | 开关是否打开。  true：开关打开；false：开关关闭。  默认值：false |
| enabled | boolean | 否 | 否 | 是否可以切换状态。  true：可以切换状态；false：不可以切换状态。  默认值：true |
| triggerChange | Callback<boolean> | 否 | 否 | 用于触发Toggle开关状态变化的回调函数，通常在自定义ContentModifier中通过编程方式改变开关状态。调用此回调并传入true可将开关状态设置为打开，传入false可将开关状态设置为关闭。 |

## 示例

### 示例1（设置开关的样式）

该示例通过配置ToggleType设置Toggle的勾选框样式、状态按钮样式及开关样式。

```ts
// xxx.ets
@Entry
@Component
struct ToggleExample {
  build() {
    Column({ space: 10 }) {
      Text('type: Switch').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Switch, isOn: false })
          .selectedColor('#007DFF')
          .switchPointColor('#FFFFFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })

        Toggle({ type: ToggleType.Switch, isOn: true })
          .selectedColor('#007DFF')
          .switchPointColor('#FFFFFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })
      }

      Text('type: Checkbox').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Checkbox, isOn: false })
          .size({ width: 20, height: 20 })
          .selectedColor('#007DFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })

        Toggle({ type: ToggleType.Checkbox, isOn: true })
          .size({ width: 20, height: 20 })
          .selectedColor('#007DFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })
      }

      Text('type: Button').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Button, isOn: false }) {
          Text('status button').fontColor('#182431').fontSize(12)
        }.width(106)
        .selectedColor('rgba(0,125,255,0.20)')
        .onChange((isOn: boolean) => {
          console.info('Component status:' + isOn);
        })

        Toggle({ type: ToggleType.Button, isOn: true }) {
          Text('status button').fontColor('#182431').fontSize(12)
        }.width(106)
        .selectedColor('rgba(0,125,255,0.20)')
        .onChange((isOn: boolean) => {
          console.info('Component status:' + isOn);
        })
      }
    }.width('100%').padding(24)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/m3h3DRNSSuKpLuC43Ls7CA/zh-cn_image_0000002742005049.gif)

### 示例2（自定义开关类型的样式）

该示例实现了自定义设置Toggle组件Switch样式，包括圆形滑块半径、关闭状态的背景颜色、圆形滑块颜色、滑轨的圆角。

```ts
// xxx.ets
@Entry
@Component
struct ToggleExample {
  build() {
    Column({ space: 10 }) {
      Text('type: Switch').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Switch, isOn: false })
          .selectedColor('#007DFF')
          .switchStyle({
            pointRadius: 15,
            trackBorderRadius: 10,
            pointColor: '#D2B48C',
            unselectedColor: Color.Pink })
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })

        Toggle({ type: ToggleType.Switch, isOn: true })
          .selectedColor('#007DFF')
          .switchStyle({
            pointRadius: 15,
            trackBorderRadius: 10,
            pointColor: '#D2B48C',
            unselectedColor: Color.Pink })
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })
      }
    }.width('100%').padding(24)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/GnBP5rbkTBGXzNPtmWn79A/zh-cn_image_0000002712406060.gif)

### 示例3（自定义Toggle样式）

该示例实现自定义Toggle样式，通过按钮切换圆形背景颜色：点击蓝圆按钮，背景变蓝色；点击黄圆按钮，背景变黄色。

```ts
// xxx.ets
// 自定义Switch样式修改器，实现ContentModifier接口定制Toggle内容区
class MySwitchStyle implements ContentModifier<ToggleConfiguration> {
  // 开关打开时的背景颜色
  selectedColor: Color = Color.White;
  // 用于按钮显示的文本
  lamp: string = 'string';

  constructor(selectedColor: Color, lamp: string) {
    this.selectedColor = selectedColor;
    this.lamp = lamp;
  }

  applyContent(): WrappedBuilder<[ToggleConfiguration]> {
    return wrapBuilder(buildSwitch);
  }
}

@Builder
function buildSwitch(config: ToggleConfiguration) {
  Column({ space: 50 }) {
    Circle({ width: 150, height: 150 })
      .fill(config.isOn ? (config.contentModifier as MySwitchStyle).selectedColor : Color.Blue)
    Row() {
      Button('蓝' + JSON.stringify((config.contentModifier as MySwitchStyle).lamp))
        .onClick(() => {
          config.triggerChange(false);
        })
      Button('黄' + JSON.stringify((config.contentModifier as MySwitchStyle).lamp))
        .onClick(() => {
          config.triggerChange(true);
        })
    }
  }
}

@Entry
@Component
struct Index {
  build() {
    Column({ space: 50 }) {
      // 使用自定义样式修改器定制Toggle内容，并通过onChange监听状态变化
      Toggle({ type: ToggleType.Switch })
        .enabled(true)
        .contentModifier(new MySwitchStyle(Color.Yellow, '灯'))
        .onChange((isOn: boolean) => {
          console.info('Switch Log:' + isOn);
        })
    }.height('100%').width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/3akqRDjqTvyW-YnEXANurQ/zh-cn_image_0000002742125009.gif)

### 示例4（Toggle沉浸光感效果）

该示例展示了Toggle组件Switch类型在开启沉浸光感前后的效果对比，包括不设置系统材质、设置undefined、设置系统材质以及设置系统材质并配合[switchPointColor](ts-basic-components-toggle.md#switchpointcolor)设置点光源颜色的效果。示例使用通用属性[systemMaterial](ts-universal-attributes-image-effect.md#systemmaterial)接口来实现沉浸光感效果。

组件沉浸光感效果会根据设备算力与用户在系统中设置的沉浸光感效果自适应调整，开发者无需额外适配。

从API版本26.0.0开始，新增systemMaterial属性。

**说明** 

系统材质的实际显示效果与设备的算力档位相关，相同的代码在不同算力档位的设备上显示效果存在差异，低算力设备上会显示简化后的材质效果。算力档位由系统根据设备硬件能力自动划分和管理，应用无需感知，也无需进行额外设置，系统会根据当前设备的算力档位自动适配材质的显示效果。

```ts
import { uiMaterial } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct ToggleMaterialTest {
  build() {
    Column({ space: 10 }) {
      // 不设置系统材质接口，无沉浸光感效果
      Toggle({ type: ToggleType.Switch, isOn: true })

      // systemMaterial设置undefined，恢复为无沉浸光感的效果
      Toggle({ type: ToggleType.Switch, isOn: true })
        .systemMaterial(undefined)

      // 设置系统材质，开启沉浸光感效果（systemMaterial参数任意仅作为系统材质开关，最终使用组件侧固定参数），默认白色点光源（颜色为switchPointColor默认值）
      Toggle({ type: ToggleType.Switch, isOn: true })
        .systemMaterial(new uiMaterial.Material())

      // 设置系统材质，开启沉浸光感效果（systemMaterial参数任意仅作为系统材质开关，最终使用组件侧固定参数），点光源颜色跟随switchPointColor设置
      Toggle({ type: ToggleType.Switch, isOn: true })
        .systemMaterial(new uiMaterial.Material())
        .switchPointColor(Color.Red)
    }
    .width('100%')
  }
}
```

高算力设备场景示例图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/F38zqp6dTWOoYkHEJtBdTg/zh-cn_image_0000002712246102.gif)

低算力设备场景示例图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/lFIbB7WhRISGPpxOyR1pHg/zh-cn_image_0000002742005051.gif)
