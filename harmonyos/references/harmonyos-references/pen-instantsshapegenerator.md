---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-instantsshapegenerator
title: InstantShapeGenerator（一笔成形功能）
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > ArkTS API > InstantShapeGenerator（一笔成形功能）
category: harmonyos-references
scraped_at: 2026-04-28T08:10:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:add7ef9cccef229e8d668f32d3a5dad49bad2939404f88ac3e44ceb1536e96b0
---

一笔成形的功能入口类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { InstantShapeGenerator, ShapeInfo } from '@kit.Penkit';
```

本模块提供以下类或接口，支持获取一笔成形的图像。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| ShapeInfo | [ShapeInfo](pen-instantsshapegenerator.md#shapeinfo) | 一笔成形识别结果对象，包含识别的图像的基本信息。 |

本模块提供以下方法。

| 方法名称 | 说明 |
| --- | --- |
| [processTouchEvent](pen-instantsshapegenerator.md#processtouchevent) | 传递触摸事件。 |
| [getPathFromString](pen-instantsshapegenerator.md#getpathfromstring) | 从给定的形状字符串中提取形状信息。 |
| [notifyAreaChange](pen-instantsshapegenerator.md#notifyareachange) | 通知控件大小变化。 |
| [setPauseTime](pen-instantsshapegenerator.md#setpausetime) | 设置触发识别的暂停时间，单位：ms。 |
| [release](pen-instantsshapegenerator.md#release) | 销毁识别工具。 |
| [onShapeRecognized](pen-instantsshapegenerator.md#onshaperecognized) | 注册识别完成时的回调方法。 |

## ShapeInfo

PhonePC/2in1Tablet

一笔成形识别结果对象，包含识别的图像的基本信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

**参数**：

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| shapePath | [Path2D](ts-components-canvas-path2d.md) | 否 | 否 | 图形对象。 |
| shapeString | string | 否 | 否 | 图形信息，可以用于保存的。 |
| shapeType | number | 否 | 否 | 图形类型。  - 未知类型（识别失败）- 0  - 直线 - 1  - 圆（椭圆）- 2  - 折线 - 3  - 矩形 - 6  - 平行四边形 - 7  - 菱形 - 9  - 等腰三角形 - 10  - 等边三角形 - 11  - 五角星形 - 12  - 正五边形 - 13  - 抛物线形 - 14  - 直线单向箭头（箭头指向起点） - 15  - 直线单向箭头（箭头指向终点）- 16  - 直线双向箭头 - 17  - 抛物线单向箭头（箭头指向起点） - 18  - 抛物线单向箭头（箭头指向终点） - 19  - 抛物线双向箭头 - 20 |

**示例：**

```
1. private shapeInfo : ShapeInfo = {
2. shapePath: '',
3. shapeString: '',
4. shapeType: 0
5. }
```

## processTouchEvent

PhonePC/2in1Tablet

processTouchEvent(event: TouchEvent): void

传递触摸事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [TouchEvent](ts-universal-events-touch.md#touchevent对象说明) | 是 | 当前触摸点事件。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API 错误码](pen-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010410001 | internal recognition engine has been released. |

**示例：**

```
1. instantShapeGenerator: InstantShapeGenerator = new InstantShapeGenerator();
2. // 画布
3. @Builder
4. Canvas() {
5. Stack()
6. .width('100%')
7. .height('100%')
8. .onTouch((event: TouchEvent) => {
9. this.instantShapeGenerator?.processTouchEvent(event);
10. })
11. }
```

## getPathFromString

PhonePC/2in1Tablet

getPathFromString(shapeString: string, penSize: number): Path2D

从给定的形状字符串中提取形状信息，并使用该信息生成Path2D对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shapeString | string | 是 | 形状字符串。无取值范围限制。 |
| penSize | number | 是 | 用于绘制结果形状的笔宽。某些形状结果会根据此值而变化，例如箭头。单位：画布宽度的千分之一。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Path2D](ts-components-canvas-path2d.md) | 形状信息生成的Path2D对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API 错误码](pen-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010410001 | internal recognition engine has been released. |

**示例：**

```
1. // 通过回调方法获取识别结果
2. private shapeInfoCallback(shapeInfo: ShapeInfo) {
3. this.drawPath = this.instantShapeGenerator?.getPathFromString(shapeInfo.shapeString, this.penWidth);
4. }
```

## notifyAreaChange

PhonePC/2in1Tablet

notifyAreaChange(width: number, height: number): void

通知组件大小更改。形状的大小（例如圆的半径）根据组件尺寸而变化。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 组件变更后的宽度。单位：vp。 |
| height | number | 是 | 组件变更后的高度。单位：vp。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API 错误码](pen-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010410001 | internal recognition engine has been released. |

**示例：**

```
1. // 画布
2. @Builder Canvas() {
3. Stack()
4. .width('100%')
5. .height('100%')
6. .onAreaChange((oldValue, newValue) => {
7. this.instantShapeGenerator?.notifyAreaChange(Number(newValue.width), Number(newValue.height));
8. })
9. }
```

## setPauseTime

PhonePC/2in1Tablet

setPauseTime(time: number): void

设置触发识别的暂停时间。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| time | number | 是 | 触发识别的暂停时间。  单位：ms。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API 错误码](pen-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010410001 | internal recognition engine has been released. |

**示例：**

```
1. aboutToAppear() {
2. console.info('InstantShapeGenerator aboutToAppear')
3. this.instantShapeGenerator?.setPauseTime(280);
4. }
```

## release

PhonePC/2in1Tablet

release(): void

销毁一笔成形工具。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

**示例：**

```
1. aboutToDisappear(){
2. console.info('InstantShapeGenerator aboutToDisappear')
3. this.instantShapeGenerator?.release();
4. }
```

## onShapeRecognized

PhonePC/2in1Tablet

onShapeRecognized(callback: Callback<ShapeInfo>): InstantShapeGenerator

注册识别完成时的回调方法。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| callback | Callback<[ShapeInfo](pen-instantsshapegenerator.md#shapeinfo)> | 是 | 图形识别完成时回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| InstantShapeGenerator | 一笔成形工具方法类实例。 |

**示例：**

```
1. // 通过回调方法获取识别结果
2. private shapeInfoCallback(shapeInfo: ShapeInfo) {
3. this.shapeInfo = shapeInfo;
4. }

6. aboutToAppear() {
7. console.info('InstantShapeGenerator aboutToAppear')
8. this.instantShapeGenerator?.onShapeRecognized(this.shapeInfoCallback)
9. }
```
