---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-animation
title: Class (Animation)
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > Class (Animation)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4edd00653704bf75cd0c5d51be65cdd3afa6db0c72f23242c398d95f383016d8
---

## 导入模块

```typescript
import { map } from '@kit.MapKit';
```

## Animation

动画抽象类。Animation类用于控制地图元素的动画效果，支持旋转、缩放、平移等多种动画类型，适用于地图交互增强、路径动画展示等场景。

**说明** 

动画持续时间默认值为250ms；

动画执行完成后的状态，默认值为[AnimationFillMode](map-map-enums.md#animationfillmode).FORWARDS；

动画插值器，默认值为[Curve](js-apis-curve.md#curve).Linear；

动画重复执行的次数，默认值为0；

重复执行的模式，默认值为[AnimationRepeatMode](map-map-enums.md#animationrepeatmode).RESTART。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```typescript
let animation = new map.RotateAnimation(0, 270);
// 动画执行时间
animation.setDuration(2000);

// 动画结束状态
animation.setFillMode(map.AnimationFillMode.BACKWARDS);

// 动画重复模式
animation.setRepeatMode(map.AnimationRepeatMode.REVERSE);

// 动画重复次数
animation.setRepeatCount(100);

// 根据开发需要设置动画监听
let callbackStart = () => {
  console.info("animationStart", `callback`);
};
let callbackEnd = () => {
  console.info("animationEnd", `callback`);
};
animation.on("animationStart", callbackStart);
animation.on("animationEnd", callbackEnd);
```

### setDuration

setDuration(duration: number): void

设置动画持续时间。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| duration | number | 是 | 动画持续时间，单位：ms，取值范围：大于等于0，异常值不处理。 |

**示例：**

```typescript
animation.setDuration(3000);
```

### setFillMode

setFillMode(fillMode: AnimationFillMode): void

设置动画执行完成后的状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| fillMode | [AnimationFillMode](map-map-enums.md#animationfillmode) | 是 | 动画执行完成后的状态。 |

**示例：**

```typescript
animation.setFillMode(map.AnimationFillMode.BACKWARDS);
```

### setInterpolator

setInterpolator(curve: Curves.Curve): void

设置动画插值器。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| curve | [Curves.Curve](js-apis-curve.md#curve) | 是 | 动画插值器。 |

**示例：**

```typescript
animation.setInterpolator(Curve.Linear);
```

### setRepeatCount

setRepeatCount(repeatCount: number): void

设置动画重复执行的次数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| repeatCount | number | 是 | 动画重复执行的次数。  正数：根据值重复执行  0：动画不重复执行  -1：执行次数是无限  小于-1或其他异常值，取值默认为0 |

**示例：**

```typescript
animation.setRepeatCount(100);
```

### setRepeatMode

setRepeatMode(repeatMode: AnimationRepeatMode): void

设置重复执行的模式，默认从前往后执行。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| repeatMode | [AnimationRepeatMode](map-map-enums.md#animationrepeatmode) | 是 | 重复执行的模式。 |

**示例：**

```typescript
animation.setRepeatMode(map.AnimationRepeatMode.RESTART);
```

### on('start')

on(type: 'start', callback: Callback<void>): void

监听动画开始事件。使用callback异步回调。

建议使用[animation.on(type: 'animationStart')](map-map-animation.md#onanimationstart)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'start'：动画开始事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果。 |

**示例：**

```typescript
animation.on("start", () => {
  console.info(`start alphaAnimation`);
});
```

### off('start')

off(type: 'start', callback: Callback<void>): void

取消监听动画开始事件。使用callback异步回调。

建议使用[animation.off(type: 'animationStart')](map-map-animation.md#offanimationstart)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'start'：动画开始事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果。 |

**示例：**

```typescript
animation.off("start", () => {
  console.info(`start alphaAnimation`);
});
```

### on('end')

on(type: 'end', callback: Callback<void>): void

监听动画结束事件。使用callback异步回调。

建议使用[animation.on(type: 'animationEnd')](map-map-animation.md#onanimationend)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'end'：动画结束事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果。 |

**示例：**

```typescript
animation.on("end", () => {
  console.info(`end alphaAnimation`);
});
```

### off('end')

off(type: 'end', callback: Callback<void>): void

取消监听动画结束事件。使用callback异步回调。

建议使用[animation.off(type: 'animationEnd')](map-map-animation.md#offanimationend)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'end'：动画结束事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果。 |

**示例：**

```typescript
animation.off("end", () => {
  console.info(`end alphaAnimation`);
});
```

### on('animationStart')

on(type: 'animationStart', callback: Callback<void>): void

监听动画开始事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'animationStart'：监听动画开始事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果。监听动画开始事件。 |

**示例：**

```typescript
let callback1 = () => {
  console.info("animationStart", `callback1`);
};
let callback2 = () => {
  console.info("animationStart", `callback2`);
};
let callback3 = () => {
  console.info("animationStart", `callback3`);
};
animation.on("animationStart", callback1);
animation.on("animationStart", callback2);
animation.on("animationStart", callback3);
```

### off('animationStart')

off(type: 'animationStart', callback?: Callback<void>): void

取消监听动画开始事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'animationStart'：监听动画开始事件。 |
| callback | Callback<void> | 否 | 回调函数，无返回结果。取消监听动画开始事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```typescript
let callback1 = () => {
  console.info("animationStart", `callback1`);
};
let callback2 = () => {
  console.info("animationStart", `callback2`);
};
let callback3 = () => {
  console.info("animationStart", `callback3`);
};
animation.on("animationStart", callback1);
animation.on("animationStart", callback2);
animation.on("animationStart", callback3);

// 只取消callback1对象的事件响应，当animationStart事件发生时，callback2和callback3会正常被调用
animation.off('animationStart', callback1);
// 取消全部animationStart事件响应
animation.off('animationStart');
```

### on('animationEnd')

on(type: 'animationEnd', callback: Callback<void>): void

监听动画结束事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'animationEnd'：动画结束事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果。监听动画结束事件。 |

**示例：**

```typescript
let callback1 = () => {
  console.info("animationEnd", `callback1`);
};
let callback2 = () => {
  console.info("animationEnd", `callback2`);
};
let callback3 = () => {
  console.info("animationEnd", `callback3`);
};
animation.on("animationEnd", callback1);
animation.on("animationEnd", callback2);
animation.on("animationEnd", callback3);
```

### off('animationEnd')

off(type: 'animationEnd', callback?: Callback<void>): void

取消监听动画结束事件。支持传递多个callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 'animationEnd'：监听动画结束事件。 |
| callback | Callback<void> | 否 | 回调函数，无返回结果。取消监听动画结束事件。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

**示例：**

```typescript
let callback1 = () => {
  console.info("animationEnd", `callback1`);
};
let callback2 = () => {
  console.info("animationEnd", `callback2`);
};
let callback3 = () => {
  console.info("animationEnd", `callback3`);
};
animation.on("animationEnd", callback1);
animation.on("animationEnd", callback2);
animation.on("animationEnd", callback3);

// 只取消callback1对象的事件响应，当animationEnd事件发生时，callback2和callback3会正常被调用
animation.off('animationEnd', callback1);
// 取消全部animationEnd事件响应
animation.off('animationEnd');
```
