---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/linkenhance_development-guide
title: 增强连接开发指导
breadcrumb: 指南 > 系统 > 网络 > Distributed Service Kit（分布式管理服务） > 应用跨设备连接管理 > 增强连接开发指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:32:37+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:b276fe9fd2424fb36fc3fd8a1efa4549c1daa6ed25216f18488651c40f7e47a9
---

## 简介

随着技术的发展，各种应用层出不穷，设备间的互联关系也成为一种常态，此时对于网络环境的依赖也不可避免。然而，在某些特殊场景下（如航空、远洋航行等），网络受限，蓝牙成为少数可行的连接方式。但是传统蓝牙连接存在着连接数量有限、连接成功率低、连接不稳定等缺点，影响了用户体验。

HarmonyOS提供了分布式增强连接能力，实现跨设备互联，完成与对端设备的连接，交换应用业务数据。相比传统蓝牙连接，使用多通道合并算法，增加设备连接数量，增强连接稳定性，提升跨端互通体验。

### 实现原理

在设备互联过程中，发现对端的蓝牙地址并建立物理链路；在多设备互联场景下，通过特有的多通道合并算法，在保证设备间交互能力的前提下，减少实际物理链路的个数，达到设备间可用连接数增大、降低干扰提升通信的稳定性的效果。

两个设备的交互实现如下，在使用[linkEnhance](../harmonyos-references/js-apis-link-enhance.md)能力后，当两端同时发起连接时，会自动识别合并底层多余物理链路，减少实际物理链路的个数，减少蓝牙链路资源的消耗，增加可用连接数量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/mRtj2guHQ-GhgN_QqLHZnA/zh-cn_image_0000002558605266.png?HW-CC-KV=V1&HW-CC-Date=20260429T053236Z&HW-CC-Expire=86400&HW-CC-Sign=0741A9EBC7148E19A684064909371D91694EDA7AE9ADFE891D579FAD8598131E)

### 约束与限制

* 设备互联时需要开启蓝牙功能。
* 通过蓝牙广播/扫描接口获取对端设备BLE MAC。蓝牙BLE接口参见[查找设备](ble-development-guide.md)。
* 不同设备间只有相同bundleName的应用才能进行互联。
* 需要配置ohos.permission.DISTRIBUTED\_DATASYNC权限。
* 该接口提供连接能力，链路安全策略遵循调用者初始设置的蓝牙配对策略（如：Numeric Comparison、Passkey Entry、Just Works、Out of Band四种方式）。

## 环境准备

### 环境要求

打开客户端和服务端设备的蓝牙开关。

### 搭建环境

1. 在PC上安装[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)，版本要求在4.1及以上。
2. 将public-SDK更新到API 20或以上。
3. 用USB线缆将两台调测设备（设备A和设备B）连接到PC。
4. 打开设备A和设备B的蓝牙开关。

## 接口说明

常用接口说明如下表。更多接口的详细介绍参考@ohos.distributedsched.linkEnhance[增强连接](../harmonyos-references/js-apis-link-enhance.md)。

| 接口名 | 功能描述 |
| --- | --- |
| connect() | Client端发起连接远端设备。 |
| disconnect() | 断开与远端设备的连接。 |
| close() | 销毁Connection对象，注销所有注册的事件，调用该接口后Connection对象将不能再使用。 |
| getPeerDeviceId() | 获取远端设备的deviceId。 |
| sendData(data:ArrayBuffer) | 向远端设备发送数据。 |
| on(type: 'connectResult') | 订阅连接结果通知变化的事件。 |
| on(type: 'disconnected') | 订阅连接状态断开的事件。 |
| on(type: 'dataReceived') | 注册收数据的通知事件。 |
| createConnection(deviceId: string,name:string) | 创建一个connection对象。 |
| start() | 服务端开启服务。 |
| stop() | 服务端停止服务。 |
| close() | 销毁Server对象，注销已注册的服务并取消已订阅的所有事件，调用该接口后Server对象将不能再使用。 |
| on(type: 'connectionAccepted') | Server端订阅收到对端连接的事件。 |
| on(type: 'serverStopped') | Server端订阅服务状态停止的事件。 |
| createServer(name: string) | 创建一个server对象。 |

## 增强连接开发指导

