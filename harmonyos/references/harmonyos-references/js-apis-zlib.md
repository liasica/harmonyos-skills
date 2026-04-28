---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-zlib
title: @ohos.zlib (Zip模块)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 数据文件处理 > @ohos.zlib (Zip模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:65968d143da42cb7acf6f4517e9e400c2a33176074c06efbd87c270392574467
---

本模块提供压缩解压缩文件的能力。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { zlib } from '@kit.BasicServicesKit';
```

## zlib.zipFile(deprecated)

PhonePC/2in1TabletTVWearable

zipFile(inFile: string, outFile: string, options: Options): Promise<void>

压缩接口，压缩完成后返回执行结果。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[zlib.compressFile](js-apis-zlib.md#zlibcompressfile9)替代。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inFile | string | 是 | 指定压缩的文件夹路径或者文件路径，路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](js-apis-inner-app-context.md)，[Stage模型](js-apis-inner-application-context.md)。 |
| outFile | string | 是 | 指定压缩结果的文件路径（文件的扩展名zip）。 |
| options | [Options](js-apis-zlib.md#options) | 是 | 压缩的可选参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**示例：**

```
1. // 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
2. import { zlib, BusinessError } from '@kit.BasicServicesKit';

4. let inFile = '/data/storage/el2/base/temp/filename.xxx';
5. let outFile = '/data/storage/el2/base/temp/xxx.zip';
6. let options: zlib.Options = {
7. level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
8. memLevel: zlib.MemLevel.MEM_LEVEL_DEFAULT,
9. strategy: zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY
10. };

12. zlib.zipFile(inFile, outFile, options).then((data: void) => {
13. console.info('zipFile result is ' + JSON.stringify(data));
14. }).catch((err: BusinessError) => {
15. console.error('error is ' + JSON.stringify(err));
16. });
```

## zlib.unzipFile(deprecated)

PhonePC/2in1TabletTVWearable

unzipFile(inFile:string, outFile:string, options: Options): Promise<void>

解压文件，解压完成后返回执行结果。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[zlib.decompressFile](js-apis-zlib.md#zlibdecompressfile9)替代。

传入的压缩包内部文件或者文件夹名称不能包含“../”，否则会返回-1错误码。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inFile | string | 是 | 指定的待解压缩文件的文件路径，路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](js-apis-inner-app-context.md)，[Stage模型](js-apis-inner-application-context.md)。如果待解压的.zip文件中包含中文的文件名或目录名，需使用UTF8进行编码，避免解压时文件名或目录名出现中文乱码。 |
| outFile | string | 是 | 指定的解压文件路径。 |
| options | [Options](js-apis-zlib.md#options) | 是 | 解压的可选参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**示例：**

```
1. // 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
2. import { zlib, BusinessError } from '@kit.BasicServicesKit';

4. let inFile = '/data/storage/el2/base/temp/xxx.zip';
5. let outFile = '/data/storage/el2/base/temp/xxx';
6. let options: zlib.Options = {
7. level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
8. memLevel: zlib.MemLevel.MEM_LEVEL_DEFAULT,
9. strategy: zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY
10. };

12. zlib.unzipFile(inFile, outFile, options).then((data: void) => {
13. console.info('unzipFile result is ' + JSON.stringify(data));
14. }).catch((err: BusinessError) => {
15. console.error('error is ' + JSON.stringify(err));
16. })
```

## zlib.compressFile9+

PhonePC/2in1TabletTVWearable

compressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>): void

压缩文件，压缩的结果。使用callback异步回调。

说明

为了避免路径穿越，从API version 13开始，inFile和outFile传入的参数不允许包含“../”，否则会返回900001、900002错误码。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inFile | string | 是 | 指定压缩的文件夹路径或者文件路径，路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](js-apis-inner-app-context.md)，[Stage模型](js-apis-inner-application-context.md)。待压缩的文件夹不可为空，否则使用[decompressFile](js-apis-zlib.md#zlibdecompressfile9)对压缩后的文件解压时会报错。 |
| outFile | string | 是 | 指定的压缩结果的文件路径。多个线程同时压缩文件时，outFile不能相同。 |
| options | [Options](js-apis-zlib.md#options) | 是 | 压缩的配置参数。 |
| callback | AsyncCallback<void> | 是 | 异步获取压缩结果之后的回调。成功返回null，失败返回错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 900001 | The input source file is invalid. |
| 900002 | The input destination file is invalid. |

**示例：**

```
1. // 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
2. import { zlib, BusinessError } from '@kit.BasicServicesKit';

4. let inFile = '/data/storage/el2/base/temp/filename.xxx';
5. let outFile = '/data/storage/el2/base/temp/xxx.zip';
6. let options: zlib.Options = {
7. level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
8. memLevel: zlib.MemLevel.MEM_LEVEL_DEFAULT,
9. strategy: zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY
10. };

12. try {
13. zlib.compressFile(inFile, outFile, options, (errData: BusinessError) => {
14. if (errData !== null) {
15. console.error(`compressFile errData is errCode:${errData.code}  message:${errData.message}`);
16. } else {
17. console.info(`compressFile success.`);
18. }
19. })
20. } catch (errData) {
21. let code = (errData as BusinessError).code;
22. let message = (errData as BusinessError).message;
23. console.error(`compressFile errData is errCode:${code}  message:${message}`);
24. }
```

## zlib.compressFile9+

PhonePC/2in1TabletTVWearable

compressFile(inFile: string, outFile: string, options: Options): Promise<void>

压缩文件，压缩的结果。使用Promise异步回调。

说明

为了避免路径穿越，从API version 13开始，inFile和outFile传入的参数不允许包含“../”，否则会返回900001、900002错误码。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inFile | string | 是 | 指定压缩的文件夹路径或者文件路径，路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](js-apis-inner-app-context.md)，[Stage模型](js-apis-inner-application-context.md)。待压缩的文件夹不可为空，否则使用[decompressFile](js-apis-zlib.md#zlibdecompressfile9)对压缩后的文件解压时会报错。 |
| outFile | string | 是 | 指定的压缩结果的文件路径。多个线程同时压缩文件时，outFile不能相同。 |
| options | [Options](js-apis-zlib.md#options) | 是 | 压缩的配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 900001 | The input source file is invalid. |
| 900002 | The input destination file is invalid. |

**示例：**

```
1. // 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
2. import { zlib, BusinessError } from '@kit.BasicServicesKit';

4. let inFile = '/data/storage/el2/base/temp/filename.xxx';
5. let outFile = '/data/storage/el2/base/temp/xxx.zip';
6. let options: zlib.Options = {
7. level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
8. memLevel: zlib.MemLevel.MEM_LEVEL_DEFAULT,
9. strategy: zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY
10. };

12. try {
13. zlib.compressFile(inFile, outFile, options).then((data: void) => {
14. console.info('compressFile success. data: ' + JSON.stringify(data));
15. }).catch((errData: BusinessError) => {
16. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
17. })
18. } catch (errData) {
19. let code = (errData as BusinessError).code;
20. let message = (errData as BusinessError).message;
21. console.error(`errData is errCode:${code}  message:${message}`);
22. }
```

## zlib.decompressFile9+

PhonePC/2in1TabletTVWearable

decompressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>): void

解压文件，解压的结果。使用callback异步回调。

说明

为了避免路径穿越，从API version 13开始，inFile和outFile传入的参数不允许包含“../”，否则会返回900001、900002错误码。

传入的压缩包内部文件或者文件夹名称不能包含“../”，否则会返回900003错误码。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inFile | string | 是 | 指定的待解压缩文件的文件路径，文件后缀需要以.zip结尾。文件路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](js-apis-inner-app-context.md)，[Stage模型](js-apis-inner-application-context.md)。如果待解压的.zip文件中包含中文的文件名或目录名，需使用UTF8进行编码，避免解压时文件名或目录名出现中文乱码。 |
| outFile | string | 是 | 指定的解压后的文件夹路径，文件夹目录路径需要在系统中存在，不存在则会解压失败。路径必须为沙箱路径，沙箱路径可以通过context获取，具体方法可参考[application/context（Stage模型）](js-apis-inner-application-context.md)或 [app/context（FA模型）](js-apis-inner-app-context.md)。如果待解压的文件或文件夹在解压后的路径下已经存在，则会直接覆盖同名文件或同名文件夹中的同名文件。多个线程同时解压文件时，outFile不能相同。 |
| options | [Options](js-apis-zlib.md#options) | 是 | 解压的配置参数。 |
| callback | AsyncCallback<void> | 是 | 异步获取解压结果之后的回调。成功返回null，失败返回错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 900001 | The input source file is invalid. |
| 900002 | The input destination file is invalid. |
| 900003 | The input source file is not in ZIP format or is damaged. |

**示例：**

```
1. // 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
2. import { zlib, BusinessError } from '@kit.BasicServicesKit';

4. let inFile = '/data/storage/el2/base/temp/xxx.zip';
5. let outFileDir = '/data/storage/el2/base/temp';
6. let options: zlib.Options = {
7. level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
8. parallel: zlib.ParallelStrategy.PARALLEL_STRATEGY_PARALLEL_DECOMPRESSION
9. };

11. try {
12. zlib.decompressFile(inFile, outFileDir, options, (errData: BusinessError) => {
13. if (errData !== null) {
14. console.error(`decompressFile errData is errCode:${errData.code}  message:${errData.message}`);
15. } else {
16. console.info(`decompressFile success.`);
17. }
18. })
19. } catch (errData) {
20. let code = (errData as BusinessError).code;
21. let message = (errData as BusinessError).message;
22. console.error(`decompressFile errData is errCode:${code}  message:${message}`);
23. }
```

## zlib.decompressFile9+

PhonePC/2in1TabletTVWearable

decompressFile(inFile: string, outFile: string, options?: Options): Promise<void>

解压文件，解压的结果。使用Promise异步回调。

说明

为了避免路径穿越，从API version 13开始，inFile和outFile传入的参数不允许包含“../”，否则会返回900001、900002错误码。

传入的压缩包内部文件或者文件夹名称不能包含“../”，否则会返回900003错误码。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inFile | string | 是 | 指定的待解压缩文件的文件路径，文件后缀需要以.zip结尾。文件路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](js-apis-inner-app-context.md)，[Stage模型](js-apis-inner-application-context.md)。如果待解压的.zip文件中包含中文的文件名或目录名，需使用UTF8进行编码，避免解压时文件名或目录名出现中文乱码。 |
| outFile | string | 是 | 指定的解压后的文件夹路径，文件夹目录路径需要在系统中存在，不存在则会解压失败。路径必须为沙箱路径，沙箱路径可以通过context获取，具体方法可参考[application/context（Stage模型）](js-apis-inner-application-context.md)或 [app/context（FA模型）](js-apis-inner-app-context.md)。如果待解压的文件或文件夹在解压后的路径下已经存在，则会直接覆盖同名文件或同名文件夹中的同名文件。多个线程同时解压文件时，outFile不能相同。 |
| options | [Options](js-apis-zlib.md#options) | 否 | 解压时的配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 900001 | The input source file is invalid. |
| 900002 | The input destination file is invalid. |
| 900003 | The input source file is not in ZIP format or is damaged. |

**示例：**

```
1. // 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
2. import { zlib, BusinessError } from '@kit.BasicServicesKit';

4. let inFile = '/data/storage/el2/base/temp/xxx.zip';
5. let outFileDir = '/data/storage/el2/base/temp';
6. let options: zlib.Options = {
7. level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION
8. };

10. try {
11. zlib.decompressFile(inFile, outFileDir, options).then((data: void) => {
12. console.info('decompressFile success. data: ' + JSON.stringify(data));
13. }).catch((errData: BusinessError) => {
14. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
15. })
16. } catch (errData) {
17. let code = (errData as BusinessError).code;
18. let message = (errData as BusinessError).message;
19. console.error(`errData is errCode:${code}  message:${message}`);
20. }
```

## zlib.decompressFile10+

PhonePC/2in1TabletTVWearable

decompressFile(inFile: string, outFile: string, callback: AsyncCallback<void>): void

解压文件，解压的结果。使用callback异步回调。

说明

为了避免路径穿越，从API version 13开始，inFile和outFile传入的参数不允许包含“../”，否则会返回900001、900002错误码。

传入的压缩包内部文件或者文件夹名称不能包含“../”，否则会返回900003错误码。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inFile | string | 是 | 指定的待解压缩文件的文件路径，文件后缀需要以.zip结尾。文件路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](js-apis-inner-app-context.md)，[Stage模型](js-apis-inner-application-context.md)。如果待解压的.zip文件中包含中文的文件名或目录名，需使用UTF8进行编码，避免解压时文件名或目录名出现中文乱码。 |
| outFile | string | 是 | 指定的解压后的文件夹路径，文件夹目录路径需要在系统中存在，不存在则会解压失败。路径必须为沙箱路径，沙箱路径可以通过context获取，具体方法可参考[application/context（Stage模型）](js-apis-inner-application-context.md)或 [app/context（FA模型）](js-apis-inner-app-context.md)。如果待解压的文件或文件夹在解压后的路径下已经存在，则会直接覆盖同名文件或同名文件夹中的同名文件。多个线程同时解压文件时，outFile不能相同。 |
| callback | AsyncCallback<void> | 是 | 异步获取解压结果之后的回调。成功返回null，失败返回错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 900001 | The input source file is invalid. |
| 900002 | The input destination file is invalid. |
| 900003 | The input source file is not in ZIP format or is damaged. |

**示例：**

```
1. // 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp,也可以通过context获取。
2. import { zlib, BusinessError } from '@kit.BasicServicesKit';

4. let inFile = '/data/storage/el2/base/temp/xxx.zip';
5. let outFileDir = '/data/storage/el2/base/temp';

7. try {
8. zlib.decompressFile(inFile, outFileDir, (errData: BusinessError) => {
9. if (errData !== null) {
10. console.error(`decompressFile failed. code is ${errData.code}, message is ${errData.message}`);
11. } else {
12. console.info(`decompressFile success.`);
13. }
14. })
15. } catch (errData) {
16. let code = (errData as BusinessError).code;
17. let message = (errData as BusinessError).message;
18. console.error(`decompressFile failed. code is ${code}, message is ${message}`);
19. }
```

## zlib.getOriginalSize12+

PhonePC/2in1TabletTVWearable

getOriginalSize(compressedFile: string): Promise<number>

获取压缩文件的原始大小。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| compressedFile | string | 是 | 指定的压缩文件的文件路径，只支持zip格式压缩文件。文件路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](js-apis-inner-app-context.md)，[Stage模型](js-apis-inner-application-context.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回压缩文件的原始大小，单位字节。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 900001 | The input source file is invalid. |
| 900003 | The input source file is not in ZIP format or is damaged. |

**示例：**

```
1. // 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp，也可以通过context获取。
2. import { zlib, BusinessError } from '@kit.BasicServicesKit';

4. let compressedFile = '/data/storage/el2/base/temp/test.zip';

6. try {
7. zlib.getOriginalSize(compressedFile).then((data: number) => {
8. console.info(`getOriginalSize success. getOriginalSize: ${data}`);
9. }).catch((errData: BusinessError) => {
10. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
11. })
12. } catch (errData) {
13. let code = (errData as BusinessError).code;
14. let message = (errData as BusinessError).message;
15. console.error(`errData is errCode:${code}  message:${message}`);
16. }
```

## zlib.compressFiles12+

PhonePC/2in1TabletTVWearable

compressFiles(inFiles: Array<string>, outFile: string, options: Options): Promise<void>

压缩指定的多个文件。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inFiles | Array<string> | 是 | 指定压缩的文件夹路径或者文件路径，路径必须为沙箱路径，沙箱路径可以通过context获取，可参考[FA模型](js-apis-inner-app-context.md)，[Stage模型](js-apis-inner-application-context.md)。待压缩的文件夹不可为空，否则使用[decompressFile](js-apis-zlib.md#zlibdecompressfile9)对压缩后的文件解压时会报错。 |
| outFile | string | 是 | 指定的压缩结果的文件路径。多个线程同时压缩文件时，outFile不能相同。 |
| options | [Options](js-apis-zlib.md#options) | 是 | 压缩的配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 900001 | The input source file is invalid. |
| 900002 | The input destination file is invalid. |

**示例：**

```
1. // 代码中使用的路径需为应用的沙箱路径，如/data/storage/el2/base/temp，也可以通过context获取。
2. import { zlib, BusinessError } from '@kit.BasicServicesKit';

4. let inFile = '/data/storage/el2/base/temp/filename.xxx';
5. let pathDir = 'data/storage/el2/base/temp/xxx';
6. let outFile = '/data/storage/el2/base/temp/xxx.zip';
7. let options: zlib.Options = {
8. level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
9. memLevel: zlib.MemLevel.MEM_LEVEL_DEFAULT,
10. strategy: zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY
11. };

13. try {
14. zlib.compressFiles([inFile, pathDir], outFile, options).then((data: void) => {
15. console.info('compressFiles success. data: ' + JSON.stringify(data));
16. }).catch((errData: BusinessError) => {
17. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
18. })
19. } catch (errData) {
20. let code = (errData as BusinessError).code;
21. let message = (errData as BusinessError).message;
22. console.error(`errData is errCode:${code}  message:${message}`);
23. }
```

## zlib.createChecksum12+

PhonePC/2in1TabletTVWearable

createChecksum(): Promise<Checksum>

创建校验对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Checksum](js-apis-zlib.md#checksum12)> | Promise对象。返回校验对象实例。 |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';

3. zlib.createChecksum().then((data) => {
4. console.info('createChecksum success');
5. })
```

## zlib.createChecksumSync12+

PhonePC/2in1TabletTVWearable

createChecksumSync(): Checksum

创建校验对象。成功时返回Checksum对象实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Checksum](js-apis-zlib.md#checksum12) | 校验对象实例。 |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';

3. let checksum = zlib.createChecksumSync()
```

## Checksum12+

PhonePC/2in1TabletTVWearable

校验对象。

### adler3212+

PhonePC/2in1TabletTVWearable

adler32(adler: number, buf: ArrayBuffer): Promise<number>

计算Adler-32校验和。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| adler | number | 是 | Adler-32校验和的初始值。 |
| buf | ArrayBuffer | 是 | 计算校验和数据缓冲区。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回计算后的Adler-32校验和。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';

3. let str = 'hello world!';
4. let arrayBufferIn = new ArrayBuffer(12);
5. let data = new Uint8Array(arrayBufferIn);

7. for (let i = 0, j = str.length; i < j; i++) {
8. data[i] = str.charCodeAt(i);
9. }

11. let checksum = zlib.createChecksumSync()

13. checksum.adler32(0, arrayBufferIn).then(data => {
14. console.info('adler32 success', data);
15. })
```

### adler32Combine12+

PhonePC/2in1TabletTVWearable

adler32Combine(adler1: number, adler2: number, len2: number): Promise<number>

将两个Adler-32校验和合并。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| adler1 | number | 是 | 第一个要合并的Adler-32校验和。 |
| adler2 | number | 是 | 第二个要合并的Adler-32校验和。 |
| len2 | number | 是 | 第二个Adler-32校验和的数据块的长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回合并后的Adler-32校验和。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(12);
6. let data = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. data[i] = str.charCodeAt(i);
9. }
10. let checksum = zlib.createChecksumSync()
11. let adler1 = 0;
12. let adler2 = 1;
13. await checksum.adler32(0, arrayBufferIn).then(data => {
14. console.info('adler32 success', data);
15. adler1 = data;
16. })
17. await checksum.adler32(1, arrayBufferIn).then(data => {
18. console.info('adler32 success', data);
19. adler2 = data;
20. })
21. await checksum.adler32Combine(adler1, adler2, 12).then((data) => {
22. console.info('adler32Combine success', data);
23. }).catch((errData: BusinessError) => {
24. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
25. })
26. }
```

### crc3212+

PhonePC/2in1TabletTVWearable

crc32(crc: number, buf: ArrayBuffer): Promise<number>

更新CRC-32校验。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| crc | number | 是 | CRC-32校验的初始值。 |
| buf | ArrayBuffer | 是 | 计算校验数据缓冲区。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回更新后的CRC-32校验。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. let str = 'hello world!';
4. let arrayBufferIn = new ArrayBuffer(12);
5. let data = new Uint8Array(arrayBufferIn);

7. for (let i = 0, j = str.length; i < j; i++) {
8. data[i] = str.charCodeAt(i);
9. }

11. let checksum = zlib.createChecksumSync()

13. checksum.crc32(0, arrayBufferIn).then((data) => {
14. console.info('crc32 success', data);
15. }).catch((errData: BusinessError) => {
16. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
17. })
```

