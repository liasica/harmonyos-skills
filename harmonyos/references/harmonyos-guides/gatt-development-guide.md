---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gatt-development-guide
title: 连接和传输数据
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 蓝牙 > 低功耗蓝牙 > 连接和传输数据
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:42+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:a813391ed2a49fe21416335040c6de87ec81d7f74731287a577aa9e4f9618d77
---

## 简介

本指南主要提供了基于通用属性协议（Generic Attribute Profile，GATT）实现BLE设备间连接和传输数据的开发指导。当两个设备间进行GATT通信交互时，依据设备功能的不同，可区分为GATT客户端和GATT服务端，本指南将分别介绍客户端与服务端的实现方法。

GATT是低功耗蓝牙（BLE）的核心协议，定义了基于服务（Service）、特征值（Characteristic）和描述符（Descriptor）进行蓝牙通信和传输数据的机制。相关术语介绍请参考[Connectivity Kit术语](terminology.md)。

## 实现原理

客户端获取到服务端的设备地址后，即可向服务端发起连接。服务端设备地址可以通过BLE扫描流程获取。待两端连接成功后，即可向服务端发起服务查询、读写特征值和接收通知等操作，从而实现向服务端发送数据或者接收服务端数据的功能。

服务端需要发送BLE广播才能被客户端发现。服务端需要支持客户端需要连接的服务，等待客户端的连接请求即可。待两端连接成功后，即可接收客户端的读写特征值和发送通知等操作，从而实现接收客户端数据或者向客户端发送数据的功能。

客户端的BLE扫描和服务端的BLE广播流程，请参考[查找设备](ble-development-guide.md)。

## 开发步骤

### 申请蓝牙权限

需要申请权限ohos.permission.ACCESS\_BLUETOOTH。如何配置和申请权限，请参考[声明权限](declare-permissions.md)和[向用户申请授权](request-user-authorization.md)。

### 导入所需API模块

导入ble、constant和错误码模块。

```
1. import { ble, constant } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

### 客户端

**1. 创建客户端实例**

客户端通过查找设备流程搜索到目标设备后，即可构造客户端实例，后续所有操作都基于该客户端实例。

```
1. // 此处是伪代码
2. let device = 'XX:XX:XX:XX:XX:XX';

