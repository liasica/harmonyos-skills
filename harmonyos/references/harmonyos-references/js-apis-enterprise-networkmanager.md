---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-networkmanager
title: @ohos.enterprise.networkManager（网络管理）
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.networkManager（网络管理）
category: harmonyos-references
scraped_at: 2026-04-28T08:10:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:59457b77d16c47fec9fd28de6427b437be15b896b00e9c59c7fdf0e05af2d602
---

本模块提供设备网络管理能力，包括查询设备IP地址、MAC地址信息等。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

## 导入模块

PhonePC/2in1Tablet

```
1. import { networkManager } from '@kit.MDMKit';
```

## networkManager.getAllNetworkInterfacesSync

PhonePC/2in1Tablet

getAllNetworkInterfacesSync(admin: Want): Array<string>

获取所有激活的有线网络接口。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回所有激活的有线网络接口名称数组。 |

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
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. let result: Array<string> = networkManager.getAllNetworkInterfacesSync(wantTemp);
12. console.info(`Succeeded in getting all network interfaces, result : ${JSON.stringify(result)}`);
13. } catch (err) {
14. console.error(`Failed to get all network interfaces. Code: ${err.code}, message: ${err.message}`);
15. }
```

## networkManager.getIpAddressSync

PhonePC/2in1Tablet

getIpAddressSync(admin: Want, networkInterface: string): string

根据网络接口获取设备IP地址。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| networkInterface | string | 是 | 指定网络接口。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回设备指定网络接口的IP地址。 |

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
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. // 参数需根据实际情况进行替换
12. let result: string = networkManager.getIpAddressSync(wantTemp, 'eth0');
13. console.info(`Succeeded in getting ip address, result : ${result}`);
14. } catch (err) {
15. console.error(`Failed to get ip address. Code: ${err.code}, message: ${err.message}`);
16. }
```

## networkManager.getMacSync

PhonePC/2in1Tablet

getMacSync(admin: Want, networkInterface: string): string

根据网络接口获取设备MAC地址。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| networkInterface | string | 是 | 指定网络接口。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回设备指定网络接口的MAC地址。 |

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
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. // 参数需根据实际情况进行替换
12. let result: string = networkManager.getMacSync(wantTemp, 'eth0');
13. console.info(`Succeeded in getting mac, result : ${result}`);
14. } catch (err) {
15. console.error(`Failed to get mac. Code: ${err.code}, message: ${err.message}`);
16. }
```

## networkManager.isNetworkInterfaceDisabledSync

PhonePC/2in1Tablet

isNetworkInterfaceDisabledSync(admin: Want, networkInterface: string): boolean

查询指定网络接口是否被禁用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| networkInterface | string | 是 | 指定网络接口。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回指定网络接口是否被禁用，true表示该网络接口被禁用，false表示该网络接口未被禁用。 |

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
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. // 参数需根据实际情况进行替换
12. let result: boolean = networkManager.isNetworkInterfaceDisabledSync(wantTemp, 'eth0');
13. console.info(`Succeeded in querying network interface is disabled or not, result : ${result}`);
14. } catch (err) {
15. console.error(`Failed to query network interface is disabled or not. Code: ${err.code}, message: ${err.message}`);
16. }
```

## networkManager.setNetworkInterfaceDisabledSync

PhonePC/2in1Tablet

setNetworkInterfaceDisabledSync(admin: Want, networkInterface: string, isDisabled: boolean): void