### crc32Combine12+

PhonePC/2in1TabletTVWearable

crc32Combine(crc1: number, crc2: number, len2: number): Promise<number>

将两个CRC-32校验合并。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| crc1 | number | 是 | 第一个要合并的CRC-32校验。 |
| crc2 | number | 是 | 第二个要合并的CRC-32校验。 |
| len2 | number | 是 | 第二个CRC-32校验的数据块的长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回合并后的CRC-32校验。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(12);
6. let data = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. data[i] = str.charCodeAt(i);
9. }
10. let checksum = zlib.createChecksumSync()
11. let crc1 = 0;
12. let crc2 = 1;
13. await checksum.crc32(0, arrayBufferIn).then(data => {
14. console.info('crc32 success', data);
15. crc1 = data;
16. })
17. await checksum.crc32(1, arrayBufferIn).then(data => {
18. console.info('crc32 success', data);
19. crc2 = data;
20. })
21. await checksum.crc32Combine(crc1, crc2, 12).then((data) => {
22. console.info('crc32Combine success', data);
23. }).catch((errData: BusinessError) => {
24. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
25. })
26. }
```

### crc6412+

PhonePC/2in1TabletTVWearable

crc64(crc: number, buf: ArrayBuffer): Promise<number>

更新CRC-64校验。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| crc | number | 是 | CRC-64校验的初始值。 |
| buf | ArrayBuffer | 是 | 计算校验数据缓冲区。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回更新后的CRC-64校验。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. let str = 'hello world!';
4. let arrayBufferIn = new ArrayBuffer(12);
5. let data = new Uint8Array(arrayBufferIn);

7. for (let i = 0, j = str.length; i < j; i++) {
8. data[i] = str.charCodeAt(i);
9. }

11. let checksum = zlib.createChecksumSync()

13. checksum.crc64(0, arrayBufferIn).then((data) => {
14. console.info('crc64 success', data);
15. }).catch((errData: BusinessError) => {
16. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
17. })
```

### getCrcTable12+

PhonePC/2in1TabletTVWearable

getCrcTable(): Promise<Array<number>>

输出CRC-32校验表。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象。返回CRC-32校验表。 |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. let checksum = zlib.createChecksumSync()

5. checksum.getCrcTable().then((data) => {
6. console.info('getCrcTable success');
7. }).catch((errData: BusinessError) => {
8. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
9. })
```

### getCrc64Table12+

PhonePC/2in1TabletTVWearable

getCrc64Table(): Promise<Array<number>>

输出CRC-64校验表。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象。返回CRC-64校验表。 |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. let checksum = zlib.createChecksumSync()

5. checksum.getCrc64Table().then((data) => {
6. console.info('getCrc64Table success');
7. }).catch((errData: BusinessError) => {
8. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
9. })
```

## zlib.createZip12+

PhonePC/2in1TabletTVWearable

createZip(): Promise<Zip>

创建压缩解压缩对象实例。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Zip](js-apis-zlib.md#zip12)> | Promise对象。返回压缩解压缩对象实例。 |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. zlib.createZip().then(data => {
4. console.info('createZip success');
5. }).catch((errData: BusinessError) => {
6. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
7. })
```

## zlib.createZipSync12+

PhonePC/2in1TabletTVWearable

createZipSync(): Zip

创建压缩解压缩对象实例，成功时返回压缩解压缩对象实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Zip](js-apis-zlib.md#zip12) | 返回压缩解压缩对象实例。 |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';

3. let zip = zlib.createZipSync();
```

## Zip12+

PhonePC/2in1TabletTVWearable

压缩解压缩对象实例，支持以zlib、deflate、gzip格式对数据进行压缩与解压。

### getZStream12+

PhonePC/2in1TabletTVWearable

getZStream(): Promise<ZStream>

