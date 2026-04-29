---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nfctech
title: nfctech (标准NFC-Tag Nfc 技术)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > tag > nfctech (标准NFC-Tag Nfc 技术)
category: harmonyos-references
scraped_at: 2026-04-29T13:58:35+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:edc386add6620649d187d72b08fabe20e38973de4303f3997c7a79654946b7e8
---

本模块主要用于采用不同Nfc技术的Tag的读写操作。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

注意

导入tag模块编辑器报错，在某个具体设备型号上能力可能超出工程默认设备定义的能力集范围，如需要使用此部分能力需额外配置自定义syscap，参考[syscap开发指南](syscap.md)。

## 导入模块

PhoneWearable

```
1. import { tag } from '@kit.ConnectivityKit';
```

## NfcATag

PhoneWearable

NfcATag 提供 NFC-A(ISO 14443-3A)技术的属性和I/O操作的访问，继承自[TagSession](js-apis-tagsession.md)。

TagSession是所有NFC Tag技术类型的基类， 提供建立连接和发送数据等共同接口。具体请参见[TagSession](js-apis-tagsession.md)。

NfcATag获取方式请参考[nfc-tag开发指南](../harmonyos-guides/nfc-tag-access-guide.md)。

以下是NfcATag的独有接口。

### NfcATag.getSak

PhoneWearable

getSak(): number

获取NFC-A标签的SAK值。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | NfcA 标签的SAK值，十六进制表示，范围是0x00~0xFF。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 nfcA
4. let sak : number = nfcA.getSak();
5. console.info("nfcA sak: " + sak);
```

### NfcATag.getAtqa

PhoneWearable

getAtqa(): number[]

获取NFC-A标签的Atqa值。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number[] | NfcA 标签的Atqa值，每个number十六进制表示，范围是0x00~0xFF。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 nfcA
4. let atqa : number[] = nfcA.getAtqa();
5. console.info("nfcA atqa: " + atqa);
```

## NfcBTag

PhoneWearable

NfcBTag 提供对NFC-B(ISO 14443-3B)技术的属性和I/O操作的访问，继承自TagSession。

TagSession是所有NFC Tag技术类型的基类，提供建立连接和发送数据等共同接口。具体请参见[TagSession](js-apis-tagsession.md)。

NfcBTag获取方式请参考[nfc-tag开发指南](../harmonyos-guides/nfc-tag-access-guide.md)。

以下是NfcBTag的独有接口。

### NfcBTag.getRespAppData

PhoneWearable

getRespAppData(): number[]

获取标签的应用程序数据。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number[] | NfcB 标签的应用程序数据，每个number十六进制表示，范围是0x00~0xFF。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 nfcB
4. let respAppData : number[] = nfcB.getRespAppData();
5. console.info("nfcB respAppData: " + respAppData);
```

### NfcBTag.getRespProtocol

PhoneWearable

getRespProtocol(): number[]

获取标签的协议信息。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number[] | NfcB 标签的协议信息，每个number十六进制表示，范围是0x00~0xFF。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 nfcB
4. let respProtocol : number[] = nfcB.getRespProtocol();
5. console.info("nfcB respProtocol: " + respProtocol);
```

## NfcFTag

PhoneWearable

NfcFTag 提供对NFC-F(JIS 6319-4)技术的属性和I/O操作的访问，继承自TagSession。

TagSession是所有NFC Tag技术类型的基类， 提供建立连接和发送数据等共同接口。具体请参见[TagSession](js-apis-tagsession.md)。

NfcFTag获取方式请参考[nfc-tag开发指南](../harmonyos-guides/nfc-tag-access-guide.md)。

以下是NfcFTag的独有接口。

### NfcFTag.getSystemCode

PhoneWearable

getSystemCode(): number[]

从标签实例获取系统代码。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number[] | NfcF 标签的系统代码，每个number十六进制表示，范围是0x00~0xFF。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 nfcF
4. let systemCode : number[] = nfcF.getSystemCode();
5. console.info("nfcF systemCode: " + systemCode);
```

### NfcFTag.getPmm

PhoneWearable

getPmm(): number[]

从标签实例获取PMm（由IC代码和制造商参数组成）。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number[] | NfcF 标签的PMm信息，每个number十六进制表示，范围是0x00~0xFF。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 nfcF
4. let pmm : number[] = nfcF.getPmm();
5. console.info("nfcF pmm: " + pmm);
```

## NfcVTag

PhoneWearable

NfcVTag 提供对NFC-V(ISO 15693)技术的属性和I/O操作的访问，继承自TagSession。

TagSession是所有NFC Tag技术类型的基类， 提供建立连接和发送数据等共同接口。具体请参见[TagSession](js-apis-tagsession.md)。

NfcVTag获取方式请参考[nfc-tag开发指南](../harmonyos-guides/nfc-tag-access-guide.md)。

以下是NfcVTag的独有接口。

### NfcVTag.getResponseFlags

PhoneWearable

getResponseFlags(): number

从标签实例获取响应标志。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | NfcV 标签的响应标志，十六进制表示，范围是0x00~0xFF。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 nfcV
4. let responseFlags : number = nfcV.getResponseFlags();
5. console.info("nfcV responseFlags: " + responseFlags);
```

### NfcVTag.getDsfId

PhoneWearable

getDsfId(): number

从标签实例获取数据存储格式标识符（DSFID）。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | NfcV 标签的数据存储格式标识符，十六进制表示，范围是0x00~0xFF。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 nfcV
4. let dsfId : number = nfcV.getDsfId();
5. console.info("nfcV dsfId: " + dsfId);
```

## IsoDepTag9+

PhoneWearable

IsoDepTag 提供对ISO-DEP(ISO 14443-4)技术的属性和I/O操作的访问，继承自TagSession。

TagSession是所有NFC Tag技术类型的基类， 提供建立连接和发送数据等共同接口。具体请参见[TagSession](js-apis-tagsession.md)。

IsoDepTag获取方式请参考[nfc-tag开发指南](../harmonyos-guides/nfc-tag-access-guide.md)。

以下是IsoDepTag的独有接口。

### IsoDepTag.getHistoricalBytes9+

PhoneWearable

getHistoricalBytes(): number[]

