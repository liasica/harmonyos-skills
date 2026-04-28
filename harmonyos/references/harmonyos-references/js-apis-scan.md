---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-scan
title: @ohos.scan (扫描)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 数据文件处理 > @ohos.scan (扫描)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:32+08:00
doc_updated_at: 2026-04-03
content_hash: sha256:6db4902b9042ce9efb7b5b592e18459962f3ba74a6caa851d68d6cdac2b8058a
---

该模块为扫描框架的js-api接口文档，提供发现和连接扫描仪的能力。

说明

本模块首批接口从API version 20开始支持。

当前界面仅包含本模块的公开接口。

## 导入模块

PhonePC/2in1Tablet

```
1. import { scan } from '@kit.BasicServicesKit';
```

## ScanErrorCode

PhonePC/2in1Tablet

定义扫描错误码的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| SCAN\_ERROR\_NO\_PERMISSION | 201 | 无权限。 |
| SCAN\_ERROR\_NOT\_SYSTEM\_APPLICATION | 202 | 非系统应用。 |
| SCAN\_ERROR\_INVALID\_PARAMETER | 401 | 无效参数。 |
| SCAN\_ERROR\_GENERIC\_FAILURE | 13100001 | 通用失败。 |
| SCAN\_ERROR\_RPC\_FAILURE | 13100002 | RPC失败。 |
| SCAN\_ERROR\_SERVER\_FAILURE | 13100003 | 服务失败。 |
| SCAN\_ERROR\_UNSUPPORTED | 13100004 | 不支持的操作。 |
| SCAN\_ERROR\_CANCELED | 13100005 | 操作取消。 |
| SCAN\_ERROR\_DEVICE\_BUSY | 13100006 | 设备忙。 |
| SCAN\_ERROR\_INVALID | 13100007 | 无效操作。 |
| SCAN\_ERROR\_JAMMED | 13100008 | 卡纸。 |
| SCAN\_ERROR\_NO\_DOCS | 13100009 | 缺纸。 |
| SCAN\_ERROR\_COVER\_OPEN | 13100010 | 盖子打开。 |
| SCAN\_ERROR\_IO\_ERROR | 13100011 | I/O错误。 |
| SCAN\_ERROR\_NO\_MEMORY | 13100012 | 内存不足。 |

## ConstraintType

PhonePC/2in1Tablet

定义参数限制类型的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| SCAN\_CONSTRAINT\_NONE | 0 | 无限制。 |
| SCAN\_CONSTRAINT\_RANGE | 1 | 范围限制。 |
| SCAN\_CONSTRAINT\_WORD\_LIST | 2 | 数字列表。 |
| SCAN\_CONSTRAINT\_STRING\_LIST | 3 | 字符串列表。 |

## PhysicalUnit

PhonePC/2in1Tablet

定义物理单位的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| SCAN\_UNIT\_NONE | 0 | 无单位。 |
| SCAN\_UNIT\_PIXEL | 1 | 像素单位。 |
| SCAN\_UNIT\_BIT | 2 | 位单位。 |
| SCAN\_UNIT\_MM | 3 | 毫米单位。 |
| SCAN\_UNIT\_DPI | 4 | DPI单位。 |
| SCAN\_UNIT\_PERCENT | 5 | 百分比单位。 |
| SCAN\_UNIT\_MICROSECOND | 6 | 微秒单位。 |

## OptionValueType

PhonePC/2in1Tablet

定义选项值类型的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| SCAN\_TYPE\_BOOL | 0 | 布尔类型。 |
| SCAN\_TYPE\_INT | 1 | 整数类型。 |
| SCAN\_TYPE\_FIXED | 2 | 定点数类型。 |
| SCAN\_TYPE\_STRING | 3 | 字符串类型。 |

## ScannerSyncMode

PhonePC/2in1Tablet

定义扫描仪同步码的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| UPDATE\_STR | 'update' | 更新码，表示扫描仪id的变化。 |
| DELETE\_STR | 'delete' | 删除码，表示扫描仪掉线。 |

## ScannerDiscoveryMode

PhonePC/2in1Tablet

定义扫描仪发现方式的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| TCP\_STR | 'TCP' | 网络扫描仪的发现模式。 |
| USB\_STR | 'USB' | USB扫描仪的发现模式。 |

## Range

PhonePC/2in1Tablet