输出流。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ZStream](js-apis-zlib.md#zstream12)> | Promise对象。返回ZStream流。 |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';

3. let zip = zlib.createZipSync();

5. zip.getZStream().then(data => {
6. console.info('getZStream success');
7. })
```

### zlibVersion12+

PhonePC/2in1TabletTVWearable

zlibVersion(): Promise<string>

获取当前链接的zlib库的版本信息。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回当前zlib库的版本信息。 |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';

3. let zip = zlib.createZipSync();

5. zip.zlibVersion().then((data) => {
6. console.info('zlibVersion success')
7. })
```

### zlibCompileFlags12+

PhonePC/2in1TabletTVWearable

zlibCompileFlags(): Promise<number>

返回指示编译时选项的标志。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回指示编译时选项的标志。 |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';

3. let zip = zlib.createZipSync();

5. zip.zlibCompileFlags().then((data) => {
6. console.info('zlibCompileFlags success')
7. })
```

### compress12+

PhonePC/2in1TabletTVWearable

compress(dest: ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<ZipOutputInfo>

将源缓冲区压缩到目标缓冲区。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dest | ArrayBuffer | 是 | 目标缓冲区。 |
| source | ArrayBuffer | 是 | 源数据缓冲区。 |
| sourceLen | number | 否 | 源数据长度。默认值为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ZipOutputInfo](js-apis-zlib.md#zipoutputinfo12)> | Promise对象。返回结果状态和目标缓冲区的总大小。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800007 | The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data. |

**示例：**

```
1. import { util } from '@kit.ArkTS';
2. import { zlib, BusinessError } from '@kit.BasicServicesKit';

4. let str = 'hello world! 你好，世界！';
5. const enc = util.TextEncoder.create('utf-8');
6. const u8 = enc.encodeInto(str);
7. const arrayBufferIn = u8.buffer.slice(u8.byteOffset, u8.byteOffset + u8.byteLength);

9. let arrayBufferOut = new ArrayBuffer(100);
10. let zip = zlib.createZipSync();

12. zip.compress(arrayBufferOut, arrayBufferIn, 20).then((data) => {
13. console.info('compress success:');
14. }).catch((errData: BusinessError) => {
15. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
16. })
```

### compress212+

PhonePC/2in1TabletTVWearable

compress2(dest: ArrayBuffer, source: ArrayBuffer, level: CompressLevel, sourceLen?: number): Promise<ZipOutputInfo>

将源缓冲区压缩到目标缓冲区。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dest | ArrayBuffer | 是 | 目标缓冲区。 |
| source | ArrayBuffer | 是 | 源数据缓冲区。 |
| level | CompressLevel | 是 | 参考[CompressLevel枚举定义](js-apis-zlib.md#compresslevel)。 |
| sourceLen | number | 否 | 源数据长度。默认值为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ZipOutputInfo](js-apis-zlib.md#zipoutputinfo12)> | Promise对象。返回结果状态和目标缓冲区的总大小。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |
| 17800007 | The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data. |

**示例：**

```
1. import { util } from '@kit.ArkTS';
2. import { zlib, BusinessError } from '@kit.BasicServicesKit';

4. let str = 'hello world! 你好，世界！';
5. const enc = util.TextEncoder.create('utf-8');
6. const u8 = enc.encodeInto(str);
7. const arrayBufferIn = u8.buffer.slice(u8.byteOffset, u8.byteOffset + u8.byteLength);

9. let arrayBufferOut = new ArrayBuffer(100);
10. let zip = zlib.createZipSync();

12. zip.compress2(arrayBufferOut, arrayBufferIn, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
13. console.info('compress2 success');
14. }).catch((errData: BusinessError) => {
15. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
16. })
```

### uncompress12+

PhonePC/2in1TabletTVWearable

uncompress(dest:ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<ZipOutputInfo>

将压缩后的数据解压缩为原始的未压缩形式。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dest | ArrayBuffer | 是 | 目标缓冲区。 |
| source | ArrayBuffer | 是 | 源数据缓冲区。 |
| sourceLen | number | 否 | 源数据长度。默认值为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ZipOutputInfo](js-apis-zlib.md#zipoutputinfo12)> | Promise对象。返回结果状态和目标缓冲区的总大小。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800005 | The input data is incorrect. For example, the data does not conform to the zlib compression format, the compressed data is corrupted, or the data is not compressed. |
| 17800007 | The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zip = zlib.createZipSync();
12. await zip.compress(arrayBufferOut, arrayBufferIn, 12).then((data) => {
13. console.info('compress success');
14. }).catch((errData: BusinessError) => {
15. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
16. })
17. await zip.uncompress(arrayBufferIn, arrayBufferOut, 20).then((data) => {
18. console.info('uncompress success');
19. }).catch((errData: BusinessError) => {
20. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
21. })
22. }
```

### uncompress212+

PhonePC/2in1TabletTVWearable

uncompress2(dest: ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<DecompressionOutputInfo>

将压缩后的数据解压缩为原始的未压缩形式。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dest | ArrayBuffer | 是 | 目标缓冲区。 |
| source | ArrayBuffer | 是 | 源数据缓冲区。 |
| sourceLen | number | 否 | 源数据长度。默认值为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DecompressionOutputInfo](js-apis-zlib.md#decompressionoutputinfo12)> | Promise对象。返回结果状态、目标缓冲区的总大小和源数据长度。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800005 | The input data is incorrect. For example, the data does not conform to the zlib compression format, the compressed data is corrupted, or the data is not compressed. |
| 17800007 | The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zip = zlib.createZipSync();
12. await zip.compress2(arrayBufferOut, arrayBufferIn, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
13. console.info('compress2 success');
14. }).catch((errData: BusinessError) => {
15. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
16. })
17. await zip.uncompress2(arrayBufferIn, arrayBufferOut, 20).then((data) => {
18. console.info('uncompress2 success');
19. }).catch((errData: BusinessError) => {
20. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
21. })
22. }
```

### compressBound12+

PhonePC/2in1TabletTVWearable

compressBound(sourceLen: number): Promise<number>

计算返回压缩大小的上限。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sourceLen | number | 是 | 源数据长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回压缩大小的上限。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. let str = 'hello world!';
4. let arrayBufferIn = new ArrayBuffer(str.length);
5. let byteArray = new Uint8Array(arrayBufferIn);

7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }

11. let zip = zlib.createZipSync();

13. zip.compressBound(str.length).then((data) => {
14. console.info('compressBound success')
15. }).catch((errData: BusinessError) => {
16. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
17. })
```

### inflateValidate12+

PhonePC/2in1TabletTVWearable

inflateValidate(strm: ZStream, check: number): Promise<ReturnStatus>

验证压缩流结构内部的校验和。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| check | number | 是 | 预期的校验和。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zip = zlib.createZipSync();
12. await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
13. ).then(data => {
14. console.info('inflateInit success')
15. }).catch((errData: BusinessError) => {
16. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
17. })
18. await zip.inflateValidate({ availableIn: 1 }, 1).then(data => {
19. console.info('inflateValidate success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. }
```

### inflateSyncPoint12+

PhonePC/2in1TabletTVWearable

inflateSyncPoint(strm: ZStream): Promise<ReturnStatus>

查找当前解压缩流的同步点。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zip = zlib.createZipSync();
12. await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
13. ).then(data => {
14. console.info('inflateInit success');
15. }).catch((errData: BusinessError) => {
16. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
17. })
18. await zip.inflateSyncPoint({ availableIn: 1 }).then(data => {
19. console.info('inflateSyncPoint success');
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. }
```

### inflateSync12+

PhonePC/2in1TabletTVWearable

inflateSync(strm: ZStream): Promise<ReturnStatus>

跳过无效的压缩数据，直到找到一个可能的完整刷新点为止。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |
| 17800005 | The input data is incorrect. For example, the data does not conform to the zlib compression format, the compressed data is corrupted, or the data is not compressed. |
| 17800007 | The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello, hello!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zip = zlib.createZipSync();
12. await zip.deflateInit({}, zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION).then((data) => {
13. console.info('deflateInit success')
14. }).catch((errData: BusinessError) => {
15. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
16. })
17. await zip.deflate({ nextIn: arrayBufferIn, availableIn: 3, nextOut: arrayBufferOut, availableOut: 100 }, zlib.CompressFlushMode.FULL_FLUSH).then((data) => {
18. console.info('deflate success')
19. }).catch((errData: BusinessError) => {
20. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
21. })
22. await zip.deflate({ availableIn: 11 }, zlib.CompressFlushMode.FINISH).then((data) => {
23. console.info('deflate success')
24. }).catch((errData: BusinessError) => {
25. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
26. })
27. await zip.deflateEnd({}).then(data => {
28. console.info('deflateEnd success')
29. }).catch((errData: BusinessError) => {
30. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
31. })
32. try {
33. await zip.inflateInit({ nextIn: arrayBufferOut, availableIn: 2 }).then(data => {
34. console.info('inflateInit2 success')
35. })
36. } catch (errData) {
37. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
38. }
39. await zip.inflate({ nextOut: arrayBufferIn, availableOut: 28 }, zlib.CompressFlushMode.NO_FLUSH).then((data) => {
40. console.info('inflate success')
41. }).catch((errData: BusinessError) => {
42. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
43. })
44. await zip.inflateSync({ availableIn: 26 }).then(data => {
45. console.info('inflateSync success');
46. }).catch((errData: BusinessError) => {
47. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
48. })
49. await zip.inflateEnd({ nextOut: arrayBufferOut }).then((data) => {
50. console.info('inflateEnd success')
51. }).catch((errData: BusinessError) => {
52. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
53. })
54. }
```

### inflateResetKeep12+

PhonePC/2in1TabletTVWearable

inflateResetKeep(strm: ZStream): Promise<ReturnStatus>

重置解压缩流的状态，以保留分配的霍夫曼解码树和预设字典。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zip = zlib.createZipSync();
12. await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
13. ).then(data => {
14. console.info('inflateInit success');
15. }).catch((errData: BusinessError) => {
16. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
17. })
18. await zip.inflateResetKeep({ availableIn: 1 }).then(data => {
19. console.info('inflateResetKeep success');
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. }
```

### inflateSetDictionary12+

PhonePC/2in1TabletTVWearable

inflateSetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<ReturnStatus>

使用给定的字典数据初始化当前解压缩流的字典内容。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| dictionary | ArrayBuffer | 是 | 字典数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |
| 17800005 | The input data is incorrect. For example, the data does not conform to the zlib compression format, the compressed data is corrupted, or the data is not compressed. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello, hello!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zip = zlib.createZipSync();
12. let dictionary = 'hello'
13. let dictionarybuf = new ArrayBuffer(dictionary.length);
14. let dictionarybufdata = new Uint8Array(dictionarybuf);
15. for (let i = 0, j = dictionary.length; i < j; i++) {
16. dictionarybufdata[i] = str.charCodeAt(i);
17. }
18. await zip.deflateInit({}, zlib.CompressLevel.COMPRESS_LEVEL_BEST_COMPRESSION).then((data) => {
19. console.info('deflateInit success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
22. })
23. await zip.deflateSetDictionary({}, dictionarybuf).then((data) => {
24. console.info('deflateSetDictionary success')
25. }).catch((errData: BusinessError) => {
26. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
27. })
28. await zip.deflate({ nextIn: arrayBufferIn, availableIn: 14, nextOut: arrayBufferOut, availableOut: 100 }, zlib.CompressFlushMode.FINISH).then((data) => {
29. console.info('deflate success')
30. }).catch((errData: BusinessError) => {
31. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
32. })
33. await zip.deflateEnd({}).then(data => {
34. console.info('deflateEnd success')
35. }).catch((errData: BusinessError) => {
36. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
37. })
38. try {
39. await zip.inflateInit({ nextIn: arrayBufferOut, availableIn: 100 }).then(data => {
40. console.info('inflateInit success')
41. })
42. } catch (errData) {
43. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
44. }
45. await zip.inflate({ nextOut: arrayBufferIn, availableOut: 28 }, zlib.CompressFlushMode.NO_FLUSH).then((data) => {
46. console.info('inflate success')
47. }).catch((errData: BusinessError) => {
48. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
49. })
50. await zip.inflateSetDictionary({}, dictionarybuf).then((data) => {
51. console.info('inflateSetDictionary success')
52. }).catch((errData: BusinessError) => {
53. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
54. })
55. await zip.inflateEnd({ nextOut: arrayBufferOut }).then((data) => {
56. console.info('inflateEnd success')
57. }).catch((errData: BusinessError) => {
58. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
59. })
60. }
```

### inflateReset212+

PhonePC/2in1TabletTVWearable

inflateReset2(strm: ZStream, windowBits: number): Promise<ReturnStatus>

重置指定解压缩流的状态并更新窗口大小配置，以重新开始新的解压操作。不会释放或重新分配内部缓冲区。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| windowBits | number | 是 | 控制内存窗口的大小，并指定数据的格式（zlib、gzip、raw deflate）。取值如下：  zlib格式：[1, 15]。  gzip格式：大于15。  raw deflate格式：[-15, -1]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zip = zlib.createZipSync();
12. await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
13. ).then(data => {
14. console.info('inflateInit success');
15. }).catch((errData: BusinessError) => {
16. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
17. })
18. await zip.inflateReset2({ availableOut: 8 }, 15).then(data => {
19. console.info('inflateReset2 success');
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. }
```

### inflateReset12+

PhonePC/2in1TabletTVWearable

inflateReset(strm: ZStream): Promise<ReturnStatus>

重置指定解压缩流的状态，使其恢复到初始化状态以重新开始新的解压操作。不会释放或重新分配内部缓冲区。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zip = zlib.createZipSync();
12. await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
13. ).then(data => {
14. console.info('inflateInit success');
15. }).catch((errData: BusinessError) => {
16. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
17. })
18. await zip.inflateReset({ availableIn: 1, availableOut: 8 }).then(data => {
19. console.info('inflateReset success');
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. }
```

### inflatePrime12+

PhonePC/2in1TabletTVWearable

inflatePrime(strm: ZStream, bits: number, value: number): Promise<ReturnStatus>

在指定解压缩流中设置初始比特数和比特值，用于在解压流开始时预填充比特缓冲区，以正确处理流起始位置的数据。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| bits | number | 是 | 指定要写入比特缓冲区的比特数。 |
| value | number | 是 | 用于填充比特缓冲区的比特值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zip = zlib.createZipSync();
12. await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
13. ).then(data => {
14. console.info('inflateInit success');
15. }).catch((errData: BusinessError) => {
16. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
17. })
18. await zip.inflatePrime({ nextOut: arrayBufferOut }, 5, 2).then(data => {
19. console.info('inflatePrime success');
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. }
```

### inflateMark12+

PhonePC/2in1TabletTVWearable

inflateMark(strm: ZStream): Promise<number>

用于标记输入数据中的位置以供随机访问。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回位置信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zip = zlib.createZipSync();
12. await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
13. ).then(data => {
14. console.info('inflateInit success');
15. }).catch((errData: BusinessError) => {
16. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
17. })
18. await zip.inflateMark({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }).then(data => {
19. console.info('inflateMark success');
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. }
```

### inflateInit212+

PhonePC/2in1TabletTVWearable

inflateInit2(strm: ZStream, windowBits: number): Promise<ReturnStatus>

初始化解压缩流并设置指定的 windowBits 参数。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| windowBits | number | 是 | 控制内存窗口的大小，并指定数据的格式（zlib、gzip、raw deflate）。取值如下：  zlib格式：[1, 15]。  gzip格式：大于15。  raw deflate格式：[-15, -1]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. let str = 'hello world!';
4. let arrayBufferIn = new ArrayBuffer(str.length);
5. let byteArray = new Uint8Array(arrayBufferIn);

7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }

11. let arrayBufferOut = new ArrayBuffer(100);
12. let zip = zlib.createZipSync();

14. zip.inflateInit2({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }, 28
15. ).then(data => {
16. console.info('inflateInit2 success');
17. }).catch((errData: BusinessError) => {
18. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
19. })
```

### inflateInit12+

PhonePC/2in1TabletTVWearable

inflateInit(strm: ZStream): Promise<ReturnStatus>

初始化解压缩流。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. let str = 'hello world!';
4. let arrayBufferIn = new ArrayBuffer(str.length);
5. let byteArray = new Uint8Array(arrayBufferIn);

7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }

11. let arrayBufferOut = new ArrayBuffer(100);
12. let zip = zlib.createZipSync();

14. zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
15. ).then(data => {
16. console.info('inflateInit success');
17. }).catch((errData: BusinessError) => {
18. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
19. })
```

### inflateGetHeader12+

PhonePC/2in1TabletTVWearable

inflateGetHeader(strm: ZStream, header: GzHeader): Promise<ReturnStatus>

用于在解压缩数据前设置gzip文件头部信息。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| header | [GzHeader](js-apis-zlib.md#gzheader12) | 是 | 从压缩数据流中提取的gzip头信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zip = zlib.createZipSync();
12. await zip.inflateInit2({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }, 28
13. ).then(data => {
14. console.info('inflateInit2 success');
15. }).catch((errData: BusinessError) => {
16. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
17. })
18. await zip.inflateGetHeader({ availableIn: 1, availableOut: 1 }, { isText: true, os: 1, time: 1, xflags: 1, extra: arrayBufferIn, extraLen: 12, name: arrayBufferIn, comment: arrayBufferOut, hcrc: true, done: true }).then(data => {
19. console.info('inflateGetHeader success');
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. }
```

