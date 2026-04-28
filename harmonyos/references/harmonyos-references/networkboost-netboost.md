---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/networkboost-netboost
title: netBoost（网络加速）
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > ArkTS API > netBoost（网络加速）
category: harmonyos-references
scraped_at: 2026-04-28T08:08:49+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:85d2f6dbc1c56a81cb748e8cee728d2de56b92741cc6db32e89ccfb1ff96df9c
---

本模块提供应用场景描述接口，使系统能够结合应用上报的业务场景与实时网络状态，动态适配业务加速策略，从而为用户提供高速、低时延的网络体验。

**起始版本：** 6.0.0(20)

## 导入模块

PhonePC/2in1Tablet

```
1. import { netBoost } from '@kit.NetworkBoostKit';
```

## netBoost.setSceneDesc

PhonePC/2in1Tablet

setSceneDesc(sceneDesc : SceneDesc): void

设置业务场景。

**需要权限：** ohos.permission.INTERNET

**系统能力:** SystemCapability.Communication.NetworkBoost.Core

**起始版本:** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sceneDesc | [SceneDesc](networkboost-netboost.md#scenedesc) | 是 | 要设置的业务场景信息。 |

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
2. import { netBoost } from '@kit.NetworkBoostKit';
3. try {
4. let sceneDesc : netBoost.SceneDesc = {
5. scene : 'realtimeVoice',
6. sceneEvent : netBoost.SceneEvent.SCENE_EVENT_ENTER
7. }
8. netBoost.setSceneDesc(sceneDesc);
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

## SceneDesc

PhonePC/2in1Tablet

业务场景描述信息。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scene | [netQuality.ServiceType](networkboost-netquality.md#servicetype) | 否 | 否 | 表示业务场景类型。 |
| sceneEvent | [SceneEvent](networkboost-netboost.md#sceneevent) | 否 | 否 | 表示业务场景事件。 |
| startTime | number | 否 | 是 | 表示要经过多长时间进入到sceneEvent事件，单位为s。  - 0表示立即发生sceneEvent事件，默认为0。  - 大于0表示预测未来多长时间进入sceneEvent事件。 |
| duration | number | 否 | 是 | 预计持续的时长，单位为s。0表示持续时长未知，以SceneEvent的离开事件表示终止。  例如应用即将在10s后进入秒杀场景，预计持续20s，scene可以传入'seckillService'类型，sceneEvent填写SCENE\_EVENT\_ENTER，startTime可填写10，duration填写20。开发者可以依据实际的场景类型进行选填。 |

## SceneEvent

PhonePC/2in1Tablet

表示业务事件枚举。

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCENE\_EVENT\_ENTER | 0 | 进入业务场景。 |
| SCENE\_EVENT\_UPDATE | 1 | 更新上一次的业务事件信息。 |
| SCENE\_EVENT\_LEAVE | 2 | 离开业务场景。 |
