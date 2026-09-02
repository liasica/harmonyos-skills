---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/p2p_communication
title: 应用间消息通信
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 手机侧应用开发 > 应用开发 > 应用间消息通信
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:38+08:00
doc_updated_at: 2026-08-24
content_hash: sha256:f1fd213533bb9d6b9861291e6076073d62388a9bebfed477ae07c9ab96f0dc65
---

在手机侧与穿戴设备侧构建应用到应用的通信隧道，用于收发应用自定义的报文消息以及文件。实现手机应用和穿戴设备应用间的交互，为用户提供分布式场景和体验。比如手机应用发送音频文件到穿戴设备侧应用，实现在穿戴设备侧应用上播放音乐；手机应用发送暂停指令，实现穿戴设备音乐播放暂停等。

收发点对点消息前，需要确保应用已在开发者联盟申请获取设备基础信息权限（参见[申请接入Wear Engine服务](wearengine_apply.md)），否则接口将调用失败。

**说明** 

* 使用该功能前，请确保穿戴设备支持应用安装能力（参见[目标设备选择](we-device-selection.md#根据设备支持的device能力集挑选目标设备)），同时穿戴设备侧已有对应的应用（参见[穿戴侧应用开发](watch_query_connected_devices.md)）。
* 手机App和穿戴设备App必须同时处于启动状态。
* 当手机App启动且穿戴设备App没有启动时，手机App可以通过[startRemoteApp](../harmonyos-references/wearengine_api.md#startremoteapp)方法拉起穿戴设备App。

## 手机侧应用检测穿戴设备侧应用是否安装

**说明** 

该接口的调用需要在开发者联盟申请设备基础信息权限（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
4. 调用[isRemoteAppInstalled](../harmonyos-references/wearengine_api.md#isremoteappinstalled)方法，查看是否安装指定的设备应用。

   ```typescript
   // 将设备侧应用包名定义为remoteBundleName
   let remoteBundleName: string = '';

   // 步骤3 获取P2pClient对象
   let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   // 步骤4 查看是否安装指定的设备侧应用
   p2pClient.isRemoteAppInstalled(targetDevice.randomId, remoteBundleName).then((isInstall) => {
     console.info(`Succeeded in checking remote app install, result is ${isInstall}.`);
   }).catch((error: BusinessError) => {
     console.error(`Failed to check remote app install. Code is ${error.code}, message is ${error.message}.`);
   });
   ```

## 手机侧应用获取穿戴设备侧应用的版本号

**说明** 

该接口的调用需要在开发者联盟申请设备基础信息权限（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
4. 调用[getRemoteAppVersion](../harmonyos-references/wearengine_api.md#getremoteappversion)方法，获取指定设备对应的应用版本号。

   ```typescript
   // 将设备侧应用包名定义为remoteBundleName
   let remoteBundleName: string = '';

   // 步骤3 获取P2pClient对象
   let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   // 步骤4 获取指定设备对应的应用版本号
   p2pClient.getRemoteAppVersion(targetDevice.randomId, remoteBundleName).then((version) => {
     console.info(`Succeeded in getting remote app version, version is ${version}.`);
   }).catch((error: BusinessError) => {
     console.error(`Failed to check get remote app version. Code is ${error.code}, message is ${error.message}.`);
   });
   ```

## 手机侧应用拉起设备侧应用

**说明** 

该接口的调用需要在开发者联盟申请设备基础信息权限（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

在发送点对点消息前，可以用[startRemoteApp](../harmonyos-references/wearengine_api.md#startremoteapp)方法拉起设备侧应用。

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
4. 调用[startRemoteApp](../harmonyos-references/wearengine_api.md#startremoteapp)方法，指定需要拉起设备侧应用包名。[transformLocalBundleName](../harmonyos-references/wearengine_api.md#startremoteapp)默认值为false，传入为true时，wearEngine会将本地的应用包名和指纹转换为兼容应用在云侧存储的包名和指纹，可参考[申请接入Wear Engine服务](wearengine_apply.md)章节。

   ```typescript
   // 将设备侧应用包名定义为remoteBundleName
   let remoteBundleName: string = '';

   // 步骤3 获取P2pClient对象
   let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
     
   // 步骤4 拉起设备侧指定应用(transformLocalBundleName不传入参数，默认为false)
   p2pClient.startRemoteApp(targetDevice.randomId, remoteBundleName).then((p2pResult) => {
     console.info(`Succeeded in starting remote app, result is ${p2pResult.code}.`);
   }).catch((error: BusinessError) => {
     console.error(`Failed to start remote app. Code is ${error.code}, message is ${error.message}.`);
   });
   ```

## 手机侧应用发送点对点消息或文件到穿戴设备侧应用

**说明** 

该接口的调用需要在开发者联盟申请设备基础信息权限（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

该接口的调用需要在AppGallery Connect平台获取指纹（请参考[获取指纹信息](wearengine_faq-9.md#harmonyos-50及之后版本设备的应用)）。

消息长度大小的限制为4096字节。针对消息长度超过限制的情况可以采用发送文件（文件大小不超过100MB）的方式或进行消息分包控制。

手机侧实现发送消息和文件功能后，穿戴设备侧应用需要对应实现接收消息和文件的功能。

### 发送点对点消息

为了使用工具类构造消息体，请先导入所需模块。

```typescript
import { util } from '@kit.ArkTS';
```

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 构造设备侧应用参数[P2pAppParam](../harmonyos-references/wearengine_api.md#p2pappparam)。
4. 构造需要发送的消息[P2pMessage](../harmonyos-references/wearengine_api.md#p2pmessage)。
5. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
6. 调用[sendMessage](../harmonyos-references/wearengine_api.md#sendmessage)方法，从手机上的应用发送简短消息到穿戴设备侧对应的应用。设备侧已注册监听消息接收后，即可收到手机发送的消息。

   ```typescript
   // 步骤3 构造设备侧应用参数
   let appInfo: wearEngine.AppInfo = {
     // 设置设备侧应用的应用信息：包名与指纹
     bundleName: '',
     fingerprint: ''
   };
   let appParam: wearEngine.P2pAppParam = {
     remoteApp: appInfo
     // transformLocalAppInfo默认为false，不转换包名指纹
   };

   // 设置需要发送的消息内容，长度限制为4096字节
   let messageContent: string = 'this is message';

   // 步骤4 构造消息结构体
   let textEncoder: util.TextEncoder = new util.TextEncoder;
   let message: wearEngine.P2pMessage = {
     content: textEncoder.encodeInto(messageContent)
   };

   // 步骤5 获取P2pClient对象
   let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   // 步骤6 发送消息
   p2pClient.sendMessage(targetDevice.randomId, appParam, message).then((p2pResult) => {
     console.info(`Succeeded in sending message, result is ${p2pResult.code}.`);
   }).catch((error: BusinessError) => {
     console.error(`Failed to send message. Code is ${error.code}, message is ${error.message}.`);
   });
   ```

### 发送文件

为能正确打开文件描述符，请先导入模块。

```typescript
import { fileIo } from '@kit.CoreFileKit';
```

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 构造设备侧应用参数[P2pAppParam](../harmonyos-references/wearengine_api.md#p2pappparam)。
4. 根据文件路径filePath，构造需要发送的文件[P2pFile](../harmonyos-references/wearengine_api.md#p2pfile)。
5. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
6. 调用[transferFile](../harmonyos-references/wearengine_api.md#transferfile)方法，从手机上的应用发送文件到穿戴设备侧对应的应用。

   ```typescript
   // 步骤3 构造设备侧应用参数
   let appInfo: wearEngine.AppInfo = {
     // 设置设备侧应用的应用信息：包名与指纹
     bundleName: '',
     fingerprint: ''
   };
   let appParam: wearEngine.P2pAppParam = {
     remoteApp: appInfo
     // transformLocalAppInfo默认为false，不转换包名指纹
   };

   try {
     // 步骤4 构造需要发送的文件
     let p2pfile: wearEngine.P2pFile = {
       // 设置需要发送的文件路径，其中不能包含'..'
       file: fileIo.openSync('');
     };
   } catch (error) {
       console.error(`Failed to operation file. Code is ${error.code}, message is ${error.message}.`);
   };

   // 步骤5 获取P2pClient对象
   let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   // 步骤6 发送指定文件至设备
   p2pClient.transferFile(targetDevice.randomId, appParam, p2pfile,
     (error: BusinessError, p2pResult: wearEngine.P2pResult) => {
     // callback处理逻辑
     if (error) {
       console.error(`Failed to transfer file. Code is ${error.code}, message is ${error.message}.`);
       return;
     }
     if (p2pResult.code) {
       if (p2pResult.code === wearEngine.P2pResultCode.COMMUNICATION_SUCCESS) {
         console.info(`Succeeded in transferring file, the result is ${p2pResult.code}.`);
       } else {
         console.info(`Failed to transfer file, the error code is ${p2pResult.code}.`);
         return;
       }
     }
     if (p2pResult.progress) {
       console.info(`Succeeded in transferring file, the progress is ${p2pResult.progress}.`);
     }
   });

   try {
     fileIo.close(p2pfile.file);
   } catch (error) {
     console.error(`Failed to close file. Code is ${error.code}, message is ${error.message}.`);
   };
   ```

### 取消发送文件

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 构造设备侧应用参数[P2pAppParam](../harmonyos-references/wearengine_api.md#p2pappparam)。
4. 根据文件路径filePath，构造需要取消发送的文件[P2pFile](../harmonyos-references/wearengine_api.md#p2pfile)。
5. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
6. 调用[cancelFileTransfer](../harmonyos-references/wearengine_api.md#cancelfiletransfer)方法，取消从手机上的应用到穿戴设备侧对应的应用的文件发送。

   ```typescript
   // 步骤3 构造设备侧应用参数
   let appInfo: wearEngine.AppInfo = {
     // 设置设备侧应用的应用信息：包名与指纹
     bundleName: '',
     fingerprint: ''
   };
   let appParam: wearEngine.P2pAppParam = {
     remoteApp: appInfo
     // transformLocalAppInfo默认为false，不转换包名指纹
   };

   try {
     // 步骤4 构造需要发送的文件
     let p2pfile: wearEngine.P2pFile = {
     // 设置需要发送的文件路径，其中不能包含'..'
     file: fileIo.openSync('')
    };
   } catch (error) {
       console.error(`Failed to operation file. Code is ${error.code}, message is ${error.message}.`);
   };

   // 步骤5 获取P2pClient对象
   let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   // 发送指定文件至设备
   p2pClient.transferFile(targetDevice.randomId, appParam, p2pfile, () => {
     // 回调函数执行逻辑
   });

   // 步骤6 取消发送文件
   p2pClient.cancelFileTransfer(targetDevice.randomId, appParam, p2pfile).then((p2pResult) => {
     if (p2pResult.code === wearEngine.P2pResultCode.COMMUNICATION_SUCCESS) {
       console.info(`Succeeded in cancelling transfer file, the result is ${p2pResult.code}.`);
     }
   }).catch((error: BusinessError) => {
     console.error(`Failed to cancel transfer file. Code is ${error.code}, message is ${error.message}.`);
   });

   try {
     fileIo.close(p2pfile.file);
   } catch (error) {
     console.error(`Failed to close file. Code is ${error.code}, message is ${error.message}.`);
   };
   ```

## 订阅接收穿戴设备侧应用发过来的消息

**说明** 

该接口的调用需要在开发者联盟申请设备基础信息权限（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

该接口的调用需要在AppGallery Connect平台获取指纹（请参考[获取指纹信息](wearengine_faq-9.md#harmonyos-50及之后版本设备的应用)）。

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
4. 构造设备侧应用参数[P2pAppParam](../harmonyos-references/wearengine_api.md#p2pappparam)。
5. 构造接收到设备侧传来消息后的回调函数[Callback](../harmonyos-references/js-apis-base.md#callback)。
6. 调用[registerMessageReceiver](../harmonyos-references/wearengine_api.md#registermessagereceiver)方法，订阅监听消息接收事件。

   ```typescript
   // 步骤3 获取P2pClient对象
   let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   // 步骤4 构造设备侧应用参数
   let appInfo: wearEngine.AppInfo = {
     bundleName: '',
     fingerprint: ''
   };
   // 将设备侧应用参数类定义为appParam
   let appParam: wearEngine.P2pAppParam = {
     remoteApp: appInfo
     // transformLocalAppInfo默认为false，不转换包名指纹
   };

   // 步骤5 构造回调函数
   let callback = (p2pMessage: wearEngine.P2pMessage) => {
     console.info(`Succeeded in receiving message, the message is ${p2pMessage.content}.`);
   };

   // 步骤6 订阅监听消息接收事件
   p2pClient.registerMessageReceiver(targetDevice.randomId, appParam, callback).then(() => {
     console.info(`Succeeded in registering message receiver.`);
   }).catch((error: BusinessError) => {
     console.error(`Failed to register message receiver. Code is ${error.code}, message is ${error.message}.`);
   });
   ```
7. 调用[unregisterMessageReceiver](../harmonyos-references/wearengine_api.md#unregistermessagereceiver)方法，手机应用取消接收穿戴设备侧应用发过来的消息，需要传入订阅监听时的同一个回调函数对象。

   ```typescript
   p2pClient.unregisterMessageReceiver(targetDevice.randomId, appParam, callback).then(() => {
     console.info(`Succeeded in unregistering message receiver.`);
   }).catch((error: BusinessError) => {
     console.error(`Failed to unregister message receiver. Code is ${error.code}, message is ${error.message}.`);
   });
   ```

## 订阅接收穿戴设备侧发送过来的文件

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
4. 构造设备侧应用参数[P2pAppParam](../harmonyos-references/wearengine_api.md#p2pappparam)。
5. 构造接收到设备侧传来文件后的回调函数[Callback](../harmonyos-references/js-apis-base.md#callback)。
6. 调用[registerFileReceiver](../harmonyos-references/wearengine_api.md#registerfilereceiver)方法，订阅监听文件接收事件。

   ```typescript
   // 步骤3 获取P2pClient对象
   let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   // 步骤4 构造设备侧应用参数
   let appInfo: wearEngine.AppInfo = {
     bundleName: '',
     fingerprint: ''
   };
   // 将设备侧应用参数类定义为appParam
   let appParam: wearEngine.P2pAppParam = {
     remoteApp: appInfo
     // transformLocalAppInfo默认为false，不转换包名指纹
   };

   // 步骤5 构造回调函数
   let callback = (p2pMessage: wearEngine.P2pFile) => {
     console.info(`Succeeded in receiving file.`);
   };

   // 步骤6 订阅监听文件接收事件
   p2pClient.registerFileReceiver(targetDevice.randomId, appParam, callback).then(() => {
     console.info(`Succeeded in registering file receiver.`);
   }).catch((error: BusinessError) => {
     console.error(`Failed to register file receiver. Code is ${error.code}, message is ${error.message}.`);
   });
   ```
7. 调用[unregisterFileReceiver](../harmonyos-references/wearengine_api.md#unregisterfilereceiver)方法，手机应用取消接收穿戴设备侧应用发过来的文件，需要传入订阅监听时的同一个回调函数对象。

   ```typescript
   p2pClient.unregisterFileReceiver(targetDevice.randomId, appParam, callback).then(() => {
     console.info(`Succeeded in unregistering file receiver.`);
   }).catch((error: BusinessError) => {
     console.error(`Failed to unregister file receiver. Code is ${error.code}, message is ${error.message}.`);
   });
   ```

## 订阅接收穿戴设备侧发送的文件和文件的传输进度

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
4. 构造设备侧应用参数[P2pAppParam](../harmonyos-references/wearengine_api.md#p2pappparam)。
5. 构造接收到设备侧传来文件和文件的传输进度后的回调函数[Callback](../harmonyos-references/js-apis-base.md#callback)。
6. 调用[registerFileReceiverWithProgress](../harmonyos-references/wearengine_api.md#registerfilereceiverwithprogress)方法，订阅监听接收文件和文件传输进度的事件。

   ```typescript
   // 步骤3 获取P2pClient对象
   let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   // 步骤4 构造设备侧应用参数
   let appInfo: wearEngine.AppInfo = {
     bundleName: '',
     fingerprint: ''
   };
   // 将设备侧应用参数类定义为appParam
   let appParam: wearEngine.P2pAppParam = {
     remoteApp: appInfo
     // transformLocalAppInfo默认为false，不转换包名指纹
   };

   // 步骤5 构造回调函数
   let callback = (p2pMessage: wearEngine.P2pFile) => {
     if (!p2pMessage.file) {
       console.info(`progress is ${p2pMessage.progress}`);
     } else {
       console.info(`Succeeded in receiving file.`);
     }
   };

   // 步骤6 订阅监听文件接收和传输进度的事件
   p2pClient.registerFileReceiverWithProgress(targetDevice.randomId, appParam, callback).then(() => {
     console.info(`Succeeded in registering file receiver.`);
   }).catch((error: BusinessError) => {
     console.error(`Failed to register file receiver. Code is ${error.code}, message is ${error.message}.`);
   });
   ```
7. 调用[unregisterFileReceiver](../harmonyos-references/wearengine_api.md#unregisterfilereceiver)方法，手机应用取消接收穿戴设备侧应用文件和文件传输进度，需要传入订阅监听时的同一个回调函数对象。

   ```typescript
   p2pClient.unregisterFileReceiver(targetDevice.randomId, appParam, callback).then(() => {
     console.info(`Succeeded in unregistering file receiver.`);
   }).catch((error: BusinessError) => {
     console.error(`Failed to unregister file receiver. Code is ${error.code}, message is ${error.message}.`);
   });
   ```
