---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicemanager-guidelines
title: 分布式设备管理开发指南
breadcrumb: 指南 > 系统 > 网络 > Distributed Service Kit（分布式管理服务） > 分布式设备管理开发指南
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:45+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:10fbe24318fb483cd0dd2f1fe1478558e8f220fa0b9be47c7e7fef32c4d1f95d
---

## 分布式设备管理简介

随着用户不同种类的终端设备数量不断增多，将不同设备作为本端设备能力的扩展，使设备之间协同合作完成各种复杂场景即为设备的分布式业务。

分布式设备管理是分布式业务入口，在分布式业务中对周边可信和非可信设备进行统一管理。

分布式设备管理提供如下四大功能：

* **发现**

  发现周围终端设备并上报。周围设备需要连接同局域网或者同时打开蓝牙，可以根据设备类型、距离、设备是否可信等进行筛选。
* **绑定**

  不同设备协同合作完成分布式业务的前提是设备间可信，对于周边发现的不可信设备，可通过绑定使彼此建立可信关系，提供PIN码、碰、扫、靠等设备认证框架，支持对接各种认证交互接口。
* **查询**

  查询功能包含：查询本机设备信息、查询周围的在线的可信设备、查询可信设备信息。
* **监听**

  监听设备上、下线。设备上线表示设备间已经可信，业务可以发起分布式操作；设备下线表示分布式业务不可用。

### 运作机制

设备管理作为分布式业务入口，需要应用在所使用的业务场景，向发现设备主动发起绑定建立可信关系；业务结束后由业务自主判断是否解除绑定关系，设备间可信关系的解除由业务自己控制。

### 约束与限制

使用设备管理能力，需要用户确认不同设备已连接同一局域网或者蓝牙开关已开启，否则该能力不可用。

设备信息属于用户敏感数据，所以即使用户已连接同一局域网或者蓝牙开关已开启，应用在获取设备位置前仍需向用户申请数据同步权限。在用户确认允许后，系统才会向应用提供设备管理能力。

## 申请分布式数据同步权限开发指导

### 场景概述

应用在使用分布式设备管理系统能力前，需要检查是否已经获取用户授权访问分布式数据同步信息。如未获得授权，可以向用户申请需要的分布式数据同步权限。

ohos.permission.DISTRIBUTED\_DATASYNC：分布式数据同步权限

使用设备管理能力，必须申请权限，并且获得用户授权。

### 开发步骤

适用于Stage应用模型。

1. 在module.json5配置文件中配置分布式数据同步权限ohos.permission.DISTRIBUTED\_DATASYNC。

   ```
   1. {
   2. "module" : {
   3. "requestPermissions":[
   4. {
   5. "name" : "ohos.permission.DISTRIBUTED_DATASYNC",
   6. "reason": "$string:distributed_permission",
   7. "usedScene": {
   8. "abilities": [
   9. "MainAbility"
   10. ],
   11. "when": "inuse"
   12. }
   13. }
   14. ]
   15. }
   16. }
   ```
2. 导入abilityAccessCtrl模块，用于获取权限申请的能力。

   ```
   1. import { abilityAccessCtrl } from '@kit.AbilityKit';
   ```
3. 分布式数据同步权限的授权方式为user\_grant，因此需要调用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)接口，以动态弹窗的方式向用户申请授权。

   ```
   1. let atManager = abilityAccessCtrl.createAtManager();
   2. atManager.requestPermissionsFromUser(context, ['ohos.permission.DISTRIBUTED_DATASYNC'])
   3. .then(async (data) => {
   4. logger.info(`data: ${JSON.stringify(data)}`);
   5. // ...
   6. })
   7. .catch((err: BusinessError) => {
   8. logger.error(`requestPermissionsFromUser error: ${JSON.stringify(err)}`);
   9. });
   ```

## 设备发现开发指导

### 场景概述

开发者可以调用设备发现相关接口，获取周边可用的设备。

### 接口说明

startDiscovering(discoverParam: {[key: string]: Object;} , filterOptions?: {[key: string]: Object;} ): void;