### inflateGetDictionary12+

PhonePC/2in1TabletTVWearable

inflateGetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<DictionaryOutputInfo>

获取当前解压缩流中使用的解压缩字典内容及其长度。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| dictionary | ArrayBuffer | 是 | 接收解压缩字典的实际内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DictionaryOutputInfo](js-apis-zlib.md#dictionaryoutputinfo12)> | Promise对象。返回结果状态和字典的长度。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zip = zlib.createZipSync();
12. await zip.inflateInit2({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }, 28
13. ).then(data => {
14. console.info('inflateInit2 success');
15. }).catch((errData: BusinessError) => {
16. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
17. })
18. await zip.inflateGetDictionary({ nextOut: arrayBufferOut }, arrayBufferOut).then((data) => {
19. console.info('inflateGetDictionary success:')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. }
```

### inflateEnd12+

PhonePC/2in1TabletTVWearable

inflateEnd(strm: ZStream): Promise<ReturnStatus>

解压流的所有动态分配的数据结构都被释放。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zip = zlib.createZipSync();
12. await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
13. ).then(data => {
14. console.info('inflateInit success');
15. }).catch((errData: BusinessError) => {
16. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
17. })
18. await zip.inflate({ availableIn: 8, availableOut: 8 }, 0).then((data) => {
19. console.info('inflate success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. await zip.inflateEnd({ nextOut: arrayBufferOut }).then((data) => {
24. console.info('inflateEnd success')
25. }).catch((errData: BusinessError) => {
26. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
27. })
28. }
```

### inflateCopy12+

PhonePC/2in1TabletTVWearable

inflateCopy(source: Zip): Promise<ReturnStatus>

复制解压流。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | Zip | 是 | 参考[Zip定义](js-apis-zlib.md#zip12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zip = zlib.createZipSync();
12. await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
13. ).then(data => {
14. console.info('inflateInit success');
15. }).catch((errData: BusinessError) => {
16. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
17. })
18. let destZip = zlib.createZipSync();
19. await destZip.inflateCopy(zip).then((data) => {
20. console.info('inflateCopy success')
21. }).catch((errData: BusinessError) => {
22. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
23. })
24. }
```

### inflateCodesUsed12+

PhonePC/2in1TabletTVWearable

inflateCodesUsed(strm: ZStream): Promise<number>

当前解压缩流中使用的霍夫曼编码树的数量。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回已使用的霍夫曼编码树的数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zip = zlib.createZipSync();
12. await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
13. ).then(data => {
14. console.info('inflateInit success');
15. }).catch((errData: BusinessError) => {
16. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
17. })
18. await zip.inflateCodesUsed({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 8 }).then(data => {
19. console.info('inflateCodesUsed success');
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. }
```

### inflateBackInit12+

PhonePC/2in1TabletTVWearable

inflateBackInit(strm: ZStream, windowBits: number, window: ArrayBuffer): Promise<ReturnStatus>

使用inflateBack()函数前初始化内部流状态以进行解压缩。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| windowBits | number | 是 | 控制内存窗口的大小，并指定数据的格式（zlib、gzip、raw deflate）。取值如下：  zlib格式：[1, 15]。  gzip格式：大于15。  raw deflate格式：[-15, -1]。 |
| window | ArrayBuffer | 是 | 预设的窗口缓冲区。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

参考[inflateBack](js-apis-zlib.md#inflateback12)中的示例代码。

### inflateBackEnd12+

PhonePC/2in1TabletTVWearable

inflateBackEnd(strm: ZStream): Promise<ReturnStatus>

inflateBackInit()函数分配的所有内存都被释放。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

参考[inflateBack](js-apis-zlib.md#inflateback12)中的示例代码。

### inflateBack12+

PhonePC/2in1TabletTVWearable

inflateBack(strm: ZStream, backIn: InflateBackInputCallback, inDesc: object, backOut: InflateBackOutputCallback, outDesc: object): Promise<ReturnStatus>

实现原始解压缩，采用回调接口来处理输入和输出。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| backIn | InflateBackInputCallback | 是 | 一种函数，用于从末尾解压缩数据，以从输入源读取原始压缩数据。 |
| inDesc | object | 是 | 通用对象。 |
| backOut | InflateBackOutputCallback | 是 | 将解压缩的数据写入目标输出。 |
| outDesc | object | 是 | 通用对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let readIn: (inDesc: object) => ArrayBuffer = (inDesc: object): ArrayBuffer => {
5. console.info("inDesc = ", JSON.stringify(inDesc));
6. let buffer = new ArrayBuffer(26)
7. let array = new Uint8Array(buffer);
8. array.set([31, 139, 8, 0, 0, 0, 0, 0, 0, 10, 243, 72, 205, 201, 201, 231, 2, 0, 22, 53, 150, 49, 6, 0, 0, 0]);
9. return buffer;
10. }

12. let writeOut: (outDesc: object, buffer: ArrayBuffer, length: number) => number = (outDesc: object, buffer: ArrayBuffer, length: number): number => {
13. console.info("outDesc = ", outDesc);
14. console.info("buffer = ", buffer);
15. console.info("length = ", length);
16. let array = new Uint8Array(buffer);
17. let dataString = "";
18. for (let i = 0; i < length; i++) {
19. dataString += String.fromCharCode(array[i]);
20. }
21. console.info('writeOut ', dataString);
22. return 0;
23. }

25. let have = 0;
26. let first = 1;
27. let arrayBuffer = new ArrayBuffer(26);
28. let next = new Uint8Array(arrayBuffer);
29. let last = 0;
30. let index = 0;
31. let flags = 0;
32. let NEXT2: () => number = (): number => {
33. let o6: object = new Object()
34. if (!have) {
35. arrayBuffer = readIn(o6)
36. next = new Uint8Array(arrayBuffer);
37. console.info('readIn next = ', next.length)
38. have = next.length;
39. }
40. if (have) {
41. have--;
42. last = next[index];
43. index++;
44. }
45. else {
46. last = -1;
47. }
48. return last;
49. }

51. let inflateBackTest: () => void = (async () => {
52. try {
53. have = 0;
54. first = 1;
55. arrayBuffer = new ArrayBuffer(26);
56. next = new Uint8Array(arrayBuffer);
57. last = 0;
58. index = 0;
59. flags = 0;
60. let sr = zlib.createZipSync();
61. let buffer = new ArrayBuffer(1024)
62. await sr.inflateBackInit({}, 15, buffer).then((result) => {
63. console.info('inflateBackInit Call result res', result)
64. })
65. let ret = 0;
66. for (; ;) {
67. if (NEXT2() == -1) {
68. ret = 0;
69. console.info('inflateBackTest Call result NEXT2() == -1')
70. break;
71. }
72. console.info('have =  last = ', have, last)
73. if (last != 31 || NEXT2() != 139 ) {
74. ret = first ? -3 : -1;
75. console.info('inflateBackTest Call result last != 31 || (NEXT2() != 139 && last != 157)')
76. break;
77. }
78. first = 0;
79. ret = -5;
80. if (NEXT2() != 8) {
81. if (last < 0) {
82. console.info('inflateBackTest Call result 1 last == -1')
83. break;
84. }
85. }
86. flags = NEXT2();
87. NEXT2();
88. NEXT2();
89. NEXT2();
90. NEXT2();
91. NEXT2();
92. NEXT2();
93. if (last < 0) {
94. console.info('inflateBackTest Call result 2 last == -1')
95. break;
96. }
97. console.info('index =  have = ', next[index], have)
98. let newArrayBuffer = new ArrayBuffer(have);
99. let newNext = new Uint8Array(newArrayBuffer);
100. for (let i = 0; i < have; i++) {
101. newNext[i] = next[26 - have + i];
102. }
103. console.info('newArrayBuffer.length = ', newArrayBuffer.byteLength)
104. console.info('newNext.length = ', newNext.length)
105. let zStream: zlib.ZStream = {
106. nextIn: newArrayBuffer,
107. availableIn: have,
108. };
109. await sr.inflateBack(
110. zStream,
111. readIn,
112. { fileName: 'test.gz' },
113. writeOut,
114. { fileName: 'test.gz' }).then((result) => {
115. ret = result;
116. console.info('inflateBack Call result res', result)
117. })
118. if (ret == 1) {
119. console.info('inflateBackTest Call result success')
120. break;
121. }
122. }
123. await sr.inflateBackEnd({}).then((result) => {
124. console.info('inflateBackEnd Call result res', result)
125. })
126. }
127. catch (errData) {
128. console.error(`errData is message:${errData}`);
129. }
130. })
131. inflateBackTest();
132. }
```

### InflateBackInputCallback12+

PhonePC/2in1TabletTVWearable

type InflateBackInputCallback = (inDesc: object) => ArrayBuffer

用于输入数据的回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inDesc | object | 是 | 用户定义数据对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 从输入数据源成功读取的内容缓冲区。 |

### InflateBackOutputCallback12+

PhonePC/2in1TabletTVWearable

type InflateBackOutputCallback = (outDesc: object, buf: ArrayBuffer, length: number) => number

用于输出数据的回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| outDesc | object | 是 | 用户定义数据对象。 |
| buf | ArrayBuffer | 是 | 用于存储要写入的数据。 |
| length | number | 是 | 写入输出缓冲区的长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 输出缓冲区的字节数。 |

### inflate12+

PhonePC/2in1TabletTVWearable

inflate(strm: ZStream, flush: CompressFlushMode): Promise<ReturnStatus>

解压数据。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| flush | CompressFlushMode | 是 | 参考[CompressFlushMode定义](js-apis-zlib.md#compressflushmode12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |
| 17800005 | The input data is incorrect. For example, the data does not conform to the zlib compression format, the compressed data is corrupted, or the data is not compressed. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zStream: zlib.ZStream = {
12. nextIn: arrayBufferIn,
13. availableIn: 1,
14. nextOut: arrayBufferOut,
15. availableOut: 1
16. };
17. let zip = zlib.createZipSync();
18. await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
19. console.info('deflateInit success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
22. })
23. await zip.deflate({ availableOut: 8 }, zlib.CompressFlushMode.FINISH).then((data) => {
24. console.info('deflate success')
25. }).catch((errData: BusinessError) => {
26. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
27. })
28. await zip.deflateEnd({ nextOut: arrayBufferOut }).then(data => {
29. console.info('deflateEnd success')
30. }).catch((errData: BusinessError) => {
31. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
32. })
33. await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
34. ).then(data => {
35. console.info('inflateInit success');
36. }).catch((errData: BusinessError) => {
37. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
38. })
39. await zip.inflate({ availableIn: 8, availableOut: 8 }, 0).then((data) => {
40. console.info('inflate success')
41. }).catch((errData: BusinessError) => {
42. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
43. })
44. await zip.inflateEnd({ nextOut: arrayBufferOut }).then((data) => {
45. console.info('inflateEnd success')
46. }).catch((errData: BusinessError) => {
47. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
48. })
49. }
```

### deflateInit12+

PhonePC/2in1TabletTVWearable

deflateInit(strm: ZStream, level: CompressLevel): Promise<ReturnStatus>

初始化压缩流并设置指定压缩级别。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| level | CompressLevel | 是 | 参考[CompressLevel枚举定义](js-apis-zlib.md#compresslevel)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zStream: zlib.ZStream = {
12. nextIn: arrayBufferIn,
13. availableIn: 1,
14. nextOut: arrayBufferOut,
15. availableOut: 1
16. };
17. let zip = zlib.createZipSync();
18. await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
19. console.info('deflateInit success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
22. })
23. }
```

### deflateInit212+

PhonePC/2in1TabletTVWearable

deflateInit2(strm: ZStream, level: CompressLevel, method: CompressMethod, windowBits: number, memLevel: MemLevel, strategy: CompressStrategy): Promise<ReturnStatus>

初始化压缩流并设置压缩级别、压缩方法、窗口大小、内存级别和压缩策略。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| level | CompressLevel | 是 | 参考[CompressLevel枚举定义](js-apis-zlib.md#compresslevel)。 |
| method | CompressMethod | 是 | 参考[CompressMethod枚举定义](js-apis-zlib.md#compressmethod12)。 |
| windowBits | number | 是 | 控制内存窗口的大小，并指定数据的格式（zlib、gzip、raw deflate）。取值如下：  zlib格式：[1, 15]。  gzip格式：大于15。  raw deflate格式：[-15, -1]。 |
| memLevel | MemLevel | 是 | 参考[MemLevel枚举定义](js-apis-zlib.md#memlevel)。 |
| strategy | CompressStrategy | 是 | 参考[CompressStrategy枚举定义](js-apis-zlib.md#compressstrategy)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zStream: zlib.ZStream = {
12. nextIn: arrayBufferIn,
13. availableIn: 1,
14. nextOut: arrayBufferOut,
15. availableOut: 1
16. };
17. let zip = zlib.createZipSync()
18. await zip.deflateInit2(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED, zlib.CompressMethod.DEFLATED, 28,
19. zlib.MemLevel.MEM_LEVEL_DEFAULT, zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY).then((data) => {
20. console.info('deflateInit2 success');
21. }).catch((errData: BusinessError) => {
22. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
23. })
24. }
```

