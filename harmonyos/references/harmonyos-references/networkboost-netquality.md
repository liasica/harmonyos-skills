---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/networkboost-netquality
title: netQuality（网络质量）
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > ArkTS API > netQuality（网络质量）
category: harmonyos-references
scraped_at: 2026-04-28T08:08:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b7d930dec0a075f1206cc69a107e5272866aa504cce256e376b4108ea0e892d5
---

本模块提供网络质量实时评估、网络场景识别以及弱信号预测等能力，以便应用针对弱网等环境下实现网络自适应，包括缓存、码率、帧率、分辨率等策略的调整。应用也可以通过网络质量中的应用传输体验反馈接口，触发系统进行网络加速。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { netQuality } from '@kit.NetworkBoostKit';
```

## netQuality.on( 'netQosChange')

PhonePC/2in1Tablet

on(type: 'netQosChange', callback: Callback<Array<NetworkQos>>): void

订阅网络质量信息。

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**系统能力:** SystemCapability.Communication.NetworkBoost.Core

**起始版本:** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"netQosChange"字符串，表示网络质量变化事件。 |
| callback | Callback<Array<[NetworkQos](networkboost-netquality.md#networkqos)>> | 是 | 回调函数，返回网络Qos变化的详细信息。 |

**错误码**：

涉及错误码均为通用错误码，[通用错误码详细描述查看](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { netQuality } from '@kit.NetworkBoostKit';
3. try {
4. netQuality.on('netQosChange', (list: Array<netQuality.NetworkQos>) => {
5. if (list.length > 0) {
6. list.forEach((qos) => {
7. // 回调信息处理
8. console.info(`Succeeded receive netQosChange info`);
9. });
10. }
11. });
12. } catch (err) {
13. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
14. }
```

## netQuality.off( 'netQosChange')

PhonePC/2in1Tablet

off(type: 'netQosChange', callback?: Callback<Array<NetworkQos>>): void

