---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-thermal
title: "@ohos.thermal (热管理)"
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 设备管理 > @ohos.thermal (热管理)
category: harmonyos-references
scraped_at: 2026-11-04T08:35:03+08:00
doc_updated_at: 2026-11-03
content_hash: sha256:cab475c50e95e5d199a1e0ea659c70a9928bba086e9933f46b68fef3c62a5c4f
---

该模块提供热管理相关的接口，包括热档位查询及注册回调等功能。

**说明** 

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import {thermal} from '@kit.BasicServicesKit';
```

## thermal.registerThermalLevelCallback9+

registerThermalLevelCallback(callback: Callback<ThermalLevel>): void

订阅热档位变化时的回调提醒。当设备温度跨越档位阈值导致热档位发生变化时，系统自动触发回调通知，通过callback返回变化后的热档位等级。使用callback异步回调。此方法与[thermal.unregisterThermalLevelCallback](js-apis-thermal.md#thermalunregisterthermallevelcallback9)配对使用，用于取消先前注册的热档位回调。

* 每个进程仅支持订阅一个回调，重复订阅将覆盖。
* 回调函数应尽快返回，不可执行耗时操作（如同步文件 I/O），否则可能阻塞系统热档位通知投递。
* 当热管理服务异常重启后，已注册的回调将自动失效且不会收到通知。开发者需重新调用 registerThermalLevelCallback 恢复订阅。
* 当热管理服务不可用时，订阅可能静默失败且不抛出异常。开发者无法从返回值判断订阅是否成功。建议在订阅后通过[thermal.getLevel](js-apis-thermal.md#thermalgetlevel9)验证服务是否可用（若[thermal.getLevel](js-apis-thermal.md#thermalgetlevel9)返回COOL且设备明显发热，则服务可能不可用）。

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

```js
try {
    thermal.registerThermalLevelCallback((level: thermal.ThermalLevel) => {
        console.info('thermal level is: ' + level);
    });
    console.info('register thermal level callback success.');
} catch(err) {
    console.error('register thermal level callback failed, err: ' + err);
}
```

## thermal.unregisterThermalLevelCallback9+

unregisterThermalLevelCallback(callback?: Callback<void>): void

取消订阅热档位变化时的回调提醒。使用callback异步回调。此方法与[thermal.registerThermalLevelCallback](js-apis-thermal.md#thermalregisterthermallevelcallback9)配对使用，用于取消先前注册的热档位回调。取消订阅未注册的回调不会报错，视为无操作。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 否 | 回调函数。反注册完成后的通知回调，无返回值。该参数仅用于接收取消订阅完成的通知，取消订阅成功后会调用该回调函数。不传入此参数时，取消订阅仍生效，但不会触发回调通知。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```js
try {
    thermal.unregisterThermalLevelCallback(() => {
        console.info('unsubscribe thermal level success.');
    });
    console.info('unregister thermal level callback success.');
} catch(err) {
    console.error('unregister thermal level callback failed, err: ' + err);
}
```

## thermal.getLevel9+

getLevel(): ThermalLevel

获取当前热档位信息。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ThermalLevel](js-apis-thermal.md#thermallevel) | 热档位信息。 |

**示例：**

```js
let level = thermal.getLevel();
console.info('thermal level is: ' + level);
```

## thermal.subscribeThermalLevel(deprecated)

subscribeThermalLevel(callback: AsyncCallback<ThermalLevel>): void

订阅热档位变化时的回调提醒。使用callback异步回调。

**说明** 

从API version 8开始支持，从API version 9开始不再维护，建议使用[thermal.registerThermalLevelCallback](js-apis-thermal.md#thermalregisterthermallevelcallback9)替代。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ThermalLevel](js-apis-thermal.md#thermallevel)> | 是 | 回调函数，返回变化后的热档位；该参数是一个函数类型。 |

**示例：**

```js
thermal.subscribeThermalLevel((err: Error, level: thermal.ThermalLevel) => {
    console.info('thermal level is: ' + level);
});
```

## thermal.unsubscribeThermalLevel(deprecated)

unsubscribeThermalLevel(callback?: AsyncCallback<void>): void

取消订阅热档位变化时的回调提醒。使用callback异步回调。

**说明** 

从API version 8开始支持，从API version 9开始不再维护，建议使用[thermal.unregisterThermalLevelCallback](js-apis-thermal.md#thermalunregisterthermallevelcallback9)替代。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 否 | 回调函数，无返回值。不填该参数则取消所有回调。 |

**示例：**

```js
thermal.unsubscribeThermalLevel(() => {
    console.info('unsubscribe thermal level success.');
});
```

## thermal.getThermalLevel(deprecated)

getThermalLevel(): ThermalLevel

获取当前热档位信息。

**说明** 

从API version 8开始支持，从API version 9开始不再维护，建议使用[thermal.getLevel](js-apis-thermal.md#thermalgetlevel9)替代。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ThermalLevel](js-apis-thermal.md#thermallevel) | 热档位信息。 |

**示例：**

```js
let level = thermal.getThermalLevel();
console.info('thermal level is: ' + level);
```

## ThermalLevel

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