定义范围的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| minValue | number | 否 | 否 | 范围的最小值。 |
| maxValue | number | 否 | 否 | 范围的最大值。 |
| quantValue | number | 否 | 否 | 范围的量化值。 |

## ScannerParameter

PhonePC/2in1Tablet

定义扫描仪参数的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| optionName | string | 否 | 否 | 选项名称。 |
| optionIndex | number | 否 | 否 | 选项索引。 |
| optionTitle | string | 否 | 否 | 选项标题。 |
| optionDesc | string | 否 | 否 | 选项描述。 |
| optionType | [OptionValueType](js-apis-scan.md#optionvaluetype) | 否 | 否 | 选项值类型。 |
| optionUnit | [PhysicalUnit](js-apis-scan.md#physicalunit) | 否 | 否 | 选项物理单位。 |
| optionConstraintType | [ConstraintType](js-apis-scan.md#constrainttype) | 否 | 否 | 选项约束类型。 |
| optionConstraintString | string[] | 否 | 是 | 选项字符串约束。 |
| optionConstraintInt | number[] | 否 | 是 | 选项整数约束。 |
| optionConstraintRange | [Range](js-apis-scan.md#range) | 否 | 是 | 选项范围约束。 |

## ScannerOptionValue

PhonePC/2in1Tablet

定义扫描仪选项值的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| valueType | [OptionValueType](js-apis-scan.md#optionvaluetype) | 否 | 否 | 值类型。 |
| numValue | number | 否 | 是 | 数值。 |
| strValue | string | 否 | 是 | 字符串值。 |
| boolValue | boolean | 否 | 是 | 布尔值。 |

## PictureScanProgress

PhonePC/2in1Tablet

定义图片扫描进度的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| progress | number | 否 | 否 | 当前进度百分比，范围从0~100。单位：百分比。 |
| pictureFd | number | 否 | 否 | 扫描图片的文件描述符。 |
| isFinal | boolean | 否 | 否 | 是否是本次扫描的最后一张图片。true表示是最后一张图片，false表示不是最后一张图片。 |

## ScannerDevice

PhonePC/2in1Tablet

定义扫描仪设备的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| scannerId | string | 否 | 否 | 扫描仪的唯一标识符。 |
| discoveryMode | [ScannerDiscoveryMode](js-apis-scan.md#scannerdiscoverymode) | 否 | 否 | 扫描仪的发现模式。 |
| uniqueId | string | 否 | 否 | 扫描仪的唯一ID。 |
| manufacturer | string | 否 | 否 | 扫描仪的制造商。 |
| model | string | 否 | 否 | 扫描仪的型号。 |
| deviceName | string | 否 | 否 | 扫描仪的设备名称。 |

## ScannerSyncDevice

PhonePC/2in1Tablet

定义扫描仪同步设备的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| scannerId | string | 否 | 否 | 扫描仪ID。 |
| discoveryMode | [ScannerDiscoveryMode](js-apis-scan.md#scannerdiscoverymode) | 否 | 否 | 发现模式。 |
| uniqueId | string | 否 | 否 | 唯一ID。 |
| syncMode | [ScannerSyncMode](js-apis-scan.md#scannersyncmode) | 否 | 否 | 同步模式。 |
| oldScannerId | string | 否 | 是 | 旧的扫描仪ID，仅在syncMode为"update"时有效。 |

## scan.init

PhonePC/2in1Tablet

init(): Promise<void>

初始化扫描服务。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { scan } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. scan.init().then(() => {
5. console.info('scan init success');
6. }).catch((error: BusinessError) => {
7. console.error('scan init failed: ' + JSON.stringify(error));
8. })
```

## scan.exit

PhonePC/2in1Tablet

exit(): Promise<void>

退出扫描服务。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { scan } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. scan.exit().then(() => {
5. console.info('scan exit success');
6. }).catch((error: BusinessError) => {
7. console.error('scan exit failed: ' + JSON.stringify(error));
8. })
```

## scan.startScannerDiscovery

PhonePC/2in1Tablet

startScannerDiscovery(): Promise<void>

开始发现扫描仪。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { scan } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. scan.startScannerDiscovery().then(() => {
5. console.info('start scanner discovery success');
6. }).catch((error: BusinessError) => {
7. console.error('start scanner discovery failed: ' + JSON.stringify(error));
8. })
```

## scan.openScanner

PhonePC/2in1Tablet

openScanner(scannerId: string): Promise<void>

打开扫描仪。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| scannerId | string | 是 | 要打开的扫描仪的ID。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { scan } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let scannerId: string = 'scanner_001';
5. scan.openScanner(scannerId).then(() => {
6. console.info('open scanner success');
7. }).catch((error: BusinessError) => {
8. console.error('open scanner failed: ' + JSON.stringify(error));
9. })
```

## scan.closeScanner

PhonePC/2in1Tablet

closeScanner(scannerId: string): Promise<void>

关闭扫描仪。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| scannerId | string | 是 | 要关闭的扫描仪的ID。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { scan } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let scannerId: string = 'scanner_001';
5. scan.closeScanner(scannerId).then(() => {
6. console.info('close scanner success');
7. }).catch((error: BusinessError) => {
8. console.error('close scanner failed: ' + JSON.stringify(error));
9. })
```

## scan.getScannerParameter

PhonePC/2in1Tablet

getScannerParameter(scannerId: string): Promise<ScannerParameter[]>

获取扫描仪参数。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| scannerId | string | 是 | 扫描仪的ID。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[ScannerParameter](js-apis-scan.md#scannerparameter)[]> | Promise对象，返回扫描仪参数数组。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { scan } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let scannerId: string = 'scanner_001';
5. scan.getScannerParameter(scannerId).then((parameters: scan.ScannerParameter[]) => {
6. console.info('get scanner parameters success: ' + JSON.stringify(parameters));
7. }).catch((error: BusinessError) => {
8. console.error('get scanner parameters failed: ' + JSON.stringify(error));
9. })
```

## scan.setScannerParameter

PhonePC/2in1Tablet

setScannerParameter(scannerId: string, optionIndex: number, value: ScannerOptionValue): Promise<void>

设置扫描仪参数。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| scannerId | string | 是 | 扫描仪的ID。 |
| optionIndex | number | 是 | 要设置的选项的索引。 |
| value | [ScannerOptionValue](js-apis-scan.md#scanneroptionvalue) | 是 | 要设置的值。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { scan } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let scannerId: string = 'scanner_001';
5. let optionIndex: number = 1;
6. let value: scan.ScannerOptionValue = {
7. valueType: scan.OptionValueType.SCAN_TYPE_INT,
8. numValue: 100
9. };
10. scan.setScannerParameter(scannerId, optionIndex, value).then(() => {
11. console.info('set scanner parameter success');
12. }).catch((error: BusinessError) => {
13. console.error('set scanner parameter failed: ' + JSON.stringify(error));
14. })
```

## scan.setScanAutoOption

PhonePC/2in1Tablet

setScanAutoOption(scannerId: string, optionIndex: number): Promise<void>

设置扫描选项为自动模式。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| scannerId | string | 是 | 扫描仪的ID。 |
| optionIndex | number | 是 | 要设置为自动的选项的索引。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { scan } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let scannerId: string = 'scanner_001';
5. let optionIndex: number = 1;
6. scan.setScanAutoOption(scannerId, optionIndex).then(() => {
7. console.info('set scan auto option success');
8. }).catch((error: BusinessError) => {
9. console.error('set scan auto option failed: ' + JSON.stringify(error));
10. })
```

## scan.getScannerCurrentSetting

PhonePC/2in1Tablet

getScannerCurrentSetting(scannerId: string, optionIndex: number): Promise<ScannerOptionValue>

获取当前扫描仪设置。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| scannerId | string | 是 | 扫描仪的ID。 |
| optionIndex | number | 是 | 要获取的选项的索引。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[ScannerOptionValue](js-apis-scan.md#scanneroptionvalue)> | Promise对象，返回扫描仪选项值。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { scan } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let scannerId: string = 'scanner_001';
5. let optionIndex: number = 1;
6. scan.getScannerCurrentSetting(scannerId, optionIndex).then((value: scan.ScannerOptionValue) => {
7. console.info('get scanner current setting success: ' + JSON.stringify(value));
8. }).catch((error: BusinessError) => {
9. console.error('get scanner current setting failed: ' + JSON.stringify(error));
10. })
```

## scan.startScan

PhonePC/2in1Tablet

startScan(scannerId: string, batchMode: boolean): Promise<void>

开始扫描。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| scannerId | string | 是 | 扫描仪的ID。 |
| batchMode | boolean | 是 | 是否使用批处理模式。true表示使用批处理模式，false表示不使用批处理模式。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { scan } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let scannerId: string = 'scanner_001';
5. let batchMode: boolean = true;
6. scan.startScan(scannerId, batchMode).then(() => {
7. console.info('start scan success');
8. }).catch((error: BusinessError) => {
9. console.error('start scan failed: ' + JSON.stringify(error));
10. })
```

## scan.cancelScan

PhonePC/2in1Tablet

cancelScan(scannerId: string): Promise<void>

取消扫描。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| scannerId | string | 是 | 扫描仪的ID。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { scan } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let scannerId: string = 'scanner_001';
5. scan.cancelScan(scannerId).then(() => {
6. console.info('cancel scan success');
7. }).catch((error: BusinessError) => {
8. console.error('cancel scan failed: ' + JSON.stringify(error));
9. })
```

## scan.getPictureScanProgress

PhonePC/2in1Tablet

getPictureScanProgress(scannerId: string): Promise<PictureScanProgress>

获取图片扫描进度。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| scannerId | string | 是 | 扫描仪的ID。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[PictureScanProgress](js-apis-scan.md#picturescanprogress)> | Promise对象，返回图片扫描进度信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { scan } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let scannerId: string = 'scanner_001';
5. scan.getPictureScanProgress(scannerId).then((progress: scan.PictureScanProgress) => {
6. console.info('get picture scan progress success: ' + JSON.stringify(progress));
7. }).catch((error: BusinessError) => {
8. console.error('get picture scan progress failed: ' + JSON.stringify(error));
9. })
```

## scan.on

PhonePC/2in1Tablet

on(type: 'scanDeviceFound', callback: Callback<ScannerDevice>): void

注册扫描仪设备发现事件回调。使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | 'scanDeviceFound' | 是 | 事件类型。 |
| callback | Callback<[ScannerDevice](js-apis-scan.md#scannerdevice)> | 是 | 回调函数，返回扫描仪设备发现信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { scan } from '@kit.BasicServicesKit';

3. scan.on('scanDeviceFound', (device: scan.ScannerDevice) => {
4. console.info('scan device found: ' + JSON.stringify(device));
5. })
```

## scan.off

PhonePC/2in1Tablet

off(type: 'scanDeviceFound', callback?: Callback<ScannerDevice>): void

取消注册扫描仪设备发现事件回调。使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | 'scanDeviceFound' | 是 | 事件类型。 |
| callback | Callback<[ScannerDevice](js-apis-scan.md#scannerdevice)> | 否 | 回调函数，返回扫描仪设备发现信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { scan } from '@kit.BasicServicesKit';

3. let callback = (device: scan.ScannerDevice) => {
4. console.info('scan device found: ' + JSON.stringify(device));
5. };
6. scan.on('scanDeviceFound', callback);
7. // 取消注册
8. scan.off('scanDeviceFound', callback);
```

## scan.on

PhonePC/2in1Tablet

on(type: 'scanDeviceSync', callback: Callback<ScannerSyncDevice>): void

注册扫描仪设备同步事件回调。使用callback异步回调。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | 'scanDeviceSync' | 是 | 事件类型。 |
| callback | Callback<[ScannerSyncDevice](js-apis-scan.md#scannersyncdevice)> | 是 | 回调函数，返回扫描仪设备同步信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { scan } from '@kit.BasicServicesKit';

3. scan.on('scanDeviceSync', (device: scan.ScannerSyncDevice) => {
4. console.info('scan device sync: ' + JSON.stringify(device));
5. })
```

## scan.off

PhonePC/2in1Tablet

off(type: 'scanDeviceSync', callback?: Callback<ScannerSyncDevice>): void

取消注册扫描仪设备同步事件回调。使用callback异步回调。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | 'scanDeviceSync' | 是 | 事件类型。 |
| callback | Callback<[ScannerSyncDevice](js-apis-scan.md#scannersyncdevice)> | 否 | 回调函数，返回扫描仪设备同步信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { scan } from '@kit.BasicServicesKit';

3. let callback = (device: scan.ScannerSyncDevice) => {
4. console.info('scan device sync: ' + JSON.stringify(device));
5. };
6. scan.on('scanDeviceSync', callback);
7. // 取消注册
8. scan.off('scanDeviceSync', callback);
```