获取标签的历史字节，针对基于NfcA通信技术的IsoDep卡片。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number[] | IsoDepTag 标签的历史字节，每个number十六进制表示，范围是0x00~0xFF。如果该IsoDep类型Tag是基于NfcB技术的，则该返回值为空。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 isoDep
4. let historicalBytes : number[] = isoDep.getHistoricalBytes();
5. console.info("isoDep historicalBytes: " + historicalBytes);
```

### IsoDepTag.getHiLayerResponse9+

PhoneWearable

getHiLayerResponse(): number[]

获取标签的更高层响应字节，针对基于NfcB通信技术的IsoDep卡片。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number[] | IsoDepTag 标签的更高层响应字节，每个number十六进制表示，范围是0x00~0xFF。如果该IsoDep类型Tag是基于NfcA技术的，则该返回值为空。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 isoDep
4. let hiLayerResponse : number[] = isoDep.getHiLayerResponse();
5. console.info("isoDep hiLayerResponse: " + hiLayerResponse);
```

### IsoDepTag.isExtendedApduSupported9+

PhoneWearable

isExtendedApduSupported(): Promise<boolean>

检查是否支持扩展的APDU，使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示支持；返回false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 isoDep
5. function nfcTechDemo() {
6. // 如果没有连接Tag，请先连接
7. if (!isoDep.isTagConnected()) {
8. if (!isoDep.connectTag()) {
9. console.error("isoDep connectTag failed.");
10. return;
11. }
12. }

14. try {
15. isoDep.isExtendedApduSupported().then((response: boolean) => {
16. console.info("isoDep isExtendedApduSupported Promise response: " + response);
17. }).catch((err: BusinessError) => {
18. console.error(`isoDep isExtendedApduSupported Promise Code: ${err.code}, message: ${err.message}`);
19. });
20. } catch (businessError) {
21. console.error(`isoDep isExtendedApduSupported Promise Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
22. }
23. }
```

### IsoDepTag.isExtendedApduSupported9+

PhoneWearable

isExtendedApduSupported(callback: AsyncCallback<boolean>): void

检查是否支持扩展的APDU。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数，true: 支持， false: 不支持。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The Tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 isoDep
5. function nfcTechDemo() {
6. // 如果没有连接Tag，请先连接
7. if (!isoDep.isTagConnected()) {
8. if (!isoDep.connectTag()) {
9. console.error("isoDep connectTag failed.");
10. return;
11. }
12. }

14. try {
15. isoDep.isExtendedApduSupported((err: BusinessError, response: boolean) => {
16. if (err) {
17. console.error(`isoDep isExtendedApduSupported AsyncCallback Code: ${err.code}, message: ${err. message}`);
18. } else {
19. console.info("isoDep isExtendedApduSupported AsyncCallback response: " + response);
20. }
21. });
22. } catch (businessError) {
23. console.error(`isoDep isExtendedApduSupported AsyncCallback Code: ${(businessError as Business).code}, message: ${(businessError as Business).message}`);
24. }
25. }
```

## NdefMessage9+

PhoneWearable

### NdefMessage.getNdefRecords9+

PhoneWearable

getNdefRecords(): [tag.NdefRecord](js-apis-nfctag.md#ndefrecord9)[]

获取NDEF消息中的所有记录。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [tag.NdefRecord](js-apis-nfctag.md#ndefrecord9)[] | NDEF标签的Record列表，详见NDEF技术规范《NFCForum-TS-NDEF\_1.0》。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 从 tag.ndef.createNdefMessage 或 ndefTag.getNdefMessage 获取 ndefMessage。
4. // let ndefMessage : tag.NdefMessage = tag.ndef.createNdefMessage(...);
5. // let ndefMessage : tag.NdefMessage = ndefTag.getNdefMessage();

7. let ndefRecords : tag.NdefRecord[] = ndefMessage.getNdefRecords();
8. console.info("ndef ndefRecords number: " + ndefRecords.length);
```

## NdefTag9+

PhoneWearable

提供对已格式化为NDEF的NFC标签的数据和操作的访问，继承自TagSession。

TagSession是所有NFC Tag技术类型的基类，提供建立连接和发送数据等共同接口。具体请参见[TagSession](js-apis-tagsession.md)。

NdefTag获取方式请参考[nfc-tag开发指南](../harmonyos-guides/nfc-tag-access-guide.md)。

以下是NdefTag的独有接口。

### NdefTag.getNdefTagType9+

PhoneWearable

getNdefTagType(): [tag.NfcForumType](js-apis-nfctag.md#nfcforumtype9)

获取NDEF标签的类型。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [tag.NfcForumType](js-apis-nfctag.md#nfcforumtype9) | NDEF标签类型，包括NFC FORUM TYPE 1/2/3/4等。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 ndefTag
4. let ndefTagType : tag.NfcForumType = ndefTag.getNdefTagType();
5. console.info("ndef ndefTagType: " + ndefTagType);
```

### NdefTag.getNdefMessage9+

PhoneWearable

getNdefMessage(): [NdefMessage](js-apis-nfctech.md#ndefmessage9)

获取发现NDEF标签时，从标签读取的Message。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NdefMessage](js-apis-nfctech.md#ndefmessage9) | NDEF标签的Message，详见NDEF技术规范《NFCForum-TS-NDEF\_1.0》。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 ndefTag
4. let ndefMessage : tag.NdefMessage = ndefTag.getNdefMessage();
5. console.info("ndef ndefMessage: " + ndefMessage);
```

### NdefTag.isNdefWritable9+

PhoneWearable

isNdefWritable(): boolean

检查NDEF标签是否可写。在调用写数据接口前，需要先判断是否支持写操作。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | 检查结果，true: 可写， false: 不可写。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 ndefTag
4. let isWritable : boolean = ndefTag.isNdefWritable();
5. console.info("ndef isNdefWritable: " + isWritable);
```

### NdefTag.readNdef9+

PhoneWearable

readNdef(): Promise<[NdefMessage](js-apis-nfctech.md#ndefmessage9)>

读取标签上的NDEF消息。使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[NdefMessage](js-apis-nfctech.md#ndefmessage9)> | Promise对象。返回从NDEF标签中读取到的Message数据对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 ndefTag
5. function nfcTechDemo(){
6. // 如果没有连接Tag，请先连接
7. if (!ndefTag.isTagConnected()) {
8. if (!ndefTag.connectTag()) {
9. console.error("ndefTag connectTag failed.");
10. return;
11. }
12. }

14. try {
15. ndefTag.readNdef().then((ndefmessage : tag.NdefMessage) => {
16. console.info("ndef readNdef Promise ndefmessage: " + ndefmessage);
17. }).catch((err : BusinessError)=> {
18. console.error("ndef readNdef Promise err Code: ${err.code}, message: ${err.message}");
19. });
20. } catch (businessError) {
21. console.error(`ndef readNdef Promise catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
22. }
23. }
```

### NdefTag.readNdef9+

PhoneWearable

readNdef(callback: AsyncCallback<[NdefMessage](js-apis-nfctech.md#ndefmessage9)>): void

读取标签上的NDEF消息。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[NdefMessage](js-apis-nfctech.md#ndefmessage9)> | 是 | 回调函数，返回从NDEF标签中读取到的Message信息。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The Tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 ndefTag
5. function nfcTechDemo() {
6. // 如果没有连接Tag，请先连接
7. if (!ndefTag.isTagConnected()) {
8. if (!ndefTag.connectTag()) {
9. console.error("ndefTag connectTag failed.");
10. return;
11. }
12. }

14. try {
15. ndefTag.readNdef((err : BusinessError, ndefmessage : tag.NdefMessage)=> {
16. if (err) {
17. console.error(`ndef readNdef AsyncCallback err Code: ${err.code}, message: ${err.message}`);
18. } else {
19. console.info("ndef readNdef AsyncCallback ndefmessage: " + ndefmessage);
20. }
21. });
22. } catch (businessError) {
23. console.error(`ndef readNdef AsyncCallback catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
24. }
25. }
```

### NdefTag.writeNdef9+

PhoneWearable

writeNdef(msg: [NdefMessage](js-apis-nfctech.md#ndefmessage9)): Promise<void>

将NDEF Message数据对象写入标签。使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msg | [NdefMessage](js-apis-nfctech.md#ndefmessage9) | 是 | NDEF Message数据对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 ndefTag
5. // 从原始数据创建的ndefMessage，例如：
6. let ndefMessage : tag.NdefMessage =
7. tag.ndef.createNdefMessage([0xD1, 0x01, 0x03, 0x54, 0x4E, 0x46, 0x43]);  // 必须是可以被解析的NDEF记录。
8. // 或从 tag.ndef.createNdefMessage(ndefRecords:NdefRecord[]) 创建 ndefMessage

10. function nfcTechDemo() {
11. // 如果没有连接Tag，请先连接
12. if (!ndefTag.isTagConnected()) {
13. if (!ndefTag.connectTag()) {
14. console.error("ndefTag connectTag failed.");
15. return;
16. }
17. }

19. try {
20. ndefTag.writeNdef(ndefMessage).then(() => {
21. console.info("ndef writeNdef Promise success.");
22. }).catch((err : BusinessError)=> {
23. console.error(`ndef writeNdef err Code: ${err.code}, message: ${err.message}`);
24. });
25. } catch (businessError) {
26. console.error(`ndef writeNdef Promise catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
27. }
28. }
```

### NdefTag.writeNdef9+

PhoneWearable

writeNdef(msg: [NdefMessage](js-apis-nfctech.md#ndefmessage9), callback: AsyncCallback<void>): void

将NDEF Message数据对象写入此标签。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msg | [NdefMessage](js-apis-nfctech.md#ndefmessage9) | 是 | NDEF Message数据对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当NDEF Message数据对象写入成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The Tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 ndefTag
5. // 从原始数据创建的ndefMessage，例如：
6. let ndefMessage : tag.NdefMessage =
7. tag.ndef.createNdefMessage([0xD1, 0x01, 0x03, 0x54, 0x4E, 0x46, 0x43]);  // 必须是可以被解析的NDEF记录。
8. // 或从 tag.ndef.createNdefMessage(ndefRecords:NdefRecord[]) 创建 ndefMessage

10. function nfcTechDemo() {
11. // 如果没有连接Tag，请先连接
12. if (!ndefTag.isTagConnected()) {
13. if (!ndefTag.connectTag()) {
14. console.error("ndefTag connectTag failed.");
15. return;
16. }
17. }

19. try {
20. ndefTag.writeNdef(ndefMessage, (err : BusinessError)=> {
21. if (err) {
22. console.error("ndef writeNdef AsyncCallback Code: ${err.code}, message: ${err.message}");
23. } else {
24. console.info("ndef writeNdef AsyncCallback success.");
25. }
26. });
27. } catch (businessError) {
28. console.error(`ndef writeNdef AsyncCallback catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
29. }
30. }
```

### NdefTag.canSetReadOnly9+

PhoneWearable

canSetReadOnly(): boolean

检查NDEF标签是否可以设置为只读。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true: NDEF标签可设置为只读， false: NDEF标签不可设置为只读。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 3100201 | The tag running state is abnormal in the service. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 ndefTag
4. let canSetReadOnly : boolean = ndefTag.canSetReadOnly();
5. console.info("ndef canSetReadOnly: " + canSetReadOnly);
```

