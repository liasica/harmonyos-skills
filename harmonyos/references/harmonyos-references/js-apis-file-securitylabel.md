---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-securitylabel
title: "@ohos.file.securityLabel (数据标签)"
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > ArkTS API > @ohos.file.securityLabel (数据标签)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2c5456e608acdfeec995c08f4ce1f1d5f841efa10cabe2350cc3170e5cc8d2eb
---

该模块提供文件数据安全等级的相关功能：向应用程序提供查询、设置文件数据安全等级的ArkTS接口。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { securityLabel } from '@kit.CoreFileKit';
```

## 使用说明

使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取方式及其接口用法请参考：

```ts
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let context = this.context;
    let pathDir = context.filesDir;
  }
}
```

使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取方式及其接口用法请参考：[应用上下文Context-获取应用文件路径](../harmonyos-guides/application-context-stage.md#获取应用文件路径)。

## DataLevel

type DataLevel = 's0' | 's1' | 's2' | 's3' | 's4'

数据安全等级。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 类型 | 说明 |
| --- | --- |
| 's0' | 数据安全等级"S0"。 |
| 's1' | 数据安全等级"S1"。 |
| 's2' | 数据安全等级"S2"。 |
| 's3' | 数据安全等级"S3"。 |
| 's4' | 数据安全等级"S4"。 |

数据安全等级详细说明请见[数据安全标签](../harmonyos-guides/access-control-by-device-and-data-level.md#数据安全标签)。

## securityLabel.setSecurityLabel

setSecurityLabel(path:string, type:DataLevel):Promise<void>

设置文件或目录的数据安全等级。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |
| type | [DataLevel](js-apis-file-securitylabel.md#datalevel) | 是 | 数据安全等级，只支持"s0","s1","s2","s3","s4"。  **注意**：数据安全等级仅可由低向高或同级设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900007 | Arg list too long |
| 13900015 | File exists |
| 13900020 | Invalid argument |
| 13900025 | No space left on device |
| 13900037 | No data available |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + '/test.txt';
securityLabel.setSecurityLabel(filePath, "s0").then(() => {
  console.info("Succeeded in setting security label.");
}).catch((err: BusinessError) => {
  console.error("Failed to set security label. Code: " + err.code + ", message: " + err.message);
});
```

## securityLabel.setSecurityLabel

setSecurityLabel(path:string, type:DataLevel, callback: AsyncCallback<void>):void

设置文件或目录的数据安全等级。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |
| type | [DataLevel](js-apis-file-securitylabel.md#datalevel) | 是 | 数据安全等级，只支持"s0","s1","s2","s3","s4"。  **注意**：数据安全等级仅可由低向高或同级设置。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置数据安全等级成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900007 | Arg list too long |
| 13900015 | File exists |
| 13900020 | Invalid argument |
| 13900025 | No space left on device |
| 13900037 | No data available |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + '/test.txt';
securityLabel.setSecurityLabel(filePath, "s0", (err: BusinessError) => {
  if (err) {
    console.error("Failed to set security label. Code: " + err.code + ", message: " + err.message);
  } else {
    console.info("Succeeded in setting security label.");
  }
});
```

## securityLabel.setSecurityLabelSync

setSecurityLabelSync(path:string, type:DataLevel):void

以同步方法设置文件或目录的数据安全等级。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |
| type | [DataLevel](js-apis-file-securitylabel.md#datalevel) | 是 | 数据安全等级，只支持"s0","s1","s2","s3","s4"。  **注意**：数据安全等级仅可由低向高或同级设置。 |

**错误码：**

以下错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900007 | Arg list too long |
| 13900015 | File exists |
| 13900020 | Invalid argument |
| 13900025 | No space left on device |
| 13900037 | No data available |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

**示例：**

```ts
let filePath = pathDir + '/test.txt';
securityLabel.setSecurityLabelSync(filePath, "s0");
```

## securityLabel.getSecurityLabel

getSecurityLabel(path:string):Promise<string>

获取文件或目录的数据安全等级。若未设置过数据安全等级则默认返回“s3”。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回数据安全等级。 |

**错误码：**

以下错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900007 | Arg list too long |
| 13900015 | File exists |
| 13900020 | Invalid argument |
| 13900025 | No space left on device |
| 13900037 | No data available |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + '/test.txt';
securityLabel.getSecurityLabel(filePath).then((type: string) => {
  console.info("Succeeded in getting security label, Label: " + type);
}).catch((err: BusinessError) => {
  console.error("Failed to get security label. Code: " + err.code + ", message: " + err.message);
});
```

## securityLabel.getSecurityLabel

getSecurityLabel(path:string, callback:AsyncCallback<string>): void

获取文件或目录的数据安全等级。若未设置过数据安全等级则默认返回“s3”。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |
| callback | AsyncCallback<string> | 是 | 回调函数，返回安全等级。 |

**错误码：**

以下错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900007 | Arg list too long |
| 13900015 | File exists |
| 13900020 | Invalid argument |
| 13900025 | No space left on device |
| 13900037 | No data available |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + '/test.txt';
securityLabel.getSecurityLabel(filePath, (err: BusinessError, type: string) => {
  if (err) {
    console.error("Failed to get security label. Code: " + err.code + ", message: " + err.message);
  } else {
    console.info("Succeeded in getting security label, Label: " + type);
  }
});
```

## securityLabel.getSecurityLabelSync

getSecurityLabelSync(path:string):string

以同步方法获取文件或目录的数据安全等级。若未设置过数据安全等级则默认返回“s3”。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回数据安全等级。 |

**错误码：**

以下错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900007 | Arg list too long |
| 13900015 | File exists |
| 13900020 | Invalid argument |
| 13900025 | No space left on device |
| 13900037 | No data available |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

**示例：**

```ts
let filePath = pathDir + '/test.txt';
let type = securityLabel.getSecurityLabelSync(filePath);
console.info("Succeeded in getting security label, Label: " + type);
```
