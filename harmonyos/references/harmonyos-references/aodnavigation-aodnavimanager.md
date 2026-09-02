---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/aodnavigation-aodnavimanager
title: aodNaviManager (熄屏导航服务)
breadcrumb: API参考 > 系统 > 硬件 > AOD Navigation Kit（熄屏导航服务） > ArkTS API > aodNaviManager (熄屏导航服务)
category: harmonyos-references
scraped_at: 2026-09-02T14:52:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7dbb94e2c01abbc5dce83d880e14cf5f96769df7e6b586ce82cb3fb4679dae57
---

本模块提供AOD Navigation Kit的基础能力，包括检查设备是否支持熄屏导航服务、检查熄屏导航开关状态、获取熄屏导航扩展能力集、熄屏导航初始化配置、规划路线设置、更新熄屏导航视图数据及数据同步等核心功能。

**起始版本：** 26.0.0

## 导入模块

```typescript
import { aodNaviManager } from '@kit.AODNavigationKit';
```

## aodNaviManager.isAodNaviSupported

isAodNaviSupported(): boolean

检查设备是否支持熄屏导航功能。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回设备是否支持熄屏导航功能。true表示支持，false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-aodnavigation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1028300001 | AOD navigation service initialization failed. |

**示例：**

```typescript
import { abilityAccessCtrl, common } from '@kit.AbilityKit';
import { aodNaviManager } from '@kit.AODNavigationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let supported: boolean = aodNaviManager.isAodNaviSupported();
hilog.info(0x0000, 'aodnavigationSample', 'Succeeded in checking whether AOD navigation is supported, supported: %{public}s', supported);
```

## aodNaviManager.isAodNaviSwitchEnabled

isAodNaviSwitchEnabled(): Promise<boolean>

检查熄屏导航开关是否已启用，使用Promise异步回调。只有在设置页面中启用开关后，应用才能接入熄屏导航功能。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示熄屏导航开关开启；返回false表示熄屏导航开关关闭。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-aodnavigation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1028300001 | AOD navigation service initialization failed. |
| 1028300002 | Marshalling or unmarshalling error. |

**示例：**

```typescript
import { aodNaviManager } from '@kit.AODNavigationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

aodNaviManager.isAodNaviSwitchEnabled().then((enabled: boolean) => {
  hilog.info(0x0000, 'aodnavigationSample', 'Succeeded in checking whether AOD navigation switch is enabled, enabled: %{public}s', enabled);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'aodnavigationSample', 'Failed to check whether AOD navigation switch is enabled: %{public}d %{public}s', err.code, err.message);
});
```

## aodNaviManager.getAodNaviExtendCapabilities

getAodNaviExtendCapabilities(): AodNaviExtendDataType[]

