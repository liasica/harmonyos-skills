---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fileshare
title: "@ohos.fileshare (文件分享)"
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > ArkTS API > @ohos.fileshare (文件分享)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d632247b81a10ad62cb54f8fbb47be5ae6d7b62555db08a02953f790298bdc54
---

该模块提供文件分享能力，支持系统应用将公共目录文件统一资源标识符（Uniform Resource Identifier，URI）按指定访问模式授权给其他应用，并支持持久化授权、权限激活和授权状态查询。授权后，应用可通过[@ohos.file.fs](js-apis-file-fs.md)的相关接口进行open、read、write等操作，实现应用间文件共享、跨应用文件编辑、文档协作等场景。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { fileShare } from '@kit.CoreFileKit';
```

## OperationMode11+

枚举，授予或激活权限的URI访问模式。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 值 | 说明 |
| --- | --- | --- |
| READ\_MODE | 0b1 | 读权限。 |
| WRITE\_MODE | 0b10 | 写权限。 |
| CREATE\_MODE20+ | 0b100 | 创建权限。父目录无写权限时，可单独为目标授予权限，支持文件/文件夹创建。当父目录有写权限时，无需单独授权。 |
| DELETE\_MODE20+ | 0b1000 | 删除权限。父目录无写权限时，可单独为目标授予权限，支持文件/文件夹删除。当父目录有写权限时，无需单独授权。 |
| RENAME\_MODE20+ | 0b10000 | 重命名权限。父目录无写权限时，可单独为目标授予权限，支持文件/文件夹重命名。当父目录有写权限时，无需单独授权。 |

## PolicyErrorCode11+

枚举，授予或激活权限策略失败的URI对应的错误码。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PERSISTENCE\_FORBIDDEN | 1 | URI禁止被持久化。 |
| INVALID\_MODE | 2 | 无效的模式。 |
| INVALID\_PATH | 3 | 无效的路径。 |
| PERMISSION\_NOT\_PERSISTED12+ | 4 | 权限没有被持久化。 |

## PolicyErrorResult11+

授予或激活权限失败的URI策略结果。支持在persistPermission、revokePermission、activatePermission、deactivatePermission接口抛出错误时使用。

**说明** 

从API version 23开始，PolicyErrorResult由type变更为interface类型。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 授予或激活权限失败的URI。 |
| code | [PolicyErrorCode](js-apis-fileshare.md#policyerrorcode11) | 否 | 否 | 授权策略失败的URI对应的错误码。 |
| message | string | 否 | 否 | 授权策略失败的URI对应的原因。 |

## PolicyInfo11+

需要授予或激活URI访问权限的策略信息。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 需要授予或激活访问权限的URI，需符合URI格式规范。 |
| operationMode | number | 否 | 否 | 授予或激活权限的URI访问模式，参考[OperationMode](js-apis-fileshare.md#operationmode11)。可取READ\_MODE、WRITE\_MODE、CREATE\_MODE、DELETE\_MODE、RENAME\_MODE，其中CREATE\_MODE、DELETE\_MODE、RENAME\_MODE仅支持临时授权；如需授予多个权限，可以组合使用，例如使用READ\_MODE | WRITE\_MODE授予读写权限。 |

## PathPolicyInfo15+

需要查询的文件或目录的信息。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| path | string | 否 | 否 | 需要查询的文件或目录路径。 |
| operationMode | OperationMode | 否 | 否 | 需要查询的文件或目录访问模式，参考[OperationMode](js-apis-fileshare.md#operationmode11)。可取READ\_MODE、WRITE\_MODE、CREATE\_MODE、DELETE\_MODE、RENAME\_MODE；如需查询多个权限，可以组合使用，例如使用READ\_MODE | WRITE\_MODE查询读写权限。 |

## PolicyType15+

枚举，所查询策略信息对应的授权模式。临时授权用于短期访问场景，持久化授权用于需要长期访问文件或目录的场景。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TEMPORARY\_TYPE | 0 | 临时授权。 |
| PERSISTENT\_TYPE | 1 | 持久化授权。 |

## fileShare.persistPermission11+

persistPermission(policies: Array<PolicyInfo>): Promise<void>

异步方法，用于对所选择的多个文件或目录URI进行持久化授权，使用Promise异步回调。持久化授权用于将已获取的临时权限保存为长期授权。该接口仅对具有该系统能力的设备开放，此接口不支持远端URI的持久化。

**说明** 

从API version 22开始，支持媒体类URI的持久化。

可以组合授予多个权限。只能对已获取到的临时权限进行持久化授权，否则会报错。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policies | Array<[PolicyInfo](js-apis-fileshare.md#policyinfo11)> | 是 | 需要持久化授权的URI策略信息数组，policies数组大小上限为500。仅支持对已获取的临时权限进行持久化授权，不支持远端URI。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)和[通用错误码](errorcode-universal.md)。

如果存在URI授权失败，则抛出13900001错误码，且失败URI信息将抛出异常data属性中以Array<[PolicyErrorResult](js-apis-fileshare.md#policyerrorresult11)>形式提供错误信息。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900001 | Operation not permitted. |
| 13900042 | Out of memory. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';

async function persistPermissionExample() {
  try {
    let documentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker();
    let uris = await documentPicker.select(documentSelectOptions);
    if (uris.length === 0) {
      console.error('No file selected');
      return;
    }
    let policyInfo: fileShare.PolicyInfo = {
      uri: uris[0],
      // 可以组合授予多个权限，例如读写权限可使用 fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE
      operationMode: fileShare.OperationMode.READ_MODE
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];
    fileShare.persistPermission(policies).then(() => {
      console.info('persistPermission successfully');
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error(`persistPermission failed with error message: ${err.message}, error code: ${err.code}`);
      if (err.code === 13900001 && err.data) {
        for (let i = 0; i < err.data.length; i++) {
          console.error(`error code: ${JSON.stringify(err.data[i].code)}`);
          console.error(`error URI: ${JSON.stringify(err.data[i].uri)}`);
          console.error(`error reason: ${JSON.stringify(err.data[i].message)}`);
        }
      }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`persistPermission failed with err: ${JSON.stringify(err)}`);
  }
}
```

