---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicemanager-guidelines
title: 分布式设备管理开发指南
breadcrumb: 指南 > 系统 > 网络 > Distributed Service Kit（分布式管理服务） > 分布式设备管理开发指南
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:32329f36602e597f4915c8367cc3ed10ba5a25d86b11b8a9531c5e95778d7db1
---

## 分布式设备管理简介

随着用户不同种类的终端设备数量不断增多，将不同设备作为本端设备能力的扩展，使设备之间协同合作完成各种复杂场景即为设备的分布式业务。

分布式设备管理是分布式业务入口，在分布式业务中对周边可信和非可信设备进行统一管理。

分布式设备管理提供如下四大功能：

* **发现**

  发现周围终端设备并上报。周围设备需要连接同局域网或者同时打开蓝牙。
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

## 模拟器支持情况

本模块暂不支持模拟器。

## 申请分布式数据同步权限开发指导

### 场景概述

应用在使用分布式设备管理系统能力前，需要检查是否已经获取用户授权访问分布式数据同步信息。如未获得授权，可以向用户申请需要的分布式数据同步权限。

ohos.permission.DISTRIBUTED\_DATASYNC：分布式数据同步权限

使用设备管理能力，必须申请权限，并且获得用户授权。

### 开发步骤

适用于Stage应用模型。

1. 在module.json5配置文件中配置分布式数据同步权限ohos.permission.DISTRIBUTED\_DATASYNC。

   ```ts
   {
     "module" : {
       "requestPermissions":[
         {
           "name" : "ohos.permission.DISTRIBUTED_DATASYNC",
           "reason": "$string:distributed_permission",
           "usedScene": {
             "abilities": [
               "MainAbility"
             ],
             "when": "inuse"
           }
         }
       ]
     }
   }
   ```
2. 导入abilityAccessCtrl模块，用于获取权限申请的能力。

   ```ts
   import { abilityAccessCtrl } from '@kit.AbilityKit';
   ```
