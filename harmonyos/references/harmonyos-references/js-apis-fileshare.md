---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fileshare
title: @ohos.fileshare (文件分享)
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > ArkTS API > @ohos.fileshare (文件分享)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0288b170c584dabcf6dcde202fdaed6c458bb21b1f45dad5d902c73cdab2983e
---

该模块提供文件分享能力，提供系统应用将公共目录文件统一资源标识符（Uniform Resource Identifier，URI）以读写权限授权给其他应用的接口，授权后应用可通过[@ohos.file.fs](js-apis-file-fs.md)的相关接口进行相关open、read、write等操作，实现文件分享。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1Tablet

```
1. import { fileShare } from '@kit.CoreFileKit';
```

## OperationMode11+

PhonePC/2in1Tablet

枚举，授予或使能权限的URI访问模式。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 值 | 说明 |
| --- | --- | --- |
| READ\_MODE | 0b1 | 读权限。 |
| WRITE\_MODE | 0b10 | 写权限。 |
| CREATE\_MODE20+ | 0b100 | 创建文件/文件夹权限。 |
| DELETE\_MODE20+ | 0b1000 | 删除文件/文件夹权限。 |
| RENAME\_MODE20+ | 0b10000 | 重命名文件/文件夹权限。 |

## PolicyErrorCode11+

PhonePC/2in1Tablet

枚举，授予或使能权限策略失败的URI对应的错误码。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PERSISTENCE\_FORBIDDEN | 1 | URI禁止被持久化。 |
| INVALID\_MODE | 2 | 无效的模式。 |
| INVALID\_PATH | 3 | 无效的路径。 |
| PERMISSION\_NOT\_PERSISTED12+ | 4 | 权限没有被持久化。 |

## PolicyErrorResult11+

PhonePC/2in1Tablet

授予或使能权限失败的URI策略结果。支持persistPermission、revokePermission、activatePermission、deactivatePermission接口抛出错误时使用。

说明

