---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-appmanager
title: @ohos.application.appManager (appManager)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 已停止维护的接口 > @ohos.application.appManager (appManager)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:50+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:baa8f98ce524e6cbc4938a2dd9b7ae4a57c1a478f2b957d66c460f259fd243a1
---

appManager模块提供应用管理的能力，包括查询当前系统是否处于稳定性测试场景、查询当前设备是否为RAM（Random Access Memory，随机存取存储器）受限设备、获取当前应用程序可以使用的最大内存值、获取有关运行进程的信息等。

说明

本模块首批接口从API version 8 开始支持，从API version 9废弃，替换模块为[@ohos.app.ability.appManager](js-apis-app-ability-appmanager.md)。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import appManager from '@ohos.application.appManager';
```

## appManager.isRunningInStabilityTest

PhonePC/2in1TabletTVWearable

isRunningInStabilityTest(callback: AsyncCallback<boolean>): void

查询当前系统是否处于稳定性测试场景。使用callback异步回调。

说明

稳定性测试场景指为验证应用在复杂、极端或长期运行条件下的可靠性而设计的特定测试环境。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 以回调方式返回接口运行结果及当前系统是否处于稳定性测试场景，可进行错误处理或其他自定义处理。返回true表示系统处于稳定性测试场景，返回false表示系统不处于稳定性测试场景。 |

**示例：**

```
1. import appManager from '@ohos.application.appManager';

3. appManager.isRunningInStabilityTest((error, flag) => {
4. if (error && error.code !== 0) {
5. console.error(`isRunningInStabilityTest fail, error: ${JSON.stringify(error)}`);
6. } else {
7. console.info(`isRunningInStabilityTest success, the result is: ${JSON.stringify(flag)}`);
8. }
9. });
```

## appManager.isRunningInStabilityTest

PhonePC/2in1TabletTVWearable

isRunningInStabilityTest(): Promise<boolean>

查询当前系统是否处于稳定性测试场景。使用Promise异步回调。

说明

稳定性测试场景指为验证应用在复杂、极端或长期运行条件下的可靠性而设计的特定测试环境。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示系统处于稳定性测试场景；返回false表示系统不处于稳定性测试场景。 |

**示例：**

```
1. import appManager from '@ohos.application.appManager';
2. import { BusinessError } from '@ohos.base';

4. appManager.isRunningInStabilityTest().then((flag) => {
5. console.info(`The result of isRunningInStabilityTest is: ${JSON.stringify(flag)}`);
6. }).catch((error: BusinessError) => {
7. console.error(`error: ${JSON.stringify(error)}`);
8. });
```

## appManager.isRamConstrainedDevice7+

PhonePC/2in1TabletTVWearable

isRamConstrainedDevice(): Promise<boolean>

查询当前设备是否为RAM受限设备（内存资源严重受限的设备）。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前设备为RAM受限设备；返回false表示当前设备为非RAM受限设备。 |

**示例：**

```
1. import appManager from '@ohos.application.appManager';
2. import { BusinessError } from '@ohos.base';

4. appManager.isRamConstrainedDevice().then((data) => {
5. console.info(`The result of isRamConstrainedDevice is: ${JSON.stringify(data)}`);
6. }).catch((error: BusinessError) => {
7. console.error(`error: ${JSON.stringify(error)}`);
8. });
```

## appManager.isRamConstrainedDevice7+

PhonePC/2in1TabletTVWearable

isRamConstrainedDevice(callback: AsyncCallback<boolean>): void

查询当前设备是否为RAM受限设备（内存资源严重受限的设备）。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 以回调方式返回接口运行结果及当前设备是否为RAM受限设备，可进行错误处理或其他自定义处理。true：当前设备为RAM受限设备，false：当前设备为非RAM受限设备。 |

**示例：**

```
1. import appManager from '@ohos.application.appManager';

3. appManager.isRamConstrainedDevice((error, data) => {
4. if (error && error.code !== 0) {
5. console.error(`isRamConstrainedDevice fail, error: ${JSON.stringify(error)}`);
6. } else {
7. console.info(`The result of isRamConstrainedDevice is: ${JSON.stringify(data)}`);
8. }
9. });
```

## appManager.getAppMemorySize7+

PhonePC/2in1TabletTVWearable

getAppMemorySize(): Promise<number>

获取当前应用程序可以使用的最大内存（RAM）值。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回当前应用程序可以使用的最大内存（RAM）值，可根据此值进行错误处理或其他自定义处理，单位是M。 |

**示例：**

```
1. import appManager from '@ohos.application.appManager';
2. import { BusinessError } from '@ohos.base';

4. appManager.getAppMemorySize().then((data) => {
5. console.info(`The size of app memory is: ${JSON.stringify(data)}`);
6. }).catch((error: BusinessError) => {
7. console.error(`error: ${JSON.stringify(error)}`);
8. });
```

## appManager.getAppMemorySize7+

PhonePC/2in1TabletTVWearable

getAppMemorySize(callback: AsyncCallback<number>): void

获取当前应用程序可以使用的最大内存（RAM）值。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 获取当前应用程序可以使用的最大内存（RAM）值，可根据此值进行错误处理或其他自定义处理，单位是M。使用callback异步回调。 |

**示例：**

```
1. import appManager from '@ohos.application.appManager';

3. appManager.getAppMemorySize((error, data) => {
4. if (error && error.code !== 0) {
5. console.error(`getAppMemorySize fail, error: ${JSON.stringify(error)}`);
6. } else {
7. console.info(`The size of app memory is: ${JSON.stringify(data)}`);
8. }
9. });
```

## appManager.getProcessRunningInfos(deprecated)

PhonePC/2in1TabletTVWearable

getProcessRunningInfos(): Promise<Array<ProcessRunningInfo>>

获取有关运行进程的信息。使用Promise异步回调。

从 API Version 9 开始废弃，建议使用[appManager.getRunningProcessInformation](js-apis-app-ability-appmanager.md#appmanagergetrunningprocessinformation)替代。

**需要权限**：ohos.permission.GET\_RUNNING\_INFO（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ProcessRunningInfo](js-apis-inner-application-processrunninginfo.md)>> | Promise对象，返回有关运行进程的信息。 |

**示例：**

```
1. import appManager from '@ohos.application.appManager';
2. import { BusinessError } from '@ohos.base';

4. appManager.getProcessRunningInfos().then((data) => {
5. console.info(`The process running infos is: ${JSON.stringify(data)}`);
6. }).catch((error: BusinessError) => {
7. console.error(`error: ${JSON.stringify(error)}`);
8. });
```

## appManager.getProcessRunningInfos(deprecated)

PhonePC/2in1TabletTVWearable

getProcessRunningInfos(callback: AsyncCallback<Array<ProcessRunningInfo>>): void

获取有关运行进程的信息。使用callback异步回调。

从 API Version 9 开始废弃，建议使用[appManager.getRunningProcessInformation](js-apis-app-ability-appmanager.md#appmanagergetrunningprocessinformation)替代。

**需要权限**：ohos.permission.GET\_RUNNING\_INFO（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[ProcessRunningInfo](js-apis-inner-application-processrunninginfo.md)>> | 是 | 回调函数，返回有关运行进程的信息。 |

**示例：**

```
1. import appManager from '@ohos.application.appManager';

3. appManager.getProcessRunningInfos((error, data) => {
4. if (error && error.code !== 0) {
5. console.error(`getProcessRunningInfos fail, error: ${JSON.stringify(error)}`);
6. } else {
7. console.info(`getProcessRunningInfos success, data: ${JSON.stringify(data)}`);
8. }
9. });
```
