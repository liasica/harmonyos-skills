---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-systemload
title: @ohos.resourceschedule.systemload (性能功耗热融合档位)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 其他 > @ohos.resourceschedule.systemload (性能功耗热融合档位)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b5e8fc33b2dc3f37fbdd0904422c4c1bf68d582e95faab3c3174f89ea717363e
---

系统根据当前温度、负载以及是否处于高负载场景等信息决策出系统负载融合档位，并在档位变化时通知已注册的应用。

说明

* 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { systemLoad } from '@kit.BasicServicesKit';
```

## systemLoad.on('systemLoadChange')

PhonePC/2in1TabletTVWearable

on(type: 'systemLoadChange', callback: Callback<SystemLoadLevel>): void

注册系统负载回调，感知系统负载融合档位变化，使用callback异步回调。

**系统能力:** SystemCapability.ResourceSchedule.SystemLoad

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定取值'systemLoadChange'，系统负载变化类型。 |
| callback | Callback<[SystemLoadLevel](js-apis-resourceschedule-systemload.md#systemloadlevel)> | 是 | 回调函数，返回本次注册系统负载时的系统负载融合档位。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Callback parameter error; 2. Register a exist callback type; 3. Parameter verification failed. |

**示例**：

```
1. import { systemLoad } from '@kit.BasicServicesKit';

3. function onSystemLoadChange(res: systemLoad.SystemLoadLevel) {
4. console.info(`system load changed, current level ` + res);
5. }

7. try {
8. systemLoad.on('systemLoadChange', onSystemLoadChange);
9. console.info(`register systemload callback succeeded. `);
10. } catch (err) {
11. console.error(`register systemload callback failed: ` + JSON.stringify(err));
12. }
```

## systemLoad.off('systemLoadChange')

PhonePC/2in1TabletTVWearable

off(type: 'systemLoadChange', callback?: Callback<SystemLoadLevel>): void

取消注册系统负载回调，使用callback异步回调。

**系统能力:** SystemCapability.ResourceSchedule.SystemLoad

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定取值'systemLoadChange'，系统负载变化类型。 |
| callback | Callback<[SystemLoadLevel](js-apis-resourceschedule-systemload.md#systemloadlevel)> | 否 | 回调函数，返回本次取消注册系统负载时的系统负载融合档位。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Callback parameter error; 2. Unregister type has not register; 3. Parameter verification failed. |

**示例**：

```
1. import { systemLoad } from '@kit.BasicServicesKit';

3. function onSystemLoadChange(res: systemLoad.SystemLoadLevel) {
4. console.info(`system load changed, current level ` + res);
5. }

7. try {
8. systemLoad.off('systemLoadChange', onSystemLoadChange);
9. console.info(`unregister systemload callback succeeded:. `);
10. } catch (err) {
11. console.error(`unregister systemload callback failed: ` + JSON.stringify(err));
12. }
```

## systemLoad.getLevel

PhonePC/2in1TabletTVWearable

getLevel(): Promise<[SystemLoadLevel](js-apis-resourceschedule-systemload.md#systemloadlevel)>

获取系统负载融合档位，使用promise异步回调。

**系统能力:** SystemCapability.ResourceSchedule.SystemLoad

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[SystemLoadLevel](js-apis-resourceschedule-systemload.md#systemloadlevel)> | Promise对象，返回系统负载融合档位。 |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { systemLoad } from '@kit.BasicServicesKit';

4. systemLoad.getLevel().then((res: systemLoad.SystemLoadLevel) => {
5. console.info(`getLevel promise succeeded. result: ` + JSON.stringify(res));
6. }).catch((err: BusinessError) => {
7. console.error(`getLevel promise failed. code is ${err.code} message is ${err.message}`);
8. })
```

## SystemLoadLevel

PhonePC/2in1TabletTVWearable

系统负载融合档位。

**系统能力:** SystemCapability.ResourceSchedule.SystemLoad

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOW | 0 | 设备当前温度、负载比较低，无高负载场景。 |
| NORMAL | 1 | 设备温度、负载正常，但邻近中等状态，无感知业务应降低规格和负载。 |
| MEDIUM | 2 | 设备温度、负载有一项或多项稍高，或者当前处于高负载场景，无感知业务应暂停或延迟运行。 |
| HIGH | 3 | 设备当前发热明显或负载比较高，或处于负载温度中等但处于高负载场景，无感知业务应停止，非关键业务应降低规格及负载。 |
| OVERHEATED | 4 | 设备发热严重或者负载较重，无感知业务与非关键业务应停止，前台关键业务应降低规格及负载。 |
| WARNING | 5 | 设备过热或负载过重，或者温度较高但处于高负载场景，即将进入紧急状态，整机资源供给大幅降低，停止所有非关键，前台关键业务应降低至最低规格。 |
| EMERGENCY | 6 | 设备已经进入过热状态或负载极高紧急状态，或接近紧急状态但处于高负载场景，整机资源供给降至最低，设备功能受限，仅保留基础功能可用。 |
| ESCAPE | 7 | 设备即将进入热逃生状态或当前负载已经不堪重负，或已经处于紧急状态且高负载状态，所有业务将被强制停止，业务需做好逃生措施，例如保存重要数据等。 |
