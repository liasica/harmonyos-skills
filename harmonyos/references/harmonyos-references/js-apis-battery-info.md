---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-battery-info
title: @ohos.batteryInfo (电量信息)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 设备管理 > @ohos.batteryInfo (电量信息)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3dbbcfc615f7a71c3b329f74d0f301baf6065d27d77889dd4eacf2420d064235
---

该模块主要提供电池状态和充放电状态的查询接口。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletWearable

```
1. import {batteryInfo} from '@kit.BasicServicesKit';
```

## 常量

PhonePC/2in1TabletWearable

描述电池信息。

**系统能力**：SystemCapability.PowerManager.BatteryManager.Core

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| batterySOC | number | 是 | 表示当前设备剩余电池电量百分比。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| chargingStatus | [BatteryChargeState](js-apis-battery-info.md#batterychargestate) | 是 | 表示当前设备电池的充电状态。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| healthStatus | [BatteryHealthState](js-apis-battery-info.md#batteryhealthstate) | 是 | 表示当前设备电池的健康状态。 |
| pluggedType | [BatteryPluggedType](js-apis-battery-info.md#batterypluggedtype) | 是 | 表示当前设备连接的充电器类型。 |
| voltage | number | 是 | 表示当前设备电池的电压，单位微伏。 |
| technology | string | 是 | 表示当前设备电池的技术型号。 |
| batteryTemperature | number | 是 | 表示当前设备电池的温度，单位0.1摄氏度。 |
| isBatteryPresent7+ | boolean | 是 | 表示当前设备是否支持电池或者电池是否在位。true表示支持电池或电池在位，false表示不支持电池或电池不在位，默认为false。 |
| batteryCapacityLevel9+ | [BatteryCapacityLevel](js-apis-battery-info.md#batterycapacitylevel9) | 是 | 表示当前设备电池电量的等级。 |
| nowCurrent12+ | number | 是 | 表示当前设备电池的电流，单位毫安。 |

**示例**：

```
1. import {batteryInfo} from '@kit.BasicServicesKit';

3. let batterySOCInfo: number = batteryInfo.batterySOC;
4. console.info("The batterySOCInfo is: " + batterySOCInfo);

6. let chargingStatusInfo = batteryInfo.chargingStatus;
7. console.info("The chargingStatusInfo is: " + chargingStatusInfo);

9. let healthStatusInfo = batteryInfo.healthStatus;
10. console.info("The healthStatusInfo is: " + healthStatusInfo);

12. let pluggedTypeInfo = batteryInfo.pluggedType;
13. console.info("The pluggedTypeInfo is: " + pluggedTypeInfo);

15. let voltageInfo: number = batteryInfo.voltage;
16. console.info("The voltageInfo is: " + voltageInfo);

18. let technologyInfo: string = batteryInfo.technology;
19. console.info("The technologyInfo is: " + technologyInfo);

21. let batteryTemperatureInfo: number = batteryInfo.batteryTemperature;
22. console.info("The batteryTemperatureInfo is: " + batteryTemperatureInfo);

24. let isBatteryPresentInfo: boolean = batteryInfo.isBatteryPresent;
25. console.info("The isBatteryPresentInfo is: " + isBatteryPresentInfo);

27. let batteryCapacityLevelInfo = batteryInfo.batteryCapacityLevel;
28. console.info("The batteryCapacityLevelInfo is: " + batteryCapacityLevelInfo);

30. let nowCurrentInfo: number = batteryInfo.nowCurrent;
31. console.info("The nowCurrentInfo is: " + nowCurrentInfo);
```

## BatteryPluggedType

PhonePC/2in1TabletWearable

表示连接的充电器类型的枚举。

**系统能力**：SystemCapability.PowerManager.BatteryManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 表示未获取到连接充电器类型。 |
| AC | 1 | 表示连接的充电器类型为交流充电器。 |
| USB | 2 | 表示连接的充电器类型为USB。 |
| WIRELESS | 3 | 表示连接的充电器类型为无线充电器。 |

## BatteryChargeState

PhonePC/2in1TabletWearable

表示电池充电状态的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.PowerManager.BatteryManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 表示电池充电状态为未充电。 |
| ENABLE | 1 | 表示电池充电状态为使能状态。 |
| DISABLE | 2 | 表示电池充电状态为停止状态。 |
| FULL | 3 | 表示电池充电状态为已充满状态。 |

## BatteryHealthState

PhonePC/2in1TabletWearable

表示电池健康状态的枚举。

**系统能力**：SystemCapability.PowerManager.BatteryManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 表示电池健康状态未知。 |
| GOOD | 1 | 表示电池健康状态为正常。 |
| OVERHEAT | 2 | 表示电池健康状态为过热。 |
| OVERVOLTAGE | 3 | 表示电池健康状态为过压。 |
| COLD | 4 | 表示电池健康状态为低温。 |
| DEAD | 5 | 表示电池健康状态为僵死状态。 |

## BatteryCapacityLevel9+

PhonePC/2in1TabletWearable

表示电池电量等级的枚举。

**系统能力**：SystemCapability.PowerManager.BatteryManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEVEL\_NONE23+ | 0 | 表示电池电量等级为未知电量。 |
| LEVEL\_FULL | 1 | 表示电池电量等级为满电量。 |
| LEVEL\_HIGH | 2 | 表示电池电量等级为高电量。 |
| LEVEL\_NORMAL | 3 | 表示电池电量等级为正常电量。 |
| LEVEL\_LOW | 4 | 表示电池电量等级为低电量。 |
| LEVEL\_WARNING | 5 | 表示电池电量等级为告警电量。 |
| LEVEL\_CRITICAL | 6 | 表示电池电量等级为极低电量。 |
| LEVEL\_SHUTDOWN | 7 | 表示电池电量等级为关机电量。 |

## CommonEventBatteryChangedKey9+

PhonePC/2in1TabletWearable

表示COMMON\_EVENT\_BATTERY\_CHANGED通用事件附加信息的查询键。

**系统能力**：SystemCapability.PowerManager.BatteryManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXTRA\_SOC | "soc" | 表示剩余电池电量百分比的查询键。 |
| EXTRA\_CHARGE\_STATE | "chargeState" | 表示当前设备电池充电状态的查询键。 |
| EXTRA\_HEALTH\_STATE | "healthState" | 表示当前设备电池健康状态的查询键。 |
| EXTRA\_PLUGGED\_TYPE | "pluggedType" | 表示当前设备连接的充电器类型的查询键。 |
| EXTRA\_VOLTAGE | "voltage" | 表示当前设备电池电压的查询键。 |
| EXTRA\_TECHNOLOGY | "technology" | 表示当前设备电池技术型号的查询键。 |
| EXTRA\_TEMPERATURE | "temperature" | 表示当前设备电池温度的查询键。 |
| EXTRA\_PRESENT | "present" | 表示当前设备是否支持电池或者电池是否在位的查询键。 |
| EXTRA\_CAPACITY\_LEVEL | "capacityLevel" | 表示当前设备电池电量等级的查询键。 |
