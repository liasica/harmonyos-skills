---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fusionconnectivity-partneragent
title: @ohos.FusionConnectivity.partnerAgent（设备状态通知模块）
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.FusionConnectivity.partnerAgent（设备状态通知模块）
category: harmonyos-references
scraped_at: 2026-04-28T08:08:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:af854e1b1075d7b676c29a82eee105b52c9e1fa54d6798fdb4ec41c0dabe35b7
---

本模块基于蓝牙通信技术，为应用提供设备发现与设备下线的通知功能，主要功能特性包括：

* 动态监听并发现应用预先注册的蓝牙设备。
* 采用进程拉起机制，当目标设备出现时自动拉起应用的[PartnerAgentExtensionAbility](is-fusionconnectivity-partneragentextensionability.md)进程。
* 采用进程销毁机制，当所有设备下线时自动销毁应用的[PartnerAgentExtensionAbility](is-fusionconnectivity-partneragentextensionability.md)进程。
* 通过[PartnerAgentExtensionAbility](is-fusionconnectivity-partneragentextensionability.md)的接口通知应用发现已注册设备。

说明

* 本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1Tablet

```
1. import { partnerAgent } from '@kit.ConnectivityKit';
```

## partnerAgent.isPartnerAgentSupported

PhonePC/2in1Tablet

isPartnerAgentSupported(): boolean

判断本机设备是否支持外设互通功能，若该接口返回值是false，该文件内的其他接口均无法使用。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 是否支持外设互通功能。true表示支持外设互通功能，false表示不支持外设互通功能。 |

**示例**：

```
1. import { partnerAgent } from '@kit.ConnectivityKit';
2. let isSupport = partnerAgent.isPartnerAgentSupported();
3. console.info(`This device support partner agent: ${isSupport}`);
```

## partnerAgent.bindDevice

PhonePC/2in1Tablet

bindDevice(deviceAddress: PartnerDeviceAddress, deviceCapability: DeviceCapability, businessCapability: BusinessCapability, partnerAgentExtensionAbilityName: string): Promise<void>

应用注册设备，使用Promise异步回调。

