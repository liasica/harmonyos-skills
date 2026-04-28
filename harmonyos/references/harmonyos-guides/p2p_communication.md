---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/p2p_communication
title: 应用间消息通信
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 手机侧应用开发 > 应用开发 > 应用间消息通信
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:057428540804edb8bdefabefaaad15f7b9ac85ad1cce7cb5d342232ec77c0824
---

在手机侧与穿戴设备侧构建应用到应用的通信隧道，用于收发应用自定义的报文消息以及文件。实现手机应用和穿戴设备应用间的交互，为用户提供分布式场景和体验。比如手机应用发送音频文件到穿戴设备侧应用，实现在穿戴设备侧应用上播放音乐；手机应用发送暂停指令，实现穿戴设备音乐播放暂停等。

收发点对点消息前，需要确保应用已在开发者联盟申请获取设备基础信息权限（参见[申请接入Wear Engine服务](wearengine_apply.md)），否则接口将调用失败。

说明

* 使用该功能前，请确保穿戴设备支持应用安装能力（参见[目标设备选择](we-device-selection.md#根据设备支持的device能力集挑选目标设备)），同时穿戴设备侧已有对应的应用（参见[穿戴侧应用开发](watch_query_connected_devices.md)）。
* 手机App和穿戴设备App必须同时处于启动状态。
* 当手机App启动且穿戴设备App没有启动时，手机App可以通过[startRemoteApp](../harmonyos-references/wearengine_api.md#startremoteapp)方法拉起穿戴设备App。

## 手机侧应用检测穿戴设备侧应用是否安装

说明

该接口的调用需要在开发者联盟申请设备基础信息权限（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
4. 调用[isRemoteAppInstalled](../harmonyos-references/wearengine_api.md#isremoteappinstalled)方法，查看是否安装指定的设备应用。

   ```
   1. // 将设备侧应用包名定义为remoteBundleName
   2. let remoteBundleName: string = '';

   4. // 步骤3 获取P2pClient对象
   5. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   7. // 步骤4 查看是否安装指定的设备侧应用
   8. p2pClient.isRemoteAppInstalled(targetDevice.randomId, remoteBundleName).then((isInstall) => {
   9. console.info(`Succeeded in checking remote app install, result is ${isInstall}.`);
   10. }).catch((error: BusinessError) => {
   11. console.error(`Failed to check remote app install. Code is ${error.code}, message is ${error.message}.`);
   12. })
   ```

## 手机侧应用获取穿戴设备侧应用的版本号

说明

该接口的调用需要在开发者联盟申请设备基础信息权限（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
4. 调用[getRemoteAppVersion](../harmonyos-references/wearengine_api.md#getremoteappversion)方法，获取指定设备对应的应用版本号。

   ```
   1. // 将设备侧应用包名定义为remoteBundleName
   2. let remoteBundleName: string = '';

   4. // 步骤3 获取P2pClient对象
   5. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   7. // 步骤4 获取指定设备对应的应用版本号
   8. p2pClient.getRemoteAppVersion(targetDevice.randomId, remoteBundleName).then((version) => {
   9. console.info(`Succeeded in getting remote app version, version is ${version}.`);
   10. }).catch((error: BusinessError) => {
   11. console.error(`Failed to check get remote app version. Code is ${error.code}, message is ${error.message}.`);
   12. })
   ```

## 手机侧应用拉起设备侧应用

说明

该接口的调用需要在开发者联盟申请设备基础信息权限（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

在发送点对点消息前，可以用[startRemoteApp](../harmonyos-references/wearengine_api.md#startremoteapp)方法拉起设备侧应用。

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
4. 调用[startRemoteApp](../harmonyos-references/wearengine_api.md#startremoteapp)方法，指定需要拉起设备侧应用包名。[transformLocalBundleName](../harmonyos-references/wearengine_api.md#startremoteapp)默认值为false，传入为true时，wearEngine会将本地的应用包名和指纹转换为兼容应用在云侧存储的包名和指纹，可参考[申请接入Wear Engine服务](wearengine_apply.md)章节。

   ```
   1. // 将设备侧应用包名定义为remoteBundleName
   2. let remoteBundleName: string = '';

   4. // 步骤3 获取P2pClient对象
   5. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   7. // 步骤4 拉起设备侧指定应用(transformLocalBundleName不传入参数，默认为false)
   8. p2pClient.startRemoteApp(targetDevice.randomId, remoteBundleName).then((p2pResult) => {
   9. console.info(`Succeeded in starting remote app, result is ${p2pResult.code}.`);
   10. }).catch((error: BusinessError) => {
   11. console.error(`Failed to start remote app. Code is ${error.code}, message is ${error.message}.`);
   12. })
   ```

## 手机侧应用发送点对点消息或文件到穿戴设备侧应用

说明

该接口的调用需要在开发者联盟申请设备基础信息权限（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

消息长度大小的限制为4096字节。针对消息长度超过限制的情况可以采用发送文件（文件大小不超过100MB）的方式或进行消息分包控制。

手机侧实现发送消息和文件功能后，穿戴设备侧应用需要对应实现接收消息和文件的功能。

### 发送点对点消息

为了使用工具类构造消息体，请先导入所需模块。

```
1. import { util } from '@kit.ArkTS';
```

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 构造设备侧应用参数[P2pAppParam](../harmonyos-references/wearengine_api.md#p2pappparam)。
4. 构造需要发送的消息[P2pMessage](../harmonyos-references/wearengine_api.md#p2pmessage)。
5. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
6. 调用[sendMessage](../harmonyos-references/wearengine_api.md#sendmessage)方法，从手机上的应用发送简短消息到穿戴设备侧对应的应用。设备侧已注册监听消息接收后，即可收到手机发送的消息。

   ```
   1. // 步骤3 构造设备侧应用参数
   2. let appInfo: wearEngine.AppInfo = {
   3. // 设置设备侧应用的应用信息：包名与指纹
   4. bundleName: '',
   5. fingerprint: ''
   6. }
   7. let appParam: wearEngine.P2pAppParam = {
   8. remoteApp: appInfo
   9. // transformLocalAppInfo默认为false，不转换包名指纹
   10. }

   12. // 设置需要发送的消息内容，长度限制为4096字节
   13. let messageContent: string = 'this is message';

   15. // 步骤4 构造消息结构体
   16. let textEncoder: util.TextEncoder = new util.TextEncoder;
   17. let message: wearEngine.P2pMessage = {
   18. content: textEncoder.encodeInto(messageContent)
   19. }

   21. // 步骤5 获取P2pClient对象
   22. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   24. // 步骤6 发送消息
   25. p2pClient.sendMessage(targetDevice.randomId, appParam, message).then((p2pResult) => {
   26. console.info(`Succeeded in sending message, result is ${p2pResult.code}.`);
   27. }).catch((error: BusinessError) => {
   28. console.error(`Failed to send message. Code is ${error.code}, message is ${error.message}.`);
   29. })
   ```

### 发送文件

为能正确打开文件描述符，请先导入模块。

```
1. import { fileIo } from '@kit.CoreFileKit';
```

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 构造设备侧应用参数[P2pAppParam](../harmonyos-references/wearengine_api.md#p2pappparam)。
4. 根据文件路径filePath，构造需要发送的文件[P2pFile](../harmonyos-references/wearengine_api.md#p2pfile)。
5. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
6. 调用[transferFile](../harmonyos-references/wearengine_api.md#transferfile)方法，从手机上的应用发送文件到穿戴设备侧对应的应用。

   ```
   1. // 步骤3 构造设备侧应用参数
   2. let appInfo: wearEngine.AppInfo = {
   3. // 设置设备侧应用的应用信息：包名与指纹
   4. bundleName: '',
   5. fingerprint: ''
   6. }
   7. let appParam: wearEngine.P2pAppParam = {
   8. remoteApp: appInfo
   9. // transformLocalAppInfo默认为false，不转换包名指纹
   10. }

   12. // 步骤4 构造需要发送的文件
   13. let p2pfile: wearEngine.P2pFile = {
   14. // 设置需要发送的文件路径，其中不能包含'..'
   15. file: fileIo.openSync('')
   16. }

   18. // 步骤5 获取P2pClient对象
   19. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   21. // 步骤6 发送指定文件至设备
   22. p2pClient.transferFile(targetDevice.randomId, appParam, p2pfile, (error: BusinessError, p2pResult: wearEngine.P2pResult) => {
   23. // callback处理逻辑
   24. if (error) {
   25. console.error(`Failed to transfer file. Code is ${error.code}, message is ${error.message}.`);
   26. return;
   27. }
   28. if (p2pResult.code) {
   29. if (p2pResult.code === wearEngine.P2pResultCode.COMMUNICATION_SUCCESS) {
   30. console.info(`Succeeded in transferring file, the result is ${p2pResult.code}.`);
   31. } else {
   32. console.info(`Failed to transfer file, the error code is ${p2pResult.code}.`);
   33. return;
   34. }
   35. }
   36. if (p2pResult.progress) {
   37. console.info(`Succeeded in transferring file, the progress is ${p2pResult.progress}.`);
   38. }
   39. });

   41. fileIo.close(p2pfile.file);
   ```

### 取消发送文件

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 构造设备侧应用参数[P2pAppParam](../harmonyos-references/wearengine_api.md#p2pappparam)。
4. 根据文件路径filePath，构造需要取消发送的文件[P2pFile](../harmonyos-references/wearengine_api.md#p2pfile)。
5. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
6. 调用[cancelFileTransfer](../harmonyos-references/wearengine_api.md#cancelfiletransfer)方法，取消从手机上的应用到穿戴设备侧对应的应用的文件发送。

   ```
   1. // 步骤3 构造设备侧应用参数
   2. let appInfo: wearEngine.AppInfo = {
   3. // 设置设备侧应用的应用信息：包名与指纹
   4. bundleName: '',
   5. fingerprint: ''
   6. }
   7. let appParam: wearEngine.P2pAppParam = {
   8. remoteApp: appInfo
   9. // transformLocalAppInfo默认为false，不转换包名指纹
   10. }

   12. // 步骤4 构造需要发送的文件
   13. let p2pfile: wearEngine.P2pFile = {
   14. // 设置需要发送的文件路径，其中不能包含'..'
   15. file: fileIo.openSync('')
   16. }

   18. // 步骤5 获取P2pClient对象
   19. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   21. // 发送指定文件至设备
   22. p2pClient.transferFile(targetDevice.randomId, appParam, p2pfile, () => {
   23. // 回调函数执行逻辑
   24. })

   26. // 步骤6 取消发送文件
   27. p2pClient.cancelFileTransfer(targetDevice.randomId, appParam, p2pfile).then((p2pResult) => {
   28. if (p2pResult.code === wearEngine.P2pResultCode.COMMUNICATION_SUCCESS) {
   29. console.info(`Succeeded in cancelling transfer file, the result is ${p2pResult.code}.`);
   30. }
   31. }).catch((error: BusinessError) => {
   32. console.error(`Failed to cancel transfer file. Code is ${error.code}, message is ${error.message}.`);
   33. })

   35. fileIo.close(p2pfile.file);
   ```

## 订阅接收穿戴设备侧应用发过来的消息

说明

该接口的调用需要在开发者联盟申请设备基础信息权限（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
4. 构造设备侧应用参数[P2pAppParam](../harmonyos-references/wearengine_api.md#p2pappparam)。
5. 构造接收到设备侧传来消息后的回调函数[Callback](../harmonyos-references/js-apis-base.md#callback)。
6. 调用[registerMessageReceiver](../harmonyos-references/wearengine_api.md#registermessagereceiver)方法，订阅监听消息接收事件。

   ```
   1. // 步骤3 获取P2pClient对象
   2. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   4. // 步骤4 构造设备侧应用参数
   5. let appInfo: wearEngine.AppInfo = {
   6. bundleName: '',
   7. fingerprint: ''
   8. }
   9. // 将设备侧应用参数类定义为appParam
   10. let appParam: wearEngine.P2pAppParam = {
   11. remoteApp: appInfo
   12. // transformLocalAppInfo默认为false，不转换包名指纹
   13. }

   15. // 步骤5 构造回调函数
   16. let callback = (p2pMessage: wearEngine.P2pMessage) => {
   17. console.info(`Succeeded in receiving message, the message is ${p2pMessage.content}.`);
   18. }

   20. // 步骤6 订阅监听消息接收事件
   21. p2pClient.registerMessageReceiver(targetDevice.randomId, appParam, callback).then(() => {
   22. console.info(`Succeeded in registering message receiver.`);
   23. }).catch((error: BusinessError) => {
   24. console.error(`Failed to register message receiver. Code is ${error.code}, message is ${error.message}.`);
   25. })
   ```
7. 调用[unregisterMessageReceiver](../harmonyos-references/wearengine_api.md#unregistermessagereceiver)方法，手机应用取消接收穿戴设备侧应用发过来的消息，需要传入订阅监听时的同一个回调函数对象。

   ```
   1. p2pClient.unregisterMessageReceiver(targetDevice.randomId, appParam, callback).then(() => {
   2. console.info(`Succeeded in unregistering message receiver.`);
   3. }).catch((error: BusinessError) => {
   4. console.error(`Failed to unregister message receiver. Code is ${error.code}, message is ${error.message}.`);
   5. })
   ```

## 订阅接收穿戴设备侧发送过来的文件

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
4. 构造设备侧应用参数[P2pAppParam](../harmonyos-references/wearengine_api.md#p2pappparam)。
5. 构造接收到设备侧传来文件后的回调函数[Callback](../harmonyos-references/js-apis-base.md#callback)。
6. 调用[registerFileReceiver](../harmonyos-references/wearengine_api.md#registerfilereceiver)方法，订阅监听文件接收事件。

   ```
   1. // 步骤3 获取P2pClient对象
   2. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   4. // 步骤4 构造设备侧应用参数
   5. let appInfo: wearEngine.AppInfo = {
   6. bundleName: '',
   7. fingerprint: ''
   8. }
   9. // 将设备侧应用参数类定义为appParam
   10. let appParam: wearEngine.P2pAppParam = {
   11. remoteApp: appInfo
   12. // transformLocalAppInfo默认为false，不转换包名指纹
   13. }

   15. // 步骤5 构造回调函数
   16. let callback = (p2pMessage: wearEngine.P2pFile) => {
   17. console.info(`Succeeded in receiving file.`);
   18. }

   20. // 步骤6 订阅监听文件接收事件
   21. p2pClient.registerFileReceiver(targetDevice.randomId, appParam, callback).then(() => {
   22. console.info(`Succeeded in registering file receiver.`);
   23. }).catch((error: BusinessError) => {
   24. console.error(`Failed to register file receiver. Code is ${error.code}, message is ${error.message}.`);
   25. })
   ```
7. 调用[unregisterFileReceiver](../harmonyos-references/wearengine_api.md#unregisterfilereceiver)方法，手机应用取消接收穿戴设备侧应用发过来的文件，需要传入订阅监听时的同一个回调函数对象。

   ```
   1. p2pClient.unregisterFileReceiver(targetDevice.randomId, appParam, callback).then(() => {
   2. console.info(`Succeeded in unregistering file receiver.`);
   3. }).catch((error: BusinessError) => {
   4. console.error(`Failed to unregister file receiver. Code is ${error.code}, message is ${error.message}.`);
   5. })
   ```
