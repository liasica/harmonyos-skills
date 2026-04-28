---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-tagsession
title: tagSession (标准NFC-Tag TagSession)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > tag > tagSession (标准NFC-Tag TagSession)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d69b4bee0d04a6afedb6dcc85f0a72b672b4cfabee87c81adf6f0fa665ae54f5
---

本模块是对NFC TagSession的使用说明。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

注意

导入tag模块编辑器报错，在某个具体设备型号上能力可能超出工程默认设备定义的能力集范围，如需要使用此部分能力需额外配置自定义syscap，参考[syscap开发指南](syscap.md#syscap开发指导)。

## **导入模块**

PhoneWearable

```
1. import { tag } from '@kit.ConnectivityKit';
```

## TagSession

PhoneWearable

TagSession是所有[nfcTag技术类型](js-apis-nfctech.md)的基类， 提供建立连接和发送数据等共同接口。

需要通过其子类来访问以下接口。在下面的示例中 统一用 getXXX()表示获取子类实例的方法。

具体使用时,请根据实际采用的nfcTag技术，选择对应的方法，具体请参见[nfcTag](js-apis-nfctag.md)文档。

### getTagInfo(deprecated)

PhoneWearable

getTagInfo(): tag.TagInfo

获取该Tag被分发时，NFC服务所提供的Tag数据对象。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tag.getTagInfo](js-apis-nfctag.md#taggettaginfo9)替代。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| **类型** | **说明** |
| --- | --- |
| tag.TagInfo | NFC服务所提供的Tag数据对象。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
4. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

6. let tagInfo : TagInfo = tag.getIsoDep(tagInfo).getTagInfo();
7. console.info("tag tagInfo: " + tagInfo);
```

### connectTag(deprecated)

PhoneWearable

connectTag(): boolean;

和标签建立连接。在从标签读取数据或将数据写入标签之前，必须调用此方法。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tagSession.connect](js-apis-tagsession.md#connect9)替代。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | 连接建立成功返回true，失败返回false。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
4. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

6. let connectStatus : boolean = tag.getIsoDep(tagInfo).connectTag();
7. console.info("connectStatus: " + connectStatus);
```

### connect9+

PhoneWearable

connect(): void;

和标签建立连接。在从标签读取数据或将数据写入标签之前，必须调用此方法。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
4. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

6. try {
7. tag.getIsoDep(tagInfo).connect();
8. console.info("tag connect success");
9. } catch (businessError) {
10. console.error("tag connect businessError: " + businessError);
11. }
```

### reset()(deprecated)

PhoneWearable

reset(): void

重置与标签的连接。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tagSession.resetConnection](js-apis-tagsession.md#resetconnection9)替代。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
4. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

6. tag.getIsoDep(tagInfo).reset();
```

### resetConnection()9+

PhoneWearable

resetConnection(): void

重置与标签的连接。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
4. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

6. try {
7. tag.getIsoDep(tagInfo).resetConnection();
8. console.info("tag resetConnection success");
9. } catch (businessError) {
10. console.error("tag resetConnection businessError: " + businessError);
11. }
```

### isTagConnected(deprecated)

PhoneWearable

isTagConnected(): boolean

检查是否已与标签建立连接。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tagSession.isConnected](js-apis-tagsession.md#isconnected9)替代。

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | 已建立连接返回 true，未建立连接返回false。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
4. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

6. let isTagConnected = tag.getIsoDep(tagInfo).isTagConnected();
7. console.info("isTagConnected: " + isTagConnected);
```

### isConnected9+

PhoneWearable

isConnected(): boolean

检查是否已与标签建立连接。如果返回未连接，则需要先调用[tagSession.connect](js-apis-tagsession.md#connect9)建立连接。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | 已建立连接返回 true，未建立连接返回false。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
4. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

6. try {
7. let isConnected = tag.getIsoDep(tagInfo).isConnected();
8. console.info("tag isConnected = " + isConnected);
9. } catch (businessError) {
10. console.error("tag isConnected businessError: " + businessError);
11. }
```

### getMaxSendLength(deprecated)

PhoneWearable

getMaxSendLength(): number

查询可以发送到标签的最大数据长度。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tagSession.getMaxTransmitSize](js-apis-tagsession.md#getmaxtransmitsize9)替代。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | 可以发送到标签的最大数据长度，非负数。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
4. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

6. let maxSendLen = tag.getIsoDep(tagInfo).getMaxSendLength();
7. console.info("tag maxSendLen: " + maxSendLen);
```

### getMaxTransmitSize9+

PhoneWearable

getMaxTransmitSize(): number

查询可以发送到标签的最大数据长度。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | 可以发送到标签的最大数据长度，非负数。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
4. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

6. try {
7. let maxTransmitSize = tag.getIsoDep(tagInfo).getMaxTransmitSize();
8. console.info("tag maxTransmitSize = " + maxTransmitSize);
9. } catch (businessError) {
10. console.error("tag getMaxTransmitSize businessError: " + businessError);
11. }
```

### getSendDataTimeout(deprecated)

PhoneWearable

getSendDataTimeout(): number

查询发送数据到Tag的等待超时时间，单位是毫秒。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tagSession.getTimeout](js-apis-tagsession.md#gettimeout9)替代。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | 发送数据到Tag的等待超时时间，单位是毫秒，非负数。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
4. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

6. let sendDataTimeout = tag.getIsoDep(tagInfo).getSendDataTimeout();
7. console.info("tag sendDataTimeout: " + sendDataTimeout);
```

### getTimeout9+

PhoneWearable

getTimeout(): number

查询发送数据到Tag的等待超时时间，单位是毫秒。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | 发送数据到Tag的等待超时时间，单位是毫秒，非负数。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
4. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

6. try {
7. let timeout = tag.getIsoDep(tagInfo).getTimeout();
8. console.info("tag timeout = " + timeout);
9. } catch (businessError) {
10. console.error("tag getTimeout businessError: " + businessError);
11. }
```

### setSendDataTimeout(deprecated)

PhoneWearable

setSendDataTimeout(timeout: number): boolean

设置发送数据到Tag的等待超时时间，单位是毫秒。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tagSession.setTimeout](js-apis-tagsession.md#settimeout9)替代。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 是 | 超时时间，单位毫秒，非负值。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | 设置超时时间成功返回true，设置失败返回false。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
4. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

6. let timeoutMs = 700;  // 修改为预期的超时时间
7. let setStatus = tag.getIsoDep(tagInfo).setSendDataTimeout(timeoutMs);
8. console.info("tag setSendDataTimeout setStatus: " + setStatus);
```

### setTimeout9+

PhoneWearable

setTimeout(timeout: number): void

设置发送数据到Tag的等待超时时间，单位是毫秒。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 是 | 超时时间，单位毫秒，非负值。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
4. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

6. let timeoutMs = 700;  // 修改为预期的超时时间
7. try {
8. tag.getIsoDep(tagInfo).setTimeout(timeoutMs);
9. console.info("tag setTimeout success");
10. } catch (businessError) {
11. console.error("tag setTimeout businessError: " + businessError);
12. }
```

### sendData(deprecated)

PhoneWearable

sendData(data: number[]): Promise<number[]>

发送指令到Tag上。使用Promise异步回调。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tagSession.transmit](js-apis-tagsession.md#transmit9)替代。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | number[] | 是 | 要发送的指令。每个number十六进制表示，范围是0x00~0xFF。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<number[]> | Promise对象，返回对端Tag对指令的响应数据，每个number十六进制表示，范围是0x00~0xFF。 |

**示例：**

```
1. import tag from '@kit.ConnectivityKit';
2. import { BusinessError } from '@ohos.base';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
5. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

7. function tagSessionDemo() {
8. // 如果没有连接，请先连接tag
9. if (!tag.getIsoDep(tagInfo).isTagConnected()) {
10. if (!tag.getIsoDep(tagInfo).connectTag()) {
11. console.error("tagSession connectTag failed.");
12. return;
13. }
14. }

16. let cmdData = [0x01, 0x02, 0x03, 0x04]; // 更改为正确的 data
17. tag.getIsoDep(tagInfo).sendData(cmdData).then((response) => {
18. console.info("tagSession sendData Promise response: " + response);
19. }).catch((err : BusinessError)=> {
20. console.error("tagSession sendData Promise err: " + err);
21. });
22. }
```

### sendData(deprecated)

PhoneWearable

sendData(data: number[], callback: AsyncCallback<number[]>): void

发送指令到Tag上。使用callback异步回调。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tagSession.transmit](js-apis-tagsession.md#transmit9-1)替代。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | number[] | 是 | 要发送的指令。每个number十六进制表示，范围是0x00~0xFF。 |
| callback | AsyncCallback<number[]> | 是 | 回调函数，返回响应数据。每个number十六进制表示，范围是0x00~0xFF。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
4. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

6. function tagSessionDemo() {
7. // 如果没有连接，请先连接tag
8. if (!tag.getIsoDep(tagInfo).isTagConnected()) {
9. if (!tag.getIsoDep(tagInfo).connectTag()) {
10. console.error("tagSession connectTag failed.");
11. return;
12. }
13. }

15. let cmdData = [0x01, 0x02, 0x03, 0x04]; // 更改为正确的 data
16. tag.getIsoDep(tagInfo).sendData(cmdData, (err, response)=> {
17. if (err) {
18. console.error("tagSession sendData AsyncCallback err: " + err);
19. } else {
20. console.info("tagSession sendData AsyncCallback response: " + response);
21. }
22. });
23. }
```

### transmit9+

PhoneWearable

transmit(data: number[]): Promise<number[]>

发送指令到Tag上。使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | number[] | 是 | 要发送的指令。每个number十六进制表示，范围是0x00~0xFF。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<number[]> | Promise对象，返回对端Tag对指令的响应数据，每个number十六进制表示，范围是0x00~0xFF。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
5. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

7. function tagSessionDemo() {
8. // 如果没有连接，请先连接tag
9. try {
10. if (!tag.getIsoDep(tagInfo).isConnected()) {
11. tag.getIsoDep(tagInfo).connect();
12. }
13. } catch (businessError) {
14. console.error("tag connect businessError: " + businessError);
15. return;
16. }

18. let cmdData = [0x01, 0x02, 0x03, 0x04]; // 更改为正确的 data
19. try {
20. tag.getIsoDep(tagInfo).transmit(cmdData).then((response) => {
21. console.info("tagSession transmit Promise response: " + response);
22. }).catch((err : BusinessError)=> {
23. console.error("tagSession transmit Promise err: " + err);
24. });
25. } catch (businessError) {
26. console.error("tag transmit businessError: " + businessError);
27. return;
28. }
29. }
```

### transmit9+

PhoneWearable

transmit(data: number[], callback: AsyncCallback<number[]>): void

发送指令到Tag上。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | number[] | 是 | 要发送的指令。每个number十六进制表示，范围是0x00~0xFF。 |
| callback | AsyncCallback<number[]> | 是 | 回调函数，返回响应数据。每个number十六进制表示，范围是0x00~0xFF。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed.. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，tagInfo是nfc服务在分派标签时给出的对象
4. // getXXX，可以是getIsoDep、getNdef、getMifareClassic...

6. function tagSessionDemo() {
7. // 如果没有连接，请先连接tag
8. try {
9. if (!tag.getIsoDep(tagInfo).isConnected()) {
10. tag.getIsoDep(tagInfo).connect();
11. }
12. } catch (businessError) {
13. console.error("tag connect businessError: " + businessError);
14. return;
15. }

17. let cmdData = [0x01, 0x02, 0x03, 0x04]; // 更改为正确的 data
18. try {
19. tag.getIsoDep(tagInfo).transmit(cmdData, (err, response)=> {
20. if (err) {
21. console.error("tagSession transmit AsyncCallback err: " + err);
22. } else {
23. console.info("tagSession transmit AsyncCallback response: " + response);
24. }
25. });
26. } catch (businessError) {
27. console.error("tag transmit businessError: " + businessError);
28. return;
29. }
30. }
```