3. 分布式数据同步权限的授权方式为user\_grant，因此需要调用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)接口，以动态弹窗的方式向用户申请授权。

   ```typescript
   let atManager = abilityAccessCtrl.createAtManager();
   atManager.requestPermissionsFromUser(context, ['ohos.permission.DISTRIBUTED_DATASYNC'])
     .then(async (data) => {
       logger.info(`data: ${JSON.stringify(data)}`);
       // ...
     })
     .catch((err: BusinessError) => {
       logger.error(`requestPermissionsFromUser error: ${JSON.stringify(err)}`);
     });
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

   ```ts
   import { distributedDeviceManager } from '@kit.DistributedServiceKit';
   ```
3. 导入BusinessError模块，用于获取distributedDeviceManager模块相关接口抛出的错误码。

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
4. 创建设备管理实例，设备管理实例是分布式设备管理方法的调用入口。

   ```typescript
   async createDeviceManager(): Promise<void> {
     if (typeof (this.deviceManager) != 'undefined') {
       return;
     }

     logger.info('[DeviceManager.RemoteDeviceModel] deviceManager.createDeviceManager begin');
     try {
       let dmInstance = distributedDeviceManager.createDeviceManager('com.samples.devicemanager');
       this.deviceManager = dmInstance
       // ...
       logger.info(`[DeviceManager.RemoteDeviceModel] createDeviceManager callback returned,
       value= ${JSON.stringify(this.deviceManager)}`);
     } catch (err) {
       let error: BusinessError = err as BusinessError;
       logger.error(`[DeviceManager.RemoteDeviceModel] createDeviceManager throw error,
       error=${error} message=${error.message}`);
     }
     logger.info('[DeviceManager.RemoteDeviceModel] distributedDeviceManager.createDeviceManager end');
   }
   ```
5. 注册发现设备的回调，调用发现接口发现周边设备。发现状态持续两分钟，超过两分钟，会停止发现，最大发现数量99个。

   ```typescript
   startDeviceDiscovery(): void {
     if (typeof (this.deviceManager) == 'undefined') {
       logger.error('[DeviceManager.RemoteDeviceModel] deviceManager has not initialized');
       this.showErrMsg('deviceManager has not initialized');
       return;
     }
     let self = this;
     try {
       this.deviceManager.on('discoverSuccess', (data) => {
         if (data == null) {
           return;
         }
         logger.info('[DeviceManager.RemoteDeviceModel] deviceFound data=' + JSON.stringify(data));
         self.deviceFound(data);
       })
       this.deviceManager.on('discoverFailure', (data) => {
         logger.info('[DeviceManager.RemoteDeviceModel] discoverFail data=' + JSON.stringify(data));
       })
       // ...
       let discoverParam: Record<string, number> = {
         'discoverTargetType': 1
       };
       let filterOptions: Record<string, number> = this.getFilterOptions();
       logger.info('[DeviceManager.RemoteDeviceModel] startDeviceDiscovery filterOptions = ' + JSON.stringify(filterOptions));
       if (Object.entries(filterOptions).length == 0) {
         this.deviceManager.startDiscovering(discoverParam);
       } else {
         this.deviceManager.startDiscovering(discoverParam, filterOptions);
       }
     } catch (err) {
       let e: BusinessError = err as BusinessError;
       logger.error('[DeviceManager.RemoteDeviceModel] startDeviceDiscovery failed err: ' + e.toString());
     }
   }
   ```
6. 发现结束或页面退出时，调用停止发现接口释放发现监听。

   ```typescript
   stopDeviceDiscovery(): void {
     if (typeof (this.deviceManager) == 'undefined') {
       logger.error('[DeviceManager.RemoteDeviceModel] deviceManager has not initialized');
       this.showErrMsg('deviceManager has not initialized');
       return;
     }
     logger.info('[DeviceManager.RemoteDeviceModel] stopDeviceDiscovery');
     try {
       this.deviceManager.stopDiscovering();
       this.deviceManager.off('discoverSuccess');
       this.deviceManager.off('discoverFailure');
     } catch (e) {
       logger.error('[DeviceManager.RemoteDeviceModel] stopDeviceDiscovery failed err: ' + e.toString());
     }
   }
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

   ```typescript
   authenticateDevice(device: distributedDeviceManager.DeviceBasicInfo): void {
     logger.info('[DeviceManager.RemoteDeviceModel] authenticateDevice ' + JSON.stringify(device));
     if (typeof (this.deviceManager) == 'undefined') {
       logger.error('[DeviceManager.RemoteDeviceModel] deviceManager has not initialized');
       this.showErrMsg('deviceManager has not initialized');
       return;
     }

     for (let i = 0; i < this.discoverList.length; i++) {
       if (this.discoverList[i].deviceId != device.deviceId) {
         continue;
       }

       let bindParam: Record<string, number | string> = {
         'bindLevel': 3,
         'bindType': 1, // PIN码认证
         'targetPkgName': 'ohos.samples.etsdevicemanager',
         'appName': 'DeviceManager',
       };
       try {
         this.deviceManager.bindTarget(device.deviceId, bindParam, (err: BusinessError, data: Object) => {
           if (err) {
             logger.error('[DeviceManager.RemoteDeviceModel] authenticateDevice error:' + JSON.stringify(err));
             return;
           }
           logger.info('[DeviceManager.RemoteDeviceModel] authenticateDevice succeed:' + JSON.stringify(data));
         })
       } catch (err) {
         let e: BusinessError = err as BusinessError;
         logger.error('[DeviceManager.RemoteDeviceModel] authenticateDevice failed err: ' + e.toString());
       }
     }
   }
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

   ```typescript
   getTrustedDeviceList(): void {
     if (typeof (this.deviceManager) == 'undefined') {
       logger.error('[DeviceManager.RemoteDeviceModel] deviceManager has not initialized');
       this.showErrMsg('deviceManager has not initialized');
       return;
     }

     logger.info('[DeviceManager.RemoteDeviceModel] getTrustedDeviceList begin');
     try {
       this.trustedDeviceList = this.deviceManager.getAvailableDeviceListSync();
       // ...
     } catch (error) {
       logger.error('[DeviceManager.RemoteDeviceModel] getTrustedDeviceList error: ${error}' + error.toString());
       this.showErrMsg('getTrustedDeviceList failed');
     }
   }
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

   ```ts
   import { distributedDeviceManager } from '@kit.DistributedServiceKit';
   ```
3. 导入BusinessError模块，用于获取distributedDeviceManager模块相关接口抛出的错误码。

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
4. 创建设备管理实例，设备管理实例是分布式设备管理方法的调用入口，并注册设备上下线回调。

   ```typescript
   registerDeviceStateListener(): void {
     logger.info('[DeviceManager.RemoteDeviceModel] registerDeviceStateListener');
     if (typeof (this.deviceManager) == 'undefined') {
       logger.error('[DeviceManager.RemoteDeviceModel] deviceManager has not initialized');
       this.showErrMsg('deviceManager has not initialized');
       return;
     }

     // ...
     try {
       this.deviceManager.on('deviceStateChange', (data: dataType) => {
         if (data == null) {
           return;
         }
         logger.info('[DeviceManager.RemoteDeviceModel] deviceStateChange data=' + JSON.stringify(data));
         switch (data.action) {
           case distributedDeviceManager.DeviceStateChange.AVAILABLE:
             logger.info('[DeviceManager.RemoteDeviceModel] deviceStateChange ONLINE');
             // ...
             break;
           case distributedDeviceManager.DeviceStateChange.UNAVAILABLE:
             logger.info('[DeviceManager.RemoteDeviceModel] deviceStateChange OFFLINE');
             // ...
             break;
           default:
             break;
         }
       })
     } catch(err) {
       let e: BusinessError = err as BusinessError;
       logger.error('[DeviceManager.RemoteDeviceModel] deviceStateChange failed err: ' + e.toString());
     }
   }
   ```
