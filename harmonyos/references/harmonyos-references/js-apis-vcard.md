---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vcard
title: "@ohos.telephony.vcard (VCard模块)"
breadcrumb: API参考 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > ArkTS API > @ohos.telephony.vcard (VCard模块)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b86794d748cda23e9dad2b329f936030e39818ebbfe3513bc777d43400b65e4a
---

VCard是电子名片的文件格式标准，它可包含的信息有：姓名、地址资讯、电话号码、URL、logo、相片等。VCard模块提供了VCard能力，包括将VCard文件导入联系人数据库和将联系人数据导出为VCard文件等。

**说明** 

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { vcard } from '@kit.TelephonyKit';
```

## vcard.importVCard

importVCard(context: Context, filePath: string, accountId: number, callback: AsyncCallback<void>): void

将VCard文件导入联系人数据库。适用于从其他设备或应用接收VCard文件后批量导入联系人、联系人数据恢复等场景。使用callback异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS 和 ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| filePath | string | 是 | VCF(VCard file)文件地址。 |
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

```ts
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { vcard } from '@kit.TelephonyKit';

class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
        let filePath: string = '/data/storage/vcf/contacts.vcf';
        let accountId: number = 0;
        vcard.importVCard(this.context, filePath, accountId, (err: BusinessError) => {
            console.error(`callback: err->${JSON.stringify(err)}`);
        });
    }
}
```

## vcard.importVCard

importVCard(context: Context, filePath: string, accountId?: number): Promise<void>

将VCard文件导入联系人数据库。适用于从其他设备或应用接收VCard文件后批量导入联系人、联系人数据恢复等场景。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS 和 ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| filePath | string | 是 | VCF(VCard file)文件地址。 |
| accountId | number | 否 | 联系人账户ID。不传入时使用默认账户。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

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

```ts
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { vcard } from '@kit.TelephonyKit';

class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
        let filePath: string = '/data/storage/vcf/contacts.vcf';
        let accountId: number = 0;
        vcard.importVCard(this.context, filePath, accountId).then(() => {
            console.info(`importVCard success.`);
        }).catch((err: BusinessError) => {
            console.error(`importVCard failed, promise: err->${JSON.stringify(err)}`);
        });
    }
}
```

## vcard.importVCard

importVCard(context: Context, filePath: string, callback: AsyncCallback<void>): void

将VCard文件导入联系人数据库。适用于从其他设备或应用接收VCard文件后批量导入联系人、联系人数据恢复等场景。使用callback异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS 和 ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| filePath | string | 是 | VCF(VCard file)文件地址。 |
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

```ts
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { vcard } from '@kit.TelephonyKit';

class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
        let filePath: string = "/data/storage/vcf/contacts.vcf";
        vcard.importVCard(this.context, filePath, (err: BusinessError) => {
            console.error(`callback: err->${JSON.stringify(err)}`);
        });
    }
}
```

## vcard.exportVCard

exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, options: VCardBuilderOptions, callback: AsyncCallback<string>): void

将联系人导出为 VCF(VCard file)文件。适用于联系人数据备份、跨设备迁移联系人、通过文件分享联系人等场景。使用callback异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS 和 ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| predicates | [dataSharePredicates.DataSharePredicates](js-apis-data-datasharepredicates.md) | 是 | 查询语句。用于筛选要导出的联系人数据。 |
| options | VCardBuilderOptions | 是 | VCard版本与编码类型。 |
| callback | AsyncCallback<string> | 是 | 回调函数。生成的 VCF(VCard file)文件地址。 |

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

```ts
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { vcard } from '@kit.TelephonyKit';
import { dataSharePredicates } from '@kit.ArkData';

class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
        let predicates = new dataSharePredicates.DataSharePredicates();
        predicates.equalTo('NAME', 'Rose');
        let options: vcard.VCardBuilderOptions = {
            cardType: vcard.VCardType.VERSION_21,
            charset: 'UTF-8'
        };
        vcard.exportVCard(this.context, predicates, options, (err: BusinessError, data: string) => {
            console.error(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
        });
    }
}
```

## vcard.exportVCard

exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, options?: VCardBuilderOptions): Promise<string>

将联系人导出为 VCF(VCard file)文件。适用于联系人数据备份、跨设备迁移联系人、通过文件分享联系人等场景。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS 和 ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| predicates | [dataSharePredicates.DataSharePredicates](js-apis-data-datasharepredicates.md) | 是 | 查询语句。用于筛选要导出的联系人数据。 |
| options | VCardBuilderOptions | 否 | VCard版本与编码类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回生成的VCF(VCard file)文件地址。 |

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

```ts
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { vcard } from '@kit.TelephonyKit';
import { dataSharePredicates } from '@kit.ArkData';

class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
        let predicates = new dataSharePredicates.DataSharePredicates();
        predicates.equalTo("NAME", "Rose");
        let options: vcard.VCardBuilderOptions = {
            cardType: vcard.VCardType.VERSION_21,
            charset: "UTF-8"
        };
        vcard.exportVCard(this.context, predicates, options).then(() => {
            console.info(`exportVCard success.`);
        }).catch((err: BusinessError) => {
            console.error(`exportVCard failed, promise: err->${JSON.stringify(err)}`);
        });
    }
}
```

## vcard.exportVCard

exportVCard(context: Context, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<string>): void

将联系人导出为 VCF(VCard file)文件。适用于联系人数据备份、跨设备迁移联系人、通过文件分享联系人等场景。使用callback异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS 和 ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| predicates | [dataSharePredicates.DataSharePredicates](js-apis-data-datasharepredicates.md) | 是 | 查询语句。用于筛选要导出的联系人。 |
| callback | AsyncCallback<string> | 是 | 回调函数。生成的 VCF(VCard file)文件地址。 |

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

```ts
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { vcard } from '@kit.TelephonyKit';
import { dataSharePredicates } from '@kit.ArkData';

class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
        let predicates = new dataSharePredicates.DataSharePredicates();
        predicates.equalTo("NAME", "Rose");

        vcard.exportVCard(this.context, predicates, (err: BusinessError, data: string) => {
            console.error(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
        });
    }
}
```

## VCardBuilderOptions

VCard版本和编码信息。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| cardType | [VCardType](js-apis-vcard.md#vcardtype) | 否 | 是 | VCard版本类型（默认值为VERSION\_21）。 |
| charset | string | 否 | 是 | VCard编码类型（默认值为'UTF-8'）。 |

## VCardType

VCard版本类型。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VERSION\_21 | 0 | VCard2.1版本。 |
| VERSION\_30 | 1 | VCard3.0版本。 |
| VERSION\_40 | 2 | VCard4.0版本。 |
