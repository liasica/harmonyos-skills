---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs
title: @ohos.file.fs (文件管理)
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > ArkTS API > @ohos.file.fs (文件管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:45+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:7ea28e1742e83d44ce646f11dfd4aa469327d3dcfa829191334818a66dd34bbc
---

该模块为基础文件操作API，提供基础文件操作能力，包括文件基本管理、文件目录管理、文件信息统计、文件流式读写等常用功能。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { fileIo } from '@kit.CoreFileKit';
```

## 使用说明

PhonePC/2in1TabletTVWearable

使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取方式及其接口用法请参考：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage) {
6. let context = this.context;
7. let pathDir = context.filesDir;
8. }
9. }
```

获取沙箱路径的方式及其接口用法也可参考：[应用上下文Context-获取应用文件路径](../harmonyos-guides/application-context-stage.md#获取应用文件路径)。

将指向资源的字符串称为URI。对于只支持沙箱路径作为入参的接口，可以使用构造fileUri对象并获取其沙箱路径的属性的方式将URI转换为沙箱路径，然后使用文件接口。URI定义解及其转换方式请参考：[文件URI](js-apis-file-fileuri.md)。

## fileIo.stat

PhonePC/2in1TabletTVWearable

stat(file: string | number): Promise<Stat>

获取文件或目录详细属性信息，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | number | 是 | 文件或目录的应用沙箱路径path、URI或已打开的文件描述符fd。  **说明**：从API version 22开始，支持传入URI。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Stat](js-apis-file-fs.md#stat)> | Promise对象。返回文件或目录的具体信息。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. fileIo.stat(filePath).then((stat: fileIo.Stat) => {
5. console.info(`Succeeded in getting file info, the size of file is ${stat.size}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to get file info. Code: ${err.code}, message: ${err.message}`);
8. });
```

## fileIo.stat

PhonePC/2in1TabletTVWearable

stat(file: string | number, callback: AsyncCallback<Stat>): void

获取文件或目录的详细属性信息，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | number | 是 | 文件或目录的应用沙箱路径path、URI或已打开的文件描述符fd。  **说明**：从API version 22开始，支持传入URI。 |
| callback | AsyncCallback<[Stat](js-apis-file-fs.md#stat)> | 是 | 异步获取文件或目录的信息之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. fileIo.stat(pathDir, (err: BusinessError, stat: fileIo.Stat) => {
4. if (err) {
5. console.error(`Failed to get file info. Code: ${err.code}, message: ${err.message}`);
6. } else {
7. console.info(`Succeeded in getting file info, the size of file is ${stat.size}`);
8. }
9. });
```

## fileIo.statSync

PhonePC/2in1TabletTVWearable

statSync(file: string | number): Stat

以同步方法获取文件或目录详细属性信息。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | number | 是 | 文件或目录的应用沙箱路径path、URI或已打开的文件描述符fd。  **说明**：从API version 22开始，支持传入URI。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Stat](js-apis-file-fs.md#stat) | 表示文件或目录的具体信息。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let stat = fileIo.statSync(pathDir);
2. console.info(`Succeeded in getting file info, the size of file is ${stat.size}`);
```

## fileIo.access

PhonePC/2in1TabletTVWearable

access(path: string, mode?: AccessModeType): Promise<boolean>

检查文件或目录是否存在，或校验操作权限，使用promise异步回调。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录应用沙箱路径。 |
| mode12+ | [AccessModeType](js-apis-file-fs.md#accessmodetype12) | 否 | 文件或目录校验的权限。不填该参数则默认校验文件是否存在。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回布尔值。返回true，表示文件存在；返回false，表示文件不存在。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. fileIo.access(filePath).then((res: boolean) => {
5. if (res) {
6. console.info(`Succeeded in checking file, file exists.`);
7. } else {
8. console.info(`Succeeded in checking file, file does not exist.`);
9. }
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to access. Code: ${err.code}, message: ${err.message}`);
12. });
```

## fileIo.access12+

PhonePC/2in1TabletTVWearable

access(path: string, mode: AccessModeType, flag: AccessFlagType): Promise<boolean>

检查文件或目录是否在本地，或校验操作权限，使用promise异步回调。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录应用沙箱路径。 |
| mode | [AccessModeType](js-apis-file-fs.md#accessmodetype12) | 是 | 文件或目录校验的权限。 |
| flag | [AccessFlagType](js-apis-file-fs.md#accessflagtype12) | 是 | 文件或目录校验的位置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回布尔值。返回true，表示文件或目录在本地且校验权限存在；返回false，表示文件或目录不存在或者文件或目录在云端或其他分布式设备上。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. fileIo.access(filePath, fileIo.AccessModeType.EXIST, fileIo.AccessFlagType.LOCAL).then((res: boolean) => {
5. if (res) {
6. console.info(`Succeeded in checking file, file exists.`);
7. } else {
8. console.info(`Succeeded in checking file, file does not exist.`);
9. }
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to access. Code: ${err.code}, message: ${err.message}`);
12. });
```

## fileIo.access

PhonePC/2in1TabletTVWearable

access(path: string, callback: AsyncCallback<boolean>): void

检查文件或目录是否存在，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录应用沙箱路径。 |
| callback | AsyncCallback<boolean> | 是 | 异步检查文件或目录是否存在的回调。如果存在，回调返回true；否则返回false。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. fileIo.access(filePath, (err: BusinessError, res: boolean) => {
5. if (err) {
6. console.error(`Failed to access. Code: ${err.code}, message: ${err.message}`);
7. } else {
8. if (res) {
9. console.info(`Succeeded in checking file, file exists.`);
10. } else {
11. console.info(`Succeeded in checking file, file does not exist.`);
12. }
13. }
14. });
```

## fileIo.accessSync

PhonePC/2in1TabletTVWearable

accessSync(path: string, mode?: AccessModeType): boolean

以同步方法检查文件或目录是否存在，或校验操作权限。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录应用沙箱路径。 |
| mode12+ | [AccessModeType](js-apis-file-fs.md#accessmodetype12) | 否 | 文件或目录校验的权限。不填该参数则默认校验文件或目录是否存在。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true，表示文件存在；返回false，表示文件不存在。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. try {
5. let res = fileIo.accessSync(filePath);
6. if (res) {
7. console.info(`Succeeded in checking file, file exists.`);
8. } else {
9. console.info(`Succeeded in checking file, file does not exist.`);
10. }
11. } catch(error) {
12. let err: BusinessError = error as BusinessError;
13. console.error(`Failed to accessSync. Code: ${err.code}, message: ${err.message}`);
14. }
```

## fileIo.accessSync12+

PhonePC/2in1TabletTVWearable

accessSync(path: string, mode: AccessModeType, flag: AccessFlagType): boolean

以同步方法检查文件或目录是否在本地，或校验操作权限。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件应用沙箱路径。 |
| mode | [AccessModeType](js-apis-file-fs.md#accessmodetype12) | 是 | 文件或目录校验的权限。 |
| flag | [AccessFlagType](js-apis-file-fs.md#accessflagtype12) | 是 | 文件或目录校验的位置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true，表示文件在本地且校验权限存在；返回false，表示文件不存在或者文件在云端或其他分布式设备上。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. try {
5. let res = fileIo.accessSync(filePath, fileIo.AccessModeType.EXIST, fileIo.AccessFlagType.LOCAL);
6. if (res) {
7. console.info(`Succeeded in checking file, file exists.`);
8. } else {
9. console.info(`Succeeded in checking file, file does not exist.`);
10. }
11. } catch(error) {
12. let err: BusinessError = error as BusinessError;
13. console.error(`Failed to accessSync. Code: ${err.code}, message: ${err.message}`);
14. }
```

## fileIo.close

PhonePC/2in1TabletTVWearable

close(file: number | File): Promise<void>

关闭文件或目录，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | number | [File](js-apis-file-fs.md#file) | 是 | 已打开的File对象或已打开的文件描述符fd。关闭后file对象或文件描述符fd不再具备实际意义，不可再用于进行读写等操作。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let file = fileIo.openSync(filePath);
5. fileIo.close(file).then(() => {
6. console.info(`Succeeded in closing file.`);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to close file. Code: ${err.code}, message: ${err.message}`);
9. });
```

## fileIo.close

PhonePC/2in1TabletTVWearable

close(file: number | File, callback: AsyncCallback<void>): void

关闭文件或目录，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | number | [File](js-apis-file-fs.md#file) | 是 | 已打开的File对象或已打开的文件描述符fd。关闭后file对象或文件描述符fd不再具备实际意义，不可再用于进行读写等操作。 |
| callback | AsyncCallback<void> | 是 | 异步关闭文件或目录之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let file = fileIo.openSync(filePath);
5. fileIo.close(file, (err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to close file. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info(`Succeeded in closing file.`);
10. }
11. });
```

## fileIo.closeSync

PhonePC/2in1TabletTVWearable

closeSync(file: number | File): void

以同步方法关闭文件或目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | number | [File](js-apis-file-fs.md#file) | 是 | 已打开的File对象或已打开的文件描述符fd。关闭后file对象或文件描述符fd不再具备实际意义，不可再用于进行读写等操作。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let file = fileIo.openSync(filePath);
3. fileIo.closeSync(file);
```

## fileIo.copy11+

PhonePC/2in1TabletTVWearable

copy(srcUri: string, destUri: string, options?: CopyOptions): Promise<void>

拷贝文件或目录，使用promise异步回调。

支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。

跨端拷贝时，最多同时存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcUri | string | 是 | 待复制文件或目录的URI。 |
| destUri | string | 是 | 目标文件或目录的URI。 |
| options | [CopyOptions](js-apis-file-fs.md#copyoptions11) | 否 | options中提供拷贝进度回调。不填该参数则无拷贝进度回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileUri } from '@kit.CoreFileKit';

4. let srcDirPathLocal: string = pathDir + "/src";
5. let dstDirPathLocal: string = pathDir + "/dest";

7. let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
8. let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);

10. let progressListener: fileIo.ProgressListener = (progress: fileIo.Progress) => {
11. console.info(`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
12. };
13. let copyOption: fileIo.CopyOptions = {
14. "progressListener" : progressListener
15. }
16. try {
17. fileIo.copy(srcDirUriLocal, dstDirUriLocal, copyOption).then(()=>{
18. console.info("Succeeded in copying.");
19. }).catch((err: BusinessError)=>{
20. console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
21. })
22. } catch(err) {
23. console.error(`Failed to copy.Code: ${err.code}, message: ${err.message}`);
24. }
```

## fileIo.copy11+

PhonePC/2in1TabletTVWearable

copy(srcUri: string, destUri: string, callback: AsyncCallback<void>): void

拷贝文件或者目录，使用callback异步回调。

支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。

跨端拷贝时，最多同时存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcUri | string | 是 | 待复制文件或目录的URI。 |
| destUri | string | 是 | 目标文件或目录的URI。 |
| callback | AsyncCallback<void> | 是 | 异步拷贝之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileUri } from '@kit.CoreFileKit';

4. let srcDirPathLocal: string = pathDir + "/src";
5. let dstDirPathLocal: string = pathDir + "/dest";

7. let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
8. let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);

10. try {
11. fileIo.copy(srcDirUriLocal, dstDirUriLocal, (err: BusinessError) => {
12. if (err) {
13. console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
14. return;
15. }
16. console.info("Succeeded in copying.");
17. })
18. } catch(err) {
19. console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
20. }
```

## fileIo.copy11+

PhonePC/2in1TabletTVWearable

copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback<void>): void

拷贝文件或者目录，使用callback异步回调。

支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。

跨端拷贝时，最多同时存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcUri | string | 是 | 待复制文件或目录的URI。 |
| destUri | string | 是 | 目标文件或目录的URI。 |
| options | [CopyOptions](js-apis-file-fs.md#copyoptions11) | 是 | 拷贝进度回调。 |
| callback | AsyncCallback<void> | 是 | 异步拷贝之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileUri } from '@kit.CoreFileKit';

4. let srcDirPathLocal: string = pathDir + "/src";
5. let dstDirPathLocal: string = pathDir + "/dest";

7. let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
8. let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);

10. try {
11. let progressListener: fileIo.ProgressListener = (progress: fileIo.Progress) => {
12. console.info(`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
13. };
14. let copyOption: fileIo.CopyOptions = {
15. "progressListener" : progressListener
16. }
17. fileIo.copy(srcDirUriLocal, dstDirUriLocal, copyOption, (err: BusinessError) => {
18. if (err) {
19. console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
20. return;
21. }
22. console.info("Succeeded in copying.");
23. })
24. } catch(err) {
25. console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
26. }
```

## fileIo.copyFile

PhonePC/2in1TabletTVWearable

copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>

复制文件，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | number | 是 | 待复制文件的路径或待复制文件的文件描述符。 |
| dest | string | number | 是 | 目标文件路径或目标文件的文件描述符。 |
| mode | number | 否 | mode提供覆盖文件的选项，当前仅支持0，且默认为0。  0：完全覆盖目标文件，未覆盖部分将被裁切掉。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let srcPath = pathDir + "/srcDir/test.txt";
4. let dstPath = pathDir + "/dstDir/test.txt";
5. fileIo.copyFile(srcPath, dstPath, 0).then(() => {
6. console.info(`Succeeded in copying file.`);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to copy file. Code: ${err.code}, message: ${err.message}`);
9. });
```

## fileIo.copyFile

PhonePC/2in1TabletTVWearable

copyFile(src: string | number, dest: string | number, mode: number, callback: AsyncCallback<void>): void

复制文件，可设置覆盖文件的方式，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | number | 是 | 待复制文件的路径或待复制文件的文件描述符。 |
| dest | string | number | 是 | 目标文件路径或目标文件的文件描述符。 |
| mode | number | 是 | mode提供覆盖文件的选项，当前仅支持0，且默认为0。  0：完全覆盖目标文件，未覆盖部分将被裁切掉。 |
| callback | AsyncCallback<void> | 是 | 异步复制文件之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let srcPath = pathDir + "/srcDir/test.txt";
4. let dstPath = pathDir + "/dstDir/test.txt";
5. fileIo.copyFile(srcPath, dstPath, 0, (err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to copy file. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info(`Succeeded in copying file.`);
10. }
11. });
```

## fileIo.copyFile

PhonePC/2in1TabletTVWearable

copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void

复制文件，覆盖方式为完全覆盖目标文件，未覆盖部分将被裁切。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | number | 是 | 待复制文件的路径或待复制文件的文件描述符。 |
| dest | string | number | 是 | 目标文件路径或目标文件的文件描述符。 |
| callback | AsyncCallback<void> | 是 | 异步复制文件之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let srcPath = pathDir + "/srcDir/test.txt";
4. let dstPath = pathDir + "/dstDir/test.txt";
5. fileIo.copyFile(srcPath, dstPath, (err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to copy file. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info(`Succeeded in copying file.`);
10. }
11. });
```

## fileIo.copyFileSync

PhonePC/2in1TabletTVWearable

copyFileSync(src: string | number, dest: string | number, mode?: number): void

以同步方法复制文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | number | 是 | 待复制文件的路径或待复制文件的文件描述符。 |
| dest | string | number | 是 | 目标文件路径或目标文件的文件描述符。 |
| mode | number | 否 | mode提供覆盖文件的选项，当前仅支持0，且默认为0。  0：完全覆盖目标文件，未覆盖部分将被裁切掉。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let srcPath = pathDir + "/srcDir/test.txt";
2. let dstPath = pathDir + "/dstDir/test.txt";
3. fileIo.copyFileSync(srcPath, dstPath);
```

## fileIo.copyDir10+

PhonePC/2in1TabletTVWearable

copyDir(src: string, dest: string, mode?: number): Promise<void>

