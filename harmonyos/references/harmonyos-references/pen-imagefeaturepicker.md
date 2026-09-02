---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker
title: imageFeaturePicker (全局取色功能)
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > ArkTS API > imageFeaturePicker (全局取色功能)
category: harmonyos-references
scraped_at: 2026-09-02T14:52:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ab848eac2e6e872978bcafde1af1f6746cf669ce7354160cbc796449a06b512d
---

全局取色的功能入口类。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { imageFeaturePicker } from '@kit.Penkit';
```

## PickedColorInfo

全局取色结果对象，包含取色的基本信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.ColorPicker

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [common2D.Color](js-apis-graphics-common2d.md#color) | 否 | 否 | 色值。 |
| colorSpace | [colorSpaceManager.ColorSpace](js-apis-colorspacemanager.md#colorspace) | 否 | 否 | 色域空间。 |
| timestamp | number | 否 | 否 | 时间戳，自系统启动以来经过的时间，单位：ms。 |
| brightness | number | 否 | 是 | 颜色的亮度，调用[pickHdrForResult](pen-imagefeaturepicker.md#pickhdrforresult)接口时会返回，单位：nit。 默认值：0。  **起始版本：** 26.0.0 |

## pickForResult

pickForResult(x?: number, y?: number): Promise<PickedColorInfo>

全局取色，不支持实时显示RGB值。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.ColorPicker

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 否 | 取色器初始位置的x轴坐标。取值范围：0~屏幕的实际宽度，取值超出上限取屏幕的实际宽度，单位：px，默认值：100。 |
| y | number | 否 | 取色器初始位置的y轴坐标。取值范围：0~屏幕的实际高度，取值超出上限取屏幕的实际高度，单位：px，默认值：100。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PickedColorInfo](pen-imagefeaturepicker.md#pickedcolorinfo)> | Promise对象，返回取色执行的结果。该Promise对象用于获取全局取色操作的结果，当取色成功时，会返回一个包含颜色信息的对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-pen.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 801 | api is not supported |
| 1013900001 | IPC communication failed |
| 1013900002 | memory is insufficient |
| 1013900003 | service is invalid |
| 1013900004 | multi app call |
| 1013900005 | background service call |

**示例：**

```typescript
import { imageFeaturePicker } from '@kit.Penkit';

try {
    // 参数0表示取色器初始位置的x轴坐标和y轴坐标，实际使用时应根据用户交互获取具体坐标。
  imageFeaturePicker.pickForResult(0, 0).then(info => {
    console.info(`info is ${JSON.stringify(info)}`);
  })
} catch (error) {
  console.error(`Failed to pickForResult. code: ${error.code}, message: ${error.message}`);
}
```

## pickForResult

pickForResult(x?: number, y?: number, showValue?: boolean): Promise<PickedColorInfo>

全局取色，支持实时显示RGB值。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.ColorPicker

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 否 | 取色器初始位置的x轴坐标。取值范围：0~屏幕的实际宽度，取值超出上限取屏幕的实际宽度，单位：px，默认值：100。 |
| y | number | 否 | 取色器初始位置的y轴坐标。取值范围：0~屏幕的实际高度，取值超出上限取屏幕的实际高度，单位：px，默认值：100。 |
| showValue | boolean | 否 | 是否显示RGB值。true：显示RGB值，false：不显示RGB值。  默认值：false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PickedColorInfo](pen-imagefeaturepicker.md#pickedcolorinfo)> | Promise对象，返回取色执行的结果。该Promise对象用于获取全局取色操作的结果，当取色成功时，会返回一个包含颜色信息的对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-pen.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 801 | api is not supported |
| 1013900001 | IPC communication failed |
| 1013900002 | memory is insufficient |
| 1013900003 | service is invalid |
| 1013900004 | multi app call |
| 1013900005 | background service call |

**示例：**

```typescript
import { imageFeaturePicker } from '@kit.Penkit';

try {
    // 参数0表示取色器初始位置的x轴坐标和y轴坐标，实际使用时应根据用户交互获取具体坐标；true表示显示RGB值。
  imageFeaturePicker.pickForResult(0, 0, true).then(info => {
    console.info(`info is ${JSON.stringify(info)}`);
  })
} catch (error) {
  console.error(`Failed to pickForResult. code: ${error.code}, message: ${error.message}`);
}
```

## pickHdrForResult

pickHdrForResult(x?: number, y?: number): Promise<PickedColorInfo>

全局取色（支持HDR图片），不支持实时显示RGB值。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.ColorPicker

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 否 | 取色器初始位置的x轴坐标。取值范围：0~屏幕的实际宽度，取值超出上限取屏幕的实际宽度，单位：px，默认值：100。 |
| y | number | 否 | 取色器初始位置的y轴坐标。取值范围：0~屏幕的实际高度，取值超出上限取屏幕的实际高度，单位：px，默认值：100。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PickedColorInfo](pen-imagefeaturepicker.md#pickedcolorinfo)> | Promise对象，返回取色执行的结果。该Promise对象用于获取全局取色操作的结果，当取色成功时，会返回一个包含颜色信息的对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-pen.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. The pickHdrForResult function cannot work properly due to limited device capabilities. |
| 1013900001 | IPC failed. |
| 1013900002 | Insufficient memory. |
| 1013900003 | Invalid service. |
| 1013900004 | Multi-app calling. |
| 1013900005 | Background service calling. |

**示例：**

```typescript
import { imageFeaturePicker } from '@kit.Penkit';

try {
    // 参数0表示取色器初始位置的x轴坐标和y轴坐标，实际使用时应根据用户交互获取具体坐标。
  imageFeaturePicker.pickHdrForResult(0, 0).then(info => {
    console.info(`info is ${JSON.stringify(info)}`);
  })
} catch (error) {
  console.error(`Failed to pickHdrForResult. code: ${error.code}, message: ${error.message}`);
}
```

## pickHdrForResult

pickHdrForResult(x?: number, y?: number, showValue?: boolean): Promise<PickedColorInfo>

全局取色（支持HDR图片），支持实时显示RGB值。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.ColorPicker

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 否 | 取色器初始位置的x轴坐标。取值范围：0~屏幕的实际宽度，取值超出上限取屏幕的实际宽度，单位：px，默认值：100。 |
| y | number | 否 | 取色器初始位置的y轴坐标。取值范围：0~屏幕的实际高度，取值超出上限取屏幕的实际高度，单位：px，默认值：100。 |
| showValue | boolean | 否 | 是否显示RGB值。true：显示RGB值，false：不显示RGB值。  默认值：false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PickedColorInfo](pen-imagefeaturepicker.md#pickedcolorinfo)> | Promise对象，返回取色执行的结果。该Promise对象用于获取全局取色操作的结果，当取色成功时，会返回一个包含颜色信息的对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-pen.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. The pickHdrForResult function cannot work properly due to limited device capabilities. |
| 1013900001 | IPC failed. |
| 1013900002 | Insufficient memory. |
| 1013900003 | Invalid service. |
| 1013900004 | Multi-app calling. |
| 1013900005 | Background service calling. |

**示例：**

```typescript
import { imageFeaturePicker } from '@kit.Penkit';

try {
    // 参数0表示取色器初始位置的x轴坐标和y轴坐标，实际使用时应根据用户交互获取具体坐标；true表示显示RGB值。
  imageFeaturePicker.pickHdrForResult(0, 0, true).then(info => {
    console.info(`info is ${JSON.stringify(info)}`);
  })
} catch (error) {
  console.error(`Failed to pickHdrForResult. code: ${error.code}, message: ${error.message}`);
}
```
