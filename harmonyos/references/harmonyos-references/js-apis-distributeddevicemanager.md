---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager
title: @ohos.distributedDeviceManager (设备管理)
breadcrumb: API参考 > 系统 > 网络 > Distributed Service Kit（分布式管理服务） > ArkTS API > @ohos.distributedDeviceManager (设备管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7212222e9e6cb27bb05a82bb87e6e9630816afc6c18f66db1f767a10de5f6934
---

本模块提供分布式设备管理能力。

应用可调用接口实现如下功能：

* 注册和解除注册设备上下线变化监听。
* 发现周边不可信设备。
* 认证和取消认证设备。
* 查询可信设备列表。
* 查询本地设备信息，包括设备名称，设备类型和设备标识等。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
```

## distributedDeviceManager.createDeviceManager

PhonePC/2in1TabletTVWearable

createDeviceManager(bundleName: string): DeviceManager

创建一个设备管理实例。设备管理实例是分布式设备管理方法的调用入口。用于获取可信设备和本地设备的相关信息。

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 指示应用程序的Bundle名称。长度范围1~255字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DeviceManager](js-apis-distributeddevicemanager.md#devicemanager) | 返回设备管理器对象实例。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
6. } catch(err) {
7. let e: BusinessError = err as BusinessError;
8. console.error('createDeviceManager errCode:' + e.code + ',errMessage:' + e.message);
9. }
```

## distributedDeviceManager.releaseDeviceManager

PhonePC/2in1TabletTVWearable

releaseDeviceManager(deviceManager: DeviceManager): void

设备管理实例不再使用后，通过该方法释放DeviceManager实例。

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceManager | [DeviceManager](js-apis-distributeddevicemanager.md#devicemanager) | 是 | 设备管理器对象实例。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[设备管理错误码](errorcode-device-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 11600101 | Failed to execute the function. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
6. distributedDeviceManager.releaseDeviceManager(dmInstance);
7. } catch (err) {
8. let e: BusinessError = err as BusinessError;
9. console.error('release device manager errCode:' + e.code + ',errMessage:' + e.message);
10. }
```

## DeviceBasicInfo

PhonePC/2in1TabletTVWearable

分布式设备基本信息。

**系统能力**：以下各项对应的系统能力均为SystemCapability.DistributedHardware.DeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 设备标识符。实际值为udid-hash与appid和盐值基于sha256方式进行混淆后的值。 |
| deviceName | string | 否 | 否 | 设备名称。 |
| deviceType | string | 否 | 否 | [设备类型](js-apis-distributeddevicemanager.md#getdevicetype)。 |
| networkId | string | 否 | 是 | 设备网络标识。 |

## DeviceStateChange

PhonePC/2in1TabletTVWearable

表示设备状态。

**系统能力**：以下各项对应的系统能力均为SystemCapability.DistributedHardware.DeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 设备物理上线，此时状态未知，在状态更改为可用之前，分布式业务无法使用。 |
| AVAILABLE | 1 | 设备可用状态，表示设备间信息已在分布式数据中同步完成，可以运行分布式业务。 |
| UNAVAILABLE | 2 | 设备物理下线，此时状态未知。 |

## DeviceManager

PhonePC/2in1TabletTVWearable

设备管理实例，用于获取可信设备和本地设备的相关信息。在调用DeviceManager的方法前，需要先通过createDeviceManager构建一个DeviceManager实例dmInstance。

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

### getAvailableDeviceListSync

PhonePC/2in1TabletTVWearable

getAvailableDeviceListSync(): Array<DeviceBasicInfo>

同步获取所有可信设备列表。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo)> | 返回可信设备列表。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[设备管理错误码](errorcode-device-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 11600101 | Failed to execute the function. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
6. let deviceInfoList: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
7. } catch (err) {
8. let e: BusinessError = err as BusinessError;
9. console.error('getAvailableDeviceListSync errCode:' + e.code + ',errMessage:' + e.message);
10. }
```

### getAvailableDeviceList

PhonePC/2in1TabletTVWearable

getAvailableDeviceList(callback:AsyncCallback<Array<DeviceBasicInfo>>): void

获取所有可信设备列表。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo)>> | 是 | 回调函数。当获取可信设备列表成功，err为undefined，data为获取到的Array<DeviceBasicInfo>；否则为错误对象。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[设备管理错误码](errorcode-device-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 11600101 | Failed to execute the function. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
6. dmInstance.getAvailableDeviceList((err: BusinessError, data: Array<distributedDeviceManager.DeviceBasicInfo>) => {
7. if (err) {
8. console.error('getAvailableDeviceList errCode:' + err.code + ',errMessage:' + err.message);
9. return;
10. }
11. console.info('get available device info: ' + JSON.stringify(data));
12. });
13. } catch (err) {
14. let e: BusinessError = err as BusinessError;
15. console.error('getAvailableDeviceList errCode:' + e.code + ',errMessage:' + e.message);
16. }
```

### getAvailableDeviceList

PhonePC/2in1TabletTVWearable

getAvailableDeviceList(): Promise<Array<DeviceBasicInfo>>

获取所有可信设备列表。使用Promise异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo)>> | Promise对象，返回分布式设备基本信息列表。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[设备管理错误码](errorcode-device-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 11600101 | Failed to execute the function. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
5. dmInstance.getAvailableDeviceList().then((data: Array<distributedDeviceManager.DeviceBasicInfo>) => {
6. console.info('get available device info: ' + JSON.stringify(data));
7. }).catch((err: BusinessError) => {
8. console.error('getAvailableDeviceList errCode:' + err.code + ',errMessage:' + err.message);
9. });
```

### getLocalDeviceNetworkId

PhonePC/2in1TabletTVWearable

getLocalDeviceNetworkId(): string

获取本地设备网络标识。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回本地设备网络标识。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[设备管理错误码](errorcode-device-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 11600101 | Failed to execute the function. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
6. let deviceNetworkId: string = dmInstance.getLocalDeviceNetworkId();
7. console.info('local device networkId: ' + JSON.stringify(deviceNetworkId));
8. } catch (err) {
9. let e: BusinessError = err as BusinessError;
10. console.error('getLocalDeviceNetworkId errCode:' + e.code + ',errMessage:' + e.message);
11. }
```

### getLocalDeviceName

PhonePC/2in1TabletTVWearable

getLocalDeviceName(): string

获取本地设备名称。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回本地设备名称。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[设备管理错误码](errorcode-device-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 11600101 | Failed to execute the function. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
6. let deviceName: string = dmInstance.getLocalDeviceName();
7. console.info('local device name: ' + JSON.stringify(deviceName));
8. } catch (err) {
9. let e: BusinessError = err as BusinessError;
10. console.error('getLocalDeviceName errCode:' + e.code + ',errMessage:' + e.message);
11. }
```

### getLocalDeviceType

PhonePC/2in1TabletTVWearable

getLocalDeviceType(): number

获取本地设备类型。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回本地设备类型。目前仅支持以下设备类型：  -0: UNKNOWN。  -14: PHONE。  -17: PAD。  -156: TV。  -131: CAR。  -109: WATCH。  -8: WiFiCamera。  -2562: SMART\_DISPLAY。  -2607: 2IN1。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[设备管理错误码](errorcode-device-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 11600101 | Failed to execute the function. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
6. let deviceType: number = dmInstance.getLocalDeviceType();
7. console.info('local device type: ' + JSON.stringify(deviceType));
8. } catch (err) {
9. let e: BusinessError = err as BusinessError;
10. console.error('getLocalDeviceType errCode:' + e.code + ',errMessage:' + e.message);
11. }
```

### getLocalDeviceId

PhonePC/2in1TabletTVWearable

getLocalDeviceId(): string

获取本地设备id，实际值为udid-hash与appid和盐值基于sha256方式进行混淆后的值。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回本地设备id。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[设备管理错误码](errorcode-device-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 11600101 | Failed to execute the function. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
6. let deviceId: string = dmInstance.getLocalDeviceId();
7. console.info('local device id: ' + JSON.stringify(deviceId));
8. } catch (err) {
9. let e: BusinessError = err as BusinessError;
10. console.error('getLocalDeviceId errCode:' + e.code + ',errMessage:' + e.message);
11. }
```

### getDeviceName

PhonePC/2in1TabletTVWearable

getDeviceName(networkId: string): string

通过指定设备的网络标识获取该设备名称。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | string | 是 | 设备的网络标识。长度范围1~255字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回指定设备名称。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[设备管理错误码](errorcode-device-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified networkId is greater than 255. |
| 11600101 | Failed to execute the function. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. // 设备网络标识，可以从可信设备列表中获取
6. let networkId = 'xxxxxxx';
7. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
8. let deviceName: string = dmInstance.getDeviceName(networkId);
9. console.info('device name: ' + JSON.stringify(deviceName));
10. } catch (err) {
11. let e: BusinessError = err as BusinessError;
12. console.error('getDeviceName errCode:' + e.code + ',errMessage:' + e.message);
13. }
```

### getDeviceType

PhonePC/2in1TabletTVWearable

getDeviceType(networkId: string): number

通过指定设备的网络标识获取该设备类型。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | string | 是 | 设备的网络标识。长度范围1~255字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回指定设备类型。目前仅支持以下设备类型：  -0: UNKNOWN。  -14: PHONE。  -17: PAD。  -156: TV。  -131: CAR。  -109: WATCH。  -8: WiFiCamera。  -2562: SMART\_DISPLAY。  -2607: 2IN1。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[设备管理错误码](errorcode-device-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified networkId is greater than 255. |
| 11600101 | Failed to execute the function. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. // 设备网络标识，可以从可信设备列表中获取
6. let networkId = 'xxxxxxx';
7. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
8. let deviceType: number = dmInstance.getDeviceType(networkId);
9. console.info('device type: ' + JSON.stringify(deviceType));
10. } catch (err) {
11. let e: BusinessError = err as BusinessError;
12. console.error('getDeviceType errCode:' + e.code + ',errMessage:' + e.message);
13. }
```

### startDiscovering

PhonePC/2in1TabletTVWearable

startDiscovering(discoverParam: {[key: string]: Object;} , filterOptions?: {[key: string]: Object;} ): void

