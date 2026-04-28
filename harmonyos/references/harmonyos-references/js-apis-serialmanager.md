---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-serialmanager
title: @ohos.usbManager.serial (串口管理)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 设备管理 > @ohos.usbManager.serial (串口管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:571a75b08eef44ee6c8c29878e91a4365d0a8cca983c5279f966b4e36bd166d2
---

本模块主要提供串口管理功能，包括打开和关闭设备的串口、写入和读取数据、设置和获取串口的配置参数、权限管理等。

说明

本模块首批接口从API version 19开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PC/2in1

```
1. import { serialManager } from '@kit.BasicServicesKit';
```

## serialManager.getPortList

PC/2in1

getPortList(): Readonly<SerialPort>[]

查询串口设备清单，包括设备名称和对应的端口号。

**系统能力：** SystemCapability.USB.USBManager.Serial

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Readonly<[SerialPort](js-apis-serialmanager.md#serialport)>[] | 串口信息列表。 |

**示例：**

说明

以下示例代码只是调用getPortList接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```
1. import { JSON } from '@kit.ArkTS';
2. import { serialManager } from '@kit.BasicServicesKit';

4. // 获取串口设备清单
5. function getPortList() {
6. let portList: serialManager.SerialPort[] = serialManager.getPortList();
7. console.info('usbSerial portList: ' + JSON.stringify(portList));
8. if (!portList || portList.length === 0) {
9. console.error('usbSerial portList is empty');
10. return;
11. }
12. let portId: number = portList[0].portId;
13. }
```

## serialManager.hasSerialRight

PC/2in1

hasSerialRight(portId: number): boolean

检查应用程序是否具有访问串口设备的权限。应用退出后再拉起时，需要重新申请授权。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| portId | number | 是 | 端口号，来自[getPortList](js-apis-serialmanager.md#serialmanagergetportlist)获取的串口参数SerialPort。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示已授权，false表示未授权。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14400005 | Database operation exception. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |

**示例：**

说明

以下示例代码只是调用hasSerialRight接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```
1. import { JSON } from '@kit.ArkTS';
2. import { serialManager } from '@kit.BasicServicesKit';

4. // 获取串口列表
5. function hasSerialRight() {
6. let portList: serialManager.SerialPort[] = serialManager.getPortList();
7. console.info('portList: ', JSON.stringify(portList));
8. if (!portList || portList.length === 0) {
9. console.error('portList is empty');
10. return;
11. }
12. let portId: number = portList[0].portId;

14. // 检测设备是否可被应用访问
15. if (serialManager.hasSerialRight(portId)) {
16. console.info('The serial port is accessible');
17. } else {
18. console.error('No permission to access the serial port');
19. }
20. }
```

## serialManager.requestSerialRight

PC/2in1

requestSerialRight(portId: number): Promise<boolean>

请求应用程序访问串口设备的权限。应用退出自动移除对串口设备的访问权限，在应用重启后需要重新申请授权。使用Promise异步回调。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| portId | number | 是 | 端口号，来自[getPortList](js-apis-serialmanager.md#serialmanagergetportlist)获取的串口参数SerialPort。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，true表示请求权限成功，false表示请求权限失败。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14400005 | Database operation exception. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |

**示例：**

说明

以下示例代码只是调用requestSerialRight接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```
1. import { JSON } from '@kit.ArkTS';
2. import { serialManager } from '@kit.BasicServicesKit';

4. // 获取串口列表
5. function requestSerialRight() {
6. let portList: serialManager.SerialPort[] = serialManager.getPortList();
7. console.info('usbSerial portList: ' + JSON.stringify(portList));
8. if (!portList || portList.length === 0) {
9. console.error('usbSerial portList is empty');
10. return;
11. }
12. let portId: number = portList[0].portId;

14. // 检测设备是否可被应用访问
15. if (!serialManager.hasSerialRight(portId)) {
16. serialManager.requestSerialRight(portId).then(result => {
17. if (!result) {
18. // 没有访问设备的权限且用户不授权则退出
19. console.error('user is not granted the operation permission');
20. return;
21. } else {
22. console.info('grant permission successfully');
23. }
24. });
25. }
26. }
```

## serialManager.open

PC/2in1

open(portId: number): void

打开串口设备。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| portId | number | 是 | 端口号，来自[getPortList](js-apis-serialmanager.md#serialmanagergetportlist)获取的串口参数SerialPort。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 31400001 | Serial port management exception. |
| 31400002 | Access denied. Call requestSerialRight to request user authorization first. |
| 31400003 | PortId does not exist. |
| 31400004 | The serial port device is occupied. |

**示例：**

说明

以下示例代码只是调用open接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```
1. import { JSON } from '@kit.ArkTS';
2. import { serialManager } from '@kit.BasicServicesKit';

4. // 获取串口列表
5. function open() {
6. let portList: serialManager.SerialPort[] = serialManager.getPortList();
7. console.info('usbSerial portList: ' + JSON.stringify(portList));
8. if (!portList || portList.length === 0) {
9. console.error('usbSerial portList is empty');
10. return;
11. }
12. let portId: number = portList[0].portId;

14. // 检测设备是否可被应用访问
15. if (!serialManager.hasSerialRight(portId)) {
16. serialManager.requestSerialRight(portId).then(result => {
17. if (!result) {
18. // 没有访问设备的权限且用户不授权则退出
19. console.error('user is not granted the operation permission');
20. return;
21. } else {
22. console.info('grant permission successfully');
23. }
24. });
25. }

27. // 打开设备
28. try {
29. serialManager.open(portId)
30. console.info('open usbSerial success, portId: ' + portId);
31. } catch (error) {
32. console.error('open usbSerial error, ' + JSON.stringify(error));
33. }
34. }
```

## serialManager.getAttribute

PC/2in1

getAttribute(portId: number): Readonly<SerialAttribute>

获取指定串口的配置参数。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| portId | number | 是 | 端口号，来自[getPortList](js-apis-serialmanager.md#serialmanagergetportlist)获取的串口参数SerialPort。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Readonly<[SerialAttribute](js-apis-serialmanager.md#serialattribute)> | 返回串口的配置参数。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |
| 31400005 | The serial port device is not opened. Call the open API first. |

**示例：**

说明

以下示例代码只是调用getAttribute接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```
1. import { JSON } from '@kit.ArkTS';
2. import { serialManager } from '@kit.BasicServicesKit';

4. // 获取串口列表
5. function getAttribute() {
6. let portList: serialManager.SerialPort[] = serialManager.getPortList();
7. console.info('usbSerial portList: ' + JSON.stringify(portList));
8. if (!portList || portList.length === 0) {
9. console.error('usbSerial portList is empty');
10. return;
11. }
12. let portId: number = portList[0].portId;

14. // 检测设备是否可被应用访问
15. if (!serialManager.hasSerialRight(portId)) {
16. serialManager.requestSerialRight(portId).then(result => {
17. if (!result) {
18. // 没有访问设备的权限且用户不授权则退出
19. console.error('user is not granted the operation permission');
20. return;
21. } else {
22. console.info('grant permission successfully');
23. }
24. });
25. }

27. // 打开设备
28. try {
29. serialManager.open(portId)
30. console.info('open usbSerial success, portId: ' + portId);
31. } catch (error) {
32. console.error('open usbSerial error, ' + JSON.stringify(error));
33. return;
34. }

36. // 获取串口配置
37. try {
38. let attribute: serialManager.SerialAttribute = serialManager.getAttribute(portId);
39. if (attribute === undefined) {
40. console.error('getAttribute usbSerial error, attribute is undefined');
41. } else {
42. console.info('getAttribute usbSerial success, attribute: ' + JSON.stringify(attribute));
43. }
44. } catch (error) {
45. console.error('getAttribute usbSerial error, ' + JSON.stringify(error));
46. }
47. }
```

## serialManager.setAttribute

PC/2in1

setAttribute(portId: number, attribute: SerialAttribute): void

设置串口的配置参数。如果未调用该方法，使用默认配置参数（波特率：9600bps；数据位：8；校验位：0；停止位：1）。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| portId | number | 是 | 端口号，来自[getPortList](js-apis-serialmanager.md#serialmanagergetportlist)获取的串口参数SerialPort。 |
| attribute | [SerialAttribute](js-apis-serialmanager.md#serialattribute) | 是 | 串口参数。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |
| 31400005 | The serial port device is not opened. Call the open API first. |

**示例：**

说明

以下示例代码只是调用setAttribute接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```
1. import { JSON } from '@kit.ArkTS';
2. import { serialManager } from '@kit.BasicServicesKit';

4. // 获取串口列表
5. function setAttribute() {
6. let portList: serialManager.SerialPort[] = serialManager.getPortList();
7. console.info('usbSerial portList: ' + JSON.stringify(portList));
8. if (!portList || portList.length === 0) {
9. console.error('usbSerial portList is empty');
10. return;
11. }
12. let portId: number = portList[0].portId;

14. // 检测设备是否可被应用访问
15. if (!serialManager.hasSerialRight(portId)) {
16. serialManager.requestSerialRight(portId).then(result => {
17. if (!result) {
18. // 没有访问设备的权限且用户不授权则退出
19. console.error('user is not granted the operation permission');
20. return;
21. } else {
22. console.info('grant permission successfully');
23. }
24. });
25. }

27. // 打开设备
28. try {
29. serialManager.open(portId)
30. console.info('open usbSerial success, portId: ' + portId);
31. } catch (error) {
32. console.error('open usbSerial error, ' + JSON.stringify(error));
33. return;
34. }

36. // 设置串口配置
37. try {
38. let attribute: serialManager.SerialAttribute = {
39. baudRate: serialManager.BaudRates.BAUDRATE_9600,
40. dataBits: serialManager.DataBits.DATABIT_8,
41. parity: serialManager.Parity.PARITY_NONE,
42. stopBits: serialManager.StopBits.STOPBIT_1
43. }
44. serialManager.setAttribute(portId, attribute);
45. console.info('setAttribute usbSerial success, attribute: ' + JSON.stringify(attribute));
46. } catch (error) {
47. console.error('setAttribute usbSerial error, ' + JSON.stringify(error));
48. }
49. }
```

## serialManager.read

PC/2in1

read(portId: number, buffer: Uint8Array, timeout?: number): Promise<number>

从串口设备异步读取数据。使用Promise异步回调。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| portId | number | 是 | 端口号，来自[getPortList](js-apis-serialmanager.md#serialmanagergetportlist)获取的串口参数SerialPort。 |
| buffer | Uint8Array | 是 | 读取数据的缓冲区。 |
| timeout | number | 否 | 超时时间（单位：ms）。API在目标端口缓冲区无数据时，等待指定时间后返回。默认值0表示不等待直接返回。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回读取数据长度。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |
| 31400005 | The serial port device is not opened. Call the open API first. |
| 31400006 | Data transfer timed out. |
| 31400007 | I/O exception. Possible causes: 1. The transfer was canceled. 2. The device offered more data than allowed. |

**示例：**

说明

以下示例代码只是调用read接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```
1. import { JSON } from '@kit.ArkTS';
2. import { serialManager } from '@kit.BasicServicesKit';

4. // 获取串口列表
5. function read() {
6. let portList: serialManager.SerialPort[] = serialManager.getPortList();
7. console.info('usbSerial portList: ' + JSON.stringify(portList));
8. if (!portList || portList.length === 0) {
9. console.error('usbSerial portList is empty');
10. return;
11. }
12. let portId: number = portList[0].portId;

14. // 检测设备是否可被应用访问
15. if (!serialManager.hasSerialRight(portId)) {
16. serialManager.requestSerialRight(portId).then(result => {
17. if (!result) {
18. // 没有访问设备的权限且用户不授权则退出
19. console.error('user is not granted the operation permission');
20. return;
21. } else {
22. console.info('grant permission successfully');
23. }
24. });
25. }

27. // 打开设备
28. try {
29. serialManager.open(portId)
30. console.info('open usbSerial success, portId: ' + portId);
31. } catch (error) {
32. console.error('open usbSerial error, ' + JSON.stringify(error));
33. }

35. // 异步读取
36. let readBuffer: Uint8Array = new Uint8Array(64);
37. serialManager.read(portId, readBuffer, 2000).then((size: number) => {
38. console.info('read usbSerial success, readBuffer: ' + readBuffer.toString());
39. }).catch((error: Error) => {
40. console.error('read usbSerial error, ' + JSON.stringify(error));
41. })
42. }
```

## serialManager.readSync

PC/2in1

readSync(portId: number, buffer: Uint8Array, timeout?: number): number

从串口设备同步读取数据。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| portId | number | 是 | 端口号，来自[getPortList](js-apis-serialmanager.md#serialmanagergetportlist)获取的串口参数SerialPort。 |
| buffer | Uint8Array | 是 | 读取数据的缓冲区。 |
| timeout | number | 否 | 超时时间（单位：ms）。API在目标端口缓冲区无数据时，等待指定时间后返回。默认值0表示不等待直接返回。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回读取数据长度。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |
| 31400005 | The serial port device is not opened. Call the open API first. |
| 31400006 | Data transfer timed out. |
| 31400007 | I/O exception. Possible causes: 1. The transfer was canceled. 2. The device offered more data than allowed. |

**示例：**

说明

以下示例代码只是调用readSync接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```
1. import { JSON } from '@kit.ArkTS';
2. import { serialManager } from '@kit.BasicServicesKit';

4. // 获取串口列表
5. function readSync() {
6. let portList: serialManager.SerialPort[] = serialManager.getPortList();
7. console.info('usbSerial portList: ' + JSON.stringify(portList));
8. if (!portList || portList.length === 0) {
9. console.error('usbSerial portList is empty');
10. return;
11. }
12. let portId: number = portList[0].portId;

14. // 检测设备是否可被应用访问
15. if (!serialManager.hasSerialRight(portId)) {
16. serialManager.requestSerialRight(portId).then(result => {
17. if (!result) {
18. // 没有访问设备的权限且用户不授权则退出
19. console.error('user is not granted the operation permission');
20. return;
21. } else {
22. console.info('grant permission successfully');
23. }
24. });
25. }

27. // 打开设备
28. try {
29. serialManager.open(portId)
30. console.info('open usbSerial success, portId: ' + portId);
31. } catch (error) {
32. console.error('open usbSerial error, ' + JSON.stringify(error));
33. }

35. // 同步读取
36. let readSyncBuffer: Uint8Array = new Uint8Array(64);
37. try {
38. serialManager.readSync(portId, readSyncBuffer, 2000);
39. console.info('readSync usbSerial success, readSyncBuffer: ' + readSyncBuffer.toString());
40. } catch (error) {
41. console.error('readSync usbSerial error, ' + JSON.stringify(error));
42. }
43. }
```

## serialManager.write

PC/2in1

write(portId: number, buffer: Uint8Array, timeout?: number): Promise<number>

向串口设备异步写数据，每次写入数据长度不超过4KB，数据过大会导致数据丢失，长数据建议分包写入。使用Promise异步回调。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| portId | number | 是 | 端口号，来自[getPortList](js-apis-serialmanager.md#serialmanagergetportlist)获取的串口参数SerialPort。 |
| buffer | Uint8Array | 是 | 写入数据的缓冲区。 |
| timeout | number | 否 | 超时时间（单位：ms），指定时间内等待API在目标端口的缓冲区是否可写，若可写则正常处理，若不可写等待超过指定时间后返回超时。默认值0表示不可写时不等待直接返回。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回写入数据长度。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |
| 31400005 | The serial port device is not opened. Call the open API first. |
| 31400006 | Data transfer timed out. |
| 31400007 | I/O exception. Possible causes: 1. The transfer was canceled. 2. The device offered more data than allowed. |

**示例：**

说明

以下示例代码只是调用write接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```
1. import { JSON } from '@kit.ArkTS';
2. import { buffer } from '@kit.ArkTS';
3. import { serialManager } from '@kit.BasicServicesKit';

5. // 获取串口列表
6. function write() {
7. let portList: serialManager.SerialPort[] = serialManager.getPortList();
8. console.info('usbSerial portList: ' + JSON.stringify(portList));
9. if (!portList || portList.length === 0) {
10. console.error('usbSerial portList is empty');
11. return;
12. }
13. let portId: number = portList[0].portId;

15. // 检测设备是否可被应用访问
16. if (!serialManager.hasSerialRight(portId)) {
17. serialManager.requestSerialRight(portId).then(result => {
18. if (!result) {
19. // 没有访问设备的权限且用户不授权则退出
20. console.error('user is not granted the operation permission');
21. return;
22. } else {
23. console.info('grant permission successfully');
24. }
25. });
26. }

28. // 打开设备
29. try {
30. serialManager.open(portId)
31. console.info('open usbSerial success, portId: ' + portId);
32. } catch (error) {
33. console.error('open usbSerial error, ' + JSON.stringify(error));
34. }

36. // 异步写入
37. let writeBuffer: Uint8Array = new Uint8Array(buffer.from('Hello World', 'utf-8').buffer)
38. serialManager.write(portId, writeBuffer, 2000).then((size: number) => {
39. console.info('write usbSerial success, writeBuffer: ' + writeBuffer.toString());
40. }).catch((error: Error) => {
41. console.error('write usbSerial error, ' + JSON.stringify(error));
42. })
43. }
```

## serialManager.writeSync

PC/2in1

writeSync(portId: number, buffer: Uint8Array, timeout?: number): number

向串口设备同步写数据，每次写入数据长度不超过4KB，数据过大会导致数据丢失，长数据建议分包写入。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| portId | number | 是 | 端口号，来自[getPortList](js-apis-serialmanager.md#serialmanagergetportlist)获取的串口参数SerialPort。 |
| buffer | Uint8Array | 是 | 写入目标缓冲区。 |
| timeout | number | 否 | 超时时间（单位：ms），指定时间内等待API在目标端口的缓冲区是否可写，若可写则正常处理，若不可写等待超过指定时间后返回超时。默认值0表示不可写时不等待直接返回。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回写入数据长度。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |
| 31400005 | The serial port device is not opened. Call the open API first. |
| 31400006 | Data transfer timed out. |
| 31400007 | I/O exception. Possible causes: 1. The transfer was canceled. 2. The device offered more data than allowed. |

**示例：**

说明

以下示例代码只是调用writeSync接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```
1. import { JSON } from '@kit.ArkTS';
2. import { buffer } from '@kit.ArkTS';
3. import { serialManager } from '@kit.BasicServicesKit';

5. // 获取串口列表
6. function writeSync() {
7. let portList: serialManager.SerialPort[] = serialManager.getPortList();
8. console.info('usbSerial portList: ' + JSON.stringify(portList));
9. if (!portList || portList.length === 0) {
10. console.error('usbSerial portList is empty');
11. return;
12. }
13. let portId: number = portList[0].portId;

15. // 检测设备是否可被应用访问
16. if (!serialManager.hasSerialRight(portId)) {
17. serialManager.requestSerialRight(portId).then(result => {
18. if (!result) {
19. // 没有访问设备的权限且用户不授权则退出
20. console.error('user is not granted the operation permission');
21. return;
22. } else {
23. console.info('grant permission successfully');
24. }
25. });
26. }

28. // 打开设备
29. try {
30. serialManager.open(portId)
31. console.info('open usbSerial success, portId: ' + portId);
32. } catch (error) {
33. console.error('open usbSerial error, ' + JSON.stringify(error));
34. }

36. // 同步写入
37. let writeSyncBuffer: Uint8Array = new Uint8Array(buffer.from('Hello World', 'utf-8').buffer)
38. try {
39. serialManager.writeSync(portId, writeSyncBuffer, 2000);
40. console.info('writeSync usbSerial success, writeSyncBuffer: ' + writeSyncBuffer.toString());
41. } catch (error) {
42. console.error('writeSync usbSerial error, ' + JSON.stringify(error));
43. }
44. }
```

## serialManager.close

PC/2in1

close(portId: number): void

关闭串口。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| portId | number | 是 | 端口号，来自[getPortList](js-apis-serialmanager.md#serialmanagergetportlist)获取的串口参数SerialPort。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |
| 31400005 | The serial port device is not opened. Call the open API first. |

**示例：**

说明

以下示例代码只是调用close接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```
1. import { JSON } from '@kit.ArkTS';
2. import { serialManager } from '@kit.BasicServicesKit';

4. // 获取串口列表
5. function close() {
6. let portList: serialManager.SerialPort[] = serialManager.getPortList();
7. console.info('usbSerial portList: ' + JSON.stringify(portList));
8. if (!portList || portList.length === 0) {
9. console.error('usbSerial portList is empty');
10. return;
11. }
12. let portId: number = portList[0].portId;

14. // 检测设备是否可被应用访问
15. if (!serialManager.hasSerialRight(portId)) {
16. serialManager.requestSerialRight(portId).then(result => {
17. if (!result) {
18. // 没有访问设备的权限且用户不授权则退出
19. console.error('user is not granted the operation permission');
20. return;
21. } else {
22. console.info('grant permission successfully');
23. }
24. });
25. }

27. // 打开设备
28. try {
29. serialManager.open(portId)
30. console.info('open usbSerial success, portId: ' + portId);
31. } catch (error) {
32. console.error('open usbSerial error, ' + JSON.stringify(error));
33. return;
34. }

36. // 关闭串口
37. try {
38. serialManager.close(portId);
39. console.info('close usbSerial success, portId: ' + portId);
40. } catch (error) {
41. console.error('close usbSerial error, ' + JSON.stringify(error));
42. }
43. }
```

## serialManager.cancelSerialRight

PC/2in1

cancelSerialRight(portId: number): void

移除应用程序运行时访问串口设备的权限。此接口会调用close关闭已打开的串口。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| portId | number | 是 | 端口号，来自[getPortList](js-apis-serialmanager.md#serialmanagergetportlist)获取的串口参数SerialPort。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14400005 | Database operation exception. |
| 31400001 | Serial port management exception. |
| 31400002 | Access denied. Call requestSerialRight to request user authorization first. |
| 31400003 | PortId does not exist. |

**示例：**

说明

以下示例代码只是调用cancelSerialRight接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```
1. import { JSON } from '@kit.ArkTS';
2. import { serialManager } from '@kit.BasicServicesKit';

4. // 获取串口列表
5. function cancelSerialRight() {
6. let portList: serialManager.SerialPort[] = serialManager.getPortList();
7. console.info('usbSerial portList: ' + JSON.stringify(portList));
8. if (!portList || portList.length === 0) {
9. console.error('usbSerial portList is empty');
10. return;
11. }
12. let portId: number = portList[0].portId;

14. // 检测设备是否可被应用访问
15. if (!serialManager.hasSerialRight(portId)) {
16. serialManager.requestSerialRight(portId).then(result => {
17. if (!result) {
18. // 没有访问设备的权限且用户不授权则退出
19. console.error('user is not granted the operation permission');
20. return;
21. } else {
22. console.info('grant permission successfully');
23. }
24. });
25. }

27. // 取消已经授予的权限
28. try {
29. serialManager.cancelSerialRight(portId);
30. console.info('cancelSerialRight success, portId: ', portId);
31. } catch (error) {
32. console.error('cancelSerialRight error, ', JSON.stringify(error));
33. }
34. }
```

## SerialAttribute

PC/2in1

串口的配置参数。

**系统能力：** SystemCapability.USB.USBManager.Serial

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| baudRate | [BaudRates](js-apis-serialmanager.md#baudrates) | 否 | 否 | 串口波特率。 |
| dataBits | [DataBits](js-apis-serialmanager.md#databits) | 否 | 是 | 串口数据位，默认值为8位。 |
| parity | [Parity](js-apis-serialmanager.md#parity) | 否 | 是 | 串口奇偶校验，默认值为None，无奇偶校验。 |
| stopBits | [StopBits](js-apis-serialmanager.md#stopbits) | 否 | 是 | 串口停止位，默认值为1位。 |

## SerialPort

PC/2in1

串口参数。

**系统能力：** SystemCapability.USB.USBManager.Serial

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| portId | number | 否 | 否 | 端口号。 |
| deviceName | string | 否 | 否 | 串口设备名称。 |

## BaudRates

PC/2in1

表示波特率的枚举

**系统能力：** SystemCapability.USB.USBManager.Serial

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BAUDRATE\_50 | 50 | 传输波特率为50。 |
| BAUDRATE\_75 | 75 | 传输波特率为75。 |
| BAUDRATE\_110 | 110 | 传输波特率为110。 |
| BAUDRATE\_134 | 134 | 传输波特率为134。 |
| BAUDRATE\_150 | 150 | 传输波特率为150。 |
| BAUDRATE\_200 | 200 | 传输波特率为200。 |
| BAUDRATE\_300 | 300 | 传输波特率为300。 |
| BAUDRATE\_600 | 600 | 传输波特率为600。 |
| BAUDRATE\_1200 | 1200 | 传输波特率为1200。 |
| BAUDRATE\_1800 | 1800 | 传输波特率为1800。 |
| BAUDRATE\_2400 | 2400 | 传输波特率为2400。 |
| BAUDRATE\_4800 | 4800 | 传输波特率为4800。 |
| BAUDRATE\_9600 | 9600 | 传输波特率为9600。 |
| BAUDRATE\_19200 | 19200 | 传输波特率为19200。 |
| BAUDRATE\_38400 | 38400 | 传输波特率为38400。 |
| BAUDRATE\_57600 | 57600 | 传输波特率为57600。 |
| BAUDRATE\_115200 | 115200 | 传输波特率为115200。 |
| BAUDRATE\_230400 | 230400 | 传输波特率为230400。 |
| BAUDRATE\_460800 | 460800 | 传输波特率为460800。 |
| BAUDRATE\_500000 | 500000 | 传输波特率为500000。 |
| BAUDRATE\_576000 | 576000 | 传输波特率为576000。 |
| BAUDRATE\_921600 | 921600 | 传输波特率为921600。 |
| BAUDRATE\_1000000 | 1000000 | 传输波特率为1000000。 |
| BAUDRATE\_1152000 | 1152000 | 传输波特率为1152000。 |
| BAUDRATE\_1500000 | 1500000 | 传输波特率为1500000。 |
| BAUDRATE\_2000000 | 2000000 | 传输波特率为2000000。 |
| BAUDRATE\_2500000 | 2500000 | 传输波特率为2500000。 |
| BAUDRATE\_3000000 | 3000000 | 传输波特率为3000000。 |
| BAUDRATE\_3500000 | 3500000 | 传输波特率为3500000。 |
| BAUDRATE\_4000000 | 4000000 | 传输波特率为4000000。 |

## DataBits

PC/2in1

表示数据位宽的枚举

**系统能力：** SystemCapability.USB.USBManager.Serial

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DATABIT\_8 | 8 | 报文的有效数据位宽为8比特。 |
| DATABIT\_7 | 7 | 报文的有效数据位宽为7比特。 |
| DATABIT\_6 | 6 | 报文的有效数据位宽为6比特。 |
| DATABIT\_5 | 5 | 报文的有效数据位宽为5比特。 |

## Parity

PC/2in1

表示校验位的校验方式的枚举

**系统能力：** SystemCapability.USB.USBManager.Serial

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PARITY\_NONE | 0 | 无校验。 |
| PARITY\_ODD | 1 | 奇校验。 |
| PARITY\_EVEN | 2 | 偶校验。 |
| PARITY\_MARK | 3 | 固定为1。 |
| PARITY\_SPACE | 4 | 固定为0。 |

## StopBits

PC/2in1

表示停止位宽的枚举

**系统能力：** SystemCapability.USB.USBManager.Serial

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STOPBIT\_1 | 0 | 报文的有效停止位宽为1比特。 |
| STOPBIT\_2 | 1 | 报文的有效停止位宽为2比特。 |
