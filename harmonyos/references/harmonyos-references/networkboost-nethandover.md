---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/networkboost-nethandover
title: netHandover（连接迁移）
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > ArkTS API > netHandover（连接迁移）
category: harmonyos-references
scraped_at: 2026-04-28T08:08:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5bdb1315f41c611cefb208c24c63e73249029b94ed85be515c4f5c8b53ee53f8
---

本模块提供网络连接迁移能力，以便在弱网环境下，系统发起多网迁移（WiFi<->蜂窝，主卡<->副卡等）的过程中，给应用提供连接迁移开始和完成通知，应用根据连接迁移通知的建议进行重建，快速恢复业务，给用户带来平滑、高速、低时延的上网体验。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { netHandover } from '@kit.NetworkBoostKit';
```

## netHandover.on( 'handoverChange')

PhonePC/2in1Tablet

on(type: 'handoverChange', callback: Callback<HandoverInfo>): void

订阅连接迁移信息。

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**系统能力:** SystemCapability.Communication.NetworkBoost.Core

**起始版本:** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"handoverChange"字符串，表示连接迁移变化事件。 |
| callback | Callback<[HandoverInfo](networkboost-nethandover.md#handoverinfo)> | 是 | 回调函数，返回连接迁移开始和完成的详细信息。 |

**错误码：**

涉及错误码均为通用错误码，[通用错误码详细描述查看](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { netHandover } from '@kit.NetworkBoostKit';
3. try {
4. netHandover.on('handoverChange', (info: netHandover.HandoverInfo) => {
5. if (info.handoverStart) {
6. // 连接迁移开始回调，应用按照HandoverStart的建议调整数传策略
7. console.info('handover start');
8. } else if (info.handoverComplete) {
9. // 连接迁移完成回调，应用按照HandoverComplete的建议进行调速和重建恢复
10. console.info('handover complete');
11. }
12. });
13. } catch (err) {
14. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
15. }
```

## netHandover.off( 'handoverChange')

PhonePC/2in1Tablet

off(type: 'handoverChange', callback?: Callback<HandoverInfo>): void

取消订阅连接迁移信息。

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"handoverChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[HandoverInfo](networkboost-nethandover.md#handoverinfo)> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

