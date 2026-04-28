---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-bluetoothmanager
title: @ohos.enterprise.bluetoothManager（蓝牙管理）
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.bluetoothManager（蓝牙管理）
category: harmonyos-references
scraped_at: 2026-04-28T08:10:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1ed5c1f572ae53696fd194ad542e8586869c95bdbdb0f5da21305e6d5c181d8b
---

本模块提供设备蓝牙管理的能力，包括设置和查询蓝牙信息等。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

全局通用限制类策略由restrictions统一提供，若要全局禁用蓝牙，请参考[@ohos.enterprise.restrictions（限制类策略）](js-apis-enterprise-restrictions.md)。

## 导入模块

PhonePC/2in1Tablet

```
1. import { bluetoothManager } from '@kit.MDMKit';
```

## bluetoothManager.getBluetoothInfo

PhonePC/2in1Tablet

getBluetoothInfo(admin: Want): BluetoothInfo

查询设备蓝牙信息。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BluetoothInfo](js-apis-enterprise-bluetoothmanager.md#bluetoothinfo) | 蓝牙信息，包含蓝牙名称、蓝牙状态和蓝牙连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { bluetoothManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. let result: bluetoothManager.BluetoothInfo = bluetoothManager.getBluetoothInfo(wantTemp);
12. console.info(`Succeeded in getting bluetooth info: ${JSON.stringify(result)}`);
13. } catch(err) {
14. console.error(`Failed to get bluetooth info. Code: ${err.code}, message: ${err.message}`);
15. }
```

## bluetoothManager.addAllowedBluetoothDevices

PhonePC/2in1Tablet

addAllowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void

添加蓝牙设备可用名单。添加蓝牙设备可用名单后当前设备仅允许连接该名单下的蓝牙设备。从API version 22开始，数组中的MAC地址必须符合蓝牙MAC规范（例如：00:1A:2B:3C:4D:5E），添加时会移除不合法的MAC地址，仅添加合法的MAC地址。

以下情况下，通过本接口添加蓝牙设备可用名单，会报策略冲突：

1. 已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口禁用了蓝牙。通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口启用蓝牙后，可解除冲突。
2. 已经通过[addDisallowedBluetoothDevices](js-apis-enterprise-bluetoothmanager.md#bluetoothmanageradddisallowedbluetoothdevices20)接口添加了蓝牙设备禁用名单。通过[removeDisallowedBluetoothDevices](js-apis-enterprise-bluetoothmanager.md#bluetoothmanagerremovedisallowedbluetoothdevices20)移除蓝牙设备禁用名单后，可解除冲突。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| deviceIds | Array<string> | 是 | 蓝牙设备MAC地址的数组。蓝牙设备允许名单数组长度上限为1000，若当前允许名单中已有300个蓝牙设备MAC地址，则只允许再添加700个。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { bluetoothManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let deviceIds: Array<string> = ["00:1A:2B:3C:4D:5E","AA:BB:CC:DD:EE:FF"];
11. try {
12. bluetoothManager.addAllowedBluetoothDevices(wantTemp,deviceIds);
13. console.info(`Succeeded in adding allowed bluetooth devices.`);
14. } catch(err) {
15. console.error(`Failed to add allowed bluetooth devices. Code: ${err.code}, message: ${err.message}`);
16. }
```

## bluetoothManager.removeAllowedBluetoothDevices

PhonePC/2in1Tablet

removeAllowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void