* 建议先使用[isPartnerAgentSupported](js-apis-fusionconnectivity-partneragent.md#partneragentispartneragentsupported)判断本机是否支持外设互通功能。仅支持情况下才能使用融合短距外设互通模块功能。
* 可以通过接口[isDeviceBound](js-apis-fusionconnectivity-partneragent.md#partneragentisdevicebound)判断设备是否已注册。若已注册，无需重复调用。
* 应用需要先实现[PartnerAgentExtensionAbility](is-fusionconnectivity-partneragentextensionability.md)。
* 应用注册该设备后，如果外设互通子系统检测到该设备，会激活应用的[PartnerAgentExtensionAbility](is-fusionconnectivity-partneragentextensionability.md)进程。应用可以在新进程中执行业务操作。每当已注册设备被发现或者已断连时，该进程将被激活并保持运行3分钟（时间随着新的通知刷新）。
* 在应用注册前，需先与该设备完成[蓝牙配对](js-apis-bluetooth-connection.md#connectionpairdevice)。如果该设备已注册，且用户在此期间取消了与该设备的配对，该设备的发现和下线通知功能将自动关闭，但注册信息会保留30天。若在这30天内重新与该设备进行蓝牙配对，外设互通子系统可以恢复设备的发现和下线通知功能。否则，注册信息会被清除。
* 可以通过接口[getBoundDevices](js-apis-fusionconnectivity-partneragent.md#partneragentgetbounddevices)获取所有已注册过的设备。
* 应用在使用该接口前，建议提示用户并获取应用注册该设备的授权。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceAddress | [PartnerDeviceAddress](js-apis-fusionconnectivity-partneragent.md#partneragentpartnerdeviceaddress) | 是 | 应用注册的设备地址信息。  应用需配置PartnerDeviceAddress类型的bluetoothAddress选项。 |
| deviceCapability | [DeviceCapability](js-apis-fusionconnectivity-partneragent.md#partneragentdevicecapability) | 是 | 注册设备支持的能力。  - 配置[supportBR](js-apis-fusionconnectivity-partneragent.md#partneragentdevicecapability)选项后，外设互通子系统将监听与该设备的[ACL](../harmonyos-guides/terminology.md#acl)连接状态，一旦建立ACL连接，即视为成功发现该设备；  - 配置[supportBleAdvertiser](js-apis-fusionconnectivity-partneragent.md#partneragentdevicecapability)选项后，系统将启动该设备的[BLE](../harmonyos-guides/terminology.md#ble)扫描，扫描到该设备后，同样视为成功发现该设备。  注意：  为了减少系统功耗，若BLE扫描到该设备后，但应用在3分钟内未与该设备建立蓝牙连接，外设互通子系统将自动终止应用的PartnerAgentExtensionAbility进程。 |
| businessCapability | [BusinessCapability](js-apis-fusionconnectivity-partneragent.md#partneragentbusinesscapability) | 是 | 应用注册设备的业务功能，包括媒体控制、通话控制。 |
| partnerAgentExtensionAbilityName | string | 是 | 该参数需与应用模块级配置文件[module.json5](../harmonyos-guides/module-configuration-file.md) 中的[extensionabilities](../harmonyos-guides/module-configuration-file.md#extensionabilities标签) name属性值相同。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参考[通用错误码说明文档](errorcode-universal.md)和[融合短距服务子系统错误码](errorcode-fusionconnectivity.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 34900003 | The device is not paired. |
| 34900004 | The device has already been bound to the PartnerAgentExtensionAbility. |
| 34900005 | Bluetooth disabled. |
| 34900099 | Internal error. |

**示例**：

```
1. import { partnerAgent, common } from '@kit.ConnectivityKit';
2. try {
3. let btAddr: common.BluetoothAddress = {
4. "address": "11:22:33:44:55:66",
5. "addressType": common.BluetoothAddressType.REAL,
6. };
7. let deviceAddress: partnerAgent.PartnerDeviceAddress = {
8. "bluetoothAddress": btAddr,
9. };
10. let capability: partnerAgent.DeviceCapability = {
11. "supportBR": true,
12. "supportBleAdvertiser": true,
13. };
14. let businessCap: partnerAgent.BusinessCapability = {
15. "supportMediaControl": true,
16. "supportTelephonyControl": true,
17. };
18. partnerAgent.bindDevice(deviceAddress, capability, businessCap, "testAbilityName")
19. .then(() => {
20. console.info(`bind device success: ${btAddr.address}`);
21. })
22. .catch((err: BusinessError) => {
23. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
24. });
25. } catch (err) {
26. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
27. }
```

## partnerAgent.unbindDevice

PhonePC/2in1Tablet

unbindDevice(deviceAddress: PartnerDeviceAddress): Promise<void>

应用解注册设备，使用Promise异步回调。

* 调用本接口进行解注册后，应用的[PartnerAgentExtensionAbility](is-fusionconnectivity-partneragentextensionability.md)进程将不再接收此设备的发现和下线状态通知。
* 应用解注册的设备需是已通过[bindDevice](js-apis-fusionconnectivity-partneragent.md#partneragentbinddevice)接口注册过的设备，建议与bindDevice接口成对使用。
* 建议使用前通过接口[isDeviceBound](js-apis-fusionconnectivity-partneragent.md#partneragentisdevicebound)判断设备是否已注册。若已注册，可调用该接口。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceAddress | [PartnerDeviceAddress](js-apis-fusionconnectivity-partneragent.md#partneragentpartnerdeviceaddress) | 是 | 应用注册的设备地址信息。  应用必须配置PartnerDeviceAddress类型的bluetoothAddress选项。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参考[通用错误码说明文档](errorcode-universal.md)和[融合短距服务子系统错误码](errorcode-fusionconnectivity.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 34900001 | The device is not bound. |
| 34900099 | Internal error. |

**示例**：

```
1. import { partnerAgent, common } from '@kit.ConnectivityKit';
2. try {
3. let btAddr: common.BluetoothAddress = {
4. "address": "11:22:33:44:55:66",
5. "addressType": common.BluetoothAddressType.REAL,
6. };
7. let deviceAddress: partnerAgent.PartnerDeviceAddress = {
8. "bluetoothAddress": btAddr,
9. };
10. partnerAgent.unbindDevice(deviceAddress)
11. .then(() => {
12. console.info(`unbind device success: ${btAddr.address}`);
13. })
14. .catch((err: BusinessError) => {
15. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
16. });
17. } catch (err) {
18. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
19. }
```

## partnerAgent.isDeviceBound

PhonePC/2in1Tablet

isDeviceBound(deviceAddress: PartnerDeviceAddress): boolean

判断当前应用是否已注册过该设备。

* 通过调用[bindDevice](js-apis-fusionconnectivity-partneragent.md#partneragentbinddevice)接口进行注册。
* 通过调用[unbindDevice](js-apis-fusionconnectivity-partneragent.md#partneragentunbinddevice)接口进行解注册。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceAddress | [PartnerDeviceAddress](js-apis-fusionconnectivity-partneragent.md#partneragentpartnerdeviceaddress) | 是 | 应用注册的设备地址信息。  应用需配置PartnerDeviceAddress类型的bluetoothAddress选项。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 应用是否注册过该设备。 true表示已注册设备，false表示未注册设备。 |

**错误码**：

以下错误码的详细介绍请参考[通用错误码说明文档](errorcode-universal.md)和[融合短距服务子系统错误码](errorcode-fusionconnectivity.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 34900099 | Internal error. |

**示例**：

```
1. import { partnerAgent, common } from '@kit.ConnectivityKit';
2. try {
3. let btAddr: common.BluetoothAddress = {
4. "address": "11:22:33:44:55:66",
5. "addressType": common.BluetoothAddressType.REAL,
6. };
7. let deviceAddress: partnerAgent.PartnerDeviceAddress = {
8. "bluetoothAddress": btAddr,
9. };
10. let isBound = partnerAgent.isDeviceBound(deviceAddress);
11. console.info(`device is bound: ${isBound}`);
12. } catch (err) {
13. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
14. }
```

## partnerAgent.getBoundDevices

PhonePC/2in1Tablet

getBoundDevices(): PartnerDeviceAddress[]

获取应用当前注册过的所有设备。

* 可通过调用[bindDevice](js-apis-fusionconnectivity-partneragent.md#partneragentbinddevice)接口注册设备。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [PartnerDeviceAddress](js-apis-fusionconnectivity-partneragent.md#partneragentpartnerdeviceaddress)[] | 应用注册过的所有设备。 |

**错误码**：

以下错误码的详细介绍请参考[通用错误码说明文档](errorcode-universal.md)和[融合短距服务子系统错误码](errorcode-fusionconnectivity.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 34900099 | Internal error. |

**示例**：

```
1. import { partnerAgent, common } from '@kit.ConnectivityKit';
2. try {
3. let devices = partnerAgent.getBoundDevices();
4. console.info(`bound devices: ${devices}`);
5. } catch (err) {
6. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
7. }
```

## partnerAgent.isDeviceControlEnabled

PhonePC/2in1Tablet

isDeviceControlEnabled(deviceAddress: PartnerDeviceAddress): boolean

判断当前设备的互通功能是否已经打开。

* 调用[bindDevice](js-apis-fusionconnectivity-partneragent.md#partneragentbinddevice)接口注册设备后，设备的互通功能将默认开启，且可在系统设置应用设备详情页显示该功能已开启。
* 如果该功能已关闭，可通过系统设置应用设备详情页信息互通功能开关使能该功能。
* 如果系统设置应用设备详情页未显示此功能开关，请先调用[bindDevice](js-apis-fusionconnectivity-partneragent.md#partneragentbinddevice)接口注册设备，之后此功能开关按钮会出现。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceAddress | [PartnerDeviceAddress](js-apis-fusionconnectivity-partneragent.md#partneragentpartnerdeviceaddress) | 是 | 应用注册的设备地址信息。  应用需在PartnerDeviceAddress中设置bluetoothAddress字段值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前设备是否已经打开互通功能。true表示已打开，false表示未打开。 |

**错误码**：

以下错误码的详细介绍请参考[通用错误码说明文档](errorcode-universal.md)和[融合短距服务子系统错误码](errorcode-fusionconnectivity.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 34900099 | Internal error. |

**示例**：

```
1. import { partnerAgent, common } from '@kit.ConnectivityKit';
2. try {
3. let btAddr: common.BluetoothAddress = {
4. "address": "11:22:33:44:55:66",
5. "addressType": common.BluetoothAddressType.REAL,
6. };
7. let deviceAddress: partnerAgent.PartnerDeviceAddress = {
8. "bluetoothAddress": btAddr,
9. };
10. let isEnabled = partnerAgent.isDeviceControlEnabled(deviceAddress);
11. console.info(`device control is enabled: ${isEnabled}`);
12. } catch (err) {
13. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
14. }
```

## partnerAgent.DeviceCapability

PhonePC/2in1Tablet

描述设备支持的被发现能力。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| supportBR | boolean | 否 | 是 | 该设备是否支持通过[ACL](../harmonyos-guides/terminology.md#acl)连接的方式发现，建立ACL连接后会认为成功发现了该设备。发现设备后，会拉起[PartnerAgentExtensionAbility](is-fusionconnectivity-partneragentextensionability.md)进程，并调用进程中[onDeviceDiscovered](is-fusionconnectivity-partneragentextensionability.md#ondevicediscovered)方法。true表示支持通过连接的方式发现，false表示不支持通过连接的方式发现。未指定默认为false。 |
| supportBleAdvertiser | boolean | 否 | 是 | 该设备是否支持通过[BLE](../harmonyos-guides/terminology.md#ble)扫描的方式发现，扫描到该设备后会认为成功发现了该设备。发现设备后，会拉起PartnerAgentExtensionAbility进程，并调用进程中onDeviceDiscovered方法。true表示支持通过BLE扫描的方式发现，false表示不支持通过BLE扫描的方式发现。未指定默认为false。  注意：  选择[supportBleAdvertiser](js-apis-fusionconnectivity-partneragent.md#partneragentdevicecapability)选项，若扫描到该设备，3min内无ACL连接，会调用[onDestroyWithReason](is-fusionconnectivity-partneragentextensionability.md#ondestroywithreason)并销毁已拉起的PartnerAgentExtensionAbility进程。 |

## partnerAgent.BusinessCapability

PhonePC/2in1Tablet

描述设备支持的业务功能。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| supportMediaControl | boolean | 否 | 是 | 该设备是否支持媒体控制功能，例如控制媒体播放、音量调节、上一首和下一首等功能。true表示支持，false表示不支持。未指定默认为false。 |
| supportTelephonyControl | boolean | 否 | 是 | 该设备是否支持通话控制功能，如接听和挂断电话。 true表示支持，false表示不支持。未指定默认为false。  注意：  supportMediaControl和supportTelephonyControl均选择false时，[设备发现](js-apis-fusionconnectivity-partneragent.md#partneragentdevicecapability)时不会拉起[PartnerAgentExtensionAbility](is-fusionconnectivity-partneragentextensionability.md)进程。 |

## partnerAgent.PartnerDeviceAddress

PhonePC/2in1Tablet

描述设备地址信息。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bluetoothAddress | [common.BluetoothAddress](js-apis-bluetooth-common.md#bluetoothaddress) | 否 | 是 | 该设备的蓝牙地址信息。 |

## partnerAgent.PartnerAgentExtensionAbilityDestroyReason

PhonePC/2in1Tablet

枚举，PartnerAgentExtensionAbility被销毁的原因。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN\_REASON | 0 | 系统内部导致的未知原因，建议重试该操作。 |
| USER\_CLOSED\_ABILITY | 1 | 用户在系统设置应用关闭了该设备的信息互通功能，建议在系统设置应用开启该设备的信息互通功能。 |
| DEVICE\_UNPAIRED | 2 | 用户取消了该设备的蓝牙配对关系，建议重新进行蓝牙配对流程。 |
| DEVICE\_LOST | 3 | 该设备已断开连接或未被发现，可能原因包括距离过长、设备关机、设备电量耗尽等，建议确认设备状态 |
| BLUETOOTH\_DISABLED | 4 | 蓝牙被关闭，建议打开蓝牙 |
