---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datapanel
title: DataPanel
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 信息展示 > DataPanel
category: harmonyos-references
scraped_at: 2026-09-02T15:01:04+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:ef336ef47ad9da8994b6bdf94390b0261ec277067da00ead8de81acfe0241acf
---

数据面板组件，用于将多个数据占比情况使用占比图进行展示，支持环形和线性两种展示类型，可自定义颜色、阴影、底板等视觉效果，适用于存储容量、任务进度、资源占比等数据可视化场景，帮助用户直观了解数据分布情况。

**说明** 

* 该组件从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 该组件从API版本26.0.0开始支持[WithTheme](ts-container-with-theme.md)。

## 子组件

无

## 接口

DataPanel(options: DataPanelOptions)

创建数据面板组件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DataPanelOptions](ts-basic-components-datapanel.md#datapaneloptions对象说明) | 是 | 数据面板配置选项，用于设置数据面板的数据值列表、最大值和数据面板类型。 |

## DataPanelOptions对象说明

数据面板选项。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| values | number[] | 否 | 否 | 数据值列表，数组长度范围[0, 9]，大于9个数据则取前9个数据。若数据值小于0则置为0。 |
| max | number | 否 | 是 | - max大于0时，表示数据的最大值。  - max小于等于0时，max等于values数据值列表各项的和，按比例显示。  默认值：100。 |
| type8+ | [DataPanelType](ts-basic-components-datapanel.md#datapaneltype8枚举说明) | 否 | 是 | 数据面板的类型（不支持动态修改）。  可选值：DataPanelType.Line（线性数据面板，适合在有限空间内展示多段数据对比）、DataPanelType.Circle（环形数据面板，适合直观展示数据占比关系）。  不传入时默认值为DataPanelType.Circle。 |

## DataPanelType8+枚举说明

数据面板的类型。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Line | 0 | 线性数据面板。 |
| Circle | 4 | 环形数据面板。 |

## 属性

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### closeEffect

closeEffect(value: boolean)

设置是否关闭数据占比图表旋转动效和投影效果。若未设置[trackShadow](ts-basic-components-datapanel.md#trackshadow10)属性，则由该属性控制投影效果，当closeEffect为false（投影开启）时，投影为默认效果。若已设置trackShadow属性，则由trackShadow属性值控制投影效果。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 关闭数据占比图表旋转动效和投影效果。  默认值：false，表示开启动效和投影；true表示关闭动效和投影。 |

### valueColors10+

valueColors(value: Array<ResourceColor | LinearGradient>)

设置各数据段颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[ResourceColor](ts-types.md#resourcecolor) | [LinearGradient](ts-basic-components-datapanel.md#lineargradient10)> | 是 | 各数据段颜色，ResourceColor为纯色，LinearGradient为渐变色。默认值为渐变色，九段数据的默认颜色为：[{ color: '#F7CE00', offset: 0 }, { color: '#F99B11', offset: 1 }]、[{ color: '#F76223', offset: 0 }, { color: '#F2400A', offset: 1 }]、[{ color: '#F772AC', offset: 0 }, { color: '#E65392', offset: 1 }]、[{ color: '#A575EB', offset: 0 }, { color: '#A12DF7', offset: 1 }]、[{ color: '#7B79F7', offset: 0 }, { color: '#4B48F7', offset: 1 }]、[{ color: '#4B8AF3', offset: 0 }, { color: '#007DFF', offset: 1 }]、[{ color: '#73C1E6', offset: 0 }, { color: '#4FB4E3', offset: 1 }]、[{ color: '#A5D61D', offset: 0 }, { color: '#69D14F', offset: 1 }]、[{ color: '#A2A2B0', offset: 0 }, { color: '#8E8E93', offset: 1 }]。  **说明：**  若设置的颜色个数少于数据段个数，剩余数据段会自动匹配默认颜色列表里对应顺序的颜色；若设置的颜色个数多于数据段个数，则显示的颜色个数与数据段个数一致，多余颜色将被忽略。 |

### trackBackgroundColor10+

trackBackgroundColor(value: ResourceColor)

设置底板颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 底板颜色。  默认值：'#08182431'，格式为十六进制ARGB值，前两位代表透明度。 |

### strokeWidth10+

strokeWidth(value: Length)

设置圆环粗细。数据面板的类型为DataPanelType.Line时该属性不生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 圆环粗细。  默认值：24  单位：vp  设置字符串类型参数时，如果不指定单位，默认单位为px，例如'10'，等同于'10px'。  **说明：**  数据面板的类型为DataPanelType.Line时该属性不生效。  设置小于0的值时，按默认值显示。  当value大于圆环半径时，圆环粗细会自动设置为圆环半径的12%。如果value过大，圆环可能会消失。 |

### trackShadow10+

trackShadow(value: DataPanelShadowOptions)

设置投影样式。若设置了本属性，则投影效果由本属性控制，closeEffect对投影效果的控制不再生效（closeEffect对旋转动效的控制不受影响）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DataPanelShadowOptions](ts-basic-components-datapanel.md#datapanelshadowoptions10对象说明) | 是 | 投影样式。  **说明：**  设置为null时，不开启投影。 |

### contentModifier12+

contentModifier(modifier: ContentModifier<DataPanelConfiguration>)

定制DataPanel内容区的方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](ts-universal-attributes-content-modifier.md#contentmodifiert)<[DataPanelConfiguration](ts-basic-components-datapanel.md#datapanelconfiguration12对象说明)> | 是 | 在DataPanel组件上，定制内容区的方法，设置后将使用开发者自定义的内容替换DataPanel原有显示内容。  modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。 |

## DataPanelShadowOptions10+对象说明

DataPanelShadowOptions继承自[MultiShadowOptions](ts-information-display-common.md#multishadowoptions)，具有MultiShadowOptions的全部属性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colors | Array<[ResourceColor](ts-types.md#resourcecolor) | [LinearGradient](ts-basic-components-datapanel.md#lineargradient10)> | 否 | 是 | 各数据段投影的颜色。  默认值：与valueColors值相同  **说明：**  若设置的投影颜色的个数少于数据段个数时，则显示的投影颜色个数等于设置的投影颜色个数。  若设置的投影颜色的个数多于数据段个数时，则显示的投影颜色个数等于数据段个数。 |

## LinearGradient10+

### constructor

constructor(colorStops: ColorStop[])

线性渐变颜色描述。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorStops | [ColorStop](ts-basic-components-datapanel.md#colorstop10)[] | 是 | 存储渐变颜色和渐变点。 |

## ColorStop10+

颜色断点类型，用于描述渐变色颜色断点。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 渐变色断点处的颜色值。 |
| offset | [Length](ts-types.md#length) | 否 | 否 | 渐变色断点（0~1之间的比例值，若该值小于0则置为0，若该值大于1则置为1）。  **说明：**  若传入字符串类型且内容为数字，则转换为对应的数值。  例如'10vp'转换为10，'10%'转换为0.1。 |

## DataPanelConfiguration12+对象说明

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](ts-universal-attributes-content-modifier.md#commonconfigurationt)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| values | number[] | 否 | 否 | 当前DataPanel的数据值。  数组长度范围是[0, 9]。  **说明：**  如果数组长度大于9，则取前9项。 |
| maxValue | number | 否 | 否 | DataPanel显示的最大值。  默认值：100。  **说明：**  如果小于或等于0，maxValue将被设为values数组中所有项的总和，并按比例显示。 |

## 示例

### 示例1（设置数据面板类型）

该示例通过[DataPanelOptions](ts-basic-components-datapanel.md#datapaneloptions对象说明)的type属性，实现了设置数据面板的类型的功能。

```ts
// xxx.ets
@Entry
@Component
struct DataPanelExample {
  public valueArr: number[] = [10, 10, 10, 10, 10, 10, 10, 10, 10];

  build() {
    Column({ space: 5 }) {
      Row() {
        Stack() {
          // 单段环形数据面板
          DataPanel({ values: [30], max: 100, type: DataPanelType.Circle }).width(168).height(168)
          Column() {
            Text('30').fontSize(35).fontColor('#182431')
            Text('1.0.0').fontSize(9.33).lineHeight(12.83).fontWeight(500).opacity(0.6)
          }

          Text('%')
            .fontSize(9.33)
            .lineHeight(12.83)
            .fontWeight(500)
            .opacity(0.6)
            .position({ x: 104.42, y: 78.17 })
        }.margin({ right: 44 })

        // 多段环形数据面板
        Stack() {
          DataPanel({ values: [50, 12, 8, 5], max: 100, type: DataPanelType.Circle }).width(168).height(168)
          Column() {
            Text('75').fontSize(35).fontColor('#182431')
            Text('已使用98GB/128GB').fontSize(8.17).lineHeight(11.08).fontWeight(500).opacity(0.6)
          }

          Text('%')
            .fontSize(9.33)
            .lineHeight(12.83)
            .fontWeight(500)
            .opacity(0.6)
            .position({ x: 104.42, y: 78.17 })
        }
      }.margin({ bottom: 59 })

      // 线形数据面板
      DataPanel({ values: this.valueArr, max: 100, type: DataPanelType.Line }).width(300).height(20)
    }.width('100%').margin({ top: 5 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/kvSOpWqJQGWef9zjur4Ysw/zh-cn_image_0000002736315189.png)

### 示例2（设置渐变色和阴影）

该示例通过[valueColors](ts-basic-components-datapanel.md#valuecolors10)和[trackShadow](ts-basic-components-datapanel.md#trackshadow10)接口设置[LinearGradient](ts-basic-components-datapanel.md#lineargradient10)颜色，实现了设置渐变色效果和阴影效果。

```ts
// xxx.ets
@Entry
@Component
struct LinearGradientDataPanelExample {
  public values1: number[] = [20, 20, 20, 20];
  public color1: LinearGradient =
      new LinearGradient([{ color: '#65EEC9A3', offset: 0 }, { color: '#FFEF629F', offset: 1 }]);
  public color2: LinearGradient =
      new LinearGradient([{ color: '#FF67F9D4', offset: 0 }, { color: '#FFFF9554', offset: 1 }]);
  public colorShadow1: LinearGradient =
      new LinearGradient([{ color: '#65EEC9A3', offset: 0 }, { color: '#65EF629F', offset: 1 }]);
  public colorShadow2: LinearGradient =
      new LinearGradient([{ color: '#65e26709', offset: 0 }, { color: '#65efbd08', offset: 1 }]);
  public colorShadow3: LinearGradient =
      new LinearGradient([{ color: '#6572B513', offset: 0 }, { color: '#6508efa6', offset: 1 }]);
  public colorShadow4: LinearGradient =
      new LinearGradient([{ color: '#65ed08f5', offset: 0 }, { color: '#65ef0849', offset: 1 }]);
  @State shadowColorArray: Array<LinearGradient | ResourceColor> =
      [this.colorShadow1, this.colorShadow2, this.colorShadow3, this.colorShadow4];
  @State color3: string = '#00FF00';
  @State color4: string = '#20FF0000';
  @State colorArray: Array<LinearGradient | ResourceColor> = [this.color1, this.color2, this.color3, this.color4];
  @State bgColor: string = '#08182431';
  @State offsetX: number = 15;
  @State offsetY: number = 15;
  @State radius: number = 5;

  build() {
    Column({ space: 5 }) {
      Text('LinearGradient')
        .fontSize(9)
        .fontColor(0xCCCCCC)
        .textAlign(TextAlign.Start)
        .width('100%')
        .margin({ top: 20, left: 20 })
      DataPanel({ values: this.values1, max: 100, type: DataPanelType.Circle })
        .width(300)
        .height(300)
        .valueColors(this.colorArray)
        .trackShadow({
          radius: this.radius,
          colors: this.shadowColorArray,
          offsetX: this.offsetX,
          offsetY: this.offsetY
        })
        .strokeWidth(30)
        .trackBackgroundColor(this.bgColor)
    }.width('100%').margin({ top: 5 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/n6DJOZs0SxWbGfmxRHCANA/zh-cn_image_0000002706676146.png)

### 示例3（设置关闭动画和阴影）

该示例通过[closeEffect](ts-basic-components-datapanel.md#closeeffect)接口，实现了关闭数据占比图表旋转动效和投影效果的功能。

```ts
// xxx.ets
@Entry
@Component
struct LinearGradientDataPanelExample {
  public values1: number[] = [20, 20, 20, 20];
  public color1: LinearGradient =
    new LinearGradient([{ color: '#65EEC9A3', offset: 0 }, { color: '#FFEF629F', offset: 1 }]);
  public color2: LinearGradient =
    new LinearGradient([{ color: '#FF67F9D4', offset: 0 }, { color: '#FFFF9554', offset: 1 }]);
  @State color3: string = '#00FF00';
  @State color4: string = '#20FF0000';
  @State colorArray: Array<LinearGradient | ResourceColor> = [this.color1, this.color2, this.color3, this.color4];
  @State bgColor: string = '#08182431';

  build() {
    Column({ space: 5 }) {
      Text('LinearGradient')
        .fontSize(9)
        .fontColor(0xCCCCCC)
        .textAlign(TextAlign.Start)
        .width('100%')
        .margin({ top: 20, left: 20 })
      DataPanel({ values: this.values1, max: 100, type: DataPanelType.Circle })
        .width(300)
        .height(300)
        .valueColors(this.colorArray)
        .strokeWidth(30)
        .closeEffect(true)
        .trackBackgroundColor(this.bgColor)
    }.width('100%').margin({ top: 5 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/jzfiFyEITfGb2M5nbJMn4g/zh-cn_image_0000002736435233.png)

### 示例4（设置定制内容区）

该示例通过[contentModifier](ts-basic-components-datapanel.md#contentmodifier12)接口，实现了定制数据面板内容区的功能。

```ts
// xxx.ets
@Builder
function buildDataPanel(config: DataPanelConfiguration) {
  Column() {
    Column() {
      ForEach(config.values, (item: number, index: number) => {
        ChildItem({ item: item, index: index, max: config.maxValue })
      }, (item: number, index: number) => item.toString())
    }.padding(10)

    Column() {
      Line().width('100%').backgroundColor('#ff373737').margin({ bottom: 5 })
    }.padding({ left: 20, right: 20 })

    Row() {
      Text('Length=' + config.values.length + '    ').margin({ left: 10 }).align(Alignment.Start)
      Text('Max=' + config.maxValue).margin({ left: 10 }).align(Alignment.Start)
    }
  }
}

class DataPanelBuilder implements ContentModifier<DataPanelConfiguration> {
  constructor() {
  }

  applyContent(): WrappedBuilder<[DataPanelConfiguration]> {
    return wrapBuilder(buildDataPanel)
  }
}

@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Data panel').margin({ top: 12 });
      Row() {
        DataPanel({ values: [12.3, 21.1, 13.4, 35.2, 26.0, 32.0], max: 140, type: DataPanelType.Circle })
          .width(400)
          .height(260)
          .constraintSize({ maxWidth: '100%' })
          .padding({ top: 10 })
          .contentModifier(new DataPanelBuilder())
      }.margin(15).backgroundColor('#fff5f5f5')
    }
  }
}

@Component
struct ChildItem {
  @Prop item: number;
  @Prop index: number;
  @Prop max: number;
  public color1: string = '#65ff00dd'
  public color2: string = '#6500ff99'
  public color3: string = '#65ffe600'
  public color4: string = '#6595ff00'
  public color5: string = '#65000dff'
  public color6: string = '#650099ff'
  public colorArray: Array<string> = [this.color1, this.color2, this.color3, this.color4, this.color5, this.color6];

  build() {
    RelativeContainer() {
      Row() {
        Rect()
          .height(25)
          .width(this.item * 600 / this.max)
          .foregroundColor((this.index < 0 || this.index >= this.colorArray.length) ? this.colorArray[0] :
            this.colorArray[this.index])
          .radius(5)
          .align(Alignment.Start)
        Text(' ' + this.item)
          .fontSize(17)
      }
    }.height(28)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/RYgQmyhuSOa0OKP3Et4l0A/zh-cn_image_0000002706836086.jpg)