发现周边同局域网或者开启蓝牙的设备。详细信息参见：[startDiscovering](../harmonyos-references/js-apis-distributeddevicemanager.md#startdiscovering)。

### 开发步骤

1. 申请分布式数据同步权限。
2. 导入distributedDeviceManager模块，所有与设备管理相关的功能API，都是通过该模块提供的。

   ```
   1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
   ```
3. 导入BusinessError模块，用于获取distributedDeviceManager模块相关接口抛出的错误码。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   ```
4. 创建设备管理实例，设备管理实例是分布式设备管理方法的调用入口。

   ```
   1. async createDeviceManager(): Promise<void> {
   2. if (typeof (this.deviceManager) != 'undefined') {
   3. return;
   4. }

   6. logger.info('[DeviceManager.RemoteDeviceModel] deviceManager.createDeviceManager begin');
   7. try {
   8. let dmInstance = distributedDeviceManager.createDeviceManager('com.samples.devicemanager');
   9. this.deviceManager = dmInstance
   10. // ...
   11. logger.info(`[DeviceManager.RemoteDeviceModel] createDeviceManager callback returned,
   12. value= ${JSON.stringify(this.deviceManager)}`);
   13. } catch (err) {
   14. let error: BusinessError = err as BusinessError;
   15. logger.error(`[DeviceManager.RemoteDeviceModel] createDeviceManager throw error,
   16. error=${error} message=${error.message}`);
   17. }
   18. logger.info('[DeviceManager.RemoteDeviceModel] distributedDeviceManager.createDeviceManager end');
   19. }
   ```
5. 注册发现设备的回调，调用发现接口发现周边设备。发现状态持续两分钟，超过两分钟，会停止发现，最大发现数量99个。

   ```
   1. startDeviceDiscovery(): void {
   2. if (typeof (this.deviceManager) == 'undefined') {
   3. logger.error('[DeviceManager.RemoteDeviceModel] deviceManager has not initialized');
   4. this.showErrMsg('deviceManager has not initialized');
   5. return;
   6. }
   7. let self = this;
   8. try {
   9. this.deviceManager.on('discoverSuccess', (data) => {
   10. if (data == null) {
   11. return;
   12. }
   13. logger.info('[DeviceManager.RemoteDeviceModel] deviceFound data=' + JSON.stringify(data));
   14. self.deviceFound(data);
   15. })
   16. this.deviceManager.on('discoverFailure', (data) => {
   17. logger.info('[DeviceManager.RemoteDeviceModel] discoverFail data=' + JSON.stringify(data));
   18. })
   19. // ...
   20. let discoverParam: Record<string, number> = {
   21. 'discoverTargetType': 1
   22. };
   23. let filterOptions: Record<string, number> = this.getFilterOptions();
   24. logger.info('[DeviceManager.RemoteDeviceModel] startDeviceDiscovery filterOptions = ' + JSON.stringify(filterOptions));
   25. if (Object.entries(filterOptions).length == 0) {
   26. this.deviceManager.startDiscovering(discoverParam);
   27. } else {
   28. this.deviceManager.startDiscovering(discoverParam, filterOptions);
   29. }
   30. } catch (err) {
   31. let e: BusinessError = err as BusinessError;
   32. logger.error('[DeviceManager.RemoteDeviceModel] startDeviceDiscovery failed err: ' + e.toString());
   33. }
   34. }
   ```

## 设备绑定开发指导

### 场景概述

开发者发现周边不可信设备后，通过绑定接口建立可信关系。

### 接口说明

bindTarget(deviceId: string, bindParam: {[key: string]: Object;} , callback: AsyncCallback<{deviceId: string;}>): void;

设备绑定。详细信息参见：[bindTarget](../harmonyos-references/js-apis-distributeddevicemanager.md#bindtarget)。

### 开发步骤

1. 申请分布式数据同步权限。
2. 发现周边不可信设备。
3. 选择不可信设备id，发起设备绑定。

   ```
   1. authenticateDevice(device: distributedDeviceManager.DeviceBasicInfo): void {
   2. logger.info('[DeviceManager.RemoteDeviceModel] authenticateDevice ' + JSON.stringify(device));
   3. if (typeof (this.deviceManager) == 'undefined') {
   4. logger.error('[DeviceManager.RemoteDeviceModel] deviceManager has not initialized');
   5. this.showErrMsg('deviceManager has not initialized');
   6. return;
   7. }

   9. for (let i = 0; i < this.discoverList.length; i++) {
   10. if (this.discoverList[i].deviceId != device.deviceId) {
   11. continue;
   12. }

   14. let bindParam: Record<string, number | string> = {
   15. 'bindLevel': 3,
   16. 'bindType': 1, // PIN码认证
   17. 'targetPkgName': 'ohos.samples.etsdevicemanager',
   18. 'appName': 'DeviceManager',
   19. };
   20. try {
   21. this.deviceManager.bindTarget(device.deviceId, bindParam, (err: BusinessError, data: Object) => {
   22. if (err) {
   23. logger.error('[DeviceManager.RemoteDeviceModel] authenticateDevice error:' + JSON.stringify(err));
   24. return;
   25. }
   26. logger.info('[DeviceManager.RemoteDeviceModel] authenticateDevice succeed:' + JSON.stringify(data));
   27. })
   28. } catch (err) {
   29. let e: BusinessError = err as BusinessError;
   30. logger.error('[DeviceManager.RemoteDeviceModel] authenticateDevice failed err: ' + e.toString());
   31. }
   32. }
   33. }
   ```

## 设备信息查询开发指导

### 场景概述

设备与周边设备建立可信关系后，通过设备信息查询接口可以获取所有上线并且可信的设备。

### 接口说明

getAvailableDeviceListSync(): Array<DeviceBasicInfo>;

设备信息查询。详细信息参见：[getAvailableDeviceListSync](../harmonyos-references/js-apis-distributeddevicemanager.md#getavailabledevicelistsync)。

### 开发步骤

1. 申请分布式数据同步权限。
2. 发现周边不可信设备。
3. 建立设备间的可信关系。
4. 查询周围上线并且可信的设备。

   ```
   1. getTrustedDeviceList(): void {
   2. if (typeof (this.deviceManager) == 'undefined') {
   3. logger.error('[DeviceManager.RemoteDeviceModel] deviceManager has not initialized');
   4. this.showErrMsg('deviceManager has not initialized');
   5. return;
   6. }

   8. logger.info('[DeviceManager.RemoteDeviceModel] getTrustedDeviceList begin');
   9. try {
   10. this.trustedDeviceList = this.deviceManager.getAvailableDeviceListSync();
   11. // ...
   12. } catch (error) {
   13. logger.error('[DeviceManager.RemoteDeviceModel] getTrustedDeviceList error: ${error}' + error.toString());
   14. this.showErrMsg('getTrustedDeviceList failed');
   15. }
   16. }
   ```

## 设备上下线监听开发指导

### 场景概述

周边可信设备可用后会给业务报上线通知，当设备不可用时会给业务报下线通知。

### 接口说明

on(type: 'deviceStateChange', callback: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>): void;

设备上下线监听。详细信息参见：[on('deviceStateChange')](../harmonyos-references/js-apis-distributeddevicemanager.md#ondevicestatechange)。

### 开发步骤

1. 申请分布式数据同步权限。
2. 导入distributedDeviceManager模块，所有与设备管理相关的功能API，都是通过该模块提供的。

   ```
   1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
   ```
3. 导入BusinessError模块，用于获取distributedDeviceManager模块相关接口抛出的错误码。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   ```
4. 创建设备管理实例，设备管理实例是分布式设备管理方法的调用入口，并注册设备上下线回调。

   ```
   1. registerDeviceStateListener(): void {
   2. logger.info('[DeviceManager.RemoteDeviceModel] registerDeviceStateListener');
   3. if (typeof (this.deviceManager) == 'undefined') {
   4. logger.error('[DeviceManager.RemoteDeviceModel] deviceManager has not initialized');
   5. this.showErrMsg('deviceManager has not initialized');
   6. return;
   7. }

   9. // ...
   10. try {
   11. this.deviceManager.on('deviceStateChange', (data: dataType) => {
   12. if (data == null) {
   13. return;
   14. }
   15. logger.info('[DeviceManager.RemoteDeviceModel] deviceStateChange data=' + JSON.stringify(data));
   16. switch (data.action) {
   17. case distributedDeviceManager.DeviceStateChange.AVAILABLE:
   18. logger.info('[DeviceManager.RemoteDeviceModel] deviceStateChange ONLINE');
   19. // ...
   20. break;
   21. case distributedDeviceManager.DeviceStateChange.UNAVAILABLE:
   22. logger.info('[DeviceManager.RemoteDeviceModel] deviceStateChange OFFLINE');
   23. // ...
   24. break;
   25. default:
   26. break;
   27. }
   28. })
   29. } catch(err) {
   30. let e: BusinessError = err as BusinessError;
   31. logger.error('[DeviceManager.RemoteDeviceModel] deviceStateChange failed err: ' + e.toString());
   32. }
   33. }
   ```
