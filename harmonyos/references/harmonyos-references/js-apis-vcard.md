---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vcard
title: @ohos.telephony.vcard (VCard模块)
breadcrumb: API参考 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > ArkTS API > @ohos.telephony.vcard (VCard模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0bbbc082a3d7ff6e7c5464a370f02e3ca7b3d1e8cab04cc9ae6efd7aa9c16b1a
---

VCard是电子名片的文件格式标准，它可包含的信息有：姓名、地址资讯、电话号码、URL、logo、相片等。VCard模块提供了VCard能力，包括将VCard文件导入联系人数据库和将联系人数据导出为VCard文件等。

说明

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhoneTabletWearable

```
1. import { vcard } from '@kit.TelephonyKit';
```

## vcard.importVCard

PhoneTabletWearable

importVCard(context: Context, filePath: string, accountId: number, callback: AsyncCallback<void>): void

将VCard文件导入联系人数据库。使用callback异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS 和 ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| filePath | string | 是 | VCF(vcard file)文件地址。 |
| accountId | number | 是 | 联系人账户ID。 |
| callback | AsyncCallback<void> | 是 | 回调函数，返回导入成功或失败的状态码。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { window } from '@kit.ArkUI';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { vcard } from '@kit.TelephonyKit';

6. class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. let filePath: string = "/data/storage/vcf/contacts.vcf";
9. let accountId: number = 0;
10. vcard.importVCard(this.context, filePath, accountId, (err: BusinessError) => {
11. console.error(`callback: err->${JSON.stringify(err)}`);
12. });
13. }
14. }
```

## vcard.importVCard

PhoneTabletWearable

importVCard(context: Context, filePath: string, accountId?: number): Promise<void>

将VCard文件导入联系人数据库。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS 和 ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| filePath | string | 是 | VCF(vcard file)文件地址。 |
| accountId | number | 否 | 联系人账户ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回重置的结果码。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { window } from '@kit.ArkUI';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { vcard } from '@kit.TelephonyKit';

6. class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. let filePath: string = "/data/storage/vcf/contacts.vcf";
9. let accountId: number = 0;
10. vcard.importVCard(this.context, filePath, accountId).then(() => {
11. console.info(`importVCard success.`);
12. }).catch((err: BusinessError) => {
13. console.error(`importVCard failed, promise: err->${JSON.stringify(err)}`);
14. });
15. }
16. }
```

## vcard.importVCard

PhoneTabletWearable

importVCard(context: Context, filePath: string, callback: AsyncCallback<void>): void

将VCard文件导入联系人数据库。使用callback异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS 和 ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| filePath | string | 是 | VCF(vcard file)文件地址。 |
| callback | AsyncCallback<void> | 是 | 回调函数，返回导入成功或失败的状态码。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { window } from '@kit.ArkUI';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { vcard } from '@kit.TelephonyKit';

6. class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. let filePath: string = "/data/storage/vcf/contacts.vcf";
9. vcard.importVCard(this.context, filePath, (err: BusinessError) => {
10. console.error(`callback: err->${JSON.stringify(err)}`);
11. });
12. }
13. }
```

## vcard.exportVCard

PhoneTabletWearable

exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, options: VCardBuilderOptions, callback: AsyncCallback<string>): void

将联系人导出为 VCF(vcard file)文件。使用callback异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS 和 ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| predicates | [dataSharePredicates.DataSharePredicates](js-apis-data-datasharepredicates.md) | 是 | 查询语句。 |
| options | VCardBuilderOptions | 是 | VCard版本与编码类型。 |
| callback | AsyncCallback<string> | 是 | 回调函数。生成的 VCF(vcard file)文件地址。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { window } from '@kit.ArkUI';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { vcard } from '@kit.TelephonyKit';
5. import { dataSharePredicates } from '@kit.ArkData';

7. class EntryAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage) {
9. let predicates = new dataSharePredicates.DataSharePredicates();
10. predicates.equalTo("NAME", "Rose");
11. let options: vcard.VCardBuilderOptions = {
12. cardType: vcard.VCardType.VERSION_21,
13. charset: "UTF-8"
14. };
15. vcard.exportVCard(this.context, predicates, options, (err: BusinessError, data: string) => {
16. console.error(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
17. });
18. }
19. }
```

## vcard.exportVCard

PhoneTabletWearable

exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, options?: VCardBuilderOptions): Promise<string>

将联系人导出为 VCF(vcard file)文件。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS 和 ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| predicates | [dataSharePredicates.DataSharePredicates](js-apis-data-datasharepredicates.md) | 是 | 查询语句。 |
| options | VCardBuilderOptions | 否 | VCard版本与编码类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回重置的结果码。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { window } from '@kit.ArkUI';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { vcard } from '@kit.TelephonyKit';
5. import { dataSharePredicates } from '@kit.ArkData';

7. class EntryAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage) {
9. let predicates = new dataSharePredicates.DataSharePredicates();
10. predicates.equalTo("NAME", "Rose");
11. let options: vcard.VCardBuilderOptions = {
12. cardType: vcard.VCardType.VERSION_21,
13. charset: "UTF-8"
14. };
15. vcard.exportVCard(this.context, predicates, options).then(() => {
16. console.info(`exportVCard success.`);
17. }).catch((err: BusinessError) => {
18. console.error(`exportVCard failed, promise: err->${JSON.stringify(err)}`);
19. });
20. }
21. }
```

## vcard.exportVCard

PhoneTabletWearable

exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<string>): void

将联系人导出为 VCF(vcard file)文件。使用callback异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS 和 ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| predicates | [dataSharePredicates.DataSharePredicates](js-apis-data-datasharepredicates.md) | 是 | 查询语句。 |
| callback | AsyncCallback<string> | 是 | 回调函数。生成的 VCF(vcard file)文件地址。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { window } from '@kit.ArkUI';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { vcard } from '@kit.TelephonyKit';
5. import { dataSharePredicates } from '@kit.ArkData';

7. class EntryAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage) {
9. let predicates = new dataSharePredicates.DataSharePredicates();
10. predicates.equalTo("NAME", "Rose");

12. vcard.exportVCard(this.context, predicates, (err: BusinessError, data: string) => {
13. console.error(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
14. });
15. }
16. }
```

## VCardBuilderOptions

PhoneTabletWearable

VCard版本和编码信息。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| cardType | [VCardType](js-apis-vcard.md#vcardtype) | 否 | 是 | VCard版本类型 (默认值为VERSION\_21)。 |
| charset | string | 否 | 是 | VCard编码类型（默认值为'UTF-8'）。 |

## VCardType

PhoneTabletWearable

VCard版本类型。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VERSION\_21 | 0 | VCard2.1版本。 |
| VERSION\_30 | 1 | VCard3.0版本。 |
| VERSION\_40 | 2 | VCard4.0版本。 |