从API version 23开始，PolicyErrorResult由type变更为interface类型。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 授予或使能权限失败的URI。 |
| code | [PolicyErrorCode](js-apis-fileshare.md#policyerrorcode11) | 否 | 否 | 授权策略失败的URI对应的错误码。 |
| message | string | 否 | 否 | 授权策略失败的URI对应的原因。 |

## PolicyInfo11+

PhonePC/2in1Tablet

需要授予或使能权限URI的策略信息。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 需要授予或使能权限的URI。 |
| operationMode | number | 否 | 否 | 授予或使能权限的URI访问模式，参考[OperationMode](js-apis-fileshare.md#operationmode11)，如需授予多个权限，可以组合使用，例如使用READ\_MODE | WRITE\_MODE授予读写权限。 |

## PathPolicyInfo15+

PhonePC/2in1Tablet

需要查询的文件或目录的信息。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| path | string | 否 | 否 | 需要查询的path。 |
| operationMode | OperationMode | 否 | 否 | 需要查询的path的访问模式，参考[OperationMode](js-apis-fileshare.md#operationmode11)。 |

## PolicyType15+

PhonePC/2in1Tablet

枚举，所查询策略信息对应的授权模式。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TEMPORARY\_TYPE | 0 | 临时授权。 |
| PERSISTENT\_TYPE | 1 | 持久化授权。 |

## fileShare.persistPermission11+

PhonePC/2in1Tablet

persistPermission(policies: Array<PolicyInfo>): Promise<void>

异步方法对所选择的多个文件或目录URI持久化授权，使用Promise异步回调。该接口仅对具有该系统能力的设备开放（此接口不支持远端URI的持久化）。

说明

从API version 22开始，支持媒体类URI的持久化。

可以组合授予多个权限。只能对已获取到的临时权限进行持久化授权，否则会报错。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policies | Array<[PolicyInfo](js-apis-fileshare.md#policyinfo11)> | 是 | 需要授权URI的策略信息，policies数组大小上限为500。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

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

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { picker } from '@kit.CoreFileKit';

4. async function persistPermissionExample() {
5. try {
6. let DocumentSelectOptions = new picker.DocumentSelectOptions();
7. let documentPicker = new picker.DocumentViewPicker();
8. let uris = await documentPicker.select(DocumentSelectOptions);
9. let policyInfo: fileShare.PolicyInfo = {
10. uri: uris[0],
11. // 可以组合授予多个权限，例如读写权限可使用 fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE
12. operationMode: fileShare.OperationMode.READ_MODE
13. };
14. let policies: Array<fileShare.PolicyInfo> = [policyInfo];
15. fileShare.persistPermission(policies).then(() => {
16. console.info("persistPermission successfully");
17. }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
18. console.error("persistPermission failed with error message: " + err.message + ", error code: " + err.code);
19. if (err.code == 13900001 && err.data) {
20. for (let i = 0; i < err.data.length; i++) {
21. console.error("error code : " + JSON.stringify(err.data[i].code));
22. console.error("error uri : " + JSON.stringify(err.data[i].uri));
23. console.error("error reason : " + JSON.stringify(err.data[i].message));
24. }
25. }
26. });
27. } catch (error) {
28. let err: BusinessError = error as BusinessError;
29. console.error('persistPermission failed with err: ' + JSON.stringify(err));
30. }
31. }
```

## fileShare.revokePermission11+

PhonePC/2in1Tablet

revokePermission(policies: Array<PolicyInfo>): Promise<void>

异步方法对所选择的多个文件或目录uri取消持久化授权，使用Promise异步回调。该接口仅对具有该系统能力的设备开放（此接口不支持远端URI的持久化）。

说明

从API version 22开始，支持媒体类URI的持久化。

可以组合取消多个权限。只能对已持久化的权限进行取消持久化，否则会报错。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policies | Array<[PolicyInfo](js-apis-fileshare.md#policyinfo11)> | 是 | 需要授权URI的策略信息，policies数组大小上限为500。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

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

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { picker } from '@kit.CoreFileKit';

4. async function revokePermissionExample() {
5. try {
6. let DocumentSelectOptions = new picker.DocumentSelectOptions();
7. let documentPicker = new picker.DocumentViewPicker();
8. let uris = await documentPicker.select(DocumentSelectOptions);
9. let policyInfo: fileShare.PolicyInfo = {
10. uri: uris[0],
11. // 可以组合取消多个权限，例如读写权限可使用 fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE
12. operationMode: fileShare.OperationMode.READ_MODE,
13. };
14. let policies: Array<fileShare.PolicyInfo> = [policyInfo];
15. fileShare.revokePermission(policies).then(() => {
16. console.info("revokePermission successfully");
17. }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
18. console.error("revokePermission failed with error message: " + err.message + ", error code: " + err.code);
19. if (err.code == 13900001 && err.data) {
20. for (let i = 0; i < err.data.length; i++) {
21. console.error("error code : " + JSON.stringify(err.data[i].code));
22. console.error("error uri : " + JSON.stringify(err.data[i].uri));
23. console.error("error reason : " + JSON.stringify(err.data[i].message));
24. }
25. }
26. });
27. } catch (error) {
28. let err: BusinessError = error as BusinessError;
29. console.error('revokePermission failed with err: ' + JSON.stringify(err));
30. }
31. }
```

## fileShare.activatePermission11+

PhonePC/2in1Tablet

activatePermission(policies: Array<PolicyInfo>): Promise<void>

异步方法使能多个已经永久授权过的文件或目录，使用Promise异步回调。该接口仅对具有该系统能力的设备开放（此接口不支持远端URI的持久化）。

说明

从API version 22开始，支持媒体类URI的持久化。

可以组合使能多个权限。只能对已持久化的权限进行使能，否则会报错。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policies | Array<[PolicyInfo](js-apis-fileshare.md#policyinfo11)> | 是 | 需要授权URI的策略信息，policies数组大小上限为500。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)和[通用错误码](errorcode-universal.md)。

如果存在URI使能权限失败，则抛出13900001错误码，且失败URI信息将抛出异常data属性中以Array<[PolicyErrorResult](js-apis-fileshare.md#policyerrorresult11)>形式提供错误信息。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900001 | Operation not permitted. |
| 13900042 | Out of memory. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function activatePermissionExample() {
4. try {
5. let uri = "file://docs/storage/Users/username/tmp.txt";
6. let policyInfo: fileShare.PolicyInfo = {
7. uri: uri,
8. // 可以组合使能多个权限，例如读写权限可使用 fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE
9. operationMode: fileShare.OperationMode.READ_MODE,
10. };
11. let policies: Array<fileShare.PolicyInfo> = [policyInfo];
12. fileShare.activatePermission(policies).then(() => {
13. console.info("activatePermission successfully");
14. }).catch(async (err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
15. console.error("activatePermission failed with error message: " + err.message + ", error code: " + err.code);
16. if (err.code == 13900001 && err.data) {
17. for (let i = 0; i < err.data.length; i++) {
18. console.error("error code : " + JSON.stringify(err.data[i].code));
19. console.error("error uri : " + JSON.stringify(err.data[i].uri));
20. console.error("error reason : " + JSON.stringify(err.data[i].message));
21. if(err.data[i].code == fileShare.PolicyErrorCode.PERMISSION_NOT_PERSISTED){
22. await fileShare.persistPermission(policies);
23. }
24. }
25. }
26. });
27. } catch (error) {
28. let err: BusinessError = error as BusinessError;
29. console.error('activatePermission failed with err: ' + JSON.stringify(err));
30. }
31. }
```

## fileShare.deactivatePermission11+

PhonePC/2in1Tablet

deactivatePermission(policies: Array<PolicyInfo>): Promise<void>

异步方法取消使能授权过的多个文件或目录，使用Promise异步回调。该接口仅对具有该系统能力的设备开放（此接口不支持远端URI的持久化）。

说明

从API version 22开始，支持媒体类URI的持久化。

可以组合取消使能多个权限。只能对已持久化的权限进行取消使能，否则会报错。

**需要权限：** ohos.permission.FILE\_ACCESS\_PERSIST

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policies | Array<[PolicyInfo](js-apis-fileshare.md#policyinfo11)> | 是 | 需要授权URI的策略信息，policies数组大小上限为500。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)和[通用错误码](errorcode-universal.md)。

如果存在URI取消使能权限失败，则抛出13900001错误码，且失败URI信息将抛出异常data属性中以Array<[PolicyErrorResult](js-apis-fileshare.md#policyerrorresult11)>形式提供错误信息。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900001 | Operation not permitted. |
| 13900042 | Out of memory. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function deactivatePermissionExample() {
4. try {
5. let uri = "file://docs/storage/Users/username/tmp.txt";
6. let policyInfo: fileShare.PolicyInfo = {
7. uri: uri,
8. // 可以组合取消使能多个权限，例如读写权限可使用 fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE
9. operationMode: fileShare.OperationMode.READ_MODE,
10. };
11. let policies: Array<fileShare.PolicyInfo> = [policyInfo];
12. fileShare.deactivatePermission(policies).then(() => {
13. console.info("deactivatePermission successfully");
14. }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
15. console.error("deactivatePermission failed with error message: " + err.message + ", error code: " + err.code);
16. if (err.code == 13900001 && err.data) {
17. for (let i = 0; i < err.data.length; i++) {
18. console.error("error code : " + JSON.stringify(err.data[i].code));
19. console.error("error uri : " + JSON.stringify(err.data[i].uri));
20. console.error("error reason : " + JSON.stringify(err.data[i].message));
21. }
22. }
23. });
24. } catch (error) {
25. let err: BusinessError = error as BusinessError;
26. console.error('deactivatePermission failed with err: ' + JSON.stringify(err));
27. }
28. }
```

## fileShare.checkPersistentPermission12+

PhonePC/2in1Tablet

checkPersistentPermission(policies: Array<PolicyInfo>): Promise<Array<boolean>>

异步方法校验所选择的多个文件或目录URI持久化授权，使用Promise异步回调。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policies | Array<[PolicyInfo](js-apis-fileshare.md#policyinfo11)> | 是 | 需要授权URI的策略信息，policies数组大小上限为500。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<boolean>> | Promise对象。返回true表示有持久化授权；false表示不具有持久化授权。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900042 | Out of memory. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { picker } from '@kit.CoreFileKit';

4. async function checkPersistentPermissionExample() {
5. try {
6. let documentSelectOptions = new picker.DocumentSelectOptions();
7. let documentPicker = new picker.DocumentViewPicker();
8. let uris = await documentPicker.select(documentSelectOptions);
9. let policyInfo: fileShare.PolicyInfo = {
10. uri: uris[0],
11. // 可以组合校验多个权限，例如读写权限可使用 fileShare.OperationMode.READ_MODE | fileShare.OperationMode.WRITE_MODE
12. operationMode: fileShare.OperationMode.READ_MODE,
13. };
14. let policies: Array<fileShare.PolicyInfo> = [policyInfo];
15. fileShare.checkPersistentPermission(policies).then(async (data) => {
16. let result: Array<boolean> = data;
17. for (let i = 0; i < result.length; i++) {
18. console.info("checkPersistentPermission result: " + JSON.stringify(result[i]));
19. if(!result[i]){
20. let info: fileShare.PolicyInfo = {
21. uri: policies[i].uri,
22. operationMode: policies[i].operationMode,
23. };
24. let policy : Array<fileShare.PolicyInfo> = [info];
25. await fileShare.persistPermission(policy);
26. }
27. }
28. }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
29. console.error("checkPersistentPermission failed with error message: " + err.message + ", error code: " + err.code);
30. });
31. } catch (error) {
32. let err: BusinessError = error as BusinessError;
33. console.error('checkPersistentPermission failed with err: ' + JSON.stringify(err));
34. }
35. }
```
