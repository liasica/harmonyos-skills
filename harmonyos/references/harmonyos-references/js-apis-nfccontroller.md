---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nfccontroller
title: @ohos.nfc.controller (标准NFC)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.nfc.controller (标准NFC)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1489037de87c0515f16c22e6535558a42ddc6f1cdb0789f1e4cd888dec7097b7
---

本模块主要用于管理NFC状态，包括打开和关闭NFC，读取NFC的状态等。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## **导入模块**

PhonePC/2in1TabletWearable

```
1. import { nfcController } from '@kit.ConnectivityKit';
```

## NfcState

PhonePC/2in1TabletWearable

定义不同的NFC状态值。

**系统能力：** SystemCapability.Communication.NFC.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_OFF | 1 | NFC已关闭状态。 |
| STATE\_TURNING\_ON | 2 | NFC正在打开状态。 |
| STATE\_ON | 3 | NFC已打开状态。 |
| STATE\_TURNING\_OFF | 4 | NFC正在关闭状态。 |

## nfcController.isNfcAvailable(deprecated)

PhonePC/2in1TabletWearable

isNfcAvailable(): boolean

查询设备是否有NFC能力。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[canIUse("SystemCapability.Communication.NFC.Core")](init.md#caniuse)替代。

**系统能力：** SystemCapability.Communication.NFC.Core

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true: 设备具备NFC能力， false: 设备不具备NFC能力。 |

## nfcController.openNfc(deprecated)

PhonePC/2in1TabletWearable

openNfc(): boolean

打开NFC开关。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[enableNfc](js-apis-nfccontroller.md#nfccontrollerenablenfc9)替代。

**需要权限：** ohos.permission.MANAGE\_SECURE\_SETTINGS（该权限仅系统应用可申请）

**系统能力：** SystemCapability.Communication.NFC.Core

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true: 打开NFC成功， false: 打开NFC失败。 |

## nfcController.enableNfc9+

PhonePC/2in1TabletWearable

enableNfc(): void

打开NFC开关，该接口只能被系统应用调用。

**需要权限：** ohos.permission.MANAGE\_SECURE\_SETTINGS（该权限仅系统应用可申请）

**系统能力：** SystemCapability.Communication.NFC.Core

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3100101 | The NFC state is abnormal in the service. |

## nfcController.closeNfc(deprecated)

PhonePC/2in1TabletWearable

closeNfc(): boolean

关闭NFC开关。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[disableNfc](js-apis-nfccontroller.md#nfccontrollerdisablenfc9)替代。

**需要权限：** ohos.permission.MANAGE\_SECURE\_SETTINGS（该权限仅系统应用可申请）

**系统能力：** SystemCapability.Communication.NFC.Core

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true: 关闭NFC成功， false: 关闭NFC失败。 |

## nfcController.disableNfc9+

PhonePC/2in1TabletWearable

disableNfc(): void

关闭NFC开关，该接口只能被系统应用调用。

**需要权限：** ohos.permission.MANAGE\_SECURE\_SETTINGS（该权限仅系统应用可申请）

**系统能力：** SystemCapability.Communication.NFC.Core

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3100101 | The NFC state is abnormal in the service. |

## nfcController.isNfcOpen

PhonePC/2in1TabletWearable

isNfcOpen(): boolean

查询NFC是否打开。

**系统能力：** SystemCapability.Communication.NFC.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true: NFC是打开的， false: NFC是关闭的。 |

## nfcController.getNfcState

PhonePC/2in1TabletWearable

getNfcState(): [NfcState](js-apis-nfccontroller.md#nfcstate)

查询NFC状态。

**系统能力：** SystemCapability.Communication.NFC.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NfcState](js-apis-nfccontroller.md#nfcstate) | NFC状态值，详细请见[NfcState](js-apis-nfccontroller.md#nfcstate)枚举值。 |

## nfcController.on('nfcStateChange')

PhonePC/2in1TabletWearable

on(type: 'nfcStateChange', callback: Callback<[NfcState](js-apis-nfccontroller.md#nfcstate)>): void

注册NFC开关状态事件，获取NFC状态的变化通知。使用callback异步回调。

**系统能力：** SystemCapability.Communication.NFC.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"nfcStateChange"字符串。 |
| callback | Callback<[NfcState](js-apis-nfccontroller.md#nfcstate)> | 是 | 回调函数，返回NFC状态的枚举值。 |

## nfcController.off('nfcStateChange')

PhonePC/2in1TabletWearable

off(type: 'nfcStateChange', callback?: Callback<[NfcState](js-apis-nfccontroller.md#nfcstate)>): void

取消NFC开关状态事件的注册，取消后NFC状态变化时，就不会再收到Callback的通知。使用callback异步回调。

**系统能力：** SystemCapability.Communication.NFC.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"nfcStateChange"字符串。 |
| callback | Callback<[NfcState](js-apis-nfccontroller.md#nfcstate)> | 否 | NFC状态改变回调函数，可以空缺不填。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例**

```
1. import { nfcController } from '@kit.ConnectivityKit';

3. // 注册回调以接收nfc状态更改通知
4. nfcController.on("nfcStateChange", (nfcState : number)=> {
5. console.info("nfcController on callback nfcState: " + nfcState);
6. });

8. // 打开nfc需要权限: ohos.permission.MANAGE_SECURE_SETTINGS（此权限仅系统应用可申请）
9. if (!nfcController.isNfcOpen()) {
10. // 从api9开始,使用'enableNfc'打开nfc
11. try {
12. nfcController.enableNfc();
13. console.info("nfcController enableNfc success");
14. } catch (businessError) {
15. console.error("nfcController enableNfc businessError: " + businessError);
16. }
17. } else {
18. console.info("nfcController NFC has been opened");
19. }

21. // 关闭nfc需要权限: ohos.permission.MANAGE_SECURE_SETTINGS（此权限仅系统应用可申请）
22. if (nfcController.isNfcOpen()) {
23. // 从api9开始,使用'disableNfc'关闭nfc
24. try {
25. nfcController.disableNfc();
26. console.info("nfcController disableNfc success");
27. } catch (businessError) {
28. console.error("nfcController disableNfc businessError: " + businessError);
29. }
30. } else {
31. console.info("nfcController NFC has been closed");
32. }

34. // 取消注册回调
35. nfcController.off("nfcStateChange");
```
