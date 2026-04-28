---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-print
title: @ohos.print (打印)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 数据文件处理 > @ohos.print (打印)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4d23de70db375207b2d819ebfdd847ee20790d161b7ada524a08b20d6b809f97
---

该模块为基本打印的操作API，提供调用基础打印功能的接口。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1Tablet

```
1. import { print } from '@kit.BasicServicesKit';
```

## PrintTask

PhonePC/2in1Tablet

打印任务完成后的事件监听回调接口类。

### on

PhonePC/2in1Tablet

on(type: 'block', callback: Callback<void>): void

注册打印任务阻塞的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 注册监听，  监听字段：block，  表示打印任务阻塞。 |
| callback | Callback<void> | 是 | 回调函数，通知调用方打印任务阻塞。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileUri } from '@kit.CoreFileKit';

5. let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
6. print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
7. printTask.on('block', () => {
8. console.info('print state is block');
9. })
10. // ...
11. }).catch((error: BusinessError) => {
12. console.error('print err ' + JSON.stringify(error));
13. })
```

### on

PhonePC/2in1Tablet

on(type: 'succeed', callback: Callback<void>): void

注册打印任务成功的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 注册监听，  监听字段：succeed，  表示打印任务成功。 |
| callback | Callback<void> | 是 | 回调函数，通知调用方打印任务成功。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileUri } from '@kit.CoreFileKit';

5. let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
6. print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
7. printTask.on('succeed', () => {
8. console.info('print state is succeed');
9. })
10. // ...
11. }).catch((error: BusinessError) => {
12. console.error('print err ' + JSON.stringify(error));
13. })
```

### on

PhonePC/2in1Tablet

on(type: 'fail', callback: Callback<void>): void

注册打印任务失败的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 注册监听，  监听字段：fail，  表示打印任务失败。 |
| callback | Callback<void> | 是 | 回调函数，通知调用方打印任务失败。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileUri } from '@kit.CoreFileKit';

5. let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
6. print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
7. printTask.on('fail', () => {
8. console.info('print state is fail');
9. })
10. // ...
11. }).catch((error: BusinessError) => {
12. console.error('print err ' + JSON.stringify(error));
13. })
```

### on

PhonePC/2in1Tablet

on(type: 'cancel', callback: Callback<void>): void

注册打印任务被取消的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 注册监听，  监听字段：cancel，  表示打印任务被取消。 |
| callback | Callback<void> | 是 | 回调函数，通知调用方打印任务被取消。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileUri } from '@kit.CoreFileKit';

5. let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
6. print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
7. printTask.on('cancel', () => {
8. console.info('print state is cancel');
9. })
10. // ...
11. }).catch((error: BusinessError) => {
12. console.error('print err ' + JSON.stringify(error));
13. })
```

### off

PhonePC/2in1Tablet

off(type: 'block', callback?: Callback<void>): void

取消打印任务阻塞的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听，  监听字段：block，  表示打印任务阻塞。 |
| callback | Callback<void> | 否 | 回调函数，取消指定的打印任务阻塞事件订阅。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileUri } from '@kit.CoreFileKit';

5. let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
6. print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
7. printTask.off('block', () => {
8. console.info('unregister state block');
9. })
10. // ...
11. }).catch((error: BusinessError) => {
12. console.error('print err ' + JSON.stringify(error));
13. })
```

### off

PhonePC/2in1Tablet

off(type: 'succeed', callback?: Callback<void>): void

取消打印任务成功的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听，  监听字段：succeed，  表示打印任务成功。 |
| callback | Callback<void> | 否 | 回调函数，取消指定的打印任务成功事件订阅。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileUri } from '@kit.CoreFileKit';

5. let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
6. print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
7. printTask.off('succeed', () => {
8. console.info('unregister state succeed');
9. })
10. // ...
11. }).catch((error: BusinessError) => {
12. console.error('print err ' + JSON.stringify(error));
13. })
```

### off

PhonePC/2in1Tablet

off(type: 'fail', callback?: Callback<void>): void

取消打印任务失败的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听，  监听字段：fail，  表示打印任务失败。 |
| callback | Callback<void> | 否 | 回调函数，取消指定的打印任务失败事件订阅。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileUri } from '@kit.CoreFileKit';

5. let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
6. print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
7. printTask.off('fail', () => {
8. console.info('unregister state fail');
9. })
10. // ...
11. }).catch((error: BusinessError) => {
12. console.error('print err ' + JSON.stringify(error));
13. })
```

### off

PhonePC/2in1Tablet

off(type: 'cancel', callback?: Callback<void>): void

取消打印任务被取消的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听，  监听字段：cancel，  表示打印任务被取消。 |
| callback | Callback<void> | 否 | 回调函数，取消指定的打印任务被取消事件订阅。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileUri } from '@kit.CoreFileKit';

5. let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
6. print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
7. printTask.off('cancel', () => {
8. console.info('unregister state cancel');
9. })
10. // ...
11. }).catch((error: BusinessError) => {
12. console.error('print err ' + JSON.stringify(error));
13. })
```

## PrintDocumentAdapter11+

PhonePC/2in1Tablet

第三方应用程序实现此接口来渲染要打印的文件。

### onStartLayoutWrite11+

PhonePC/2in1Tablet

onStartLayoutWrite(jobId: string, oldAttrs: PrintAttributes, newAttrs: PrintAttributes, fd: number, writeResultCallback: (jobId: string, writeResult: PrintFileCreationState) => void): void

