---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-fileguard
title: fileGuard (文件分级管控)
breadcrumb: API参考 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > ArkTS API > fileGuard (文件分级管控)
category: harmonyos-references
scraped_at: 2026-04-29T13:57:51+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:c71ec95b0ea851de9673130ba0303310fc991aab352cc55b316987d693f86fa7
---

文件分级管控服务为企业安全管控类[MDM](../harmonyos-guides/mdm-kit.md)应用提供统一企业关键信息资产（KIA）文件的识别和外发管控能力，保证企业数据安全。功能包括扫描全盘目录下的文档，识别KIA文件，并管控KIA文件通过网络发送到非可信网段。

仅供企业安全管控类MDM应用申请权限后使用。

**起始版本：** 4.0.0(10)

## 导入模块

PC/2in1

```
1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';
```

## CommonDirScanType

PC/2in1

公共目录扫描类型枚举。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MEDIA\_ONLY | 0 | 表示媒体库目录。 |
| MEDIA\_AND\_SANDBOX | 1 | 表示媒体库和沙箱目录。 |

## SecurityLevel

PC/2in1

文件安全等级枚举。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | -1 | 表示文件安全等级不生效。  **起始版本：** 5.1.1(19) |
| EXTERNAL | 0 | 表示文件安全等级为外部公开。 |
| INTERNAL | 1 | 表示文件安全等级为内部公开。 |
| SECRET | 2 | 表示文件安全等级为秘密。 |
| CONFIDENTIAL | 3 | 表示文件安全等级为机密。 |
| TOP\_SECRET | 4 | 表示文件安全等级为绝密。 |

## FilePathInfo

PC/2in1

表示文件路径信息。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| absolutePath | string | 否 | 否 | 表示文件绝对路径。 |
| uri | string | 否 | 否 | 表示文件URI。 |

## FileTagInfo

PC/2in1

