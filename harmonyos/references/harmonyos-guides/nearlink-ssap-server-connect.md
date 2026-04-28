---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-ssap-server-connect
title: SSAP服务端
breadcrumb: 指南 > 系统 > 网络 > NearLink Kit（星闪服务） > SSAP连接及数据传输 > SSAP服务端
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:072dfc9ccc4e73f67fc3eb05d3ec6fa9044f2b61e33c3e698b5c0bc92cead9dd
---

提供SSAP（SparkLink Service Access Protocol）服务端相关的连接、数据传输和服务管理功能。

注意

建立SSAP连接后，SSAP服务端广播会自动停止。后续如果服务端期望被客户端发现，可参见[发送星闪广播](nearlink-send-advertising.md)，重新发起广播。

## 场景介绍

支持应用基于Nearlink技术进行数据传输，设备作为服务端，客户端可连接该服务端进行数据传输。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [createServer](../harmonyos-references/nearlink-ssap.md#createserver)(): Server | 创建ssap服务端实例。 |
| [addService](../harmonyos-references/nearlink-ssap.md#addservice)(service: Service): void | 服务端添加服务。 |
| [on](../harmonyos-references/nearlink-ssap.md#onconnectionstatechange)(type: 'connectionStateChange', callback: Callback<ConnectionChangeState>): void | 订阅连接状态变化事件。 |
| [on](../harmonyos-references/nearlink-ssap.md#on-propertyread)(type: 'propertyRead', callback: Callback<PropertyReadRequest>): void | 订阅客户端的读请求事件。 |
| [sendResponse](../harmonyos-references/nearlink-ssap.md#sendresponse)(response: ServerResponse): void | 回复客户端读/写请求。 |
| [notifyPropertyChanged](../harmonyos-references/nearlink-ssap.md#notifypropertychanged)(address: string, property: Property): Promise<void> | 通知客户端property值更新。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { ssap } from '@kit.NearLinkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建ssap服务端实例。

   ```
   1. let server: ssap.Server;
   2. try {
   3. server = ssap.createServer();
   4. console.info('server: ' + JSON.stringify(server));
   5. } catch (err) {
   6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   7. }
   ```
3. 添加服务端支持的服务，其中server对象在步骤2创建，后续步骤中使用的server对象也是一样，不再赘述。

   ```
   1. // 构造descriptor
   2. let descriptorsArray: Array<ssap.PropertyDescriptor> = [];
   3. let arrayBuffer = new ArrayBuffer(2);
   4. let descValue = new Uint8Array(arrayBuffer);
   5. descValue[0] = 11;
   6. descValue[1] = 22;
   7. let descriptor: ssap.PropertyDescriptor = {
   8. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
   9. propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
   10. value: arrayBuffer,
   11. descriptorType:ssap.PropertyDescriptorType.PROPERTY,
   12. isWriteable:true
   13. };
   14. descriptorsArray[0] = descriptor;
   15. // 构造properties
   16. let propertiesArray: Array<ssap.Property> = [];
   17. let arrayBufferProperty = new ArrayBuffer(1);
   18. let properValue = new Uint8Array(arrayBufferProperty);
   19. properValue[0] = 1;
   20. let property1: ssap.Property = {
   21. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
   22. propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
   23. value: arrayBufferProperty,
   24. descriptors:descriptorsArray,
   25. operation:3 // 属性可读且可写
   26. };
   27. let property2: ssap.Property = {
   28. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
   29. propertyUuid: '37bea880-fc70-11ea-b720-000000003421',
   30. value: arrayBufferProperty,
   31. descriptors:descriptorsArray,
   32. operation:3 // 属性可读且可写
   33. };
   34. propertiesArray[0] = property1;
   35. propertiesArray[1] = property2;
   36. // 构造服务
   37. let Service: ssap.Service = {
   38. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
   39. properties:propertiesArray
   40. };
   41. try {
   42. server.addService(Service);
   43. } catch (err) {
   44. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   45. }
   ```
4. 订阅连接状态变化事件。

   ```
   1. let onReceiveConnectionChangeEvent:(data: ssap.ConnectionChangeState) => void = (data: ssap.ConnectionChangeState) => {
   2. console.info('data:'+ JSON.stringify(data));
   3. }
   4. try {
   5. server.on('connectionStateChange', onReceiveConnectionChangeEvent);
   6. } catch (err) {
   7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   8. }
   ```
5. 订阅客户端读请求事件。

   ```
   1. let onReceivePropertyReadEvent:(data: ssap.PropertyReadRequest) => void = (data: ssap.PropertyReadRequest) => {
   2. console.info('data:'+ JSON.stringify(data));
   3. }
   4. try {
   5. server.on('propertyRead', onReceivePropertyReadEvent);
   6. } catch (err) {
   7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   8. }
   ```
6. 收到客户端读请求事件后，回复响应。读请求通过步骤5订阅。

   ```
   1. // 订阅客户端的读写请求，收到请求后通过该接口回复
   2. let arrayBuffer = new ArrayBuffer(2);
   3. let descValue = new Uint8Array(arrayBuffer);
   4. descValue[0] = 11;
   5. descValue[1] = 22;
   6. let resp: ssap.ServerResponse = {
   7. address: '00:11:22:33:AA:FF', // 请求方的客户端地址
   8. requestId: 1, // 请求方传入
   9. value: arrayBuffer // 回复的数据
   10. };
   11. try {
   12. // 地址是服务端缓存的已连接的客户端设备
   13. server.sendResponse(resp);
   14. } catch (err) {
   15. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   16. }
   ```
7. 通知客户端property值更新。其中参数address是步骤4中获取的已连接客户端设备地址。

   ```
   1. // 构造properties
   2. let arrayBufferProperty = new ArrayBuffer(8);
   3. let properValue = new Uint8Array(arrayBufferProperty);
   4. properValue[0] = 123; // 本次更新后的值
   5. let property: ssap.Property = {
   6. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
   7. propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
   8. value: arrayBufferProperty,
   9. };
   10. try {
   11. let address = '00:11:22:33:AA:FF'; // 已连接的设备地址
   12. server.notifyPropertyChanged(address, property).then(() => {
   13. console.info('notifyPropertyChanged success');
   14. }).catch ((err: BusinessError) => {
   15. console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
   16. });
   17. } catch (err) {
   18. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   19. }
   ```

## 示例代码

SSAP服务端功能可参考[星闪示例代码](https://gitcode.com/harmonyos_samples/nearlink-kit_-sample-code)，entry/src/main/ets/pages/SsapServerPage.ets中的实现方法。