禁止设备使用指定网络接口。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| networkInterface | string | 是 | 指定网络接口。 |
| isDisabled | boolean | 是 | true表示禁用该网络接口，false表示开启该网络接口。 |

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
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. // 参数需根据实际情况进行替换
12. networkManager.setNetworkInterfaceDisabledSync(wantTemp, 'eth0', true);
13. console.info(`Succeeded in setting network interface disabled`);
14. } catch (err) {
15. console.error(`Failed to set network interface disabled. Code: ${err.code}, message: ${err.message}`);
16. }
```

## networkManager.setGlobalProxySync

PhonePC/2in1Tablet

setGlobalProxySync(admin: Want, httpProxy: connection.HttpProxy): void

设置网络全局代理。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| httpProxy | [connection.HttpProxy](js-apis-net-connection.md#httpproxy10) | 是 | 网络全局Http代理配置信息。 |

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
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';
3. import { connection } from '@kit.NetworkKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };

11. // 需根据实际情况进行替换
12. let exclusionStr: string = "192.168,baidu.com";
13. let exclusionArray: Array<string> = exclusionStr.split(',');
14. let httpProxy: connection.HttpProxy = {
15. host: "192.168.xx.xxx",
16. port: 8080,
17. exclusionList: exclusionArray
18. };

20. try {
21. networkManager.setGlobalProxySync(wantTemp, httpProxy);
22. console.info(`Succeeded in setting network global proxy.`);
23. } catch (err) {
24. console.error(`Failed to set network global proxy. Code: ${err.code}, message: ${err.message}`);
25. }
```

## networkManager.setGlobalProxyForAccount15+

PhonePC/2in1Tablet

setGlobalProxyForAccount(admin: Want, httpProxy: connection.HttpProxy, accountId: number): void