发现周边设备。发现状态持续两分钟，超过两分钟，会停止发现，最大发现数量99个。wifi场景要求同局域网。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| discoverParam | {[key: string]: Object;} | 是 | 发现标识。 标识发现的目标类型。  discoverTargetType: 发现目标默认为设备，值为1。 |
| filterOptions | {[key: string]: Object;} | 否 | 发现设备过滤信息。可选，默认为undefined，发现未上线设备。会携带以下key值：  availableStatus(0-1)：仅发现设备可信，值为0表示设备不可信。  -0：设备离线，客户端需要通过调用bindTarget绑定设备。  -1：设备已在线，客户端可以进行连接。  discoverDistance(0-100)：发现距离本地一定距离内的设备，单位为cm。wifi场景不传该参数。  authenticationStatus(0-1)：根据不同的认证状态发现设备：  -0：设备未认证。  -1：设备已认证。  authorizationType(0-2)：根据不同的授权类型发现设备：  -0：根据临时协商的会话密钥认证的设备。  -1：基于同账号密钥进行身份验证的设备。  -2：基于不同账号凭据密钥认证的设备。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[设备管理错误码](errorcode-device-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed. |
| 11600101 | Failed to execute the function. |
| 11600104 | Discovery unavailable. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. interface DiscoverParam {
5. discoverTargetType: number;
6. }

8. interface FilterOptions {
9. availableStatus: number;
10. discoverDistance: number;
11. authenticationStatus: number;
12. authorizationType: number;
13. }

15. let discoverParam: Record<string, number> = {
16. 'discoverTargetType': 1
17. };
18. let filterOptions: Record<string, number> = {
19. 'availableStatus': 0
20. };

22. try {
23. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
24. dmInstance.startDiscovering(discoverParam, filterOptions); // 当有设备发现时，通过discoverSuccess回调通知给应用程序
25. } catch (err) {
26. let e: BusinessError = err as BusinessError;
27. console.error('startDiscovering errCode:' + e.code + ',errMessage:' + e.message);
28. }
```

### stopDiscovering

PhonePC/2in1TabletTVWearable

stopDiscovering(): void

停止发现周边设备。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[设备管理错误码](errorcode-device-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 11600101 | Failed to execute the function. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
6. dmInstance.stopDiscovering();
7. } catch (err) {
8. let e: BusinessError = err as BusinessError;
9. console.error('stopDiscovering errCode:' + e.code + ',errMessage:' + e.message);
10. }
```

### bindTarget

PhonePC/2in1TabletTVWearable

bindTarget(deviceId: string, bindParam: {[key: string]: Object;} , callback: AsyncCallback<{deviceId: string;}>): void

认证设备。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 设备标识。长度范围1~255字符。 |
| bindParam | {[key: string]: Object;} | 是 | 认证参数。由开发者自行决定传入的键值对。默认会携带以下key值：  bindType 此值是绑定的类型，必填。  -1：PIN码。  targetPkgName 绑定目标的包名。  appName 尝试绑定目标的应用程序名称。  appOperation 应用程序要绑定目标的原因。  customDescription 操作的详细说明。 |
| callback | AsyncCallback<{deviceId: string; }> | 是 | 认证结果回调。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[设备管理错误码](errorcode-device-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified deviceId is greater than 255. |
| 11600101 | Failed to execute the function. |
| 11600103 | Authentication unavailable. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class Data {
5. deviceId: string = '';
6. }

8. // 认证的设备信息，可以从发现的结果中获取
9. let deviceId = 'XXXXXXXX';
10. let bindParam: Record<string, string | number> = {
11. 'bindType': 1, // 认证类型： 1 - 无账号PIN码认证
12. 'targetPkgName': 'xxxx',
13. 'appName': 'xxxx',
14. 'appOperation': 'xxxx',
15. 'customDescription': 'xxxx'
16. };

18. try {
19. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
20. dmInstance.bindTarget(deviceId, bindParam, (err: BusinessError, data: Data) => {
21. if (err) {
22. console.error('bindTarget errCode:' + err.code + ',errMessage:' + err.message);
23. return;
24. }
25. console.info('bindTarget result:' + JSON.stringify(data));
26. });
27. } catch (err) {
28. let e: BusinessError = err as BusinessError;
29. console.error('bindTarget errCode:' + e.code + ',errMessage:' + e.message);
30. }
```

### unbindTarget

PhonePC/2in1TabletTVWearable

unbindTarget(deviceId: string): void

解除认证设备。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 设备标识。长度范围1~255字符。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[设备管理错误码](errorcode-device-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified deviceId is greater than 255. |
| 11600101 | Failed to execute the function. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let deviceId = 'XXXXXXXX';
6. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
7. dmInstance.unbindTarget(deviceId);
8. } catch (err) {
9. let e: BusinessError = err as BusinessError;
10. console.error('unbindTarget errCode:' + e.code + ',errMessage:' + e.message);
11. }
```

### on('deviceStateChange')

PhonePC/2in1TabletTVWearable

on(type: 'deviceStateChange', callback: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>): void

注册设备状态回调，以便在设备状态发生变化时根据应用捆绑包名通知应用。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册设备状态回调，固定为deviceStateChange。 |
| callback | Callback<{ action: [DeviceStateChange](js-apis-distributeddevicemanager.md#devicestatechange); device: [DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo); }> | 是 | 指示要注册的设备状态回调，返回设备状态和设备信息。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class Data {
5. action: distributedDeviceManager.DeviceStateChange = 0;
6. device: distributedDeviceManager.DeviceBasicInfo = {
7. deviceId: '',
8. deviceName: '',
9. deviceType: '',
10. networkId: ''
11. };
12. }

14. try {
15. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
16. dmInstance.on('deviceStateChange', (data: Data) => {
17. console.info('deviceStateChange on:' + JSON.stringify(data));
18. });
19. } catch (err) {
20. let e: BusinessError = err as BusinessError;
21. console.error('deviceStateChange errCode:' + e.code + ',errMessage:' + e.message);
22. }
```

### off('deviceStateChange')

PhonePC/2in1TabletTVWearable

off(type: 'deviceStateChange', callback?: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>): void

取消注册设备状态回调。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 根据应用程序的包名取消注册设备状态回调，固定为deviceStateChange。 |
| callback | Callback<{ action: [DeviceStateChange](js-apis-distributeddevicemanager.md#devicestatechange); device: [DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo); }> | 否 | 指示要取消注册的设备状态回调，返回设备状态和设备信息。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class Data {
5. action: distributedDeviceManager.DeviceStateChange = 0;
6. device: distributedDeviceManager.DeviceBasicInfo = {
7. deviceId: '',
8. deviceName: '',
9. deviceType: '',
10. networkId: ''
11. };
12. }

14. try {
15. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
16. dmInstance.off('deviceStateChange', (data: Data) => {
17. console.info('deviceStateChange' + JSON.stringify(data));
18. });
19. } catch (err) {
20. let e: BusinessError = err as BusinessError;
21. console.error('deviceStateChange errCode:' + e.code + ',errMessage:' + e.message);
22. }
```

### on('discoverSuccess')

PhonePC/2in1TabletTVWearable

on(type: 'discoverSuccess', callback: Callback<{ device: DeviceBasicInfo; }>): void

注册发现设备成功回调监听。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册设备发现回调，以便在发现周边设备时通知应用程序，固定为discoverSuccess。 |
| callback | Callback<{ device: [DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo); }> | 是 | 注册设备发现的回调方法。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class Data {
5. device: distributedDeviceManager.DeviceBasicInfo = {
6. deviceId: '',
7. deviceName: '',
8. deviceType: '',
9. networkId: ''
10. };
11. }

13. try {
14. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
15. dmInstance.on('discoverSuccess', (data: Data) => {
16. console.info('discoverSuccess:' + JSON.stringify(data));
17. });
18. } catch (err) {
19. let e: BusinessError = err as BusinessError;
20. console.error('discoverSuccess errCode:' + e.code + ',errMessage:' + e.message);
21. }
```

### off('discoverSuccess')

PhonePC/2in1TabletTVWearable

off(type: 'discoverSuccess', callback?: Callback<{ device: DeviceBasicInfo; }>): void

取消注册设备发现成功回调。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消注册设备发现回调，固定为discoverSuccess。 |
| callback | Callback<{ device: [DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo); }> | 否 | 指示要取消注册的设备发现回调，返回设备状态和设备信息。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class Data {
5. device: distributedDeviceManager.DeviceBasicInfo = {
6. deviceId: '',
7. deviceName: '',
8. deviceType: '',
9. networkId: ''
10. };
11. }

13. try {
14. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
15. dmInstance.off('discoverSuccess', (data: Data) => {
16. console.info('discoverSuccess' + JSON.stringify(data));
17. });
18. } catch (err) {
19. let e: BusinessError = err as BusinessError;
20. console.error('discoverSuccess errCode:' + e.code + ',errMessage:' + e.message);
21. }
```

### on('deviceNameChange')

PhonePC/2in1TabletTVWearable

on(type: 'deviceNameChange', callback: Callback<{ deviceName: string; }>): void

注册设备名称变更回调，以便在设备名称改变时通知应用程序。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册设备名称改变回调，以便在设备名称改变时通知应用程序，固定为deviceNameChange。 |
| callback | Callback<{ deviceName: string;}> | 是 | 注册设备名称改变的回调方法。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class Data {
5. deviceName: string = '';
6. }

8. try {
9. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
10. dmInstance.on('deviceNameChange', (data: Data) => {
11. console.info('deviceNameChange on:' + JSON.stringify(data));
12. });
13. } catch (err) {
14. let e: BusinessError = err as BusinessError;
15. console.error('deviceNameChange errCode:' + e.code + ',errMessage:' + e.message);
16. }
```

### off('deviceNameChange')

PhonePC/2in1TabletTVWearable

off(type: 'deviceNameChange', callback?: Callback<{ deviceName: string; }>): void

取消注册设备名称变更回调监听。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消注册设备名称改变回调，固定为deviceNameChange。 |
| callback | Callback<{ deviceName: string;}> | 否 | 指示要取消注册设备名称改变的回调方法。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class Data {
5. deviceName: string = '';
6. }

8. try {
9. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
10. dmInstance.off('deviceNameChange', (data: Data) => {
11. console.info('deviceNameChange' + JSON.stringify(data));
12. });
13. } catch (err) {
14. let e: BusinessError = err as BusinessError;
15. console.error('deviceNameChange errCode:' + e.code + ',errMessage:' + e.message);
16. }
```

### on('discoverFailure')

PhonePC/2in1TabletTVWearable

on(type: 'discoverFailure', callback: Callback<{ reason: number; }>): void

注册设备发现失败回调监听。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册设备发现失败回调，以便在发现周边设备失败时通知应用程序，固定为discoverFailure。 |
| callback | Callback<{ reason: number; }> | 是 | 注册设备发现失败的回调方法。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class Data {
5. reason: number = 0;
6. }

8. try {
9. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
10. dmInstance.on('discoverFailure', (data: Data) => {
11. console.info('discoverFailure on:' + JSON.stringify(data));
12. });
13. } catch (err) {
14. let e: BusinessError = err as BusinessError;
15. console.error('discoverFailure errCode:' + e.code + ',errMessage:' + e.message);
16. }
```

### off('discoverFailure')

PhonePC/2in1TabletTVWearable

off(type: 'discoverFailure', callback?: Callback<{ reason: number; }>): void

取消注册设备发现失败回调。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消注册设备发现失败回调，固定为discoverFailure。 |
| callback | Callback<{ reason: number; }> | 否 | 指示要取消注册的设备发现失败回调。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class Data {
5. reason: number = 0;
6. }

8. try {
9. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
10. dmInstance.off('discoverFailure', (data: Data) => {
11. console.info('discoverFailure' + JSON.stringify(data));
12. });
13. } catch (err) {
14. let e: BusinessError = err as BusinessError;
15. console.error('discoverFailure errCode:' + e.code + ',errMessage:' + e.message);
16. }
```

### on('serviceDie')

PhonePC/2in1TabletTVWearable

on(type: 'serviceDie', callback?: Callback<{}>): void

注册设备管理服务死亡回调，以便在服务死亡时通知应用程序。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册serviceDie回调，以便在devicemanager服务异常终止时通知应用程序，固定为serviceDie。 |
| callback | Callback<{}> | 否 | 注册serviceDie的回调方法。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
6. dmInstance.on('serviceDie', () => {
7. console.info('serviceDie on');
8. });
9. } catch (err) {
10. let e: BusinessError = err as BusinessError;
11. console.error('serviceDie errCode:' + e.code + ',errMessage:' + e.message);
12. }
```

### off('serviceDie')

PhonePC/2in1TabletTVWearable

off(type: 'serviceDie', callback?: Callback<{}>): void

取消注册设备管理服务死亡回调。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消注册serviceDie回调，以便在devicemanager服务异常终止时通知应用程序，固定为serviceDie。 |
| callback | Callback<{}> | 否 | 取消注册serviceDie的回调方法。 |

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
6. dmInstance.off('serviceDie', () => {
7. console.info('serviceDie off');
8. });
9. } catch (err) {
10. let e: BusinessError = err as BusinessError;
11. console.error('serviceDie errCode:' + e.code + ',errMessage:' + e.message);
12. }
```