取消订阅网络质量信息。

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"netQosChange"字符串，表示连接状态变化事件。 |
| callback | Callback<Array<[NetworkQos](networkboost-netquality.md#networkqos)>> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

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
2. import { netQuality } from '@kit.NetworkBoostKit';
3. try {
4. netQuality.off('netQosChange');
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

## netQuality.on( 'netSceneChange')

PhonePC/2in1Tablet

on(type: 'netSceneChange', callback: Callback<Array<NetworkScene>>): void

订阅网络场景信息。

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**系统能力:** SystemCapability.Communication.NetworkBoost.Core

**起始版本:** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"netSceneChange"字符串，表示网络场景变化事件。 |
| callback | Callback<Array<[NetworkScene](networkboost-netquality.md#networkscene)>> | 是 | 回调函数，返回网络场景变化的详细信息。 |

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
2. import { netQuality } from '@kit.NetworkBoostKit';
3. try {
4. netQuality.on('netSceneChange', (list: Array<netQuality.NetworkScene>) => {
5. if (list.length > 0) {
6. list.forEach((scene) => {
7. // 回调信息处理
8. console.info(`Succeeded receive netSceneChange info`);
9. if (scene.weakSignalPrediction) {
10. // 弱信号预测处理
11. }
12. });
13. }
14. });
15. } catch (err) {
16. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
17. }
```

## netQuality.off( 'netSceneChange')

PhonePC/2in1Tablet

off(type: 'netSceneChange', callback?: Callback<Array<NetworkScene>>): void

取消订阅网络场景信息。

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"netSceneChange"字符串，表示网络场景变化事件。 |
| callback | Callback<Array<[NetworkScene](networkboost-netquality.md#networkscene)>> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

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
2. import { netQuality } from '@kit.NetworkBoostKit';
3. try {
4. netQuality.off('netSceneChange');
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

## netQuality.reportQoe

PhonePC/2in1Tablet

reportQoe(appQoe: AppQoe): void

应用传输体验反馈，上报失败，接口会抛出异常。

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appQoe | [AppQoe](networkboost-netquality.md#appqoe) | 是 | 表示应用需要反馈的传输体验信息。 |

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
2. import { netQuality } from '@kit.NetworkBoostKit';
3. try {
4. let serviceType: netQuality.ServiceType = 'shortVideo';
5. let qoeType: netQuality.BadQoeCause = 'serverErr';
6. let appQoe: netQuality.AppQoe = {
7. serviceType,
8. qoeType
9. };
10. netQuality.reportQoe(appQoe);
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```

## AppQoe

PhonePC/2in1Tablet

应用传输体验信息。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceType | [ServiceType](networkboost-netquality.md#servicetype) | 否 | 否 | 应用的业务类型。 |
| qoeType | [QoeType](networkboost-netquality.md#qoetype) | 否 | 否 | 应用体验类型。 |

## NetworkQos

PhonePC/2in1Tablet

网络质量回调信息。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pathType | [PathType](networkboost-netquality.md#pathtype) | 否 | 否 | 表明相应的数据路径上的网络质量信息。 |
| linkUpBandwidth | [RateBps](networkboost-netquality.md#ratebps) | 否 | 否 | 上行带宽信息，单位为bps。 |
| linkDownBandwidth | [RateBps](networkboost-netquality.md#ratebps) | 否 | 否 | 下行带宽信息，单位为bps。 |
| linkUpRate | [RateBps](networkboost-netquality.md#ratebps) | 否 | 否 | 上行速率，单位为bps。 |
| linkDownRate | [RateBps](networkboost-netquality.md#ratebps) | 否 | 否 | 下行速率，单位为bps。 |
| rttMs | number | 否 | 否 | RTT时延，表示统计时间间隔内，pathType对应数据路径上，所有的TCP上下行数据包的平均往返时延。取值范围为0或任意正数，单位：毫秒（ms）。  如果在统计时间间隔内没有收到某次TCP请求的回复，则该次的RTT时延不会被计入该统计时间间隔内。因此，在完全不可上网的场景下，由于无法收到TCP的回复，回调中的RTT时延值会比较小，与实际状态不一致。针对完全不可上网的场景，建议结合[on('netCapabilitiesChange')](js-apis-net-connection.md#onnetcapabilitieschange)方法进行综合判断。 |
| linkUpBufferDelayMs | number | 否 | 否 | 上行发送空口缓冲时延，取值范围是任意正数。 |
| linkUpBufferCongestionPercent | number | 否 | 是 | 上行发送空口缓冲时延占总缓冲时间的比例，取值范围[0, 100]。 |

## PathType

PhonePC/2in1Tablet

数据路径类型，枚举值。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CELLULAR\_PRIMARY | 0 | 蜂窝主卡。 |
| CELLULAR\_SECONDARY | 1 | 蜂窝副卡。 |
| WIFI\_PRIMARY | 2 | 主WiFi。 |
| WIFI\_SECONDARY | 3 | 辅WiFi。 |

## RateBps

PhonePC/2in1Tablet

type RateBps = number

带宽或速率的抽象表示。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| number | 表示值的类型为number，可取任意正数，单位为bps。 |

## ServiceType

PhonePC/2in1Tablet

type ServiceType = 'default' | 'background' | 'realtimeVoice' | 'realtimeVideo' | 'callSignaling' | 'realtimeGame' | 'normalGame' | 'shortVideo' | 'longVideo' | 'livestreamingAnchor' | 'livestreamingWatcher' | 'download' | 'upload' | 'browser' | 'transaction' | 'shopping' | 'detection' | 'cloudService' | 'voiceConference' | 'videoConference' | 'audio' | 'navigation' | 'seckillService' | 'login'

应用业务类型。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| 'default' | 表示默认服务类型，值固定为'default'字符串。 |
| 'background' | 表示后台类型，值固定为'background'字符串。 |
| 'realtimeVoice' | 表示实时语音类型，值固定为'realtimeVoice'字符串。 |
| 'realtimeVideo' | 表示实时视频类型，值固定为'realtimeVideo'字符串。 |
| 'callSignaling' | 表示语音信令类型，值固定为'callSignaling'字符串。 |
| 'realtimeGame' | 表示实时游戏类型，值固定为'realtimeGame'字符串。 |
| 'normalGame' | 表示普通游戏类型，值固定为'normalGame'字符串。 |
| 'shortVideo' | 表示短视频类型，值固定为'shortVideo'字符串。 |
| 'longVideo' | 表示长视频类型，值固定为'longVideo'字符串。 |
| 'livestreamingAnchor' | 表示直播主播类型，值固定为'livestreamingAnchor'字符串。 |
| 'livestreamingWatcher' | 表示直播观看类型，值固定为'livestreamingWatcher'字符串。 |
| 'download' | 表示下载类型，值固定为'download'字符串。 |
| 'upload' | 表示上传类型，值固定为'upload'字符串。 |
| 'browser' | 表示浏览页面类型，值固定为'browser'字符串。 |
| 'transaction' | 表示交易支付或者扫码类型，值固定为'transaction'字符串。该类型从API 20开始支持。 |
| 'shopping' | 表示购物类型，值固定为'shopping'字符串。该类型从API 20开始支持。 |
| 'detection' | 表示探测类型，值固定为'detection'字符串。该类型从API 20开始支持。 |
| 'cloudService' | 表示云业务、云游戏类型，值固定为'cloudService'字符串。该类型从API 20开始支持。 |
| 'voiceConference' | 表示语音会议类型，值固定为'voiceConference'字符串。该类型从API 20开始支持。 |
| 'videoConference' | 表示视频会议类型，值固定为'videoConference'字符串。该类型从API 20开始支持。 |
| 'audio' | 表示音乐、音频类型，值固定为'audio'字符串。该类型从API 20开始支持。 |
| 'navigation' | 表示导航定位类型，值固定为'navigation'字符串。该类型从API 20开始支持。 |
| 'seckillService' | 表示秒杀业务类型，如抢票、抢购、抢单、抢红包等，值固定为'seckillService'字符串。该类型从API 20开始支持。 |
| 'login' | 表示登录（含一键登录）类型，值固定为'login'字符串。该类型从API 20开始支持。 |

## QoeType

PhonePC/2in1Tablet

type QoeType = 'good' | BadQoeCause

应用体验类型。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| 'good' | 表示体验良好，值固定为'good'字符串。 |
| [BadQoeCause](networkboost-netquality.md#badqoecause) | 表示体验差类型。 |

## BadQoeCause

PhonePC/2in1Tablet

type BadQoeCause = 'unknown' | 'serverErr' | 'noData' | 'packetLost' | 'packetOutOfOrder' | 'highJitter' | 'highLatency'

应用体验差类型。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| 'unknown' | 表示未知原因，值固定为'unknown'字符串。 |
| 'serverErr' | 表示服务器异常，值固定为'serverErr'字符串。 |
| 'noData' | 表示无数据，值固定为'noData'字符串。 |
| 'packetLost' | 表示丢包，值固定为'packetLost'字符串。 |
| 'packetOutOfOrder' | 表示乱序，值固定为'packetOutOfOrder'字符串。 |
| 'highJitter' | 表示高抖动，值固定为'highJitter'字符串。 |
| 'highLatency' | 表示高时延，值固定为'highLatency'字符串。 |

## 速率带宽级别

PhonePC/2in1Tablet

定义了多个速率或带宽的常量值。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| BPS | number | 1 | 1bps |
| KBPS | number | 1000 | 1kbps |
| MBPS | number | 1000000 | 1Mbps |
| GBPS | number | 1000000000 | 1Gbps |
| TBPS | number | 1000000000000 | 1Tbps |

## NetworkScene

PhonePC/2in1Tablet

网络场景状态变更回调信息。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pathType | [PathType](networkboost-netquality.md#pathtype) | 否 | 否 | 表明相应的数据路径上的网络场景信息。 |
| scene | [Scene](networkboost-netquality.md#scene) | 否 | 否 | 场景状态。 |
| recommendedAction | [RecommendedAction](networkboost-netquality.md#recommendedaction) | 否 | 否 | 建议的数传策略。 |
| weakSignalPrediction | [WeakSignalPrediction](networkboost-netquality.md#weaksignalprediction) | 否 | 是 | 弱信号预测相关信息。 |

## WeakSignalPrediction

PhonePC/2in1Tablet

弱信号预测相关信息。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isLastPredictionValid | boolean | 否 | 否 | 最近一次的弱信号预测是否有效，true表示最近一次的弱信号预测依旧有效，false表示最近一次的弱信号预测失效，此时startTime和duration参数忽略。 |
| startTime | number | 否 | 否 | 预计多长时间进入弱信号（单位：秒），取值范围为0和任意正数。 |
| duration | number | 否 | 否 | 预计在弱信号区域停留时长（单位：秒），取任意正数。取值0，此次预测结果无效。 |

## Scene

PhonePC/2in1Tablet

type Scene = 'normal' | 'congestion' | 'frequentHandover' | 'weakSignal'

场景类型。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| 'normal' | 表示正常场景，值固定为'normal'字符串。 |
| 'congestion' | 表示拥塞场景，值固定为'congestion'字符串。 |
| 'frequentHandover' | 表示小区切换频繁场景，值固定为'frequentHandover'字符串。 |
| 'weakSignal' | 表示弱信号场景，值固定为'weakSignal'字符串。 |

## DataSpeedSimpleAction

PhonePC/2in1Tablet

type DataSpeedSimpleAction = 'suspendData' | 'decreaseData' | 'increaseData' | 'keepData'

应用发包策略的简单建议。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| 'suspendData' | 表示停止发包，值固定为'suspendData'字符串。 |
| 'decreaseData' | 表示降低发包速率，值固定为'decreaseData'字符串。 |
| 'increaseData' | 表示增加发包速率，值固定为'increaseData'字符串。 |
| 'keepData' | 表示保持当前发包速率，值固定为'keepData'字符串。 |

## RecommendedAction

PhonePC/2in1Tablet

type RecommendedAction = 'doCaching' | DataSpeedSimpleAction

应用数传策略建议。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| 'doCaching' | 表示做缓存动作，值固定为'doCaching'字符串。 |
| [DataSpeedSimpleAction](networkboost-netquality.md#dataspeedsimpleaction) | 应用发包策略的简单建议。 |