表示文件的标签属性信息。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| securityLevel | number | 否 | 否 | 表示文件安全等级，其值参考[SecurityLevel](dataguard-fileguard.md#securitylevel)枚举类型。 |
| tag | string | 否 | 否 | 表示文件标签信息。 |

## ScanFileCallback

PC/2in1

表示扫描结果回调类。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

### onReceiveFileList

PC/2in1

onReceiveFileList(files: Array<string>): void

文件目录扫描结果回调函数。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 表示扫描文件的绝对路径列表。 |

**示例：**

```
1. let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
2. files.forEach((value: string) => {
3. console.info(`Succeeded in getting file: ${value}.`);
4. })
5. };
```

### onTaskCompleted

PC/2in1

onTaskCompleted(count: number): void

文件目录扫描完成信息获取回调函数。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 表示扫描完成后文件的数量。 |

**示例：**

```
1. let onTaskCompleted: (count: number) => void = (count: number) => {
2. console.info(`Succeeded in getting count: ${count}.`);
3. };
```

## FileGuard

PC/2in1

FileGuard类提供了文件分级管控相关接口，包括如下功能：文件目录扫描、标注文件扩展属性、下发文件管控策略等。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

### constructor

PC/2in1

constructor()

创建FileGuard对象。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**示例：**

```
1. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
```

### startFileScanTask

PC/2in1

startFileScanTask(type: CommonDirScanType, callback: ScanFileCallback, batchNum?: number): void

启动公共目录文件扫描任务。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [CommonDirScanType](dataguard-fileguard.md#commondirscantype) | 是 | 公共目录扫描范围。取值：MEDIA\_ONLY | MEDIA\_AND\_SANDBOX。 |
| callback | [ScanFileCallback](dataguard-fileguard.md#scanfilecallback) | 是 | 回调函数，返回的文件列表和扫描结束通知。 |
| batchNum | number | 否 | 每次调用回调函数时返回的文件列表数量。取值在1~200间，如果超出此范围，参数设置无效，按照默认每次调用回调函数返回100个文件，直到扫描结束。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

3. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
4. // 文件目录扫描结果回调函数
5. let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
6. console.info(`Succeeded in getting number of files obtained in each callback: ${files.length}.`);
7. files.forEach((value: string) => {
8. console.info(`Succeeded in getting file: ${value}.`);
9. })
10. };
11. // 文件目录扫描完成信息获取回调函数
12. let onCompleteScanTask: (count: number) => void = (count: number) => {
13. console.info(`Succeeded in getting count: ${count}.`);
14. };
15. // 扫描结果回调
16. let scanFileCallback: fileGuard.ScanFileCallback = {
17. onReceiveFileList: onReceiveFileList,
18. onTaskCompleted: onCompleteScanTask
19. };
20. guard.startFileScanTask(fileGuard.CommonDirScanType.MEDIA_ONLY, scanFileCallback);
```

### startFileScanTask

PC/2in1

startFileScanTask(path: string, callback: ScanFileCallback, batchNum?: number): void

启动指定目录文件扫描任务。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下的目录子集。 |
| callback | [ScanFileCallback](dataguard-fileguard.md#scanfilecallback) | 是 | 回调函数，返回的文件列表和扫描结束通知。 |
| batchNum | number | 否 | 每次调用回调函数时返回的文件列表数量。取值在1~200间，如果超出此范围，参数设置无效，按照默认每次调用回调函数返回100个文件，直到扫描结束。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

3. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
4. let path: string = '/data/service/el2/test';
5. // 文件目录扫描结果回调函数
6. let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
7. console.info(`Succeeded in getting number of files obtained in each callback: ${files.length}.`);
8. files.forEach((value: string) => {
9. console.info(`Succeeded in getting file: ${value}.`);
10. })
11. };
12. // 文件目录扫描完成信息获取回调函数
13. let onCompleteScanTask: (count: number) => void = (count: number) => {
14. console.info(`Succeeded in getting count: ${count}.`);
15. };
16. // 扫描结果回调
17. let scanFileCallback: fileGuard.ScanFileCallback = {
18. onReceiveFileList: onReceiveFileList,
19. onTaskCompleted: onCompleteScanTask
20. };
21. guard.startFileScanTask(path, scanFileCallback);
```

### openFile

PC/2in1

openFile(path: string, callback: AsyncCallback<number>): void

打开文件。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下的绝对路径子集。 |
| callback | AsyncCallback<number> | 是 | 回调函数，当打开文件成功，err为undefined，data为获取到的文件描述符，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let path: string = '/data/service/el2/test/test.txt';
6. guard.openFile(path, (err: BusinessError, fd: number) => {
7. if (err) {
8. console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}.`);
9. return;
10. }
11. console.info(`Succeeded in opening file. path: ${path}, fd: ${fd}.`);
12. });
```

### openFile

PC/2in1

openFile(path: string): Promise<number>

打开文件。使用Promise异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下的绝对路径子集。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let path: string = '/data/service/el2/test/test.txt';
6. guard.openFile(path).then((fd: number) => {
7. console.info(`Succeeded in opening file. path: ${path}, fd: ${fd}.`);
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}.`);
10. });
```

### openFileWrite

PC/2in1

openFileWrite(path: string, callback: AsyncCallback<number>): void

只写模式打开文件。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [用户的个人数据目录](../harmonyos-guides/dataguard-introduction.md#访问限制)下的绝对路径子集。 |
| callback | AsyncCallback<number> | 是 | 回调函数，当只写模式打开文件成功，err为undefined，data为获取到的文件描述符，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
6. guard.openFileWrite(path, (err: BusinessError, fd: number) => {
7. if (err) {
8. console.error(`Failed to open file in write-only mode. Code: ${err.code}, message: ${err.message}.`);
9. return;
10. }
11. console.info(`Succeeded in opening file in write-only mode. path: ${path}, fd: ${fd}.`);
12. });
```

### openFileWrite

PC/2in1

openFileWrite(path: string): Promise<number>

只写模式打开文件。使用Promise异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [用户的个人数据目录](../harmonyos-guides/dataguard-introduction.md#访问限制)下的绝对路径子集。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
6. guard.openFileWrite(path).then((fd: number) => {
7. console.info(`Succeeded in opening file in write-only mode. path: ${path}, fd: ${fd}.`);
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to open file in write-only mode. Code: ${err.code}, message: ${err.message}.`);
10. });
```

### setFileTag

PC/2in1

setFileTag(path: string, level: SecurityLevel, tag: string, callback: AsyncCallback<void>): void

设置文件属性标签。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下的绝对路径子集。 |
| level | [SecurityLevel](dataguard-fileguard.md#securitylevel) | 是 | 用于标识文件安全等级（外部公开、内部公开、秘密、机密、绝密），需由开发者设定，并配合[queryFileTag](dataguard-fileguard.md#queryfiletag)接口使用。 |
| tag | string | 是 | 标签名称，使用[updatePolicy](dataguard-fileguard.md#updatepolicy)接口设置自定义标签策略后，根据标签名称进行相应管控。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步设置文件属性标签成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let path: string = '/data/service/el2/test/test.txt';
6. let tag: string = 'test';
7. guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag, (err: BusinessError) => {
8. if (err) {
9. console.error(`Failed to set file tag. Code: ${err.code}, message: ${err.message}.`);
10. return;
11. }
12. console.info(`Succeeded in setting file tag.`);
13. });
```

### setFileTag

PC/2in1

setFileTag(path: string, level: SecurityLevel, tag: string): Promise<void>

设置文件属性标签。使用Promise异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下的绝对路径子集。 |
| level | [SecurityLevel](dataguard-fileguard.md#securitylevel) | 是 | 用于标识文件安全等级（外部公开、内部公开、秘密、机密、绝密），需由开发者设定，并配合[queryFileTag](dataguard-fileguard.md#queryfiletag)接口使用。 |
| tag | string | 是 | 标签名称，使用[updatePolicy](dataguard-fileguard.md#updatepolicy)接口设置自定义标签策略后，根据标签名称进行相应管控。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let path: string = '/data/service/el2/test/test.txt';
6. let tag: string = 'test';
7. guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag).then(() => {
8. console.info(`Succeeded in setting file tag.`);
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to set file tag. Code: ${err.code}, message: ${err.message}.`);
11. });
```

### queryFileTag

PC/2in1

queryFileTag(path: string, callback: AsyncCallback<FileTagInfo>): void

获取文件属性标签。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下的绝对路径子集。 |
| callback | AsyncCallback<[FileTagInfo](dataguard-fileguard.md#filetaginfo)> | 是 | 回调函数，返回文件标签信息对象。  回调函数，当异步获取文件属性标签成功，err为undefined，data为获取到的[FileTagInfo](dataguard-fileguard.md#filetaginfo)，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let path: string = '/data/service/el2/test/test.txt';
6. guard.queryFileTag(path, (err: BusinessError, data: fileGuard.FileTagInfo) => {
7. if (err) {
8. console.error(`Failed to query file tag. Code: ${err.code}, message: ${err.message}.`);
9. return;
10. }
11. console.info(`Succeeded in querying file tag. securityLevel: ${data.securityLevel}, tag: ${data.tag}.`);
12. });
```

### queryFileTag

PC/2in1

queryFileTag(path: string): Promise<FileTagInfo>

获取文件属性标签。使用Promise异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下的绝对路径子集。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FileTagInfo](dataguard-fileguard.md#filetaginfo)> | Promise对象，返回文件标签信息对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let path: string = '/data/service/el2/test/test.txt';
6. guard.queryFileTag(path).then((data: fileGuard.FileTagInfo) => {
7. console.info(`Succeeded in querying file tag. securityLevel: ${data.securityLevel}, tag: ${data.tag}.`);
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to query file tag. Code: ${err.code}, message: ${err.message}.`);
10. });
```

### getFileUri

PC/2in1

getFileUri(path: string, callback: AsyncCallback<FilePathInfo>): void

获取文件URI。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [用户的个人数据目录](../harmonyos-guides/dataguard-introduction.md#访问限制)下的绝对路径子集。 |
| callback | AsyncCallback<[FilePathInfo](dataguard-fileguard.md#filepathinfo)> | 是 | 回调函数。当获取文件URI成功，err为undefined，data为获取到的[FilePathInfo](dataguard-fileguard.md#filepathinfo)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/test/test.txt';
6. guard.getFileUri(path, (err: BusinessError, data: fileGuard.FilePathInfo) => {
7. if (err) {
8. console.error(`Failed to get file uri. Code: ${err.code}, message: ${err.message}.`);
9. }else{
10. console.info(`Succeeded in getting file uri.`);
11. }
12. });
```

### getFileUri

PC/2in1

getFileUri(path: string): Promise<FilePathInfo>

获取文件URI。使用Promise异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [用户的个人数据目录](../harmonyos-guides/dataguard-introduction.md#访问限制)下的绝对路径子集。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FilePathInfo](dataguard-fileguard.md#filepathinfo)> | Promise对象，返回文件绝对路径和URI。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/test/test.txt';
6. guard.getFileUri(path).then((data: fileGuard.FilePathInfo) => {
7. console.info(`Succeeded in getting file uri.`);
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to get file uri. Code: ${err.code}, message: ${err.message}.`);
10. });
```

### deleteFile

PC/2in1

deleteFile(path: string, callback: AsyncCallback<void>): void

删除指定路径下的文件。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [用户的个人数据目录](../harmonyos-guides/dataguard-introduction.md#访问限制)下的绝对路径子集。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步删除文件成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
6. guard.deleteFile(path, (err: BusinessError) => {
7. if (err) {
8. console.error(`Failed to delete file. Code: ${err.code}, message: ${err.message}.`);
9. }else{
10. console.info(`Succeeded in deleting file.`);
11. }
12. });
```

### deleteFile

PC/2in1

deleteFile(path: string): Promise<void>

删除指定路径下的文件。使用Promise异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [用户的个人数据目录](../harmonyos-guides/dataguard-introduction.md#访问限制)下的绝对路径子集。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
6. guard.deleteFile(path).then(() => {
7. console.info(`Succeeded in deleting file.`);
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to delete file. Code: ${err.code}, message: ${err.message}.`);
10. });
```

### updatePolicy

PC/2in1

updatePolicy(policy: string, callback: AsyncCallback<void>): void

更新安全管控策略。使用callback异步回调。

**需要权限：** ohos.permission.SET\_FILE\_GUARD\_POLICY

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policy | string | 是 | 安全管控策略：网络策略、文件策略、蓝牙策略、星闪策略、多用户策略、可信任应用列表和五种自定义标签。  - **网络策略**  - default\_policy：网段管控默认策略。判断在默认网段范围范围内，但不处于可信任网段和不可信任网段范围内的ip是否需要被管控，0表示不管控，1表示管控，默认为0。  - net\_intercept\_toggle：KIA网络拦截使能开关。0表示关闭，设置为0时，KIA网络拦截不生效；1表示开启（默认为1），设置为1时，开启拦截，具体拦截规则如下：  -当default\_policy设置为0（不管控）时，系统会拦截通过网络向外发送至默认网段范围外或不可信网段的KIA文件。  -当default\_policy设置为1（管控）时，系统仅允许文件发往明确配置的可信任网段，以下所有情况均会被拦截：发往默认网段范围外的地址，发往不可信任网段地址，以及发往默认网段内但既未列入可信任网段也未列入不可信网段的地址。  - net\_reject\_cache\_time：网络外发拦截管控时间。当成功触发网络外发拦截后，在该管控时间范围内，相关进程通过网络进行的任何文件外发操作都会被拦截。正整数，默认为30，单位：s。  - boundary：默认网段范围。限定默认管控的网段范围，向不在此范围内的ip地址外发文件默认会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.0.0.0-10.255.255.255"。  - netsegment\_trustlist：可信任网段。限定可信任的网段范围，外发至该网段内的文件不会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.0.0.0-10.255.255.255"。  - netsegment\_blocklist：不可信网段。限定不可信任的网段范围，外发至该网段内的文件会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.0.0.0-10.255.255.255"。  - netsegment\_update\_type：网段更新方式。0表示下发策略中的网段信息将覆盖原有策略中的网段信息；1表示在原有网段信息的基础下追加新下发策略中的网段信息，默认为0。  - **文件策略**  - usb\_intercept\_toggle：U盘拦截管控开关。当KIA文件外发到U盘时，设置为0表示关闭拦截（不启用管控），设置为1表示开启拦截，默认为0。  - smb\_client\_intercept\_toggle：Samba客户端拦截管控开关。当通过网络邻居外发KIA文件时，0表示关闭拦截（不启用管控），1表示开启拦截，默认为1。从6.0.1(21)版本开始支持此管控策略。  - smb\_server\_intercept\_toggle：Samba服务端拦截管控开关。当通过网络邻居访问KIA文件时，0表示关闭拦截（不启用管控），1表示开启，拦截，默认为1。从6.0.1(21)版本开始支持此管控策略。  - new\_file\_audit\_toggle：新建文件审计开关。开启后，会向审计框架上报文件新建的审计事件，0表示关闭，1表示开启，默认为0。起始版本：从5.1.1(19)版本开始支持此管控策略。  - kia\_variant\_toggle：KIA变种开关。开启后，系统将监控KIA变种事件，并支持通过注册回调的方式监听并处理相关变种事件，0表示关闭，1表示开启，默认为1。从5.0.3(15)版本开始支持此管控策略。  - audit\_filter\_toggle：KIA文件创建事件及变种事件的过滤开关。0表示关闭，关闭后，会记录所有进程行为下的KIA文件创建事件及变种事件；1表示开启，开启后，仅记录应用行为下的KIA文件创建事件及变种事件，默认为0。从5.0.3(15)版本开始支持此管控策略。  - **蓝牙策略**  从6.0.1(21)版本开始支持此管控策略。  - bluetooth\_intercept\_toggle：蓝牙拦截管控开关。设置后，通过蓝牙外发KIA文件会被拦截。字符串列表，可填入"bt\_socket","bt\_ble","bt\_opp"三种蓝牙协议名称，默认为空。  - bluetooth\_intercept\_time：蓝牙外发拦截管控时间。当成功触发蓝牙外发拦截后，在该管控时间范围内，通过蓝牙进行的任何文件外发操作都会被拦截。正整数，默认为15，单位：s。  - **星闪策略**  从6.0.1(21)版本开始支持此管控策略。  - nearlink\_intercept\_toggle：星闪拦截管控开关。设置后，通过相关星闪协议外发KIA文件会被拦截。字符串列表，可填入"nearlink\_ssap","nearlink\_dataTransfer"两种星闪协议名称，默认为空。  - nearlink\_intercept\_time：星闪外发拦截管控时间。当成功触发星闪外发拦截后，在该管控时间范围内，通过星闪进行的任何文件外发操作都会被拦截。正整数，默认为15，单位：s。  - **多用户策略**  从5.1.1(19)版本开始支持此管控策略。  - user\_id：用户ID。设置用户ID后，本次下发的管控策略范围将仅适用于该user\_id对应的用户；若未指定user\_id，则采用默认的管控策略。在使用过程中，系统会优先采用用户的专属策略，若无法匹配，则自动采用默认策略。  - **可信任应用列表**  从5.0.3(15)版本开始支持此管控策略。  - trust\_app\_list：可信任应用列表，在可信任应用列表中的应用才可读取KIA文件。字符串列表，元素为[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)，默认为空。  - **五种自定义标签**  从5.1.1(19)版本开始支持此管控策略。最多支持五种自定义标签管控策略，该策略会自动识别文件扩展属性中包含指定"tag"内容的文件，并对这些文件进行相应管控。  - "tag": 标签名称，用于在[setFileTag](dataguard-fileguard.md#setfiletag)、[setFileCustomTag](dataguard-fileguard.md#setfilecustomtag)和[unsetFileCustomTag](dataguard-fileguard.md#unsetfilecustomtag)中管控对应标签的文件，默认为空。  - "usb\_intercept\_toggle"：U盘拦截管控开关，默认为0。  - "net\_intercept\_toggle"：网络拦截管控开关，默认为0。  - "boundary"：默认网段范围。  - "netsegment\_trustlist"：可信任网段。  - "netsegment\_blocklist"：不可信网段。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步更新安全管控策略成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { BusinessError, osAccount } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. async function updatePolicy() {
5. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
6. let userId: number = await accountManager.getOsAccountLocalId();

8. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
9. let policy: string = '{' +
10. '"net_intercept_toggle":1,' +
11. '"default_policy":1,' +
12. '"net_reject_cache_time":30,' +
13. '"boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
14. '"netsegment_trustlist":["10.0.0.0-10.255.255.255","192.168.0.0-192.168.255.255"],' +
15. '"netsegment_blocklist":["172.16.0.0-172.31.255.255"],' +
16. '"netsegment_update_type": 0,' +
17. '"usb_intercept_toggle":1,' +
18. '"smb_client_intercept_toggle":1,' +
19. '"smb_server_intercept_toggle":1,' +
20. '"new_file_audit_toggle":1,' +
21. '"kia_variant_toggle":1,' +
22. '"audit_filter_toggle":1,' +
23. '"bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
24. '"bluetooth_intercept_time":30,' +
25. '"nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
26. '"nearlink_intercept_time":30,' +
27. `"user_id": ${userId},` +
28. '"trust_app_list":["ohos.app.hap.myapplication_BPch04bPYBrkJX8RAsmiGDbHFaG+BYvhkg4TK4fHQzJOL4VnoBCZU3boBBXGVEB+M/j0X2nnd7KVeyWuEORVxI2g="],' +
29. '"Tag1":{' +
30. '   "tag":"sensitive",' +
31. '   "usb_intercept_toggle":1,' +
32. '   "net_intercept_toggle":1,' +
33. '   "boundary":["10.0.0.0-10.255.255.255"],' +
34. '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
35. '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
36. '  },' +
37. '"Tag2":{' +
38. '   "tag":"confidential",' +
39. '   "usb_intercept_toggle":1,' +
40. '   "net_intercept_toggle":1,' +
41. '   "boundary":["10.0.0.0-10.255.255.255"],' +
42. '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
43. '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
44. '  },' +
45. '"Tag3":{' +
46. '   "tag":"public",' +
47. '   "usb_intercept_toggle":0,' +
48. '   "net_intercept_toggle":0,' +
49. '   "boundary":["10.0.0.0-10.255.255.255"],' +
50. '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
51. '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
52. '  },' +
53. '"Tag4":{' +
54. '   "tag":"general",' +
55. '   "usb_intercept_toggle":1,' +
56. '   "net_intercept_toggle":0,' +
57. '   "boundary":["10.0.0.0-10.255.255.255"],' +
58. '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
59. '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
60. '  },' +
61. '"Tag5":{' +
62. '   "tag":"special",' +
63. '   "usb_intercept_toggle":1,' +
64. '   "net_intercept_toggle":1,' +
65. '   "boundary":["10.0.0.0-10.255.255.255"],' +
66. '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
67. '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
68. '  }' +
69. '}';
70. guard.updatePolicy(policy, (err: BusinessError) => {
71. if (err) {
72. console.error(`Failed to update policy. Code: ${err.code}, message: ${err.message}.`);
73. } else {
74. console.info(`Succeeded in updating policy.`);
75. }
76. });
77. }
```

### updatePolicy

PC/2in1

updatePolicy(policy: string): Promise<void>

更新安全管控策略。使用Promise异步回调。

**需要权限：** ohos.permission.SET\_FILE\_GUARD\_POLICY

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policy | string | 是 | 安全管控策略：网络策略、文件策略、蓝牙策略、星闪策略、多用户策略、可信任应用列表和五种自定义标签。  - **网络策略**  - default\_policy：网段管控默认策略。判断在默认网段范围范围内，但不处于可信任网段和不可信任网段范围内的ip是否需要被管控，0表示不管控，1表示管控，默认为0。  - net\_intercept\_toggle：KIA网络拦截使能开关。0表示关闭，设置为0时，KIA网络拦截不生效；1表示开启（默认为1），设置为1时，开启拦截，具体拦截规则如下：  -当default\_policy设置为0（不管控）时，系统会拦截通过网络向外发送至默认网段范围外或不可信网段的KIA文件。  -当default\_policy设置为1（管控）时，系统仅允许文件发往明确配置的可信任网段，以下所有情况均会被拦截：发往默认网段范围外的地址，发往不可信任网段地址，以及发往默认网段内但既未列入可信任网段也未列入不可信网段的地址。  - net\_reject\_cache\_time：网络外发拦截管控时间。当成功触发网络外发拦截后，在该管控时间范围内，相关进程通过网络进行的任何文件外发操作都会被拦截。正整数，默认为30，单位：s。  - boundary：默认网段范围。限定默认管控的网段范围，向不在此范围内的ip地址外发文件默认会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.0.0.0-10.255.255.255"。  - netsegment\_trustlist：可信任网段。限定可信任的网段范围，外发至该网段内的文件不会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.0.0.0-10.255.255.255"。  - netsegment\_blocklist：不可信网段。限定不可信任的网段范围，外发至该网段内的文件会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.0.0.0-10.255.255.255"。  - netsegment\_update\_type：网段更新方式。0表示下发策略中的网段信息将覆盖原有策略中的网段信息；1表示在原有网段信息的基础下追加新下发策略中的网段信息，默认为0。  - **文件策略**  - usb\_intercept\_toggle：U盘拦截管控开关。当KIA文件外发到U盘时，设置为0表示关闭拦截（不启用管控），设置为1表示开启拦截，默认为0。  - smb\_client\_intercept\_toggle：Samba客户端拦截管控开关。当通过网络邻居外发KIA文件时，0表示关闭拦截（不启用管控），1表示开启拦截，默认为1。从6.0.1(21)版本开始支持此管控策略。  - smb\_server\_intercept\_toggle：Samba服务端拦截管控开关。当通过网络邻居访问KIA文件时，0表示关闭拦截（不启用管控），1表示开启，拦截，默认为1。从6.0.1(21)版本开始支持此管控策略。  - new\_file\_audit\_toggle：新建文件审计开关。开启后，会向审计框架上报文件新建的审计事件，0表示关闭，1表示开启，默认为0。起始版本：从5.1.1(19)版本开始支持此管控策略。  - kia\_variant\_toggle：KIA变种开关。开启后，系统将监控KIA变种事件，并支持通过注册回调的方式监听并处理相关变种事件，0表示关闭，1表示开启，默认为1。从5.0.3(15)版本开始支持此管控策略。  - audit\_filter\_toggle：KIA文件创建事件及变种事件的过滤开关。0表示关闭，关闭后，会记录所有进程行为下的KIA文件创建事件及变种事件；1表示开启，开启后，仅记录应用行为下的KIA文件创建事件及变种事件，默认为0。从5.0.3(15)版本开始支持此管控策略。  - **蓝牙策略**  从6.0.1(21)版本开始支持此管控策略。  - bluetooth\_intercept\_toggle：蓝牙拦截管控开关。设置后，通过蓝牙外发KIA文件会被拦截。字符串列表，可填入"bt\_socket","bt\_ble","bt\_opp"三种蓝牙协议名称，默认为空。  - bluetooth\_intercept\_time：蓝牙外发拦截管控时间。当成功触发蓝牙外发拦截后，在该管控时间范围内，通过蓝牙进行的任何文件外发操作都会被拦截。正整数，默认为15，单位：s。  - **星闪策略**  从6.0.1(21)版本开始支持此管控策略。  - nearlink\_intercept\_toggle：星闪拦截管控开关。设置后，通过相关星闪协议外发KIA文件会被拦截。字符串列表，可填入"nearlink\_ssap","nearlink\_dataTransfer"两种星闪协议名称，默认为空。  - nearlink\_intercept\_time：星闪外发拦截管控时间。当成功触发星闪外发拦截后，在该管控时间范围内，通过星闪进行的任何文件外发操作都会被拦截。正整数，默认为15，单位：s。  - **多用户策略**  从5.1.1(19)版本开始支持此管控策略。  - user\_id：用户ID。设置用户ID后，本次下发的管控策略范围将仅适用于该user\_id对应的用户；若未指定user\_id，则采用默认的管控策略。在使用过程中，系统会优先采用用户的专属策略，若无法匹配，则自动采用默认策略。  - **可信任应用列表**  从5.0.3(15)版本开始支持此管控策略。  - trust\_app\_list：可信任应用列表，在可信任应用列表中的应用才可读取KIA文件。字符串列表，元素为[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)，默认为空。  - **五种自定义标签**  从5.1.1(19)版本开始支持此管控策略。最多支持五种自定义标签管控策略，该策略会自动识别文件扩展属性中包含指定"tag"内容的文件，并对这些文件进行相应管控。  - "tag": 标签名称，用于在[setFileTag](dataguard-fileguard.md#setfiletag)、[setFileCustomTag](dataguard-fileguard.md#setfilecustomtag)和[unsetFileCustomTag](dataguard-fileguard.md#unsetfilecustomtag)中管控对应标签的文件，默认为空。  - "usb\_intercept\_toggle"：U盘拦截管控开关，默认为0。  - "net\_intercept\_toggle"：网络拦截管控开关，默认为0。  - "boundary"：默认网段范围。  - "netsegment\_trustlist"：可信任网段。  - "netsegment\_blocklist"：不可信网段。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { BusinessError, osAccount } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. async function updatePolicy() {
5. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
6. let userId: number = await accountManager.getOsAccountLocalId();

8. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
9. let policy: string = '{' +
10. '"net_intercept_toggle":1,' +
11. '"default_policy":1,' +
12. '"net_reject_cache_time":30,' +
13. '"boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
14. '"netsegment_trustlist":["10.0.0.0-10.255.255.255","192.168.0.0-192.168.255.255"],' +
15. '"netsegment_blocklist":["172.16.0.0-172.31.255.255"],' +
16. '"netsegment_update_type": 0,' +
17. '"usb_intercept_toggle":1,' +
18. '"smb_client_intercept_toggle":1,' +
19. '"smb_server_intercept_toggle":1,' +
20. '"new_file_audit_toggle":1,' +
21. '"kia_variant_toggle":1,' +
22. '"audit_filter_toggle":1,' +
23. '"bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
24. '"bluetooth_intercept_time":30,' +
25. '"nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
26. '"nearlink_intercept_time":30,' +
27. `"user_id": ${userId},` +
28. '"trust_app_list":["ohos.app.hap.myapplication_BPch04bPYBrkJX8RAsmiGDbHFaG+BYvhkg4TK4fHQzJOL4VnoBCZU3boBBXGVEB+M/j0X2nnd7KVeyWuEORVxI2g="],' +
29. '"Tag1":{' +
30. '   "tag":"sensitive",' +
31. '   "usb_intercept_toggle":1,' +
32. '   "net_intercept_toggle":1,' +
33. '   "boundary":["10.0.0.0-10.255.255.255"],' +
34. '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
35. '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
36. '  },' +
37. '"Tag2":{' +
38. '   "tag":"confidential",' +
39. '   "usb_intercept_toggle":1,' +
40. '   "net_intercept_toggle":1,' +
41. '   "boundary":["10.0.0.0-10.255.255.255"],' +
42. '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
43. '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
44. '  },' +
45. '"Tag3":{' +
46. '   "tag":"public",' +
47. '   "usb_intercept_toggle":0,' +
48. '   "net_intercept_toggle":0,' +
49. '   "boundary":["10.0.0.0-10.255.255.255"],' +
50. '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
51. '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
52. '  },' +
53. '"Tag4":{' +
54. '   "tag":"general",' +
55. '   "usb_intercept_toggle":1,' +
56. '   "net_intercept_toggle":0,' +
57. '   "boundary":["10.0.0.0-10.255.255.255"],' +
58. '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
59. '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
60. '  },' +
61. '"Tag5":{' +
62. '   "tag":"special",' +
63. '   "usb_intercept_toggle":1,' +
64. '   "net_intercept_toggle":1,' +
65. '   "boundary":["10.0.0.0-10.255.255.255"],' +
66. '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
67. '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"]' +
68. '  }' +
69. '}';
70. guard.updatePolicy(policy).then(() => {
71. console.info(`Succeeded in updating policy.`);
72. }).catch((err: BusinessError) => {
73. console.error(`Failed to update policy. Code: ${err.code}, message: ${err.message}.`);
74. });
75. }
```

### setKiaFilelist

PC/2in1

setKiaFilelist(filelist: string, callback: AsyncCallback<void>): void

设置KIA文件列表。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filelist | string | 是 | kia\_filelist：[默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下的KIA文件绝对路径列表，相关文件会被标记为KIA文件。  kia\_keyword：受控文件关键字列表，文件名中包含相关关键字的文件会被管控。  kia\_suffix：受控文件后缀名列表，文件名包含相关后缀名的文件会被管控。  compress\_suffix：压缩文件后缀名列表，只有经过压缩后的文件后缀名在该列表范围内，才会上报压缩变种事件。  kia\_update\_type：KIA文件更新类型，当type为0时，新增策略将会替换原有策略；当type为1时，会在原有策略的基础上追加新增策略；当type为2时，会在原有策略的基础上删除新的策略，默认为0。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步设置KIA文件列表成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let fileListStr: string =
6. '{"kia_filelist":["/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/1.txt",' +
7. '"/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/2.txt"],' +
8. '"kia_keyword":["key1","key2","key3"],' +
9. '"kia_suffix":[".java", ".html", ".cpp", ".docx"],' +
10. '"compress_suffix":[".rar", ".zip"],' +
11. '"kia_update_type":0}';
12. guard.setKiaFilelist(fileListStr, (err: BusinessError) => {
13. if (err) {
14. console.error(`Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.`);
15. } else {
16. console.info(`Succeeded in setting the list of KIA file.`);
17. }
18. });
```

### setKiaFilelist

PC/2in1

setKiaFilelist(filelist: string): Promise<void>

设置KIA文件列表。使用Promise异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filelist | string | 是 | kia\_filelist：[默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下的KIA文件绝对路径列表，相关文件会被标记为KIA文件。  kia\_keyword：受控文件关键字列表，文件名中包含相关关键字的文件会被管控。  kia\_suffix：受控文件后缀名列表，文件名包含相关后缀名的文件会被管控。  compress\_suffix：压缩文件后缀名列表，只有经过压缩后的文件后缀名在该列表范围内，才会上报压缩变种事件。  kia\_update\_type：KIA文件更新类型，当type为0时，新增策略将会替换原有策略；当type为1时，会在原有策略的基础上追加新增策略；当type为2时，会在原有策略的基础上删除新的策略，默认为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let fileListStr: string =
6. '{"kia_filelist":["/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/1.txt",' +
7. '"/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/2.txt"],' +
8. '"kia_keyword":["key1","key2","key3"],' +
9. '"kia_suffix":[".java", ".html", ".cpp", ".docx"],' +
10. '"compress_suffix":[".rar", ".zip"],' +
11. '"kia_update_type":0}';
12. guard.setKiaFilelist(fileListStr).then(() => {
13. console.info(`Succeeded in setting the list of KIA file.`);
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.`);
16. });
```

### on('kiaCopy')

PC/2in1

on(type: 'kiaCopy', callback: Callback<string>): void

订阅KIA文件拷贝事件。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaCopy'：固定取值，表示监听KIA文件拷贝事件。 |
| callback | Callback<string> | 是 | 回调函数，返回KIA文件拷贝事件。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

3. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

5. function onKiaCopyCallback(eventData: string) {
6. console.info(`Succeeded in receiving eventData: ${eventData}.`);
7. }

9. try {
10. guard.on('kiaCopy', onKiaCopyCallback);
11. } catch (e) {
12. console.error(`Failed to listen the kia file copy event. Code: ${e.code}, message: ${e.message}.`);
13. }
```

### off('kiaCopy')

PC/2in1

off(type: 'kiaCopy', callback?: Callback<string>): void

取消订阅KIA文件拷贝事件。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaCopy'：固定取值，表示取消监听KIA文件拷贝事件。 |
| callback | Callback<string> | 否 | 回调函数，返回KIA文件拷贝信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

3. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

5. function offKiaCopyCallback(eventData: string) {
6. console.info(`Succeeded in receiving eventData: ${eventData}.`);
7. }

9. try {
10. guard.off('kiaCopy', offKiaCopyCallback);
11. } catch (e) {
12. console.error(`Failed to cancel listen the KIA file copy event. Code: ${e.code}, message: ${e.message}.`);
13. }
```

### on('kiaRename')

PC/2in1

on(type: 'kiaRename', callback: Callback<string>): void

订阅KIA文件重命名事件。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaRename'：固定取值，表示监听KIA文件重命名事件。 |
| callback | Callback<string> | 是 | 回调函数，返回KIA文件重命名事件。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

3. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

5. function onKiaRenameCallback(eventData: string) {
6. console.info(`Succeeded in receiving eventData: ${eventData}.`);
7. }

9. try {
10. guard.on('kiaRename', onKiaRenameCallback);
11. } catch (e) {
12. console.error(`Failed to listen the KIA file rename event. Code: ${e.code}, message: ${e.message}.`);
13. }
```

### off('kiaRename')

PC/2in1

off(type: 'kiaRename', callback?: Callback<string>): void

取消订阅KIA文件重命名事件。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaRename'：固定取值，表示取消监听KIA文件重命名事件。 |
| callback | Callback<string> | 否 | 回调函数，返回KIA文件重命名信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

3. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

5. function offKiaRenameCallback(eventData: string) {
6. console.info(`Succeeded in receiving eventData: ${eventData}.`);
7. }

9. try {
10. guard.off('kiaRename', offKiaRenameCallback);
11. } catch (e) {
12. console.error(`Failed to cancel listen the KIA file rename event. Code: ${e.code}, message: ${e.message}.`);
13. }
```

### on('kiaCompress')

PC/2in1

on(type: 'kiaCompress', callback: Callback<string>): void

订阅KIA文件压缩事件。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaCompress'：固定取值，表示监听KIA文件压缩事件。 |
| callback | Callback<string> | 是 | 回调函数，返回KIA文件压缩事件。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

3. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

5. function onKiaCompressCallback(eventData: string) {
6. console.info(`Succeeded in receiving eventData: ${eventData}.`);
7. }

9. try {
10. guard.on('kiaCompress', onKiaCompressCallback);
11. } catch (e) {
12. console.error(`Failed to listen the KIA file compress event. Code: ${e.code}, message: ${e.message}.`);
13. }
```

### off('kiaCompress')

PC/2in1

off(type: 'kiaCompress', callback?: Callback<string>): void

取消订阅KIA文件压缩事件。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaCompress'：固定取值，表示取消监听KIA文件压缩事件。 |
| callback | Callback<string> | 否 | 回调函数，返回KIA文件压缩信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

3. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

5. function offKiaCompressCallback(eventData: string) {
6. console.info(`Succeeded in receiving eventData: ${eventData}.`);
7. }

9. try {
10. guard.off('kiaCompress', offKiaCompressCallback);
11. } catch (e) {
12. console.error(`Failed to cancel listen the KIA file compress event. Code: ${e.code}, message: ${e.message}.`);
13. }
```

### setKiaWatermarkImage

PC/2in1

setKiaWatermarkImage(image: Uint8Array, info: string): Promise<void>

设置KIA文件水印图片。使用Promise异步回调。

**需要权限：** ohos.permission.SET\_FILE\_GUARD\_POLICY

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | Uint8Array | 是 | 水印图片。当传入的数组为空时，可取消已设置的水印。 |
| info | string | 是 | 水印附加信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |

**示例：**

```
1. import { fileIo } from '@kit.CoreFileKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

5. async function testSetKiaWaterMarkImage() {
6. try {
7. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
8. let imagePath: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/1.png';
9. let fd: number = await guard.openFile(imagePath);
10. let stat: fileIo.Stat = fileIo.statSync(fd);
11. let buffer: ArrayBuffer = new ArrayBuffer(stat.size);
12. fileIo.readSync(fd, buffer);

14. let image: Uint8Array = new Uint8Array(buffer);
15. let info: string = new Date().toLocaleString();
16. guard.setKiaWatermarkImage(image, info).then(() => {
17. console.info(`Succeeded in setting the watermark image for Kia file.`);
18. }).catch((err: BusinessError) => {
19. console.error(`Failed to set the watermark image for Kia file. Code: ${err.code}, message: ${err.message}.`);
20. })
21. } catch (e) {
22. console.error(`testSetKiaWaterMarkImage Exception, Code: ${e.code}, message: ${e.message}`);
23. }
24. }
```

### setFileCustomTag

PC/2in1

setFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void

设置文件自定义属性标签。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下的绝对路径子集。 |
| tagList | Array<string> | 是 | 标签列表，标签数量不超过5个。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步设置文件自定义属性标签成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1001700103 | The path is not exist. |
| 1001700104 | The tag list check failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
6. let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
7. guard.setFileCustomTag(path, tagList, (err: BusinessError) => {
8. if (err) {
9. console.error(`Failed to set file custom tag. Code: ${err.code}, message: ${err.message}.`);
10. } else {
11. console.info(`Succeeded in setting file custom tag.`);
12. }
13. });
```

### setFileCustomTag

PC/2in1

setFileCustomTag(path: string, tagList: Array<string>): Promise<void>

设置文件自定义属性标签。使用Promise异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下的绝对路径子集。 |
| tagList | Array<string> | 是 | 标签列表，标签数量不超过5个。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1001700103 | The path is not exist. |
| 1001700104 | The tag list check failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
6. let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
7. guard.setFileCustomTag(path, tagList).then(() => {
8. console.info(`Succeeded in setting file custom tag.`);
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to set file custom tag. Code: ${err.code}, message: ${err.message}.`);
11. });
```

### unsetFileCustomTag

PC/2in1

unsetFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void

取消文件自定义属性标签。使用callback异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下的绝对路径子集。 |
| tagList | Array<string> | 是 | 标签列表，标签数量不超过5个。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步取消文件自定义属性标签成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1001700103 | The path is not exist. |
| 1001700104 | The tag list check failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
6. let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
7. guard.unsetFileCustomTag(path, tagList, (err: BusinessError) => {
8. if (err) {
9. console.error(`Failed to unset file custom tag. Code: ${err.code}, message: ${err.message}.`);
10. } else {
11. console.info(`Succeeded in unsetting file custom tag.`);
12. }
13. });
```

### unsetFileCustomTag

PC/2in1

unsetFileCustomTag(path: string, tagList: Array<string>): Promise<void>

取消文件自定义标签。使用Promise异步回调。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下的绝对路径子集。 |
| tagList | Array<string> | 是 | 标签列表，标签数量不超过5个。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1001700103 | The path is not exist. |
| 1001700104 | The tag list check failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileGuard } from '@kit.EnterpriseDataGuardKit';

4. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
5. let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
6. let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
7. guard.unsetFileCustomTag(path, tagList).then(() => {
8. console.info(`Succeeded in unsetting file custom tag.`);
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to unset file custom tag. Code: ${err.code}, message: ${err.message}.`);
11. });
```