* 服务端开启蓝牙后，创建Server对象，并调用[start()接口](../harmonyos-references/js-apis-link-enhance.md#start)开启服务，让服务端处于可连接状态，通过注册的事件监听，监听事件的变化通知。
* 客户端开启蓝牙后，创建Connection对象，并调用[connect()接口](../harmonyos-references/js-apis-link-enhance.md#connect)发起连接，通过注册的事件监听，监听事件的变化通知。
* 连接成功后，可以使用[sendData接口](../harmonyos-references/js-apis-link-enhance.md#senddata)发送数据。

### 服务端开发指导

1. 导入所需的模块。

   ```
   1. import {linkEnhance} from '@kit.DistributedServiceKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 在module.json5配置文件中配置分布式数据同步权限ohos.permission.DISTRIBUTED\_DATASYNC。

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
3. 创建server对象，并开启服务，注册监听。

   ```
   1. const TAG = 'TEST';
   2. // server端注册服务
   3. linkEnhanceStart(name: string) {
   4. console.info(TAG + 'start server deviceId = ' + name);
   5. try {
   6. // 使用服务名构造Server
   7. let server: linkEnhance.Server = linkEnhance.createServer(name);

   9. // 订阅服务接收事件和服务停止事件
   10. server.on('connectionAccepted', (connection: linkEnhance.Connection): void => {
   11. console.info(TAG + 'serverOnCallback');
   12. });
   13. server.on('serverStopped', (reason: number): void => {
   14. console.info(TAG, 'serverStopped， reason= ' + reason);
   15. });
   16. // 启动服务
   17. server.start();
   18. } catch (err) {
   19. console.error(TAG + 'start server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
   20. (err as BusinessError).message);
   21. }
   22. }
   ```
4. 当连接被连上时，需要保存connection对象。

   ```
   1. serverAcceptOnCallback = (connection: linkEnhance.Connection): void => {
   2. console.info(TAG + 'serverOnCallback');
   3. try {

   5. // 收到连接请求后，订阅connection的断连事件。
   6. connection.on('disconnected', (reason: number)=> {
   7. console.info(TAG + 'disconnected, reason = ' + reason);
   8. });
   9. // 收到连接请求后，订阅connection的数据接收事件。
   10. connection.on('dataReceived', (data: ArrayBuffer)=> {
   11. console.info(TAG + 'dataReceived, dataLen=' + data.byteLength);
   12. });

   14. let len = 1;
   15. let arraybuffer = new ArrayBuffer(len);
   16. // 向远端发送数据。
   17. connection.sendData(arraybuffer);
   18. } catch (err) {
   19. console.error(TAG + 'server on callback errCode: ' + (err as BusinessError).code + ', errMessage: ' +
   20. (err as BusinessError).message);
   21. }
   22. }
   ```
5. 断开连接并销毁Connection对象。

   ```
   1. // 断连接。
   2. linkEnhanceDisconnect(connection: linkEnhance.Connection) {
   3. console.info(TAG + 'disconnect deviceId = ' + connection.getPeerDeviceId());
   4. try {
   5. connection.disconnect();
   6. connection.close();
   7. } catch (err) {
   8. console.error(TAG + 'disconnect errCode: ' + (err as BusinessError).code + ', errMessage: ' +
   9. (err as BusinessError).message);
   10. }
   11. }
   ```
6. 停止服务并销毁server对象。

   ```
   1. // Server端停止服务
   2. linkEnhanceStop(server: linkEnhance.Server) {
   3. console.info(TAG + 'stop server');
   4. try {
   5. server.stop();
   6. } catch (err) {
   7. console.info(TAG + 'stop server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
   8. (err as BusinessError).message);
   9. }
   10. }
   11. // Server端停止服务并取消所有的订阅事件
   12. linkEnhanceClose(server: linkEnhance.Server) {
   13. console.info(TAG + 'close server' );
   14. try {
   15. server.close();
   16. } catch (err) {
   17. console.error(TAG + 'close server errCode: ' + (err as BusinessError).code + ', errMessage: ' +
   18. (err as BusinessError).message);
   19. }
   20. }
   ```

### 客户端开发指导

1. 导入所需的模块。

   ```
   1. import { linkEnhance } from '@kit.DistributedServiceKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 在module.json5配置文件中配置分布式数据同步权限ohos.permission.DISTRIBUTED\_DATASYNC。

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
3. 创建connection对象，订阅连接结果通知变化的事件，连接服务端。

   ```
   1. const TAG = "testDemo";
   2. // client端主动连接时调用
   3. linkEnhanceConnect(peerDeviceId: string) {
   4. console.info(TAG + 'connection server deviceId = ' + peerDeviceId);
   5. try {
   6. // 使用peerDeviceId构造Connection后续的交互都需要使用该对象
   7. let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
   8. // 订阅连接结果
   9. connection.on('connectResult', (data: linkEnhance.ConnectResult): void => {
   10. console.info(TAG + 'clientConnectResultCallback result = ' + data.success);
   11. if (data.success) {
   12. // 向服务端发送数据
   13. let len = 1;
   14. let arraybuffer = new ArrayBuffer(len);
   15. connection.sendData(arraybuffer);
   16. }
   17. });
   18. connection.on('disconnected', (reason: number)=> {
   19. console.info(TAG + 'disconnected reason = ' + reason);
   20. });
   21. connection.on('dataReceived', (data: ArrayBuffer)=> {
   22. console.info(TAG + 'dataReceived, dataLen=' + data.byteLength);
   23. });
   24. // 发起连接
   25. connection.connect();
   26. } catch (err) {
   27. console.error(TAG + 'connect errCode: ' + (err as BusinessError).code + ', errMessage: ' +
   28. (err as BusinessError).message);
   29. }
   30. }
   ```
4. 断开连接，销毁Connection对象。

   ```
   1. disconnect(connection: linkEnhance.Connection) {
   2. console.info(TAG + 'disconnect deviceId = ' + connection.getPeerDeviceId());
   3. try {
   4. connection.disconnect();
   5. connection.close();
   6. } catch (err) {
   7. console.error(TAG + 'disconnect errCode: ' + (err as BusinessError).code + ', errMessage: ' +
   8. (err as BusinessError).message);
   9. }
   10. }
   ```