### deflate12+

PhonePC/2in1TabletTVWearable

deflate(strm: ZStream, flush: CompressFlushMode): Promise<ReturnStatus>

压缩数据。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| flush | CompressFlushMode | 是 | 参考[CompressFlushMode定义](js-apis-zlib.md#compressflushmode12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |
| 17800007 | The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zStream: zlib.ZStream = {
12. nextIn: arrayBufferIn,
13. availableIn: 1,
14. nextOut: arrayBufferOut,
15. availableOut: 1
16. };
17. let zip = zlib.createZipSync();
18. await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
19. console.info('deflateInit success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
22. })
23. await zip.deflate({ availableOut: 8 }, zlib.CompressFlushMode.FINISH).then((data) => {
24. console.info('deflate success')
25. }).catch((errData: BusinessError) => {
26. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
27. })
28. }
```

### deflateEnd12+

PhonePC/2in1TabletTVWearable

deflateEnd(strm: ZStream): Promise<ReturnStatus>

压缩流的所有动态分配的数据结构都被释放。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zStream: zlib.ZStream = {
12. nextIn: arrayBufferIn,
13. availableIn: 1,
14. nextOut: arrayBufferOut,
15. availableOut: 1
16. };
17. let zip = zlib.createZipSync();
18. await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
19. console.info('deflateInit success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
22. })
23. await zip.deflate({ availableOut: 8 }, zlib.CompressFlushMode.FINISH).then((data) => {
24. console.info('deflate success')
25. }).catch((errData: BusinessError) => {
26. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
27. })
28. await zip.deflateEnd({ nextOut: arrayBufferOut }).then(data => {
29. console.info('deflateEnd success')
30. }).catch((errData: BusinessError) => {
31. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
32. })
33. }
```

### deflateBound12+

PhonePC/2in1TabletTVWearable

deflateBound(strm: ZStream, sourceLength: number): Promise<number>

计算压缩大小的上限。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| sourceLength | number | 是 | 源数据长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回压缩大小的上限。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zStream: zlib.ZStream = {
12. nextIn: arrayBufferIn,
13. availableIn: 1,
14. nextOut: arrayBufferOut,
15. availableOut: 1
16. };
17. let zip = zlib.createZipSync();
18. await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
19. console.info('deflateInit success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. await zip.deflateBound({ nextOut: arrayBufferOut }, 12).then((data) => {
24. console.info('deflateBound success')
25. }).catch((errData: BusinessError) => {
26. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
27. })
28. }
```

### deflateSetHeader12+

PhonePC/2in1TabletTVWearable

deflateSetHeader(strm: ZStream, head: GzHeader): Promise<ReturnStatus>

当deflateInit2()请求gzip流时，提供gzip标头信息。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| head | [GzHeader](js-apis-zlib.md#gzheader12) | 是 | 从压缩数据流中提取的gzip头信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zStream: zlib.ZStream = {
12. nextIn: arrayBufferIn,
13. availableIn: 1,
14. nextOut: arrayBufferOut,
15. availableOut: 1
16. };
17. let zip = zlib.createZipSync()
18. await zip.deflateInit2(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED, zlib.CompressMethod.DEFLATED, 28,
19. zlib.MemLevel.MEM_LEVEL_DEFAULT, zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY).then((data) => {
20. console.info('deflateInit2 success');
21. }).catch((errData: BusinessError) => {
22. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
23. })
24. await zip.deflateSetHeader({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }, { isText: true, os: 1, time: 1, xflags: 1, extra: arrayBufferIn, extraLen: 12, name: arrayBufferIn, comment: arrayBufferOut, hcrc: true, done: true }).then((data) => {
25. console.info('deflateSetHeader success');
26. }).catch((errData: BusinessError) => {
27. console.error(`errData is errCode:${errData.code}  message:${errData.message}`)
28. })
29. }
```

### deflateCopy12+

PhonePC/2in1TabletTVWearable

deflateCopy(source: Zip): Promise<ReturnStatus>

复制压缩流。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | Zip | 是 | 参考[Zip定义](js-apis-zlib.md#zip12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zStream: zlib.ZStream = {
12. nextIn: arrayBufferIn,
13. availableIn: 1,
14. nextOut: arrayBufferOut,
15. availableOut: 1
16. };
17. let zip = zlib.createZipSync();
18. await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
19. console.info('deflateInit success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. await zip.deflateCopy(zip).then((data) => {
24. console.info('deflateCopy success')
25. }).catch((errData: BusinessError) => {
26. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
27. })
28. }
```

### deflateSetDictionary12+

PhonePC/2in1TabletTVWearable

deflateSetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<ReturnStatus>

从给定的字节序列初始化压缩字典。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| dictionary | ArrayBuffer | 是 | 字典数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zStream: zlib.ZStream = {
12. nextIn: arrayBufferIn,
13. availableIn: 1,
14. nextOut: arrayBufferOut,
15. availableOut: 1
16. };
17. let zip = zlib.createZipSync();
18. await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
19. console.info('deflateInit success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. await zip.deflateSetDictionary({ nextOut: arrayBufferOut }, arrayBufferOut).then((data) => {
24. console.info('deflateSetDictionary success')
25. }).catch((errData: BusinessError) => {
26. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
27. })
28. }
```

### deflateGetDictionary12+

PhonePC/2in1TabletTVWearable

deflateGetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<DictionaryOutputInfo>

获取当前压缩流中使用的解压缩字典内容及其长度。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| dictionary | ArrayBuffer | 是 | 接收压缩字典的实际内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DictionaryOutputInfo](js-apis-zlib.md#dictionaryoutputinfo12)> | Promise对象。返回结果状态和字典的长度。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zStream: zlib.ZStream = {
12. nextIn: arrayBufferIn,
13. availableIn: 1,
14. nextOut: arrayBufferOut,
15. availableOut: 1
16. };
17. let zip = zlib.createZipSync();
18. await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
19. console.info('deflateInit success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. await zip.deflateSetDictionary({ nextOut: arrayBufferOut }, arrayBufferOut).then((data) => {
24. console.info('deflateSetDictionary success')
25. }).catch((errData: BusinessError) => {
26. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
27. })
28. await zip.deflateGetDictionary({ nextOut: arrayBufferOut }, arrayBufferOut).then((data) => {
29. console.info('deflateGetDictionary success')
30. }).catch((errData: BusinessError) => {
31. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
32. })
33. }
```

### deflateTune12+

PhonePC/2in1TabletTVWearable

deflateTune(strm: ZStream, goodLength: number, maxLazy: number, niceLength: number, maxChain: number): Promise<ReturnStatus>

微调deflate的内部压缩参数。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| goodLength | number | 是 | 匹配的长度阈值。 |
| maxLazy | number | 是 | 压缩算法在构建哈夫曼树时的延迟匹配策略，取值范围为0到4的整数。1到4，值越大，算法越‘懒’，匹配过程越慢，但可能生成更优的压缩结果。0：禁用懒惰匹配，算法会尽快构建哈夫曼树，压缩速度快，但压缩率低。 |
| niceLength | number | 是 | 适合的延迟长度阈值。 |
| maxChain | number | 是 | 最大链条长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zStream: zlib.ZStream = {
12. nextIn: arrayBufferIn,
13. availableIn: 1,
14. nextOut: arrayBufferOut,
15. availableOut: 1
16. };
17. let zip = zlib.createZipSync();
18. await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
19. console.info('deflateInit success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. await zip.deflateTune({ nextOut: arrayBufferOut }, 2, 2, 2, 2).then((data) => {
24. console.info('deflateTune success:')
25. }).catch((errData: BusinessError) => {
26. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
27. })
28. }
```

### deflateReset12+

PhonePC/2in1TabletTVWearable

deflateReset(strm: ZStream): Promise<ReturnStatus>

这个函数相当于先调用deflateEnd再调用deflateInit，但是并不会释放和重新分配内部解压缩状态。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zStream: zlib.ZStream = {
12. nextIn: arrayBufferIn,
13. availableIn: 1,
14. nextOut: arrayBufferOut,
15. availableOut: 1
16. };
17. let zip = zlib.createZipSync();
18. await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
19. console.info('deflateInit success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. await zip.deflateReset({ nextOut: arrayBufferOut }).then((data) => {
24. console.info('deflateReset success')
25. }).catch((errData: BusinessError) => {
26. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
27. })
28. }
```

### deflateResetKeep12+

PhonePC/2in1TabletTVWearable

deflateResetKeep(strm: ZStream): Promise<ReturnStatus>

重置初始化的deflate压缩流，但保留其设置的压缩参数和字典。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zStream: zlib.ZStream = {
12. nextIn: arrayBufferIn,
13. availableIn: 1,
14. nextOut: arrayBufferOut,
15. availableOut: 1
16. };
17. let zip = zlib.createZipSync();
18. await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
19. console.info('deflateInit success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. await zip.deflateResetKeep({ nextOut: arrayBufferOut }).then((data) => {
24. console.info('deflateResetKeep success')
25. }).catch((errData: BusinessError) => {
26. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
27. })
28. }
```

### deflatePending12+

PhonePC/2in1TabletTVWearable

deflatePending(strm: ZStream): Promise<DeflatePendingOutputInfo>

返回已生成但尚未在可用输出中提供的输出的字节数和位数。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DeflatePendingOutputInfo](js-apis-zlib.md#deflatependingoutputinfo12)> | Promise对象。返回结果状态、输出位数和输出字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zStream: zlib.ZStream = {
12. nextIn: arrayBufferIn,
13. availableIn: 1,
14. nextOut: arrayBufferOut,
15. availableOut: 1
16. };
17. let zip = zlib.createZipSync();
18. await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
19. console.info('deflateInit success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. await zip.deflatePending({ nextOut: arrayBufferOut }).then((data) => {
24. console.info('deflatePending success')
25. }).catch((errData: BusinessError) => {
26. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
27. })
28. }
```

### deflateParams12+

PhonePC/2in1TabletTVWearable

deflateParams(strm: ZStream, level: CompressLevel, strategy: CompressStrategy): Promise<ReturnStatus>

动态更新压缩级别和压缩策略。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| level | CompressLevel | 是 | 参考[CompressLevel枚举定义](js-apis-zlib.md#compresslevel)。 |
| strategy | CompressStrategy | 是 | 参考[CompressStrategy枚举定义](js-apis-zlib.md#compressstrategy)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zStream: zlib.ZStream = {
12. nextIn: arrayBufferIn,
13. availableIn: 1,
14. nextOut: arrayBufferOut,
15. availableOut: 1
16. };
17. let zip = zlib.createZipSync()
18. await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
19. console.info('deflateInit success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. await zip.deflateParams(zStream, zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION, zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY).then((data) => {
24. console.info('deflateParams success')
25. }).catch((errData: BusinessError) => {
26. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
27. })
28. }
```

### deflatePrime12+

PhonePC/2in1TabletTVWearable

deflatePrime(strm: ZStream, bits: number, value: number): Promise<ReturnStatus>

在压缩流中插入位和值。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strm | ZStream | 是 | 参考[ZStream定义](js-apis-zlib.md#zstream12)。 |
| bits | number | 是 | 要插入的位数，取值范围在0~16。 |
| value | number | 是 | 与位数相对应的位值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象。返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib, BusinessError } from '@kit.BasicServicesKit';

