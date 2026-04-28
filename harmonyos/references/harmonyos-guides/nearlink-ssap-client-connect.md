---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-ssap-client-connect
title: SSAP客户端
breadcrumb: 指南 > 系统 > 网络 > NearLink Kit（星闪服务） > SSAP连接及数据传输 > SSAP客户端
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8e31b51a937d2366bc5b9013938753a514444f6e2863d67461661134b3bd79da
---

说明

提供SSAP（SparkLink Service Access Protocol）客户端相关的连接、数据传输和服务操作功能。

## 场景介绍

提供设备作为客户端的能力，客户端可连接服务端进行数据传输。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [createClient](../harmonyos-references/nearlink-ssap.md#createclient)(address: string): Client | 创建ssap客户端实例。 |
| [connect](../harmonyos-references/nearlink-ssap.md#connect)(): Promise<void> | 向服务端发起连接。 |
| [getServices](../harmonyos-references/nearlink-ssap.md#getservices)(): Promise<Array<Service>>; | 获取服务端支持的服务列表。 |
| [readProperty](../harmonyos-references/nearlink-ssap.md#readproperty)(property: Property): Promise<Property> | 读取服务端property。 |
| [writeProperty](../harmonyos-references/nearlink-ssap.md#writeproperty)(property: Property, writeType: PropertyWriteType): Promise<void> | 写入服务端property。 |
| [setPropertyNotification](../harmonyos-references/nearlink-ssap.md#setpropertynotification)(property: Property, enable: boolean): Promise<void> | 启用/禁用某个property变化的通知。 |
| [on](../harmonyos-references/nearlink-ssap.md#on-propertychange)(type: 'propertyChange', callback: Callback<Property>): void | 订阅property变化事件。 |
| [on](../harmonyos-references/nearlink-ssap.md#on-connectionstatechange)(type: 'connectionStateChange', callback: Callback<ConnectionChangeState>): void | 订阅连接状态变化事件。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { ssap } from '@kit.NearLinkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建ssap客户端实例。其中参数addr是通过[扫描流程](nearlink-start-scan.md)获取的远端设备地址。

   ```
   1. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
   2. let client: ssap.Client;
   3. try {
   4. client = ssap.createClient(addr);
   5. console.info('client: ' + JSON.stringify(client));
   6. } catch (err) {
   7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   8. }
   ```
3. 订阅连接状态变化事件。其中client对象在步骤2创建，后续步骤中使用的client对象也是一样，不再赘述。

   ```
   1. let onReceiveConnectionChangeEvent:(data: ssap.ConnectionChangeState) => void = (data: ssap.ConnectionChangeState) => {
   2. console.info('data:'+ JSON.stringify(data));
   3. }
   4. try {
   5. client.on('connectionStateChange', onReceiveConnectionChangeEvent);
   6. } catch (err) {
   7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   8. }
   ```
4. 订阅Property变化事件。

   ```
   1. let onReceivePropertyChangeEvent:(data: ssap.Property) => void = (data: ssap.Property) => {
   2. console.info('data:'+ JSON.stringify(data));
   3. }
   4. try {
   5. client.on('propertyChange', onReceivePropertyChangeEvent);
   6. } catch (err) {
   7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   8. }
   ```
5. 向服务端发起连接。连接成功后会收到步骤3中订阅的连接状态变化的回调，之后可以进行数据交互。

   ```
   1. try {
   2. client.connect().then(() => {
   3. console.info("connect success");
   4. }).catch ((err: BusinessError) => {
   5. console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
   6. });
   7. } catch (err) {
   8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   9. }
   ```
6. 获取服务端支持的服务列表。

   ```
   1. try {
   2. client.getServices().then((result: Array<ssap.Service>) => {
   3. console.info('getServices successfully:' + JSON.stringify(result));
   4. }).catch ((err: BusinessError) => {
   5. console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
   6. });
   7. } catch (err) {
   8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   9. }
   ```
7. 读取指定服务的Property值，参数property中的[serviceUuid](../harmonyos-references/nearlink-ssap.md#property)以及[propertyUuid](../harmonyos-references/nearlink-ssap.md#property)通过步骤6获取。

   ```
   1. try {
   2. // 创建property,实际开发时需要通过getServices接口从服务端获取
   3. let arrayBufferC = new ArrayBuffer(1);
   4. let properV = new Uint8Array(arrayBufferC);
   5. properV[0] = 1;
   6. let property: ssap.Property = {
   7. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
   8. propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
   9. value: arrayBufferC
   10. };
   11. client.readProperty(property).then((result: ssap.Property) => {
   12. console.info('readProperty successfully:' + JSON.stringify(result));
   13. }).catch ((err: BusinessError) => {
   14. console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
   15. });
   16. } catch (err) {
   17. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   18. }
   ```
8. 写入指定服务的Property值，参数property中的[serviceUuid](../harmonyos-references/nearlink-ssap.md#property)以及[propertyUuid](../harmonyos-references/nearlink-ssap.md#property)通过步骤6获取。

   ```
   1. try {
   2. let arrayBufferC = new ArrayBuffer(1);
   3. // 期望写入的property值
   4. let properV = new Uint8Array(arrayBufferC);
   5. properV[0] = 1;
   6. let property: ssap.Property = {
   7. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
   8. propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
   9. value: arrayBufferC
   10. };
   11. client.writeProperty(property, ssap.PropertyWriteType.WRITE_NO_RESPONSE).then(() => {
   12. console.info('writeProperty success');
   13. }).catch ((err: BusinessError) => {
   14. console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
   15. });
   16. } catch (err) {
   17. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   18. }
   ```
9. 设置支持Property变化通知，参数property中的[serviceUuid](../harmonyos-references/nearlink-ssap.md#property)以及[propertyUuid](../harmonyos-references/nearlink-ssap.md#property)通过步骤6获取。

   之后如果服务端Property值发生变化，则客户端通过步骤4订阅的事件接收新数据。

   ```
   1. try {
   2. let arrayBufferC = new ArrayBuffer(1);
   3. let properV = new Uint8Array(arrayBufferC);
   4. properV[0] = 1;
   5. let property: ssap.Property = {
   6. serviceUuid:'37bea880-fc70-11ea-b720-000000004386',
   7. propertyUuid: '37bea880-fc70-11ea-b720-000000001234',
   8. value: arrayBufferC
   9. };
   10. client.setPropertyNotification(property, true).then(() => {
   11. console.info('setPropertyNotification success');
   12. }).catch ((err: BusinessError) => {
   13. console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
   14. });
   15. } catch (err) {
   16. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   17. }
   ```

## 示例代码

SSAP客户端功能可参考[星闪示例代码](https://gitcode.com/harmonyos_samples/nearlink-kit_-sample-code)，entry/src/main/ets/pages/SsapClientPage.ets中的实现方法。
