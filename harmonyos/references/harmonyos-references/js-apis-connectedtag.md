---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-connectedtag
title: @ohos.connectedTag (有源标签)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.connectedTag (有源标签)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:59+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:08dcc08aa36762fe7783276097aa78ebe59aca45fac3d9a355430d03a1f4eab1
---

本模块提供有源标签的使用，包括初始化有源标签芯片、读取有源标签内容、写入内容到有源标签等。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PC/2in1

```
1. import { connectedTag } from '@kit.ConnectivityKit';
```

## connectedTag.init(deprecated)

PC/2in1

init(): boolean

初始化有源标签芯片。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[initialize](js-apis-connectedtag.md#connectedtaginitialize9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true：初始化成功。  false：初始化失败。 |

## connectedTag.initialize9+

PC/2in1

initialize(): void

初始化有源标签芯片。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

## connectedTag.uninit(deprecated)

PC/2in1

uninit(): boolean

卸载有源标签芯片资源。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[uninitialize](js-apis-connectedtag.md#connectedtaguninitialize9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true：卸载操作成功。  false：卸载操作失败。 |

## connectedTag.uninitialize9+

PC/2in1

uninitialize(): void

卸载有源标签芯片资源。

**需要权限:** ohos.permission.NFC\_TAG

**系统能力:** SystemCapability.Communication.ConnectedTag

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

## connectedTag.readNdefTag(deprecated)

PC/2in1

readNdefTag(): Promise<string>

读取有源标签内容，使用promise方式作为异步方法。

说明

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[connectedTag.read](js-apis-connectedtag.md#connectedtagread9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<string> | 返回读取有源标签内容。 |

**示例：**

```
1. import { connectedTag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connectedTag.readNdefTag().then((data) => {
5. console.info("connectedTag readNdefTag Promise data = " + data);
6. }).catch((err: BusinessError)=> {
7. console.error("connectedTag readNdefTag Promise err: " + err);
8. });
```

## connectedTag.read9+

PC/2in1

read(): Promise<number[]>

读取有源标签内容，使用promise方式作为异步方法。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<number[]> | 返回读取有源标签内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

**示例：**

```
1. import { connectedTag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. connectedTag.read().then((data) => {
5. console.info("connectedTag read Promise data = " + data);
6. }).catch((err: BusinessError)=> {
7. console.error("connectedTag read Promise err: " + err);
8. });
```

## connectedTag.readNdefTag(deprecated)

PC/2in1

readNdefTag(callback: AsyncCallback<string>): void

读取有源标签内容，使用AsyncCallback方式作为异步方法。

说明

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[connectedTag.read](js-apis-connectedtag.md#connectedtagread9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 读取有源标签内容回调函数。 |

**示例：**

```
1. import { connectedTag } from '@kit.ConnectivityKit';

3. connectedTag.readNdefTag((err, data)=> {
4. if (err) {
5. console.error("connectedTag readNdefTag AsyncCallback err: " + err);
6. } else {
7. console.info("connectedTag readNdefTag AsyncCallback data: " + data);
8. }
9. });
```

## connectedTag.read9+

PC/2in1

read(callback: AsyncCallback<number[]>): void

读取有源标签内容，使用AsyncCallback方式作为异步方法。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| callback | AsyncCallback<number[]> | 是 | 读取有源标签内容回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

**示例：**

```
1. import { connectedTag } from '@kit.ConnectivityKit';

3. connectedTag.read((err, data)=> {
4. if (err) {
5. console.error("connectedTag read AsyncCallback err: " + err);
6. } else {
7. console.info("connectedTag read AsyncCallback data: " + data);
8. }
9. });
```

## connectedTag.writeNdefTag(deprecated)

PC/2in1

writeNdefTag(data: string): Promise<void>

写入内容到有源标签，使用promise方式作为异步方法。

说明

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[connectedTag.write](js-apis-connectedtag.md#connectedtagwrite9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| data | string | 是 | 有源标签内容, 最大长度为1024个字节。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回值。 |

**示例：**

```
1. import { connectedTag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let rawData = "010203"; // change it to be correct.
5. connectedTag.writeNdefTag(rawData).then(() => {
6. console.info("connectedTag.writeNdefTag Promise success.");
7. }).catch((err: BusinessError)=> {
8. console.error("connectedTag.writeNdefTag Promise err: " + err);
9. });
```

## connectedTag.write9+

PC/2in1

write(data: number[]): Promise<void>

写入内容到有源标签，使用promise方式作为异步方法。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| data | number[] | 是 | 有源标签内容, 由十六进制数字组成。范围：0x00至0xFF。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

**示例：**

```
1. import { connectedTag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let rawData = [0x01, 0x02, 0x03]; // change it to be correct.
5. connectedTag.write(rawData).then(() => {
6. console.info("connectedTag.write Promise success.");
7. }).catch((err: BusinessError)=> {
8. console.error("connectedTag.write Promise err: " + err);
9. });
```

## connectedTag.writeNdefTag(deprecated)

PC/2in1

writeNdefTag(data: string, callback: AsyncCallback<void>): void

写入内容到有源标签，使用AsyncCallback方式作为异步方法。

说明

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[connectedTag.write](js-apis-connectedtag.md#connectedtagwrite9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| data | string | 是 | 有源标签内容, 最大长度为1024个字节。 |
| callback | AsyncCallback<void> | 是 | 读取有源标签内容回调函数。 |

**示例：**

```
1. import { connectedTag } from '@kit.ConnectivityKit';

3. let rawData = "010203"; // change it to be correct.
4. connectedTag.writeNdefTag(rawData, (err)=> {
5. if (err) {
6. console.error("connectedTag.writeNdefTag AsyncCallback err: " + err);
7. } else {
8. console.info("connectedTag.writeNdefTag AsyncCallback success.");
9. }
10. });
```

## connectedTag.write9+

PC/2in1

write(data: number[], callback: AsyncCallback<void>): void

写入内容到有源标签，使用AsyncCallback方式作为异步方法。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| data | number[] | 是 | 有源标签内容, 由十六进制数字组成。范围：0x00至0xFF。 |
| callback | AsyncCallback<void> | 是 | 读取有源标签内容回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

**示例：**

```
1. import { connectedTag } from '@kit.ConnectivityKit';

3. let rawData = [0x01, 0x02, 0x03]; // change it to be correct.
4. connectedTag.write(rawData, (err)=> {
5. if (err) {
6. console.error("connectedTag.write AsyncCallback err: " + err);
7. } else {
8. console.info("connectedTag.write AsyncCallback success.");
9. }
10. });
```

## connectedTag.on('notify')

PC/2in1

on(type: "notify", callback: Callback<number>): void

注册NFC场强状态事件。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"notify"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数，返回值参见[NfcRfType](js-apis-connectedtag.md#nfcrftype)。 |

## connectedTag.off('notify')

PC/2in1

off(type: "notify", callback?: Callback<number>): void

取消NFC场强状态事件的注册。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"notify"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将“去注册”该事件关联的所有回调函数。 |

**示例：**

```
1. import { connectedTag } from '@kit.ConnectivityKit';

3. function nfcStatusCb(rfState: connectedTag.NfcRfType) {
4. console.info("connectedTag on Callback rfState: ", rfState);
5. }

7. // 有源nfc标签的使用流程
8. async function nfcTagTestOn(): Promise<void> {
9. try {
10. console.info("connectedTag initialize");
11. connectedTag.initialize();
12. } catch (error) {
13. console.error("initialize error:" + error);
14. }
15. // 注册回调以接收nfc进离场状态更改通知
16. connectedTag.on("notify", nfcStatusCb);
17. try {
18. let tag = [3, 1, 0];
19. console.info("connectedTag write: tag=" + tag);
20. await connectedTag.write(tag);
21. let data = await connectedTag.read();
22. console.info("connectedTag read: data=" + data);
23. } catch (error) {
24. console.error("connectedTag error: " + error);
25. }
26. }

28. // 业务退出时，取消注册回调、取消初始化
29. async function nfcTagTestOff(): Promise<void> {
30. // 取消注册回调
31. connectedTag.off("notify", nfcStatusCb);
32. try {
33. console.info("connectedTag uninitialize");
34. connectedTag.uninitialize();
35. } catch (error) {
36. console.error("connectedTag error: " + error);
37. }
38. }

40. export { nfcTagTestOn, nfcTagTestOff }
```

## NfcRfType

PC/2in1

表示NFC场强状态的枚举。

**系统能力**：SystemCapability.Communication.ConnectedTag

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NFC\_RF\_LEAVE | 0 | NFC离场事件。 |
| NFC\_RF\_ENTER | 1 | NFC进场事件。 |
