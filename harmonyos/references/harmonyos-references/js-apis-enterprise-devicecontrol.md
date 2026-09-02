---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-devicecontrol
title: "@ohos.enterprise.deviceControl（设备控制管理）"
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.deviceControl（设备控制管理）
category: harmonyos-references
scraped_at: 2026-09-02T15:02:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2a3344427eb503c71b630d33247a42a0dcbdd7347536c206f9ebfa8a6962c173
---

本模块提供设备控制能力，用于企业设备管理场景。管理员可以通过本模块远程控制设备，包括设备重启、关机、锁屏、恢复出厂设置等操作，帮助企业实现设备统一管理和安全管控。

**说明** 

本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

## 导入模块

```ts
import { deviceControl } from '@kit.MDMKit';
```

## deviceControl.operateDevice

operateDevice(admin: Want, operate: string, addition?: string): void

允许管理员对设备执行恢复出厂设置、重启、关机、锁屏等操作，例如在企业设备管理场景下，管理员可远程控制员工设备执行恢复出厂设置、重启、关机或锁屏等操作。

**需要权限：** ohos.permission.ENTERPRISE\_OPERATE\_DEVICE

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| operate | string | 是 | 要执行的操作。仅支持以下操作类型：  - resetFactory：设备恢复出厂设置。接口调用后，设备将立即恢复出厂设置。恢复完成后，整机设备数据将全部被擦除且无法恢复。企业需要做好应用的安全设计，防止应用被攻击导致企业数据丢失。已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口禁用了恢复出厂，需要先解除禁用。  - reboot：设备重启。  - shutDown：设备关机。  - lockScreen：设备锁屏。  - lockDevice：设备锁定。该能力使用后设备屏幕无法使用，按键无响应，仅支持锁屏文案定制，不支持在锁屏界面定制交互功能。在开发过程中，下发设备锁定策略前一定要预留逃生通道，并且确保逃生通道正常。建议开发时保留hdc能力与远程通信能力，通过hdc命令或者远程push能力能触发设备解锁定功能。  如果需要实现在屏幕锁定的情况下支持自定义行为的能力，建议使用[setAllowedKioskApps](js-apis-enterprise-applicationmanager.md#applicationmanagersetallowedkioskapps20)接口配置支持[Kiosk模式](js-apis-app-ability-kioskmanager.md#kioskmanagerenterkioskmode)。  - unlockDevice：设备解锁定。  在API version21之前，设备锁定和解锁定仅支持PC/2in1使用。从API version21开始，设备锁定和解锁定支持Phone和Tablet。 |
| addition | string | 否 | 执行时附加参数。若operate为lockDevice，表示屏幕锁定后展示的描述信息。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { deviceControl } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  deviceControl.operateDevice(wantTemp, 'resetFactory');
} catch (err) {
  console.error(`Failed to reset factory. Code is ${err.code}, message is ${err.message}`);
}
```

## deviceControl.operateDevice

operateDevice(admin: Want, operation: Operation, addition?: string): void

允许管理员操作设备，例如磁盘擦除。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_OPERATE\_DEVICE

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| operation | [Operation](js-apis-enterprise-devicecontrol.md#operation) | 是 | 要执行的操作。 |
| addition | string | 否 | 执行时附加参数。当operation类型为磁盘擦除时，附加参数为图片的沙箱路径。若磁盘擦除成功后需给用户展示信息，可设置该参数传递信息，该图片大小需小于5KB（建议使用二维码图片）。长度限制为1024字节 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 9200012 | Parameter verification failed. |
| 9201048 | Failed to operate the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { deviceControl } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let filePath: string = '/test.png';

try {
  // 参数需根据实际情况进行替换
  deviceControl.operateDevice(wantTemp, deviceControl.Operation.DISK_ERASURE, filePath);
} catch (err) {
  console.error(`Failed to disk erase. Code is ${err.code}, message is ${err.message}`);
}
```

## Operation

设备操作。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISK\_ERASURE | 0 | 磁盘擦除。接口调用后，设备将立即执行磁盘擦除操作。磁盘擦除完成后，整机设备数据将全部被擦除且无法恢复。企业需要做好应用的安全设计，防止应用被攻击导致企业数据丢失。仅支持PC/2in1设备。 |