## fileShare.revokePermission11+

revokePermission(policies: Array<PolicyInfo>): Promise<void>

异步方法，用于对所选择的多个文件或目录URI取消持久化授权，使用Promise异步回调。取消持久化授权后，需要重新获取临时权限才能再次持久化授权。该接口仅对具有该系统能力的设备开放，此接口不支持远端URI的持久化。

**说明** 

从API version 22开始，支持媒体类URI的持久化。

可以组合取消多个权限。只能对已持久化的权限进行取消持久化，否则会报错。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policies | Array<[PolicyInfo](js-apis-fileshare.md#policyinfo11)> | 是 | 需要取消持久化授权的URI策略信息数组，policies数组大小上限为500。仅支持对已持久化的权限进行取消持久化授权，不支持远端URI。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)和[通用错误码](errorcode-universal.md)。

如果存在URI取消授权失败，则抛出13900001错误码，且失败URI信息将抛出异常data属性中以Array<[PolicyErrorResult](js-apis-fileshare.md#policyerrorresult11)>形式提供错误信息。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900001 | Operation not permitted. |
| 13900042 | Out of memory. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';

async function revokePermissionExample() {
  try {
    let documentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker();
    let uris = await documentPicker.select(documentSelectOptions);
    if (uris.length === 0) {
      console.error('No file selected');
      return;
    }
    let policyInfo: fileShare.PolicyInfo = {
      uri: uris[0],
      // 可以组合取消多个权限，例如读写权限可使用 fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE
      operationMode: fileShare.OperationMode.READ_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];
    fileShare.revokePermission(policies).then(() => {
      console.info('revokePermission successfully');
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error(`revokePermission failed with error message: ${err.message}, error code: ${err.code}`);
      if (err.code === 13900001 && err.data) {
        for (let i = 0; i < err.data.length; i++) {
          console.error(`error code: ${JSON.stringify(err.data[i].code)}`);
          console.error(`error URI: ${JSON.stringify(err.data[i].uri)}`);
          console.error(`error reason: ${JSON.stringify(err.data[i].message)}`);
        }
      }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`revokePermission failed with err: ${JSON.stringify(err)}`);
  }
}
```

## fileShare.activatePermission11+

activatePermission(policies: Array<PolicyInfo>): Promise<void>

异步方法，用于激活多个已持久化授权的文件或目录，使用Promise异步回调。持久化授权是激活的前提，激活后可通过deactivatePermission取消激活。该接口仅对具有该系统能力的设备开放，此接口不支持远端URI的持久化。

**说明** 

从API version 22开始，支持媒体类URI的持久化。

可以组合激活多个权限。需要先调用persistPermission完成持久化授权，才能激活权限，否则会报错。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policies | Array<[PolicyInfo](js-apis-fileshare.md#policyinfo11)> | 是 | 需要激活权限的URI策略信息数组，policies数组大小上限为500。仅支持对已持久化的权限进行激活，不支持远端URI。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)和[通用错误码](errorcode-universal.md)。

如果存在URI激活权限失败，则抛出13900001错误码，且失败URI信息将抛出异常data属性中以Array<[PolicyErrorResult](js-apis-fileshare.md#policyerrorresult11)>形式提供错误信息。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900001 | Operation not permitted. |
| 13900042 | Out of memory. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function activatePermissionExample() {
  try {
    let uri = 'file://docs/storage/Users/username/tmp.txt';
    let policyInfo: fileShare.PolicyInfo = {
      uri: uri,
      // 可以组合激活多个权限，例如读写权限可使用fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE
      operationMode: fileShare.OperationMode.READ_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];
    fileShare.activatePermission(policies).then(() => {
      console.info('activatePermission successfully');
    }).catch(async (err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error(`activatePermission failed with error message: ${err.message}, error code: ${err.code}`);
      if (err.code === 13900001 && err.data) {
        for (let i = 0; i < err.data.length; i++) {
          console.error(`error code: ${JSON.stringify(err.data[i].code)}`);
          console.error(`error URI: ${JSON.stringify(err.data[i].uri)}`);
          console.error(`error reason: ${JSON.stringify(err.data[i].message)}`);
          if (err.data[i].code === fileShare.PolicyErrorCode.PERMISSION_NOT_PERSISTED) {
            await fileShare.persistPermission(policies);
          }
        }
      }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`activatePermission failed with err: ${JSON.stringify(err)}`);
  }
}
```

## fileShare.deactivatePermission11+

deactivatePermission(policies: Array<PolicyInfo>): Promise<void>

异步方法，用于取消激活授权过的多个文件或目录，使用Promise异步回调。取消激活后，持久化授权仍保留，可再次通过activatePermission激活。该接口仅对具有该系统能力的设备开放，此接口不支持远端URI的持久化。

**说明** 

从API version 22开始，支持媒体类URI的持久化。

可以组合取消激活多个权限。只能对已持久化的权限进行取消激活，需要先调用activatePermission激活权限，否则会报错。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policies | Array<[PolicyInfo](js-apis-fileshare.md#policyinfo11)> | 是 | 需要取消激活权限的URI策略信息数组，policies数组大小上限为500。仅支持对已持久化的权限进行取消激活，不支持远端URI。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)和[通用错误码](errorcode-universal.md)。

如果存在URI取消激活权限失败，则抛出13900001错误码，且失败URI信息将抛出异常data属性中以Array<[PolicyErrorResult](js-apis-fileshare.md#policyerrorresult11)>形式提供错误信息。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900001 | Operation not permitted. |
| 13900042 | Out of memory. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function deactivatePermissionExample() {
  try {
    let uri = 'file://docs/storage/Users/username/tmp.txt';
    let policyInfo: fileShare.PolicyInfo = {
      uri: uri,
      // 可以组合取消激活多个权限，例如读写权限可使用fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE
      operationMode: fileShare.OperationMode.READ_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];
    fileShare.deactivatePermission(policies).then(() => {
      console.info('deactivatePermission successfully');
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error(`deactivatePermission failed with error message: ${err.message}, error code: ${err.code}`);
      if (err.code === 13900001 && err.data) {
        for (let i = 0; i < err.data.length; i++) {
          console.error(`error code: ${JSON.stringify(err.data[i].code)}`);
          console.error(`error URI: ${JSON.stringify(err.data[i].uri)}`);
          console.error(`error reason: ${JSON.stringify(err.data[i].message)}`);
        }
      }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`deactivatePermission failed with err: ${JSON.stringify(err)}`);
  }
}
```

## fileShare.checkPersistentPermission12+

checkPersistentPermission(policies: Array<PolicyInfo>): Promise<Array<boolean>>

异步方法，用于校验所选择的多个文件或目录URI的持久化授权，使用Promise异步回调。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policies | Array<[PolicyInfo](js-apis-fileshare.md#policyinfo11)> | 是 | 需要校验持久化授权的URI策略信息数组，policies数组大小上限为500。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<boolean>> | Promise对象，返回持久化授权校验结果数组，数组元素与policies数组元素一一对应。返回true表示有持久化授权；false表示不具有持久化授权。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900042 | Out of memory. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';

async function checkPersistentPermissionExample() {
  try {
    let documentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker();
    let uris = await documentPicker.select(documentSelectOptions);
    if (uris.length === 0) {
      console.error('No file selected');
      return;
    }
    let policyInfo: fileShare.PolicyInfo = {
      uri: uris[0],
      // 可以组合校验多个权限，例如读写权限可使用 fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE
      operationMode: fileShare.OperationMode.READ_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];
    fileShare.checkPersistentPermission(policies).then(async (data) => {
      let result: Array<boolean> = data;
      for (let i = 0; i < result.length; i++) {
        console.info(`checkPersistentPermission result: ${JSON.stringify(result[i])}`);
        if (!result[i]) {
          let info: fileShare.PolicyInfo = {
            uri: policies[i].uri,
            operationMode: policies[i].operationMode,
          };
          let policy: Array<fileShare.PolicyInfo> = [info];
          await fileShare.persistPermission(policy);
        }
      }
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error(`checkPersistentPermission failed with error message: ${err.message}, error code: ${err.code}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`checkPersistentPermission failed with err: ${JSON.stringify(err)}`);
  }
}
```