3. async function demo() {
4. let str = 'hello world!';
5. let arrayBufferIn = new ArrayBuffer(str.length);
6. let byteArray = new Uint8Array(arrayBufferIn);
7. for (let i = 0, j = str.length; i < j; i++) {
8. byteArray[i] = str.charCodeAt(i)
9. }
10. let arrayBufferOut = new ArrayBuffer(100);
11. let zStream: zlib.ZStream = {
12. nextIn: arrayBufferIn,
13. availableIn: 1,
14. nextOut: arrayBufferOut,
15. availableOut: 1
16. };
17. let zip = zlib.createZipSync();
18. await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED).then((data) => {
19. console.info('deflateInit success')
20. }).catch((errData: BusinessError) => {
21. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
22. })
23. await zip.deflatePrime({ nextOut: arrayBufferOut }, 5, 2).then((data) => {
24. console.info('deflatePrime success')
25. }).catch((errData: BusinessError) => {
26. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
27. })
28. }
```

## Options

PhonePC/2in1TabletTVWearable

Options用于指定在压缩或解压Zip文件时的选项。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| level | [CompressLevel](js-apis-zlib.md#compresslevel) | 否 | 是 | 压缩或解压时指定的压缩等级。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| memLevel | [MemLevel](js-apis-zlib.md#memlevel) | 否 | 是 | 压缩时指定的使用内存等级。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| strategy | [CompressStrategy](js-apis-zlib.md#compressstrategy) | 否 | 是 | 压缩时指定的压缩策略。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| parallel18+ | [ParallelStrategy](js-apis-zlib.md#parallelstrategy18) | 否 | 是 | 压缩或解压时指定的串行或并行策略。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| pathSeparatorStrategy21+ | [PathSeparatorStrategy](js-apis-zlib.md#pathseparatorstrategy21) | 否 | 是 | 解压时指定的压缩包内文件路径中分隔符的处理策略。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |

## CompressLevel

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COMPRESS\_LEVEL\_NO\_COMPRESSION | 0 | 压缩率为0压缩等级。 |
| COMPRESS\_LEVEL\_BEST\_SPEED | 1 | 最佳速度压缩等级。 |
| COMPRESS\_LEVEL\_BEST\_COMPRESSION | 9 | 最佳压缩等级。 |
| COMPRESS\_LEVEL\_DEFAULT\_COMPRESSION | -1 | 默认压缩等级。 |

## MemLevel

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MEM\_LEVEL\_MIN | 1 | zlib接口在压缩过程中最小使用内存。 |
| MEM\_LEVEL\_MAX | 9 | zlib接口在压缩过程中最大使用内存。 |
| MEM\_LEVEL\_DEFAULT | 8 | zlib接口在压缩过程中默认使用内存。 |

## CompressStrategy

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COMPRESS\_STRATEGY\_DEFAULT\_STRATEGY | 0 | 常规数据策略。 |
| COMPRESS\_STRATEGY\_FILTERED | 1 | 过滤器产生的数据压缩策略。 |
| COMPRESS\_STRATEGY\_HUFFMAN\_ONLY | 2 | 霍夫曼编码格式压缩策略。 |
| COMPRESS\_STRATEGY\_RLE | 3 | 游标编码压缩策略。 |
| COMPRESS\_STRATEGY\_FIXED | 4 | 固定的压缩策略。 |

## ParallelStrategy18+

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PARALLEL\_STRATEGY\_SEQUENTIAL | 0 | 默认值，串行压缩/解压策略。 |
| PARALLEL\_STRATEGY\_PARALLEL\_DECOMPRESSION | 1 | 并行解压策略。 |

## PathSeparatorStrategy21+

PhonePC/2in1TabletTVWearable

PathSeparatorStrategy作为[Options](js-apis-zlib.md#options)的一个属性，用于指定解压时目标压缩包内文件路径中分隔符的处理策略。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PATH\_SEPARATOR\_STRATEGY\_DEFAULT | 0 | 默认值，压缩包内文件路径中的分隔符不做处理。 |
| PATH\_SEPARATOR\_STRATEGY\_REPLACE\_BACKSLASH | 1 | 压缩包内文件路径中的反斜杠'\'替换为斜杠'/'。 |

## ErrorCode(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，暂无替代接口。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ERROR\_CODE\_OK | 0 | 函数调用成功。 |
| ERROR\_CODE\_ERRNO | -1 | 函数调用失败。 |

## CompressFlushMode12+

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_FLUSH | 0 | 默认值，表示正常操作。 |
| PARTIAL\_FLUSH | 1 | 在流中生成部分刷新点。 |
| SYNC\_FLUSH | 2 | 在保持压缩流状态的同时强制输出所有压缩数据。 |
| FULL\_FLUSH | 3 | 重置压缩状态。 |
| FINISH | 4 | 压缩或解压缩过程结束。 |
| BLOCK | 5 | 允许更精确的控制。 |
| TREES | 6 | 实施过程中有特殊目的。 |

## CompressMethod12+

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFLATED | 8 | 压缩方法。 |

## ReturnStatus12+

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OK | 0 | 函数调用成功。该接口支持在元服务中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| STREAM\_END | 1 | 函数调用成功，表示已处理了整个数据。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NEED\_DICT | 2 | 函数调用成功，表示需要预设字典才能继续解压缩。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ERRNO23+ | -1 | 函数调用失败，表示文件操作错误。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| STREAM\_ERROR23+ | -2 | 函数调用失败，表示压缩或解压缩流错误。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| DATA\_ERROR23+ | -3 | 函数调用失败，表示输入数据不正确。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| MEM\_ERROR23+ | -4 | 函数调用失败，表示内存分配失败。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| BUF\_ERROR23+ | -5 | 函数调用失败，表示输入缓冲区不正确。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## ZStream12+

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| nextIn | ArrayBuffer | 否 | 是 | 需要压缩的输入字节。 |
| availableIn | number | 否 | 是 | nextIn可用的字节数。 |
| totalIn | number | 否 | 是 | 到目前为止读取的输入字节总数。 |
| nextOut | ArrayBuffer | 否 | 是 | 压缩后的输出字节。 |
| availableOut | number | 否 | 是 | nextOut的剩余可用字节数。 |
| totalOut | number | 否 | 是 | 到目前为止输出字节总数。 |
| dataType | number | 否 | 是 | 关于数据类型的最佳猜测：deflate的二进制或文本，或inflate的解码状态。 |
| adler | number | 否 | 是 | 未压缩数据的Adler-32或CRC-32值。 |

## ZipOutputInfo12+

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| status | ReturnStatus | 否 | 否 | 参考[ReturnStatus枚举定义](js-apis-zlib.md#returnstatus12)。 |
| destLen | number | 否 | 否 | 目标缓冲区的总长度。 |

## DictionaryOutputInfo12+

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| status | ReturnStatus | 否 | 否 | 参考[ReturnStatus枚举定义](js-apis-zlib.md#returnstatus12)。 |
| dictionaryLength | number | 否 | 否 | 字典的长度。 |

## DecompressionOutputInfo12+

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| status | ReturnStatus | 否 | 否 | 参考[ReturnStatus枚举定义](js-apis-zlib.md#returnstatus12)。 |
| destLength | number | 否 | 否 | 目标缓冲区的长度。 |
| sourceLength | number | 否 | 否 | 源缓冲区的长度。 |

## DeflatePendingOutputInfo12+

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| status | ReturnStatus | 否 | 否 | 参考[ReturnStatus枚举定义](js-apis-zlib.md#returnstatus12)。 |
| pending | number | 否 | 否 | 已生成的输出字节数。 |
| bits | number | 否 | 否 | 已生成的输出位数。 |

## GzHeader12+

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isText | boolean | 否 | 是 | 如果压缩数据被认为是文本，则为True。 |
| os | number | 否 | 是 | 操作系统。 |
| time | number | 否 | 是 | 修改时间。 |
| xflags | number | 否 | 是 | 额外标志。 |
| extra | ArrayBuffer | 否 | 是 | 额外字段。 |
| extraLen | number | 否 | 是 | 额外字段的长度。 |
| name | ArrayBuffer | 否 | 是 | 文件名。 |
| comment | ArrayBuffer | 否 | 是 | 注释。 |
| hcrc | boolean | 否 | 是 | 如果存在crc标头，则为True。 |
| done | boolean | 否 | 是 | 读取gzip标头后为True。 |

## zlib.createGZip12+

PhonePC/2in1TabletTVWearable

createGZip(): Promise<GZip>

创建GZip对象。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[GZip](js-apis-zlib.md#gzip12)> | Promise对象。返回GZip对象实例。 |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';

3. zlib.createGZip().then((data) => {
4. console.info('createGZip success');
5. })
```

## zlib.createGZipSync12+

PhonePC/2in1TabletTVWearable

createGZipSync(): GZip

创建GZip对象。成功时返回GZip对象实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GZip](js-apis-zlib.md#gzip12) | GZip对象实例。 |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';

3. let gzip = zlib.createGZipSync();
```

## GZip12+

PhonePC/2in1TabletTVWearable

Gzip相关接口。

### gzdopen12+

PhonePC/2in1TabletTVWearable

gzdopen(fd: number, mode: string): Promise<void>

将gzFile与文件描述符fd相关联，打开文件，用于进行读取并解压缩，或者压缩并写入。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 文件描述符。通常情况下，通过系统调用“open”或其他方法获得的。 |
| mode | string | 是 | 用于指定访问模式。详情与[gzopen](js-apis-zlib.md#gzopen12)一致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800002 | No such file or access mode error. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzdopenDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzdopen");
6. let path = pathDir + "/gzdopen/test.gz";
7. let file = fs.openSync(path, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
8. let gzip = zlib.createGZipSync();
9. await gzip.gzdopen(file.fd, "wb");
10. await gzip.gzclose();
11. }

13. @Entry
14. @Component
15. struct Index {
16. build() {
17. Row() {
18. Column() {
19. Button('test gzip interface')
20. .type(ButtonType.Capsule)
21. .height(60)
22. .width(200)
23. .onClick(() => {
24. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
25. if (typeof pathDir === 'string') {
26. gzdopenDemo(pathDir);
27. }
28. })
29. }
30. .width('100%')
31. }
32. .height('100%')
33. }
34. }
```

### gzbuffer12+

PhonePC/2in1TabletTVWearable

gzbuffer(size: number):Promise<number>

为当前库函数设置内部缓冲区尺寸。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 需要设置的内部缓冲区尺寸。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，成功时，返回0。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800009 | Internal structure error. |

**示例：**

```
1. import { fileIo as fs } from '@kit.CoreFileKit';
2. import { zlib } from '@kit.BasicServicesKit';

4. async function gzbufferDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzbuffer");
6. let path = pathDir + "/gzbuffer/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. await gzip.gzclose();
10. await gzip.gzopen(path, "rb");
11. let result = await gzip.gzbuffer(648);
12. await gzip.gzclose();
13. }

15. @Entry
16. @Component
17. struct Index {
18. build() {
19. Row() {
20. Column() {
21. Button('test gzip interface')
22. .type(ButtonType.Capsule)
23. .height(60)
24. .width(200)
25. .onClick(() => {
26. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
27. if (typeof pathDir === 'string') {
28. gzbufferDemo(pathDir);
29. }
30. })
31. }
32. .width('100%')
33. }
34. .height('100%')
35. }
36. }
```

### gzopen12+

PhonePC/2in1TabletTVWearable

gzopen(path: string, mode: string): Promise<void>

打开位于指定路径的gzip(.gz)文件，用于进行读取并解压缩，或者压缩并写入。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 需要打开的文件路径。 |
| mode | string | 是 | 指定文件打开方法。  基础模式（必须三选一）：  - “r”或“rb”：读取模式，自动检测并解压gzip文件（若非gzip格式则直接读取原始数据）。  - “w”或“wb”：写入模式，创建新文件并压缩数据。  - “a”或“ab”：追加模式，在现有文件末尾追加新的gzip流（不校验原文件格式）。  可选功能参数（可组合使用）：  - 压缩级别：0（不压缩）至9（最佳压缩），默认压缩级别为6，需要配合写入模式或者追加模式使用。  - 压缩策略：“f”（过滤策略）、“h”（霍夫曼策略）、“R”（游标编码策略）、“F”（固定编码策略），只能选取一种压缩策略。  - 透明模式：“T”，写入时不压缩且不生成gzip头（生成普通文件），与压缩策略互斥。  - 独占创建：“x”，如果文件存在则打开失败，需要配合写入模式或者追加模式使用  - close-on-exec标志：“e”，设置文件描述符的FD\_CLOEXEC属性（依赖系统支持）。  模式字符串示例：  - “r”：读取模式，读取时以二进制形式读取。  - “rb”：读取模式，读取时以二进制形式读取。  - “wb6”：写入模式，压缩时以二进制形式写入，压缩级别为6。  - “wb9f”：写入模式，压缩时以二进制形式写入，压缩级别为最佳压缩，压缩策略采用过滤策略。  - “wbT”：写入模式，不压缩，生成普通文件。  - “wbx”：写入模式，压缩时以二进制形式写入，采用独占创建的方式写入文件。  - “abx”：追加模式，压缩时以二进制形式追加并写入，采用独占创建的方式写入文件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800002 | No such file or access mode error. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzopenDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzopen");
6. let path = pathDir + "/gzopen/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. await gzip.gzclose();
10. }