设置指定用户下的网络代理。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| httpProxy | [connection.HttpProxy](js-apis-net-connection.md#httpproxy10) | 是 | 网络代理配置信息。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';
3. import { connection } from '@kit.NetworkKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };

11. let httpProxy: connection.HttpProxy = {
12. // 需根据实际情况进行替换
13. host: '192.168.xx.xxx',
14. port: 8080,
15. exclusionList: ['192.168', 'baidu.com']
16. };

18. try {
19. // 参数需根据实际情况进行替换
20. networkManager.setGlobalProxyForAccount(wantTemp, httpProxy, 100);
21. console.info(`Succeeded in setting network global proxy.`);
22. } catch (err) {
23. console.error(`Failed to set network global proxy. Code: ${err.code}, message: ${err.message}`);
24. }
```

## networkManager.getGlobalProxySync

PhonePC/2in1Tablet

getGlobalProxySync(admin: Want): connection.HttpProxy

获取网络全局代理。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [connection.HttpProxy](js-apis-net-connection.md#httpproxy10) | 返回网络全局HTTP代理配置信息。 |

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
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';
3. import { connection } from '@kit.NetworkKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };

11. try {
12. let result: connection.HttpProxy = networkManager.getGlobalProxySync(wantTemp);
13. console.info(`Succeeded in getting network global proxy, result : ${JSON.stringify(result)}`);
14. } catch (err) {
15. console.error(`Failed to get network global proxy. Code: ${err.code}, message: ${err.message}`);
16. }
```

## networkManager.getGlobalProxyForAccount15+

PhonePC/2in1Tablet

getGlobalProxyForAccount(admin: Want | null, accountId: number): connection.HttpProxy

获取指定用户下的网络代理。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [connection.HttpProxy](js-apis-net-connection.md#httpproxy10) | 网络代理配置信息。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';
3. import { connection } from '@kit.NetworkKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };

11. try {
12. // 参数需根据实际情况进行替换
13. let result: connection.HttpProxy = networkManager.getGlobalProxyForAccount(wantTemp, 100);
14. console.info(`Succeeded in getting network global proxy, result : ${JSON.stringify(result)}`);
15. } catch (err) {
16. console.error(`Failed to get network global proxy. Code: ${err.code}, message: ${err.message}`);
17. }
```

## networkManager.addFirewallRule

PhonePC/2in1Tablet

addFirewallRule(admin: Want, firewallRule: FirewallRule): void

为设备添加防火墙过滤规则。

API version 21及之前版本，仅支持IPv4。从API version 22开始，支持IPv4和IPv6。

从API version 23开始，支持[LogType](js-apis-enterprise-networkmanager.md#logtype23)。

添加了[Action](js-apis-enterprise-networkmanager.md#action)为ALLOW规则后，将会默认添加DENY规则，不在ALLOW规则之内的网络数据包将会被丢弃或拦截。

设备重启，将会清空防火墙过滤规则。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| firewallRule | [FirewallRule](js-apis-enterprise-networkmanager.md#firewallrule) | 是 | 添加防火墙过滤规则。 |

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
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. let firewallRule: networkManager.FirewallRule = {
10. // 需根据实际情况进行替换
11. "srcAddr": "192.168.1.1-192.168.22.66",
12. "destAddr": "10.1.1.1",
13. "srcPort": "8080",
14. "destPort": "8080",
15. "appUid": "9696",
16. "direction": networkManager.Direction.OUTPUT,
17. "action": networkManager.Action.DENY,
18. "protocol": networkManager.Protocol.UDP,
19. "family": 1,
20. "logType": networkManager.LogType.NFLOG
21. };

23. try {
24. networkManager.addFirewallRule(wantTemp, firewallRule);
25. console.info('Succeeded in adding firewall rule.');
26. } catch (err) {
27. console.error(`Failed to add firewall rule. Code: ${err.code}, message: ${err.message}`);
28. }
```

## networkManager.removeFirewallRule

PhonePC/2in1Tablet

removeFirewallRule(admin: Want, firewallRule?: FirewallRule): void

移除设备防火墙过滤规则。

API version 21及之前版本，仅支持IPv4。从API version 22开始，支持IPv4和IPv6。

从API version 23开始，支持[LogType](js-apis-enterprise-networkmanager.md#logtype23)。

移除规则后如果不存在[Action](js-apis-enterprise-networkmanager.md#action)为ALLOW规则后，会将[addFirewallRule](js-apis-enterprise-networkmanager.md#networkmanageraddfirewallrule)添加的默认DENY规则清空。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| firewallRule | [FirewallRule](js-apis-enterprise-networkmanager.md#firewallrule) | 否 | 移除防火墙过滤规则。值为空时，清空所有的防火墙规则。 |

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
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. let firewallRule: networkManager.FirewallRule = {
11. // 需根据实际情况进行替换
12. "srcAddr": "192.168.1.1-192.168.22.66",
13. "destAddr": "10.1.1.1",
14. "srcPort": "8080",
15. "destPort": "8080",
16. "appUid": "9696",
17. "direction": networkManager.Direction.OUTPUT,
18. "action": networkManager.Action.DENY,
19. "protocol": networkManager.Protocol.UDP,
20. "family": 1,
21. "logType": networkManager.LogType.NFLOG
22. };

24. // 移除指定的规则
25. try {
26. networkManager.removeFirewallRule(wantTemp, firewallRule);
27. console.info('Succeeded in removing firewall rule.');
28. } catch (err) {
29. console.error(`Failed to remove firewall rule. Code: ${err.code}, message: ${err.message}`);
30. }

32. // 清空所有规则
33. try {
34. networkManager.removeFirewallRule(wantTemp);
35. console.info('Succeeded in removing all firewall rule.');
36. } catch (err) {
37. console.error(`Failed to remove all firewall rule. Code: ${err.code}, message: ${err.message}`);
38. }
```

## networkManager.getFirewallRules

PhonePC/2in1Tablet

getFirewallRules(admin: Want): Array<FirewallRule>

查询设备防火墙过滤规则。

API version 21及之前版本，仅支持IPv4。从API version 22开始，支持IPv4和IPv6。

从API version 23开始，支持[LogType](js-apis-enterprise-networkmanager.md#logtype23)。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[FirewallRule](js-apis-enterprise-networkmanager.md#firewallrule)> | 返回当前设备配置的防火墙过滤规则列表，当方法调用错误时会抛出异常。 |

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
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. let firewallRule: Array<networkManager.FirewallRule>;
10. try {
11. firewallRule = networkManager.getFirewallRules(wantTemp);
12. console.info('Succeeded in getting firewall rules');
13. } catch (err) {
14. console.error(`Failed to get firewall rules. Code: ${err.code}, message: ${err.message}`);
15. }
```

## networkManager.addDomainFilterRule

PhonePC/2in1Tablet

addDomainFilterRule(admin: Want, domainFilterRule: DomainFilterRule): void

为设备添加域名过滤规则。

API version 21及之前版本，仅支持IPv4。从API version 22开始，支持IPv4和IPv6。

从API version 23开始，支持[LogType](js-apis-enterprise-networkmanager.md#logtype23)。

添加了[Action](js-apis-enterprise-networkmanager.md#action)为ALLOW规则后，将会默认添加DENY规则，不在ALLOW规则之内的域名解析数据包将会被丢弃或拦截。

设备重启，将会清空域名过滤规则。

说明

为避免DNS缓存导致拦截规则失效，建议系统启动后立即配置域名过滤规则。若已因DNS缓存导致拦截失效，重启系统可清除缓存，恢复拦截功能。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| domainFilterRule | [DomainFilterRule](js-apis-enterprise-networkmanager.md#domainfilterrule) | 是 | 添加域名过滤规则。 |

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
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. let domainFilterRule: networkManager.DomainFilterRule = {
10. // 需根据实际情况进行替换
11. "domainName": "www.example.com",
12. "appUid": "9696",
13. "action": networkManager.Action.DENY,
14. "family": 1,
15. "logType": networkManager.LogType.NFLOG
16. };

18. try {
19. networkManager.addDomainFilterRule(wantTemp, domainFilterRule);
20. console.info('Succeeded in adding domain filter rules');
21. } catch (err) {
22. console.error(`Failed to add domain filter rules. Code: ${err.code}, message: ${err.message}`);
23. }
```

## networkManager.removeDomainFilterRule

PhonePC/2in1Tablet

removeDomainFilterRule(admin: Want, domainFilterRule?: DomainFilterRule): void

移除设备域名过滤规则。

API version 21及之前版本，仅支持IPv4。从API version 22开始，支持IPv4和IPv6。

从API version 23开始，支持[LogType](js-apis-enterprise-networkmanager.md#logtype23)。

移除规则后如果不存在[Action](js-apis-enterprise-networkmanager.md#action)为ALLOW规则后，会将[addDomainFilterRule](js-apis-enterprise-networkmanager.md#networkmanageradddomainfilterrule)添加的默认DENY规则清空。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| domainFilterRule | [DomainFilterRule](js-apis-enterprise-networkmanager.md#domainfilterrule) | 否 | 移除域名过滤规则。值为空时，清空所有的域名规则。 |

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
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. let domainFilterRule: networkManager.DomainFilterRule = {
11. // 需根据实际情况进行替换
12. "domainName": "www.example.com",
13. "appUid": "9696",
14. "action": networkManager.Action.DENY,
15. "family": 1,
16. "logType": networkManager.LogType.NFLOG
17. };

19. // 移除指定的规则
20. try {
21. networkManager.removeDomainFilterRule(wantTemp, domainFilterRule);
22. console.info('Succeeded in removing domain filter rules');
23. } catch (err) {
24. console.error(`Failed to remove domain filter rules. Code: ${err.code}, message: ${err.message}`);
25. }

27. // 清空所有规则
28. try {
29. networkManager.removeDomainFilterRule(wantTemp);
30. console.info('Succeeded in removing all domain filter rules');
31. } catch (err) {
32. console.error(`Failed to remove all domain filter rules. Code: ${err.code}, message: ${err.message}`);
33. }
```

## networkManager.getDomainFilterRules

PhonePC/2in1Tablet

getDomainFilterRules(admin: Want): Array<DomainFilterRule>

查询设备域名过滤规则。

API version 21及之前版本，仅支持IPv4。从API version 22开始，支持IPv4和IPv6。

从API version 23开始，支持[LogType](js-apis-enterprise-networkmanager.md#logtype23)。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[DomainFilterRule](js-apis-enterprise-networkmanager.md#domainfilterrule)> | 返回当前设备配置的域名过滤规则列表，当方法调用错误时会抛出异常。 |

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
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. let domainFilterRule: Array<networkManager.DomainFilterRule>;
10. try {
11. domainFilterRule = networkManager.getDomainFilterRules(wantTemp);
12. console.info('Succeeded in getting  domain filter rules');
13. } catch (err) {
14. console.error(`Failed to get domain filter rules. Code: ${err.code}, message: ${err.message}`);
15. }
```

## networkManager.turnOnMobileData20+

PhonePC/2in1Tablet

turnOnMobileData(admin: Want, isForce: boolean): void

开启移动数据网络。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** 任意MDM应用通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口禁用了移动数据网络，则无法通过本接口直接开启移动数据网络。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| isForce | boolean | 是 | 是否强制打开移动数据网络。true表示强制开启，强制开启后不支持用户在设备上手动关闭，必须采用[turnOffMobileData](js-apis-enterprise-networkmanager.md#networkmanagerturnoffmobiledata20)接口关闭。false表示非强制开启，此时用户可以在设备上手动操作关闭移动数据网络。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. networkManager.turnOnMobileData(wantTemp, true);
11. console.info(`Turn on mobile data succeeded`);
12. } catch (err) {
13. console.error(`Failed to turn on mobile data. Code: ${err.code}, message: ${err.message}`);
14. }
```

## networkManager.turnOffMobileData20+

PhonePC/2in1Tablet

turnOffMobileData(admin: Want): void

关闭移动数据网络。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** 任意MDM应用通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口禁用了移动数据网络，则无法通过本接口直接关闭移动数据网络。

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

**示例：**

```
1. import { networkManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. networkManager.turnOffMobileData(wantTemp);
11. console.info(`Turn off mobile data succeeded`);
12. } catch (err) {
13. console.error(`Failed to turn off mobile data. Code: ${err.code}, message: ${err.message}`);
14. }
```

## networkManager.addApn20+

PhonePC/2in1Tablet

addApn(admin: Want, apnInfo: Record<string, string>): void

添加APN（Access Point Name，接入点名称）。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_APN

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| apnInfo | Record<string, string> | 是 | 需要添加的APN参数信息。  - apnName：APN配置的名称标识符，必选。  - mcc：3位数字的移动国家代码，必选。  - mnc：2-3位数字的移动网络代码，必选。  - apn：接入点名称，必选。  - type：APN的服务类型，可选。  - user：APN身份验证的用户名，可选。  - password：APN身份验证的密码，可选。  - proxy：普通数据连接的代理服务器地址，可选。  - mmsproxy：彩信服务的专用代理地址，可选。  - authType：APN的认证协议类型，可选。 |

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
2. import { networkManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility',
8. };
9. let apnInfo: Record<string, string> = {
10. // 需根据实际情况进行替换
11. "apnName": "CTNET",
12. "apn": "CTNET",
13. "mnc": "11",
14. "mcc": "460",
15. };
16. try {
17. networkManager.addApn(wantTemp, apnInfo);
18. console.info(`Succeeded in adding apn.`);
19. } catch (err) {
20. console.error(`Failed to add apn. Code: ${err.code}, message: ${err.message}`);
21. }
```

## networkManager.deleteApn20+

PhonePC/2in1Tablet

deleteApn(admin: Want, apnId: string): void

删除APN。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_APN

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| apnId | string | 是 | 需要删除的APN ID。可以通过[networkManager.queryApn](js-apis-enterprise-networkmanager.md#networkmanagerqueryapn20)获取设备信息。 |

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
2. import { networkManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility',
8. };
9. let apnId: string = "1"; // 需根据实际情况进行替换
10. try {
11. networkManager.deleteApn(wantTemp, apnId);
12. console.info(`Succeeded in deleting apn.`);
13. } catch (err) {
14. console.error(`Failed to delete apn. Code: ${err.code}, message: ${err.message}`);
15. }
```

## networkManager.updateApn20+

PhonePC/2in1Tablet

updateApn(admin: Want, apnInfo: Record<string, string>, apnId: string): void

更新APN。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_APN

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| apnInfo | Record<string, string> | 是 | 需要更新的APN参数信息。  - apnName：APN配置的名称标识符，可选。  - mcc：3位数字的移动国家代码，可选。  - mnc：2-3位数字的移动网络代码，可选。  - APN：接入点名称，可选。  - type：APN的服务类型，可选。  - user：APN身份验证的用户名，可选。  - password：APN身份验证的密码，可选。  - proxy：普通数据连接的代理服务器地址，可选。  - mmsproxy：彩信服务的专用代理地址，可选。  - authType：APN的认证协议类型，可选。 |
| apnId | string | 是 | 需要更新的APN ID。可以通过[networkManager.queryApn](js-apis-enterprise-networkmanager.md#networkmanagerqueryapn20)获取设备信息。 |

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
2. import { networkManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility',
8. };
9. let apnInfo: Record<string, string> = {
10. // 需根据实际情况进行替换
11. "apnName": "CTNET",
12. "apn": "CTNET",
13. "mnc": "11",
14. "mcc": "460",
15. };
16. let apnId: string = "1"; // 需根据实际情况进行替换
17. try {
18. networkManager.updateApn(wantTemp, apnInfo, apnId);
19. console.info(`Succeeded in updating apn.`);
20. } catch (err) {
21. console.error(`Failed to update apn. Code: ${err.code}, message: ${err.message}`);
22. }
```

## networkManager.setPreferredApn20+

PhonePC/2in1Tablet

setPreferredApn(admin: Want, apnId: string): void

设置优选APN。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_APN

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| apnId | string | 是 | 需要设置成优选的APN ID。可以通过[networkManager.queryApn](js-apis-enterprise-networkmanager.md#networkmanagerqueryapn20)获取设备信息。 |

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
2. import { networkManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility',
8. };
9. let apnId: string = "1"; // 需根据实际情况进行替换
10. try {
11. networkManager.setPreferredApn(wantTemp, apnId);
12. console.info(`Succeeded in setting preferred apn.`);
13. } catch (err) {
14. console.error(`Failed to set preferred apn. Code: ${err.code}, message: ${err.message}`);
15. }
```

## networkManager.queryApn20+

PhonePC/2in1Tablet

queryApn(admin: Want, apnInfo: Record<string, string>): Array<string>

查询符合特定APN信息的APN ID。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_APN

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| apnInfo | Record<string, string> | 是 | APN的查询条件。  - apnName：APN配置的名称标识符，可选。  - mcc：3位数字的移动国家代码，可选。  - mnc：2-3位数字的移动网络代码，可选。  - apn：接入点名称，可选。  - type：APN的服务类型，可选。  - user：APN身份验证的用户名，可选。  - proxy：普通数据连接的代理服务器地址，可选。  - mmsproxy：彩信服务的专用代理地址，可选。  - authType：APN的认证协议类型，可选。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 满足要求的APN ID。 |

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
2. import { networkManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility',
8. };
9. let apnInfo: Record<string, string> = {
10. // 需根据实际情况进行替换
11. "apnName": "CTNET",
12. "apn": "CTNET",
13. "mnc": "11",
14. "mcc": "460",
15. };
16. try {
17. let queryResult: Array<string> = networkManager.queryApn(wantTemp, apnInfo);
18. console.info(`Succeeded in querying apn, result : ${JSON.stringify(queryResult)}`);
19. } catch (err) {
20. console.error(`Failed to query apn. Code: ${err.code}, message: ${err.message}`);
21. }
```

## networkManager.queryApn20+

PhonePC/2in1Tablet

queryApn(admin: Want, apnId: string): Record<string, string>

查询特定APN的APN参数信息。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_APN

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| apnId | string | 是 | 指定的APN ID。可以通过[networkManager.queryApn](js-apis-enterprise-networkmanager.md#networkmanagerqueryapn20)获取设备信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record<string, string> | 指定APN ID的APN参数信息。  - apnName：APN配置的名称标识符。  - mcc：3位数字的移动国家代码。  - mnc：2-3位数字的移动网络代码。  - apn：接入点名称。  - type：APN的服务类型。  - user：APN身份验证的用户名。  - proxy：普通数据连接的代理服务器地址。  - mmsproxy：彩信服务的专用代理地址。  - authType：APN的认证协议类型。 |

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
2. import { networkManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility',
8. };
9. let apnId: string = "1"; // 需根据实际情况进行替换
10. try {
11. let queryResult: Record<string, string> = networkManager.queryApn(wantTemp, apnId);
12. console.info(`Succeeded in querying apn, result : ${JSON.stringify(queryResult)}`);
13. } catch (err) {
14. console.error(`Failed to query apn. Code: ${err.code}, message: ${err.message}`);
15. }
```

## networkManager.setEthernetConfig23+

PhonePC/2in1Tablet

setEthernetConfig(admin: Want, networkInterface: string, config: InterfaceConfig): void

设置特定以太网网络接口的IP地址。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。 |
| networkInterface | string | 是 | 要设置的网络接口名。 |
| config | [InterfaceConfig](js-apis-enterprise-networkmanager.md#interfaceconfig23) | 是 | 要设置的网络接口配置信息。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9201010 | Ethernet configuration failed. Ethernet device not connected. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { networkManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility',
8. };
9. let config: networkManager.InterfaceConfig = {
10. // 需根据实际情况进行替换
11. "ipSetMode": networkManager.IpSetMode.STATIC,
12. "ipAddress": "192.168.1.121",
13. "gateway": "192.168.1.1",
14. "netMask": "255.255.255.0",
15. "dnsServers": "192.168.1.1"
16. }
17. let networkInterface: string = "eth0"; // 需根据实际情况进行替换
18. try {
19. networkManager.setEthernetConfig(wantTemp, networkInterface, config);
20. console.info('Succeeded in setting ethernet config.');
21. } catch (err) {
22. console.error(`Failed to set ethernet config. Code: ${err.code}, message: ${err.message}`);
23. }
```

## FirewallRule

PhonePC/2in1Tablet

防火墙过滤规则。

API version 21及之前版本，仅支持IPv4。从API version 22开始，支持IPv4和IPv6。

从API version 23开始，支持[LogType](js-apis-enterprise-networkmanager.md#logtype23)。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| srcAddr | string | 否 | 是 | ip源地址。支持IP段，例如：192.168.0.0/22或者192.168.1.100-192.168.1.200 |
| destAddr | string | 否 | 是 | ip目标地址。支持IP段，例如：192.168.0.0/22或者192.168.1.100-192.168.1.200 |
| srcPort | string | 否 | 是 | 源端口。 |
| destPort | string | 否 | 是 | 目标端口。 |
| appUid | string | 否 | 是 | 应用uid。 |
| direction | [Direction](js-apis-enterprise-networkmanager.md#direction) | 否 | 是 | 规则链。  添加防火墙过滤规则时必填；  移除防火墙时非必填，当值为空时，表示清空所有的[Direction](js-apis-enterprise-networkmanager.md#direction)链，且srcAddr，destAddr，srcPort，destPort，appUid也必须传入空值。 |
| action | [Action](js-apis-enterprise-networkmanager.md#action) | 否 | 是 | 接收或者丢弃数据包。  添加防火墙过滤规则时必填；  移除防火墙时非必填，当值为空时，表示清空所有的匹配[Action](js-apis-enterprise-networkmanager.md#action)规则的链，且srcAddr，destAddr，srcPort，destPort，appUid也必须传入空值。 |
| protocol | [Protocol](js-apis-enterprise-networkmanager.md#protocol) | 否 | 是 | 网络协议。当值为ALL或者ICMP时，设置srcPort与destPort无效。 |
| family22+ | number | 否 | 是 | IP协议版本。支持取值为1或2，取值为1表示IPv4，取值为2表示IPv6。 |
| logType23+ | [LogType](js-apis-enterprise-networkmanager.md#logtype23) | 否 | 是 | 日志类型，当前仅支持配置NFLOG类型，该参数仅支持PC/2in1设备。  添加防火墙过滤规则时，此参数非必填。若填写，仅在丢弃或拒绝数据包时生效。生效后，在访问被过滤目的地址时，会记录网络数据包日志，并向上层提供可查询的日志信息，可以通过[订阅安全审计数据](devicesecurity-securityaudit-api.md#section10996135475216)获取。  移除防火墙过滤规则时，当清空某条链时非必填，不影响整条链的清空；当移除单条规则时，是否填写必须与该规则一致，否则可能导致过滤规则已经移除，但是日志还在记录的问题；相同过滤规则移除时必须按添加时的顺序移除。  获取防火墙过滤规则时，仅日志生效的场景可以获取到logType字段。 |

## DomainFilterRule

PhonePC/2in1Tablet

域名过滤规则。

API version 21及之前版本，仅支持IPv4。从API version 22开始，支持IPv4和IPv6。

从API version 23开始，支持[LogType](js-apis-enterprise-networkmanager.md#logtype23)。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| domainName | string | 否 | 是 | 域名。添加域名过滤规则时必填。支持域名分段匹配，例如，domainName传入"example.com"，那么"example.com"、"[www.example.com"、"www.test.example.com"会被匹配，"linkexample.com"不会被匹配。](http://www.example.com) |
| appUid | string | 否 | 是 | 应用uid。 |
| action | [Action](js-apis-enterprise-networkmanager.md#action) | 否 | 是 | 接收或者丢弃数据包。  添加域名过滤规则时必填；  移除域名过滤规则时非必填，当值为空时，表示清空所有的匹配[Action](js-apis-enterprise-networkmanager.md#action)规则的链，且domainName，appUid也必须传入空值。 |
| direction15+ | [Direction](js-apis-enterprise-networkmanager.md#direction) | 否 | 是 | 规则链。  添加域名过滤规则时非必填；当值设为输出链或输入链时，实际效果为输出链。设为转发链时，appUid需设置为空，否则会报401错误码。  移除域名过滤规则时非必填，当值为空时，表示清空所有的[Direction](js-apis-enterprise-networkmanager.md#direction)链，且domainName，appUid也必须传入空值。 |
| family22+ | number | 否 | 是 | IP协议版本。支持取值为1或2，取值为1表示IPv4，取值为2表示IPv6。 |
| logType23+ | [LogType](js-apis-enterprise-networkmanager.md#logtype23) | 否 | 是 | 日志类型，当前仅支持配置NFLOG类型，该参数仅支持PC/2in1设备。  添加域名过滤规则时，此参数非必填。若填写，仅在丢弃或拒绝数据包时生效。生效后，在访问被过滤域名时，会记录网络数据包日志，并向上层提供可查询的日志信息，可以通过[订阅安全审计数据](devicesecurity-securityaudit-api.md#section10996135475216)获取。  移除域名过滤规则时，当清空某条链时非必填，不影响整条链的清空；当移除单条规则时，是否填写必须与该规则一致，否则可能导致过滤规则已经移除，但是日志还在记录的问题；相同过滤规则移除时必须按添加时的顺序移除。  获取域名过滤规则时，仅日志生效的场景可以获取到logType字段。 |

## Direction

PhonePC/2in1Tablet

规则链。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INPUT | 0 | 输入链。 |
| OUTPUT | 1 | 输出链。 |
| FORWARD15+ | 2 | 转发链。 |

## Action

PhonePC/2in1Tablet

数据包的行为。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALLOW | 0 | 接收数据包。 |
| DENY | 1 | 丢弃数据包。 |
| REJECT15+ | 2 | 拒绝数据包。 |

## Protocol

PhonePC/2in1Tablet

网络协议。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 0 | 全部网络协议。 |
| TCP | 1 | 网络协议TCP。 |
| UDP | 2 | 网络协议UDP。 |
| ICMP | 3 | 网络协议ICMP。 |

## LogType23+

PhonePC/2in1Tablet

日志类型。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NFLOG | 0 | 内核Netfilter框架中的数据包日志功能。 |

## InterfaceConfig23+

PhonePC/2in1Tablet

以太网的网络接口配置。仅支持IPv4。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ipSetMode | [IpSetMode](js-apis-enterprise-networkmanager.md#ipsetmode23) | 否 | 否 | 以太网连接配置模式。 |
| ipAddress | string | 否 | 是 | 静态IP地址，地址值范围0.0.0.0到255.255.255.255（DHCP模式无需配置）。 |
| gateway | string | 否 | 是 | 网关，地址值范围0.0.0.0到255.255.255.255（DHCP模式无需配置）。 |
| netMask | string | 否 | 是 | 子网掩码，地址值范围0.0.0.0到255.255.255.255（DHCP模式无需配置）。 |
| dnsServers | string | 否 | 是 | DNS服务地址，地址值范围0.0.0.0到255.255.255.255（DHCP模式无需配置），多地址间用“,”隔开。 |

## IpSetMode23+

PhonePC/2in1Tablet

以太网连接模式。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATIC | 0 | 以太网连接静态配置网络信息，设置为该模式时，需要同步设置IP地址、子网掩码、默认网关、DNS服务器。 |
| DHCP | 1 | 以太网连接动态配置网络信息，设置为该模式时，由网络中的DHCP服务器自动分配IP地址等信息。 |
