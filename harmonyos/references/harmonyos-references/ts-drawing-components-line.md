---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-line
title: Line
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 图形绘制 > Line
category: harmonyos-references
scraped_at: 2026-09-02T15:01:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b93cf69db66f0d383ef762ea86f910429986e5217e2f9c246653be43014fba84
---

Line组件用于在应用界面中绘制直线，支持自定义直线的起点、终点、颜色、宽度、透明度、虚线样式、端点样式等属性。适用于绘制分隔线、装饰性线条、图表中的坐标轴或连接线、自定义图形边框等场景。

**说明** 

该组件从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

该组件从API version 20开始支持使用[AttributeUpdater](js-apis-arkui-attributeupdater.md)类的[updateConstructorParams](js-apis-arkui-attributeupdater.md#属性)接口更新构造参数。

* Line组件无法形成闭合区域，fill和fillOpacity属性设置无效。
* Line组件不支持拐角，strokeLineJoin和strokeMiterLimit属性设置无效。

## 子组件

无

## 接口

### Line

new Line(options?: LineOptions)

用于绘制直线的构造函数。Line组件在width和height定义的矩形区域内绘制直线，绘制区域的左上角为坐标原点(0,0)，x轴向右延伸，y轴向下延伸。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [LineOptions](ts-drawing-components-line.md#lineoptions18对象说明) | 否 | Line组件绘制区域，包含width和height属性，用于设置Line组件的宽高。不传递此参数时，Line组件的width和height属性将按照各自属性的缺省逻辑处理（参见LineOptions对象说明）。  异常值undefined和null按照无效值处理，本次设置不生效。 |

### Line

Line(options?: LineOptions)

用于绘制直线的构造函数。Line组件在width和height定义的矩形区域内绘制直线，绘制区域的左上角为坐标原点(0,0)，x轴向右延伸，y轴向下延伸。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [LineOptions](ts-drawing-components-line.md#lineoptions18对象说明) | 否 | Line组件绘制区域，包含width和height属性，用于设置Line组件的宽高。不传递此参数时，Line组件的width和height属性将按照各自属性的缺省逻辑处理（参见LineOptions对象说明）。  异常值undefined和null按照无效值处理，本次设置不生效。 |

## LineOptions18+对象说明

用于描述Line组件绘制属性。

**说明** 

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width7+ | [Length](ts-types.md#length) | 否 | 是 | 宽度。  值为异常值或缺省时，根据startPoint和endPoint自动计算所需的绘制区域宽度。  默认单位：vp  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| height7+ | [Length](ts-types.md#length) | 否 | 是 | 高度。  值为异常值或缺省时，根据startPoint和endPoint自动计算所需的绘制区域高度。  默认单位：vp  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## 属性

除支持[通用属性](ts-component-general-attributes.md)以及[图形绘制通用属性](ts-drawing-components-common.md)外，还支持以下属性：

### startPoint

startPoint(value: Array<any>)

设置直线起点坐标点（相对于Line组件绘制区域的左上角原点），支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，异常值按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<any> | 是 | 直线起点坐标点（相对于Line组件绘制区域的左上角原点），单位vp。数组格式为[x坐标, y坐标]，数组长度必须为2，元素应为Length类型。  默认值：[0, 0]  异常值undefined和null按照默认值处理。 |

### endPoint

endPoint(value: Array<any>)

设置直线终点坐标点（相对于Line组件绘制区域的左上角原点），支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，异常值按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<any> | 是 | 直线终点坐标点（相对于Line组件绘制区域的左上角原点），单位vp。数组格式为[x坐标, y坐标]，数组长度必须为2，元素应为Length类型。  默认值：[0, 0]  异常值undefined和null按照默认值处理。 |

## 示例

### 示例1（组件属性绘制）

通过startPoint、endPoint、strokeOpacity、stroke、strokeWidth、strokeDashArray、strokeDashOffset属性分别绘制直线的起始点、结束点、透明度、直线颜色、线条宽度、边框间隙、绘制起点。

```ts
// xxx.ets
@Entry
@Component
struct LineExample {
  build() {
    Column({ space: 10 }) {
      // 线条绘制的起止点坐标均是相对于Line组件本身绘制区域的坐标
      Line()
        .width(200)
        .height(150)
        .startPoint([0, 0])
        .endPoint([50, 100])
        .stroke(Color.Black)
        .backgroundColor('#F5F5F5')
      // 设置起始点为(50, 50)，终点为(150, 150)，线条宽度为5，线条颜色为橙色，线条透明度为0.5
      Line()
        .width(200)
        .height(150)
        .startPoint([50, 50])
        .endPoint([150, 150])
        .strokeWidth(5)
        .stroke(Color.Orange)
        .strokeOpacity(0.5)
        .backgroundColor('#F5F5F5')
      // strokeDashOffset用于定义关联虚线strokeDashArray数组渲染时的偏移
      Line()
        .width(200)
        .height(150)
        .startPoint([0, 0])
        .endPoint([100, 100])
        .stroke(Color.Black)
        .strokeWidth(3)
        .strokeDashArray([10, 3])
        .strokeDashOffset(5)
        .backgroundColor('#F5F5F5')
      // 当坐标点设置的值超出Line组件的宽高范围时，线条会画出组件绘制区域。设置虚线模式：线段长度10，间隙长度3
      Line()
        .width(50)
        .height(50)
        .startPoint([0, 0])
        .endPoint([100, 100])
        .stroke(Color.Black)
        .strokeWidth(3)
        .strokeDashArray([10, 3])
        .backgroundColor('#F5F5F5')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/X2_QJwAHQNqlwFyn15mOZA/zh-cn_image_0000002736435317.png)

### 示例2（线条端点绘制）

通过strokeLineCap属性绘制直线的线条端点样式。

```ts
// xxx.ets
@Entry
@Component
struct LineExample1 {
  build() {
    Row({ space: 10 }) {
      // 当LineCapStyle值为Butt时
      Line()
        .width(100)
        .height(200)
        .startPoint([50, 50])
        .endPoint([50, 200])
        .stroke(Color.Black)
        .strokeWidth(20)
        .strokeLineCap(LineCapStyle.Butt)
        .backgroundColor('#F5F5F5')
        .margin(10)
      // 当LineCapStyle值为Round时
      Line()
        .width(100)
        .height(200)
        .startPoint([50, 50])
        .endPoint([50, 200])
        .stroke(Color.Black)
        .strokeWidth(20)
        .strokeLineCap(LineCapStyle.Round)
        .backgroundColor('#F5F5F5')
      // 当LineCapStyle值为Square时
      Line()
        .width(100)
        .height(200)
        .startPoint([50, 50])
        .endPoint([50, 200])
        .stroke(Color.Black)
        .strokeWidth(20)
        .strokeLineCap(LineCapStyle.Square)
        .backgroundColor('#F5F5F5')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/PLeOGVucRaWk_UoBVdidCA/zh-cn_image_0000002706836170.png)

### 示例3（线条间隙绘制）

通过strokeDashArray属性绘制直线的线条间隙。

```ts
// xxx.ets
@Entry
@Component
struct LineExample {
  build() {
    Column() {
      Line()
        .width(300)
        .height(30)
        .startPoint([50, 30])
        .endPoint([300, 30])
        .stroke(Color.Black)
        .strokeWidth(10)
      // 设置strokeDashArray的数组间隔为 50
      Line()
        .width(300)
        .height(30)
        .startPoint([50, 20])
        .endPoint([300, 20])
        .stroke(Color.Black)
        .strokeWidth(10)
        .strokeDashArray([50])
      // 设置strokeDashArray的数组间隔为 50, 10
      Line()
        .width(300)
        .height(30)
        .startPoint([50, 20])
        .endPoint([300, 20])
        .stroke(Color.Black)
        .strokeWidth(10)
        .strokeDashArray([50, 10])
      // 设置strokeDashArray的数组间隔为 50, 10, 20
      Line()
        .width(300)
        .height(30)
        .startPoint([50, 20])
        .endPoint([300, 20])
        .stroke(Color.Black)
        .strokeWidth(10)
        .strokeDashArray([50, 10, 20])
      // 设置strokeDashArray的数组间隔为 50, 10, 20, 30
      Line()
        .width(300)
        .height(30)
        .startPoint([50, 20])
        .endPoint([300, 20])
        .stroke(Color.Black)
        .strokeWidth(10)
        .strokeDashArray([50, 10, 20, 30])
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/LCMJXh2ERiKGp7AuJY-qtg/zh-cn_image_0000002736315275.png)

### 示例4（宽和高使用不同参数类型绘制直线）

width、height属性分别使用不同的长度类型绘制直线。

```ts
// xxx.ets
@Entry
@Component
struct LineTypeExample {
  build() {
    Column({ space: 10 }) {
      // 在200 * 200的区域内绘制一个起始点为（0,0），终点为（150,150），线条宽度为10的直线
      Line({ width: '200', height: '200' })// 使用string类型
        .startPoint([0, 0])
        .endPoint([150, 150])
        .stroke(Color.Black)
        .strokeWidth(10)
        .backgroundColor('#F5F5F5')
        .margin(10)
      // 在200 * 200的区域内绘制一个起始点为（0,50），终点为（150,150），线条宽度为10的直线
      Line({ width: 200, height: 200 })// 使用number类型
        .startPoint([0, 50])
        .endPoint([150, 150])
        .stroke(Color.Black)
        .strokeWidth(10)
        .backgroundColor('#F5F5F5')
        .margin(10)
      // 在200 * 200的区域内绘制一个起始点为（0,100），终点为（150,150），线条宽度为10的直线
      Line({ width: $r('app.string.LineWidth'), height: $r('app.string.LineHeight') })// 使用Resource类型，需用户自定义
        .startPoint([0, 100])
        .endPoint([150, 150])
        .stroke(Color.Black)
        .strokeWidth(10)
        .backgroundColor('#F5F5F5')
        .margin(10)
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/25S_V9MZS1exuGGNA4b0Bg/zh-cn_image_0000002706676236.png)

### 示例5（使用attributeModifier动态设置Line组件的属性）

以下示例展示了如何使用attributeModifier动态设置Line组件的startPoint、endPoint、stroke、strokeDashArray、strokeDashOffset、strokeLineCap、strokeOpacity、strokeWidth和antiAlias属性。

```ts
// xxx.ets
class MyLineModifier implements AttributeModifier<LineAttribute> {
  applyNormalAttribute(instance: LineAttribute): void {
    // 一个起始点为（10, 10），终点为（120, 10）的直线，线条颜色#2787D9，线条间隙[20]，设置虚线偏移量为15，线条两端样式为半圆，线条透明度0.5，线条宽度10，抗锯齿开启
    instance.startPoint([10, 10])
    instance.endPoint([120, 10])
    instance.stroke('#2787D9')
    instance.strokeDashArray([20])
    instance.strokeDashOffset('15')
    instance.strokeLineCap(LineCapStyle.Round)
    instance.strokeOpacity(0.5)
    instance.strokeWidth(10)
    instance.antiAlias(true)
  }
}

@Entry
@Component
struct LineModifierDemo {
  @State modifier: MyLineModifier = new MyLineModifier()

  build() {
    Column() {
      Line()
        .attributeModifier(this.modifier)
        .offset({ x: 20, y: 20 })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Bdt7B51HS9uUjzuZjRKdCg/zh-cn_image_0000002736435319.png)