12. @Entry
13. @Component
14. struct Index {
15. build() {
16. Row() {
17. Column() {
18. Button('test gzip interface')
19. .type(ButtonType.Capsule)
20. .height(60)
21. .width(200)
22. .onClick(() => {
23. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
24. if (typeof pathDir === 'string') {
25. gzopenDemo(pathDir);
26. }
27. })
28. }
29. .width('100%')
30. }
31. .height('100%')
32. }
33. }
```

### gzeof12+

PhonePC/2in1TabletTVWearable

gzeof(): Promise<number>

检查gzip压缩文件的读取位置是否已到达文件的末尾。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，如果在读取时设置了文件的文件结束指示符，则返回1。 |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzeofDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzeof");
6. let path = pathDir + "/gzeof/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. let writeBufferWithData = new ArrayBuffer(16);
10. let uint8View = new Uint8Array(writeBufferWithData);
11. for (let i = 0; i < uint8View.length; i++) {
12. uint8View[i] = i;
13. }
14. let writeNum = await gzip.gzwrite(writeBufferWithData, 16)
15. await gzip.gzclose();
16. await gzip.gzopen(path, "rb");
17. let readBufferWithData = new ArrayBuffer(20);
18. let readNum = await gzip.gzread(readBufferWithData);
19. let eofNum = await gzip.gzeof();
20. await gzip.gzclose();
21. }

23. @Entry
24. @Component
25. struct Index {
26. build() {
27. Row() {
28. Column() {
29. Button('test gzip interface')
30. .type(ButtonType.Capsule)
31. .height(60)
32. .width(200)
33. .onClick(() => {
34. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
35. if (typeof pathDir === 'string') {
36. gzeofDemo(pathDir);
37. }
38. })
39. }
40. .width('100%')
41. }
42. .height('100%')
43. }
44. }
```

### gzdirect12+

PhonePC/2in1TabletTVWearable

gzdirect(): Promise<number>

检查指定的gzip文件句柄文件是否直接访问原始未压缩数据，重新分配缓冲区。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，如果直接访问原始未压缩数据，则返回1。 |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzdirectDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzdirect");
6. let path = pathDir + "/gzdirect/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. let directNum = await gzip.gzdirect();
10. await gzip.gzclose();
11. }

13. @Entry
14. @Component
15. struct Index {
16. build() {
17. Row() {
18. Column() {
19. Button('test gzip interface')
20. .type(ButtonType.Capsule)
21. .height(60)
22. .width(200)
23. .onClick(() => {
24. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
25. if (typeof pathDir === 'string') {
26. gzdirectDemo(pathDir);
27. }
28. })
29. }
30. .width('100%')
31. }
32. .height('100%')
33. }
34. }
```

### gzclose12+

PhonePC/2in1TabletTVWearable

gzclose(): Promise<ReturnStatus>

清除文件的所有挂起输出，如有必要，关闭文件和释放（解）压缩状态。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象，返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |
| 17800006 | Memory allocation failed. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzcloseDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzclose");
6. let path = pathDir + "/gzclose/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. await gzip.gzclose();
10. }

12. @Entry
13. @Component
14. struct Index {
15. build() {
16. Row() {
17. Column() {
18. Button('test gzip interface')
19. .type(ButtonType.Capsule)
20. .height(60)
21. .width(200)
22. .onClick(() => {
23. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
24. if (typeof pathDir === 'string') {
25. gzcloseDemo(pathDir);
26. }
27. })
28. }
29. .width('100%')
30. }
31. .height('100%')
32. }
33. }
```

### gzclearerr12+

PhonePC/2in1TabletTVWearable

gzclearerr(): Promise<void>

清除文件的错误和文件结束标志。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzclearerrDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzclearerr");
6. let path = pathDir + "/gzclearerr/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. let writeBufferWithData = new ArrayBuffer(16);
10. let uint8View = new Uint8Array(writeBufferWithData);
11. for (let i = 0; i < uint8View.length; i++) {
12. uint8View[i] = i;
13. }
14. let writeNum = await gzip.gzwrite(writeBufferWithData, 16)
15. await gzip.gzclose();
16. await gzip.gzopen(path, "rb");
17. let readBufferWithData = new ArrayBuffer(20);
18. let readNum = await gzip.gzread(readBufferWithData);
19. let eofNum = await gzip.gzeof();
20. await gzip.gzclearerr();
21. let eofNumClear = await gzip.gzeof();
22. await gzip.gzclose();
23. }

25. @Entry
26. @Component
27. struct Index {
28. build() {
29. Row() {
30. Column() {
31. Button('test gzip interface')
32. .type(ButtonType.Capsule)
33. .height(60)
34. .width(200)
35. .onClick(() => {
36. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
37. if (typeof pathDir === 'string') {
38. gzclearerrDemo(pathDir);
39. }
40. })
41. }
42. .width('100%')
43. }
44. .height('100%')
45. }
46. }
```

### gzerror12+

PhonePC/2in1TabletTVWearable

gzerror(): Promise<GzErrorOutputInfo>

文件上发生的最后一个错误的错误消息。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[GzErrorOutputInfo](js-apis-zlib.md#gzerroroutputinfo12)> | Promise对象，返回结果状态和出现的最后一个状态的状态消息。 |

**错误码：**

以下错误码的详细介绍请参见[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzerrorDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzerror");
6. let path = pathDir + "/gzerror/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. let writeBufferWithData = new ArrayBuffer(16);
10. let uint8View = new Uint8Array(writeBufferWithData);
11. for (let i = 0; i < uint8View.length; i++) {
12. uint8View[i] = i;
13. }
14. try {
15. await gzip.gzwrite(writeBufferWithData, -1);
16. } catch (errData) {
17. await gzip.gzerror().then((GzErrorOutputInfo) => {
18. console.info('errCode', GzErrorOutputInfo.status);
19. console.info('errMsg', GzErrorOutputInfo.statusMsg);
20. })
21. }
22. await gzip.gzclose();
23. }

25. @Entry
26. @Component
27. struct Index {
28. build() {
29. Row() {
30. Column() {
31. Button('test gzip interface')
32. .type(ButtonType.Capsule)
33. .height(60)
34. .width(200)
35. .onClick(() => {
36. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
37. if (typeof pathDir === 'string') {
38. gzerrorDemo(pathDir);
39. }
40. })
41. }
42. .width('100%')
43. }
44. .height('100%')
45. }
46. }
```

### gzgetc12+

PhonePC/2in1TabletTVWearable

gzgetc(): Promise<number>

从文件中读取并解压缩一个字节。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回读取字符的ASCII值。 |

**错误码：**

以下错误码的详细介绍请参见[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17800009 | Internal structure error. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzgetcDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzgetc");
6. let path = pathDir + "/gzgetc/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. await gzip.gzputc(1);
10. await gzip.gzclose();
11. await gzip.gzopen(path, "rb");
12. let result = await gzip.gzgetc();
13. await gzip.gzclose();
14. }

16. @Entry
17. @Component
18. struct Index {
19. build() {
20. Row() {
21. Column() {
22. Button('test gzip interface')
23. .type(ButtonType.Capsule)
24. .height(60)
25. .width(200)
26. .onClick(() => {
27. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
28. if (typeof pathDir === 'string') {
29. gzgetcDemo(pathDir);
30. }
31. })
32. }
33. .width('100%')
34. }
35. .height('100%')
36. }
37. }
```

### gzflush12+

PhonePC/2in1TabletTVWearable

gzflush(flush: CompressFlushMode): Promise<ReturnStatus>

将所有挂起的输出刷新到文件中。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flush | CompressFlushMode | 是 | 控制刷新操作的行为，参考[CompressFlushMode枚举](js-apis-zlib.md#compressflushmode12)的定义。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象，返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzflushDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzflush");
6. let path = pathDir + "/gzflush/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. let flushNum = await gzip.gzflush(zlib.CompressFlushMode.NO_FLUSH);
10. await gzip.gzclose();
11. }

13. @Entry
14. @Component
15. struct Index {
16. build() {
17. Row() {
18. Column() {
19. Button('test gzip interface')
20. .type(ButtonType.Capsule)
21. .height(60)
22. .width(200)
23. .onClick(() => {
24. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
25. if (typeof pathDir === 'string') {
26. gzflushDemo(pathDir);
27. }
28. })
29. }
30. .width('100%')
31. }
32. .height('100%')
33. }
34. }
```

### gzfwrite12+

PhonePC/2in1TabletTVWearable

gzfwrite(buf: ArrayBuffer, size: number, nitems: number): Promise<number>

将大小为size，数量为nitems的数据块从buf压缩并写入文件。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 要将数据写入的缓冲区。 |
| size | number | 是 | 单个数据块中的字节数。 |
| nitems | number | 是 | 要写入的数据块数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回写入大小为size的完整数据块的数目。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800009 | Internal structure error. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzfwriteDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzfwrite");
6. let path = pathDir + "/gzfwrite/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. let bufferWithData = new ArrayBuffer(16);
10. let uint8View = new Uint8Array(bufferWithData);
11. for (let i = 0; i < uint8View.length; i++) {
12. uint8View[i] = i;
13. }
14. let result = await gzip.gzfwrite(bufferWithData, 8, 2)
15. await gzip.gzclose();
16. }

18. @Entry
19. @Component
20. struct Index {
21. build() {
22. Row() {
23. Column() {
24. Button('test gzip interface')
25. .type(ButtonType.Capsule)
26. .height(60)
27. .width(200)
28. .onClick(() => {
29. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
30. if (typeof pathDir === 'string') {
31. gzfwriteDemo(pathDir);
32. }
33. })
34. }
35. .width('100%')
36. }
37. .height('100%')
38. }
39. }
```

### gzfread12+

PhonePC/2in1TabletTVWearable

gzfread(buf: ArrayBuffer, size: number, nitems: number): Promise<number>

从gzip压缩文件中解压缩并读取数据。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 用于存储读取结果的目标缓冲区。 |
| size | number | 是 | 单个数据块中的字节数。 |
| nitems | number | 是 | 要写入的数据块数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回读取大小为size的完整数据块的数目。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800009 | Internal structure error. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzfreadDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzfread");
6. let path = pathDir + "/gzfread/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. let writeBuffer = new ArrayBuffer(16);
10. let uint8View = new Uint8Array(writeBuffer);
11. for (let i = 0; i < uint8View.length; i++) {
12. uint8View[i] = i;
13. }
14. await gzip.gzfwrite(writeBuffer, 8, 2);
15. await gzip.gzclose();
16. await gzip.gzopen(path, "rb");
17. let readBuffer = new ArrayBuffer(16);
18. let result = await gzip.gzfread(readBuffer, 8, 2);
19. await gzip.gzclose();
20. }

22. @Entry
23. @Component
24. struct Index {
25. build() {
26. Row() {
27. Column() {
28. Button('test gzip interface')
29. .type(ButtonType.Capsule)
30. .height(60)
31. .width(200)
32. .onClick(() => {
33. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
34. if (typeof pathDir === 'string') {
35. gzfreadDemo(pathDir);
36. }
37. })
38. }
39. .width('100%')
40. }
41. .height('100%')
42. }
43. }
```

### gzclosew12+

PhonePC/2in1TabletTVWearable

gzclosew(): Promise<ReturnStatus>

与gzclose()功能相同，仅适用于写入或追加时。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象，返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |
| 17800006 | Memory allocation failed. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzclosewDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzclosew");
6. let path = pathDir + "/gzclosew/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. await gzip.gzclosew();
10. }

12. @Entry
13. @Component
14. struct Index {
15. build() {
16. Row() {
17. Column() {
18. Button('test gzip interface')
19. .type(ButtonType.Capsule)
20. .height(60)
21. .width(200)
22. .onClick(() => {
23. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
24. if (typeof pathDir === 'string') {
25. gzclosewDemo(pathDir);
26. }
27. })
28. }
29. .width('100%')
30. }
31. .height('100%')
32. }
33. }
```

### gzcloser12+

PhonePC/2in1TabletTVWearable

gzcloser(): Promise<ReturnStatus>

与gzclose()功能相同，仅适用于读取时。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象，返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzcloserDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzcloser");
6. let path = pathDir + "/gzcloser/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. await gzip.gzclose();
10. await gzip.gzopen(path, "rb");
11. await gzip.gzcloser();
12. }

14. @Entry
15. @Component
16. struct Index {
17. build() {
18. Row() {
19. Column() {
20. Button('test gzip interface')
21. .type(ButtonType.Capsule)
22. .height(60)
23. .width(200)
24. .onClick(() => {
25. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
26. if (typeof pathDir === 'string') {
27. gzcloserDemo(pathDir);
28. }
29. })
30. }
31. .width('100%')
32. }
33. .height('100%')
34. }
35. }
```

### gzwrite12+

PhonePC/2in1TabletTVWearable

gzwrite(buf: ArrayBuffer, len: number): Promise<number>