获取熄屏导航服务的扩展能力集，使用Promise异步回调。不同设备可能支持不同的扩展能力，用户可以使用此接口检查支持的能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AodNaviExtendDataType](aodnavigation-aodnavimanager.md#aodnaviextenddatatype)[] | 返回支持的扩展数据类型列表。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-aodnavigation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1028300001 | AOD navigation service initialization failed. |

**示例：**

```typescript
import { aodNaviManager } from '@kit.AODNavigationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let capabilities: aodNaviManager.AodNaviExtendDataType[] = aodNaviManager.getAodNaviExtendCapabilities();
hilog.info(0x0000, 'aodnavigationSample', 'Succeeded in getting AOD navigation extend capabilities, capabilities: %{public}s', JSON.stringify(capabilities));
```

## aodNaviManager.setupAodNaviConfig

setupAodNaviConfig(config: AodNaviConfig): Promise<void>

熄屏导航配置初始化。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**设备行为差异：** 在支持熄屏导航功能的Phone设备上可正常调用，在不支持熄屏导航功能的Phone设备上返回801错误码，可调用[isAodNaviSupported](aodnavigation-aodnavimanager.md#aodnavimanagerisaodnavisupported)接口调用当前设备是否支持。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [AodNaviConfig](aodnavigation-aodnavimanager.md#aodnaviconfig) | 是 | 熄屏导航配置对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-aodnavigation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported because the device is not supported by the chip. |
| 1028300001 | AOD navigation service initialization failed. |
| 1028300002 | Marshalling or unmarshalling error. |
| 1028300003 | Service dependency error. |
| 1028300004 | The AOD navigation permission is not enabled. |
| 1028300005 | The AOD navigation switch is not enabled. |
| 1028300009 | Invalid AOD view data count. Possible causes: 1.Data count must be within the range of 1 to 6. 2.Data count does not match the number of configured entries. 3.Configuration includes items unsupported by the current device. |

**示例：**

```typescript
import { aodNaviManager } from '@kit.AODNavigationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let config: aodNaviManager.AodNaviConfig = {
  aliveStrategy: aodNaviManager.AodNaviAliveStrategy.KEEP_ALIVE,
  aodViewDataConfig: {
    aodViewDataCount: 4,
    aodViewDataTypes: [
      aodNaviManager.AodNaviBasicDataType.DISTANCE,
      aodNaviManager.AodNaviBasicDataType.STEPS,
      aodNaviManager.AodNaviBasicDataType.CURRENT_SPEED,
      aodNaviManager.AodNaviBasicDataType.OVERALL_ELAPSED_TIME
    ]
  },
  aodVoiceBroadcastConfig: {
    distance: 1000,
    timeInterval: 60,
    enableGpsBroadcast: true
  },
  aodProxyDataTypes: [
    aodNaviManager.AodNaviBasicDataType.DISTANCE,
    aodNaviManager.AodNaviBasicDataType.STEPS,
    aodNaviManager.AodNaviBasicDataType.CURRENT_SPEED
  ]
};

aodNaviManager.setupAodNaviConfig(config).then(() => {
  hilog.info(0x0000, 'aodnavigationSample', 'Succeeded in setting up AOD navigation config.');
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'aodnavigationSample', 'Failed to set up AOD navigation config: %{public}d %{public}s', err.code, err.message);
});
```

## aodNaviManager.onAodNaviEvent

onAodNaviEvent(callback: Callback<AodNaviEventInfo>): void

注册熄屏导航事件监听。只允许注册一个回调，新回调将覆盖之前的回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[AodNaviEventInfo](aodnavigation-aodnavimanager.md#aodnavieventinfo)> | 是 | 熄屏导航事件的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-aodnavigation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1028300001 | AOD navigation service initialization failed. |
| 1028300002 | Marshalling or unmarshalling error. |
| 1028300003 | Service dependency error. |
| 1028300004 | The AOD navigation permission is not enabled. |

**示例：**

```typescript
import { aodNaviManager } from '@kit.AODNavigationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

aodNaviManager.onAodNaviEvent((eventInfo: aodNaviManager.AodNaviEventInfo) => {
  hilog.info(0x0000, 'aodnavigationSample', 'Received AOD navigation event: eventType: %{public}d, eventId: %{public}s', eventInfo.eventType, eventInfo.eventId);
  
  switch (eventInfo.eventType) {
    case aodNaviManager.AodNaviEventType.AOD_NAVI_ENTER:
      hilog.info(0x0000, 'aodnavigationSample', 'AOD navigation enter event handled.');
      break;
    case aodNaviManager.AodNaviEventType.AOD_NAVI_EXIT:
      hilog.info(0x0000, 'aodnavigationSample', 'AOD navigation exit event handled.');
      break;
    case aodNaviManager.AodNaviEventType.AOD_NAVI_DATA_CACHE:
      hilog.info(0x0000, 'aodnavigationSample', 'AOD navigation data cache event handled.');
      break;
    case aodNaviManager.AodNaviEventType.AOD_NAVI_VOICE_BROADCAST:
      hilog.info(0x0000, 'aodnavigationSample', 'AOD navigation voice broadcast event handled.');
      break;
  }
});
```

## aodNaviManager.offAodNaviEvent

offAodNaviEvent(callback?: Callback<AodNaviEventInfo>): void

解注册熄屏导航事件监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[AodNaviEventInfo](aodnavigation-aodnavimanager.md#aodnavieventinfo)> | 否 | AOD交互事件的回调函数，如果不传则停止所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-aodnavigation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1028300001 | AOD navigation service initialization failed. |
| 1028300002 | Marshalling or unmarshalling error. |

**示例：**

```typescript
import { aodNaviManager } from '@kit.AODNavigationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  aodNaviManager.offAodNaviEvent();
  hilog.info(0x0000, 'aodnavigationSample', 'Succeeded in stopping AOD navigation event listener.');
  } catch (error) {
    hilog.error(0x0000, 'aodNavigationSample', 'Failed to stop AOD navigation event listener:  %{public}d %{public}s', error.code, error.message);
}
```

## aodNaviManager.setPlanRouteToAod

setPlanRouteToAod(planRoutes: PlanRoute[], markPoints?: MarkPoint[]): Promise<void>

设置熄屏导航规划路线至AOD Navigation Kit，熄屏导航界面进行导航规划路线绘制，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**设备行为差异：** 在支持熄屏导航功能的Phone设备上可正常调用，在不支持熄屏导航功能的Phone设备上返回801错误码，可调用[isAodNaviSupported](aodnavigation-aodnavimanager.md#aodnavimanagerisaodnavisupported)接口调用当前设备是否支持。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| planRoutes | [PlanRoute](aodnavigation-aodnavimanager.md#planroute)[] | 是 | 规划路线数组。  **说明**：数组最大长度限制为50000个，若路线轨迹点超过50000个点，需要应用进行抽稀后下发。 |
| markPoints | [MarkPoint](aodnavigation-aodnavimanager.md#markpoint)[] | 否 | 标记点列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-aodnavigation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported because the device is not supported by the chip. |
| 1028300001 | AOD navigation service initialization failed. |
| 1028300002 | Marshalling or unmarshalling error. |
| 1028300006 | The AOD navigation configuration has not been set up. |
| 1028300007 | The number of route points exceeds the limit. |
| 1028300011 | Failed to save the route points. |

**示例：**

```typescript
import { aodNaviManager } from '@kit.AODNavigationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let planRoutes: aodNaviManager.PlanRoute[] = [
  { longitude: 116.404, latitude: 39.915 },
  { longitude: 116.414, latitude: 39.925 },
  { longitude: 116.424, latitude: 39.935 }
];

let markPoints: aodNaviManager.MarkPoint[] = [
  { name: '起点', longitude: 116.404, latitude: 39.915 },
  { name: '终点', longitude: 116.424, latitude: 39.935 }
];

aodNaviManager.setPlanRouteToAod(planRoutes, markPoints).then(() => {
  hilog.info(0x0000, 'aodnavigationSample', 'Succeeded in setting plan route to AOD.');
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'aodnavigationSample', 'Failed to set plan route to AOD: %{public}d %{public}s', err.code, err.message);
});
```

## aodNaviManager.setNaviDataToAod

setNaviDataToAod(eventId: string, aodNaviInteractData: AodNaviInteractData): Promise<void>

将设备亮屏期间应用产生的轨迹及导航数据同步至AOD Navigation Kit。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**设备行为差异：** 在支持熄屏导航功能的Phone设备上可正常调用，在不支持熄屏导航功能的Phone设备上返回801错误码，可调用[isAodNaviSupported](aodnavigation-aodnavimanager.md#aodnavimanagerisaodnavisupported)接口调用当前设备是否支持。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 熄屏导航事件ID。 |
| aodNaviInteractData | [AodNaviInteractData](aodnavigation-aodnavimanager.md#aodnaviinteractdata) | 是 | 设备亮屏期间应用产生的轨迹及导航数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-aodnavigation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported because the device is not supported by the chip. |
| 1028300001 | AOD navigation service initialization failed. |
| 1028300002 | Marshalling or unmarshalling error. |
| 1028300006 | The AOD navigation configuration has not been set up. |
| 1028300007 | The number of route points exceeds the limit. |
| 1028300008 | Invalid event ID. |
| 1028300011 | Failed to save the route points. |

**示例：**

```typescript
import { aodNaviManager } from '@kit.AODNavigationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventId: string = 'event_123456';
let historyRoutes: aodNaviManager.HistoryRoute[] = [
  { timestamp: 1234567890, longitude: 116.404, latitude: 39.915 },
  { timestamp: 1234567891, longitude: 116.405, latitude: 39.916 }
];

let aodNaviData: aodNaviManager.AodNaviData = {
  timestamp: Date.now() / 1000,
  distance: 1000,
  steps: 1500,
  currentSpeed: 5.5
};

let aodNaviInteractData: aodNaviManager.AodNaviInteractData = {
  historyRoutes: historyRoutes,
  aodNaviData: aodNaviData
};

aodNaviManager.setNaviDataToAod(eventId, aodNaviInteractData).then(() => {
  hilog.info(0x0000, 'aodnavigationSample', 'Succeeded in setting navigation data to AOD.');
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'aodnavigationSample', 'Failed to set navigation data to AOD: %{public}d %{public}s', err.code, err.message);
});
```

## aodNaviManager.updateAodViewData

updateAodViewData(aodViewData: AodViewData): Promise<void>

更新熄屏导航界面视图数据。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**设备行为差异：** 在支持熄屏导航功能的Phone设备上可正常调用，在不支持熄屏导航功能的Phone设备上返回801错误码，可调用[isAodNaviSupported](aodnavigation-aodnavimanager.md#aodnavimanagerisaodnavisupported)接口调用当前设备是否支持。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aodViewData | [AodViewData](aodnavigation-aodnavimanager.md#aodviewdata) | 是 | 熄屏导航界面视图数据配置项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-aodnavigation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported because the device is not supported by the chip. |
| 1028300001 | AOD navigation service initialization failed. |
| 1028300002 | Marshalling or unmarshalling error. |
| 1028300006 | The AOD navigation configuration has not been set up. |
| 1028300010 | UpdateAodViewData must not be called under the hibernate strategy. |

**示例：**

```typescript
import { aodNaviManager } from '@kit.AODNavigationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let aodViewData: aodNaviManager.AodViewData = {
  "distance": 1500,
  "steps": 2000,
  "currentSpeed": 6.0
};

aodNaviManager.updateAodViewData(aodViewData).then(() => {
  hilog.info(0x0000, 'aodnavigationSample', 'Succeeded in updating AOD view data.');
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'aodnavigationSample', 'Failed to update AOD view data: %{public}d %{public}s', err.code, err.message);
});
```

## aodNaviManager.updateAppRecordStatus

updateAppRecordStatus(recordStatus: AppRecordStatus): Promise<void>

更新应用导航记录状态。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**设备行为差异：** 在支持熄屏导航功能的Phone设备上可正常调用，在不支持熄屏导航功能的Phone设备上返回801错误码，可调用[isAodNaviSupported](aodnavigation-aodnavimanager.md#aodnavimanagerisaodnavisupported)接口调用当前设备是否支持。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recordStatus | [AppRecordStatus](aodnavigation-aodnavimanager.md#apprecordstatus) | 是 | 应用导航记录状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-aodnavigation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported because the device is not supported by the chip. |
| 1028300001 | AOD navigation service initialization failed. |
| 1028300002 | Marshalling or unmarshalling error. |
| 1028300006 | The AOD navigation configuration has not been set up. |

**示例：**

```typescript
import { aodNaviManager } from '@kit.AODNavigationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

aodNaviManager.updateAppRecordStatus(aodNaviManager.AppRecordStatus.RECORDING).then(() => {
  hilog.info(0x0000, 'aodnavigationSample', 'Succeeded in updating app record status.');
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'aodnavigationSample', 'Failed to update app record status: %{public}d %{public}s', err.code, err.message);
});
```

## aodNaviManager.onAltitudeClimbChange

onAltitudeClimbChange(callback: Callback<AltitudeClimbInfo>): void

注册累计爬升变化监听。只允许注册一个回调，新回调将覆盖之前的回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**设备行为差异：** 在支持累计爬升功能的Phone设备上可正常调用，在不支持累计爬升功能的Phone设备上返回801错误码，可调用[getAodNaviExtendCapabilities](aodnavigation-aodnavimanager.md#aodnavimanagergetaodnaviextendcapabilities)接口获取设备是否支持累计爬升能力。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[AltitudeClimbInfo](aodnavigation-aodnavimanager.md#altitudeclimbinfo)> | 是 | 返回累计爬升信息的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-aodnavigation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | The capability is not supported because the barometer is not supported. |
| 1028300001 | AOD navigation service initialization failed. |
| 1028300002 | Marshalling or unmarshalling error. |
| 1028300003 | Service dependency error. |
| 1028300006 | The AOD navigation configuration has not been set up. |

**示例：**

```typescript
import { aodNaviManager } from '@kit.AODNavigationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
try {
  aodNaviManager.onAltitudeClimbChange((info: aodNaviManager.AltitudeClimbInfo) => {
    hilog.info(0x0000, 'aodnavigationSample', 'Altitude climb change - climbUp: %{public}d, climbDown: %{public}d', info.accumulateClimbUp, info.accumulateClimbDown);
  });
} catch (error) {
    hilog.error(0x0000, 'aodNavigationSample', 'Failed to subscribe altitude climb change: %{public}d %{public}s', error.code, error.message);
}
```

## aodNaviManager.offAltitudeClimbChange

offAltitudeClimbChange(callback?: Callback<AltitudeClimbInfo>): void

解注册累计爬升变化监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[AltitudeClimbInfo](aodnavigation-aodnavimanager.md#altitudeclimbinfo)> | 否 | 回调函数，如果省略则移除所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-aodnavigation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1028300002 | Marshalling or unmarshalling error. |

**示例：**

```typescript
import { aodNaviManager } from '@kit.AODNavigationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

aodNaviManager.offAltitudeClimbChange();
hilog.info(0x0000, 'aodnavigationSample', 'Succeeded in unsubscribing from altitude climb change.');
```

## AodNaviConfig

熄屏导航配置项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| aliveStrategy | [AodNaviAliveStrategy](aodnavigation-aodnavimanager.md#aodnavialivestrategy) | 否 | 否 | 熄屏导航时应用休眠策略。  **说明**：配置项差异导致的具体运行差异请查看[运行机制](../harmonyos-guides/aodnavigation-introduction.md#运行机制)。 |
| aodViewDataConfig | [AodViewDataConfig](aodnavigation-aodnavimanager.md#aodviewdataconfig) | 否 | 否 | 熄屏导航界面视图数据项配置。 |
| aodVoiceBroadcastConfig | [AodVoiceBroadcastConfig](aodnavigation-aodnavimanager.md#aodvoicebroadcastconfig) | 否 | 是 | 熄屏导航语音播报配置。  **说明**：仅在应用保活策略为休眠时需要配置该项。 |
| aodProxyDataTypes | [AodNaviDataType](aodnavigation-aodnavimanager.md#aodnavidatatype)[] | 否 | 是 | 熄屏导航代理数据项配置。  **说明**：熄屏导航时此部分数据项将由AOD Navigation Kit进行代理计算。仅在应用保活策略为休眠时需要配置该项。 |

## AodNaviInteractData

应用与AOD Navigation Kit之间的交互数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| historyRoutes | [HistoryRoute](aodnavigation-aodnavimanager.md#historyroute)[] | 否 | 否 | 历史轨迹点列表。  **说明**：设备亮屏期间应用产生的轨迹数据和熄屏导航期间AOD代理产生的轨迹数据。数组长度最大限制为50000。 |
| aodNaviData | [AodNaviData](aodnavigation-aodnavimanager.md#aodnavidata) | 否 | 否 | 导航数据。  **说明**：设备亮屏期间应用产生的导航数据（里程、步数等）和熄屏导航期间AOD代理产生的导航数据。 |
| historyClimbInfo | [AltitudeClimbInfo](aodnavigation-aodnavimanager.md#altitudeclimbinfo)[] | 否 | 是 | 历史爬升信息。  **说明**：设备亮屏期间应用产生的海拔爬升数据和熄屏导航期间AOD代理产生的海拔爬升数据。 |

## AltitudeClimbInfo

海拔爬升信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 否 | 是 | 累计爬升时间戳。单位：秒。值应为整数。 |
| accumulateClimbUp | number | 否 | 否 | 累计爬升高度。单位：米。值应为整数。 |
| accumulateClimbDown | number | 否 | 否 | 累计下降高度。单位：米。值应为整数。 |

## AodNaviData

熄屏导航数据，包括距离、步数及步频等数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 否 | 否 | 导航数据时间戳。单位：秒。值应为整数。 |
| lastBroadcastTimestamp | number | 否 | 是 | 上次广播时间戳。单位：秒。值应为整数。 |
| distance | number | 否 | 是 | 距离。单位：km。值保留两位小数。 |
| steps | number | 否 | 是 | 步数。 |
| cadence | number | 否 | 是 | 步频。单位：步/分钟。值应为整数。 |
| overallElapsedTime | number | 否 | 是 | 总用时。单位：秒。 |
| sportElapsedTime | number | 否 | 是 | 运动用时。单位：秒。 |
| currentSpeed | number | 否 | 是 | 当前速度。单位：km/h。 |
| overallAvgSpeed | number | 否 | 是 | 总平均速度。单位：km/h。 |
| sportAvgSpeed | number | 否 | 是 | 运动平均速度。单位：km/h。 |
| currentPace | number | 否 | 是 | 当前配速。单位：分钟/km。 |
| avgPace | number | 否 | 是 | 平均配速。单位：分钟/km。 |
| altitudeClimbInfo | [AltitudeClimbInfo](aodnavigation-aodnavimanager.md#altitudeclimbinfo) | 否 | 是 | 累计爬升信息。 |

## AodVoiceBroadcastConfig

熄屏导航语音播报配置项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| distance | number | 否 | 是 | 里程碑距离。单位：km。值应为整数。 |
| timeInterval | number | 否 | 是 | 时间间隔阈值。单位：分钟。 |
| yawDistanceThreshold | number | 否 | 是 | 偏航距离阈值。单位：km。 |
| yawIntervalSeconds | number | 否 | 是 | 偏航播报时间间隔。单位：秒。值应为整数。 |
| enableGpsBroadcast | boolean | 否 | 是 | 是否启用GPS状态变化播报。 |
| altitudeClimbUpThreshold | number | 否 | 是 | 累计爬升阈值。单位：米。值应为整数。 |
| altitudeClimbDownThreshold | number | 否 | 是 | 累计下降阈值。单位：米。值应为整数。 |
| speedThreshold | number | 否 | 是 | 速度阈值。单位：km/h。 |
| markPointDistanceThreshold | number[] | 否 | 是 | 标记点距离阈值。单位：米。 |
| broadcastContent | [AodNaviDataType](aodnavigation-aodnavimanager.md#aodnavidatatype)[] | 否 | 是 | 熄屏导航播报内容。 |

## AodViewDataConfig

熄屏导航视图数据配置项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| aodViewDataCount | number | 否 | 否 | 数据项数量。值必须为[1，6]范围内的整数。 |
| aodViewDataTypes | [AodNaviDataType](aodnavigation-aodnavimanager.md#aodnavidatatype)[] | 否 | 否 | 熄屏导航视图数据列表，熄屏界面将根据应用配置顺序进行显示布局。  **说明**：如果应用休眠策略为保活时，可跳过能力检查直接应用所有配置。否则，在配置之前必须检查扩展能力是否支持。 |

## PlanRoute

规划路线信息，包括经度和纬度。采用GCJ02坐标系标准。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| longitude | number | 否 | 否 | 经度。 |
| latitude | number | 否 | 否 | 纬度。 |

## HistoryRoute

历史轨迹信息。采用GCJ02坐标系标准。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 否 | 否 | 时间戳。单位：毫秒。 |
| longitude | number | 否 | 否 | 经度。 |
| latitude | number | 否 | 否 | 纬度。 |
| altitude | number | 否 | 是 | 海拔。单位：米。值应为整数。 |
| hSpeed | number | 否 | 是 | 水平速度。单位：km/h。 |

## MarkPoint

标记点信息。采用GCJ02坐标系标准。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 是 | 标记点名称。 |
| longitude | number | 否 | 否 | 经度。 |
| latitude | number | 否 | 否 | 纬度。 |

## AodNaviEventInfo

熄屏导航事件信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eventId | string | 是 | 否 | 唯一事件标识符。 |
| eventType | [AodNaviEventType](aodnavigation-aodnavimanager.md#aodnavieventtype) | 否 | 否 | 事件类型。 |
| eventData | [AodNaviInteractData](aodnavigation-aodnavimanager.md#aodnaviinteractdata) | [VoiceBroadcastData](aodnavigation-aodnavimanager.md#voicebroadcastdata) | 否 | 是 | 应用与AOD Navigation Kit之间的交互数据或语音播报数据。 |

## VoiceBroadcastData

语音播报数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 否 | 否 | 语音播报触发时间戳。单位：秒。值应为整数。 |
| voiceBroadcastEvent | [VoiceBroadcastEvent](aodnavigation-aodnavimanager.md#voicebroadcastevent) | 否 | 否 | 语音播报事件类型。 |
| voiceBroadcastParam | number | [GPSStatus](aodnavigation-aodnavimanager.md#gpsstatus) | [MarkPointIndexToDistance](aodnavigation-aodnavimanager.md#markpointindextodistance) | 否 | 否 | 语音播报参数。 |
| voiceBroadcastContent | [AodNaviData](aodnavigation-aodnavimanager.md#aodnavidata) | 否 | 否 | 语音播报内容。 |

## AodNaviDataType

type AodNaviDataType = AodNaviBasicDataType | AodNaviExtendDataType

熄屏导航服务数据类型，主要包括基础数据类型和扩展数据类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 类型 | 说明 |
| --- | --- |
| [AodNaviBasicDataType](aodnavigation-aodnavimanager.md#aodnavibasicdatatype) | 熄屏导航基础数据类型。 |
| [AodNaviExtendDataType](aodnavigation-aodnavimanager.md#aodnaviextenddatatype) | 熄屏导航扩展数据类型。 |

## AodViewData

type AodViewData = Partial<Record<AodNaviDataType, number>>

熄屏导航视图数据，用于更新熄屏导航显示数据项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 类型 | 说明 |
| --- | --- |
| Record<[AodNaviDataType](aodnavigation-aodnavimanager.md#aodnavidatatype), number> | 熄屏导航数据类型到数值的映射。 |

## MarkPointIndexToDistance

type MarkPointIndexToDistance = Record<number, number>

标记点索引到距离的映射。用于熄屏导航语音播报。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 类型 | 说明 |
| --- | --- |
| Record<number, number> | 标记点索引到距离的映射。用于语音播报。 |

## AodNaviBasicDataType

熄屏导航基本数据类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISTANCE | 'distance' | 距离。 |
| STEPS | 'steps' | 步数。 |
| CADENCE | 'cadence' | 步频。 |
| OVERALL\_ELAPSED\_TIME | 'overallElapsedTime' | 总用时。 |
| SPORT\_ELAPSED\_TIME | 'sportElapsedTime' | 运动用时。 |
| CURRENT\_SPEED | 'currentSpeed' | 当前速度。 |
| OVERALL\_AVG\_SPEED | 'overallAvgSpeed' | 总平均速度。 |
| SPORT\_AVG\_SPEED | 'sportAvgSpeed' | 运动平均速度。 |
| CURRENT\_PACE | 'currentPace' | 当前配速。 |
| AVG\_PACE | 'avgPace' | 平均配速。 |

## AodNaviExtendDataType

熄屏导航扩展数据类型枚举。扩展数据类型依赖于设备硬件支持。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALTITUDE\_CLIMB\_UP | 'altitudeClimbUp' | 累计爬升高度。 |
| ALTITUDE\_CLIMB\_DOWN | 'altitudeClimbDown' | 累计下降高度。 |

## AodNaviEventType

熄屏导航事件回调类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AOD\_NAVI\_ENTER | 0 | 设备熄屏进入熄屏导航。  **说明**：接收到该类型回调事件后，应用需要：  1. 调用[setNaviDataToAod](aodnavigation-aodnavimanager.md#aodnavimanagersetnavidatatoaod)接口，将设备亮屏期间应用产生的轨迹和导航数据下发至AOD Navigation Kit  2. 若休眠策略为应用休眠，建议延后5秒释放长时任务以平衡性能，并主动丢弃该期间返回的数据。  3. 若休眠策略为应用保活，可启动定时刷新任务，通过[updateAodViewData](aodnavigation-aodnavimanager.md#aodnavimanagerupdateaodviewdata)接口更新熄屏数据，刷新频率最高为1秒/次。 |
| AOD\_NAVI\_EXIT | 1 | 设备亮屏退出熄屏导航。  **说明**：接收到该类型回调事件后，应用需要：  1. 若休眠策略为应用休眠，回调返回熄屏期间系统代理产生的轨迹点和导航数据，应用收到后进行数据合并。  2. 若休眠策略为应用保活，收到回调事件后，应用需暂停刷新熄屏界面数据项信息。 |
| AOD\_NAVI\_DATA\_CACHE | 2 | 熄屏导航数据缓存事件。  **说明**：当AOD Navigation Kit数据缓存满时（达到1440个轨迹点），将熄屏导航期间缓存的导航数据返回给应用。 |
| AOD\_NAVI\_VOICE\_BROADCAST | 3 | 熄屏导航期间语音播报事件。  **说明**：熄屏导航期间触发了语音播报条件，AOD Navigation Kit不支持语音播报能力，需要应用接收到播报事件后进行语音播报。 |

## VoiceBroadcastEvent

语音播报事件类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISTANCE | 0 | 距离。 |
| TIME | 1 | 时间。 |
| YAW | 2 | 偏航距离。 |
| GPS\_STATUS\_CHANGE | 3 | GPS状态变化。 |
| ALTITUDE\_CLIMB\_UP | 4 | 累计爬升。 |
| ALTITUDE\_CLIMB\_DOWN | 5 | 累计下降。 |
| SPEED | 6 | 速度阈值。 |
| MARK\_POINT | 7 | 标记点距离。 |

## AodNaviAliveStrategy

熄屏导航应用保活策略：应用休眠或保活。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HIBERNATE | 1 | 应用休眠。  **说明**：熄屏导航时导航业务由AOD代理，熄屏导航界面显示数据由AOD代理产生。 |
| KEEP\_ALIVE | 2 | 应用保活。  **说明**：熄屏导航时导航业务仍然运行在应用，熄屏导航界面显示数据来源于应用。 |

## GPSStatus

GPS状态枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOCATING | 0 | 定位中。 |
| CONNECTED | 1 | 已连接。 |
| DISCONNECTED | 2 | 已断开。 |

## AppRecordStatus

应用导航记录状态枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PhoneService.AodNaviService

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RECORDING | 0 | 记录中。 |
| PAUSED | 1 | 暂停。  **说明**：在应用暂停导航状态下，AOD Navigation Kit会同步暂停业务代理的计算，且熄屏界面不展示内容。 |