4. try {
5. let gattClient: ble.GattClientDevice = ble.createGattClientDevice(device);
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

**2. 订阅连接状态变化事件**

通过订阅连接状态变化事件，可以获取实时的GATT连接状态。整个连接过程会涉及多种状态的跃迁，其中[STATE\_CONNECTED](../harmonyos-references/js-apis-bluetooth-constant.md#profileconnectionstate)表示已连接，[STATE\_DISCONNECTED](../harmonyos-references/js-apis-bluetooth-constant.md#profileconnectionstate)表示已断连。

```
1. // 此处是伪代码
2. let device = 'XX:XX:XX:XX:XX:XX';

4. function clientConnectStateChanged(state: ble.BLEConnectionChangeState) {
5. console.info('bluetooth connect state changed');
6. let connectState: ble.ProfileConnectionState = state.state;
7. }

9. try {
10. let gattClient: ble.GattClientDevice = ble.createGattClientDevice(device);
11. gattClient.on('BLEConnectionStateChange', clientConnectStateChanged);
12. } catch (err) {
13. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
14. }
```

**3. 发起连接**

通过创建的客户端实例，直接发起连接即可。通过连接状态变化事件判断是否已连接成功。

```
1. // 此处是伪代码
2. let device = 'XX:XX:XX:XX:XX:XX';

4. try {
5. let gattClient: ble.GattClientDevice = ble.createGattClientDevice(device);
6. gattClient.connect();
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

**4. 服务发现**

服务发现是获取服务端支持的所有服务能力集合的过程。客户端需要根据服务发现结果，判断服务端是否存在应用需要的服务能力。

* 后续的读写特征值、读写描述符等操作都需要在服务发现操作完成后进行，否则会失败。
* 后续的读写等操作中指定的特征值或描述符必须包含在服务能力集合中，否则会失败。

```
1. // 此处是伪代码
2. let device = 'XX:XX:XX:XX:XX:XX';

4. try {
5. let gattClient: ble.GattClientDevice = ble.createGattClientDevice(device);
6. // 此处是伪代码，需要连接上后，才可以调用
7. gattClient.getServices().then((result: Array<ble.GattService>) => {
8. console.info('getServices successfully:' + JSON.stringify(result));
9. });
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

**5. 传输数据**

传输数据通过操作服务端的特征值或者描述符实现。

**5.1 读取或写入特征值**

读取特征值操作，可以获取服务端特征值的数据内容。

写入特征值操作，可以更新服务端特征值的数据内容。

相关API请参考[readCharacteristicValue](../harmonyos-references/js-apis-bluetooth-ble.md#readcharacteristicvalue)和[writeCharacteristicValue](../harmonyos-references/js-apis-bluetooth-ble.md#writecharacteristicvalue)。

```
1. // 此处是伪代码
2. let device = 'XX:XX:XX:XX:XX:XX';
3. let descriptors: Array<ble.BLEDescriptor> = [];
4. let bufferDesc = new ArrayBuffer(2);
5. let descV = new Uint8Array(bufferDesc);
6. descV[0] = 11;
7. let descriptor: ble.BLEDescriptor = {
8. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
9. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
10. descriptorUuid: '00008888-0000-1000-8000-00805F9B34FB',
11. descriptorValue: bufferDesc
12. };
13. descriptors[0] = descriptor;
14. let bufferCCC = new ArrayBuffer(2);
15. let cccV = new Uint8Array(bufferCCC);
16. cccV[0] = 1;
17. let characteristic: ble.BLECharacteristic = {
18. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
19. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
20. characteristicValue: bufferCCC,
21. descriptors:descriptors
22. };

24. let gattClient: ble.GattClientDevice = ble.createGattClientDevice(device);

26. // 读取特征值
27. try {
28. gattClient.readCharacteristicValue(characteristic).then((outData: ble.BLECharacteristic) => {
29. });
30. } catch (err) {
31. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
32. }

34. // 写入特征值
35. try {
36. gattClient.writeCharacteristicValue(characteristic, ble.GattWriteType.WRITE, (err) => {
37. if (err) {
38. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
39. return;
40. }
41. console.info(TAG, 'writeCharacteristicValue success');
42. });
43. } catch (err) {
44. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
45. }
```

**5.2 读取或写入描述符**

读取描述符操作，可以获取服务端描述符的数据内容。

写入描述符操作，可以更新服务端描述符的数据内容。

相关API请参考[readDescriptorValue](../harmonyos-references/js-apis-bluetooth-ble.md#readdescriptorvalue)和[writeDescriptorValue](../harmonyos-references/js-apis-bluetooth-ble.md#writedescriptorvalue)。

```
1. // 此处是伪代码
2. let device = 'XX:XX:XX:XX:XX:XX';
3. let bufferDesc = new ArrayBuffer(2);
4. let descV = new Uint8Array(bufferDesc);
5. descV[0] = 11;
6. let descriptor: ble.BLEDescriptor = {
7. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
8. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
9. descriptorUuid: '00008888-0000-1000-8000-00805F9B34FB',
10. descriptorValue: bufferDesc
11. };
12. let gattClient: ble.GattClientDevice = ble.createGattClientDevice(device);

14. // 读取描述符
15. try {
16. gattClient.readDescriptorValue(descriptor).then((outData: ble.BLEDescriptor) => {
17. });
18. } catch (err) {
19. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
20. }

22. // 写入描述符
23. try {
24. gattClient.writeDescriptorValue(descriptor, (err) => {
25. if (err) {
26. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
27. return;
28. }
29. });
30. } catch (err) {
31. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
32. }
```

**5.3 接收服务端特征值变化通知或指示**

当服务端特征值的数据内容发生变化时，客户端可以通过接收服务端的特征值变化通知或者指示来实现更新数据。该服务端特征值需包含蓝牙标准协议定义的Client Characteristic Configuration描述符UUID（00002902-0000-1000-8000-00805f9b34fb），才能支持通知或者指示能力。

客户端收到服务端通知时，不需要回复确认；客户端收到服务端指示时，需要回复确认，蓝牙子系统会实现该操作，应用无需关注。

* 先订阅服务端特征值变化事件，详情请见[on('BLECharacteristicChange')](../harmonyos-references/js-apis-bluetooth-ble.md#onblecharacteristicchange)。
* 再使能服务端特征值变化通知或者指示能力，应用根据实际场景选择一种方式即可。相关API请参考[setCharacteristicChangeNotification](../harmonyos-references/js-apis-bluetooth-ble.md#setcharacteristicchangenotification)和[setCharacteristicChangeIndication](../harmonyos-references/js-apis-bluetooth-ble.md#setcharacteristicchangeindication)。

```
1. // 此处是伪代码
2. let device = 'XX:XX:XX:XX:XX:XX';

4. // 定义服务端特征值变化事件
5. function characteristicChange(characteristicChangeReq: ble.BLECharacteristic) {
6. let serviceUuid: string = characteristicChangeReq.serviceUuid;
7. let characteristicUuid: string = characteristicChangeReq.characteristicUuid;
8. let value: Uint8Array = new Uint8Array(characteristicChangeReq.characteristicValue);
9. }

11. let descriptors: Array<ble.BLEDescriptor> = [];
12. let arrayBuffer = new ArrayBuffer(2);
13. let descV = new Uint8Array(arrayBuffer);
14. descV[0] = 11;
15. let descriptor: ble.BLEDescriptor = {
16. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
17. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
18. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB',
19. descriptorValue: arrayBuffer
20. };
21. descriptors[0] = descriptor;
22. let arrayBufferC = new ArrayBuffer(2);
23. let characteristic: ble.BLECharacteristic = {
24. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
25. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
26. characteristicValue: arrayBufferC,
27. descriptors:descriptors
28. };

30. let gattClient: ble.GattClientDevice = ble.createGattClientDevice(device);

32. // 发起订阅
33. try {
34. gattClient.on('BLECharacteristicChange', characteristicChange);
35. } catch (err) {
36. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
37. }

39. // 通知和指示，2选1即可
40. // 设置特征值变化通知能力
41. try {
42. // enable入参: true表示启用，false表示禁用
43. gattClient.setCharacteristicChangeNotification(characteristic, true, (err: BusinessError) => {
44. if (err) {
45. console.error('setCharacteristicChangeNotification callback failed');
46. } else {
47. console.info('setCharacteristicChangeNotification callback successful');
48. }
49. });
50. } catch (err) {
51. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
52. }

54. // 设置特征值变化指示能力
55. try {
56. // enable入参: true表示启用，false表示禁用
57. gattClient.setCharacteristicChangeIndication(characteristic, true, (err: BusinessError) => {
58. if (err) {
59. console.error('setCharacteristicChangeIndication callback failed');
60. } else {
61. console.info('setCharacteristicChangeIndication callback successful');
62. }
63. });
64. } catch (err) {
65. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
66. }
```

**6. 断开连接**

当应用不再需要已建立的连接时，需主动断开连接。

```
1. // 此处是伪代码
2. let device = 'XX:XX:XX:XX:XX:XX';

4. let gattClient: ble.GattClientDevice = ble.createGattClientDevice(device);
5. try {
6. // 发起断连
7. gattClient.disconnect();

9. // 如果应用不再使用此gattClient，则需要close，gattClient实例将不能再使用
10. gattClient.close()
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```

### 服务端

**1. 创建服务端实例**

构造服务端实例，后续所有操作都基于该服务端实例。

```
1. try {
2. let gattServer: ble.GattServer = ble.createGattServer();
3. } catch (err) {
4. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
5. }
```

**2. 添加服务**

添加应用需要的服务，将在蓝牙子系统中注册指定的UUID服务。客户端会发起服务查询，判断服务端是否支持特定的服务。

```
1. // 创建descriptors
2. let descriptors: Array<ble.BLEDescriptor> = [];
3. let arrayBuffer = new ArrayBuffer(2);
4. let descV = new Uint8Array(arrayBuffer);
5. descV[0] = 11;
6. let descriptor: ble.BLEDescriptor = {
7. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
8. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
9. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB',
10. descriptorValue: arrayBuffer};
11. descriptors[0] = descriptor;

13. // 创建characteristics
14. let characteristics: Array<ble.BLECharacteristic> = [];
15. let arrayBufferC = new ArrayBuffer(2);
16. let cccV = new Uint8Array(arrayBufferC);
17. cccV[0] = 1;
18. let characteristic: ble.BLECharacteristic = {
19. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
20. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
21. characteristicValue: arrayBufferC,
22. descriptors:descriptors
23. };
24. characteristics[0] = characteristic;

26. // 创建gattService
27. let gattService: ble.GattService = {
28. serviceUuid:'00001810-0000-1000-8000-00805F9B34FB',
29. isPrimary: true,
30. characteristics:characteristics,
31. includeServices:[]
32. };

34. try {
35. let gattServer: ble.GattServer = ble.createGattServer();
36. gattServer.addService(gattService);
37. } catch (err) {
38. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
39. }
```

**3. 订阅连接状态变化事件**

通过订阅连接状态变化事件，可以获取实时的GATT连接状态以及客户端的设备地址。整个连接过程涉及多种状态的跃迁，其中[STATE\_CONNECTED](../harmonyos-references/js-apis-bluetooth-constant.md#profileconnectionstate)表示已连接，[STATE\_DISCONNECTED](../harmonyos-references/js-apis-bluetooth-constant.md#profileconnectionstate)表示已断连。

```
1. function ServerConnectStateChanged(state: ble.BLEConnectionChangeState) {
2. console.info('bluetooth connect state changed');
3. let connectState: ble.ProfileConnectionState = state.state;
4. let device = state.deviceId;
5. }

7. try {
8. let gattServer: ble.GattServer = ble.createGattServer();
9. gattServer.on('connectionStateChange', ServerConnectStateChanged);
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

**4. 传输数据**

传输数据可以通过客户端读写特征值数据内容、读写描述符数据内容、主动发送特征值数据内容变化通知或指示实现。

**4.1 订阅特征值读取或写入事件**

通过订阅特征值读取或写入事件，获取客户端的操作请求，相关API请参考[on('characteristicRead')](../harmonyos-references/js-apis-bluetooth-ble.md#oncharacteristicread)和[on('characteristicWrite')](../harmonyos-references/js-apis-bluetooth-ble.md#oncharacteristicwrite)。

* 收到读取特征值请求时，需要调用[sendResponse](../harmonyos-references/js-apis-bluetooth-ble.md#sendresponse)进行回复对应特征值的数据内容。
* 收到写入特征值请求时，可保存客户端写入的特征值数据内容。根据写入请求[CharacteristicWriteRequest](../harmonyos-references/js-apis-bluetooth-ble.md#characteristicwriterequest)的needRsp判断是否需要调用[sendResponse](../harmonyos-references/js-apis-bluetooth-ble.md#sendresponse)进行回复。

```
1. let gattServer: ble.GattServer = ble.createGattServer();
2. let arrayBufferCCC = new ArrayBuffer(2);
3. let cccValue = new Uint8Array(arrayBufferCCC);
4. cccValue[0] = 1;

6. // 定义特征值读取回调函数
7. function readCharacteristicReq(characteristicReadRequest: ble.CharacteristicReadRequest) {
8. let deviceId: string = characteristicReadRequest.deviceId;
9. let transId: number = characteristicReadRequest.transId;
10. let offset: number = characteristicReadRequest.offset;
11. let characteristicUuid: string = characteristicReadRequest.characteristicUuid;

13. let serverResponse: ble.ServerResponse = {
14. deviceId: deviceId,
15. transId: transId,
16. status: 0,
17. offset: offset,
18. value:arrayBufferCCC // 传入服务端对应特征值的数据内容，此处是伪代码
19. };

21. try {
22. gattServer.sendResponse(serverResponse);
23. } catch (err) {
24. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
25. }
26. }

28. // 定义特征值写入回调函数
29. function writeCharacteristicReq(characteristicWriteRequest: ble.CharacteristicWriteRequest) {
30. let deviceId: string = characteristicWriteRequest.deviceId;
31. let transId: number = characteristicWriteRequest.transId;
32. let offset: number = characteristicWriteRequest.offset;
33. let needRsp: boolean = characteristicWriteRequest.needRsp;
34. if (!needRsp) { // 判断是否需要回复客户端
35. return;
36. }
37. let value: Uint8Array =  new Uint8Array(characteristicWriteRequest.value); // 可保存写入的数据内容
38. let characteristicUuid: string = characteristicWriteRequest.characteristicUuid;
39. cccValue[0] = value[0];
40. let serverResponse: ble.ServerResponse = {
41. deviceId: deviceId,
42. transId: transId,
43. status: 0,
44. offset: offset,
45. value:arrayBufferCCC
46. };

48. try {
49. gattServer.sendResponse(serverResponse);
50. } catch (err) {
51. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
52. }
53. }

55. // 订阅特征值读取事件
56. gattServer.on('characteristicRead', readCharacteristicReq);

58. // 订阅特征值写入事件
59. gattServer.on('characteristicWrite', writeCharacteristicReq);
```

**4.2 订阅描述符读取或写入事件**

通过订阅描述符读取或写入事件，获取客户端的操作请求，相关API请参考[on('descriptorRead')](../harmonyos-references/js-apis-bluetooth-ble.md#ondescriptorread)和[on('descriptorWrite')](../harmonyos-references/js-apis-bluetooth-ble.md#ondescriptorwrite)。

* 收到读取描述符请求时，需要调用[sendResponse](../harmonyos-references/js-apis-bluetooth-ble.md#sendresponse)进行回复对应描述符的数据内容。
* 收到写入描述符请求时，可保存客户端写入的描述符数据内容。根据写入请求[DescriptorWriteRequest](../harmonyos-references/js-apis-bluetooth-ble.md#descriptorwriterequest)的needRsp判断是否需要调用[sendResponse](../harmonyos-references/js-apis-bluetooth-ble.md#sendresponse)进行回复。

```
1. let gattServer: ble.GattServer = ble.createGattServer();

3. // 定义描述符读取回调函数
4. let arrayBufferDesc = new ArrayBuffer(2);
5. let descValue = new Uint8Array(arrayBufferDesc);
6. descValue[0] = 1;
7. function readDescriptorReq(descriptorReadRequest: ble.DescriptorReadRequest) {
8. let deviceId: string = descriptorReadRequest.deviceId;
9. let transId: number = descriptorReadRequest.transId;
10. let offset: number = descriptorReadRequest.offset;
11. let descriptorUuid: string = descriptorReadRequest.descriptorUuid;

13. let serverResponse: ble.ServerResponse = {
14. deviceId: deviceId,
15. transId: transId,
16. status: 0,
17. offset: offset,
18. value:arrayBufferDesc
19. };

21. try {
22. gattServer.sendResponse(serverResponse);
23. } catch (err) {
24. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
25. }
26. }

28. // 定义描述符写入回调函数
29. function writeDescriptorReq(descriptorWriteRequest: ble.DescriptorWriteRequest) {
30. let deviceId: string = descriptorWriteRequest.deviceId;
31. let transId: number = descriptorWriteRequest.transId;
32. let offset: number = descriptorWriteRequest.offset;
33. let isPrepared: boolean = descriptorWriteRequest.isPrepared;
34. let needRsp: boolean = descriptorWriteRequest.needRsp;
35. if (!needRsp) { // 判断是否需要回复客户端
36. return;
37. }

39. let value: Uint8Array = new Uint8Array(descriptorWriteRequest.value); // 可保存写入的数据内容
40. let descriptorUuid: string = descriptorWriteRequest.descriptorUuid;
41. descValue[0] = value[0];
42. let serverResponse: ble.ServerResponse = {
43. deviceId: deviceId,
44. transId: transId,
45. status: 0,
46. offset: offset,
47. value:arrayBufferDesc
48. };

50. try {
51. gattServer.sendResponse(serverResponse);
52. } catch (err) {
53. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
54. }
55. }

57. // 订阅描述符读取事件
58. gattServer.on('descriptorRead', readDescriptorReq);

60. // 订阅描述符写入事件
61. gattServer.on('descriptorWrite', writeDescriptorReq);
```

**4.3 发送特征值变化通知或指示**

当服务端的特征值数据内容发生变化时，可以通过通知或者指示主动知会到客户端，相关API请参考[notifyCharacteristicChanged](../harmonyos-references/js-apis-bluetooth-ble.md#notifycharacteristicchanged)。

发送通知时，不需要客户端回复确认；发送指示时，需要客户端回复确认。应用根据[NotifyCharacteristic](../harmonyos-references/js-apis-bluetooth-ble.md#notifycharacteristic)的confirm参数决定发送哪种类型。

* 该特征值需包含蓝牙标准协议定义的Client Characteristic Configuration描述符UUID（00002902-0000-1000-8000-00805f9b34fb），才支持通知或者指示能力。
* 使用通知或者指示能力需要使能。客户端可以通过[setCharacteristicChangeNotification](../harmonyos-references/js-apis-bluetooth-ble.md#setcharacteristicchangenotification)或[setCharacteristicChangeIndication](../harmonyos-references/js-apis-bluetooth-ble.md#setcharacteristicchangeindication)使能该能力，应用根据实际场景选择一种方式即可。

```
1. let device = 'XX:XX:XX:XX:XX:XX'; // 该设备地址表示客户端地址，可以通过连接状态变化事件中获取
2. let arrayBufferC = new ArrayBuffer(2);
3. let notifyCharacter: ble.NotifyCharacteristic = {
4. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
5. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
6. characteristicValue: arrayBufferC,
7. confirm: true // 决定发送通知还是指示
8. };
9. try {
10. let gattServer: ble.GattServer = ble.createGattServer();
11. // 发送变更通知或指示
12. gattServer.notifyCharacteristicChanged(device, notifyCharacter, (err: BusinessError) => {
13. if (err) {
14. console.error('notifyCharacteristicChanged callback failed');
15. } else {
16. console.info('notifyCharacteristicChanged callback successful');
17. }
18. });
19. } catch (err) {
20. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
21. }
```

**5. 关闭服务端实例**

当应用不再需要创建的服务端实例时，需要主动关闭，并释放相关资源。例如：删除已添加的服务，取消已订阅事件。

```
1. try {
2. let gattServer: ble.GattServer = ble.createGattServer();
3. gattServer.removeService('00001810-0000-1000-8000-00805F9B34FB'); // 删除此前注册的服务
4. gattServer.close() // 应用不再使用此gattServer，则需要close
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

## 完整示例

### 客户端

```
1. import { ble, constant } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const TAG: string = 'GattClientManager';

6. export class GattClientManager {
7. device: string = '';
8. gattClient: ble.GattClientDevice | undefined = undefined;
9. connectState: ble.ProfileConnectionState = constant.ProfileConnectionState.STATE_DISCONNECTED;
10. myServiceUuid: string = '00001810-0000-1000-8000-00805F9B34FB';
11. myCharacteristicUuid: string = '00001820-0000-1000-8000-00805F9B34FB';
12. // 标准协议描述符Client Characteristic Configuration，用于特征值变化通知或指示
13. myFirstDescriptorUuid: string = '00002902-0000-1000-8000-00805F9B34FB';
14. // 自定义描述符
15. mySecondDescriptorUuid: string = '00008888-0000-1000-8000-00805F9B34FB';

17. myService: ble.GattService | undefined = undefined;
18. myCharacteristic: ble.BLECharacteristic | undefined = undefined;
19. myFirstDescriptor: ble.BLEDescriptor | undefined = undefined;
20. mySecondDescriptor: ble.BLEDescriptor | undefined = undefined;

22. foundService: boolean = false;
23. foundChar: boolean = false;
24. foundFirstDes: boolean = false;
25. foundSecondDes: boolean = false;

27. // 构造BLEDescriptor
28. private initDescriptor(des: string, value: ArrayBuffer): ble.BLEDescriptor {
29. let descriptor: ble.BLEDescriptor = {
30. serviceUuid: this.myServiceUuid,
31. characteristicUuid: this.myCharacteristicUuid,
32. descriptorUuid: des,
33. descriptorValue: value
34. };
35. return descriptor;
36. }

38. // 构造BLECharacteristic
39. private initCharacteristic(isWrite: boolean): ble.BLECharacteristic {
40. let descriptors: Array<ble.BLEDescriptor> = [];
41. let charBuffer = new ArrayBuffer(2);
42. if (isWrite) {
43. let charValue = new Uint8Array(charBuffer);
44. charValue[0] = 21;
45. charValue[1] = 22;
46. }
47. let characteristic: ble.BLECharacteristic = {
48. serviceUuid: this.myServiceUuid,
49. characteristicUuid: this.myCharacteristicUuid,
50. characteristicValue: charBuffer,
51. descriptors: descriptors
52. };
53. return characteristic;
54. }

56. private logCharacteristic(char: ble.BLECharacteristic) {
57. let message = 'logCharacteristic uuid:' + char.characteristicUuid + ', value: ';
58. let value = new Uint8Array(char.characteristicValue);
59. message += 'logCharacteristic value: ';
60. for (let i = 0; i < char.characteristicValue.byteLength; i++) {
61. message += value[i] + ' ';
62. }
63. console.info(TAG, message);
64. }

66. private logDescriptor(des: ble.BLEDescriptor) {
67. let message = 'logDescriptor uuid:' + des.descriptorUuid + ', value: ';
68. let value = new Uint8Array(des.descriptorValue);
69. message += 'logDescriptor value: ';
70. for (let i = 0; i < des.descriptorValue.byteLength; i++) {
71. message += value[i] + ' ';
72. }
73. console.info(TAG, message);
74. }

76. private checkService(services: Array<ble.GattService>) {
77. for (let i = 0; i < services.length; i++) {
78. if (services[i].serviceUuid != this.myServiceUuid) {
79. continue;
80. }
81. this.myService = services[i];
82. this.foundService = true;
83. for (let j = 0; j < services[i].characteristics.length; j++) {
84. if (services[i].characteristics[j].characteristicUuid != this.myCharacteristicUuid) {
85. continue;
86. }
87. this.logCharacteristic(services[i].characteristics[j]);
88. this.myCharacteristic = services[i].characteristics[j];
89. this.foundChar = true;
90. for (let k = 0; k < services[i].characteristics[j].descriptors.length; k++) {
91. if (services[i].characteristics[j].descriptors[k].descriptorUuid == this.myFirstDescriptorUuid) {
92. this.myFirstDescriptor= services[i].characteristics[j].descriptors[k];
93. this.foundFirstDes = true;
94. continue;
95. }
96. if (services[i].characteristics[j].descriptors[k].descriptorUuid == this.mySecondDescriptorUuid) {
97. this.mySecondDescriptor = services[i].characteristics[j].descriptors[k];
98. this.foundSecondDes = true;
99. continue;
100. }
101. }
102. }
103. }
104. console.info(TAG, 'foundService: ' + this.foundService + ', foundChar: ' + this.foundChar +
105. ', foundFirDes: ' + this.foundFirstDes + ', foundSecDes: ' + this.foundSecondDes);
106. }

108. // 1. 定义连接状态变化回调函数
109. onGattClientStateChange = (stateInfo: ble.BLEConnectionChangeState) => {
110. let state = '';
111. switch (stateInfo.state) {
112. case 0:
113. state = 'DISCONNECTED';
114. break;
115. case 1:
116. state = 'CONNECTING';
117. break;
118. case 2:
119. state = 'CONNECTED';
120. break;
121. case 3:
122. state = 'DISCONNECTING';
123. break;
124. default:
125. state = 'undefined';
126. break;
127. }
128. console.info(TAG, 'onGattClientStateChange: device=' + stateInfo.deviceId + ', state=' + state);
129. if (stateInfo.deviceId == this.device) {
130. this.connectState = stateInfo.state;
131. }
132. };

134. // 2. client端主动连接时调用
135. public startConnect(peerDevice: string) { // 对端设备一般通过ble查找设备获取到
136. if (this.connectState != constant.ProfileConnectionState.STATE_DISCONNECTED) {
137. console.error(TAG, 'startConnect failed');
138. return;
139. }
140. console.info(TAG, 'startConnect ' + peerDevice);
141. this.device = peerDevice;
142. // 2.1 使用device构造gattClient，后续的交互都需要使用该实例
143. this.gattClient = ble.createGattClientDevice(peerDevice);
144. try {
145. // 2.2 订阅连接状态
146. this.gattClient.on('BLEConnectionStateChange', this.onGattClientStateChange);

148. // 2.3 发起连接
149. this.gattClient.connect();
150. } catch (err) {
151. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
152. }
153. }

155. // 3. client端连接成功后，需要进行服务发现
156. public async discoverServices() {
157. if (!this.gattClient) {
158. console.error(TAG, 'gattClient does not exist');
159. return;
160. }
161. console.info(TAG, 'discoverServices');
162. try {
163. let serverService = await this.gattClient.getServices();
164. this.checkService(serverService); // 要确保server端的服务内容有业务所需要的服务
165. if (typeof this.myService !== 'undefined') {
166. console.info(TAG, 'Service: ' + JSON.stringify(this.myService));
167. }
168. if (typeof this.myCharacteristic !== 'undefined') {
169. this.logCharacteristic(this.myCharacteristic);
170. }
171. if (typeof this.myFirstDescriptor !== 'undefined') {
172. this.logDescriptor(this.myFirstDescriptor);
173. }
174. if (typeof this.mySecondDescriptor !== 'undefined') {
175. this.logDescriptor(this.mySecondDescriptor);
176. }
177. } catch (err) {
178. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
179. }
180. }

182. // 4. 在确保拿到了server端的服务结果后，读取server端特定服务的特征值时调用
183. public readCharacteristicValue() {
184. if (!this.gattClient || this.connectState != constant.ProfileConnectionState.STATE_CONNECTED) {
185. console.error(TAG, 'gattClient does not exist or state not connected');
186. return;
187. }
188. if (!this.foundChar) { // 要确保server端有对应的characteristic
189. console.error(TAG, 'server characteristic does not exist');
190. return;
191. }

193. let characteristic = this.initCharacteristic(false);
194. console.info(TAG, 'readCharacteristicValue');
195. try {
196. this.gattClient.readCharacteristicValue(characteristic).then((outData: ble.BLECharacteristic) => {
197. this.myCharacteristic = outData;
198. this.logCharacteristic(this.myCharacteristic);
199. });
200. } catch (err) {
201. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
202. }
203. }

205. // 5. 在确保拿到了server端的服务结果后，写入server端特定服务的特征值时调用
206. public writeCharacteristicValue() {
207. if (!this.gattClient || this.connectState != constant.ProfileConnectionState.STATE_CONNECTED) {
208. console.error(TAG, 'gattClient does not exist or state not connected');
209. return;
210. }
211. if (!this.foundChar) { // 要确保server端有对应的characteristic
212. console.error(TAG, 'server characteristic does not exist');
213. return;
214. }

216. let characteristic = this.initCharacteristic(true);
217. console.info(TAG, 'writeCharacteristicValue');
218. try {
219. this.gattClient.writeCharacteristicValue(characteristic, ble.GattWriteType.WRITE, (err) => {
220. if (err) {
221. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
222. return;
223. }
224. console.info(TAG, 'writeCharacteristicValue success');
225. });
226. } catch (err) {
227. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
228. }
229. }

231. // 6. 在确保拿到了server端的服务结果后，读取server端特定服务的描述符时调用
232. public readDescriptorValue() {
233. if (!this.gattClient || this.connectState != constant.ProfileConnectionState.STATE_CONNECTED) {
234. console.error(TAG, 'gattClient does not exist or state not connected');
235. return;
236. }
237. if (!this.foundSecondDes) { // 要确保server端有对应的descriptor
238. console.error(TAG, 'server descriptor does not exist');
239. return;
240. }

242. let descBuffer = new ArrayBuffer(0);
243. let descriptor = this.initDescriptor(this.mySecondDescriptorUuid, descBuffer);
244. console.info(TAG, 'readDescriptorValue');
245. try {
246. this.gattClient.readDescriptorValue(descriptor).then((outData: ble.BLEDescriptor) => {
247. this.logDescriptor(outData);
248. });
249. } catch (err) {
250. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
251. }
252. }

254. // 7. 在确保拿到了server端的服务结果后，写入server端特定服务的描述符时调用
255. public writeDescriptorValue() {
256. if (!this.gattClient || this.connectState != constant.ProfileConnectionState.STATE_CONNECTED) {
257. console.error(TAG, 'gattClient does not exist or state not connected');
258. return;
259. }
260. if (!this.foundSecondDes) { // 要确保server端有对应的descriptor
261. console.error(TAG, 'server descriptor does not exist');
262. return;
263. }

265. let descBuffer = new ArrayBuffer(2);
266. let descValue = new Uint8Array(descBuffer);
267. descValue[0] = 41;
268. descValue[1] = 42;
269. let descriptor = this.initDescriptor(this.mySecondDescriptorUuid, descBuffer);
270. console.info(TAG, 'writeDescriptorValue');
271. try {
272. this.gattClient.writeDescriptorValue(descriptor, (err) => {
273. if (err) {
274. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
275. return;
276. }
277. console.info(TAG, 'writeDescriptorValue success');
278. });
279. } catch (err) {
280. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
281. }
282. }

284. // 8. 定义特征值变化回调函数
285. onCharacteristicChange = (char: ble.BLECharacteristic) => {
286. console.info(TAG, 'onCharacteristicChange: uuid: ' + char.characteristicUuid + ', value: ' + JSON.stringify(new Uint8Array(char.characteristicValue)));
287. this.myCharacteristic = char;
288. this.logCharacteristic(this.myCharacteristic);
289. }

291. // 9. 使能或禁用接收服务端端特征值内容变更通知的能力时调用，一般通知或者指示，二选一
292. public Notify(enable: boolean) {
293. if (!this.gattClient || this.connectState != constant.ProfileConnectionState.STATE_CONNECTED) {
294. console.error(TAG, 'gattClient does not exist or state not connected');
295. return;
296. }

298. if (!this.foundFirstDes) { // 要确保server端有对应的client configuration descriptor
299. console.error(TAG, 'server client configuration descriptor does not exist');
300. return;
301. }

303. console.info(TAG, 'Notify ' + this.device + ' enable: ' + enable);
304. try {
305. // 订阅特征值变化
306. this.gattClient.on('BLECharacteristicChange', this.onCharacteristicChange);
307. // 设置特征值变化通知能力，enable: true表示启用，false表示禁用
308. this.gattClient.setCharacteristicChangeNotification(this.myCharacteristic, enable, (err: BusinessError) => {
309. if (err) {
310. console.error('setCharacteristicChangeNotification callback failed');
311. } else {
312. console.info('setCharacteristicChangeNotification callback successful');
313. }
314. });
315. } catch (err) {
316. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
317. }
318. }

320. // 10. 使能或禁用接收服务端端特征值内容变更指示的能力时调用，一般通知或者指示，二选一
321. public Indicate(enable: boolean) {
322. if (!this.gattClient || this.connectState != constant.ProfileConnectionState.STATE_CONNECTED) {
323. console.error(TAG, 'gattClient does not exist or state not connected');
324. return;
325. }

327. if (!this.foundFirstDes) { // 要确保server端有对应的client configuration descriptor
328. console.error(TAG, 'server client configuration descriptor does not exist');
329. return;
330. }

332. console.info(TAG, 'Indicate ' + this.device + ' enable: ' + enable);
333. try {
334. // 订阅特征值变化
335. this.gattClient.on('BLECharacteristicChange', this.onCharacteristicChange);
336. // 设置特征值变化指示能力，enable: true表示启用，false表示禁用
337. this.gattClient.setCharacteristicChangeIndication(this.myCharacteristic, enable, (err: BusinessError) => {
338. if (err) {
339. console.error('setCharacteristicChangeIndication callback failed');
340. } else {
341. console.info('setCharacteristicChangeIndication callback successful');
342. }
343. });
344. } catch (err) {
345. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
346. }
347. }

349. // 11.client端主动断开时调用
350. public stopConnect() {
351. if (!this.gattClient || this.connectState != constant.ProfileConnectionState.STATE_CONNECTED) {
352. console.error(TAG, 'gattClient does not exist or state not connected');
353. return;
354. }

356. console.info(TAG, 'stopConnect ' + this.device);
357. try {
358. this.gattClient.disconnect(); // 11.1 断开连接
359. this.gattClient.off('BLEConnectionStateChange', this.onGattClientStateChange); // 11.2 取消订阅连接状态
360. this.gattClient.off('BLECharacteristicChange', this.onCharacteristicChange); // 11.3 取消订阅特征值变化
361. this.gattClient.close() // 11.4 如果应用不再使用此gattClient，则需要close
362. } catch (err) {
363. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
364. }
365. }
366. }

368. let gattClientManager = new GattClientManager();
369. export default gattClientManager as GattClientManager;
```

### 服务端

```
1. import { ble, constant } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const TAG: string = 'GattServerManager';

6. export class GattServerManager {
7. device = '';
8. gattServer: ble.GattServer | undefined = undefined;
9. connectState: ble.ProfileConnectionState = constant.ProfileConnectionState.STATE_DISCONNECTED;
10. myServiceUuid: string = '00001810-0000-1000-8000-00805F9B34FB';
11. myCharacteristicUuid: string = '00001820-0000-1000-8000-00805F9B34FB';
12. // 标准协议描述符Client Characteristic Configuration，用于特征值变化通知或指示
13. myFirstDescriptorUuid: string = '00002902-0000-1000-8000-00805F9B34FB';
14. // 自定义描述符
15. mySecondDescriptorUuid: string = '00008888-0000-1000-8000-00805F9B34FB';

17. charBuffer = new ArrayBuffer(2);
18. charValue = new Uint8Array(this.charBuffer);

20. firDescBuffer = new ArrayBuffer(2);
21. firDescValue = new Uint8Array(this.firDescBuffer);

23. secDescBuffer = new ArrayBuffer(2);
24. secDescValue = new Uint8Array(this.secDescBuffer);

26. // 构造BLEDescriptor
27. private initDescriptor(des: string, value: ArrayBuffer): ble.BLEDescriptor {
28. let descriptor: ble.BLEDescriptor = {
29. serviceUuid: this.myServiceUuid,
30. characteristicUuid: this.myCharacteristicUuid,
31. descriptorUuid: des,
32. descriptorValue: value
33. };
34. return descriptor;
35. }

37. // 构造BLECharacteristic
38. private initCharacteristic(): ble.BLECharacteristic {
39. let descriptors: Array<ble.BLEDescriptor> = [];
40. // 默认Client Characteristic Configuration描述符没有使能特征值变化通知或者指示能力
41. descriptors[0] = this.initDescriptor(this.myFirstDescriptorUuid, this.firDescBuffer);
42. this.secDescValue[0] = 31;
43. this.secDescValue[1] = 32;
44. descriptors[1] = this.initDescriptor(this.mySecondDescriptorUuid, this.secDescBuffer);
45. this.charValue[0] = 1;
46. this.charValue[1] = 2;
47. let characteristic: ble.BLECharacteristic = {
48. serviceUuid: this.myServiceUuid,
49. characteristicUuid: this.myCharacteristicUuid,
50. characteristicValue: this.charBuffer,
51. descriptors: descriptors
52. };
53. return characteristic;
54. }

56. // 1. 定义连接状态变化回调函数
57. onGattServerStateChange = (stateInfo: ble.BLEConnectionChangeState) => {
58. let state = '';
59. switch (stateInfo.state) {
60. case 0:
61. state = 'DISCONNECTED';
62. break;
63. case 1:
64. state = 'CONNECTING';
65. break;
66. case 2:
67. state = 'CONNECTED';
68. break;
69. case 3:
70. state = 'DISCONNECTING';
71. break;
72. default:
73. state = 'undefined';
74. break;
75. }
76. console.info(TAG, 'onGattServerStateChange: device=' + stateInfo.deviceId + ', state=' + state);
77. this.device = stateInfo.deviceId;
78. }

80. // 2. 定义读取特征值请求回调函数
81. onCharacteristicRead = (charReq: ble.CharacteristicReadRequest) => {
82. let deviceId: string = charReq.deviceId;
83. let transId: number = charReq.transId;
84. let offset: number = charReq.offset;
85. console.info(TAG, 'receive characteristicRead: uuid: ' + charReq.characteristicUuid + ', value: ' + JSON.stringify(this.charValue));
86. let serverResponse: ble.ServerResponse = {
87. deviceId: deviceId,
88. transId: transId,
89. status: 0, // 0表示成功
90. offset: offset,
91. value: this.charBuffer
92. };

94. try {
95. this.gattServer?.sendResponse(serverResponse);
96. } catch (err) {
97. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
98. }
99. };

101. // 检查client configuration descriptor的通知能力是否使能
102. private checkDescriptorNotification(buffer: Uint8Array): boolean {
103. const notify = new ArrayBuffer(2);
104. let notifyValue = new Uint8Array(notify);
105. notifyValue.set([1, 0]); // 使能client configuration descriptor notification的值
106. return notifyValue.every((value, index) => value === buffer[index]);
107. }

109. // 检查client configuration descriptor的指示能力是否使能
110. private checkDescriptorIndication(buffer: Uint8Array): boolean {
111. const notify = new ArrayBuffer(2);
112. let notifyValue = new Uint8Array(notify);
113. notifyValue.set([2, 0]); // 使能client configuration descriptor indication的值
114. return notifyValue.every((value, index) => value === buffer[index]);
115. }

117. // 3. 定义写入特征值请求回调函数
118. onCharacteristicWrite = (charReq: ble.CharacteristicWriteRequest) => {
119. let deviceId: string = charReq.deviceId;
120. let transId: number = charReq.transId;
121. let offset: number = charReq.offset;
122. this.charBuffer = charReq.value;
123. this.charValue = new Uint8Array(charReq.value);
124. console.info(TAG, 'receive characteristicWrite: uuid: ' + charReq.characteristicUuid + ', needRsp=' + charReq.needRsp + ', value: ' + JSON.stringify(this.charValue));
125. if (!charReq.needRsp) {
126. return;
127. }
128. let rspBuffer = new ArrayBuffer(0);
129. let serverResponse: ble.ServerResponse = {
130. deviceId: deviceId,
131. transId: transId,
132. status: 0, // 0表示成功
133. offset: offset,
134. value: rspBuffer
135. };

137. try {
138. this.gattServer?.sendResponse(serverResponse);
139. this.sendCharacterChange(); // 此处特征值变化了，模拟主动发送变化通知或者指示
140. } catch (err) {
141. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
142. }
143. }

145. // 4. 定义读取描述符请求回调函数
146. onDescriptorRead = (desReq: ble.DescriptorReadRequest) => {
147. let deviceId: string = desReq.deviceId;
148. let transId: number = desReq.transId;
149. let offset: number = desReq.offset;
150. let tmpBuffer = new ArrayBuffer(2);
151. if (desReq.descriptorUuid == this.myFirstDescriptorUuid) {
152. tmpBuffer = this.firDescBuffer;
153. } else {
154. tmpBuffer = this.secDescBuffer;
155. }
156. let tmpValue = new Uint8Array(tmpBuffer);
157. console.info(TAG, 'receive descriptorRead: ' + desReq.descriptorUuid + ', tmpValue: ' + JSON.stringify(tmpValue));
158. let serverResponse: ble.ServerResponse = {
159. deviceId: deviceId,
160. transId: transId,
161. status: 0, // 0表示成功
162. offset: offset,
163. value: tmpBuffer
164. };

166. try {
167. this.gattServer?.sendResponse(serverResponse);
168. } catch (err) {
169. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
170. }
171. }

173. // 5. 定义写入描述符请求回调函数
174. onDescriptorWrite = (desReq: ble.DescriptorWriteRequest) => {
175. let deviceId: string = desReq.deviceId;
176. let transId: number = desReq.transId;
177. let offset: number = desReq.offset;
178. console.info(TAG, 'receive descriptorWrite: uuid: ' + desReq.descriptorUuid + ', needRsp: '+ desReq.needRsp + ', value: ' + JSON.stringify(new Uint8Array(desReq.value)));
179. if (desReq.descriptorUuid == this.myFirstDescriptorUuid) {
180. this.firDescBuffer = desReq.value;
181. this.firDescValue = new Uint8Array(desReq.value);
182. } else {
183. this.secDescBuffer = desReq.value;
184. this.secDescValue = new Uint8Array(desReq.value);
185. }
186. if (!desReq.needRsp) {
187. return;
188. }
189. let rspBuffer = new ArrayBuffer(0);
190. let serverResponse: ble.ServerResponse = {
191. deviceId: deviceId,
192. transId: transId,
193. status: 0, // 0表示成功
194. offset: offset,
195. value: rspBuffer
196. };

198. try {
199. this.gattServer?.sendResponse(serverResponse);
200. } catch (err) {
201. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
202. }
203. }

205. // 6. server端注册服务时调用
206. public registerServer() {
207. let characteristics: Array<ble.BLECharacteristic> = [];
208. let characteristic = this.initCharacteristic();
209. characteristics.push(characteristic);
210. let gattService: ble.GattService = {
211. serviceUuid: this.myServiceUuid,
212. isPrimary: true,
213. characteristics: characteristics
214. };

216. console.info(TAG, 'registerServer ' + this.myServiceUuid);
217. try {
218. this.gattServer = ble.createGattServer(); // 6.1 构造gattServer，后续的交互都需要使用该实例
219. this.gattServer.addService(gattService); // 6.2 注册服务
220. this.gattServer.on('connectionStateChange', this.onGattServerStateChange); // 6.3 订阅连接状态
221. this.gattServer.on('characteristicRead', this.onCharacteristicRead); // 6.4 订阅特征值读事件
222. this.gattServer.on('characteristicWrite', this.onCharacteristicWrite); // 6.5 订阅特征值写事件
223. this.gattServer.on('descriptorRead', this.onDescriptorRead); // 6.6 订阅描述符读事件
224. this.gattServer.on('descriptorWrite', this.onDescriptorWrite); // 6.7 订阅描述符写事件
225. } catch (err) {
226. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
227. }
228. }

230. // 7. 特征值内容发生变化时调用
231. public sendCharacterChange() {
232. console.info(TAG, 'sendCharacterChange: uuid: ' + this.myCharacteristicUuid + ', value: ' + JSON.stringify(new Uint8Array(this.charBuffer)));
233. if (this.checkDescriptorNotification(this.firDescValue)) {
234. let notifyCharacter: ble.NotifyCharacteristic = {
235. serviceUuid: this.myServiceUuid,
236. characteristicUuid: this.myCharacteristicUuid,
237. characteristicValue: this.charBuffer,
238. confirm: false
239. };
240. console.info(TAG, 'sendCharacterChange notification');
241. this.gattServer?.notifyCharacteristicChanged(this.device, notifyCharacter, (err: BusinessError) => {
242. if (err) {
243. console.error(TAG, 'notifyCharacteristicChanged notification callback failed');
244. } else {
245. console.info(TAG, 'notifyCharacteristicChanged notification callback successful');
246. }
247. });
248. } else if (this.checkDescriptorIndication(this.firDescValue)) {
249. let notifyCharacter: ble.NotifyCharacteristic = {
250. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
251. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
252. characteristicValue: this.charBuffer,
253. confirm: true
254. };
255. console.info(TAG, 'sendCharacterChange indication');
256. this.gattServer?.notifyCharacteristicChanged(this.device, notifyCharacter, (err: BusinessError) => {
257. if (err) {
258. console.error(TAG, 'notifyCharacteristicChanged indication callback failed');
259. } else {
260. console.info(TAG, 'notifyCharacteristicChanged indication callback successful');
261. }
262. });
263. } else {
264. console.info(TAG, 'notification/indication is disabled');
265. }
266. }

268. // 8. server端删除服务，不再使用时调用
269. public unRegisterServer() {
270. if (!this.gattServer) {
271. console.error(TAG, 'no gattServer');
272. return;
273. }

275. console.info(TAG, 'unRegisterServer ' + this.myServiceUuid);
276. try {
277. this.gattServer.removeService(this.myServiceUuid); // 8.1 删除服务
278. this.gattServer.off('connectionStateChange', this.onGattServerStateChange); // 8.2 取消订阅连接状态
279. this.gattServer.off('characteristicRead', this.onCharacteristicRead); // 8.3 取消订阅特征值读事件
280. this.gattServer.off('characteristicWrite', this.onCharacteristicWrite); // 8.4 取消订阅特征值写事件
281. this.gattServer.off('descriptorRead', this.onDescriptorRead); // 8.5 取消订阅描述符读事件
282. this.gattServer.off('descriptorWrite', this.onDescriptorWrite); // 8.6 取消订阅描述符写事件
283. this.gattServer.close() // 8.7 如果应用不再使用此gattServer，则需要close
284. } catch (err) {
285. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
286. }
287. }
288. }

290. let gattServerManager = new GattServerManager();
291. export default gattServerManager as GattServerManager;
```