### NdefTag.setReadOnly9+

PhoneWearable

setReadOnly(): Promise<void>

将NDEF标签设置为只读。使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 ndefTag

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!ndefTag.isTagConnected()) {
9. if (!ndefTag.connectTag()) {
10. console.error("ndefTag connectTag failed.");
11. return;
12. }
13. }

15. try {
16. ndefTag.setReadOnly().then(() => {
17. console.info("ndef setReadOnly Promise success.");
18. }).catch((err : BusinessError)=> {
19. console.error("ndef setReadOnly Promise err Code: ${err.code}, message: ${err.message}");
20. });
21. } catch (businessError) {
22. console.error(`ndef setReadOnly Promise catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
23. }
24. }
```

### NdefTag.setReadOnly9+

PhoneWearable

setReadOnly(callback: AsyncCallback<void>): void

将NDEF标签设置为只读。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当NDEF标签设置为只读成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The Tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 ndefTag

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!ndefTag.isTagConnected()) {
9. if (!ndefTag.connectTag()) {
10. console.error("ndefTag connectTag failed.");
11. return;
12. }
13. }

15. try {
16. ndefTag.setReadOnly((err : BusinessError)=> {
17. if (err) {
18. console.error(`ndef setReadOnly AsyncCallback err Code: ${err.code}, message: ${err.message}`);
19. } else {
20. console.info("ndef setReadOnly AsyncCallback success.");
21. }
22. });
23. } catch (businessError) {
24. console.error(`ndef setReadOnly AsyncCallback catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
25. }
26. }
```

### NdefTag.getNdefTagTypeString9+

PhoneWearable

getNdefTagTypeString(type: [tag.NfcForumType](js-apis-nfctag.md#nfcforumtype9)): string

将NFC论坛类型，转换为NFC论坛中定义的字符串描述。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [tag.NfcForumType](js-apis-nfctag.md#nfcforumtype9) | 是 | NDEF标签类型，包括NFC FORUM TYPE 1/2/3/4等。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| string | NFC论坛类型的字符串描述。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 ndefTag

6. try {
7. let ndefTypeString : string = ndefTag.getNdefTagTypeString(tag.NfcForumType.NFC_FORUM_TYPE_1);
8. console.info("ndef ndefTypeString: " + ndefTypeString);
9. } catch (businessError) {
10. console.error(`ndef getNdefTagTypeString catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
11. }
```

## MifareClassicTag9+

PhoneWearable

MifareClassicTag提供对MIFARE Classic属性和I/O操作的访问，继承自[TagSession](js-apis-tagsession.md)。

TagSession是所有NFC Tag技术类型的基类， 提供建立连接和发送数据等共同接口。具体请参见[TagSession](js-apis-tagsession.md)。

MifareClassicTag获取方式请参考[nfc-tag开发指南](../harmonyos-guides/nfc-tag-access-guide.md)。

以下是MifareClassicTag的独有接口。

### MifareClassicTag.authenticateSector9+

PhoneWearable

authenticateSector(sectorIndex: number, key: number[], isKeyA: boolean): Promise<void>

使用密钥对扇区进行身份验证，只有身份验证成功的扇区可以进行操作。使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sectorIndex | number | 是 | 待验证的扇区索引，从0开始。 |
| key | number[] | 是 | 用于扇区验证的密钥（6字节）。 |
| isKeyA | boolean | 是 | isKeyA标志。true 表示KeyA，false 表示KeyB。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareClassic.isTagConnected()) {
9. if (!mifareClassic.connectTag()) {
10. console.error("mifareClassic connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let sectorIndex = 1; // 将其更改为正确的 index
17. let key = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06]  // 必须是6个字节，将其更改为正确的key
18. mifareClassic.authenticateSector(sectorIndex, key, true).then(() => {
19. console.info("mifareClassic authenticateSector Promise success.");
20. }).catch((err : BusinessError)=> {
21. console.error("mifareClassic authenticateSector Promise errCode: ${err.code}, " + "message: ${err.message}");
22. });
23. } catch (businessError) {
24. console.error(`mifareClassic authenticateSector Promise catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
25. }
26. }
```

### MifareClassicTag.authenticateSector9+

PhoneWearable

authenticateSector(sectorIndex: number, key: number[], isKeyA: boolean, callback: AsyncCallback<void>): void

使用密钥对扇区进行身份验证，只有身份验证成功的扇区可以进行操作。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sectorIndex | number | 是 | 待验证的扇区索引，从0开始。 |
| key | number[] | 是 | 用于扇区验证的密钥（6字节）。 |
| isKeyA | boolean | 是 | isKeyA标志。true 表示KeyA，false 表示KeyB。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当身份验证成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The Tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareClassic.isTagConnected()) {
9. if (!mifareClassic.connectTag()) {
10. console.error("mifareClassic connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let sectorIndex = 1; // 将其更改为正确的 index
17. let key = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06]  // 必须是6个字节，将其更改为正确的key
18. mifareClassic.authenticateSector(sectorIndex, key, true, (err : BusinessError)=> {
19. if (err) {
20. console.error(`mifareClassic authenticateSector AsyncCallback errCode: ${err.code}, message: ${err.message}`);
21. } else {
22. console.info("mifareClassic authenticateSector AsyncCallback success.");
23. }
24. });
25. } catch (businessError) {
26. console.error(`mifareClassic authenticateSector AsyncCallback catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
27. }
28. }
```

### MifareClassicTag.readSingleBlock9+

PhoneWearable

readSingleBlock(blockIndex: number): Promise<number[]>

读取标签中一个块存储的内容，一个块大小为16字节。使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | number | 是 | 要读取的块索引，从0开始。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<number[]> | Promise对象。返回读取的块数据。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareClassic.isTagConnected()) {
9. if (!mifareClassic.connectTag()) {
10. console.error("mifareClassic connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let blockIndex = 1; // 将其更改为正确的 index
17. mifareClassic.readSingleBlock(blockIndex).then((data : number[]) => {
18. console.info("mifareClassic readSingleBlock Promise data: " + data);
19. }).catch((err : BusinessError)=> {
20. console.error(`mifareClassic readSingleBlock Promise errCode: ${err.code}, message: ${err.message}`);
21. });
22. } catch (businessError) {
23. console.error(`mifareClassic readSingleBlock Promise catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
24. }
25. }
```

### MifareClassicTag.readSingleBlock9+

PhoneWearable

readSingleBlock(blockIndex: number, callback: AsyncCallback<number[]>): void

读取标签中一个块存储的内容，一个块大小为16字节。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | number | 是 | 要读取的块索引，从0开始。 |
| callback | AsyncCallback<number[]> | 是 | 以callback形式异步返回读取到的块数据。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The Tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareClassic.isTagConnected()) {
9. if (!mifareClassic.connectTag()) {
10. console.error("mifareClassic connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let blockIndex = 1;  // 将其更改为正确的 index
17. mifareClassic.readSingleBlock(blockIndex, (err : BusinessError, data : number[])=> {
18. if (err) {
19. console.error("mifareClassic readSingleBlock AsyncCallback err: " + err);
20. } else {
21. console.info("mifareClassic readSingleBlock AsyncCallback data: " + data);
22. }
23. });
24. } catch (businessError) {
25. console.error(`mifareClassic readSingleBlock AsyncCallback catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
26. }
27. }
```

### MifareClassicTag.writeSingleBlock9+

PhoneWearable

writeSingleBlock(blockIndex: number, data: number[]): Promise<void>

向标签中一个块存储写入内容，一个块大小为16字节。使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | number | 是 | 要写入的块索引，从0开始。 |
| data | number[] | 是 | 要写入的数据，大小必须是16个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareClassic.isTagConnected()) {
9. if (!mifareClassic.connectTag()) {
10. console.error("mifareClassic connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let blockIndex = 1; // 将其更改为正确的 index
17. let rawData = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A,
18. 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10]; // 必须是16个字节，将其更改为正确的key
19. mifareClassic.writeSingleBlock(blockIndex, rawData).then(() => {
20. console.info("mifareClassic writeSingleBlock Promise success.");
21. }).catch((err : BusinessError)=> {
22. console.error("mifareClassic writeSingleBlock Promise errCode: ${err.code}, message: ${err.message}");
23. });
24. } catch (businessError) {
25. console.error(`mifareClassic writeSingleBlock Promise catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
26. }
27. }
```

### MifareClassicTag.writeSingleBlock9+

PhoneWearable

writeSingleBlock(blockIndex: number, data: number[], callback: AsyncCallback<void>): void

向标签中一个块存储写入内容，一个块大小为16字节。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | number | 是 | 要写入的块索引，从0开始。 |
| data | number[] | 是 | 要写入的数据，大小必须是16个字节。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当向块存储写入内容成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The Tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareClassic.isTagConnected()) {
9. if (!mifareClassic.connectTag()) {
10. console.error("mifareClassic connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let blockIndex = 1; // 将其更改为正确的 index
17. let rawData = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A,
18. 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10]; // 必须是16个字节，将其更改为正确的data
19. mifareClassic.writeSingleBlock(blockIndex, rawData, (err : BusinessError)=> {
20. if (err) {
21. console.error(`mifareClassic writeSingleBlock AsyncCallback err Code: ${err.code}, message: ${err.message}`);
22. } else {
23. console.info("mifareClassic writeSingleBlock AsyncCallback success.");
24. }
25. });
26. } catch (businessError) {
27. console.error(`mifareClassic writeSingleBlock AsyncCallback catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
28. }
29. }
```

### MifareClassicTag.incrementBlock9+

PhoneWearable

incrementBlock(blockIndex: number, value: number): Promise<void>

对指定块的内容，增加指定的数值，并将结果存储在内部传输缓冲器中。使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | number | 是 | 要指定增加的块索引，从0开始。 |
| value | number | 是 | 要指定增加的数据，非负数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareClassic.isTagConnected()) {
9. if (!mifareClassic.connectTag()) {
10. console.error("mifareClassic connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let blockIndex = 1; // 将其更改为正确的 index
17. let value = 0x20; // 将其更改为正确的数据
18. mifareClassic.incrementBlock(blockIndex, value).then(() => {
19. console.info("mifareClassic incrementBlock Promise success.");
20. }).catch((err : BusinessError)=> {
21. console.error(`mifareClassic incrementBlock Promise err Code: ${err.code}, message: ${err.message}`);
22. });
23. } catch (businessError) {
24. console.error(`mifareClassic incrementBlock Promise catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
25. }
26. }
```

### MifareClassicTag.incrementBlock9+

PhoneWearable

incrementBlock(blockIndex: number, value: number, callback: AsyncCallback<void>): void

对指定块的内容，增加指定的数值，并将结果存储在内部传输缓冲器中。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | number | 是 | 要被运算的块索引，从0开始。 |
| value | number | 是 | 要增加的数值，非负数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当对块增加指定数值成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The Tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareClassic.isTagConnected()) {
9. if (!mifareClassic.connectTag()) {
10. console.error("mifareClassic connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let blockIndex = 1; // 将其更改为正确的 index
17. let value = 0x20; // 将其更改为正确的数据
18. mifareClassic.incrementBlock(blockIndex, value, (err : BusinessError)=> {
19. if (err) {
20. console.error(`mifareClassic incrementBlock AsyncCallback err Code: ${err.code}, message: ${err.message}`);
21. } else {
22. console.info("mifareClassic incrementBlock AsyncCallback success.");
23. }
24. });
25. } catch (businessError) {
26. console.error(`mifareClassic incrementBlock AsyncCallback catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
27. }
28. }
```

### MifareClassicTag.decrementBlock9+

PhoneWearable

decrementBlock(blockIndex: number, value: number): Promise<void>

对指定块的内容，减少指定的数值，并将结果存储在内部传输缓冲器中。使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | number | 是 | 要被运算的块索引，从0开始。 |
| value | number | 是 | 要减少的数值，非负数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareClassic.isTagConnected()) {
9. if (!mifareClassic.connectTag()) {
10. console.error("mifareClassic connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let blockIndex = 1; // 将其更改为正确的 index
17. let value = 0x20; // 将其更改为正确的数据
18. mifareClassic.decrementBlock(blockIndex, value).then(() => {
19. console.info("mifareClassic decrementBlock Promise success.");
20. }).catch((err : BusinessError)=> {
21. console.error("mifareClassic decrementBlock Promise errCode: ${err.code}, message: ${err.message}");
22. });
23. } catch (businessError) {
24. console.error(`mifareClassic decrementBlock Promise catch businessError: Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
25. }
26. }
```

### MifareClassicTag.decrementBlock9+

PhoneWearable

decrementBlock(blockIndex: number, value: number, callback: AsyncCallback<void>): void

对指定块的内容，减少指定的数值。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | number | 是 | 要被运算的块索引，从0开始。 |
| value | number | 是 | 要减少的数值，非负数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当对块减少指定数值成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The Tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareClassic.isTagConnected()) {
9. if (!mifareClassic.connectTag()) {
10. console.error("mifareClassic connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let blockIndex = 1; // 将其更改为正确的 index
17. let value = 0x20; // 将其更改为正确的数据
18. mifareClassic.decrementBlock(blockIndex, value, (err : BusinessError)=> {
19. if (err) {
20. console.error("mifareClassic decrementBlock AsyncCallback errCode:" +
21. "${err.code}, message: ${err.message}");
22. } else {
23. console.info("mifareClassic decrementBlock AsyncCallback success.");
24. }
25. });
26. } catch (businessError) {
27. console.error(`mifareClassic decrementBlock AsyncCallback catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
28. }
29. }
```

### MifareClassicTag.transferToBlock9+

PhoneWearable

transferToBlock(blockIndex: number): Promise<void>

将临时寄存器的值转移到指定的块。使用Promise异步异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | number | 是 | 被操作的块的索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareClassic.isTagConnected()) {
9. if (!mifareClassic.connectTag()) {
10. console.error("mifareClassic connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let blockIndex = 1; // 将其更改为正确的 index
17. mifareClassic.transferToBlock(blockIndex).then(() => {
18. console.info("mifareClassic transferToBlock Promise success.");
19. }).catch((err : BusinessError)=> {
20. console.error(`mifareClassic transferToBlock Promise err Code: ${err.code}, message: ${err.message}`);
21. });
22. } catch (businessError) {
23. console.error(`mifareClassic transferToBlock Promise catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
24. }
25. }
```

### MifareClassicTag.transferToBlock9+

PhoneWearable

transferToBlock(blockIndex: number, callback: AsyncCallback<void>): void

将临时寄存器的值转移到指定的块。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | number | 是 | 被操作的块的索引，从0开始。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当临时寄存器的值转移到指定块成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The Tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareClassic.isTagConnected()) {
9. if (!mifareClassic.connectTag()) {
10. console.error("mifareClassic connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let blockIndex = 1; // 将其更改为正确的 index
17. mifareClassic.transferToBlock(blockIndex, (err : BusinessError)=> {
18. if (err) {
19. console.error(`mifareClassic transferToBlock AsyncCallback errCode: ${err.code}, message: ${err.message}`);
20. } else {
21. console.info("mifareClassic transferToBlock AsyncCallback success.");
22. }
23. });
24. } catch (businessError) {
25. console.error(`mifareClassic transferToBlock AsyncCallback catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
26. }
27. }
```

### MifareClassicTag.restoreFromBlock9+

PhoneWearable

restoreFromBlock(blockIndex: number): Promise<void>

将指定块的值复制到临时寄存器。使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | number | 是 | 被操作的块的索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareClassic.isTagConnected()) {
9. if (!mifareClassic.connectTag()) {
10. console.error("mifareClassic connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let blockIndex = 1; // 将其更改为正确的 index
17. mifareClassic.restoreFromBlock(blockIndex).then(() => {
18. console.info("mifareClassic restoreFromBlock Promise success.");
19. }).catch((err : BusinessError)=> {
20. console.error(`mifareClassic restoreFromBlock Promise errCode: ${err.code}, message: ${err.message}`);
21. });
22. } catch (businessError) {
23. console.error(`mifareClassic restoreFromBlock Promise catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
24. }
25. }
```

### MifareClassicTag.restoreFromBlock9+

PhoneWearable

restoreFromBlock(blockIndex: number, callback: AsyncCallback<void>): void

将指定块的值复制到临时寄存器。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | number | 是 | 被操作的块的索引，从0开始。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当复制指定块内容到临时寄存器成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The Tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareClassic.isTagConnected()) {
9. if (!mifareClassic.connectTag()) {
10. console.error("mifareClassic connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let blockIndex = 1; // 将其更改为正确的 index
17. mifareClassic.restoreFromBlock(blockIndex, (err : BusinessError)=> {
18. if (err) {
19. console.error(`mifareClassic restoreFromBlock AsyncCallback err Code: ${err.code}, message: ${err.message}`);
20. } else {
21. console.info("mifareClassic restoreFromBlock AsyncCallback success.");
22. }
23. });
24. } catch (businessError) {
25. console.error(`mifareClassic restoreFromBlock AsyncCallback catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
26. }
27. }
```

### MifareClassicTag.getSectorCount9+

PhoneWearable

getSectorCount(): number

获取MIFARE Classic标签中的扇区数。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | 标签中的扇区数量。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic
5. let sectorCount : number = mifareClassic.getSectorCount();
6. console.info("mifareClassic sectorCount: " + sectorCount);
```

### MifareClassicTag.getBlockCountInSector9+

PhoneWearable

getBlockCountInSector(sectorIndex: number): number

获取指定扇区中的块数。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sectorIndex | number | 是 | 扇区序号，从0开始。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | 该扇区内的块数量。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. try {
7. let sectorIndex = 1; // 将其更改为正确的 index
8. let blockCnt : number = mifareClassic.getBlockCountInSector(sectorIndex);
9. console.info("mifareClassic blockCnt: " + blockCnt);
10. } catch (businessError) {
11. console.error(`mifareClassic getBlockCountInSector catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
12. }
```

### MifareClassicTag.getType9+

PhoneWearable

getType(): [tag.MifareClassicType](js-apis-nfctag.md#mifareclassictype9)

获取MIFARE Classic标签的类型。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [tag.MifareClassicType](js-apis-nfctag.md#mifareclassictype9) | MifareClassic标签的类型。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic
4. let getType : tag.MifareClassicType = mifareClassic.getType();
5. console.info("mifareClassic getType: " + getType);
```

### MifareClassicTag.getTagSize9+

PhoneWearable

getTagSize(): number

获取标签的存储空间大小，具体请参见[MifareClassicSize](js-apis-nfctag.md#mifareclassicsize9)。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | 标签的大小，单位为字节，请参见[MifareClassicSize](js-apis-nfctag.md#mifareclassicsize9)。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic
5. let tagSize : number = mifareClassic.getTagSize();
6. console.info("mifareClassic tagSize: " + tagSize);
```

### MifareClassicTag.isEmulatedTag9+

PhoneWearable

isEmulatedTag(): boolean

检查标签是不是被模拟的。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | 检查结果，true: 是；false：否。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic
5. let isEmulatedTag : boolean = mifareClassic.isEmulatedTag();
6. console.info("mifareClassic isEmulatedTag: " + isEmulatedTag);
```

### MifareClassicTag.getBlockIndex9+

PhoneWearable

getBlockIndex(sectorIndex: number): number

获取特定扇区的第一个块的序号。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sectorIndex | number | 是 | 扇区序号，从0开始。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | 该扇区内的第一个块的序号，从0开始。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. try {
7. let sectorIndex = 1; // 将其更改为正确的 index
8. let blockIndex : number = mifareClassic.getBlockIndex(sectorIndex);
9. console.info("mifareClassic blockIndex: " + blockIndex);
10. } catch (businessError) {
11. console.error(`mifareClassic getBlockIndex catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
12. }
```

### MifareClassicTag.getSectorIndex9+

PhoneWearable

getSectorIndex(blockIndex: number): number

获取包含指定块号的扇区序号。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | number | 是 | 块序号，从0开始。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | 扇区序号，从0开始。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareClassic

6. try {
7. let blockIndex = 1; // 将其更改为正确的 index
8. let sectorIndex : number = mifareClassic.getSectorIndex(blockIndex);
9. console.info("mifareClassic sectorIndex: " + sectorIndex);
10. } catch (businessError) {
11. console.error(`mifareClassic getSectorIndex catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
12. }
```

## MifareUltralightTag9+

PhoneWearable

MifareUltralightTag 提供对MIFARE Ultralight属性和I/O操作的访问，继承自TagSession。

TagSession是所有NFC Tag技术类型的基类， 提供建立连接和发送数据等共同接口。具体请参见[TagSession](js-apis-tagsession.md)。

MifareUltralightTag获取方式请参考[nfc-tag开发指南](../harmonyos-guides/nfc-tag-access-guide.md)。

以下是MifareUltralightTag的独有接口。

### MifareUltralightTag.readMultiplePages9+

PhoneWearable

readMultiplePages(pageIndex: number): Promise<number[]>

读取标签的4页数据，共16字节的数据。每个页面数据大小为4字节。使用Promise异步回调

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 要读取页面的索引，从0开始。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<number[]> | Promise对象。以Promise形式返回读取的4页的数据，共16字节。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareUltralight

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareUltralight.isTagConnected()) {
9. if (!mifareUltralight.connectTag()) {
10. console.error("mifareUltralight connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let pageIndex = 1; // 将其更改为正确的 index
17. mifareUltralight.readMultiplePages(pageIndex).then((data : number[]) => {
18. console.info("mifareUltralight readMultiplePages Promise data = " + data);
19. }).catch((err : BusinessError)=> {
20. console.error(`mifareUltralight readMultiplePages Promise Code: ${err.code}, message: ${err.message}`);
21. });
22. } catch (businessError) {
23. console.error(`mifareUltralight readMultiplePages Promise catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
24. }
25. }
```

### MifareUltralightTag.readMultiplePages9+

PhoneWearable

readMultiplePages(pageIndex: number, callback: AsyncCallback<number[]>): void

读取标签的4页数据，共16字节的数据。每个页面数据大小为4字节。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 要读取页面的索引，从0开始。 |
| callback | AsyncCallback<number[]> | 是 | 以callback形式异步返回页操作结果。返回读取到的数据，共16字节。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The Tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareUltralight

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareUltralight.isTagConnected()) {
9. if (!mifareUltralight.connectTag()) {
10. console.error("mifareUltralight connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let pageIndex = 1; // 将其更改为正确的 index
17. mifareUltralight.readMultiplePages(pageIndex, (err : BusinessError, data : number[])=> {
18. if (err) {
19. console.error(`mifareUltralight readMultiplePages AsyncCallback Code: ${err.code}, message: ${err.message}`);
20. } else {
21. console.info("mifareUltralight readMultiplePages AsyncCallback data: " + data);
22. }
23. });
24. } catch (businessError) {
25. console.error(`mifareUltralight readMultiplePages AsyncCallback catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
26. }
27. }
```

### MifareUltralightTag.writeSinglePage9+

PhoneWearable

writeSinglePage(pageIndex: number, data: number[]): Promise<void>

写入一页数据，数据大小为4字节。使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 要写入页面的索引，从0开始。 |
| data | number[] | 是 | 要写入页面的数据内容，必须是4个字节大小。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareUltralight

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareUltralight.isTagConnected()) {
9. if (!mifareUltralight.connectTag()) {
10. console.error("mifareUltralight connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let pageIndex = 1; // 将其更改为正确的 index
17. let rawData = [0x01, 0x02, 0x03, 0x04]; // 必须是4个字节，将其更改为正确的data
18. mifareUltralight.writeSinglePage(pageIndex, rawData).then(() => {
19. console.info("mifareUltralight writeSinglePage Promise success.");
20. }).catch((err : BusinessError)=> {
21. console.error(`mifareUltralight writeSinglePage Promise err Code: ${err.code}, message: ${err.message}`);
22. });
23. } catch (businessError) {
24. console.error(`mifareUltralight writeSinglePage Promise catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
25. }
26. }
```

### MifareUltralightTag.writeSinglePage9+

PhoneWearable

writeSinglePage(pageIndex: number, data: number[], callback: AsyncCallback<void>): void

写入一页数据，数据大小为4字节。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 要写入页面的索引，从0开始。 |
| data | number[] | 是 | 要写入页面的数据内容，必须是4个字节大小。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当写入数据成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The Tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareUltralight

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!mifareUltralight.isTagConnected()) {
9. if (!mifareUltralight.connectTag()) {
10. console.error("mifareUltralight connectTag failed.");
11. return;
12. }
13. }

15. try {
16. let pageIndex = 1; // 将其更改为正确的 index
17. let rawData = [0x01, 0x02, 0x03, 0x04];  // 必须是4个字节，将其更改为正确的data
18. mifareUltralight.writeSinglePage(pageIndex, rawData, (err : BusinessError)=> {
19. if (err) {
20. console.error(`mifareUltralight writeSinglePage AsyncCallback Code: ${err.code}, message: ${err.message}`);
21. } else {
22. console.info("mifareUltralight writeSinglePage AsyncCallback success.");
23. }
24. });
25. } catch (businessError) {
26. console.error(`mifareUltralight writeSinglePage AsyncCallback catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
27. }
28. }
```

### MifareUltralightTag.getType9+

PhoneWearable

getType(): [tag.MifareUltralightType](js-apis-nfctag.md#mifareultralighttype9)

获取MIFARE Ultralight标签的类型。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [tag.MifareUltralightType](js-apis-nfctag.md#mifareultralighttype9) | MIFARE Ultralight标签的类型。 |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 mifareUltralight
4. let getType : tag.MifareUltralightType = mifareUltralight.getType();
5. console.info("mifareUltralight getType: " + getType);
```

## NdefFormatableTag9+

PhoneWearable

NdefFormatableTag为NDEF Formattable的标签提供格式化操作，继承自TagSession。

TagSession是所有NFC Tag 技术类型的基类， 提供建立连接和发送数据等共同接口。具体请参见[TagSession](js-apis-tagsession.md)。

NdefFormatableTag获取方式请参考[nfc-tag开发指南](../harmonyos-guides/nfc-tag-access-guide.md)。

以下是NdefFormatableTag的独有接口。

### NdefFormatableTag.format9+

PhoneWearable

format(message: [NdefMessage](js-apis-nfctech.md#ndefmessage9)): Promise<void>

将标签格式化为NDEF标签，将NDEF消息写入NDEF标签。使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | [NdefMessage](js-apis-nfctech.md#ndefmessage9) | 是 | 格式化成功时要写入的NDEF消息。可以为null，为null时仅格式化标签，不写入内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 ndefFormatable

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!ndefFormatable.isTagConnected()) {
9. if (!ndefFormatable.connectTag()) {
10. console.error("ndefFormatable connectTag failed.");
11. return;
12. }
13. }

15. try {
16. // 从原始数据创建的ndefMessage，例如：
17. let ndefMessage = tag.ndef.createNdefMessage([0xD1, 0x01, 0x03, 0x54, 0x4E, 0x46, 0x43]);
18. // 必须是可以被解析的NDEF记录
19. // 或从 tag.ndef.createNdefMessage(ndefRecords:NdefRecord[]) 创建 ndefMessage

21. ndefFormatable.format(ndefMessage).then(() => {
22. console.info("ndefFormatable format Promise success.");
23. }).catch((err : BusinessError)=> {
24. console.error(`ndefFormatable format Promise err Code: ${err.code}, message: ${err.message}`);
25. });
26. } catch (businessError) {
27. console.error(`ndefFormatable format Promise catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
28. }
29. }
```

### NdefFormatableTag.format9+

PhoneWearable

format(message: [NdefMessage](js-apis-nfctech.md#ndefmessage9), callback: AsyncCallback<void>): void

将标签格式化为NDEF标签，然后将NDEF消息写入NDEF标签。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | [NdefMessage](js-apis-nfctech.md#ndefmessage9) | 是 | 格式化成功时要写入的Ndef消息。可以为null，为null时仅格式化标签，不写入内容。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当NDEF消息写入标签成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The Tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 ndefFormatable

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!ndefFormatable.isTagConnected()) {
9. if (!ndefFormatable.connectTag()) {
10. console.error("ndefFormatable connectTag failed.");
11. return;
12. }
13. }

15. try {
16. // 从原始数据创建的ndefMessage，例如：
17. let ndefMessage = tag.ndef.createNdefMessage([0xD1, 0x01, 0x03, 0x54, 0x4E, 0x46, 0x43]);  // 必须是可以被解析的NDEF记录
18. // 或从 tag.ndef.createNdefMessage(ndefRecords:NdefRecord[]) 创建 ndefMessage

20. ndefFormatable.format(ndefMessage, (err : BusinessError)=> {
21. if (err) {
22. console.error(`ndefFormatable format AsyncCallback Code: ${err.code}, message: ${err.message}`);
23. } else {
24. console.info("ndefFormatable format AsyncCallback success.");
25. }
26. });
27. } catch (businessError) {
28. console.error(`ndefFormatable format AsyncCallback catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
29. }
30. }
```

### NdefFormatableTag.formatReadOnly9+

PhoneWearable

formatReadOnly(message: [NdefMessage](js-apis-nfctech.md#ndefmessage9)): Promise<void>

将标签格式化为NDEF标签，将NDEF消息写入NDEF标签，之后将标签设置为只读。使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | [NdefMessage](js-apis-nfctech.md#ndefmessage9) | 是 | 格式化成功时要写入的NDEF消息。可以为null，为null时仅格式化标签，不写入内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 ndefFormatable

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!ndefFormatable.isTagConnected()) {
9. if (!ndefFormatable.connectTag()) {
10. console.error("ndefFormatable connectTag failed.");
11. return;
12. }
13. }

15. try {
16. // 从原始数据创建的ndefMessage，例如：
17. let ndefMessage = tag.ndef.createNdefMessage([0xD1, 0x01, 0x03, 0x54, 0x4E, 0x46, 0x43]);
18. // 必须是可以被解析的NDEF记录
19. // 或从 tag.ndef.createNdefMessage(ndefRecords:NdefRecord[]) 创建 ndefMessage

21. ndefFormatable.formatReadOnly(ndefMessage).then(() => {
22. console.info("ndefFormatable formatReadOnly Promise success.");
23. }).catch((err : BusinessError)=> {
24. console.error(`ndefFormatable formatReadOnly Promise Code: ${err.code}, message: ${err.message}`);
25. });
26. } catch (businessError) {
27. console.error(`ndefFormatable formatReadOnly Promise catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
28. }
29. }
```

### NdefFormatableTag.formatReadOnly9+

PhoneWearable

formatReadOnly(message: [NdefMessage](js-apis-nfctech.md#ndefmessage9), callback: AsyncCallback<void>): void

将标签格式化为NDEF标签，然后将NDEF消息写入NDEF标签，之后将标签设置为只读。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | [NdefMessage](js-apis-nfctech.md#ndefmessage9) | 是 | 格式化成功时要写入的NDEF消息。可以为null，为null时仅格式化标签，不写入内容。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当NDEF消息写入NDEF标签成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The Tag I/O operation failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 参考 @ohos.nfc.tag（标准NFC-Tag）中 tag.TagInfo 接口，获取正确的 ndefFormatable

6. function nfcTechDemo() {
7. // 如果没有连接Tag，请先连接
8. if (!ndefFormatable.isTagConnected()) {
9. if (!ndefFormatable.connectTag()) {
10. console.error("ndefFormatable connectTag failed.");
11. return;
12. }
13. }

15. try {
16. // 从原始数据创建的ndefMessage，例如：
17. let ndefMessage = tag.ndef.createNdefMessage([0xD1, 0x01, 0x03, 0x54, 0x4E, 0x46, 0x43]);
18. // 必须是可以被解析的NDEF记录
19. // 或从 tag.ndef.createNdefMessage(ndefRecords:NdefRecord[]) 创建 ndefMessage

21. ndefFormatable.formatReadOnly(ndefMessage, (err : BusinessError)=> {
22. if (err) {
23. console.error(`ndefFormatable formatReadOnly AsyncCallback err Code: ${err.code}, message: ${err.message}`);
24. } else {
25. console.info("ndefFormatable formatReadOnly AsyncCallback success.");
26. }
27. });
28. } catch (businessError) {
29. console.error(`ndefFormatable formatReadOnly AsyncCallback catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
30. }
31. }
```

## BarcodeTag18+

PhoneWearable

BarcodeTag提供读取条形码标签的属性和访问I/O操作的能力，继承自TagSession。

TagSession是所有NFC Tag 技术类型的基类， 提供建立连接和发送数据等共同接口。具体请参见[TagSession](js-apis-tagsession.md)。

BarcodeTag获取方式请参考[nfc-tag开发指南](../harmonyos-guides/nfc-tag-access-guide.md)。

以下是BarcodeTag的独有接口。

### BarcodeTag.getBarcode18+

PhoneWearable

getBarcode(): Promise<ArrayBuffer>

获取读到的Barcode类型的完整Tag。使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象。返回BarCode类型的 tag。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |
