---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-tapgesture
title: TapGesture
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 手势处理 > 基础手势 > TapGesture
category: harmonyos-references
scraped_at: 2026-09-05T06:17:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:819b9cb3b02e45824dd858501c534c787c6ed9ab9208519e9e64141a30cf0287
---

支持单击、双击和多次点击事件的识别，适用于为组件绑定点击交互、区分不同点击次数并触发对应业务逻辑的场景。

**说明** 

从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

当组件同时绑定双击和单击手势且双击手势先绑定时，单击手势会有300ms的延时。

## 接口

TapGesture(value?: TapGestureParameters)

创建点击手势对象。继承自[GestureInterface<T>](ts-gesture-common.md#gestureinterfacet11)。

触发点击手势事件的设备类型为键盘或手柄时，事件的[SourceTool](ts-gesture-settings.md#sourcetool枚举说明9)值为Unknown；设备类型为键盘时，事件的[SourceType](ts-gesture-settings.md#sourcetype枚举说明8)值为KEY；设备类型为手柄时，事件的[SourceType](ts-gesture-settings.md#sourcetype枚举说明8)值为JOYSTICK。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TapGestureParameters](ts-basic-gestures-tapgesture.md#tapgestureparameters12对象说明) | 否 | 点击手势的相关参数。用于配置连续点击次数、触发点击的手指数、点击手势移动阈值等点击识别条件；当需要自定义点击手势识别条件时传入。不传入时使用TapGestureParameters中各参数的默认配置。 |

## TapGestureParameters12+对象说明

**说明** 

为规范匿名对象的定义，API 12版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

点击手势参数。继承自[BaseHandlerOptions](ts-gesturehandler.md#basehandleroptions15)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| count11+ | number | 否 | 是 | 识别的连续点击次数。当设置的值小于1或不设置时，会被转化为默认值。  默认值：1  取值范围：[0, +∞)  **说明：**  1. 当配置多击时，上一次的最后一根手指抬起和下一次的第一根手指按下的超时时间为300毫秒。  2. 当上次点击的位置与当前点击的位置距离超过60vp时，手势识别失败。在多指情况下，点击的位置为所有参与手势响应的手指的平均位置。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fingers11+ | number | 否 | 是 | 触发点击的手指数，取值范围：[1, 10]，单位：指。当设置小于1的值或不设置时，会被转化为默认值。  默认值：1  **说明：**  1. 当配置多指时，第一根手指按下后300毫秒内未有足够的手指数按下，手势识别失败；手指抬起时，抬起后剩余的手指数小于阈值时开始计时，如300ms内未全部抬起则手势识别失败。  2. 实际点击手指数超过配置值，手势识别成功。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| distanceThreshold | number | 否 | 是 | 点击手势移动阈值。当设置的值小于等于0或不设置时，会被转化为默认值。  默认值：2³¹-1  取值范围：(0, +∞)  单位：vp  **说明：**  当手指的移动距离超出开发者预设的移动阈值时，点击识别失败。使用默认阈值时，手指移动超过组件热区范围，点击识别失败。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## 事件

**说明** 

组件通过手势事件绑定不同GestureType的手势对象，各手势对象在响应手势操作的事件回调中提供手势相关信息。下面通过TapGesture手势对象的[onAction](ts-basic-gestures-tapgesture.md#onaction)事件响应点击事件，获取事件相关信息。其余手势对象的事件定义见各个手势对象章节。 若需绑定多种手势，请使用[GestureGroup](ts-combined-gestures.md)。

在[GestureEvent](ts-gesture-common.md#gestureevent对象说明)的fingerList元素中，手指索引编号与位置相对应，即fingerList[index]的id为index。对于先按下但未参与当前手势触发的手指，fingerList中对应的位置为空。建议优先使用fingerInfos。

### onAction

onAction(event: (event: GestureEvent) => void)

点击手势识别成功回调。当组件同时绑定双击和单击手势且双击手势先绑定时，单击手势对应的onAction回调会有300ms的延时。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 手势事件回调函数，用于在点击手势识别成功时接收手势事件信息。回调参数event表示点击手势事件对象，包含手势触发位置、手指信息等事件相关数据。 |

## EventLocationInfo20+

用于点击手势获取点击位置坐标。

### 属性

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 相对于组件左上角的X坐标。  取值范围：[0, +∞)  单位：vp  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| y | number | 否 | 否 | 相对于组件左上角的Y坐标。  取值范围：[0, +∞)  单位：vp  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| windowX | number | 否 | 否 | 相对于窗口的左上角X坐标。  取值范围：[0, +∞)  单位：vp  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| windowY | number | 否 | 否 | 相对于窗口的左上角Y坐标。  取值范围：[0, +∞)  单位：vp  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| displayX | number | 否 | 否 | 相对于屏幕的左上角X坐标。  取值范围：[0, +∞)  单位：vp  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| displayY | number | 否 | 否 | 相对于屏幕的左上角Y坐标。  取值范围：[0, +∞)  单位：vp  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| globalDisplayX23+ | number | 否 | 是 | 相对于主屏幕左上角为原点的坐标系中的X坐标。未获取到该坐标时，该属性为undefined。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| globalDisplayY23+ | number | 否 | 是 | 相对于主屏幕左上角为原点的坐标系中的Y坐标。未获取到该坐标时，该属性为undefined。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

### getCurrentLocalPosition

getCurrentLocalPosition?(): Coordinate2D

获取点击位置相对于当前组件实时位置的左上角坐标。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Coordinate2D](ts-types.md#coordinate2d) | 返回Coordinate2D对象，用于表示点击位置相对于当前组件实时位置左上角的二维坐标。 |

## 示例

### 示例1（双击手势识别）

该示例通过TapGesture实现了双击手势的识别。

```ts
// xxx.ets
@Entry
@Component
struct TapGestureExample {
  @State value: string = '';

  build() {
    Column() {
      // 单指双击文本触发手势事件
      Text('Click twice').fontSize(28)
        .gesture(
        TapGesture({ count: 2 })
          .onAction((event: GestureEvent) => {
            if (event) {
              this.value = JSON.stringify(event.fingerList[0]);
            }
          })
        );
      Text(this.value);
    }
    .height(300)
    .width(300)
    .padding(20)
    .border({ width: 3 })
    .margin(30);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/rMJn84bvQMK8a__7gKkiaA/zh-cn_image_0000002742004921.gif)

### 示例2（获取单击手势坐标）

该示例通过TapGesture获取单击手势点击位置的坐标。

```ts
// xxx.ets
@Entry
@Component
struct TapGestureExample {

  build() {
    Column() {
      Text('Click Once').fontSize(28)
        .gesture(
          TapGesture({ count: 1, fingers: 1 })
            .onAction((event: GestureEvent | undefined) => {
              if (event) {
                console.info(`x = ${JSON.stringify(event.tapLocation?.x)}`);
                console.info(`y = ${JSON.stringify(event.tapLocation?.y)}`);
                console.info(`windowX = ${JSON.stringify(event.tapLocation?.windowX)}`);
                console.info(`windowY = ${JSON.stringify(event.tapLocation?.windowY)}`);
                console.info(`displayX = ${JSON.stringify(event.tapLocation?.displayX)}`);
                console.info(`displayY = ${JSON.stringify(event.tapLocation?.displayY)}`);
                // 从API version 23开始，新增globalDisplayX和globalDisplayY属性。
                console.info(`globalDisplayX = ${JSON.stringify(event.tapLocation?.globalDisplayX)}`);
                console.info(`globalDisplayY = ${JSON.stringify(event.tapLocation?.globalDisplayY)}`);
              }
            })
        );
    }
    .height(200)
    .width(300)
    .padding(20)
    .border({ width: 3 })
    .margin(30)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/qH2GMqLMThCQhxNDighfTg/zh-cn_image_0000002712405932.png)

### 示例3（获取组件实时位置）

该示例通过[getCurrentLocalPosition](ts-basic-gestures-tapgesture.md#getcurrentlocalposition)方法获取点击位置相对于当前组件实时位置左上角的坐标。

从API版本26.0.0开始，新增支持getCurrentLocalPosition接口。

```ts
// xxx.ets
@Entry
@Component
struct GetCurrentLocalPositionExample {
  @State positionText: string = '';
  @State textOffsetY: number = 0;

  build() {
    Column() {
      Button('点击获取点击位置相对于当前组件实时位置左上角的坐标').translate({ y: this.textOffsetY })
        .gesture(
          TapGesture({ count: 1 })
            .onAction((event: GestureEvent) => {
              if (event) {
                // 移动组件后延迟获取点击位置相对于组件实时位置左上角的坐标。
                this.textOffsetY = -200;
                setTimeout(() => {
                  let localPos: Coordinate2D | undefined = event?.tapLocation?.getCurrentLocalPosition?.();
                  this.positionText = `相对于当前组件实时位置左上角的坐标:\n  x: ${localPos?.x ?? 0}\n  y: ${localPos?.y ?? 0}`;
                }, 2000);
              }
            })
        );

      Text(this.positionText);
    }.width('100%');
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/jzmWA49JRu2xEqnPG-8LWw/zh-cn_image_0000002712405800.gif)