移除蓝牙设备可用名单。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| deviceIds | Array<string> | 是 | 蓝牙设备MAC地址的数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { bluetoothManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let deviceIds: Array<string> = ["00:1A:2B:3C:4D:5E","AA:BB:CC:DD:EE:FF"];
11. try {
12. bluetoothManager.removeAllowedBluetoothDevices(wantTemp,deviceIds);
13. console.info(`Succeeded in removing allowed bluetooth devices.`);
14. } catch(err) {
15. console.error(`Failed to remove allowed bluetooth devices. Code: ${err.code}, message: ${err.message}`);
16. }
```

## bluetoothManager.getAllowedBluetoothDevices

PhonePC/2in1Tablet

getAllowedBluetoothDevices(admin: Want): Array<string>

获取蓝牙设备可用名单。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 可用名单中蓝牙设备MAC地址的数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { bluetoothManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let result: Array<string> = bluetoothManager.getAllowedBluetoothDevices(wantTemp);
11. console.info(`Succeeded in getting allowed bluetooth devices. Result: ${JSON.stringify(result)}`);
12. } catch(err) {
13. console.error(`Failed to get allowed bluetooth devices. Code: ${err.code}, message: ${err.message}`);
14. }
```

## bluetoothManager.addDisallowedBluetoothDevices20+

PhonePC/2in1Tablet

addDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void

添加蓝牙设备禁用名单。添加禁用名单后当前设备不允许连接该名单下的蓝牙设备。从API version 22开始，数组中的MAC地址必须符合蓝牙MAC规范（例如：00:1A:2B:3C:4D:5E），添加时会移除不合法的MAC地址，仅添加合法的MAC地址。

以下情况下，通过本接口添加蓝牙设备禁用名单，会报策略冲突：

1. 已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口禁用了蓝牙。通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口启用蓝牙后，可解除冲突。
2. 已经通过[addAllowedBluetoothDevices](js-apis-enterprise-bluetoothmanager.md#bluetoothmanageraddallowedbluetoothdevices)接口添加了蓝牙设备可用名单。通过[removeAllowedBluetoothDevices](js-apis-enterprise-bluetoothmanager.md#bluetoothmanagerremoveallowedbluetoothdevices)移除蓝牙设备可用名单后，可解除冲突。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| deviceIds | Array<string> | 是 | 蓝牙设备MAC地址的数组。蓝牙设备禁用名单数组长度上限为1000，若当前禁用名单中已有300个蓝牙设备MAC地址，则只允许再添加700个。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { bluetoothManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let deviceIds: Array<string> = ["00:1A:2B:3C:4D:5E","AA:BB:CC:DD:EE:FF"];
11. try {
12. bluetoothManager.addDisallowedBluetoothDevices(wantTemp,deviceIds);
13. console.info(`Succeeded in adding disallowed bluetooth devices.`);
14. } catch(err) {
15. console.error(`Failed to add disallowed bluetooth devices. Code: ${err.code}, message: ${err.message}`);
16. }
```

## bluetoothManager.removeDisallowedBluetoothDevices20+

PhonePC/2in1Tablet

removeDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void

移除蓝牙设备禁用名单。若移除禁用名单中的部分蓝牙设备，则当前设备不允许连接禁用名单内剩余的蓝牙设备。若移除禁用名单中的所有蓝牙设备，则当前设备可以连接任意的蓝牙设备。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| deviceIds | Array<string> | 是 | 蓝牙设备MAC地址的数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { bluetoothManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let deviceIds: Array<string> = ["00:1A:2B:3C:4D:5E","AA:BB:CC:DD:EE:FF"];
11. try {
12. bluetoothManager.removeDisallowedBluetoothDevices(wantTemp,deviceIds);
13. console.info(`Succeeded in removing disallowed bluetooth devices.`);
14. } catch(err) {
15. console.error(`Failed to remove disallowed bluetooth devices. Code: ${err.code}, message: ${err.message}`);
16. }
```

## bluetoothManager.getDisallowedBluetoothDevices20+

PhonePC/2in1Tablet

getDisallowedBluetoothDevices(admin: Want): Array<string>

获取蓝牙设备禁用名单。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 禁用名单中蓝牙设备MAC地址的数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { bluetoothManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let result: Array<string> = bluetoothManager.getDisallowedBluetoothDevices(wantTemp);
11. console.info(`Succeeded in getting disallowed bluetooth devices. Result: ${JSON.stringify(result)}`);
12. } catch(err) {
13. console.error(`Failed to get disallowed bluetooth devices. Code: ${err.code}, message: ${err.message}`);
14. }
```

## bluetoothManager.turnOnBluetooth20+

PhonePC/2in1Tablet

turnOnBluetooth(admin: Want): void

开启蓝牙。蓝牙开启后用户可以手动关闭。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 203 | This function is prohibited by enterprise management policies. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { bluetoothManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. bluetoothManager.turnOnBluetooth(wantTemp);
11. console.info(`Succeeded in turning on bluetooth.`);
12. } catch(err) {
13. console.error(`Failed to turn on bluetooth. Code: ${err.code}, message: ${err.message}`);
14. }
```

## bluetoothManager.turnOffBluetooth20+

PhonePC/2in1Tablet

turnOffBluetooth(admin: Want): void

关闭蓝牙。蓝牙关闭后用户可以手动打开。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 203 | This function is prohibited by enterprise management policies. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { bluetoothManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. bluetoothManager.turnOffBluetooth(wantTemp);
11. console.info('Succeeded in turning off bluetooth.');
12. } catch(err) {
13. console.error(`Failed to turn off bluetooth. Code: ${err.code}, message: ${err.message}`);
14. }
```

## bluetoothManager.addDisallowedBluetoothProtocols20+

PhonePC/2in1Tablet

addDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>): void

添加蓝牙协议禁用名单。添加后，指定用户将无法使用该禁用名单中的蓝牙协议向其他设备外发文件。通过该接口禁用GATT或SPP协议，对系统服务和系统应用不生效。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |
| protocols | Array<[Protocol](js-apis-enterprise-bluetoothmanager.md#protocol20)> | 是 | 蓝牙协议的数组。数组长度上限为10000。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { bluetoothManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let accountId: number = 100;
11. let protocols: Array<bluetoothManager.Protocol> = [bluetoothManager.Protocol.GATT, bluetoothManager.Protocol.SPP];
12. try{
13. bluetoothManager.addDisallowedBluetoothProtocols(wantTemp, accountId, protocols);
14. console.info('Succeeded in adding disallowed bluetooth protocols policy.');
15. } catch (err) {
16. console.error(`Failed to add disallowed bluetooth protocols. Code: ${err.code}, message: ${err.message}`);
17. }
```

## bluetoothManager.removeDisallowedBluetoothProtocols20+

PhonePC/2in1Tablet

removeDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>): void

移除蓝牙协议禁用名单。若移除禁用名单中某个用户的部分蓝牙协议，则该用户不能使用禁用名单内剩余的蓝牙协议向其他设备外发文件。若移除禁用名单中某个用户的所有蓝牙协议，则该用户可以使用任意蓝牙协议向其他设备外发文件。若移除禁用名单中不存在的蓝牙协议，接口可调用成功，但不会移除禁用名单中不存在的蓝牙协议。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |
| protocols | Array<[Protocol](js-apis-enterprise-bluetoothmanager.md#protocol20)> | 是 | 蓝牙协议的数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { bluetoothManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let accountId: number = 100;
11. let protocols: Array<bluetoothManager.Protocol> = [bluetoothManager.Protocol.GATT, bluetoothManager.Protocol.SPP];
12. try{
13. bluetoothManager.removeDisallowedBluetoothProtocols(wantTemp, accountId, protocols);
14. console.info('Succeeded in removing disallowed bluetooth protocols policy.');
15. } catch (err) {
16. console.error(`Failed to remove disallowed bluetooth protocols. Code: ${err.code}, message: ${err.message}`);
17. }
```

## bluetoothManager.getDisallowedBluetoothProtocols20+

PhonePC/2in1Tablet

getDisallowedBluetoothProtocols(admin: Want, accountId: number): Array<Protocol>

获取指定用户的蓝牙协议禁用名单。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BLUETOOTH

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[Protocol](js-apis-enterprise-bluetoothmanager.md#protocol20)> | 禁用名单中蓝牙协议的数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { bluetoothManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let accountId: number = 100;
11. try{
12. let result: Array<bluetoothManager.Protocol> = bluetoothManager.getDisallowedBluetoothProtocols(wantTemp, accountId);
13. console.info(`Succeeded in getting disallowed bluetooth protocols. Result: ${JSON.stringify(result)}`);
14. } catch (err) {
15. console.error(`Failed to get disallowed bluetooth protocols. Code: ${err.code}, message: ${err.message}`);
16. }
```

## BluetoothInfo

PhonePC/2in1Tablet

设备的蓝牙信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 表示设备的蓝牙名称。 |
| state | [access.BluetoothState](js-apis-bluetooth-access.md#bluetoothstate) | 否 | 否 | 表示设备的蓝牙状态。 |
| connectionState | [constant.ProfileConnectionState](js-apis-bluetooth-constant.md#profileconnectionstate) | 否 | 否 | 表示设备的蓝牙连接状态。 |

## Protocol20+

PhonePC/2in1Tablet

蓝牙协议类型。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GATT | 0 | [GATT协议](../harmonyos-guides/terminology.md#gatt)。 |
| SPP | 1 | [SPP协议](../harmonyos-guides/terminology.md#spp)。 |
| OPP | 2 | [OPP协议](../harmonyos-guides/terminology.md#opp)。 |