复制源目录至目标路径下，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 否 | 复制模式，默认值为0。  - mode为0，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](js-apis-file-fs.md#conflictfiles10)>形式提供。  - mode为1，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // copy directory from srcPath to destPath
4. let srcPath = pathDir + "/srcDir/";
5. let destPath = pathDir + "/destDir/";
6. fileIo.copyDir(srcPath, destPath, 0).then(() => {
7. console.info(`Succeeded in copying directory.`);
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to copy directory. Code: ${err.code}, message: ${err.message}`);
10. });
```

## fileIo.copyDir10+

PhonePC/2in1TabletTVWearable

copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void

复制源目录至目标路径下，可设置复制模式。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 是 | 复制模式，默认值为0。  - mode为0，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](js-apis-file-fs.md#conflictfiles10)>形式提供。  - mode为1，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。 |
| callback | AsyncCallback<void, Array<[ConflictFiles](js-apis-file-fs.md#conflictfiles10)>> | 是 | 异步复制目录之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ConflictFiles } from '@kit.CoreFileKit';

4. // copy directory from srcPath to destPath
5. let srcPath = pathDir + "/srcDir/";
6. let destPath = pathDir + "/destDir/";
7. fileIo.copyDir(srcPath, destPath, 0, (err: BusinessError<Array<ConflictFiles>>) => {
8. if (err && err.code == 13900015 && err.data?.length !== undefined) {
9. for (let i = 0; i < err.data.length; i++) {
10. console.error(`Failed to copy directory, with conflicting files: ${err.data[i].srcFile} ${err.data[i].destFile}`);
11. }
12. } else if (err) {
13. console.error(`Failed to copy directory. Code: ${err.code}, message: ${err.message}`);
14. } else {
15. console.info(`Succeeded in copying directory.`);
16. }
17. });
```

## fileIo.copyDir10+

PhonePC/2in1TabletTVWearable

copyDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void

复制源目录至目标路径下，使用callback异步回调。

如果目标目录下有与源目录名冲突的目录，且冲突目录下有同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](js-apis-file-fs.md#conflictfiles10)>形式提供。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| callback | AsyncCallback<void, Array<[ConflictFiles](js-apis-file-fs.md#conflictfiles10)>> | 是 | 异步复制目录之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ConflictFiles } from '@kit.CoreFileKit';

4. // copy directory from srcPath to destPath
5. let srcPath = pathDir + "/srcDir/";
6. let destPath = pathDir + "/destDir/";
7. fileIo.copyDir(srcPath, destPath, (err: BusinessError<Array<ConflictFiles>>) => {
8. if (err && err.code == 13900015 && err.data?.length !== undefined) {
9. for (let i = 0; i < err.data.length; i++) {
10. console.error(`Failed to copy directory, with conflicting files: ${err.data[i].srcFile} ${err.data[i].destFile}`);
11. }
12. } else if (err) {
13. console.error(`Failed to copy directory. Code: ${err.code}, message: ${err.message}`);
14. } else {
15. console.info(`Succeeded in copying directory.`);
16. }
17. });
```

## fileIo.copyDirSync10+

PhonePC/2in1TabletTVWearable

copyDirSync(src: string, dest: string, mode?: number): void

以同步方法复制源目录至目标路径下。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 否 | 复制模式，默认值为0。  - mode为0，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](js-apis-file-fs.md#conflictfiles10)>形式提供。  - mode为1，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // copy directory from srcPath to destPath
4. let srcPath = pathDir + "/srcDir/";
5. let destPath = pathDir + "/destDir/";
6. try {
7. fileIo.copyDirSync(srcPath, destPath, 0);
8. console.info(`Succeeded in copying directory.`);
9. } catch (error) {
10. let err: BusinessError = error as BusinessError;
11. console.error(`Failed to copy directory. Code: ${err.code}, message: ${err.message}`);
12. }
```

## fileIo.dup10+

PhonePC/2in1TabletTVWearable

dup(fd: number): File

复制文件描述符，并返回对应的File对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [File](js-apis-file-fs.md#file) | 打开的File对象。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let file1 = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
3. let fd: number = file1.fd;
4. let file2 = fileIo.dup(fd);
5. console.info(`Succeeded in getting file name of the file2 is ${file2.name}`);
6. fileIo.closeSync(file1);
7. fileIo.closeSync(file2);
```

## fileIo.connectDfs12+

PhonePC/2in1TabletTVWearable

connectDfs(networkId: string, listeners: DfsListeners): Promise<void>

业务调用connectDfs接口，触发建链。如果对端设备出现异常，业务执行回调DfsListeners内[onStatus](js-apis-file-fs.md#onstatus12)通知应用。可参考[跨设备文件共享和访问](../harmonyos-guides/file-access-across-devices.md)文档进行开发。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | string | 是 | 设备的网络Id。通过[distributedDeviceManager](js-apis-distributeddevicemanager.md)接口调用[DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo)获得。 |
| listeners | [DfsListeners](js-apis-file-fs.md#fileiodfslisteners12) | 是 | 分布式文件系统状态监听器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { distributedDeviceManager } from '@kit.DistributedServiceKit';

4. let dmInstance = distributedDeviceManager.createDeviceManager("com.example.filesync");
5. let deviceInfoList: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
6. if (deviceInfoList && deviceInfoList.length > 0) {
7. console.info(`Succeeded in getting available device list.`);
8. let networkId = deviceInfoList[0].networkId;
9. let listeners: fileIo.DfsListeners = {
10. onStatus(networkId, status) {
11. console.info('onStatus');
12. }
13. };
14. fileIo.connectDfs(networkId, listeners).then(() => {
15. console.info("Succeeded in connecting dfs.");
16. }).catch((err: BusinessError) => {
17. console.error(`Failed to connectDfs. Code: ${err.code}, message: ${err.message}`);
18. });
19. }
```

## fileIo.disconnectDfs12+

PhonePC/2in1TabletTVWearable

disconnectDfs(networkId: string): Promise<void>

业务调用disconnectDfs接口，传入networkId参数，触发断链。可参考[跨设备文件共享和访问](../harmonyos-guides/file-access-across-devices.md)文档进行开发。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | string | 是 | 设备的网络Id。通过[distributedDeviceManager](js-apis-distributeddevicemanager.md)接口调用[DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo)获得。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[空间统计错误码](errorcode-filemanagement.md#空间统计错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { distributedDeviceManager } from '@kit.DistributedServiceKit';

4. let dmInstance = distributedDeviceManager.createDeviceManager("com.example.filesync");
5. let deviceInfoList: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
6. if (deviceInfoList && deviceInfoList.length > 0) {
7. console.info(`Succeeded in getting available device list.`);
8. let networkId = deviceInfoList[0].networkId;
9. fileIo.disconnectDfs(networkId).then(() => {
10. console.info("Succeeded in disconnecting dfs.");
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to disconnect dfs. Code: ${err.code}, message: ${err.message}`);
13. })
14. }
```

## fileIo.setxattr12+

PhonePC/2in1TabletTVWearable

setxattr(path: string, key: string, value: string): Promise<void>

设置文件或目录的扩展属性。使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |
| key | string | 是 | 扩展属性的key。仅支持前缀为“user.”的字符串，且长度需小于256字节。 |
| value | string | 是 | 扩展属性的value。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let attrKey = "user.comment";
5. let attrValue = "Test file.";

7. fileIo.setxattr(filePath, attrKey, attrValue).then(() => {
8. console.info(`Succeeded in setting extended attribute successfully.`);
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to set extended attribute. Code: ${err.code}, message: ${err.message}`);
11. });
```

## fileIo.setxattrSync12+

PhonePC/2in1TabletTVWearable

setxattrSync(path: string, key: string, value: string): void

设置文件或目录的扩展属性。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |
| key | string | 是 | 扩展属性的key。仅支持前缀为“user.”的字符串，且长度需小于256字节。 |
| value | string | 是 | 扩展属性的value。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let attrKey = "user.comment";
5. let attrValue = "Test file.";

7. try {
8. fileIo.setxattrSync(filePath, attrKey, attrValue);
9. console.info(`Succeeded in setting extended attribute successfully.`);
10. } catch (err) {
11. console.error(`Failed to set extended attribute. Code: ${err.code}, message: ${err.message}`);
12. }
```

## fileIo.getxattr12+

PhonePC/2in1TabletTVWearable

getxattr(path: string, key: string): Promise<string>

获取文件或目录的扩展属性。使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |
| key | string | 是 | 扩展属性的key。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回扩展属性的value。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let attrKey = "user.comment";

6. fileIo.getxattr(filePath, attrKey).then((attrValue: string) => {
7. console.info(`Succeeded in getting extended attribute, the value is: ${attrValue}`);
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to get extended attribute. Code: ${err.code}, message: ${err.message}`);
10. });
```

## fileIo.getxattrSync12+

PhonePC/2in1TabletTVWearable

getxattrSync(path: string, key: string): string

使用同步接口获取文件或目录的扩展属性。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |
| key | string | 是 | 扩展属性的key。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回扩展属性的value。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let attrKey = "user.comment";

6. try {
7. let attrValue = fileIo.getxattrSync(filePath, attrKey);
8. console.info(`Succeeded in getting extended attribute, the value is: ${attrValue}`);
9. } catch (err) {
10. console.error(`Failed to get extended attribute. Code: ${err.code}, message: ${err.message}`);
11. }
```

## fileIo.mkdir

PhonePC/2in1TabletTVWearable

mkdir(path: string): Promise<void>

创建目录，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let dirPath = pathDir + "/testDir";
4. fileIo.mkdir(dirPath).then(() => {
5. console.info(`Succeeded in making directory.`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to make directory. Code: ${err.code}, message: ${err.message}`);
8. });
```

## fileIo.mkdir11+

PhonePC/2in1TabletTVWearable

mkdir(path: string, recursion: boolean): Promise<void>

创建目录，使用promise异步回调。当recursion指定为true时，可递归创建目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| recursion | boolean | 是 | 是否递归创建目录。recursion指定为true时，可递归创建目录。recursion指定为false时，仅可创建单层目录。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let dirPath = pathDir + "/testDir1/testDir2/testDir3";
4. fileIo.mkdir(dirPath, true).then(() => {
5. console.info(`Succeeded in making directory.`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to make directory. Code: ${err.code}, message: ${err.message}`);
8. });
```

## fileIo.mkdir

PhonePC/2in1TabletTVWearable

mkdir(path: string, callback: AsyncCallback<void>): void

创建目录，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步创建目录操作完成之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let dirPath = pathDir + "/testDir";
4. fileIo.mkdir(dirPath, (err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to make directory. Code: ${err.code}, message: ${err.message}`);
7. } else {
8. console.info(`Succeeded in making directory.`);
9. }
10. });
```

## fileIo.mkdir11+

PhonePC/2in1TabletTVWearable

mkdir(path: string, recursion: boolean, callback: AsyncCallback<void>): void

创建目录，使用callback异步回调。当recursion指定为true，可递归创建目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| recursion | boolean | 是 | 是否递归创建目录。recursion指定为true时，可递归创建目录。recursion指定为false时，仅可创建单层目录。 |
| callback | AsyncCallback<void> | 是 | 异步创建目录操作完成之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let dirPath = pathDir + "/testDir1/testDir2/testDir3";
4. fileIo.mkdir(dirPath, true, (err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to make directory. Code: ${err.code}, message: ${err.message}`);
7. } else {
8. console.info(`Succeeded in making directory.`);
9. }
10. });
```

## fileIo.mkdirSync

PhonePC/2in1TabletTVWearable

mkdirSync(path: string): void

以同步方法创建目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let dirPath = pathDir + "/testDir";
2. fileIo.mkdirSync(dirPath);
```

## fileIo.mkdirSync11+

PhonePC/2in1TabletTVWearable

mkdirSync(path: string, recursion: boolean): void

以同步方法创建目录。当recursion指定为true，可递归创建目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| recursion | boolean | 是 | 是否递归创建目录。recursion指定为true时，可递归创建目录。recursion指定为false时，仅可创建单层目录。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let dirPath = pathDir + "/testDir1/testDir2/testDir3";
2. fileIo.mkdirSync(dirPath, true);
```

## fileIo.open

PhonePC/2in1TabletTVWearable

open(path: string, mode?: number): Promise<File>

打开文件或目录，使用promise异步回调。支持使用URI打开文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径或文件URI。 |
| mode | number | 否 | 打开文件或目录的[选项](js-apis-file-fs.md#openmode)，必须指定如下选项中的一个，默认以只读方式打开：  - OpenMode.READ\_ONLY(0o0)：只读打开。  - OpenMode.WRITE\_ONLY(0o1)：只写打开。  - OpenMode.READ\_WRITE(0o2)：读写打开。  可以追加以下功能选项，以按位或的方式组合，默认情况下不追加任何额外选项。  - OpenMode.CREATE(0o100)：如果文件不存在，则创建文件。  - OpenMode.TRUNC(0o1000)：如果文件存在且文件具有写权限，则将其长度裁剪为零。  - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到文件末尾。  - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。  - OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。  - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。  - OpenMode.SYNC(0o4010000)：以同步IO方式打开文件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[File](js-apis-file-fs.md#file)> | Promise对象。返回File对象。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. fileIo.open(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE).then((file: fileIo.File) => {
5. console.info(`Succeeded in getting file fd: ${file.fd}`);
6. fileIo.closeSync(file);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}`);
9. });
```

## fileIo.open

PhonePC/2in1TabletTVWearable

open(path: string, mode: number, callback: AsyncCallback<File>): void

打开文件或目录，可设置打开文件的选项。使用callback异步回调。

支持使用URI打开文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径或URI。 |
| mode | number | 是 | 打开文件或目录的[选项](js-apis-file-fs.md#openmode)，必须指定如下选项中的一个，默认以只读方式打开：  - OpenMode.READ\_ONLY(0o0)：只读打开。  - OpenMode.WRITE\_ONLY(0o1)：只写打开。  - OpenMode.READ\_WRITE(0o2)：读写打开。  给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：  - OpenMode.CREATE(0o100)：若文件不存在，则创建文件。  - OpenMode.TRUNC(0o1000)：如果文件存在且文件具有写权限，则将其长度裁剪为零。  - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到文件末尾。  - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。  - OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。  - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。  - OpenMode.SYNC(0o4010000)：以同步IO的方式打开文件。 |
| callback | AsyncCallback<[File](js-apis-file-fs.md#file)> | 是 | 异步打开文件之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. fileIo.open(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE, (err: BusinessError, file: fileIo.File) => {
5. if (err) {
6. console.error(`Failed to open. Code: ${err.code}, message: ${err.message}`);
7. } else {
8. console.info(`Succeeded in getting file fd: ${file.fd}`);
9. fileIo.closeSync(file);
10. }
11. });
```

## fileIo.open

PhonePC/2in1TabletTVWearable

open(path: string, callback: AsyncCallback<File>): void

打开文件或目录，使用callback异步回调。支持使用URI打开文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径或URI。 |
| callback | AsyncCallback<[File](js-apis-file-fs.md#file)> | 是 | 异步打开文件之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. fileIo.open(filePath, (err: BusinessError, file: fileIo.File) => {
5. if (err) {
6. console.error(`Failed to open. Code: ${err.code}, message: ${err.message}`);
7. } else {
8. console.info(`Succeeded in getting file fd: ${file.fd}`);
9. fileIo.closeSync(file);
10. }
11. });
```

## fileIo.openSync

PhonePC/2in1TabletTVWearable

openSync(path: string, mode?: number): File

以同步方法打开文件或目录。支持使用URI打开文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 打开文件或目录的应用沙箱路径或URI。 |
| mode | number | 否 | 打开文件或目录的[选项](js-apis-file-fs.md#openmode)，必须指定如下选项中的一个，默认以只读方式打开：  - OpenMode.READ\_ONLY(0o0)：只读打开。  - OpenMode.WRITE\_ONLY(0o1)：只写打开。  - OpenMode.READ\_WRITE(0o2)：读写打开。  给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：  - OpenMode.CREATE(0o100)：若文件不存在，则创建文件。  - OpenMode.TRUNC(0o1000)：如果文件存在且文件具有写权限，则将其长度裁剪为零。  - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到文件末尾。  - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。  - OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。  - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。  - OpenMode.SYNC(0o4010000)：以同步IO的方式打开文件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [File](js-apis-file-fs.md#file) | 打开的File对象。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
3. console.info(`Succeeded in getting file fd: ${file.fd}`);
4. fileIo.closeSync(file);
```

## fileIo.read

PhonePC/2in1TabletTVWearable

read(fd: number, buffer: ArrayBuffer, options?: ReadOptions): Promise<number>