打印服务会通过本接口将一个空的pdf文件的文件描述符传给三方应用，由三方应用使用新的打印参数更新待打印文件，更新文件完成后通过本接口的回调方法writeResultCallback通知打印服务。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| jobId | string | 是 | 表示打印任务ID。 |
| oldAttrs | [PrintAttributes](js-apis-print.md#printattributes11) | 是 | 表示旧打印参数。 |
| newAttrs | [PrintAttributes](js-apis-print.md#printattributes11) | 是 | 表示新打印参数。 |
| fd | number | 是 | 表示打印文件传给接口调用方的pdf文件的文件描述符。 |
| writeResultCallback | (jobId: string, writeResult: [PrintFileCreationState](js-apis-print.md#printfilecreationstate11)) => void | 是 | 表示三方应用使用新的打印参数更新待打印文件完成后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';

3. class MyPrintDocumentAdapter implements print.PrintDocumentAdapter {
4. onStartLayoutWrite(jobId: string, oldAttrs: print.PrintAttributes, newAttrs: print.PrintAttributes, fd: number,
5. writeResultCallback: (jobId: string, writeResult: print.PrintFileCreationState) => void) {
6. writeResultCallback(jobId, print.PrintFileCreationState.PRINT_FILE_CREATED);
7. };
8. onJobStateChanged(jobId: string, state: print.PrintDocumentAdapterState) {
9. if (state == print.PrintDocumentAdapterState.PREVIEW_DESTROY) {
10. console.info('PREVIEW_DESTROY');
11. } else if (state == print.PrintDocumentAdapterState.PRINT_TASK_SUCCEED) {
12. console.info('PRINT_TASK_SUCCEED');
13. } else if (state == print.PrintDocumentAdapterState.PRINT_TASK_FAIL) {
14. console.info('PRINT_TASK_FAIL');
15. } else if (state == print.PrintDocumentAdapterState.PRINT_TASK_CANCEL) {
16. console.info('PRINT_TASK_CANCEL');
17. } else if (state == print.PrintDocumentAdapterState.PRINT_TASK_BLOCK) {
18. console.info('PRINT_TASK_BLOCK');
19. }
20. }
21. }
```

### onJobStateChanged11+

PhonePC/2in1Tablet

onJobStateChanged(jobId: string, state: PrintDocumentAdapterState): void

实现这个接口来监听打印任务状态的改变。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| jobId | string | 是 | 表示打印任务ID。 |
| state | [PrintDocumentAdapterState](js-apis-print.md#printdocumentadapterstate11) | 是 | 表示打印任务更改为该状态。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class MyPrintDocumentAdapter implements print.PrintDocumentAdapter {
5. onStartLayoutWrite(jobId: string, oldAttrs: print.PrintAttributes, newAttrs: print.PrintAttributes, fd: number,
6. writeResultCallback: (jobId: string, writeResult: print.PrintFileCreationState) => void) {
7. writeResultCallback(jobId, print.PrintFileCreationState.PRINT_FILE_CREATED);
8. };
9. onJobStateChanged(jobId: string, state: print.PrintDocumentAdapterState) {
10. if (state == print.PrintDocumentAdapterState.PREVIEW_DESTROY) {
11. console.info('PREVIEW_DESTROY');
12. } else if (state == print.PrintDocumentAdapterState.PRINT_TASK_SUCCEED) {
13. console.info('PRINT_TASK_SUCCEED');
14. } else if (state == print.PrintDocumentAdapterState.PRINT_TASK_FAIL) {
15. console.info('PRINT_TASK_FAIL');
16. } else if (state == print.PrintDocumentAdapterState.PRINT_TASK_CANCEL) {
17. console.info('PRINT_TASK_CANCEL');
18. } else if (state == print.PrintDocumentAdapterState.PRINT_TASK_BLOCK) {
19. console.info('PRINT_TASK_BLOCK');
20. }
21. }
22. }
```

## print.print

PhonePC/2in1Tablet

print(files: Array<string>, callback: AsyncCallback<PrintTask>): void

打印接口，传入文件进行打印，使用callback异步回调。拉起系统打印预览界面，需要使用[print](js-apis-print.md#printprint11-1)接口，传入context。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 待打印文件列表，支持图片（.jpg .png .gif .bmp .webp）和pdf。文件需先保存到应用沙箱，通过fileUri.getUriFromPath获取到沙箱uri，再作为参数传入到本接口。 |
| callback | AsyncCallback<[PrintTask](js-apis-print.md#printtask)> | 是 | 异步获取打印完成之后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileUri } from '@kit.CoreFileKit';

5. // 传入文件的uri
6. let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
7. print.print([fileUri.getUriFromPath(filePath)], (err: BusinessError, printTask: print.PrintTask) => {
8. if (err) {
9. console.error('print err ' + JSON.stringify(err));
10. } else {
11. printTask.on('succeed', () => {
12. console.info('print state is succeed');
13. })
14. // ...
15. }
16. })
```

## print.print

PhonePC/2in1Tablet

print(files: Array<string>): Promise<PrintTask>

打印接口，传入文件进行打印，使用Promise异步回调。拉起系统打印预览界面，需要使用[print](js-apis-print.md#printprint11-1)接口，传入context。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 待打印文件列表，支持图片（.jpg .png .gif .bmp .webp）和pdf。文件需先保存到应用沙箱，通过fileUri.getUriFromPath获取到沙箱uri，再作为参数传入到本接口。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[PrintTask](js-apis-print.md#printtask)> | 打印完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileUri } from '@kit.CoreFileKit';

5. // 传入文件的uri
6. let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
7. print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
8. printTask.on('succeed', () => {
9. console.info('print state is succeed');
10. })
11. // ...
12. }).catch((error: BusinessError) => {
13. console.error('print err ' + JSON.stringify(error));
14. })
```

## print.print11+

PhonePC/2in1Tablet

print(files: Array<string>, context: Context, callback: AsyncCallback<PrintTask>): void

打印接口，传入文件进行打印，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 待打印文件列表，当前支持的文件类型：".bm", ".bmp", ".doc", ".docm", ".docx", ".dot", ".dotm", ".dotx", ".gif", ".jfif", ".jpe", ".jpeg", ".jpg", "pdf", ".pot", ".potm", ".potx", ".pps", ".ppsm", ".ppsx", ".ppt", ".pptm", ".pptx", ".png", ".rtf", ".txt", ".webp", ".wps", ".xls", ".xlsb", ".xlsm", ".xlsx", ".xlt", ".xltx", ".xml"。文件需先保存到应用沙箱，通过fileUri.getUriFromPath获取到沙箱uri，再作为参数传入到本接口。 |
| context | Context | 是 | 用于拉起系统打印界面的UIAbilityContext。 |
| callback | AsyncCallback<[PrintTask](js-apis-print.md#printtask)> | 是 | 异步获取打印完成之后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileUri } from '@kit.CoreFileKit';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. Scroll() {
10. Column({ space: 10 }) {
11. Button("打印").width('90%').height(50).onClick(() => {
12. let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
13. let context = this.getUIContext().getHostContext();
14. print.print([fileUri.getUriFromPath(filePath)], context, (err: BusinessError, printTask: print.PrintTask) => {
15. if (err) {
16. console.error('print err ' + JSON.stringify(err));
17. } else {
18. printTask.on('succeed', () => {
19. console.info('print state is succeed');
20. })
21. // ...
22. }
23. })
24. })
25. }
26. .justifyContent(FlexAlign.Center)
27. .constraintSize({ minHeight: '100%' })
28. .width('100%')
29. }
30. .height('100%')
31. }
32. }
```

## print.print11+

PhonePC/2in1Tablet

print(files: Array<string>, context: Context): Promise<PrintTask>

打印接口，传入文件进行打印，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 待打印文件列表，当前支持的文件类型：".bm", ".bmp", ".doc", ".docm", ".docx", ".dot", ".dotm", ".dotx", ".gif", ".jfif", ".jpe", ".jpeg", ".jpg", "pdf", ".pot", ".potm", ".potx", ".pps", ".ppsm", ".ppsx", ".ppt", ".pptm", ".pptx", ".png", ".rtf", ".txt", ".webp", ".wps", ".xls", ".xlsb", ".xlsm", ".xlsx", ".xlt", ".xltx", ".xml"。文件需先保存到应用沙箱，通过fileUri.getUriFromPath获取到沙箱uri，再作为参数传入到本接口。 |
| context | Context | 是 | 用于拉起系统打印界面的UIAbilityContext。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[PrintTask](js-apis-print.md#printtask)> | 打印完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileUri } from '@kit.CoreFileKit';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. Scroll() {
10. Column({ space: 10 }) {
11. Button("打印").width('90%').height(50).onClick(() => {
12. let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
13. let context = this.getUIContext().getHostContext();
14. print.print([fileUri.getUriFromPath(filePath)], context).then((printTask: print.PrintTask) => {
15. printTask.on('succeed', () => {
16. console.info('print state is succeed');
17. })
18. // ...
19. }).catch((error: BusinessError) => {
20. console.error('print err ' + JSON.stringify(error));
21. })
22. })
23. }
24. .justifyContent(FlexAlign.Center)
25. .constraintSize({ minHeight: '100%' })
26. .width('100%')
27. }
28. .height('100%')
29. }
30. }
```

## print.print11+

PhonePC/2in1Tablet

print(jobName: string, printAdapter: PrintDocumentAdapter, printAttributes: PrintAttributes, context: Context): Promise<PrintTask>

打印接口，传入文件进行打印，三方应用需要更新打印文件，使用Promise异步回调。当前支持的文件类型：".pdf"。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| jobName | string | 是 | 表示待打印文件名称，例如：test.pdf。当前仅支持".pdf"文件类型。打印侧会通过[onStartLayoutWrite](js-apis-print.md#onstartlayoutwrite11)接口将空的pdf文件的fd传给接口调用方，由调用方使用新的打印参数更新待打印文件。 |
| printAdapter | [PrintDocumentAdapter](js-apis-print.md#printdocumentadapter11) | 是 | 表示三方应用实现的[PrintDocumentAdapter](js-apis-print.md#printdocumentadapter11)接口实例。 |
| printAttributes | [PrintAttributes](js-apis-print.md#printattributes11) | 是 | 表示打印参数。 |
| context | Context | 是 | 用于拉起系统打印界面的UIAbilityContext。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[PrintTask](js-apis-print.md#printtask)> | 打印完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Scroll() {
9. Column({ space: 10 }) {
10. Button("打印").width('90%').height(50).onClick(() => {
11. let jobName : string = "jobName";
12. let printAdapter : print.PrintDocumentAdapter | null = null;
13. let printAttributes : print.PrintAttributes = {
14. copyNumber: 1,
15. pageRange: {
16. startPage: 0,
17. endPage: 5,
18. pages: []
19. },
20. pageSize: print.PrintPageType.PAGE_ISO_A3,
21. directionMode: print.PrintDirectionMode.DIRECTION_MODE_AUTO,
22. colorMode: print.PrintColorMode.COLOR_MODE_MONOCHROME,
23. duplexMode: print.PrintDuplexMode.DUPLEX_MODE_NONE
24. }
25. let context = this.getUIContext().getHostContext();

27. print.print(jobName, printAdapter, printAttributes, context).then((printTask: print.PrintTask) => {
28. printTask.on('succeed', () => {
29. console.info('print state is succeed');
30. })
31. // ...
32. }).catch((error: BusinessError) => {
33. console.error('print err ' + JSON.stringify(error));
34. })
35. })
36. }
37. .justifyContent(FlexAlign.Center)
38. .constraintSize({ minHeight: '100%' })
39. .width('100%')
40. }
41. .height('100%')
42. }
43. }
```

## PrintAttributes11+

PhonePC/2in1Tablet

定义打印参数的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| copyNumber | number | 否 | 是 | 表示文件打印份数。默认值为1。 |
| pageRange | [PrintPageRange](js-apis-print.md#printpagerange11) | 否 | 是 | 表示待打印文件的页面范围。 |
| pageSize | [PrintPageSize](js-apis-print.md#printpagesize11) | [PrintPageType](js-apis-print.md#printpagetype11) | 否 | 是 | 表示待打印文件的纸张类型。 |
| directionMode | [PrintDirectionMode](js-apis-print.md#printdirectionmode11) | 否 | 是 | 表示待打印文件的方向。 |
| colorMode | [PrintColorMode](js-apis-print.md#printcolormode11) | 否 | 是 | 表示待打印文件的色彩模式。 |
| duplexMode | [PrintDuplexMode](js-apis-print.md#printduplexmode11) | 否 | 是 | 表示待打印文件的单双面模式。 |

## PrintPageRange11+

PhonePC/2in1Tablet

定义打印范围的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| startPage | number | 否 | 是 | 表示起始页。默认值为1。 |
| endPage | number | 否 | 是 | 表示结束页。默认值为待打印文件的最大页数。 |
| pages | Array<number> | 否 | 是 | 表示待打印的页面范围的集合。默认值为空。 |

## PrintPageSize11+

PhonePC/2in1Tablet

定义打印页面尺寸的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 表示纸张类型ID。 |
| name | string | 否 | 否 | 表示纸张类型名称。 |
| width | number | 否 | 否 | 表示页面宽度，单位：毫米。 |
| height | number | 否 | 否 | 表示页面高度，单位：毫米。 |

## PrintDirectionMode11+

PhonePC/2in1Tablet

打印纸张方向的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| DIRECTION\_MODE\_AUTO | 0 | 表示自动选择纸张方向。 |
| DIRECTION\_MODE\_PORTRAIT | 1 | 表示纵向打印。 |
| DIRECTION\_MODE\_LANDSCAPE | 2 | 表示横向打印。 |

## PrintColorMode11+

PhonePC/2in1Tablet

打印色彩模式的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| COLOR\_MODE\_MONOCHROME | 0 | 表示黑白打印。 |
| COLOR\_MODE\_COLOR | 1 | 表示彩色打印。 |

## PrintDuplexMode11+

PhonePC/2in1Tablet

打印单双面模式的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| DUPLEX\_MODE\_NONE | 0 | 表示单面打印。 |
| DUPLEX\_MODE\_LONG\_EDGE | 1 | 表示双面打印沿长边翻转。 |
| DUPLEX\_MODE\_SHORT\_EDGE | 2 | 表示双面打印沿短边翻转。 |

## PrintPageType11+

PhonePC/2in1Tablet

打印纸张类型的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| PAGE\_ISO\_A3 | 0 | 表示A3。 |
| PAGE\_ISO\_A4 | 1 | 表示A4。 |
| PAGE\_ISO\_A5 | 2 | 表示A5。 |
| PAGE\_JIS\_B5 | 3 | 表示B5。 |
| PAGE\_ISO\_C5 | 4 | 表示C5。 |
| PAGE\_ISO\_DL | 5 | 表示DL。 |
| PAGE\_LETTER | 6 | 表示Letter。 |
| PAGE\_LEGAL | 7 | 表示Legal。 |
| PAGE\_PHOTO\_4X6 | 8 | 表示4x6相纸。 |
| PAGE\_PHOTO\_5X7 | 9 | 表示5x7相纸。 |
| PAGE\_INT\_DL\_ENVELOPE | 10 | 表示INT DL ENVELOPE。 |
| PAGE\_B\_TABLOID | 11 | 表示B Tabloid。 |

## PrintDocumentAdapterState11+

PhonePC/2in1Tablet

打印任务状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| PREVIEW\_DESTROY | 0 | 表示预览失败。 |
| PRINT\_TASK\_SUCCEED | 1 | 表示打印任务成功。 |
| PRINT\_TASK\_FAIL | 2 | 表示打印任务失败。 |
| PRINT\_TASK\_CANCEL | 3 | 表示打印任务取消。 |
| PRINT\_TASK\_BLOCK | 4 | 表示打印任务阻塞。 |

## PrintFileCreationState11+

PhonePC/2in1Tablet

打印文件创建状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| PRINT\_FILE\_CREATED | 0 | 表示打印文件创建成功。 |
| PRINT\_FILE\_CREATION\_FAILED | 1 | 表示打印文件创建失败。 |
| PRINT\_FILE\_CREATED\_UNRENDERED | 2 | 表示打印文件创建成功但未渲染。 |

## PrinterState14+

PhonePC/2in1Tablet

打印机状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| PRINTER\_ADDED | 0 | 表示新打印机到达。 |
| PRINTER\_REMOVED | 1 | 表示打印机丢失。 |
| PRINTER\_CAPABILITY\_UPDATED | 2 | 表示打印机更新。 |
| PRINTER\_CONNECTED | 3 | 表示打印机已连接。 |
| PRINTER\_DISCONNECTED | 4 | 表示打印机已断开连接。 |
| PRINTER\_RUNNING | 5 | 表示打印机正在运行。 |

## PrintJobState14+

PhonePC/2in1Tablet

打印任务状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| PRINT\_JOB\_PREPARE | 0 | 表示打印任务的初始状态。 |
| PRINT\_JOB\_QUEUED | 1 | 表示打印任务传送到打印机。 |
| PRINT\_JOB\_RUNNING | 2 | 表示执行打印任务。 |
| PRINT\_JOB\_BLOCKED | 3 | 表示打印任务已被阻止。 |
| PRINT\_JOB\_COMPLETED | 4 | 表示打印任务完成。 |

## PrintJobSubState14+

PhonePC/2in1Tablet

打印任务子状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| PRINT\_JOB\_COMPLETED\_SUCCESS | 0 | 表示打印任务成功。 |
| PRINT\_JOB\_COMPLETED\_FAILED | 1 | 表示打印任务失败。 |
| PRINT\_JOB\_COMPLETED\_CANCELLED | 2 | 表示打印任务已取消。 |
| PRINT\_JOB\_COMPLETED\_FILE\_CORRUPTED | 3 | 表示打印文件已损坏。 |
| PRINT\_JOB\_BLOCK\_OFFLINE | 4 | 表示打印处于离线状态。 |
| PRINT\_JOB\_BLOCK\_BUSY | 5 | 表示打印被其他进程占用。 |
| PRINT\_JOB\_BLOCK\_CANCELLED | 6 | 表示打印任务已取消。 |
| PRINT\_JOB\_BLOCK\_OUT\_OF\_PAPER | 7 | 表示打印纸张用完。 |
| PRINT\_JOB\_BLOCK\_OUT\_OF\_INK | 8 | 表示打印墨水用完。 |
| PRINT\_JOB\_BLOCK\_OUT\_OF\_TONER | 9 | 表示打印墨粉用完。 |
| PRINT\_JOB\_BLOCK\_JAMMED | 10 | 表示打印卡纸。 |
| PRINT\_JOB\_BLOCK\_DOOR\_OPEN | 11 | 表示打印盖开启。 |
| PRINT\_JOB\_BLOCK\_SERVICE\_REQUEST | 12 | 表示打印服务请求。 |
| PRINT\_JOB\_BLOCK\_LOW\_ON\_INK | 13 | 表示打印墨水不足。 |
| PRINT\_JOB\_BLOCK\_LOW\_ON\_TONER | 14 | 表示打印墨粉不足。 |
| PRINT\_JOB\_BLOCK\_REALLY\_LOW\_ON\_INK | 15 | 表示打印墨水量非常低。 |
| PRINT\_JOB\_BLOCK\_BAD\_CERTIFICATE | 16 | 表示打印证书有误。 |
| PRINT\_JOB\_BLOCK\_DRIVER\_EXCEPTION20+ | 17 | 表示打印驱动异常。 |
| PRINT\_JOB\_BLOCK\_ACCOUNT\_ERROR | 18 | 表示打印账户时出错。 |
| PRINT\_JOB\_BLOCK\_PRINT\_PERMISSION\_ERROR | 19 | 表示打印许可异常。 |
| PRINT\_JOB\_BLOCK\_PRINT\_COLOR\_PERMISSION\_ERROR | 20 | 表示彩色打印权限异常。 |
| PRINT\_JOB\_BLOCK\_NETWORK\_ERROR | 21 | 表示设备未连接到网络。 |
| PRINT\_JOB\_BLOCK\_SERVER\_CONNECTION\_ERROR | 22 | 表示无法连接服务器。 |
| PRINT\_JOB\_BLOCK\_LARGE\_FILE\_ERROR | 23 | 表示打印大文件异常。 |
| PRINT\_JOB\_BLOCK\_FILE\_PARSING\_ERROR | 24 | 表示文件分析异常。 |
| PRINT\_JOB\_BLOCK\_SLOW\_FILE\_CONVERSION | 25 | 表示文件转换太慢。 |
| PRINT\_JOB\_RUNNING\_UPLOADING\_FILES | 26 | 表示正在上传文件。 |
| PRINT\_JOB\_RUNNING\_CONVERTING\_FILES | 27 | 表示正在转换文件。 |
| PRINT\_JOB\_BLOCK\_FILE\_UPLOADING\_ERROR18+ | 30 | 表示文件上传失败。 |
| PRINT\_JOB\_BLOCK\_DRIVER\_MISSING20+ | 34 | 表示打印驱动缺失。 |
| PRINT\_JOB\_BLOCK\_INTERRUPT20+ | 35 | 表示打印任务中断。 |
| PRINT\_JOB\_BLOCK\_PRINTER\_UNAVAILABLE20+ | 98 | 表示打印机不可用。 |
| PRINT\_JOB\_BLOCK\_UNKNOWN | 99 | 表示打印未知问题。 |

## PrintErrorCode14+

PhonePC/2in1Tablet

打印错误代码的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| E\_PRINT\_NONE | 0 | 表示没有错误。 |
| E\_PRINT\_NO\_PERMISSION | 201 | 表示没有许可。 |
| E\_PRINT\_INVALID\_PARAMETER | 401 | 表示无效的参数。 |
| E\_PRINT\_GENERIC\_FAILURE | 13100001 | 表示一般打印失败。 |
| E\_PRINT\_RPC\_FAILURE | 13100002 | 表示RPC失败。 |
| E\_PRINT\_SERVER\_FAILURE | 13100003 | 表示打印服务失败。 |
| E\_PRINT\_INVALID\_EXTENSION | 13100004 | 表示打印扩展无效。 |
| E\_PRINT\_INVALID\_PRINTER | 13100005 | 表示打印机无效。 |
| E\_PRINT\_INVALID\_PRINT\_JOB | 13100006 | 表示打印任务无效。 |
| E\_PRINT\_FILE\_IO | 13100007 | 表示文件输入/输出错误。 |
| E\_PRINT\_TOO\_MANY\_FILES18+ | 13100010 | 表示文件数量超过上限，当前上限99个。 |

## ApplicationEvent14+

PhonePC/2in1Tablet

打印应用事件的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| APPLICATION\_CREATED | 0 | 表示打印应用被拉起的事件。 |
| APPLICATION\_CLOSED\_FOR\_STARTED | 1 | 表示由于点击打印而关闭打印应用的事件。 |
| APPLICATION\_CLOSED\_FOR\_CANCELED | 2 | 表示由于点击取消而关闭打印应用的事件。 |

## print.addPrinterToDiscovery14+

PhonePC/2in1Tablet

addPrinterToDiscovery(printerInformation: PrinterInformation): Promise<void>

添加打印机到系统打印机发现列表，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| printerInformation | [PrinterInformation](js-apis-print.md#printerinformation14) | 是 | 表示新发现的打印机。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 添加打印机到系统打印机发现列表完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let printerInformation : print.PrinterInformation = {
5. printerId : 'testPrinterId',
6. printerName : 'testPrinterName',
7. printerStatus : 0,
8. description : 'testDesc',
9. uri : 'testUri',
10. printerMake : 'testPrinterMake',
11. options : 'testOps'
12. };
13. print.addPrinterToDiscovery(printerInformation).then(() => {
14. console.info('addPrinterToDiscovery success');
15. }).catch((error: BusinessError) => {
16. console.error('addPrinterToDiscovery error : ' + JSON.stringify(error));
17. })
```

## print.updatePrinterInDiscovery14+

PhonePC/2in1Tablet

updatePrinterInDiscovery(printerInformation: PrinterInformation): Promise<void>

更新打印机能力到系统打印机发现列表，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| printerInformation | [PrinterInformation](js-apis-print.md#printerinformation14) | 是 | 表示待更新能力的打印机。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 更新打印机能力到系统打印机发现列表完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let testPageSize : print.PrintPageSize = {
5. id : 'ISO_A4',
6. name : 'iso_a4_210x297mm',
7. width : 8268,
8. height : 11692
9. };

11. let testCapability : print.PrinterCapabilities = {
12. supportedPageSizes : [testPageSize],
13. supportedColorModes : [print.PrintColorMode.COLOR_MODE_MONOCHROME],
14. supportedDuplexModes : [print.PrintDuplexMode.DUPLEX_MODE_NONE],
15. supportedMediaTypes : ['stationery'],
16. supportedQualities : [print.PrintQuality.QUALITY_NORMAL],
17. supportedOrientations : [print.PrintOrientationMode.ORIENTATION_MODE_PORTRAIT],
18. options : 'testOptions'
19. };

21. let printerInformation : print.PrinterInformation = {
22. printerId : 'testPrinterId',
23. printerName : 'testPrinterName',
24. printerStatus : 0,
25. description : 'testDesc',
26. capability : testCapability,
27. uri : 'testUri',
28. printerMake : 'testPrinterMake',
29. options : 'testOptions'
30. };
31. print.updatePrinterInDiscovery(printerInformation).then(() => {
32. console.info('updatePrinterInDiscovery success');
33. }).catch((error: BusinessError) => {
34. console.error('updatePrinterInDiscovery error : ' + JSON.stringify(error));
35. })
```

## print.removePrinterFromDiscovery14+

PhonePC/2in1Tablet

removePrinterFromDiscovery(printerId: string): Promise<void>

从系统打印机发现列表里移除打印机，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| printerId | string | 是 | 表示待移除的打印机。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 从系统打印机发现列表里移除打印机完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let printerId : string = 'testPrinterId';
5. print.removePrinterFromDiscovery(printerId).then(() => {
6. console.info('removePrinterFromDiscovery success');
7. }).catch((error: BusinessError) => {
8. console.error('removePrinterFromDiscovery error : ' + JSON.stringify(error));
9. })
```

## print.getPrinterInformationById14+

PhonePC/2in1Tablet

getPrinterInformationById(printerId: string): Promise<PrinterInformation>

根据打印机id获取打印机信息，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| printerId | string | 是 | 表示待获取信息的打印机id。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[PrinterInformation](js-apis-print.md#printerinformation14)> | 根据打印机id获取的对应打印机信息。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let printerId : string = 'testPrinterId';
5. print.getPrinterInformationById(printerId).then((printerInformation : print.PrinterInformation) => {
6. console.info('getPrinterInformationById data : ' + JSON.stringify(printerInformation));
7. }).catch((error: BusinessError) => {
8. console.error('getPrinterInformationById error : ' + JSON.stringify(error));
9. })
```

## PrinterInformation14+

PhonePC/2in1Tablet

定义打印机信息的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| printerId | string | 否 | 否 | 表示打印机ID。 |
| printerName | string | 否 | 否 | 表示打印机名称。 |
| printerStatus | [PrinterStatus](js-apis-print.md#printerstatus14) | 否 | 否 | 表示当前打印机状态。 |
| description | string | 否 | 是 | 表示打印机说明。 |
| capability | [PrinterCapabilities](js-apis-print.md#printercapabilities14) | 否 | 是 | 表示打印机能力。 |
| uri | string | 否 | 是 | 表示打印机uri。 |
| printerMake | string | 否 | 是 | 表示打印机型号。 |
| preferences18+ | [PrinterPreferences](js-apis-print.md#printerpreferences18) | 否 | 是 | 表示打印机首选项。 |
| alias18+ | string | 否 | 是 | 表示打印机别名。 |
| options | string | 否 | 是 | 表示打印机详细信息。 |

## PrinterCapabilities14+

PhonePC/2in1Tablet

定义打印机能力的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| supportedPageSizes | Array<[PrintPageSize](js-apis-print.md#printpagesize11)> | 否 | 否 | 表示打印机支持的纸张尺寸列表。 |
| supportedColorModes | Array<[PrintColorMode](js-apis-print.md#printcolormode11)> | 否 | 否 | 表示打印机支持的色彩模式列表。 |
| supportedDuplexModes | Array<[PrintDuplexMode](js-apis-print.md#printduplexmode11)> | 否 | 否 | 表示打印机支持的单双面模式列表。 |
| supportedMediaTypes | Array<string> | 否 | 是 | 表示打印机支持的纸张类型列表。 |
| supportedQualities | Array<[PrintQuality](js-apis-print.md#printquality14)> | 否 | 是 | 表示打印机支持的打印质量列表。 |
| supportedOrientations | Array<[PrintOrientationMode](js-apis-print.md#printorientationmode14)> | 否 | 是 | 表示打印机支持的打印方向列表。 |
| options | string | 否 | 是 | 表示打印机能力详细信息。 |

## PrintQuality14+

PhonePC/2in1Tablet

打印质量的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| QUALITY\_DRAFT | 3 | 表示经济的打印质量。 |
| QUALITY\_NORMAL | 4 | 表示标准的打印质量。 |
| QUALITY\_HIGH | 5 | 表示最佳的打印质量。 |

## PrintOrientationMode14+

PhonePC/2in1Tablet

打印方向的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| ORIENTATION\_MODE\_PORTRAIT | 0 | 表示纵向打印。 |
| ORIENTATION\_MODE\_LANDSCAPE | 1 | 表示横向打印。 |
| ORIENTATION\_MODE\_REVERSE\_LANDSCAPE | 2 | 表示横向翻转打印。 |
| ORIENTATION\_MODE\_REVERSE\_PORTRAIT | 3 | 表示纵向翻转打印。 |
| ORIENTATION\_MODE\_NONE | 4 | 表示自适应方向打印。 |

## PrinterStatus14+

PhonePC/2in1Tablet

打印机状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| PRINTER\_IDLE | 0 | 表示打印机空闲状态。 |
| PRINTER\_BUSY | 1 | 表示打印机忙碌状态。 |
| PRINTER\_UNAVAILABLE | 2 | 表示打印机脱机状态。 |

## PrinterPreferences18+

PhonePC/2in1Tablet

定义打印机首选项的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| defaultDuplexMode | [PrintDuplexMode](js-apis-print.md#printduplexmode11) | 否 | 是 | 表示默认单双面模式。 |
| defaultPrintQuality | [PrintQuality](js-apis-print.md#printquality14) | 否 | 是 | 表示默认打印质量。 |
| defaultMediaType | string | 否 | 是 | 表示默认纸张类型。 |
| defaultPageSizeId | string | 否 | 是 | 表示默认纸张尺寸的ID，其范围包含国际标准化组织定义的标准纸张尺寸，如ISO\_A4，和系统中定义的非标准的纸张尺寸，如Custom.178x254mm，表示这种纸张尺寸为178毫米 x 254毫米。 |
| defaultOrientation | [PrintOrientationMode](js-apis-print.md#printorientationmode14) | 否 | 是 | 表示默认打印方向。 |
| borderless | boolean | 否 | 是 | 表示是否无边距打印，true表示无边距，false表示有边距。默认值为false。 |
| options | string | 否 | 是 | 表示打印机首选项中不在以上字段中的其他字段，查询打印机或者从打印机驱动获取，以json格式存储在string中。 |

## PrinterEvent18+

PhonePC/2in1Tablet

打印机相关事件的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| PRINTER\_EVENT\_ADDED | 0 | 表示打印机添加事件。 |
| PRINTER\_EVENT\_DELETED | 1 | 表示打印机删除事件。 |
| PRINTER\_EVENT\_STATE\_CHANGED | 2 | 表示打印机状态变化事件。 |
| PRINTER\_EVENT\_INFO\_CHANGED | 3 | 表示打印机信息变化事件。 |
| PRINTER\_EVENT\_PREFERENCE\_CHANGED | 4 | 表示打印机首选项变化事件。 |
| PRINTER\_EVENT\_LAST\_USED\_PRINTER\_CHANGED | 5 | 表示上次使用的打印机的变化事件。 |

## DefaultPrinterType18+

PhonePC/2in1Tablet

默认打印类型的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| **名称** | **值** | **说明** |
| --- | --- | --- |
| DEFAULT\_PRINTER\_TYPE\_SET\_BY\_USER | 0 | 表示将用户手动设置的默认打印机作为当前默认打印机。 |
| DEFAULT\_PRINTER\_TYPE\_LAST\_USED\_PRINTER | 1 | 表示自动将上次使用的打印机作为当前默认打印机。 |

## print.getAddedPrinters18+

PhonePC/2in1Tablet

getAddedPrinters(): Promise<Array<string>>

获取系统中已添加的打印机列表，使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB or ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<Array<string>> | 获取系统中已添加的打印机列表的完成结果回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. print.getAddedPrinters().then((printers: string[]) => {
5. console.info('getAddedPrinters success ' + JSON.stringify(printers));
6. // ...
7. }).catch((error: BusinessError) => {
8. console.error('failed to getAddedPrinters because ' + JSON.stringify(error));
9. })
```

## PrinterChangeCallback18+

PhonePC/2in1Tablet

type PrinterChangeCallback = (event: PrinterEvent, printerInformation: PrinterInformation) => void

将打印机事件和打印机信息作为参数的回调方法。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| event | [PrinterEvent](js-apis-print.md#printerevent18) | 是 | 表示打印机事件。 |
| printerInformation | [PrinterInformation](js-apis-print.md#printerinformation14) | 是 | 表示打印机信息。 |

## print.on18+

PhonePC/2in1Tablet

on(type: 'printerChange', callback: PrinterChangeCallback): void

注册打印机变动事件回调，使用callback回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | 'printerChange' | 是 | 表示打印机变动事件。 |
| callback | [PrinterChangeCallback](js-apis-print.md#printerchangecallback18) | 是 | 打印机变动之后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';

3. // Trigger this callback when a added printer is changed.
4. let onPrinterChange =
5. (event: print.PrinterEvent, printerInformation: print.PrinterInformation) => {
6. console.info('printerChange, event: ' + event + ', printerInformation: ' + JSON.stringify(printerInformation));
7. };
8. print.on('printerChange', onPrinterChange);
```

## print.off18+

PhonePC/2in1Tablet

off(type: 'printerChange', callback?: PrinterChangeCallback): void

取消注册打印机变动事件回调，使用callback回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | 'printerChange' | 是 | 表示打印机变动事件。 |
| callback | [PrinterChangeCallback](js-apis-print.md#printerchangecallback18) | 否 | 表示取消注册打印机变动事件后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';

3. // Trigger this callback when a added printer is changed.
4. let onPrinterChange =
5. (event: print.PrinterEvent, printerInformation: print.PrinterInformation) => {
6. console.info('printerChange, event: ' + event + ', printerInformation: ' + JSON.stringify(printerInformation));
7. };
8. print.on('printerChange', onPrinterChange);
9. print.off('printerChange');
```

## print.startDiscoverPrinter20+

PhonePC/2in1Tablet

startDiscoverPrinter(extensionList: Array<string>, callback: AsyncCallback<void>): void

通过指定“打印扩展能力列表”来发现打印机，发现的打印机具备包含指定的打印扩展能力。如果指定空的打印扩展能力列表，则表示加载所有扩展能力。使用callback异步回调。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| extensionList | Array<string> | 是 | 要加载的[打印扩展能力](js-apis-app-ability-printextensionability.md)列表，列表成员为打印扩展能力的包名，空列表表示加载所有扩展能力。 |
| callback | AsyncCallback<void> | 是 | 异步开始发现打印机之后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 加载所有打印扩展能力
5. let extensionList: string[] = [];
6. // 通过指定自己应用的包名，在发现时加载自己的打印扩展能力
7. // let extensionList: string[] = ['com.myapplication.test'];
8. print.startDiscoverPrinter(extensionList, (err: BusinessError) => {
9. if (err) {
10. console.error('failed to start Discover Printer because : ' + JSON.stringify(err));
11. } else {
12. console.info('start Discover Printer success');
13. }
14. })
```

## print.startDiscoverPrinter20+

PhonePC/2in1Tablet

startDiscoverPrinter(extensionList: Array<string>): Promise<void>

通过指定“打印扩展能力列表”来发现打印机，发现的打印机具备包含指定的打印扩展能力。如果指定空的打印扩展能力列表，则表示加载所有扩展能力，使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| extensionList | Array<string> | 是 | 要加载的[打印扩展能力](js-apis-app-ability-printextensionability.md)列表，列表成员为打印扩展能力的包名，空列表表示加载所有扩展能力。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 开始发现打印机的完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 加载所有打印扩展能力
5. let extensionList: string[] = [];
6. // 通过指定自己应用的包名，在发现时加载自己的打印扩展能力
7. // let extensionList: string[] = ['com.myapplication.test'];
8. print.startDiscoverPrinter(extensionList).then(() => {
9. console.info('start Discovery success');
10. }).catch((error: BusinessError) => {
11. console.error('failed to start Discovery because : ' + JSON.stringify(error));
12. })
```

## print.stopDiscoverPrinter20+

PhonePC/2in1Tablet

stopDiscoverPrinter(callback: AsyncCallback<void>): void

停止发现打印机，使用callback异步回调。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 停止发现打印机的异步回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. print.stopDiscoverPrinter((err: BusinessError) => {
5. if (err) {
6. console.error('failed to stop Discover Printer because : ' + JSON.stringify(err));
7. } else {
8. console.info('stop Discover Printer success');
9. }
10. })
```

## print.stopDiscoverPrinter20+

PhonePC/2in1Tablet

stopDiscoverPrinter(): Promise<void>

停止发现打印机，使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 停止发现打印机的完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. print.stopDiscoverPrinter().then(() => {
5. console.info('stop Discovery success');
6. }).catch((error: BusinessError) => {
7. console.error('failed to stop Discovery because : ' + JSON.stringify(error));
8. })
```

## print.connectPrinter20+

PhonePC/2in1Tablet

connectPrinter(printerId: string, callback: AsyncCallback<void>): void

通过打印机ID连接打印机，使用callback异步回调。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| printerId | string | 是 | 打印机ID。 |
| callback | AsyncCallback<void> | 是 | 通过打印机ID异步连接打印机的回调。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let printerId: string = 'printerId_32';
5. print.connectPrinter(printerId, (err: BusinessError) => {
6. if (err) {
7. console.error('failed to connect Printer because : ' + JSON.stringify(err));
8. } else {
9. console.info('start connect Printer success');
10. }
11. })
```

## print.connectPrinter20+

PhonePC/2in1Tablet

connectPrinter(printerId: string): Promise<void>

通过打印机ID连接打印机，使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| printerId | string | 是 | 打印机ID |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | 通过打印机ID连接打印机完成结果。 |

**错误码：**

以下错误码的详细介绍请参见[打印服务错误码](errorcode-print.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let printerId: string = 'printerId_32';
5. print.connectPrinter(printerId).then(() => {
6. console.info('start connect Printer success');
7. }).catch((error: BusinessError) => {
8. console.error('failed to connect Printer because : ' + JSON.stringify(error));
9. })
```

## print.startPrint23+

PhonePC/2in1Tablet

startPrint(job: PrintJobData): Promise<void>

打印接口，传入文件或者二进制数据进行打印，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| job | [PrintJobData](js-apis-print.md#printjobdata23) | 是 | 打印任务数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```
1. import { print } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileIo } from '@kit.CoreFileKit';

5. let tempPath = '/data/stroage/el2/base/haps/entry/files/note.jpg';
6. let file: fileIo.File;
7. file = fileIo.openSync(tempPath, 4);

9. let printJobData: print.PrintJobData = {
10. printerId: "printerId",
11. jobName: "jobName",
12. documentFormat: print.PrintDocumentFormat.DOCUMENT_FORMAT_AUTO,
13. docFlavor: print.DocFlavor.FILE_DESCRIPTOR,
14. copyNumber: 1,
15. isLandscape: false,
16. colorMode: print.PrintColorMode.COLOR_MODE_MONOCHROME,
17. duplexMode: print.PrintDuplexMode.DUPLEX_MODE_NONE,
18. pageSize: {id: "ISO_A4", name: "ISO_A4", width:8268, height: 11692},
19. fdList: [file.fd],
20. }
21. print.startPrint(printJobData).then(() => {
22. console.info('start print success');
23. }).catch((error: BusinessError) => {
24. console.error('failed to print because : ' + JSON.stringify(error));
25. })
```

## PrintDocumentFormat23+

PhonePC/2in1Tablet

打印数据格式的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DOCUMENT\_FORMAT\_AUTO | 0 | 表示自动检测格式。 |
| DOCUMENT\_FORMAT\_JPEG | 1 | 表示Jpeg格式。 |
| DOCUMENT\_FORMAT\_PDF | 2 | 表示PDF格式。 |
| DOCUMENT\_FORMAT\_POSTSCRIPT | 3 | 表示PostScript格式。 |
| DOCUMENT\_FORMAT\_TEXT | 4 | 表示文本格式。 |
| DOCUMENT\_FORMAT\_RAW | 5 | 表示RAW格式。 |

## DocFlavor23+

PhonePC/2in1Tablet

打印数据来源形式的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FILE\_DESCRIPTOR | 0 | 表示文件数据。 |
| BYTES | 1 | 表示二进制数据。 |

## PrintJobData23+

PhonePC/2in1Tablet

定义打印任务的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| printerId | string | 否 | 否 | 表示打印机ID。 |
| jobName | string | 否 | 否 | 表示打印任务名称。 |
| documentFormat | [PrintDocumentFormat](js-apis-print.md#printdocumentformat23) | 否 | 否 | 表示打印数据格式。 |
| docFlavor | [DocFlavor](js-apis-print.md#docflavor23) | 否 | 否 | 表示打印数据来源形式。 |
| copyNumber | number | 否 | 否 | 表示文件列表副本数。 |
| isLandscape | boolean | 否 | 否 | 表示是否横向打印。true表示横向打印，false表示纵向打印。默认值为false。 |
| colorMode | [PrintColorMode](js-apis-print.md#printcolormode11) | 否 | 否 | 表示色彩模式。 |
| duplexMode | [PrintDuplexMode](js-apis-print.md#printduplexmode11) | 否 | 否 | 表示单双面打印模式。 |
| pageSize | [PrintPageSize](js-apis-print.md#printpagesize11) | 否 | 否 | 表示选定的页面尺寸。 |
| jobId | string | 否 | 是 | 表示打印任务的唯一标识符。 |
| fdList | number[]; | 否 | 是 | 表示待打印文件fd列表。 |
| binaryData | Uint8Array | 否 | 是 | 表示待打印二进制数据。 |
| printQuality | [PrintQuality](js-apis-print.md#printquality14) | 否 | 是 | 表示打印质量。 |
| mediaType | string | 否 | 是 | 表示打印纸张类型。 |
| isBorderless | boolean | 否 | 是 | 表示是否无边框打印。true表示无边框打印，false表示有边框打印。默认值为true。 |
| isAutoRotate | boolean | 否 | 是 | 表示是否自动旋转页面。true表示自动旋转页面，false表示不自动旋转页面。默认值为true。 |
| isReverse | boolean | 否 | 是 | 表示是否逆序打印。true表示逆序打印，false表示顺序打印。默认值为false。 |
| isCollate | boolean | 否 | 是 | 表示打印顺序方式。true表示逐页打印，false表示逐份打印。默认值为true。 |
| isSequential | boolean | 否 | 是 | 表示是否连续打印。true表示连续打印，false表示不连续打印。默认值为false。 |
| options | string | 否 | 是 | 表示以JSON格式字符串化的对象。 |
