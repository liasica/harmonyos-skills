---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-stylusinteraction
title: stylusInteraction (手写笔交互功能)
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > ArkTS API > stylusInteraction (手写笔交互功能)
category: harmonyos-references
scraped_at: 2026-04-28T08:10:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:408ee4d2715f3801c7e0bb7c0938a262b3399bfcb7c9fad7f69f1b323d719e5e
---

手写笔交互功能入口类，当前包含手写笔笔身轻捏事件和手写笔笔身双击事件。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 5.1.1(19)

## 导入模块

PhonePC/2in1Tablet

```
1. import { stylusInteraction } from '@kit.Penkit';
```

## stylusInteraction.on('squeeze')

PhonePC/2in1Tablet

on(type: 'squeeze', receiver: Callback<SqueezeEvent>): void

监听手写笔笔身轻捏事件。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"squeeze"字符串，表示手写笔笔身轻捏事件。 |
| receiver | Callback<[SqueezeEvent](pen-stylusinteraction.md#squeezeevent)> | 是 | 回调函数，返回手写笔笔身轻捏事件的详细信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. stylusInteraction.on('squeeze', (event: stylusInteraction.SqueezeEvent) => {
5. console.info(`got squeeze event, time: ${event.timestamp}`);
6. });
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## stylusInteraction.off('squeeze')

PhonePC/2in1Tablet

off(type: 'squeeze', receiver?: Callback<SqueezeEvent>): void

取消监听手写笔笔身轻捏事件。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"squeeze"字符串，表示手写笔笔身轻捏事件。 |
| receiver | Callback<[SqueezeEvent](pen-stylusinteraction.md#squeezeevent)> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的轻捏事件。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. stylusInteraction.off('squeeze', (event: stylusInteraction.SqueezeEvent) => {
4. console.info(`off squeeze event, time: ${event.timestamp}`);
5. });
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

## stylusInteraction.on('doubleTap')

PhonePC/2in1Tablet

on(type: 'doubleTap', receiver: Callback<DoubleTapEvent>): void

监听手写笔笔身双击事件。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"doubleTap"字符串，表示手写笔笔身双击事件。 |
| receiver | Callback<[DoubleTapEvent](pen-stylusinteraction.md#doubletapevent)> | 是 | 回调函数，返回手写笔笔身双击事件的详细信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. stylusInteraction.on('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
4. console.info(`got doubleTap event, time: ${event.timestamp}`);
5. });
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

## stylusInteraction.off('doubleTap')

PhonePC/2in1Tablet

off(type: 'doubleTap', receiver?: Callback<DoubleTapEvent>): void

取消监听手写笔笔身双击事件。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 5.1.1(19)

**参数：：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"doubleTap"字符串，表示手写笔笔身双击事件。 |
| receiver | Callback<[DoubleTapEvent](pen-stylusinteraction.md#doubletapevent)> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的双击事件。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. stylusInteraction.off('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
4. console.info(`off doubleTap event, time: ${event.timestamp}`);
5. });
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

## SqueezeEvent

PhonePC/2in1Tablet

手写笔笔身轻捏事件信息。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 5.1.1(19)

**参数：**

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| timestamp | number | 否 | 否 | 时间戳，自系统启动以来经过的时间，单位：ms。 |

## DoubleTapEvent

PhonePC/2in1Tablet

手写笔笔身双击事件信息。

**系统能力：** SystemCapability.Stylus.StylusService

**起始版本：** 5.1.1(19)

**参数：**

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| timestamp | number | 否 | 否 | 时间戳，自系统启动以来经过的时间，单位：ms。 |
