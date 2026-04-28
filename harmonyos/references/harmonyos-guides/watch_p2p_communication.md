---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/watch_p2p_communication
title: 应用间消息通信
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 穿戴侧应用开发 > 应用间消息通信
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:54+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:18d7945dfedd7698403b58b59d4ecd6fc4ebd63bbc8b7871bfe70a8f91d6eb39
---

## 约束与限制

* 使用该功能前，请确保对端设备侧已有对应的应用。
* 对端设备侧应用和穿戴设备应用必须同时处于已启动状态。

## 穿戴侧应用检测对端设备侧应用是否安装

1. 参见[已连接对端设备查询](watch_query_connected_devices.md)章节，从已连接设备列表中选定需要通信的对端设备。
2. 调用[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
3. 调用[isRemoteAppInstalled](../harmonyos-references/wearengine_api.md#isremoteappinstalled)方法，查看对端设备是否安装指定应用。

   ```
   1. // 将对端应用包名定义为remoteBundleName
   2. let remoteBundleName: string = '';

   4. // 步骤2 获取P2pClient对象
   5. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   7. // 步骤3 查看是否安装指定的对端应用
   8. p2pClient.isRemoteAppInstalled(targetDevice.randomId, remoteBundleName).then((isInstall) => {
   9. console.info(`Succeeded in checking remote app install, result is ${isInstall}.`);
   10. }).catch((error: BusinessError) => {
   11. console.error(`Failed to check remote app install. Code is ${error.code}, message is ${error.message}.`);
   12. })
   ```

## 穿戴侧应用发送点对点消息或文件到对端应用

消息长度大小的限制为4096字节。针对消息长度超过限制的情况可以采用发送文件（文件大小不超过100MB）的方式或进行消息分包控制。

穿戴侧实现发送消息和文件功能后，对端应用需要实现接收消息和文件的功能。

### 发送点对点消息

1. 为了使用工具类构造消息体，请先导入所需模块。

   ```
   1. import { util } from '@kit.ArkTS';
   ```
2. 参见[已连接对端设备查询](watch_query_connected_devices.md)章节，从已连接设备列表中选定需要通信的对端设备。
3. 构造对端应用参数[P2pAppParam](../harmonyos-references/wearengine_api.md#p2pappparam)。
4. 构造需要发送的消息[P2pMessage](../harmonyos-references/wearengine_api.md#p2pmessage)。
5. 调用[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
6. 调用[sendMessage](../harmonyos-references/wearengine_api.md#sendmessage)方法，从穿戴侧应用发送简短消息到对端应用。对端应用已注册监听消息接收后，即可收到穿戴侧应用发送的消息。

   ```
   1. // 步骤2 构造对端应用参数
   2. let appInfo: wearEngine.AppInfo = {
   3. // 设置对端应用的应用信息：包名与指纹
   4. bundleName: '',
   5. fingerprint: ''
   6. }
   7. let appParam: wearEngine.P2pAppParam = {
   8. remoteApp: appInfo
   9. }

   11. // 设置需要发送的消息内容，长度限制为4096字节
   12. let messageContent: string = 'this is message';

   14. // 步骤3 构造消息结构体
   15. let textEncoder: util.TextEncoder = new util.TextEncoder;
   16. let message: wearEngine.P2pMessage = {
   17. content: textEncoder.encodeInto(messageContent)
   18. }

   20. // 步骤4 获取P2pClient对象
   21. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   23. // 步骤5 发送消息
   24. p2pClient.sendMessage(targetDevice.randomId, appParam, message).then((p2pResult) => {
   25. console.info(`Succeeded in sending message, result is ${p2pResult.code}.`);
   26. }).catch((error: BusinessError) => {
   27. console.error(`Failed to send message. Code is ${error.code}, message is ${error.message}.`);
   28. })
   ```

### 发送文件

1. 发送文件前需要打开文件描述符，请先导入模块。

   ```
   1. import { fileIo } from '@kit.CoreFileKit';
   ```
2. 参见[已连接对端设备查询](watch_query_connected_devices.md)章节，从已连接设备列表中选定需要通信的对端设备。
3. 构造对端应用参数[P2pAppParam](../harmonyos-references/wearengine_api.md#p2pappparam)。
4. 根据文件路径filePath，构造需要发送的文件[P2pFile](../harmonyos-references/wearengine_api.md#p2pfile)。
5. 调用[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
6. 调用[transferFile](../harmonyos-references/wearengine_api.md#transferfile)方法，从穿戴侧应用发送文件到对端应用。

   ```
   1. // 步骤2 构造对端应用参数
   2. let appInfo: wearEngine.AppInfo = {
   3. // 设置对端应用的应用信息：包名与指纹
   4. bundleName: '',
   5. fingerprint: ''
   6. }
   7. let appParam: wearEngine.P2pAppParam = {
   8. remoteApp: appInfo
   9. }

   11. // 步骤3 构造需要发送的文件
   12. let p2pfile: wearEngine.P2pFile = {
   13. // 设置需要发送的文件路径，其中不能包含'..'
   14. file: fileIo.openSync('')
   15. }

   17. // 步骤4 获取P2pClient对象
   18. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   20. // 步骤5 发送指定文件至对端
   21. p2pClient.transferFile(targetDevice.randomId, appParam, p2pfile, (error: BusinessError, p2pResult: wearEngine.P2pResult) => {
   22. // callback处理逻辑
   23. if (error) {
   24. console.error(`Failed to transfer file. Code is ${error.code}, message is ${error.message}.`);
   25. return;
   26. }
   27. if (p2pResult.code) {
   28. if (p2pResult.code === wearEngine.P2pResultCode.COMMUNICATION_SUCCESS) {
   29. console.info(`Succeeded in transferring file, the result is ${p2pResult.code}.`);
   30. } else {
   31. console.info(`Failed to transfer file, the error code is ${p2pResult.code}.`);
   32. return;
   33. }
   34. }
   35. if (p2pResult.progress) {
   36. console.info(`Succeeded in transfering file, the progress is ${p2pResult.progress}.`);
   37. }
   38. });

   40. fileIo.close(p2pfile.file);
   ```

## 订阅接收对端应用发来的消息

1. 参见[已连接对端设备查询](watch_query_connected_devices.md)章节，从已连接设备列表中选定需要通信的对端设备。
2. 调用[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
3. 构造对端应用参数[P2pAppParam](../harmonyos-references/wearengine_api.md#p2pappparam)。
4. 构造接收到对端传来消息后的回调函数[Callback](../harmonyos-references/js-apis-base.md#callback)。
5. 调用[registerMessageReceiver](../harmonyos-references/wearengine_api.md#registermessagereceiver)方法，订阅监听消息接收事件。

   ```
   1. // 步骤2 获取P2pClient对象
   2. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   4. // 步骤3 构造对端应用参数
   5. let appInfo: wearEngine.AppInfo = {
   6. bundleName: '',
   7. fingerprint: ''
   8. }
   9. // 将对端应用参数类定义为appParam
   10. let appParam: wearEngine.P2pAppParam = {
   11. remoteApp: appInfo
   12. }

   14. // 步骤4 构造回调函数
   15. let callback = (p2pMessage: wearEngine.P2pMessage) => {
   16. console.info(`Succeeded in receiving message, the message is ${p2pMessage.content}.`);
   17. }

   19. // 步骤5 订阅监听消息接收事件
   20. p2pClient.registerMessageReceiver(targetDevice.randomId, appParam, callback).then(() => {
   21. console.info(`Succeeded in registering message receiver.`);
   22. }).catch((error: BusinessError) => {
   23. console.error(`Failed to register message receiver. Code is ${error.code}, message is ${error.message}.`);
   24. })
   ```
6. 调用[unregisterMessageReceiver](../harmonyos-references/wearengine_api.md#unregistermessagereceiver)方法，穿戴侧应用取消接收对端应用发过来的消息，需要传入订阅监听时的同一个回调函数对象。

   ```
   1. p2pClient.unregisterMessageReceiver(targetDevice.randomId, appParam, callback).then(() => {
   2. console.info(`Succeeded in unregistering message receiver.`);
   3. }).catch((error: BusinessError) => {
   4. console.error(`Failed to unregister message receiver. Code is ${error.code}, message is ${error.message}.`);
   5. })
   ```

## 订阅接收对端应用发送来的文件

1. 参见[已连接对端设备查询](watch_query_connected_devices.md)章节，从已连接设备列表中选定需要通信的对端设备。
2. 调用[getP2pClient](../harmonyos-references/wearengine_api.md#wearenginegetp2pclient)方法，获取[P2pClient](../harmonyos-references/wearengine_api.md#p2pclient)对象。
3. 构造设备侧应用参数[P2pAppParam](../harmonyos-references/wearengine_api.md#p2pappparam)。
4. 构造接收到设备侧传来文件后的回调函数[Callback](../harmonyos-references/js-apis-base.md#callback)。
5. 调用[registerFileReceiver](../harmonyos-references/wearengine_api.md#registerfilereceiver)方法，订阅监听文件接收事件。

   ```
   1. // 步骤2 获取P2pClient对象
   2. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

   4. // 步骤3 构造对端应用参数
   5. let appInfo: wearEngine.AppInfo = {
   6. bundleName: '',
   7. fingerprint: ''
   8. }
   9. // 将对端应用参数类定义为appParam
   10. let appParam: wearEngine.P2pAppParam = {
   11. remoteApp: appInfo
   12. }

   14. // 步骤4 构造回调函数
   15. let callback = (p2pMessage: wearEngine.P2pFile) => {
   16. console.info(`Succeeded in receiving file.`);
   17. }

   19. // 步骤5 订阅监听文件接收事件
   20. p2pClient.registerFileReceiver(targetDevice.randomId, appParam, callback).then(() => {
   21. console.info(`Succeeded in registering file receiver.`);
   22. }).catch((error: BusinessError) => {
   23. console.error(`Failed to register file receiver. Code is ${error.code}, message is ${error.message}.`);
   24. })
   ```
6. 调用[unregisterFileReceiver](../harmonyos-references/wearengine_api.md#unregisterfilereceiver)方法，穿戴侧应用取消接收对端应用发过来的文件，需要传入订阅监听时的同一个回调函数对象。

   ```
   1. p2pClient.unregisterFileReceiver(targetDevice.randomId, appParam, callback).then(() => {
   2. console.info(`Succeeded in unregistering file receiver.`);
   3. }).catch((error: BusinessError) => {
   4. console.error(`Failed to unregister file receiver. Code is ${error.code}, message is ${error.message}.`);
   5. })
   ```

## 对端应用通过startRemoteApp方法拉起穿戴侧应用

如果对端应用通过调用startRemoteApp方法拉起穿戴侧应用时，需要在穿戴侧配置需要拉起的页面。

1. 创建名为HiWearMainAbility.ets的文件，需继承UIAbility，重写onWindowStageCreate函数，配置要跳转的界面。

   ```
   1. // 必须继承UIAbility
   2. import hilog from '@ohos.hilog';
   3. import UIAbility from '@ohos.app.ability.UIAbility';
   4. import window from '@ohos.window';

   6. /**
   7. * 对端应用通过startRemoteApp方法拉起穿戴侧应用的HiWearMainAbility
   8. */
   9. export default class HiWearMainAbility extends UIAbility {
   10. onWindowStageCreate(windowStage: window.WindowStage): void {
   11. hilog.info(0x0000, 'HiWearMainAbility', '%{public}s', 'Ability onWindowStageCreate');

   13. // 配置要跳转的界面为”XXXPage”
   14. windowStage.loadContent("pages/XXXPage", (err, data) => {
   15. if (err.code) {
   16. hilog.error(0x0000, 'HiWearMainAbility', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
   17. return;
   18. }
   19. hilog.info(0x0000, 'HiWearMainAbility', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
   20. });
   21. }
   22. }
   ```
2. 在module.json5中的abilities中配置HiWearMainAbility。更多配置详情参考[abilities标签](module-configuration-file.md#abilities标签)。

   * 配置name为HiWearMainAbility。
   * 配置srcEntry为HiWearMainAbility.ets文件的路径。
   * 配置startWindowIcon为标识当前UIAbility组件启动页面图标资源文件的索引。
   * 配置startWindowBackground为标识当前UIAbility组件启动页面背景颜色资源文件的索引。

     ```
     1. "module": {
     2. "name": "xxxx",
     3. "type": "entry",
     4. "description": "xxxx",
     5. "mainElement": "xxxx",
     6. "deviceTypes": [],
     7. "pages": "xxxx",
     8. "abilities": [
     9. {
     10. "name": "HiWearMainAbility",
     11. "srcEntry": "xxxx",
     12. "startWindowIcon": "xxxx", // 标识当前UIAbility组件启动页面图标资源文件的索引
     13. "startWindowBackground": "xxxx" // 标识当前UIAbility组件启动页面背景颜色资源文件的索引
     14. }],
     15. "metadata": []
     16. }
     ```
3. 在module.json5中的metadata中配置对端应用包名、待拉起的Ability名称，以及是否要等待穿戴侧完成订阅消息接收或者文件接收。

   * 对端应用包名配置时，name为wearEngineRemoteAppNameList，value为具体的对端应用包名，如果存在多个应用包名，使用英文逗号隔开，value值最长不超过4KB；
   * Ability名称配置时，name为wearEngineUIAbilityName，value为指定要拉起的UIAbility名称，不配置默认拉起HiWearMainAbility；
   * AwaitRegisterReceiver配置时，name为wearEngineAwaitRegisterReceiver，value取值为true、false。true表示要等待穿戴侧完成订阅消息接收或者文件接收，false则反之。

     ```
     1. "module": {
     2. "name": "xxxx",
     3. "type": "entry",
     4. "description": "xxxx",
     5. "mainElement": "xxxx",
     6. "deviceTypes": [],
     7. "pages": "xxxx",
     8. "abilities": [],
     9. "metadata": [ // 配置如下信息
     10. {
     11. "name": "wearEngineRemoteAppNameList",
     12. "value": "xxxx1,xxxx2,xxxx3"
     13. },
     14. {
     15. "name": "wearEngineUIAbilityName",
     16. "value": "xxxx"
     17. },
     18. {
     19. "name": "wearEngineAwaitRegisterReceiver",
     20. "value": "true"
     21. }
     22. ]}
     ```