读取文件数据，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | [ReadOptions](js-apis-file-fs.md#readoptions11) | 否 | 支持如下选项：  - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。  - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回实际读取的数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { buffer } from '@kit.ArkTS';

4. let filePath = pathDir + "/test.txt";
5. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
6. let arrayBuffer = new ArrayBuffer(4096);
7. fileIo.read(file.fd, arrayBuffer).then((readLen: number) => {
8. let buf = buffer.from(arrayBuffer, 0, readLen);
9. console.info(`Succeeded in reading file data. The content of file: ${buf.toString()}`);
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to read file data. Code: ${err.code}, message: ${err.message}`);
12. }).finally(() => {
13. fileIo.closeSync(file);
14. });
```

## fileIo.read

PhonePC/2in1TabletTVWearable

read(fd: number, buffer: ArrayBuffer, options?: ReadOptions, callback: AsyncCallback<number>): void

从文件读取数据，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | [ReadOptions](js-apis-file-fs.md#readoptions11) | 否 | 支持如下选项：  - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。  - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。 |
| callback | AsyncCallback<number> | 是 | 异步读取数据之后的回调。返回实际读取的数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { buffer } from '@kit.ArkTS';

4. let filePath = pathDir + "/test.txt";
5. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
6. let arrayBuffer = new ArrayBuffer(4096);
7. fileIo.read(file.fd, arrayBuffer, (err: BusinessError, readLen: number) => {
8. if (err) {
9. console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
10. } else {
11. let buf = buffer.from(arrayBuffer, 0, readLen);
12. console.info(`Succeeded in reading file data. The content of file: ${buf.toString()}`);
13. }
14. fileIo.closeSync(file);
15. });
```

## fileIo.readSync

PhonePC/2in1TabletTVWearable

readSync(fd: number, buffer: ArrayBuffer, options?: ReadOptions): number

以同步方法从文件读取数据。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | [ReadOptions](js-apis-file-fs.md#readoptions11) | 否 | 支持如下选项：  - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。  - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回实际读取的数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
3. let buf = new ArrayBuffer(4096);
4. fileIo.readSync(file.fd, buf);
5. fileIo.closeSync(file);
```

## fileIo.rmdir

PhonePC/2in1TabletTVWearable

rmdir(path: string): Promise<void>

删除目录及其所有子目录和文件，使用promise异步回调。

说明

该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlink接口删除单个文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let dirPath = pathDir + "/testDir";
4. fileIo.rmdir(dirPath).then(() => {
5. console.info(`Succeeded in removing directory.`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to remove directory. Code: ${err.code}, message: ${err.message}`);
8. });
```

## fileIo.rmdir

PhonePC/2in1TabletTVWearable

rmdir(path: string, callback: AsyncCallback<void>): void

删除目录及其所有子目录和文件，使用callback异步回调。

说明

该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlink接口删除单个文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步删除目录之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let dirPath = pathDir + "/testDir";
4. fileIo.rmdir(dirPath, (err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to remove directory. Code: ${err.code}, message: ${err.message}`);
7. } else {
8. console.info(`Succeeded in removing directory.`);
9. }
10. });
```

## fileIo.rmdirSync

PhonePC/2in1TabletTVWearable

rmdirSync(path: string): void

以同步方法删除目录及其所有子目录和文件。

说明

该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlinkSync接口删除单个文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let dirPath = pathDir + "/testDir";
2. fileIo.rmdirSync(dirPath);
```

## fileIo.unlink

PhonePC/2in1TabletTVWearable

unlink(path: string): Promise<void>

删除单个文件，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. fileIo.unlink(filePath).then(() => {
5. console.info(`Succeeded in removing file.`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to remove file. Code: ${err.code}, message: ${err.message}`);
8. });
```

## fileIo.unlink

PhonePC/2in1TabletTVWearable

unlink(path: string, callback: AsyncCallback<void>): void

删除文件，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步删除文件之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. fileIo.unlink(filePath, (err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to remove file. Code: ${err.code}, message: ${err.message}`);
7. } else {
8. console.info(`Succeeded in removing file.`);
9. }
10. });
```

## fileIo.unlinkSync

PhonePC/2in1TabletTVWearable

unlinkSync(path: string): void

以同步方法删除文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. fileIo.unlinkSync(filePath);
```

## fileIo.write

PhonePC/2in1TabletTVWearable

write(fd: number, buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>

将数据写入文件，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](js-apis-file-fs.md#writeoptions11) | 否 | 支持如下选项：  - offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写入。  - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。  - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。当前仅支持 'utf-8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回实际写入的数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
5. let str: string = "hello, world";
6. fileIo.write(file.fd, str).then((writeLen: number) => {
7. console.info(`Succeeded in writing data to file, size is: ${writeLen}`);
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to write data to file. Code: ${err.code}, message: ${err.message}`);
10. }).finally(() => {
11. fileIo.closeSync(file);
12. });
```

## fileIo.write

PhonePC/2in1TabletTVWearable

write(fd: number, buffer: ArrayBuffer | string, options?: WriteOptions, callback: AsyncCallback<number>): void

将数据写入文件，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](js-apis-file-fs.md#writeoptions11) | 否 | 支持如下选项：  - offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。  - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。  - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。当前仅支持 'utf-8'。 |
| callback | AsyncCallback<number> | 是 | 异步将数据写入完成后执行的回调函数。返回实际写入的数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
5. let str: string = "hello, world";
6. fileIo.write(file.fd, str, (err: BusinessError, writeLen: number) => {
7. if (err) {
8. console.error(`Failed to write data to file. Code: ${err.code}, message: ${err.message}`);
9. } else {
10. console.info(`Succeeded in writing data to file, size is: ${writeLen}`);
11. }
12. fileIo.closeSync(file);
13. });
```

## fileIo.writeSync

PhonePC/2in1TabletTVWearable

writeSync(fd: number, buffer: ArrayBuffer | string, options?: WriteOptions): number

以同步方法将数据写入文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](js-apis-file-fs.md#writeoptions11) | 否 | 支持如下选项：  - offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。  - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。  - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。当前仅支持 'utf-8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回实际写入的数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
3. let str: string = "hello, world";
4. let writeLen = fileIo.writeSync(file.fd, str);
5. console.info(`Succeeded in writing data to file, size is: ${writeLen}`);
6. fileIo.closeSync(file);
```

## fileIo.truncate

PhonePC/2in1TabletTVWearable

truncate(file: string | number, len?: number): Promise<void>

截断文件，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | number | 是 | 文件的应用沙箱路径或已打开的文件描述符fd。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let len: number = 5;
5. fileIo.truncate(filePath, len).then(() => {
6. console.info(`Succeeded in truncating file.`);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to truncate file. Code: ${err.code}, message: ${err.message}`);
9. });
```

## fileIo.truncate

PhonePC/2in1TabletTVWearable

truncate(file: string | number, len?: number, callback: AsyncCallback<void>): void

截断文件，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | number | 是 | 文件的应用沙箱路径或已打开的文件描述符fd。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |
| callback | AsyncCallback<void> | 是 | 回调函数，本调用无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let len: number = 5;
5. fileIo.truncate(filePath, len, (err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to truncate. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info(`Succeeded in truncating.`);
10. }
11. });
```

## fileIo.truncateSync

PhonePC/2in1TabletTVWearable

truncateSync(file: string | number, len?: number): void

以同步方法截断文件内容。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | number | 是 | 文件的应用沙箱路径或已打开的文件描述符fd。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let len: number = 5;
3. fileIo.truncateSync(filePath, len);
```

## fileIo.readLines11+

PhonePC/2in1TabletTVWearable

readLines(filePath: string, options?: Options): Promise<ReaderIterator>

逐行读取文件文本内容，使用promise异步回调。只支持读取utf-8格式文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | [Options](js-apis-file-fs.md#options11) | 否 | 可选项。支持以下选项：  - encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReaderIterator](js-apis-file-fs.md#readeriterator11)> | Promise对象。返回文件读取迭代器。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Options } from '@kit.CoreFileKit';

4. let filePath = pathDir + "/test.txt";
5. let options: Options = {
6. encoding: 'utf-8'
7. };
8. fileIo.readLines(filePath, options).then((readerIterator: fileIo.ReaderIterator) => {
9. for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
10. console.info(`Succeeded in reading lines, content: ${it.value}`);
11. }
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to read lines. Code: ${err.code}, message: ${err.message}`);
14. });
```

## fileIo.readLines11+

PhonePC/2in1TabletTVWearable

readLines(filePath: string, options?: Options, callback: AsyncCallback<ReaderIterator>): void

逐行读取文件文本内容，使用callback异步回调，只支持读取utf-8格式文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | [Options](js-apis-file-fs.md#options11) | 否 | 可选项。支持以下选项：  - encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |
| callback | AsyncCallback<[ReaderIterator](js-apis-file-fs.md#readeriterator11)> | 是 | 逐行读取文件文本内容回调。返回文件读取迭代器。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Options } from '@kit.CoreFileKit';

4. let filePath = pathDir + "/test.txt";
5. let options: Options = {
6. encoding: 'utf-8'
7. };
8. fileIo.readLines(filePath, options, (err: BusinessError, readerIterator: fileIo.ReaderIterator) => {
9. if (err) {
10. console.error(`Failed to read lines. Code: ${err.code}, message: ${err.message}`);
11. } else {
12. for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
13. console.info(`Succeeded in reading lines, content: ${it.value}`);
14. }
15. }
16. });
```

## fileIo.readLinesSync11+

PhonePC/2in1TabletTVWearable

readLinesSync(filePath: string, options?: Options): ReaderIterator

以同步方式逐行读取文件的文本内容。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | [Options](js-apis-file-fs.md#options11) | 否 | 可选项。支持以下选项：  - encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ReaderIterator](js-apis-file-fs.md#readeriterator11) | 返回文件读取迭代器。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { Options } from '@kit.CoreFileKit';

3. let filePath = pathDir + "/test.txt";
4. let options: Options = {
5. encoding: 'utf-8'
6. };
7. let readerIterator = fileIo.readLinesSync(filePath, options);
8. for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
9. console.info(`Succeeded in reading lines, content: ${it.value}`);
10. }
```

## ReaderIterator11+

PhonePC/2in1TabletTVWearable

文件读取迭代器。在调用ReaderIterator的方法前，需要先通过readLines方法（同步或异步）来构建一个ReaderIterator实例。

### next11+

PhonePC/2in1TabletTVWearable

next(): ReaderIteratorResult

获取迭代器下一项内容。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ReaderIteratorResult](js-apis-file-fs.md#readeriteratorresult11) | 文件读取迭代器返回结果。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

说明

如果ReaderIterator读取的当前行的编码方式不是'utf-8'，接口返回错误码13900037。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Options } from '@kit.CoreFileKit';

4. let filePath = pathDir + "/test.txt";
5. let options: Options = {
6. encoding: 'utf-8'
7. };
8. fileIo.readLines(filePath, options).then((readerIterator: fileIo.ReaderIterator) => {
9. for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
10. console.info(`Succeeded in reading lines, content: ${it.value}`);
11. }
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to read lines. Code: ${err.code}, message: ${err.message}`);
14. });
```

## ReaderIteratorResult11+

PhonePC/2in1TabletTVWearable

文件读取迭代器返回结果，支持ReaderIterator接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| done | boolean | 迭代器是否已完成迭代。true：已完成迭代；false：未完成迭代。 |
| value | string | 逐行读取的文件文本内容。 |

## fileIo.readText

PhonePC/2in1TabletTVWearable

readText(filePath: string, options?: ReadTextOptions): Promise<string>

基于文本方式读取文件（即直接读取文件的文本内容），使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | [ReadTextOptions](js-apis-file-fs.md#readtextoptions11) | 否 | 支持如下选项：  - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。  - length，number类型，表示期望读取数据，单位为Byte。可选，默认文件长度。  - encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回读取文件的内容。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. fileIo.readText(filePath).then((str: string) => {
5. console.info(`Succeeded in reading text, text is: ${str}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to read text. Code: ${err.code}, message: ${err.message}`);
8. });
```

## fileIo.readText

PhonePC/2in1TabletTVWearable

readText(filePath: string, options?: ReadTextOptions, callback: AsyncCallback<string>): void

基于文本方式读取文件内容，使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | [ReadTextOptions](js-apis-file-fs.md#readtextoptions11) | 否 | 支持如下选项：  - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。  - length，number类型，表示期望读取数据，单位为Byte。可选，默认文件长度。  - encoding，string类型，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |
| callback | AsyncCallback<string> | 是 | 回调函数，返回读取文件的内容。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ReadTextOptions } from '@kit.CoreFileKit';

4. let filePath = pathDir + "/test.txt";
5. let stat = fileIo.statSync(filePath);
6. let readTextOption: ReadTextOptions = {
7. offset: 1,
8. length: stat.size,
9. encoding: 'utf-8'
10. };
11. fileIo.readText(filePath, readTextOption, (err: BusinessError, str: string) => {
12. if (err) {
13. console.error(`Failed to read text. Code: ${err.code}, message: ${err.message}`);
14. } else {
15. console.info(`Succeeded in reading text, text is: ${str}`);
16. }
17. });
```

## fileIo.readTextSync

PhonePC/2in1TabletTVWearable

readTextSync(filePath: string, options?: ReadTextOptions): string

以同步方法基于文本方式读取文件（即直接读取文件的文本内容）。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | [ReadTextOptions](js-apis-file-fs.md#readtextoptions11) | 否 | 支持如下选项：  - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。  - length，number类型，表示期望读取数据，单位为Byte。可选，默认文件长度。  - encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回读取文件的内容。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { ReadTextOptions } from '@kit.CoreFileKit';

3. let filePath = pathDir + "/test.txt";
4. let readTextOptions: ReadTextOptions = {
5. offset: 1,
6. length: 0,
7. encoding: 'utf-8'
8. };
9. let stat = fileIo.statSync(filePath);
10. readTextOptions.length = stat.size;
11. let str = fileIo.readTextSync(filePath, readTextOptions);
12. console.info(`Succeeded in reading text, text is: ${str}`);
```

## fileIo.lstat

PhonePC/2in1TabletTVWearable

lstat(path: string): Promise<Stat>

获取符号链接文件信息，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径path或URI。  **说明**：从API version 22开始，支持传入URI。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Stat](js-apis-file-fs.md#stat)> | Promise对象。返回Stat对象，表示文件的具体信息，详情见Stat。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/linkToFile";
4. fileIo.lstat(filePath).then((stat: fileIo.Stat) => {
5. console.info(`Succeeded in getting symbolic link info, the size of file is ${stat.size}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to get symbolic link info. Code: ${err.code}, message: ${err.message}`);
8. });
```

## fileIo.lstat

PhonePC/2in1TabletTVWearable

lstat(path: string, callback: AsyncCallback<Stat>): void

获取符号链接文件信息，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径path或URI。  **说明**：从API version 22开始，支持传入URI。 |
| callback | AsyncCallback<[Stat](js-apis-file-fs.md#stat)> | 是 | 异步获取文件具体信息之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/linkToFile";
4. fileIo.lstat(filePath, (err: BusinessError, stat: fileIo.Stat) => {
5. if (err) {
6. console.error(`Failed to get symbolic link info. Code: ${err.code}, message: ${err.message}`);
7. } else {
8. console.info(`Succeeded in getting symbolic link info, the size of file is ${stat.size}`);
9. }
10. });
```

## fileIo.lstatSync

PhonePC/2in1TabletTVWearable

lstatSync(path: string): Stat

以同步方法获取符号链接文件信息。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径path或URI。  **说明**：从API version 22开始，支持传入URI。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Stat](js-apis-file-fs.md#stat) | 表示文件的具体信息。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/linkToFile";
2. let fileStat = fileIo.lstatSync(filePath);
3. console.info(`Succeeded in getting symbolic link info, the size of file is ${fileStat.size}`);
```

## fileIo.rename

PhonePC/2in1TabletTVWearable

rename(oldPath: string, newPath: string): Promise<void>

重命名文件或目录，使用promise异步回调。

说明

该接口不支持在分布式文件路径下操作。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oldPath | string | 是 | 文件的应用沙箱原路径。 |
| newPath | string | 是 | 文件的应用沙箱新路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let srcFile = pathDir + "/test.txt";
4. let dstFile = pathDir + "/new.txt";
5. fileIo.rename(srcFile, dstFile).then(() => {
6. console.info(`Succeeded in renaming.`);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to rename. Code: ${err.code}, message: ${err.message}`);
9. });
```

## fileIo.rename

PhonePC/2in1TabletTVWearable

rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void

重命名文件或目录，使用callback异步回调。

说明

该接口不支持在分布式文件路径下操作。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oldPath | string | 是 | 文件的应用沙箱原路径。 |
| newPath | string | 是 | 文件的应用沙箱新路径。 |
| callback | AsyncCallback<void> | 是 | 异步重命名文件之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let srcFile = pathDir + "/test.txt";
4. let dstFile = pathDir + "/new.txt";
5. fileIo.rename(srcFile, dstFile, (err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to rename. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info(`Succeeded in renaming.`);
10. }
11. });
```

## fileIo.renameSync

PhonePC/2in1TabletTVWearable

renameSync(oldPath: string, newPath: string): void

以同步方法重命名文件或目录。

说明

该接口不支持在分布式文件路径下操作。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oldPath | string | 是 | 文件的应用沙箱原路径。 |
| newPath | string | 是 | 文件的应用沙箱新路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let srcFile = pathDir + "/test.txt";
2. let dstFile = pathDir + "/new.txt";
3. fileIo.renameSync(srcFile, dstFile);
```

## fileIo.fsync

PhonePC/2in1TabletTVWearable

fsync(fd: number): Promise<void>

将文件系统缓存数据写入磁盘，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let file = fileIo.openSync(filePath);
5. fileIo.fsync(file.fd).then(() => {
6. console.info(`Succeeded in syncing data.`);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to sync data. Code: ${err.code}, message: ${err.message}`);
9. }).finally(() => {
10. fileIo.closeSync(file);
11. });
```

## fileIo.fsync

PhonePC/2in1TabletTVWearable

fsync(fd: number, callback: AsyncCallback<void>): void

将文件系统缓存数据写入磁盘，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| callback | AsyncCallback<void> | 是 | 异步将文件数据同步之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let file = fileIo.openSync(filePath);
5. fileIo.fsync(file.fd, (err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to sync. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info(`Succeeded in syncing.`);
10. }
11. fileIo.closeSync(file);
12. });
```

## fileIo.fsyncSync

PhonePC/2in1TabletTVWearable

fsyncSync(fd: number): void

以同步方法将文件系统缓存数据写入磁盘。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let file = fileIo.openSync(filePath);
3. fileIo.fsyncSync(file.fd);
4. fileIo.closeSync(file);
```

## fileIo.fdatasync

PhonePC/2in1TabletTVWearable

fdatasync(fd: number): Promise<void>

实现文件内容数据同步，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let file = fileIo.openSync(filePath);
5. fileIo.fdatasync(file.fd).then(() => {
6. console.info(`Succeeded in syncing data.`);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to sync data. Code: ${err.code}, message: ${err.message}`);
9. }).finally(() => {
10. fileIo.closeSync(file);
11. });
```

## fileIo.fdatasync

PhonePC/2in1TabletTVWearable

fdatasync(fd: number, callback: AsyncCallback<void>): void

实现文件内容数据同步，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| callback | AsyncCallback<void> | 是 | 异步将文件内容数据同步之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let file = fileIo.openSync(filePath);
5. fileIo.fdatasync(file.fd, (err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to syncing data. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info(`Succeeded in syncing data.`);
10. }
11. fileIo.closeSync(file);
12. });
```

## fileIo.fdatasyncSync

PhonePC/2in1TabletTVWearable

fdatasyncSync(fd: number): void

以同步方法实现文件内容的数据同步。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let file = fileIo.openSync(filePath);
3. fileIo.fdatasyncSync(file.fd);
4. fileIo.closeSync(file);
```

## fileIo.symlink

PhonePC/2in1TabletTVWearable

symlink(target: string, srcPath: string): Promise<void>

基于文件路径创建符号链接，使用promise异步回调。

说明

从API version 11开始，不支持三方应用使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | string | 是 | 要链接的目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let srcFile = pathDir + "/test.txt";
4. let dstFile = pathDir + "/test";
5. fileIo.symlink(srcFile, dstFile).then(() => {
6. console.info(`Succeeded in creating symbolic link.`);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to create symbolic link. Code: ${err.code}, message: ${err.message}`);
9. });
```

## fileIo.symlink

PhonePC/2in1TabletTVWearable

symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void

基于文件路径创建符号链接，使用callback异步回调。

说明

从API version 11开始，不支持三方应用使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | string | 是 | 要链接的目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步创建符号链接信息之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let srcFile = pathDir + "/test.txt";
4. let dstFile = pathDir + "/test";
5. fileIo.symlink(srcFile, dstFile, (err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to create symbolic link. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info(`Succeeded in creating symbolic link.`);
10. }
11. });
```

## fileIo.symlinkSync

PhonePC/2in1TabletTVWearable

symlinkSync(target: string, srcPath: string): void

以同步的方法基于文件路径创建符号链接。

说明

从API version 11开始，不支持三方应用使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | string | 是 | 要链接的目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let srcFile = pathDir + "/test.txt";
2. let dstFile = pathDir + "/test";
3. fileIo.symlinkSync(srcFile, dstFile);
```

## fileIo.listFile

PhonePC/2in1TabletTVWearable

listFile(path: string, options?: ListFileOptions): Promise<string[]>

默认列出当前目录下所有文件名和目录名。支持过滤。使用promise异步回调。

可通过配置options中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| options | [ListFileOptions](js-apis-file-fs.md#listfileoptions11) | 否 | 文件过滤选项。默认不进行过滤。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string[]> | Promise对象。返回文件名数组，默认以'utf-8'编码。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Filter, ListFileOptions } from '@kit.CoreFileKit';

4. let listFileOption: ListFileOptions = {
5. recursion: false,
6. listNum: 0,
7. filter: {
8. suffix: [".png", ".jpg", ".jpeg"],
9. displayName: ["*abc", "efg*"],
10. fileSizeOver: 1024
11. }
12. }
13. fileIo.listFile(pathDir, listFileOption).then((filenames: Array<string>) => {
14. console.info(`Succeeded in listing file.`);
15. for (let i = 0; i < filenames.length; i++) {
16. console.info(`Succeeded in listing file, file name: ${filenames[i]}`);
17. }
18. }).catch((err: BusinessError) => {
19. console.error(`Failed to list file. Code: ${err.code}, message: ${err.message}`);
20. });
```

## fileIo.listFile

PhonePC/2in1TabletTVWearable

listFile(path: string, options?: ListFileOptions, callback: AsyncCallback<string[]>): void

默认列出当前目录下所有文件名和目录名。支持过滤。使用callback异步回调。

可通过配置options中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| options | [ListFileOptions](js-apis-file-fs.md#listfileoptions11) | 否 | 文件过滤选项。默认不进行过滤。 |
| callback | AsyncCallback<string[]> | 是 | 异步列出文件名数组之后的回调，默认以'utf-8'编码。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Filter, ListFileOptions } from '@kit.CoreFileKit';

4. let listFileOption: ListFileOptions = {
5. recursion: false,
6. listNum: 0,
7. filter: {
8. suffix: [".png", ".jpg", ".jpeg"],
9. displayName: ["*abc", "efg*"],
10. fileSizeOver: 1024
11. }
12. };
13. fileIo.listFile(pathDir, listFileOption, (err: BusinessError, filenames: Array<string>) => {
14. if (err) {
15. console.error(`Failed to list file. Code: ${err.code}, message: ${err.message}`);
16. } else {
17. console.info(`Succeeded in listing file.`);
18. for (let i = 0; i < filenames.length; i++) {
19. console.info(`Succeeded in listing file, file name: ${filenames[i]}`);
20. }
21. }
22. });
```

## fileIo.listFileSync

PhonePC/2in1TabletTVWearable

listFileSync(path: string, options?: ListFileOptions): string[]

默认以同步方式列出当前目录下所有文件名和目录名。支持过滤。

可通过配置options中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| options | [ListFileOptions](js-apis-file-fs.md#listfileoptions11) | 否 | 文件过滤选项。默认不进行过滤。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 返回文件名数组，默认以'utf-8'编码。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { Filter, ListFileOptions} from '@kit.CoreFileKit';

3. let listFileOption: ListFileOptions = {
4. recursion: false,
5. listNum: 0,
6. filter: {
7. suffix: [".png", ".jpg", ".jpeg"],
8. displayName: ["*abc", "efg*"],
9. fileSizeOver: 1024
10. }
11. };
12. let filenames = fileIo.listFileSync(pathDir, listFileOption);
13. console.info(`Succeeded in listing file.`);
14. for (let i = 0; i < filenames.length; i++) {
15. console.info(`Succeeded in listing file, file name: ${filenames[i]}`);
16. }
```

## fileIo.lseek11+

PhonePC/2in1TabletTVWearable

lseek(fd: number, offset: number, whence?: WhenceType): number

调整文件偏移指针位置。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 文件描述符。 |
| offset | number | 是 | 相对偏移位置，单位为Byte。 |
| whence | [WhenceType](js-apis-file-fs.md#whencetype11) | 否 | 偏移指针相对位置类型。不指定则默认为文件起始位置处。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前文件偏移指针位置（相对于文件头的偏移量，单位为Byte）。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
3. let offset = fileIo.lseek(file.fd, 5, fileIo.WhenceType.SEEK_SET);
4. console.info(`Succeeded in seeking, the current offset is at ${offset}`);
5. fileIo.closeSync(file);
```

## fileIo.moveDir10+

PhonePC/2in1TabletTVWearable

moveDir(src: string, dest: string, mode?: number): Promise<void>

移动源目录至目标路径下，使用promise异步回调。

说明

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 否 | 移动模式，默认值为0。  - mode为0，目录级别抛异常。若目标目录下存在与源目录名冲突的非空目录，则抛出异常。  - mode为1，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](js-apis-file-fs.md#conflictfiles10)>形式提供。  - mode为2，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。  - mode为3，目录级别强制覆盖。移动源目录至目标目录下，目标目录下移动的目录内容与源目录完全一致。若目标目录下存在与源目录名冲突的目录，该目录下的所有原始文件将被删除。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let srcPath = pathDir + "/srcDir";
4. let destPath = pathDir + "/destDir";
5. fileIo.moveDir(srcPath, destPath, 1).then(() => {
6. console.info(`Succeeded in moving directory.`);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to move directory. Code: ${err.code}, message: ${err.message}`);
9. });
```

## fileIo.moveDir10+

PhonePC/2in1TabletTVWearable

moveDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void

移动源目录至目标路径下，支持设置移动模式。使用callback异步回调。

说明

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 是 | 移动模式，默认值为0。  - mode为0，目录级别抛异常。若目标目录下存在与源目录名冲突的目录，则抛出异常。  - mode为1，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](js-apis-file-fs.md#conflictfiles10)>形式提供。  - mode为2，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。  - mode为3，目录级别强制覆盖。移动源目录至目标目录下，目标目录下移动的目录内容与源目录完全一致。若目标目录下存在与源目录名冲突的目录，该目录下所有原始文件将被删除。 |
| callback | AsyncCallback<void, Array<[ConflictFiles](js-apis-file-fs.md#conflictfiles10)>> | 是 | 异步移动目录之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ConflictFiles } from '@kit.CoreFileKit';

4. let srcPath = pathDir + "/srcDir";
5. let destPath = pathDir + "/destDir";
6. fileIo.moveDir(srcPath, destPath, 1, (err: BusinessError<Array<ConflictFiles>>) => {
7. if (err && err.code == 13900015 && err.data?.length !== undefined) {
8. for (let i = 0; i < err.data.length; i++) {
9. console.error(`Failed to move directory, with conflicting files: ${err.data[i].srcFile} ${err.data[i].destFile}`);
10. }
11. } else if (err) {
12. console.error(`Failed to move directory. Code: ${err.code}, message: ${err.message}`);
13. } else {
14. console.info(`Succeeded in moving directory.`);
15. }
16. });
```

## fileIo.moveDir10+

PhonePC/2in1TabletTVWearable

moveDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void

移动源目录至目标路径下。使用callback异步回调。

移动模式为目录级别抛异常。当目标目录下存在与源目录名冲突的目录，则抛出异常。

说明

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| callback | AsyncCallback<void, Array<[ConflictFiles](js-apis-file-fs.md#conflictfiles10)>> | 是 | 异步移动目录之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ConflictFiles } from '@kit.CoreFileKit';

4. let srcPath = pathDir + "/srcDir";
5. let destPath = pathDir + "/destDir";
6. fileIo.moveDir(srcPath, destPath, (err: BusinessError<Array<ConflictFiles>>) => {
7. if (err && err.code == 13900015 && err.data?.length !== undefined) {
8. for (let i = 0; i < err.data.length; i++) {
9. console.error(`Failed to move directory, with conflicting files: ${err.data[i].srcFile} ${err.data[i].destFile}`);
10. }
11. } else if (err) {
12. console.error(`Failed to move directory. Code: ${err.code}, message: ${err.message}`);
13. } else {
14. console.info(`Succeeded in moving directory.`);
15. }
16. });
```

## fileIo.moveDirSync10+

PhonePC/2in1TabletTVWearable

moveDirSync(src: string, dest: string, mode?: number): void

以同步方法移动源目录至目标路径下。

说明

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 否 | 移动模式，默认值为0。  - mode为0，目录级别抛异常。若目标目录下存在与源目录名冲突的目录，则抛出异常。  - mode为1，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](js-apis-file-fs.md#conflictfiles10)>形式提供。  - mode为2，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。  - mode为3，目录级别强制覆盖。移动源目录至目标目录下，目标目录下移动的目录内容与源目录完全一致。若目标目录下存在与源目录名冲突的目录，该目录下所有原始文件将被删除。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ConflictFiles } from '@kit.CoreFileKit';

4. let srcPath = pathDir + "/srcDir";
5. let destPath = pathDir + "/destDir";
6. try {
7. fileIo.moveDirSync(srcPath, destPath, 1);
8. console.info(`Succeeded in moving directory.`);
9. } catch (error) {
10. let err: BusinessError<Array<ConflictFiles>> = error as BusinessError<Array<ConflictFiles>>;
11. if (err.code == 13900015 && err.data?.length !== undefined) {
12. for (let i = 0; i < err.data.length; i++) {
13. console.error(`Failed to move directory, with conflicting files: ${err.data[i].srcFile} ${err.data[i].destFile}`);
14. }
15. } else {
16. console.error(`Failed to move directory. Code: ${err.code}, message: ${err.message}`);
17. }
18. }
```

## fileIo.moveFile

PhonePC/2in1TabletTVWearable

moveFile(src: string, dest: string, mode?: number): Promise<void>

移动文件，使用promise异步回调。

说明

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源文件的应用沙箱路径。 |
| dest | string | 是 | 目标文件的应用沙箱路径。 |
| mode | number | 否 | 移动模式。若mode为0，移动位置存在同名文件时，强制移动覆盖。若mode为1，移动位置存在同名文件时，抛出异常。默认为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let srcPath = pathDir + "/source.txt";
4. let destPath = pathDir + "/dest.txt";
5. fileIo.moveFile(srcPath, destPath, 0).then(() => {
6. console.info(`Succeeded in moving file.`);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to move file. Code: ${err.code}, message: ${err.message}`);
9. });
```

## fileIo.moveFile

PhonePC/2in1TabletTVWearable

moveFile(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void

移动文件，支持设置移动模式。使用callback异步回调。

说明

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源文件的应用沙箱路径。 |
| dest | string | 是 | 目标文件的应用沙箱路径。 |
| mode | number | 是 | 移动模式。若mode为0，移动位置存在同名文件时，强制移动覆盖。若mode为1，移动位置存在同名文件时，抛出异常。默认为0。 |
| callback | AsyncCallback<void> | 是 | 异步移动文件之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let srcPath = pathDir + "/source.txt";
4. let destPath = pathDir + "/dest.txt";
5. fileIo.moveFile(srcPath, destPath, 0, (err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to move file. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info(`Succeeded in moving file.`);
10. }
11. });
```

## fileIo.moveFile

PhonePC/2in1TabletTVWearable

moveFile(src: string, dest: string, callback: AsyncCallback<void>): void

移动文件。如果移动位置存在同名文件，将强制覆盖。使用callback异步回调。

说明

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源文件的应用沙箱路径。 |
| dest | string | 是 | 目标文件的应用沙箱路径。 |
| callback | AsyncCallback<void> | 是 | 异步移动文件之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let srcPath = pathDir + "/source.txt";
4. let destPath = pathDir + "/dest.txt";
5. fileIo.moveFile(srcPath, destPath, (err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to move file. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info(`Succeeded in moving file.`);
10. }
11. });
```

## fileIo.moveFileSync

PhonePC/2in1TabletTVWearable

moveFileSync(src: string, dest: string, mode?: number): void

以同步方式移动文件。

说明

该接口不支持在分布式文件路径下操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源文件的应用沙箱路径。 |
| dest | string | 是 | 目标文件的应用沙箱路径。 |
| mode | number | 否 | 移动模式。若mode为0，移动位置存在同名文件时，强制移动覆盖。若mode为1，移动位置存在同名文件时，抛出异常。默认为0。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let srcPath = pathDir + "/source.txt";
2. let destPath = pathDir + "/dest.txt";
3. fileIo.moveFileSync(srcPath, destPath, 0);
4. console.info(`Succeeded in moving file.`);
```

## fileIo.mkdtemp

PhonePC/2in1TabletTVWearable

mkdtemp(prefix: string): Promise<string>

创建临时目录，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 指定目录路径，命名时需要以"XXXXXX"作为结尾。路径末尾的"XXXXXX"字符串将被替换为随机字符，以创建唯一的目录名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回生成的唯一目录路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. fileIo.mkdtemp(pathDir + "/XXXXXX").then((dir: string) => {
4. console.info(`Succeeded in making temporary directory.`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to make temporary directory. Code: ${err.code}, message: ${err.message}`);
7. });
```

## fileIo.mkdtemp

PhonePC/2in1TabletTVWearable

mkdtemp(prefix: string, callback: AsyncCallback<string>): void

创建临时目录，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 指定目录路径，命名时需要以"XXXXXX"作为结尾。路径末尾的"XXXXXX"字符串将被替换为随机字符，以创建唯一的目录名。 |
| callback | AsyncCallback<string> | 是 | 异步创建临时目录之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. fileIo.mkdtemp(pathDir + "/XXXXXX", (err: BusinessError, res: string) => {
4. if (err) {
5. console.error(`Failed to make temporary directory. Code: ${err.code}, message: ${err.message}`);
6. } else {
7. console.info(`Succeeded in making temporary directory.`);
8. }
9. });
```

## fileIo.mkdtempSync

PhonePC/2in1TabletTVWearable

mkdtempSync(prefix: string): string

以同步的方法创建临时目录。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 指定目录路径，命名时需要以"XXXXXX"作为结尾。路径末尾的"XXXXXX"字符串将被替换为随机字符，以创建唯一的目录名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 产生的唯一目录路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let res = fileIo.mkdtempSync(pathDir + "/XXXXXX");
```

## fileIo.utimes11+

PhonePC/2in1TabletTVWearable

utimes(path: string, mtime: number): void

更改文件上次修改该文件的时间。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径。 |
| mtime | number | 是 | 待更新的时间戳。自1970年1月1日起至目标时间的毫秒数。仅支持更改上次修改该文件的时间属性。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
3. fileIo.writeSync(file.fd, 'test data');
4. fileIo.closeSync(file);
5. fileIo.utimes(filePath, new Date().getTime());
```

## fileIo.createRandomAccessFile10+

PhonePC/2in1TabletTVWearable

createRandomAccessFile(file: string | File, mode?: number): Promise<RandomAccessFile>

基于文件路径或文件对象创建RandomAccessFile对象，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | [File](js-apis-file-fs.md#file) | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| mode | number | 否 | 创建文件RandomAccessFile对象的[选项](js-apis-file-fs.md#openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：  - OpenMode.READ\_ONLY(0o0)：只读创建。  - OpenMode.WRITE\_ONLY(0o1)：只写创建。  - OpenMode.READ\_WRITE(0o2)：读写创建。  给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：  - OpenMode.CREATE(0o100)：若文件不存在，则创建文件。  - OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。  - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。  - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。  - OpenMode.DIR(0o200000)：如果path未指向目录，则出错。不允许附加写权限。  - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。  - OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RandomAccessFile](js-apis-file-fs.md#randomaccessfile10)> | Promise对象。返回RandomAccessFile对象的结果。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
5. fileIo.createRandomAccessFile(file).then((randomAccessFile: fileIo.RandomAccessFile) => {
6. console.info(`Succeeded in creating randomaccessfile, fd: ${randomAccessFile.fd}`);
7. randomAccessFile.close();
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to create randomaccessfile. Code: ${err.code}, message: ${err.message}`);
10. }).finally(() => {
11. fileIo.closeSync(file);
12. });
```

## fileIo.createRandomAccessFile10+

PhonePC/2in1TabletTVWearable

createRandomAccessFile(file: string | File, callback: AsyncCallback<RandomAccessFile>): void

基于文件路径或文件对象，以只读方式创建RandomAccessFile对象，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | [File](js-apis-file-fs.md#file) | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| callback | AsyncCallback<[RandomAccessFile](js-apis-file-fs.md#randomaccessfile10)> | 是 | 异步创建RandomAccessFile对象之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
5. fileIo.createRandomAccessFile(file, (err: BusinessError, randomAccessFile: fileIo.RandomAccessFile) => {
6. if (err) {
7. console.error(`Failed to create randomaccessfile. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info(`Succeeded in creating randomaccessfile, fd: ${randomAccessFile.fd}`);
10. randomAccessFile.close();
11. }
12. fileIo.closeSync(file);
13. });
```

## fileIo.createRandomAccessFile10+

PhonePC/2in1TabletTVWearable

createRandomAccessFile(file: string | File, mode: number, callback: AsyncCallback<RandomAccessFile>): void

基于文件路径或文件对象创建RandomAccessFile对象，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | [File](js-apis-file-fs.md#file) | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| mode | number | 是 | 创建文件RandomAccessFile对象的[选项](js-apis-file-fs.md#openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：  - OpenMode.READ\_ONLY(0o0)：只读创建。  - OpenMode.WRITE\_ONLY(0o1)：只写创建。  - OpenMode.READ\_WRITE(0o2)：读写创建。  给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：  - OpenMode.CREATE(0o100)：若文件不存在，则创建文件。  - OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。  - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。  - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。  - OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。  - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。  - OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。 |
| callback | AsyncCallback<[RandomAccessFile](js-apis-file-fs.md#randomaccessfile10)> | 是 | 异步创建RandomAccessFile对象之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
5. fileIo.createRandomAccessFile(file, fileIo.OpenMode.READ_ONLY, (err: BusinessError, randomAccessFile: fileIo.RandomAccessFile) => {
6. if (err) {
7. console.error(`Failed to create randomaccessfile. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info(`Succeeded in creating randomaccessfile, fd: ${randomAccessFile.fd}`);
10. randomAccessFile.close();
11. }
12. fileIo.closeSync(file);
13. });
```

## fileIo.createRandomAccessFile12+

PhonePC/2in1TabletTVWearable

createRandomAccessFile(file: string | File, mode?: number, options?: RandomAccessFileOptions): Promise<RandomAccessFile>

基于文件路径或文件对象创建RandomAccessFile对象，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | [File](js-apis-file-fs.md#file) | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| mode | number | 否 | 创建文件RandomAccessFile对象的[选项](js-apis-file-fs.md#openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：  - OpenMode.READ\_ONLY(0o0)：只读创建。  - OpenMode.WRITE\_ONLY(0o1)：只写创建。  - OpenMode.READ\_WRITE(0o2)：读写创建。  给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：  - OpenMode.CREATE(0o100)：若文件不存在，则创建文件。  - OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。  - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。  - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。  - OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。  - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。  - OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。 |
| options | [RandomAccessFileOptions](js-apis-file-fs.md#randomaccessfileoptions12) | 否 | 支持如下选项：  - start，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。  - end，number类型，表示期望读取结束的位置，单位为Byte。可选，默认文件末尾。  此选项仅对[getreadstream](js-apis-file-fs.md#getreadstream12)及[getwritestream](js-apis-file-fs.md#getwritestream12)获取的文件流对象生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RandomAccessFile](js-apis-file-fs.md#randomaccessfile10)> | Promise对象。返回RandomAccessFile对象的结果。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. fileIo.createRandomAccessFile(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE, { start: 10, end: 100 })
5. .then((randomAccessFile: fileIo.RandomAccessFile) => {
6. console.info(`Succeeded in creating randomaccessfile, fd: ${randomAccessFile.fd}`);
7. randomAccessFile.close();
8. })
9. .catch((err: BusinessError) => {
10. console.error(`Failed to create randomaccessfile. Code: ${err.code}, message: ${err.message}`);
11. });
```

## fileIo.createRandomAccessFileSync10+

PhonePC/2in1TabletTVWearable

createRandomAccessFileSync(file: string | File, mode?: number): RandomAccessFile

基于文件路径或文件对象创建RandomAccessFile对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | [File](js-apis-file-fs.md#file) | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| mode | number | 否 | 创建文件RandomAccessFile对象的[选项](js-apis-file-fs.md#openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：  - OpenMode.READ\_ONLY(0o0)：只读创建。  - OpenMode.WRITE\_ONLY(0o1)：只写创建。  - OpenMode.READ\_WRITE(0o2)：读写创建。  给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：  - OpenMode.CREATE(0o100)：若文件不存在，则创建文件。  - OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。  - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。  - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。  - OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。  - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。  - OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RandomAccessFile](js-apis-file-fs.md#randomaccessfile10) | 返回RandomAccessFile对象。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
3. let randomAccessFile = fileIo.createRandomAccessFileSync(file);
4. randomAccessFile.close();
```

## fileIo.createRandomAccessFileSync12+

PhonePC/2in1TabletTVWearable

createRandomAccessFileSync(file: string | File, mode?: number, options?: RandomAccessFileOptions): RandomAccessFile

基于文件路径或文件对象创建RandomAccessFile对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | [File](js-apis-file-fs.md#file) | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| mode | number | 否 | 创建文件RandomAccessFile对象的[选项](js-apis-file-fs.md#openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：  - OpenMode.READ\_ONLY(0o0)：只读创建。  - OpenMode.WRITE\_ONLY(0o1)：只写创建。  - OpenMode.READ\_WRITE(0o2)：读写创建。  给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：  - OpenMode.CREATE(0o100)：若文件不存在，则创建文件。  - OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。  - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。  - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。  - OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。  - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。  - OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。 |
| options | [RandomAccessFileOptions](js-apis-file-fs.md#randomaccessfileoptions12) | 否 | 支持如下选项：  - start，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。  - end，number类型，表示期望读取结束的位置，单位为Byte。可选，默认文件末尾。  此选项仅对[getreadstream](js-apis-file-fs.md#getreadstream12)及[getwritestream](js-apis-file-fs.md#getwritestream12)获取的文件流对象生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RandomAccessFile](js-apis-file-fs.md#randomaccessfile10) | 返回RandomAccessFile对象。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE,
3. { start: 10, end: 100 });
4. randomAccessFile.close();
```

## fileIo.createStream

PhonePC/2in1TabletTVWearable

createStream(path: string, mode: string): Promise<Stream>

基于文件路径创建文件流，使用promise异步回调。需要配合[Stream](js-apis-file-fs.md#stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。  - r+：打开可读写的文件，该文件必须存在。  - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。  - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Stream](js-apis-file-fs.md#stream)> | Promise对象。返回文件流的结果。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. fileIo.createStream(filePath, "a+").then((stream: fileIo.Stream) => {
5. stream.closeSync();
6. console.info(`Succeeded in creating stream.`);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to create stream. Code: ${err.code}, message: ${err.message}`);
9. });
```

## fileIo.createStream

PhonePC/2in1TabletTVWearable

createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void

基于文件路径创建文件流，使用callback异步回调。需要配合[Stream](js-apis-file-fs.md#stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。  - r+：打开可读写的文件，该文件必须存在。  - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。  - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |
| callback | AsyncCallback<[Stream](js-apis-file-fs.md#stream)> | 是 | 异步打开文件流之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. fileIo.createStream(filePath, "r+", (err: BusinessError, stream: fileIo.Stream) => {
5. if (err) {
6. console.error(`Failed to create stream. Code: ${err.code}, message: ${err.message}`);
7. } else {
8. stream.closeSync();
9. console.info(`Succeeded in creating stream.`);
10. }
11. })
```

## fileIo.createStreamSync

PhonePC/2in1TabletTVWearable

createStreamSync(path: string, mode: string): Stream

以同步方法基于文件路径创建文件流。需要配合[Stream](js-apis-file-fs.md#stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。  - r+：打开可读写的文件，该文件必须存在。  - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。  - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Stream](js-apis-file-fs.md#stream) | 返回文件流的结果。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let stream = fileIo.createStreamSync(filePath, "r+");
3. console.info(`Succeeded in creating stream.`);
4. stream.closeSync();
```

## fileIo.fdopenStream

PhonePC/2in1TabletTVWearable

fdopenStream(fd: number, mode: string): Promise<Stream>

基于文件描述符打开文件流，使用promise异步回调。需要配合[Stream](js-apis-file-fs.md#stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。  - r+：打开可读写的文件，该文件必须存在。  - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。  - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Stream](js-apis-file-fs.md#stream)> | Promise对象。返回文件流的结果。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let file = fileIo.openSync(filePath);
5. fileIo.fdopenStream(file.fd, "r+").then((stream: fileIo.Stream) => {
6. console.info(`Succeeded in opening stream.`);
7. stream.closeSync();
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to open stream. Code: ${err.code}, message: ${err.message}`);
10. // 文件流打开失败后，文件描述符需要手动关闭
11. fileIo.closeSync(file);
12. });
```

注意

使用文件描述符创建的文件流时，文件描述符的生命周期将由文件流对象管理。调用文件流的close()函数后，初始的文件描述符也会被关闭。

## fileIo.fdopenStream

PhonePC/2in1TabletTVWearable

fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void

基于文件描述符打开文件流，使用callback异步回调。需要配合[Stream](js-apis-file-fs.md#stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。  - r+：打开可读写的文件，该文件必须存在。  - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。  - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |
| callback | AsyncCallback<[Stream](js-apis-file-fs.md#stream)> | 是 | 异步打开文件流之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY);
5. fileIo.fdopenStream(file.fd, "r+", (err: BusinessError, stream: fileIo.Stream) => {
6. if (err) {
7. console.error(`Failed to fdopen stream. Code: ${err.code}, message: ${err.message}`);
8. // 文件流打开失败后，文件描述符需要手动关闭
9. fileIo.closeSync(file);
10. } else {
11. console.info(`Succeeded in fdopening stream.`);
12. stream.closeSync();
13. }
14. });
```

注意

使用文件描述符创建的文件流，文件描述符的生命周期也交由文件流对象，在调用文件流的close()函数后，初始的文件描述符也会被关闭。

## fileIo.fdopenStreamSync

PhonePC/2in1TabletTVWearable

fdopenStreamSync(fd: number, mode: string): Stream

以同步方法基于文件描述符打开文件流。需要配合[Stream](js-apis-file-fs.md#stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。  - r+：打开可读写的文件，该文件必须存在。  - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。  - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。  - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Stream](js-apis-file-fs.md#stream) | 返回文件流的结果。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY | fileIo.OpenMode.CREATE);
3. let stream = fileIo.fdopenStreamSync(file.fd, "r+");
4. stream.closeSync();
```

注意

使用文件描述符创建的文件流，文件描述符的生命周期也交由文件流对象，在调用文件流的close()函数后，初始的文件描述符也会被关闭。

## fileIo.createReadStream12+

PhonePC/2in1TabletTVWearable

createReadStream(path: string, options?: ReadStreamOptions ): ReadStream

以同步方法打开文件可读流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件路径。 |
| options | [ReadStreamOptions](js-apis-file-fs.md#readstreamoptions12) | 否 | 支持如下选项：  - start，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。  - end，number类型，表示期望读取结束的位置，单位为Byte。可选，默认文件末尾。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ReadStream](js-apis-file-fs.md#readstream12) | 文件可读流。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. // 创建文件可读流
2. const rs = fileIo.createReadStream(`${pathDir}/read.txt`);
3. // 创建文件可写流
4. const ws = fileIo.createWriteStream(`${pathDir}/write.txt`);
5. // 暂停模式拷贝文件
6. rs.on('readable', () => {
7. const data = rs.read();
8. if (!data) {
9. return;
10. }
11. ws.write(data);
12. });
```

## fileIo.createWriteStream12+

PhonePC/2in1TabletTVWearable

createWriteStream(path: string, options?: WriteStreamOptions): WriteStream

以同步方法打开文件可写流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件路径。 |
| options | [WriteStreamOptions](js-apis-file-fs.md#writestreamoptions12) | 否 | 支持如下选项：  - start，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。  - mode，number 类型，创建文件可写流的[选项](js-apis-file-fs.md#openmode)，可选，默认以只写方式创建。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WriteStream](js-apis-file-fs.md#writestream12) | 文件可写流。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. // 创建文件可读流
2. const rs = fileIo.createReadStream(`${pathDir}/read.txt`);
3. // 创建文件可写流
4. const ws = fileIo.createWriteStream(`${pathDir}/write.txt`);
5. // 暂停模式拷贝文件
6. rs.on('readable', () => {
7. const data = rs.read();
8. if (!data) {
9. return;
10. }
11. ws.write(data);
12. });
```

## AtomicFile15+

PhonePC/2in1TabletTVWearable

AtomicFile是一个用于对文件进行原子读写操作的类。

在写操作时，通过写入临时文件，并在写入成功后将其重命名到原始文件位置来确保写入文件的完整性；而在写入失败时删除临时文件，不修改原始文件内容。

使用者可以自行调用finishWrite或failWrite来完成文件内容的写入或回滚。

**系统能力**：SystemCapability.FileManagement.File.FileIO

### constructor15+

PhonePC/2in1TabletTVWearable

constructor(path: string)

对于给定路径的文件创建一个AtomicFile类。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的沙箱路径。 |

### getBaseFile15+

PhonePC/2in1TabletTVWearable

getBaseFile(): File

通过AtomicFile对象获取文件对象。

文件描述符fd需要由用户调用close方法关闭。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [File](js-apis-file-fs.md#file) | 打开的File对象。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { common } from '@kit.AbilityKit';

3. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
4. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
5. let pathDir = context.filesDir;

7. try {
8. let atomicFile = new fileIo.AtomicFile(`${pathDir}/write.txt`);
9. let writeStream = atomicFile.startWrite();
10. writeStream.write("hello, world", "utf-8", ()=> {
11. atomicFile.finishWrite();
12. let file = atomicFile.getBaseFile();
13. console.info(`Succeeded in getting base file. fd: ${file.fd}, path: ${file.path}, name:${file.name}`);
14. })
15. } catch (err) {
16. console.error(`Failed to get baseFile. Code: ${err.code}, message: ${err.message}`);
17. }
```

### openRead15+

PhonePC/2in1TabletTVWearable

openRead(): ReadStream

创建一个读文件流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ReadStream](js-apis-file-fs.md#readstream12) | 文件可读流。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { common } from '@kit.AbilityKit';

3. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
4. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
5. let pathDir = context.filesDir;

7. try {
8. let file = new fileIo.AtomicFile(`${pathDir}/read.txt`);
9. let writeStream = file.startWrite();
10. writeStream.write("hello, world", "utf-8", ()=> {
11. file.finishWrite();
12. setTimeout(()=>{
13. let readStream = file.openRead();
14. readStream.on('readable', () => {
15. const data = readStream.read();
16. if (!data) {
17. console.error(`Failed to read atomicfile, data is null.`);
18. return;
19. }
20. console.info(`Succeeded in reading atomicfile, data is: ${data}`);
21. });
22. },1000);
23. })
24. } catch (err) {
25. console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
26. }
```

### readFully15+

PhonePC/2in1TabletTVWearable

readFully(): ArrayBuffer

读取文件全部内容。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 文件的全部内容。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { util, buffer } from '@kit.ArkTS';

4. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let pathDir = context.filesDir;

8. try {
9. let file = new fileIo.AtomicFile(`${pathDir}/read.txt`);
10. let writeStream = file.startWrite();
11. writeStream.write("hello, world", "utf-8", ()=> {
12. file.finishWrite();
13. setTimeout(()=>{
14. let data = file.readFully();
15. let decoder = util.TextDecoder.create('utf-8');
16. let str = decoder.decodeToString(new Uint8Array(data));
17. console.info(`Succeeded in reading atomicfile fully, str is: ${str}`);
18. },1000);
19. })
20. } catch (err) {
21. console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
22. }
```

### startWrite15+

PhonePC/2in1TabletTVWearable

startWrite(): WriteStream

对文件开始新的写入操作。将返回一个WriteStream，用于在其中写入新的文件数据。

当文件不存在时新建文件。

在写入文件完成后，写入成功需要调用finishWrite()，写入失败需要调用failWrite()。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WriteStream](js-apis-file-fs.md#writestream12) | 文件可写流。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { common } from '@kit.AbilityKit';

3. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
4. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
5. let pathDir = context.filesDir;

7. try {
8. let file = new fileIo.AtomicFile(`${pathDir}/write.txt`);
9. let writeStream = file.startWrite();
10. writeStream.write("hello, world", "utf-8", ()=> {
11. file.finishWrite();
12. console.info(`Succeeded in writing atomicfile finished.`);
13. })
14. } catch (err) {
15. console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
16. }
```

### finishWrite15+

PhonePC/2in1TabletTVWearable

finishWrite(): void

在完成对startWrite返回流的写入操作时调用，表示文件写入成功。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { common } from '@kit.AbilityKit';

3. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
4. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
5. let pathDir = context.filesDir;

7. try {
8. let file = new fileIo.AtomicFile(`${pathDir}/write.txt`);
9. let writeStream = file.startWrite();
10. writeStream.write("hello, world", "utf-8", ()=> {
11. file.finishWrite();
12. })
13. } catch (err) {
14. console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
15. }
```

### failWrite15+

PhonePC/2in1TabletTVWearable

failWrite(): void

文件写入失败后调用，将执行文件回滚操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { common } from '@kit.AbilityKit';

3. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
4. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
5. let pathDir = context.filesDir;

7. let file = new fileIo.AtomicFile(`${pathDir}/write.txt`);
8. try {
9. let writeStream = file.startWrite();
10. writeStream.write("hello, world", "utf-8", ()=> {
11. console.info(`Succeeded in writing atomicFile.`);
12. })
13. } catch (err) {
14. file.failWrite();
15. console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
16. }
```

### delete15+

PhonePC/2in1TabletTVWearable

delete(): void

删除AtomicFile类，会删除原始文件和临时文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { util } from '@kit.ArkTS';

4. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let pathDir = context.filesDir;

8. try {
9. let file = new fileIo.AtomicFile(`${pathDir}/read.txt`);
10. let writeStream = file.startWrite();
11. writeStream.write("hello, world", "utf-8", ()=> {
12. file.finishWrite();
13. setTimeout(()=>{
14. let data = file.readFully();
15. let decoder = util.TextDecoder.create('utf-8');
16. let str = decoder.decodeToString(new Uint8Array(data));
17. file.delete();
18. console.info(`Succeeded in delete atomicfile.`);
19. },1000);
20. })
21. } catch (err) {
22. console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
23. }
```

## fileIo.createWatcher10+

PhonePC/2in1TabletTVWearable

createWatcher(path: string, events: number, listener: WatchEventListener): Watcher

创建Watcher对象，监听文件或目录变动。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 监听文件或目录的沙箱路径。 |
| events | number | 是 | 监听变动的事件集，多个事件通过或(|)的方式进行集合。  - 0x1: IN\_ACCESS， 文件被访问。  - 0x2: IN\_MODIFY，文件内容被修改。  - 0x4: IN\_ATTRIB，文件元数据被修改。  - 0x8: IN\_CLOSE\_WRITE，文件在打开时进行了写操作，然后被关闭。  - 0x10: IN\_CLOSE\_NOWRITE，文件或目录在打开时未进行写操作，然后被关闭。  - 0x20: IN\_OPEN，文件或目录被打开。  - 0x40: IN\_MOVED\_FROM，监听目录中文件被移动走。  - 0x80: IN\_MOVED\_TO，监听目录中文件被移动过来。  - 0x100: IN\_CREATE，监听目录中文件或子目录被创建。  - 0x200: IN\_DELETE，监听目录中文件或子目录被删除。  - 0x400: IN\_DELETE\_SELF，监听的目录被删除，删除后监听停止。  - 0x800: IN\_MOVE\_SELF，监听的文件或目录被移动，移动后监听继续。  - 0xfff: IN\_ALL\_EVENTS，监听以上所有事件。 |
| listener | [WatchEventListener](js-apis-file-fs.md#watcheventlistener10) | 是 | 监听事件发生后的回调。监听事件每发生一次，回调一次。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Watcher](js-apis-file-fs.md#watcher10) | 返回Watcher对象。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { WatchEvent } from '@kit.CoreFileKit';

4. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let pathDir = context.filesDir;
7. let filePath = pathDir + "/test.txt";
8. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
9. let watcher = fileIo.createWatcher(filePath, 0x2 | 0x10, (watchEvent: WatchEvent) => {
10. if (watchEvent.event == 0x2) {
11. console.info(watchEvent.fileName + 'was modified');
12. } else if (watchEvent.event == 0x10) {
13. console.info(watchEvent.fileName + 'was closed');
14. }
15. });
16. watcher.start();
17. fileIo.writeSync(file.fd, 'test');
18. fileIo.closeSync(file);
19. watcher.stop();
```

## WatchEventListener10+

PhonePC/2in1TabletTVWearable

(event: WatchEvent): void

事件监听类。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [WatchEvent](js-apis-file-fs.md#watchevent10) | 是 | 回调的事件类。 |

## WatchEvent10+

PhonePC/2in1TabletTVWearable

事件类

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fileName | string | 是 | 否 | 发生监听事件对应文件的沙箱路径，该沙箱路径包含文件名称。 |
| event | number | 是 | 否 | 监听变动的事件集，多个事件通过或(|)的方式进行集合。  - 0x1: IN\_ACCESS， 文件被访问。  - 0x2: IN\_MODIFY，文件内容被修改。  - 0x4: IN\_ATTRIB，文件元数据被修改。  - 0x8: IN\_CLOSE\_WRITE，文件在打开时进行了写操作，然后被关闭。  - 0x10: IN\_CLOSE\_NOWRITE，文件或目录在打开时未进行写操作，然后被关闭。  - 0x20: IN\_OPEN，文件或目录被打开。  - 0x40: IN\_MOVED\_FROM，监听目录中文件被移动走。  - 0x80: IN\_MOVED\_TO，监听目录中文件被移动过来。  - 0x100: IN\_CREATE，监听目录中文件或子目录被创建。  - 0x200: IN\_DELETE，监听目录中文件或子目录被删除。  - 0x400: IN\_DELETE\_SELF，监听的目录被删除，删除后监听停止。  - 0x800: IN\_MOVE\_SELF，监听的文件或目录被移动，移动后监听继续。  - 0xfff: IN\_ALL\_EVENTS，监听以上所有事件。 |
| cookie | number | 是 | 否 | 绑定相关事件的cookie。当前仅支持事件IN\_MOVED\_FROM与IN\_MOVED\_TO，同一个文件的移动事件IN\_MOVED\_FROM和IN\_MOVED\_TO具有相同的cookie值。 |

## Progress11+

PhonePC/2in1TabletTVWearable

拷贝进度回调数据

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| processedSize | number | 是 | 否 | 已拷贝的数据大小，单位为Byte。 |
| totalSize | number | 是 | 否 | 待拷贝的数据总大小，单位为Byte。 |

## TaskSignal12+

PhonePC/2in1TabletTVWearable

拷贝中断信号。

**系统能力**：SystemCapability.FileManagement.File.FileIO

### cancel12+

PhonePC/2in1TabletTVWearable

cancel(): void

取消拷贝任务。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileUri } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';

5. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
6. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let pathDir = context.filesDir;

9. let srcDirPathLocal: string = pathDir + "/src";
10. let dstDirPathLocal: string = pathDir + "/dest";
11. let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
12. let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);
13. let copySignal = new fileIo.TaskSignal;
14. let progressListener: fileIo.ProgressListener = (progress: fileIo.Progress) => {
15. console.info(`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
16. if (progress.processedSize / progress.totalSize > 0.5) {
17. copySignal.cancel();
18. console.info("copy cancel.");
19. }
20. };
21. let options: fileIo.CopyOptions = {
22. "progressListener" : progressListener,
23. "copySignal" : copySignal,
24. }

26. try {
27. fileIo.copy(srcDirUriLocal, dstDirUriLocal, options, (err: BusinessError) => {
28. if (err) {
29. console.error("copy fail, err: ", err.message);
30. return;
31. }
32. console.info("copy success.");
33. })
34. } catch (err) {
35. console.error("copyFileWithCancel failed, err: ", err.message);
36. }
```

### onCancel12+

PhonePC/2in1TabletTVWearable

onCancel(): Promise<string>

取消拷贝事件监听。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。最后一个拷贝的文件路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { TaskSignal } from '@kit.CoreFileKit';

3. let copySignal: fileIo.TaskSignal = new TaskSignal();
4. copySignal.onCancel();
```

## CopyOptions11+

PhonePC/2in1TabletTVWearable

拷贝进度回调监听

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progressListener | [ProgressListener](js-apis-file-fs.md#progresslistener11) | 否 | 是 | 拷贝进度监听。 |
| copySignal | [TaskSignal](js-apis-file-fs.md#tasksignal12) | 否 | 是 | 取消拷贝信号。 |

## ProgressListener11+

PhonePC/2in1TabletTVWearable

拷贝进度监听。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 类型 | 说明 |
| --- | --- |
| (progress: [Progress](js-apis-file-fs.md#progress11)) => void | 拷贝进度监听 |

**示例：**

```
1. import { TaskSignal } from '@kit.CoreFileKit';

3. let copySignal: fileIo.TaskSignal = new TaskSignal();
4. let progressListener: fileIo.ProgressListener = (progress: fileIo.Progress) => {
5. console.info(`processedSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
6. };
7. let copyOption: fileIo.CopyOptions = {
8. "progressListener" : progressListener,
9. "copySignal" : copySignal,
10. }
```

## Stat

PhonePC/2in1TabletTVWearable

文件具体信息，在调用Stat的方法前，需要先通过[stat()](js-apis-file-fs.md#fileiostat)方法（同步或异步）构建一个Stat实例。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ino | bigint | 是 | 否 | 标识该文件。通常同设备上的不同文件的INO不同。 |
| mode | number | 是 | 否 | 表示文件权限，各特征位的含义如下：  **说明**：以下值为八进制，取得的返回值为十进制，请换算后查看。  - 0o400：用户读。对于普通文件，所有者可读取文件；对于目录，所有者可读取目录项。  - 0o200：用户写。对于普通文件，所有者可写入文件；对于目录，所有者可创建/删除目录项。  - 0o100：用户执行。对于普通文件，所有者可执行文件；对于目录，所有者可在目录中搜索给定路径名。  - 0o040：用户组读。对于普通文件，所有用户组可读取文件；对于目录，所有用户组可读取目录项。  - 0o020：用户组写。对于普通文件，所有用户组可写入文件；对于目录，所有用户组可创建/删除目录项。  - 0o010：用户组执行。对于普通文件，所有用户组可执行文件；对于目录，所有用户组是否可在目录中搜索给定路径名。  - 0o004：其他读。对于普通文件，其余用户可读取文件；对于目录，其他用户组可读取目录项。  - 0o002：其他写。对于普通文件，其余用户可写入文件；对于目录，其他用户组可创建/删除目录项。  - 0o001：其他执行。对于普通文件，其余用户可执行文件；对于目录，其他用户组可在目录中搜索给定路径名。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| uid | number | 是 | 否 | 文件所有者的ID。 |
| gid | number | 是 | 否 | 文件所有组的ID。 |
| size | number | 是 | 否 | 文件的大小，单位为Byte。仅对普通文件有效。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| atime | number | 是 | 否 | 上次访问该文件的时间，表示距1970年1月1日0时0分0秒的秒数。  **注意**：目前用户数据分区默认以“noatime”方式挂载，atime更新被禁用。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| mtime | number | 是 | 否 | 上次修改该文件的时间，表示距1970年1月1日0时0分0秒的秒数。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| ctime | number | 是 | 否 | 最近改变文件状态的时间，表示距1970年1月1日0时0分0秒的秒数。 |
| atimeNs15+ | bigint | 是 | 是 | 上次访问该文件的时间，表示距1970年1月1日0时0分0秒的纳秒数。  **注意**：目前用户数据分区默认以“noatime”方式挂载，atime更新被禁用。 |
| mtimeNs15+ | bigint | 是 | 是 | 上次修改该文件的时间，表示距1970年1月1日0时0分0秒的纳秒数。 |
| ctimeNs15+ | bigint | 是 | 是 | 最近改变文件状态的时间，表示距1970年1月1日0时0分0秒的纳秒数。 |
| location11+ | [LocationType](js-apis-file-fs.md#locationtype11) | 是 | 否 | 文件的位置，表示该文件是本地文件或者云端文件。 |

说明

Stat中部分属性仅支持普通文件获取，开发者可通过[isFile()](js-apis-file-fs.md#isfile)接口判断文件是否为普通文件。

### isBlockDevice

PhonePC/2in1TabletTVWearable

isBlockDevice(): boolean

用于判断文件是否是块特殊文件。一个块特殊文件只能以块为粒度进行访问，且访问的时候带缓存。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是块特殊设备。true：是块特殊设备；false：不是块特殊设备。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let isBLockDevice = fileIo.statSync(filePath).isBlockDevice();
```

### isCharacterDevice

PhonePC/2in1TabletTVWearable

isCharacterDevice(): boolean

判断文件是否为字符特殊文件。字符特殊设备支持随机访问，且访问时无缓存。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是字符特殊设备。true：是字符特殊设备；false：不是字符特殊设备。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let isCharacterDevice = fileIo.statSync(filePath).isCharacterDevice();
```

### isDirectory

PhonePC/2in1TabletTVWearable

isDirectory(): boolean

判断文件是否为目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是目录。true：是目录；false：不是目录。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let dirPath = pathDir + "/test";
2. let isDirectory = fileIo.statSync(dirPath).isDirectory();
```

### isFIFO

PhonePC/2in1TabletTVWearable

isFIFO(): boolean

用于判断文件是否是命名管道（有时也称为FIFO）。命名管道通常用于进程间通信。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是 FIFO。true：是FIFO；false：不是FIFO。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let isFIFO = fileIo.statSync(filePath).isFIFO();
```

### isFile

PhonePC/2in1TabletTVWearable

isFile(): boolean

用于判断文件是否是普通文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是普通文件。true：是普通文件；false：不是普通文件。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let isFile = fileIo.statSync(filePath).isFile();
```

### isSocket

PhonePC/2in1TabletTVWearable

isSocket(): boolean

判断文件是否是套接字。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是套接字。true：是套接字；false：不是套接字。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let isSocket = fileIo.statSync(filePath).isSocket();
```

### isSymbolicLink

PhonePC/2in1TabletTVWearable

isSymbolicLink(): boolean

判断文件是否为符号链接。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是符号链接。true：是符号链接；false：不是符号链接。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let isSymbolicLink = fileIo.statSync(filePath).isSymbolicLink();
```

## Stream

PhonePC/2in1TabletTVWearable

文件流，在调用Stream的方法前，需要先通过[fileIo.createStream](js-apis-file-fs.md#fileiocreatestream)方法或者[fileIo.fdopenStream](js-apis-file-fs.md#fileiofdopenstream)（同步或异步）来构建一个Stream实例。

### close

PhonePC/2in1TabletTVWearable

close(): Promise<void>

关闭文件流，使用promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let stream = fileIo.createStreamSync(filePath, "r+");
5. stream.close().then(() => {
6. console.info(`Succeeded in closing file stream.`);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to close file stream. Code: ${err.code}, message: ${err.message}`);
9. });
```

### close

PhonePC/2in1TabletTVWearable

close(callback: AsyncCallback<void>): void

异步关闭文件流，使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 异步关闭文件流之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let stream = fileIo.createStreamSync(filePath, "r+");
5. stream.close((err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to close stream. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info(`Succeeded in closing stream.`);
10. }
11. });
```

### closeSync

PhonePC/2in1TabletTVWearable

closeSync(): void

同步关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let stream = fileIo.createStreamSync(filePath, "r+");
3. stream.closeSync();
```

### flush

PhonePC/2in1TabletTVWearable

flush(): Promise<void>

刷新文件流，使用promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。返回表示异步刷新文件流的结果。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let stream = fileIo.createStreamSync(filePath, "r+");
5. stream.flush().then(() => {
6. console.info(`Succeeded in flushing.`);
7. stream.close();
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to flush. Code: ${err.code}, message: ${err.message}`);
10. });
```

### flush

PhonePC/2in1TabletTVWearable

flush(callback: AsyncCallback<void>): void

异步刷新文件流，使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 异步刷新文件流后的回调函数。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let stream = fileIo.createStreamSync(filePath, "r+");
5. stream.flush((err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to flush stream. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info(`Succeeded in flushing.`);
10. stream.close();
11. }
12. });
```

### flushSync

PhonePC/2in1TabletTVWearable

flushSync(): void

同步刷新文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let stream = fileIo.createStreamSync(filePath, "r+");
3. stream.flushSync();
4. stream.close();
```

### write

PhonePC/2in1TabletTVWearable

write(buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>

将数据写入流文件，使用promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](js-apis-file-fs.md#writeoptions11) | 否 | 支持如下选项：  - length，number类型，表示期望写入数据的长度，单位为Byte。默认缓冲区长度。  - offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。  - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回实际写入的长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { WriteOptions } from '@kit.CoreFileKit';

4. let filePath = pathDir + "/test.txt";
5. let stream = fileIo.createStreamSync(filePath, "r+");
6. let writeOption: WriteOptions = {
7. offset: 5,
8. length: 5,
9. encoding: 'utf-8'
10. };
11. stream.write("hello, world", writeOption).then((number: number) => {
12. console.info(`Succeeded in writing, size is: ${number}`);
13. stream.close();
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to write. Code: ${err.code}, message: ${err.message}`);
16. });
```

### write

PhonePC/2in1TabletTVWearable

write(buffer: ArrayBuffer | string, options?: WriteOptions, callback: AsyncCallback<number>): void

将数据写入流文件，使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](js-apis-file-fs.md#writeoptions11) | 否 | 支持如下选项：  - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。  - offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。  - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 |
| callback | AsyncCallback<number> | 是 | 异步写入完成后执行的回调函数。返回实际写入的数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { WriteOptions } from '@kit.CoreFileKit';

4. let filePath = pathDir + "/test.txt";
5. let stream = fileIo.createStreamSync(filePath, "r+");
6. let writeOption: WriteOptions = {
7. offset: 5,
8. length: 5,
9. encoding: 'utf-8'
10. };
11. stream.write("hello, world", writeOption, (err: BusinessError, bytesWritten: number) => {
12. if (err) {
13. console.error(`Failed to write stream. Code: ${err.code}, message: ${err.message}`);
14. } else {
15. if (bytesWritten) {
16. console.info(`Succeeded in writing, size is: ${bytesWritten}`);
17. }
18. }
19. stream.close();
20. });
```

### writeSync

PhonePC/2in1TabletTVWearable

writeSync(buffer: ArrayBuffer | string, options?: WriteOptions): number

以同步方法将数据写入流文件。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](js-apis-file-fs.md#writeoptions11) | 否 | 支持如下选项：  - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。  - offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。  - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际写入的长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { WriteOptions } from '@kit.CoreFileKit';

3. let filePath = pathDir + "/test.txt";
4. let stream = fileIo.createStreamSync(filePath,"r+");
5. let writeOption: WriteOptions = {
6. offset: 5,
7. length: 5,
8. encoding: 'utf-8'
9. };
10. let num = stream.writeSync("hello, world", writeOption);
11. stream.close();
```

### read

PhonePC/2in1TabletTVWearable

read(buffer: ArrayBuffer, options?: ReadOptions): Promise<number>

从流文件读取数据，使用promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | [ReadOptions](js-apis-file-fs.md#readoptions11) | 否 | 支持如下选项：  - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。  - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回读取的结果，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { buffer } from '@kit.ArkTS';
3. import { ReadOptions } from '@kit.CoreFileKit';

5. let filePath = pathDir + "/test.txt";
6. let stream = fileIo.createStreamSync(filePath, "r+");
7. let arrayBuffer = new ArrayBuffer(4096);
8. let readOption: ReadOptions = {
9. offset: 5,
10. length: 5
11. };
12. stream.read(arrayBuffer, readOption).then((readLen: number) => {
13. let buf = buffer.from(arrayBuffer, 0, readLen);
14. console.info(`Succeeded in reading data, the content of file is: ${buf.toString()}`);
15. stream.close();
16. }).catch((err: BusinessError) => {
17. console.error(`Failed to read data. Code: ${err.code}, message: ${err.message}`);
18. });
```

### read

PhonePC/2in1TabletTVWearable

read(buffer: ArrayBuffer, options?: ReadOptions, callback: AsyncCallback<number>): void

从流文件读取数据，使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | [ReadOptions](js-apis-file-fs.md#readoptions11) | 否 | 支持如下选项：  - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。  - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。 |
| callback | AsyncCallback<number> | 是 | 异步读取完成后的回调。返回读取的结果，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { buffer } from '@kit.ArkTS';
3. import { ReadOptions } from '@kit.CoreFileKit';

5. let filePath = pathDir + "/test.txt";
6. let stream = fileIo.createStreamSync(filePath, "r+");
7. let arrayBuffer = new ArrayBuffer(4096);
8. let readOption: ReadOptions = {
9. offset: 5,
10. length: 5
11. };
12. stream.read(arrayBuffer, readOption, (err: BusinessError, readLen: number) => {
13. if (err) {
14. console.error(`Failed to read stream. Code: ${err.code}, message: ${err.message}`);
15. } else {
16. let buf = buffer.from(arrayBuffer, 0, readLen);
17. console.info(`Succeeded in reading data, the content of file is: ${buf.toString()}`);
18. stream.close();
19. }
20. });
```

### readSync

PhonePC/2in1TabletTVWearable

readSync(buffer: ArrayBuffer, options?: ReadOptions): number

以同步方法从流文件读取数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | [ReadOptions](js-apis-file-fs.md#readoptions11) | 否 | 支持如下选项：  - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。  - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际读取的长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { ReadOptions } from '@kit.CoreFileKit';

3. let filePath = pathDir + "/test.txt";
4. let stream = fileIo.createStreamSync(filePath, "r+");
5. let readOption: ReadOptions = {
6. offset: 5,
7. length: 5
8. };
9. let buf = new ArrayBuffer(4096);
10. let num = stream.readSync(buf, readOption);
11. stream.close();
```

## File

PhonePC/2in1TabletTVWearable

由open接口打开的File对象。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fd | number | 是 | 否 | 打开的文件描述符。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| path10+ | string | 是 | 否 | 文件路径。 |
| name10+ | string | 是 | 否 | 文件名。 |

### getParent11+

PhonePC/2in1TabletTVWearable

getParent(): string

获取File对象对应文件父目录。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回父目录路径。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
3. console.info(`Succeeded in getting parent path, the parent path is: ${file.getParent()}`);
4. fileIo.closeSync(file);
```

### lock

PhonePC/2in1TabletTVWearable

lock(exclusive?: boolean): Promise<void>

对文件阻塞式施加共享锁或独占锁，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exclusive | boolean | 否 | 是否施加独占锁，默认false。true：施加独占锁；false：不施加独占锁。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
5. file.lock(true).then(() => {
6. console.info(`Succeeded in locking file.`);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to lock file. Code: ${err.code}, message: ${err.message}`);
9. }).finally(() => {
10. fileIo.closeSync(file);
11. });
```

### lock

PhonePC/2in1TabletTVWearable

lock(exclusive?: boolean, callback: AsyncCallback<void>): void

对文件阻塞式施加共享锁或独占锁，使Callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exclusive | boolean | 否 | 是否施加独占锁，默认false。true：施加独占锁；false：不施加独占锁。 |
| callback | AsyncCallback<void> | 是 | 异步文件上锁之后的回调。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let filePath = pathDir + "/test.txt";
4. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
5. file.lock(true, (err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to lock file. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info(`Succeeded in locking file.`);
10. }
11. fileIo.closeSync(file);
12. });
```

### tryLock

PhonePC/2in1TabletTVWearable

tryLock(exclusive?: boolean): void

文件非阻塞式施加共享锁或独占锁。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exclusive | boolean | 否 | 是否施加独占锁，默认false。true：施加独占锁；false：不施加独占锁。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
3. file.tryLock(true);
4. console.info(`Succeeded in locking file.`);
5. fileIo.closeSync(file);
```

### unlock

PhonePC/2in1TabletTVWearable

unlock(): void

以同步方式解锁文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
3. file.tryLock(true);
4. file.unlock();
5. console.info(`Succeeded in unlocking file.`);
6. fileIo.closeSync(file);
```

## fileIo.DfsListeners12+

PhonePC/2in1TabletTVWearable

事件监听类。创建DFSListener对象，用于监听分布式文件系统状态。

**系统能力**：SystemCapability.FileManagement.File.FileIO

### onStatus12+

PhonePC/2in1TabletTVWearable

onStatus(networkId: string, status: number): void;

事件回调类。参数由[connectDfs](js-apis-file-fs.md#fileioconnectdfs12)传入。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | string | 是 | 设备的网络Id。 |
| status | number | 是 | 分布式文件系统的状态码（以connectDfs回调onStatus的特定错误码作为入参）。触发场景为connectDfs调用过程中出现对端设备异常，对应错误码为：  - [13900046](errorcode-filemanagement.md#section13900046-软件造成连接中断)：软件造成连接中断。 |

## RandomAccessFile10+

PhonePC/2in1TabletTVWearable

随机读写文件流。在调用RandomAccessFile的方法前，需要先通过createRandomAccessFile()方法（同步或异步）来构建一个RandomAccessFile实例。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fd | number | 是 | 否 | 打开的文件描述符。 |
| filePointer | number | 是 | 否 | RandomAccessFile对象的偏移指针，单位为Byte。 |

### setFilePointer10+

PhonePC/2in1TabletTVWearable

setFilePointer(filePointer:number): void

设置文件偏移指针。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePointer | number | 是 | RandomAccessFile对象的偏移指针，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
3. randomAccessFile.setFilePointer(1);
4. randomAccessFile.close();
```

### close10+

PhonePC/2in1TabletTVWearable

close(): void

以同步方式关闭RandomAccessFile对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
3. randomAccessFile.close();
```

### write10+

PhonePC/2in1TabletTVWearable

write(buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>

将数据写入文件，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](js-apis-file-fs.md#writeoptions11) | 否 | 支持如下选项：  - length，number类型，表示期望写入数据的长度，单位为Byte。默认缓冲区长度。  - offset，number类型，表示期望写入文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。  - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回实际写入的长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { WriteOptions } from '@kit.CoreFileKit';

4. let filePath = pathDir + "/test.txt";
5. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
6. let randomAccessFile = fileIo.createRandomAccessFileSync(file);
7. let bufferLength: number = 4096;
8. let writeOption: WriteOptions = {
9. offset: 1,
10. length: 5,
11. encoding: 'utf-8'
12. };
13. let arrayBuffer = new ArrayBuffer(bufferLength);
14. randomAccessFile.write(arrayBuffer, writeOption).then((bytesWritten: number) => {
15. console.info(`Succeeded in writing, bytes written: ${bytesWritten}`);
16. }).catch((err: BusinessError) => {
17. console.error(`Failed to write. Code: ${err.code}, message: ${err.message}`);
18. }).finally(() => {
19. randomAccessFile.close();
20. fileIo.closeSync(file);
21. });
```

### write10+

PhonePC/2in1TabletTVWearable

write(buffer: ArrayBuffer | string, options?: WriteOptions, callback: AsyncCallback<number>): void

将数据写入文件，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](js-apis-file-fs.md#writeoptions11) | 否 | 支持如下选项：  - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认为缓冲区长度。  - offset，number类型，表示期望写入文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。  - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 |
| callback | AsyncCallback<number> | 是 | 异步写入完成后执行的回调函数。返回实际写入数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { WriteOptions } from '@kit.CoreFileKit';

4. let filePath = pathDir + "/test.txt";
5. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
6. let randomAccessFile = fileIo.createRandomAccessFileSync(file);
7. let bufferLength: number = 4096;
8. let writeOption: WriteOptions = {
9. offset: 1,
10. length: bufferLength,
11. encoding: 'utf-8'
12. };
13. let arrayBuffer = new ArrayBuffer(bufferLength);
14. randomAccessFile.write(arrayBuffer, writeOption, (err: BusinessError, bytesWritten: number) => {
15. if (err) {
16. console.error(`Failed to write. Code: ${err.code}, message: ${err.message}`);
17. } else {
18. if (bytesWritten) {
19. console.info(`Succeeded in writing, size is: ${bytesWritten}`);
20. }
21. }
22. randomAccessFile.close();
23. fileIo.closeSync(file);
24. });
```

### writeSync10+

PhonePC/2in1TabletTVWearable

writeSync(buffer: ArrayBuffer | string, options?: WriteOptions): number

以同步方法将数据写入文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](js-apis-file-fs.md#writeoptions11) | 否 | 支持如下选项：  - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。  - offset，number类型，表示期望写入文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。  - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际写入的长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { WriteOptions } from '@kit.CoreFileKit';

3. let filePath = pathDir + "/test.txt";
4. let randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
5. let writeOption: WriteOptions = {
6. offset: 5,
7. length: 5,
8. encoding: 'utf-8'
9. };
10. let bytesWritten = randomAccessFile.writeSync("hello, world", writeOption);
11. randomAccessFile.close();
```

### read10+

PhonePC/2in1TabletTVWearable

read(buffer: ArrayBuffer, options?: ReadOptions): Promise<number>

从文件读取数据，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | [ReadOptions](js-apis-file-fs.md#readoptions11) | 否 | 支持如下选项：  - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认为缓冲区长度。  - offset，number类型，表示期望读取文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始读。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回读取的结果，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ReadOptions } from '@kit.CoreFileKit';

4. let filePath = pathDir + "/test.txt";
5. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
6. let randomAccessFile = fileIo.createRandomAccessFileSync(file);
7. let bufferLength: number = 4096;
8. let readOption: ReadOptions = {
9. offset: 1,
10. length: 5
11. };
12. let arrayBuffer = new ArrayBuffer(bufferLength);
13. randomAccessFile.read(arrayBuffer, readOption).then((readLength: number) => {
14. console.info(`Succeeded in reading, read length: ${readLength}`);
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
17. }).finally(() => {
18. randomAccessFile.close();
19. fileIo.closeSync(file);
20. });
```

### read10+

PhonePC/2in1TabletTVWearable

read(buffer: ArrayBuffer, options?: ReadOptions, callback: AsyncCallback<number>): void

从文件读取数据，使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | [ReadOptions](js-apis-file-fs.md#readoptions11) | 否 | 支持如下选项：  - length，number类型，表示读取数据的长度，单位为Byte。可选，默认为缓冲区长度。  - offset，number类型，表示读取文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从filePointer开始读。 |
| callback | AsyncCallback<number> | 是 | 异步读取完成后的回调。返回实际读取的数据长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ReadOptions } from '@kit.CoreFileKit';

4. let filePath = pathDir + "/test.txt";
5. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
6. let randomAccessFile = fileIo.createRandomAccessFileSync(file);
7. let length: number = 20;
8. let readOption: ReadOptions = {
9. offset: 1,
10. length: 5
11. };
12. let arrayBuffer = new ArrayBuffer(length);
13. randomAccessFile.read(arrayBuffer, readOption, (err: BusinessError, readLength: number) => {
14. if (err) {
15. console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
16. } else {
17. if (readLength) {
18. console.info(`Succeeded in reading, size is: ${readLength}`);
19. }
20. }
21. randomAccessFile.close();
22. fileIo.closeSync(file);
23. });
```

### readSync10+

PhonePC/2in1TabletTVWearable

readSync(buffer: ArrayBuffer, options?: ReadOptions): number

以同步方法从文件读取数据。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | [ReadOptions](js-apis-file-fs.md#readoptions11) | 否 | 支持如下选项：  - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。  - offset，number类型，表示期望读取文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始读。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际读取的长度，单位为Byte。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
3. let randomAccessFile = fileIo.createRandomAccessFileSync(file);
4. let length: number = 4096;
5. let arrayBuffer = new ArrayBuffer(length);
6. let readLength = randomAccessFile.readSync(arrayBuffer);
7. randomAccessFile.close();
8. fileIo.closeSync(file);
```

### getReadStream12+

PhonePC/2in1TabletTVWearable

getReadStream(): ReadStream

获取当前 RandomAccessFile 的一个 ReadStream 实例。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ReadStream](js-apis-file-fs.md#readstream12) | 文件可读流。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. const filePath = pathDir + "/test.txt";
2. const randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
3. const rs = randomAccessFile.getReadStream();
4. rs.close();
5. randomAccessFile.close();
```

### getWriteStream12+

PhonePC/2in1TabletTVWearable

getWriteStream(): WriteStream

获取当前 RandomAccessFile 的一个 WriteStream 实例。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WriteStream](js-apis-file-fs.md#writestream12) | 文件可写流。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. const filePath = pathDir + "/test.txt";
2. const randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
3. const ws = randomAccessFile.getWriteStream();
4. ws.close();
5. randomAccessFile.close();
```

## Watcher10+

PhonePC/2in1TabletTVWearable

文件目录变化监听对象。由createWatcher接口获得。

### start10+

PhonePC/2in1TabletTVWearable

start(): void

开启监听。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let watcher = fileIo.createWatcher(filePath, 0xfff, () => {});
3. watcher.start();
4. watcher.stop();
```

### stop10+

PhonePC/2in1TabletTVWearable

stop(): void

停止监听并移除Watcher对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. let filePath = pathDir + "/test.txt";
2. let watcher = fileIo.createWatcher(filePath, 0xfff, () => {});
3. watcher.start();
4. watcher.stop();
```

## OpenMode

PhonePC/2in1TabletTVWearable

open接口flags参数常量。文件打开标签。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| READ\_ONLY | number | 0o0 | 只读打开。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| WRITE\_ONLY | number | 0o1 | 只写打开。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| READ\_WRITE | number | 0o2 | 读写打开。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| CREATE | number | 0o100 | 若文件不存在，则创建文件。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| TRUNC | number | 0o1000 | 如果文件存在且以只写或读写的方式打开，则将其长度裁剪为零。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| APPEND | number | 0o2000 | 以追加方式打开，后续写将追加到文件末尾。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| NONBLOCK | number | 0o4000 | 如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。 |
| DIR | number | 0o200000 | 如果path不指向目录，则出错。 |
| NOFOLLOW | number | 0o400000 | 如果path指向符号链接，则出错。 |
| SYNC | number | 0o4010000 | 以同步IO的方式打开文件。 |

## Filter10+

PhonePC/2in1TabletTVWearable

文件过滤配置项，支持listFile接口使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| suffix | Array<string> | 否 | 是 | 文件后缀名完全匹配，各个关键词OR关系。 |
| displayName | Array<string> | 否 | 是 | 文件名模糊匹配，各个关键词OR关系。当前仅支持通配符\*。 |
| mimeType | Array<string> | 否 | 是 | mime类型完全匹配，各个关键词OR关系。预留字段，暂不支持使用。 |
| fileSizeOver | number | 否 | 是 | 文件大小匹配，大于指定大小的文件，单位为Byte。 |
| lastModifiedAfter | number | 否 | 是 | 文件最近修改时间匹配，在指定时间点及之后的文件。 |
| excludeMedia | boolean | 否 | 是 | 是否排除Media中已有的文件。true：排除Media中已有的文件；false：不排除Media中已有的文件。 |

## ConflictFiles10+

PhonePC/2in1TabletTVWearable

冲突文件信息，支持copyDir及moveDir接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| srcFile | string | 源冲突文件路径。 |
| destFile | string | 目标冲突文件路径。 |

## Options11+

PhonePC/2in1TabletTVWearable

可选项类型，支持readLines接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| encoding | string | 文件编码方式。可选项。 |

## WhenceType11+

PhonePC/2in1TabletTVWearable

枚举，文件偏移指针相对偏移位置类型，支持lseek接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SEEK\_SET | 0 | 文件起始位置处。 |
| SEEK\_CUR | 1 | 当前文件偏移指针位置处。 |
| SEEK\_END | 2 | 文件末尾位置处。 |

## LocationType11+

PhonePC/2in1TabletTVWearable

枚举，文件位置，表示该文件是否在本地或者云端存在。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOCAL | 1 | 文件在本地存在。 |
| CLOUD | 2 | 文件在云端存在。 |

## AccessModeType12+

PhonePC/2in1TabletTVWearable

枚举，表示需要校验的具体权限。若不填，默认校验文件是否存在。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXIST | 0 | 文件是否存在。 |
| WRITE | 2 | 文件是否具有写入权限。 |
| READ | 4 | 文件是否具有读取权限。 |
| READ\_WRITE | 6 | 文件是否具有读写权限。 |

## AccessFlagType12+

PhonePC/2in1TabletTVWearable

枚举，表示需要校验的文件位置。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOCAL | 0 | 文件是否在本地。 |

## ReadOptions11+

PhonePC/2in1TabletTVWearable

可选项类型，支持read接口使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 是 | 期望读取文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始读。 |
| length | number | 否 | 是 | 期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。 |

## ReadTextOptions11+

PhonePC/2in1TabletTVWearable

可选项类型，支持readText接口使用，ReadTextOptions继承至[ReadOptions](js-apis-file-fs.md#readoptions11)。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 是 | 期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。 |
| length | number | 否 | 是 | 期望读取数据的长度，单位为Byte。可选，默认文件长度。 |
| encoding | string | 否 | 是 | 当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |

## WriteOptions11+

PhonePC/2in1TabletTVWearable

可选项类型，支持write接口使用，WriteOptions继承至[Options](js-apis-file-fs.md#options11)。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 是 | 期望写入文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| length | number | 否 | 是 | 期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| encoding | string | 否 | 是 | 当数据是string类型时有效，表示数据的编码方式。默认 'utf-8'。仅支持 'utf-8'。 |

## ListFileOptions11+

PhonePC/2in1TabletTVWearable

可选项类型，支持listFile接口使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| recursion | boolean | 否 | 是 | 是否递归子目录下文件名。可选，默认为false。当recursion为false时，返回当前目录下满足过滤要求的文件名及目录名。当recursion为true时，返回此目录下所有满足过滤要求的文件的相对路径（以/开头）。 |
| listNum | number | 否 | 是 | 列出文件名数量。可选，当设置0时，列出所有文件，默认为0。 |
| filter | [Filter](js-apis-file-fs.md#filter10) | 否 | 是 | 文件过滤配置项。 可选，设置过滤条件。 |

## ReadStream12+

PhonePC/2in1TabletTVWearable

文件可读流，需要先通过[fileIo.createReadStream](js-apis-file-fs.md#fileiocreatereadstream12)方法来构建一个ReadStream实例。ReadStream继承自数据流基类[stream.Readable](js-apis-stream.md#readable)。

**规格**：ReadStream读到的数据为解码后的字符串，其编码格式当前仅支持'utf-8'。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bytesRead | number | 是 | 否 | 可读流已经读取的字节数。 |
| path | string | 是 | 否 | 当前可读流对应的文件路径。 |

### seek12+

PhonePC/2in1TabletTVWearable

seek(offset: number, whence?: WhenceType): number

调整可读流偏移指针位置。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 相对偏移位置，单位为Byte。 |
| whence | [WhenceType](js-apis-file-fs.md#whencetype11) | 否 | 偏移指针相对位置类型。默认值：SEEK\_SET，文件起始位置处。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前可读流偏移指针位置（相对于文件头的偏移量，单位为Byte）。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. const filePath = pathDir + "/test.txt";
2. const rs = fileIo.createReadStream(filePath);
3. const curOff = rs.seek(5, fileIo.WhenceType.SEEK_SET);
4. console.info(`Succeeded in seeking, current offset is ${curOff}`);
5. rs.close();
```

### close12+

PhonePC/2in1TabletTVWearable

close(): void

关闭可读流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. const filePath = pathDir + "/test.txt";
2. const rs = fileIo.createReadStream(filePath);
3. rs.close();
```

## WriteStream12+

PhonePC/2in1TabletTVWearable

文件可写流，需要先通过[fileIo.createWriteStream](js-apis-file-fs.md#fileiocreatewritestream12)方法来构建一个WriteStream实例。WriteStream继承自数据流基类[stream.Writable](js-apis-stream.md#writable)。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bytesWritten | number | 是 | 否 | 可写流已经写入的字节数。 |
| path | string | 是 | 否 | 当前可写流对应的文件路径。 |

### seek12+

PhonePC/2in1TabletTVWearable

seek(offset: number, whence?: WhenceType): number;

调整可写流的偏移指针位置。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 相对偏移位置，单位为Byte。 |
| whence | [WhenceType](js-apis-file-fs.md#whencetype11) | 否 | 偏移指针相对位置类型。默认值：SEEK\_SET，文件起始位置处。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前可写流偏移指针位置（相对于文件头的偏移量，单位为Byte）。 |

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)和[通用错误码](errorcode-universal.md)。

**示例：**

```
1. const filePath = pathDir + "/test.txt";
2. const ws = fileIo.createWriteStream(filePath);
3. const curOff = ws.seek(5, fileIo.WhenceType.SEEK_SET);
4. console.info(`Succeeded in seeking, current offset is ${curOff}`);
5. ws.close();
```

### close12+

PhonePC/2in1TabletTVWearable

close(): void

关闭可写流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](errorcode-filemanagement.md#基础文件io错误码)。

**示例：**

```
1. const filePath = pathDir + "/test.txt";
2. const ws = fileIo.createWriteStream(filePath);
3. ws.close();
```

## RandomAccessFileOptions12+

PhonePC/2in1TabletTVWearable

可选项类型，支持 createRandomAccessFile 接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 是 | 表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。 |
| end | number | 否 | 是 | 表示期望读取结束的位置，单位为Byte。可选，默认文件末尾。 |

## ReadStreamOptions12+

PhonePC/2in1TabletTVWearable

可选项类型，支持 createReadStream 接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 是 | 表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。 |
| end | number | 否 | 是 | 表示期望读取结束的位置，单位为Byte。可选，默认文件末尾。 |

## WriteStreamOptions12+

PhonePC/2in1TabletTVWearable

可选项类型，支持 createWriteStream 接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 是 | 表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。 |
| mode | number | 否 | 是 | 创建文件可写流的[选项](js-apis-file-fs.md#openmode)，必须指定如下选项中的一个，默认只写方式创建：  - OpenMode.READ\_ONLY(0o0)：只读。  - OpenMode.WRITE\_ONLY(0o1)：只写。  - OpenMode.READ\_WRITE(0o2)：读写。  给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：  - OpenMode.CREATE(0o100)：若文件不存在，则创建文件。  - OpenMode.TRUNC(0o1000)：如果文件存在且文件具有写权限，则将其长度裁剪为零。  - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到文件末尾。  - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。  - OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。  - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。  - OpenMode.SYNC(0o4010000)：以同步IO的方式打开文件。 |
