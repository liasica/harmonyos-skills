---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-thermal
title: @ohos.thermal (热管理)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 设备管理 > @ohos.thermal (热管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9c6b77e08f7d96e46c130c9338887ddce0a4867be0f78a3b46791a684d39d9a8
---

该模块提供热管理相关的接口，包括热档位查询及注册回调等功能。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import {thermal} from '@kit.BasicServicesKit';
```

## thermal.registerThermalLevelCallback9+

PhonePC/2in1TabletTVWearable

registerThermalLevelCallback(callback: Callback<ThermalLevel>): void

**方法介绍：** 订阅热档位变化时的回调提醒。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[ThermalLevel](js-apis-thermal.md#thermallevel)> | 是 | 回调函数，返回变化后的热档位；该参数是一个函数类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```
1. try {
2. thermal.registerThermalLevelCallback((level: thermal.ThermalLevel) => {
3. console.info('thermal level is: ' + level);
4. });
5. console.info('register thermal level callback success.');
6. } catch(err) {
7. console.error('register thermal level callback failed, err: ' + err);
8. }
```

## thermal.unregisterThermalLevelCallback9+

PhonePC/2in1TabletTVWearable

unregisterThermalLevelCallback(callback?: Callback<void>): void

**方法介绍：** 取消订阅热档位变化时的回调提醒。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 否 | 可选参数，回调函数，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```
1. try {
2. thermal.unregisterThermalLevelCallback(() => {
3. console.info('unsubscribe thermal level success.');
4. });
5. console.info('unregister thermal level callback success.');
6. } catch(err) {
7. console.error('unregister thermal level callback failed, err: ' + err);
8. }
```

## thermal.getLevel9+

PhonePC/2in1TabletTVWearable

getLevel(): ThermalLevel

**方法介绍：** 获取当前热档位信息。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ThermalLevel](js-apis-thermal.md#thermallevel) | 热档位信息。 |

**示例：**

```
1. let level = thermal.getLevel();
2. console.info('thermal level is: ' + level);
```

## thermal.subscribeThermalLevel(deprecated)

PhonePC/2in1TabletTVWearable

subscribeThermalLevel(callback: AsyncCallback<ThermalLevel>): void

说明

从API version 8开始支持，从API version 9开始不再维护，建议使用[thermal.registerThermalLevelCallback](js-apis-thermal.md#thermalregisterthermallevelcallback9)替代。

**方法介绍：** 订阅热档位变化时的回调提醒。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ThermalLevel](js-apis-thermal.md#thermallevel)> | 是 | 回调函数。AsyncCallback只返回一个参数，为热档位信息。 |

**示例：**

```
1. thermal.subscribeThermalLevel((err: Error, level: thermal.ThermalLevel) => {
2. console.info('thermal level is: ' + level);
3. });
```

## thermal.unsubscribeThermalLevel(deprecated)

PhonePC/2in1TabletTVWearable

unsubscribeThermalLevel(callback?: AsyncCallback<void>): void

说明

从API version 8开始支持，从API version 9开始不再维护，建议使用[thermal.unregisterThermalLevelCallback](js-apis-thermal.md#thermalunregisterthermallevelcallback9)替代。

**方法介绍：** 取消订阅热档位变化时的回调提醒。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 否 | 回调函数，无返回值。不填该参数则取消所有回调。 |

**示例：**

```
1. thermal.unsubscribeThermalLevel(() => {
2. console.info('unsubscribe thermal level success.');
3. });
```

## thermal.getThermalLevel(deprecated)

PhonePC/2in1TabletTVWearable

getThermalLevel(): ThermalLevel

说明

从API version 8开始支持，从API version 9开始不再维护，建议使用[thermal.getLevel](js-apis-thermal.md#thermalgetlevel9)替代。

**方法介绍：** 获取当前热档位信息。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ThermalLevel](js-apis-thermal.md#thermallevel) | 热档位信息。 |

**示例：**

```
1. let level = thermal.getThermalLevel();
2. console.info('thermal level is: ' + level);
```

## ThermalLevel

PhonePC/2in1TabletTVWearable

热档位信息。

**系统能力：** SystemCapability.PowerManager.ThermalManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COOL | 0 | 表明设备处于清凉状态，业务执行不受热控的限制。 |
| NORMAL | 1 | 表明设备温度正常，但邻近温热状态，无感知业务应降低规格和负载。 |
| WARM | 2 | 表明设备进入温热状态，无感知业务应暂停或延迟运行。 |
| HOT | 3 | 表明设备发热明显，无感知业务应停止，非关键业务应降低规格及负载。 |
| OVERHEATED | 4 | 表明设备发热严重，无感知业务与非关键业务应停止，前台关键业务应降低规格及负载。 |
| WARNING | 5 | 表明设备过热即将进入紧急状态，整机资源供给大幅降低，停止所有非关键业务，前台关键业务应降低至最低规格。 |
| EMERGENCY | 6 | 表明设备已经进入过热紧急状态，整机资源供给降至最低，设备功能受限，仅保留基础功能可用。 |
| ESCAPE11+ | 7 | 表明设备即将进入热逃生状态，所有业务将被强制停止，业务需做好逃生措施，例如保存重要数据等。  **说明**: 从API version 11开始支持。 |
