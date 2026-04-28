---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-start-scan
title: 发起星闪扫描
breadcrumb: 指南 > 系统 > 网络 > NearLink Kit（星闪服务） > 发起星闪扫描
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bb42c37e7927fd4b30db080540ad8f94f3b26f0549414429bec155c0f4c94635
---

## 场景介绍

发起星闪扫描，可以扫描到正在发送星闪广播的外围设备。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [startScan](../harmonyos-references/nearlink-scan.md#startscan)(filters: Array<ScanFilters>, options?: ScanOptions): Promise<void> | 启动星闪扫描。 |
| [stopScan](../harmonyos-references/nearlink-scan.md#stopscan)(): Promise<void> | 停止星闪扫描。 |
| [on](../harmonyos-references/nearlink-scan.md#on-devicefound)(type: 'deviceFound', callback: Callback<Array<ScanResults>>): void | 订阅扫描结果。 |
| [off](../harmonyos-references/nearlink-scan.md#off-devicefound)(type: 'deviceFound', callback?: Callback<Array<ScanResults>>): void | 取消订阅扫描结果。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { scan } from '@kit.NearLinkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { util } from '@kit.ArkTS';
   ```
2. 定义扫描结果回调，解析扫描结果。

   ```
   1. const SLE_ADV_DATA_TYPE_DISCOVERY_LEVEL = 0x01;
   2. const SLE_ADV_DATA_TYPE_SERVICE_DATA_16BIT_UUID = 0x03;
   3. const SLE_ADV_DATA_TYPE_SERVICE_DATA_128BIT_UUID = 0x04;
   4. const SLE_ADV_DATA_TYPE_COMPLETE_LIST_OF_16BIT_SERVICE_UUIDS = 0x05;
   5. const SLE_ADV_DATA_TYPE_COMPLETE_LIST_OF_128BIT_SERVICE_UUIDS = 0x06;
   6. const SLE_ADV_DATA_TYPE_INCOMPLETE_LIST_OF_16BIT_SERVICE_UUIDS = 0x07;
   7. const SLE_ADV_DATA_TYPE_INCOMPLETE_LIST_OF_128BIT_SERVICE_UUIDS = 0x08;
   8. const SLE_ADV_DATA_TYPE_SHORTENED_LOCAL_NAME = 0x0A;
   9. const SLE_ADV_DATA_TYPE_COMPLETE_LOCAL_NAME = 0x0B;
   10. const SLE_ADV_DATA_TYPE_MANUFACTURER_SPECIFIC_DATA = 0xFF;

   12. const NEARLINK_UUID_16_BIT_LENGTH = 2;
   13. const NEARLINK_UUID_128_BIT_LENGTH = 16;

   15. const NEARLINK_MANUFACTURE_ID_LENGTH = 2;

   17. // 定义扫描结果回调
   18. let onReceiveEvent:(data: Array<scan.ScanResults>) => void = (data: Array<scan.ScanResults>) => {
   19. console.info('scan result addr:'+ data[0].address + 'name:' + data[0].deviceName);
   20. parseScanResult(data[0].data);
   21. }

   23. // 按照数据类型解析扫描结果
   24. function parseScanResult(data: ArrayBuffer) {
   25. let advData = new Uint8Array(data);
   26. if (advData.byteLength == 0) {
   27. console.warn('nothing, adv data length is 0');
   28. return;
   29. }
   30. console.info('advData: ' + JSON.stringify(advData));

   32. let discoveryLevel: number = -1;
   33. let serviceData: Record<string, Uint8Array> = {};
   34. let standardUuids: string[] = [];
   35. let specificUuids: string[] = [];
   36. let localName: string = "";
   37. let manufactureSpecificData: Record<number, Uint8Array> = {};

   39. let curPos: number= 0;
   40. while (curPos < advData.byteLength) {
   41. let advDataType: number = advData[curPos++];
   42. let advDataLength: number = advData[curPos++];
   43. if (advDataLength == 0) {
   44. break;
   45. }
   46. switch (advDataType) {
   47. case SLE_ADV_DATA_TYPE_DISCOVERY_LEVEL: // 发现等级
   48. discoveryLevel = advData[curPos];
   49. break;
   50. case SLE_ADV_DATA_TYPE_SERVICE_DATA_16BIT_UUID: // 标准服务数据信息
   51. parseServiceData(NEARLINK_UUID_16_BIT_LENGTH, curPos, advDataLength, advData, serviceData);
   52. break;
   53. case SLE_ADV_DATA_TYPE_SERVICE_DATA_128BIT_UUID: // 自定义服务数据信息
   54. parseServiceData(NEARLINK_UUID_128_BIT_LENGTH, curPos, advDataLength, advData, serviceData);
   55. break;
   56. case SLE_ADV_DATA_TYPE_COMPLETE_LIST_OF_16BIT_SERVICE_UUIDS: // 完整标准服务标识列表
   57. case SLE_ADV_DATA_TYPE_INCOMPLETE_LIST_OF_16BIT_SERVICE_UUIDS: // 部分标准服务标识列表
   58. parseServiceUuid(NEARLINK_UUID_16_BIT_LENGTH, curPos, advDataLength, advData, standardUuids);
   59. break;
   60. case SLE_ADV_DATA_TYPE_COMPLETE_LIST_OF_128BIT_SERVICE_UUIDS: // 完整自定义服务标识列表
   61. case SLE_ADV_DATA_TYPE_INCOMPLETE_LIST_OF_128BIT_SERVICE_UUIDS: // 部分自定义服务标识列表
   62. parseServiceUuid(NEARLINK_UUID_128_BIT_LENGTH, curPos, advDataLength, advData, specificUuids);
   63. break;
   64. case SLE_ADV_DATA_TYPE_SHORTENED_LOCAL_NAME: // 设备缩写本地名称
   65. case SLE_ADV_DATA_TYPE_COMPLETE_LOCAL_NAME: // 设备完整本地名称
   66. let tmpName: Uint8Array = advData.slice(curPos, curPos + advDataLength);
   67. let decoder = util.TextDecoder.create('utf-8');
   68. localName = decoder.decodeToString(new Uint8Array(tmpName));
   69. break;
   70. case SLE_ADV_DATA_TYPE_MANUFACTURER_SPECIFIC_DATA: // 厂商自定义信息
   71. parseManufactureData(curPos, advDataLength, advData, manufactureSpecificData);
   72. break;
   73. default:
   74. break;
   75. }
   76. curPos += advDataLength;
   77. }
   78. }

   80. // 解析服务数据信息
   81. function parseServiceData (uuidLength: number, curPos: number, advDataLength: number,
   82. advData: Uint8Array, serviceData: Record<string, Uint8Array>) {
   83. let tmpUuid: Uint8Array = advData.slice(curPos, curPos + uuidLength);
   84. getUuidFromUint8Array(uuidLength, tmpUuid);
   85. let tmpValue: Uint8Array = advData.slice(curPos + uuidLength, curPos + advDataLength);
   86. serviceData[tmpUuid.toString()] = tmpValue;
   87. }

   89. // 解析服务标识列表
   90. function parseServiceUuid (uuidLength: number, curPos: number, advDataLength: number,
   91. advData: Uint8Array, serviceUuids: string[]) {
   92. while (advDataLength > 0) {
   93. let tmpData: Uint8Array = advData.slice(curPos, curPos + uuidLength);
   94. serviceUuids.push(getUuidFromUint8Array(uuidLength, tmpData));
   95. advDataLength -= uuidLength;
   96. curPos += uuidLength;
   97. }
   98. }

   100. // 解析厂商自定义信息
   101. function parseManufactureData(curPos: number, advDataLength: number,
   102. advData: Uint8Array, manufactureSpecificData: Record<number, Uint8Array>) {
   103. let manufactureId: number = (advData[curPos + 1] << 8) + advData[curPos];
   104. let tmpValue: Uint8Array = advData.slice(curPos + NEARLINK_MANUFACTURE_ID_LENGTH, curPos + advDataLength);
   105. manufactureSpecificData[manufactureId] = tmpValue;
   106. }

   108. // 解析UUID
   109. function getUuidFromUint8Array(uuidLength: number, uuidData: Uint8Array): string {
   110. let uuid: string = '';
   111. let temp: string = '';
   112. for (let i = uuidLength - 1; i > -1; i--) {
   113. temp += uuidData[i].toString(16).padStart(2, '0');
   114. }
   115. switch (uuidLength) {
   116. case NEARLINK_UUID_16_BIT_LENGTH:
   117. uuid = `37BEA880-FC70-11EA-B720-00000000${temp}`;
   118. break;
   119. case NEARLINK_UUID_128_BIT_LENGTH:
   120. uuid = `${temp.substring(0, 8)}-${temp.substring(8, 12)}-${temp.substring(12, 16)}-${temp.substring(16,
   121. 20)}-${temp.substring(20, 32)}`;
   122. break;
   123. default:
   124. break;
   125. }
   126. return uuid;
   127. }
   ```
3. 订阅扫描结果。

   ```
   1. try {
   2. scan.on("deviceFound", onReceiveEvent);
   3. // 订阅星闪扫描结果。返回的扫描结果中携带的地址为远端设备随机地址。
   4. } catch (err) {
   5. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   6. }
   ```
4. 配置扫描参数，扫描过滤器配置期望的设备名称、地址等信息。

   注意

   1. 扫描过滤器至少携带一个过滤条件，否则扫描过滤器无效。
   2. 过滤器可以配置多组，组之间的条件是或的关系，如步骤5所示。
   3. 一组过滤器内的条件是与的关系，如下示例：address和deviceName同时满足才会上报。

   ```
   1. let scanFilter1: scan.ScanFilters = {
   2. address:"11:22:33:44:AA:BB", // 期望扫描到的外围设备1的地址
   3. deviceName:"deviceName1" // 期望扫描到的外围设备1的名称
   4. };
   5. let scanFilter2: scan.ScanFilters = {
   6. address:"22:33:44:AB:CD:EF", // 期望扫描到的外围设备2的地址
   7. deviceName:"deviceName2" // 期望扫描到的外围设备2的名称
   8. };
   9. let scanOptions: scan.ScanOptions = {
   10. scanMode: scan.ScanMode.SCAN_MODE_LOW_POWER
   11. }
   ```
5. 开启星闪扫描，参数配置在步骤4中构造。

   ```
   1. try {
   2. scan.startScan([scanFilter1, scanFilter2], scanOptions).then(() => {
   3. console.info("start scan success");
   4. }).catch ((err: BusinessError) => {
   5. console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
   6. });
   7. } catch (err) {
   8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   9. }
   ```
6. 停止星闪扫描。

   ```
   1. try {
   2. scan.stopScan().then(() => {
   3. console.info("stop scan success");
   4. }).catch ((err: BusinessError) => {
   5. console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
   6. });
   7. } catch (err) {
   8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   9. }
   ```
7. 取消订阅扫描结果，其中onReceiveEvent是在步骤3中注册的回调函数。

   ```
   1. try {
   2. scan.off("deviceFound", onReceiveEvent);
   3. } catch (err) {
   4. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   5. }
   ```

## 示例代码

星闪扫描场景可参考[星闪示例代码](https://gitcode.com/harmonyos_samples/nearlink-kit_-sample-code)，entry/src/main/ets/pages/ScanConfigPage.ets中的实现方法。