涉及错误码均为通用错误码，[通用错误码详细描述查看](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { netHandover } from '@kit.NetworkBoostKit';
3. try {
4. netHandover.off('handoverChange');
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

## netHandover.setHandoverMode

PhonePC/2in1Tablet

setHandoverMode(mode: HandoverMode): void

应用可通过该接口变更连接迁移模式，包括委托模式由系统发起连接迁移，和自主模式由应用发起连接迁移，默认为委托模式。设置失败，接口会抛出异常。

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [HandoverMode](networkboost-nethandover.md#handovermode) | 是 | 表示应用需要通知系统侧的迁移模式。 |

**错误码：**

涉及错误码均为通用错误码，[通用错误码详细描述查看](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { netHandover } from '@kit.NetworkBoostKit';
3. try {
4. // 设置为自主模式，由应用发起连接迁移
5. let mode: netHandover.HandoverMode = netHandover.HandoverMode.DISCRETION;
6. netHandover.setHandoverMode(mode);
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## netHandover.getMultiPathQuotaStats

PhonePC/2in1Tablet

getMultiPathQuotaStats(): MultiPathQuota

获取当前应用多网使用的配额，包括已使用的配额信息和剩余配额信息。

**需要权限：** ohos.permission.LINKTURBO

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MultiPathQuota](networkboost-nethandover.md#multipathquota) | 应用配额信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](networkboost-arkts-errorcode.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1013600001 | Internal error. For example, the internal management state machine is abnormal, or the internal message queue processing is blocked. |
| 1013600002 | System service error. For example, IPC call processes fails, or the network management service failed to start. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { netHandover } from '@kit.NetworkBoostKit';
3. try {
4. let multiquota : netHandover.MultiPathQuota = netHandover.getMultiPathQuotaStats();
5. console.info('getMultiPathQuotaStats multiPathQuota.used.count is:' + multiquota.used.count)
6. console.info('getMultiPathQuotaStats multiPathQuota.used.duration is:' + multiquota.used.duration)
7. console.info('getMultiPathQuotaStats multiPathQuota.remaining.count is:' + multiquota.remaining.count)
8. console.info('getMultiPathQuotaStats multiPathQuota.remaining.durationis:' + multiquota.remaining.duration)
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

## netHandover.requestMultiPath

PhonePC/2in1Tablet

requestMultiPath(callback: Callback<MultiPathRequestResult>): void

发起多网请求。

**需要权限：** ohos.permission.LINKTURBO

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[MultiPathRequestResult](networkboost-nethandover.md#multipathrequestresult)> | 是 | 回调函数，返回发起多网的结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](networkboost-arkts-errorcode.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1013600001 | Internal error. For example, the internal management state machine is abnormal, or the internal message queue processing is blocked. |
| 1013600002 | System service error. For example, IPC call processes fails, or the network management service failed to start. |
| 1013620000 | Multi-path capability is disabled. |
| 1013620001 | Multi-path links are already active or in the process of being established. |
| 1013620002 | App request limit reached. |
| 1013620003 | Request denied due to power consumption restrictions. |
| 1013620004 | No quota. |
| 1013620005 | Conflict. |
| 1013620006 | Requests are too frequent. |
| 1013620007 | No suitable path. |
| 1013620008 | Insufficient traffic. |
| 1013620009 | Concurrency is not allowed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { netHandover } from '@kit.NetworkBoostKit';
3. try {
4. netHandover.requestMultiPath((data: netHandover.MultiPathRequestResult) => {
5. console.info(` requestMultiPath result:` + JSON.stringify(data));
6. });
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## netHandover.releaseMultiPath

PhonePC/2in1Tablet

releaseMultiPath(): void

释放多网请求。

**需要权限：** ohos.permission.LINKTURBO

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](networkboost-arkts-errorcode.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1013600001 | Internal error. For example, the internal management state machine is abnormal, or the internal message queue processing is blocked. |
| 1013600002 | System service error. For example, IPC call processes fails, or the network management service failed to start. |
| 1013620100 | Release request mismatch. |
| 1013620101 | Multi-path not activated. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { netHandover } from '@kit.NetworkBoostKit';
3. try {
4. netHandover.releaseMultiPath();
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

## netHandover.on('multiPathStateChange')

PhonePC/2in1Tablet

on(type: 'multiPathStateChange', callback: Callback<MultiPathStateInfo>): void

订阅多网状态变化事件。

**需要权限：** ohos.permission.LINKTURBO

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"multiPathStateChange"字符串，表示多网状态变化事件。 |
| callback | Callback<[MultiPathStateInfo](networkboost-nethandover.md#multipathstateinfo)> | 是 | 回调函数，返回多网状态变化信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](networkboost-arkts-errorcode.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1013600001 | Internal error. For example, the internal management state machine is abnormal, or the internal message queue processing is blocked. |
| 1013600002 | System service error. For example, IPC call processes fails, or the network management service failed to start. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { netHandover } from '@kit.NetworkBoostKit';
3. try {
4. netHandover.on('multiPathStateChange', (data: netHandover.MultiPathStateInfo) => {
5. // 回调信息处理
6. console.info("on multiPathStateChange: " + JSON.stringify(data));
7. });
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## netHandover.off('multiPathStateChange')

PhonePC/2in1Tablet

off(type: 'multiPathStateChange', callback?: Callback<MultiPathStateInfo>): void

取消订阅多网状态变化事件。

**需要权限：** ohos.permission.LINKTURBO

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"multiPathStateChange"字符串，表示多网状态变化事件。 |
| callback | Callback<[MultiPathStateInfo](networkboost-nethandover.md#multipathstateinfo)> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](networkboost-arkts-errorcode.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1013600001 | Internal error. For example, the internal management state machine is abnormal, or the internal message queue processing is blocked. |
| 1013600002 | System service error. For example, IPC call processes fails, or the network management service failed to start. |

**示例**：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { netHandover } from '@kit.NetworkBoostKit';
3. try {
4. netHandover.off('multiPathStateChange');
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

## netHandover.on('multiPathRecommendation')

PhonePC/2in1Tablet

on(type: 'multiPathRecommendation', callback: Callback<MultiPathRecommendationInfo>): void

订阅系统多网建议变化事件。

**需要权限：** ohos.permission.LINKTURBO

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"multiPathRecommendation"字符串，表示系统多网建议变化事件。 |
| callback | Callback<[MultiPathRecommendationInfo](networkboost-nethandover.md#multipathrecommendationinfo)> | 是 | 回调函数，返回多网建议变化信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](networkboost-arkts-errorcode.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1013600001 | Internal error. For example, the internal management state machine is abnormal, or the internal message queue processing is blocked. |
| 1013600002 | System service error. For example, IPC call processes fails, or the network management service failed to start. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { netHandover } from '@kit.NetworkBoostKit';
3. try {
4. netHandover.on('multiPathRecommendation', (data: netHandover.MultiPathRecommendationInfo) => {
5. // 回调信息处理
6. console.info("on multiPathRecommendation: " + JSON.stringify(data));
7. });
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## netHandover.off('multiPathRecommendation')

PhonePC/2in1Tablet

off(type: 'multiPathRecommendation', callback?: Callback<MultiPathRecommendationInfo>): void

取消订阅系统多网建议变化事件。

**需要权限：** ohos.permission.LINKTURBO

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"multiPathRecommendation"字符串，表示系统多网建议变化事件。 |
| callback | Callback<[MultiPathRecommendationInfo](networkboost-nethandover.md#multipathrecommendationinfo)> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](networkboost-arkts-errorcode.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1013600001 | Internal error. For example, the internal management state machine is abnormal, or the internal message queue processing is blocked. |
| 1013600002 | System service error. For example, IPC call processes fails, or the network management service failed to start. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { netHandover } from '@kit.NetworkBoostKit';
3. try {
4. netHandover.off('multiPathRecommendation');
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

## HandoverInfo

PhonePC/2in1Tablet

连接迁移回调信息。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| handoverStart | [HandoverStart](networkboost-nethandover.md#handoverstart) | 是 | 是 | 表示连接迁移开始信息。 |
| handoverComplete | [HandoverComplete](networkboost-nethandover.md#handovercomplete) | 是 | 是 | 表示连接迁移完成信息。 |

## HandoverStart

PhonePC/2in1Tablet

连接迁移开始信息。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| expires | number | 否 | 否 | 连接迁移全流程的超时时间，单位为秒，取值为任意正整数或者0。 |
| dataSpeedAction | [DataSpeedAction](networkboost-nethandover.md#dataspeedaction) | 否 | 否 | 老链路的发包建议。 |

## HandoverComplete

PhonePC/2in1Tablet

连接迁移完成信息。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | [ErrorResult](networkboost-nethandover.md#errorresult) | 否 | 否 | 连接迁移结果。 |
| handoverContinue | boolean | 否 | 否 | 是否还有HandoverComplete消息。  true表示还有新链路待激活，系统还会上报HandoverComplete消息，一般发生在连接迁移到多个网络的场景。  false表示当前已经是最后一个HandoverComplete消息，连接迁移流程完成。 |
| oldPathLifetime | number | 否 | 否 | 老链路的剩余生存时长，单位为秒，取值为任意正整数或0。 |
| oldDataSpeedAction | [DataSpeedAction](networkboost-nethandover.md#dataspeedaction) | 否 | 否 | 老链路发包建议。 |
| pathTypeChanged | boolean | 否 | 否 | 新老链路类型是否发生变更。true表示发生变化，如WiFi<->蜂窝。false表示没有发生变化。 |
| newNetHandle | [connection.NetHandle](js-apis-net-connection.md#nethandle) | 否 | 是 | 新链路的NetHandle信息。 |
| reEstAction | [ReEstAction](networkboost-nethandover.md#reestaction) | 否 | 否 | 链路重建类型。 |
| newDataSpeedAction | [DataSpeedAction](networkboost-nethandover.md#dataspeedaction) | 否 | 否 | 新链路发包建议。 |

## DataSpeedAction

PhonePC/2in1Tablet

发包速率建议。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dataSpeedSimpleAction | [netQuality.DataSpeedSimpleAction](networkboost-netquality.md#dataspeedsimpleaction) | 否 | 否 | 应用发包策略的简单建议。 |
| linkUpBandwidth | [netQuality.RateBps](networkboost-netquality.md#ratebps) | 否 | 否 | 老链路上行带宽。 |
| linkDownBandwidth | [netQuality.RateBps](networkboost-netquality.md#ratebps) | 否 | 否 | 老链路下行带宽。 |

## MultiPathStateInfo

PhonePC/2in1Tablet

多网状态信息。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| multiPathState | [MultiPathState](networkboost-nethandover.md#multipathstate) | 否 | 否 | 多网状态。 |
| cause | [MultiPathChangeCause](networkboost-nethandover.md#multipathchangecause) | 否 | 否 | 多网状态变化原因。 |
| netHandle | [connection.NetHandle](js-apis-net-connection.md#nethandle) | 否 | 否 | 多网链路的netHandle。 |
| pathState | [PathState](networkboost-nethandover.md#pathstate) | 否 | 否 | 多网链路状态。 |
| pathType | [netQuality.PathType](networkboost-netquality.md#pathtype) | 否 | 否 | 多网链路类型。 |

## MultiPathRecommendationInfo

PhonePC/2in1Tablet

多网推荐信息。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| action | [MultiPathAction](networkboost-nethandover.md#multipathaction) | 否 | 否 | 多网推荐动作。 |

## MultiPathQuota

PhonePC/2in1Tablet

应用配额使用信息。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| used | [MultiPathQuotaInfo](networkboost-nethandover.md#multipathquotainfo) | 是 | 否 | 应用已使用配额信息。 |
| remaining | [MultiPathQuotaInfo](networkboost-nethandover.md#multipathquotainfo) | 是 | 否 | 应用剩余使用配额信息。 |

## MultiPathQuotaInfo

PhonePC/2in1Tablet

配额信息。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| count | number | 否 | 否 | 配额次数信息。 |
| duration | number | 否 | 否 | 配额时长信息，单位为秒。 |

## MultiPathRequestResult

PhonePC/2in1Tablet

多网请求结果。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | [MultiPathErrorResult](networkboost-nethandover.md#multipatherrorresult) | 否 | 否 | 多网请求结果。 |

## MultiPathAction

PhonePC/2in1Tablet

多网推荐动作的枚举。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MULTIPATH\_ACTION\_REQUEST | 0 | 建议发起多网请求。 |
| MULTIPATH\_ACTION\_RELEASE | 1 | 建议释放多网请求。 |

## MultiPathErrorResult

PhonePC/2in1Tablet

多网建立结果的枚举。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MULTIPATH\_ERROR\_NONE | 0 | 多网建立成功。 |
| MULTIPATH\_ERROR\_NETWORK\_REFUSED | 1 | 多网请求被网络拒绝。 |
| MULTIPATH\_ERROR\_TIMEOUT | 2 | 多网建立超时。 |
| MULTIPATH\_ERROR\_LOCAL | 3 | 多网建立过程中，本地释放，例如在建立过程中数据开关关闭，或者其他事件发生，已经不满足拉起多网的条件。 |

## MultiPathState

PhonePC/2in1Tablet

多网状态。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MULTIPATH\_IDLE | 0 | 多网处于空闲状态。 |
| MULTIPATH\_CREATING | 1 | 多网正在建立中。 |
| MULTIPATH\_CREATED | 2 | 多网已建立。 |
| MULTIPATH\_RELEASING | 3 | 多网正在释放中。 |

## PathState

PhonePC/2in1Tablet

多网链路状态。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PATH\_IDLE | 0 | 多网链路处于空闲状态。 |
| PATH\_CONNECTED | 1 | 多网链路已连接。 |
| PATH\_SUSPENDED | 2 | 多网链路处于挂起状态。 |

## MultiPathChangeCause

PhonePC/2in1Tablet

多网变化原因的枚举。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MULTIPATH\_CHANGE\_CAUSE\_REQUEST\_NORMAL | 0 | 正常发起多网请求。 |
| MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NORMAL | 50 | 正常释放多网请求。 |
| MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NETWORK | 51 | 网络原因释放多网。 |
| MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_USER\_REFUSED | 52 | 用户操作开关释放多网。 |
| MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NO\_QUOTA | 53 | 配额耗尽释放多网。 |
| MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_POWER\_CONSUMPTION | 54 | 功耗原因释放多网。 |
| MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_INSUFFICIENT\_TRAFFIC | 55 | 流量原因释放多网。 |
| MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_CONFLICT | 56 | 场景冲突释放多网。 |
| MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_FUSING | 57 | 应用使用不规范，比如长时间拉起多网不释放，系统释放多网。 |
| MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_DEFAULT | 99 | 系统网络状态变化释放多网。 |
| MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_ENTER | 100 | 多网进入挂起状态，此时多网虽未释放，但是实际链路无法传输数据。 |
| MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_LEAVE | 101 | 多网退出挂起状态。 |
| MULTIPATH\_CHANGE\_CAUSE\_CONN\_PROPERTIES\_UPDATE | 102 | 多网链路的链接属性信息更新，比如IP地址更新。 |

## HandoverMode

PhonePC/2in1Tablet

表示连接迁移模式枚举。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DELEGATION | 0 | 委托模式，表示由系统发起连接迁移。应用未调用setHandoverMode接口则默认为该模式。 |
| DISCRETION | 1 | 自主模式，表示由应用发起连接迁移。应用可以通过该接口禁止系统发起连接迁移。在某些场景下，比如该应用切换到后台时，依旧有可能由系统触发切换。 |

## ReEstAction

PhonePC/2in1Tablet

表示重建枚举。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 表示应用需要使用同样的远端IP，进行重建链路。 |
| QUERY\_DNS | 1 | 表示数据链路类型发生变化，比如WiFi <-> CELL，或者是数据链路所在的运营商信息等变化。 |
| CHANGE\_REMOTE\_IP | 2 | 表示应用需要使用不同的远端IP进行重建。 |
| CHANGE\_IP\_VERSION | 3 | 表示应用需要修改IP类型进行重建，比如IPV4 <-> IPV6。 |
| NO\_EST | 4 | 表示应用应该在老链路进行立即重试，再次发起网络资源请求和交互，无需重建链路。 |

## ErrorResult

PhonePC/2in1Tablet

表示连接迁移结果枚举。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ERROR\_NONE | 0 | 表示连接迁移成功。 |
| ERROR\_HANDOVER\_TIMEOUT | 1 | 表示连接迁移超时。 |
| ERROR\_NEW\_PATH\_ACTIVATION\_FAILED | 2 | 表示连接迁移时新链路激活失败。 |
| ERROR\_ABORT | 3 | 表示连接迁移被取消。 |