将buf中的len长度的未压缩字节进行压缩并将其写入文件。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 对象指向要写入的数据缓冲区。 |
| len | number | 是 | 未压缩字节长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回写入的未压缩字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800009 | Internal structure error. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzwriteDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzwrite");
6. let path = pathDir + "/gzwrite/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. let bufferWithData = new ArrayBuffer(16);
10. let uint8View = new Uint8Array(bufferWithData);
11. for (let i = 0; i < uint8View.length; i++) {
12. uint8View[i] = i;
13. }
14. let result = await gzip.gzwrite(bufferWithData, 16);
15. await gzip.gzclose();
16. }

18. @Entry
19. @Component
20. struct Index {
21. build() {
22. Row() {
23. Column() {
24. Button('test gzip interface')
25. .type(ButtonType.Capsule)
26. .height(60)
27. .width(200)
28. .onClick(() => {
29. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
30. if (typeof pathDir === 'string') {
31. gzwriteDemo(pathDir);
32. }
33. })
34. }
35. .width('100%')
36. }
37. .height('100%')
38. }
39. }
```

### gzungetc12+

PhonePC/2in1TabletTVWearable

gzungetc(c: number): Promise<number>

将c推回到流中，以便在下次读取文件时将作为第一个字符读取。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| c | number | 是 | 回退到输入流之前的字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回推送的字符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800009 | Internal structure error. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzungetcDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzungetc");
6. let path = pathDir + "/gzungetc/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. await gzip.gzclose();
10. await gzip.gzopen(path, "rb");
11. await gzip.gzread(new ArrayBuffer(1));
12. let result = await gzip.gzungetc(1);
13. await gzip.gzclose();
14. }

16. @Entry
17. @Component
18. struct Index {
19. build() {
20. Row() {
21. Column() {
22. Button('test gzip interface')
23. .type(ButtonType.Capsule)
24. .height(60)
25. .width(200)
26. .onClick(() => {
27. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
28. if (typeof pathDir === 'string') {
29. gzungetcDemo(pathDir);
30. }
31. })
32. }
33. .width('100%')
34. }
35. .height('100%')
36. }
37. }
```

### gztell12+

PhonePC/2in1TabletTVWearable

gztell(): Promise<number>

返回文件中下一个gzread或gzwrite的起始位置。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回文件种下一个gzread或gzwrite的起始位置。 |

**错误码：**

以下错误码的详细介绍请参见[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17800009 | Internal structure error. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gztellDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gztell");
6. let path = pathDir + "/gztell/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. let result = await gzip.gztell();
10. await gzip.gzclose();
11. }

13. @Entry
14. @Component
15. struct Index {
16. build() {
17. Row() {
18. Column() {
19. Button('test gzip interface')
20. .type(ButtonType.Capsule)
21. .height(60)
22. .width(200)
23. .onClick(() => {
24. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
25. if (typeof pathDir === 'string') {
26. gztellDemo(pathDir);
27. }
28. })
29. }
30. .width('100%')
31. }
32. .height('100%')
33. }
34. }
```

### gzsetparams12+

PhonePC/2in1TabletTVWearable

gzsetparams(level: CompressLevel, strategy: CompressStrategy): Promise<ReturnStatus>

动态更新文件的压缩级别和压缩策略。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | CompressLevel | 是 | 压缩级别，参考[CompressLevel枚举定义](js-apis-zlib.md#compresslevel)。 |
| strategy | CompressStrategy | 是 | 压缩策略，参考[CompressStrategy枚举定义](js-apis-zlib.md#compressstrategy)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象，返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzsetparamsDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzsetparams");
6. let path = pathDir + "/gzsetparams/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. let result = await gzip.gzsetparams(zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
10. zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY);
11. await gzip.gzclose();
12. }

14. @Entry
15. @Component
16. struct Index {
17. build() {
18. Row() {
19. Column() {
20. Button('test gzip interface')
21. .type(ButtonType.Capsule)
22. .height(60)
23. .width(200)
24. .onClick(() => {
25. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
26. if (typeof pathDir === 'string') {
27. gzsetparamsDemo(pathDir);
28. }
29. })
30. }
31. .width('100%')
32. }
33. .height('100%')
34. }
35. }
```

### gzseek12+

PhonePC/2in1TabletTVWearable

gzseek(offset: number, whence: OffsetReferencePoint): Promise<number>

将起始位置设置为相对于文件中下一个gzread或gzwrite的偏移位置。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 目标偏移位置。 |
| whence | OffsetReferencePoint | 是 | 定义偏移的参考点，参考[OffsetReferencePoint枚举定义](js-apis-zlib.md#offsetreferencepoint12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回从未压缩流开始以字节为单位测量的结果偏移位置。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800009 | Internal structure error. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzseekDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzseek");
6. let path = pathDir + "/gzseek/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. let result = await gzip.gzseek(2, zlib.OffsetReferencePoint.SEEK_CUR);
10. await gzip.gzclose();
11. }

13. @Entry
14. @Component
15. struct Index {
16. build() {
17. Row() {
18. Column() {
19. Button('test gzip interface')
20. .type(ButtonType.Capsule)
21. .height(60)
22. .width(200)
23. .onClick(() => {
24. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
25. if (typeof pathDir === 'string') {
26. gzseekDemo(pathDir);
27. }
28. })
29. }
30. .width('100%')
31. }
32. .height('100%')
33. }
34. }
```

### gzrewind12+

PhonePC/2in1TabletTVWearable

gzrewind(): Promise<ReturnStatus>

将文件指针重新定位到文件的开头，此功能仅用于读取。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReturnStatus](js-apis-zlib.md#returnstatus12)> | Promise对象，返回结果状态。 |

**错误码：**

以下错误码的详细介绍请参见[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17800009 | Internal structure error. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzrewindDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzrewind");
6. let path = pathDir + "/gzrewind/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. await gzip.gzclose();
10. await gzip.gzopen(path, "rb");
11. let result = await gzip.gzrewind();
12. await gzip.gzclose();
13. }

15. @Entry
16. @Component
17. struct Index {
18. build() {
19. Row() {
20. Column() {
21. Button('test gzip interface')
22. .type(ButtonType.Capsule)
23. .height(60)
24. .width(200)
25. .onClick(() => {
26. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
27. if (typeof pathDir === 'string') {
28. gzrewindDemo(pathDir);
29. }
30. })
31. }
32. .width('100%')
33. }
34. .height('100%')
35. }
36. }
```

### gzread12+

PhonePC/2in1TabletTVWearable

gzread(buf: ArrayBuffer): Promise<number>

从文件中读取最多len个未压缩字节并将其解压缩到buf中。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 目标偏移位置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回实际读取的未压缩字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800009 | Internal structure error. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzreadDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzread");
6. let path = pathDir + "/gzread/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. let writeBuffer = new ArrayBuffer(16);
10. let uint8View = new Uint8Array(writeBuffer);
11. for (let i = 0; i < uint8View.length; i++) {
12. uint8View[i] = i;
13. }
14. await gzip.gzwrite(writeBuffer, 16);
15. await gzip.gzclose();
16. await gzip.gzopen(path, "rb");
17. let readBuffer = new ArrayBuffer(16);
18. let result = await gzip.gzread(readBuffer);
19. await gzip.gzclose();
20. }

22. @Entry
23. @Component
24. struct Index {
25. build() {
26. Row() {
27. Column() {
28. Button('test gzip interface')
29. .type(ButtonType.Capsule)
30. .height(60)
31. .width(200)
32. .onClick(() => {
33. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
34. if (typeof pathDir === 'string') {
35. gzreadDemo(pathDir);
36. }
37. })
38. }
39. .width('100%')
40. }
41. .height('100%')
42. }
43. }
```

### gzputs12+

PhonePC/2in1TabletTVWearable

gzputs(str: string): Promise<number>

压缩给定的以null结尾的字符串并将其写入文件，不包括终止的null字符。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | 格式化描述符和纯文本。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回写入的字符数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800009 | Internal structure error. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzputsDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzputs");
6. let path = pathDir + "/gzputs/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. let result = await gzip.gzputs("hello");
10. await gzip.gzclose();
11. }

13. @Entry
14. @Component
15. struct Index {
16. build() {
17. Row() {
18. Column() {
19. Button('test gzip interface')
20. .type(ButtonType.Capsule)
21. .height(60)
22. .width(200)
23. .onClick(() => {
24. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
25. if (typeof pathDir === 'string') {
26. gzputsDemo(pathDir);
27. }
28. })
29. }
30. .width('100%')
31. }
32. .height('100%')
33. }
34. }
```

### gzputc12+

PhonePC/2in1TabletTVWearable

gzputc(ch: number): Promise<number>

将转换为无符号字符的c压缩并写入文件。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ch | number | 是 | 写入字符ASCII。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回已写入的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800009 | Internal structure error. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzputcDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzputc");
6. let path = pathDir + "/gzputc/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. let result = await gzip.gzputc(0);
10. await gzip.gzclose();
11. }

13. @Entry
14. @Component
15. struct Index {
16. build() {
17. Row() {
18. Column() {
19. Button('test gzip interface')
20. .type(ButtonType.Capsule)
21. .height(60)
22. .width(200)
23. .onClick(() => {
24. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
25. if (typeof pathDir === 'string') {
26. gzputcDemo(pathDir);
27. }
28. })
29. }
30. .width('100%')
31. }
32. .height('100%')
33. }
34. }
```

### gzprintf12+

PhonePC/2in1TabletTVWearable

gzprintf(format: string, ...args: Array<string | number>): Promise<number>

在字符串格式的控制下，将参数转换和格式化后，压缩并写入文件，如fprintf中所示。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| format | string | 是 | 格式化描述符和纯文本。 |
| ...args | Array<string | number> | 否 | 可变参数列表。传入可变参数，例如gzprintf("name is %s, age is %d", "Tom", 23)，写入内容为“name is Tom, age is 23”。不传可变参数，例如gzprintf("name is %s, age is %d")，写入内容为“name is %s, age is %d”。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回实际写入的未压缩字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |
| 17800009 | Internal structure error. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzprintfDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzprintf");
6. let path = pathDir + "/gzprintf/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. let result = await gzip.gzprintf("name is %s, age is %d", "Tom", 23);
10. await gzip.gzclose();
11. }

13. @Entry
14. @Component
15. struct Index {
16. build() {
17. Row() {
18. Column() {
19. Button('test gzip interface')
20. .type(ButtonType.Capsule)
21. .height(60)
22. .width(200)
23. .onClick(() => {
24. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
25. if (typeof pathDir === 'string') {
26. gzprintfDemo(pathDir);
27. }
28. })
29. }
30. .width('100%')
31. }
32. .height('100%')
33. }
34. }
```

### gzoffset12+

PhonePC/2in1TabletTVWearable

gzoffset(): Promise<number>

返回文件的当前压缩（实际）读或写偏移量。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回文件的当前压缩（实际）读或写偏移量。 |

**错误码：**

以下错误码的详细介绍请参见[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17800009 | Internal structure error. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzoffsetDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzoffset");
6. let path = pathDir + "/gzoffset/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. let result = await gzip.gzoffset();
10. await gzip.gzclose();
11. }

13. @Entry
14. @Component
15. struct Index {
16. build() {
17. Row() {
18. Column() {
19. Button('test gzip interface')
20. .type(ButtonType.Capsule)
21. .height(60)
22. .width(200)
23. .onClick(() => {
24. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
25. if (typeof pathDir === 'string') {
26. gzoffsetDemo(pathDir);
27. }
28. })
29. }
30. .width('100%')
31. }
32. .height('100%')
33. }
34. }
```

### gzgets12+

PhonePC/2in1TabletTVWearable

gzgets(buf: ArrayBuffer): Promise<string>

从文件中读取字节并将其解压缩到buf中，直到读取len-1字符，或者直到读取换行符并将其传输到buf，或者遇到文件结束条件。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 存储读取的行数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回以null结尾的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[zlib子系统错误码](errorcode-zlib.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 17800009 | Internal structure error. |

**示例：**

```
1. import { zlib } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. async function gzgetsDemo(pathDir: string) {
5. fs.mkdirSync(pathDir + "/gzgets");
6. let path = pathDir + "/gzgets/test.gz";
7. let gzip = zlib.createGZipSync();
8. await gzip.gzopen(path, "wb");
9. await gzip.gzputs("hello");
10. await gzip.gzclose();
11. await gzip.gzopen(path, "rb");
12. let bufferWithData = new ArrayBuffer(16);
13. let result = await gzip.gzgets(bufferWithData);
14. await gzip.gzclose();
15. }

17. @Entry
18. @Component
19. struct Index {
20. build() {
21. Row() {
22. Column() {
23. Button('test gzip interface')
24. .type(ButtonType.Capsule)
25. .height(60)
26. .width(200)
27. .onClick(() => {
28. let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
29. if (typeof pathDir === 'string') {
30. gzgetsDemo(pathDir);
31. }
32. })
33. }
34. .width('100%')
35. }
36. .height('100%')
37. }
38. }
```

## GzErrorOutputInfo12+

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| status | ReturnStatus | 否 | 否 | 返回zlib文件状态码，参考ReturnStatus的定义。 |
| statusMsg | string | 否 | 否 | zlib文件上发生的最后一个状态的状态消息。 |

## OffsetReferencePoint12+

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SEEK\_SET | 0 | 从文件开头查找。 |
| SEEK\_CUR | 1 | 从当前位置查找。 |
