---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-print
title: "@ohos.print (打印)"
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 数据文件处理 > @ohos.print (打印)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1375368c517e2110346002f250bc789ae0b9746d9089659193de7f640cb60dab
---

该模块提供打印相关的操作接口，支持文件打印、打印任务事件监听、打印机发现与管理、打印任务状态更新等功能，适用于需要在应用内集成打印相关能力的场景。

**说明** 

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { print } from '@kit.BasicServicesKit';
```

## PrintTask

打印任务状态变化的事件监听回调接口类，用于监听打印任务执行过程中的状态变化事件（如阻塞、成功、失败、取消等）。通过print.print接口获取PrintTask实例后，可注册监听打印任务的状态变化事件。

### on

on(type: 'block', callback: Callback<void>): void

注册打印任务阻塞的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册监听，  监听字段：block，  表示打印任务阻塞。 |
| callback | Callback<void> | 是 | 回调函数，通知调用方打印任务阻塞。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button('打印').width('90%').height(50).onClick(() => {
                    let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
                    let context = this.getUIContext().getHostContext();
                    print.print([fileUri.getUriFromPath(filePath)], context).then((printTask: print.PrintTask) => {
                        printTask.on('block', () => {
                            console.info('print state is block');
                        })
                        // ...
                    }).catch((error: BusinessError) => {
                        console.error(`Failed to print. Code: ${error.code}, message: ${error.message}`);
                    })
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}
```

### on

on(type: 'succeed', callback: Callback<void>): void

注册打印任务成功的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册监听，  监听字段：succeed，  表示打印任务成功。 |
| callback | Callback<void> | 是 | 回调函数，通知调用方打印任务成功。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button('打印').width('90%').height(50).onClick(() => {
                    let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
                    let context = this.getUIContext().getHostContext();
                    print.print([fileUri.getUriFromPath(filePath)], context).then((printTask: print.PrintTask) => {
                        printTask.on('succeed', () => {
                            console.info('print state is succeed');
                        })
                        // ...
                    }).catch((error: BusinessError) => {
                        console.error(`Failed to print. Code: ${error.code}, message: ${error.message}`);
                    })
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}
```

### on

on(type: 'fail', callback: Callback<void>): void

注册打印任务失败的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册监听，  监听字段：fail，  表示打印任务失败。 |
| callback | Callback<void> | 是 | 回调函数，通知调用方打印任务失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button('打印').width('90%').height(50).onClick(() => {
                    let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
                    let context = this.getUIContext().getHostContext();
                    print.print([fileUri.getUriFromPath(filePath)], context).then((printTask: print.PrintTask) => {
                        printTask.on('fail', () => {
                            console.info('print state is fail');
                        })
                        // ...
                    }).catch((error: BusinessError) => {
                        console.error(`Failed to print. Code: ${error.code}, message: ${error.message}`);
                    })
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}
```

### on

on(type: 'cancel', callback: Callback<void>): void

注册打印任务被取消的监听，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册监听，  监听字段：cancel，  表示打印任务被取消。 |
| callback | Callback<void> | 是 | 回调函数，通知调用方打印任务被取消。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button('打印').width('90%').height(50).onClick(() => {
                    let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
                    let context = this.getUIContext().getHostContext();
                    print.print([fileUri.getUriFromPath(filePath)], context).then((printTask: print.PrintTask) => {
                        printTask.on('cancel', () => {
                            console.info('print state is cancel');
                        })
                        // ...
                    }).catch((error: BusinessError) => {
                        console.error(`Failed to print. Code: ${error.code}, message: ${error.message}`);
                    })
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}
```

### off

off(type: 'block', callback?: Callback<void>): void

取消打印任务阻塞的监听。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听，  监听字段：block，  表示打印任务阻塞。 |
| callback | Callback<void> | 否 | 回调函数，取消指定的打印任务阻塞事件订阅。不传入时取消调用方所有已注册的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button('打印').width('90%').height(50).onClick(() => {
                    let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
                    let context = this.getUIContext().getHostContext();
                    print.print([fileUri.getUriFromPath(filePath)], context).then((printTask: print.PrintTask) => {
                        printTask.off('block', () => {
                            console.info('unregister state block');
                        })
                        // ...
                    }).catch((error: BusinessError) => {
                        console.error(`Failed to print. Code: ${error.code}, message: ${error.message}`);
                    })
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}
```

### off

off(type: 'succeed', callback?: Callback<void>): void

取消打印任务成功的监听。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听，  监听字段：succeed，  表示打印任务成功。 |
| callback | Callback<void> | 否 | 回调函数，取消指定的打印任务成功事件订阅。不传入时取消调用方所有已注册的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button('打印').width('90%').height(50).onClick(() => {
                    let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
                    let context = this.getUIContext().getHostContext();
                    print.print([fileUri.getUriFromPath(filePath)], context).then((printTask: print.PrintTask) => {
                        printTask.off('succeed', () => {
                            console.info('unregister state succeed');
                        })
                        // ...
                    }).catch((error: BusinessError) => {
                        console.error(`Failed to print. Code: ${error.code}, message: ${error.message}`);
                    })
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}
```

### off

off(type: 'fail', callback?: Callback<void>): void

取消打印任务失败的监听。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听，  监听字段：fail，  表示打印任务失败。 |
| callback | Callback<void> | 否 | 回调函数，取消指定的打印任务失败事件订阅。不传入时取消调用方所有已注册的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button('打印').width('90%').height(50).onClick(() => {
                    let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
                    let context = this.getUIContext().getHostContext();
                    print.print([fileUri.getUriFromPath(filePath)], context).then((printTask: print.PrintTask) => {
                        printTask.off('fail', () => {
                            console.info('unregister state fail');
                        })
                        // ...
                    }).catch((error: BusinessError) => {
                        console.error(`Failed to print. Code: ${error.code}, message: ${error.message}`);
                    })
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}
```

### off

off(type: 'cancel', callback?: Callback<void>): void

取消打印任务被取消的监听。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听，  监听字段：cancel，  表示打印任务被取消。 |
| callback | Callback<void> | 否 | 回调函数，取消指定的打印任务被取消事件订阅。不传入时取消调用方所有已注册的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button('打印').width('90%').height(50).onClick(() => {
                    let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
                    let context = this.getUIContext().getHostContext();
                    print.print([fileUri.getUriFromPath(filePath)], context).then((printTask: print.PrintTask) => {
                        printTask.off('cancel', () => {
                            console.info('unregister state cancel');
                        })
                        // ...
                    }).catch((error: BusinessError) => {
                        console.error(`Failed to print. Code: ${error.code}, message: ${error.message}`);
                    })
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}
```

## PrintDocumentAdapter11+

三方应用实现此接口来渲染要打印的文件。该接口提供文件渲染和打印任务状态监听等回调方法，可通过print.print接口传入PrintDocumentAdapter实例配合使用。

### onStartLayoutWrite11+

onStartLayoutWrite(jobId: string, oldAttrs: PrintAttributes, newAttrs: PrintAttributes, fd: number, writeResultCallback: (jobId: string, writeResult: PrintFileCreationState) => void): void

打印服务通过本接口将一个空的PDF文件的文件描述符传给三方应用。三方应用使用新的打印参数更新待打印文件。更新完成后，三方应用通过回调方法writeResultCallback通知打印服务。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jobId | string | 是 | 表示打印任务ID。 |
| oldAttrs | [PrintAttributes](js-apis-print.md#printattributes11) | 是 | 表示旧打印参数。 |
| newAttrs | [PrintAttributes](js-apis-print.md#printattributes11) | 是 | 表示新打印参数，应用使用该参数更新待打印文件。 |
| fd | number | 是 | 表示打印服务传给接口调用方的PDF文件的文件描述符。 |
| writeResultCallback | (jobId: string, writeResult: [PrintFileCreationState](js-apis-print.md#printfilecreationstate11)) => void | 是 | 表示三方应用使用新的打印参数更新待打印文件完成后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';

class MyPrintDocumentAdapter implements print.PrintDocumentAdapter {
    onStartLayoutWrite(jobId: string, oldAttrs: print.PrintAttributes, newAttrs: print.PrintAttributes, fd: number,
        writeResultCallback: (jobId: string, writeResult: print.PrintFileCreationState) => void) {
        writeResultCallback(jobId, print.PrintFileCreationState.PRINT_FILE_CREATED);
    }
    onJobStateChanged(jobId: string, state: print.PrintDocumentAdapterState) {
        if (state === print.PrintDocumentAdapterState.PREVIEW_DESTROY) {
            console.info('PREVIEW_DESTROY');
        } else if (state === print.PrintDocumentAdapterState.PRINT_TASK_SUCCEED) {
            console.info('PRINT_TASK_SUCCEED');
        } else if (state === print.PrintDocumentAdapterState.PRINT_TASK_FAIL) {
            console.info('PRINT_TASK_FAIL');
        } else if (state === print.PrintDocumentAdapterState.PRINT_TASK_CANCEL) {
            console.info('PRINT_TASK_CANCEL');
        } else if (state === print.PrintDocumentAdapterState.PRINT_TASK_BLOCK) {
            console.info('PRINT_TASK_BLOCK');
        }
    }
}
```

### onJobStateChanged11+

onJobStateChanged(jobId: string, state: PrintDocumentAdapterState): void

实现这个接口来监听打印任务状态的改变。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jobId | string | 是 | 表示打印任务ID。 |
| state | [PrintDocumentAdapterState](js-apis-print.md#printdocumentadapterstate11) | 是 | 表示打印任务更改为该状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyPrintDocumentAdapter implements print.PrintDocumentAdapter {
    onStartLayoutWrite(jobId: string, oldAttrs: print.PrintAttributes, newAttrs: print.PrintAttributes, fd: number,
        writeResultCallback: (jobId: string, writeResult: print.PrintFileCreationState) => void) {
        writeResultCallback(jobId, print.PrintFileCreationState.PRINT_FILE_CREATED);
    }
    onJobStateChanged(jobId: string, state: print.PrintDocumentAdapterState) {
        if (state === print.PrintDocumentAdapterState.PREVIEW_DESTROY) {
            console.info('PREVIEW_DESTROY');
        } else if (state === print.PrintDocumentAdapterState.PRINT_TASK_SUCCEED) {
            console.info('PRINT_TASK_SUCCEED');
        } else if (state === print.PrintDocumentAdapterState.PRINT_TASK_FAIL) {
            console.info('PRINT_TASK_FAIL');
        } else if (state === print.PrintDocumentAdapterState.PRINT_TASK_CANCEL) {
            console.info('PRINT_TASK_CANCEL');
        } else if (state === print.PrintDocumentAdapterState.PRINT_TASK_BLOCK) {
            console.info('PRINT_TASK_BLOCK');
        }
    }
}
```

## print.print(deprecated)

print(files: Array<string>, callback: AsyncCallback<PrintTask>): void

打印接口，传入文件进行打印，使用callback异步回调。如需拉起系统打印预览界面，需要使用[print](js-apis-print.md#printprint11-1)接口，传入context。

**说明** 

从 API version 10开始支持，从API version 26.0.0开始废弃。建议使用[print](js-apis-print.md#printprint11)替代。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 待打印文件列表，支持图片（.jpg .png .gif .bmp .webp）和.pdf。文件需先保存到应用沙箱，通过fileUri.getUriFromPath获取到沙箱URI，再作为参数传入到本接口。 |
| callback | AsyncCallback<[PrintTask](js-apis-print.md#printtask)> | 是 | 异步获取打印完成之后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

// 传入文件的URI
let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print([fileUri.getUriFromPath(filePath)], (error: BusinessError, printTask: print.PrintTask) => {
    if (error) {
        console.error(`Failed to print. Code: ${error.code}, message: ${error.message}`);
    } else {
        printTask.on('succeed', () => {
            console.info('print state is succeed');
        })
        // ...
    }
})
```

## print.print(deprecated)

print(files: Array<string>): Promise<PrintTask>

打印接口，传入文件进行打印，使用Promise异步回调。如需拉起系统打印预览界面，需要使用[print](js-apis-print.md#printprint11-1)接口，传入context。

**说明** 

从 API version 10开始支持，从API version 26.0.0开始废弃。建议使用[print](js-apis-print.md#printprint11-1)替代。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 待打印文件列表，支持图片（.jpg .png .gif .bmp .webp）和.pdf。文件需先保存到应用沙箱，通过fileUri.getUriFromPath获取到沙箱URI，再作为参数传入到本接口。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PrintTask](js-apis-print.md#printtask)> | Promise对象，返回[PrintTask](js-apis-print.md#printtask)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

// 传入文件的URI
let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print([fileUri.getUriFromPath(filePath)]).then((printTask: print.PrintTask) => {
    printTask.on('succeed', () => {
        console.info('print state is succeed');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error(`Failed to print. Code: ${error.code}, message: ${error.message}`);
})
```

## print.print11+

print(files: Array<string>, context: Context, callback: AsyncCallback<PrintTask>): void

打印接口，传入文件进行打印，拉起系统打印预览界面，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 待打印文件列表，当前支持的文件类型：".bm", ".bmp", ".doc", ".docm", ".docx", ".dot", ".dotm", ".dotx", ".gif", ".jfif", ".jpe", ".jpeg", ".jpg", ".pdf", ".pot", ".potm", ".potx", ".pps", ".ppsm", ".ppsx", ".ppt", ".pptm", ".pptx", ".png", ".rtf", ".txt", ".webp", ".wps", ".xls", ".xlsb", ".xlsm", ".xlsx", ".xlt", ".xltx", ".xml"。文件需先保存到应用沙箱，通过fileUri.getUriFromPath获取到沙箱URI，再作为参数传入到本接口。 |
| context | Context | 是 | 用于拉起系统打印界面的UIAbilityContext。 |
| callback | AsyncCallback<[PrintTask](js-apis-print.md#printtask)> | 是 | 异步获取打印完成之后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button('打印').width('90%').height(50).onClick(() => {
                    let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
                    let context = this.getUIContext().getHostContext();
                    print.print([fileUri.getUriFromPath(filePath)], context, (error: BusinessError, printTask: print.PrintTask) => {
                        if (error) {
                            console.error(`Failed to print. Code: ${error.code}, message: ${error.message}`);
                        } else {
                            printTask.on('succeed', () => {
                                console.info('print state is succeed');
                            })
                            // ...
                        }
                    })
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}
```

## print.print11+

print(files: Array<string>, context: Context): Promise<PrintTask>

打印接口，传入文件进行打印，拉起系统打印预览界面，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 待打印文件列表，当前支持的文件类型：".bm", ".bmp", ".doc", ".docm", ".docx", ".dot", ".dotm", ".dotx", ".gif", ".jfif", ".jpe", ".jpeg", ".jpg", ".pdf", ".pot", ".potm", ".potx", ".pps", ".ppsm", ".ppsx", ".ppt", ".pptm", ".pptx", ".png", ".rtf", ".txt", ".webp", ".wps", ".xls", ".xlsb", ".xlsm", ".xlsx", ".xlt", ".xltx", ".xml"。文件需先保存到应用沙箱，通过fileUri.getUriFromPath获取到沙箱URI，再作为参数传入到本接口。 |
| context | Context | 是 | 用于拉起系统打印界面的UIAbilityContext。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PrintTask](js-apis-print.md#printtask)> | Promise对象，返回[PrintTask](js-apis-print.md#printtask)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button('打印').width('90%').height(50).onClick(() => {
                    let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
                    let context = this.getUIContext().getHostContext();
                    print.print([fileUri.getUriFromPath(filePath)], context).then((printTask: print.PrintTask) => {
                        printTask.on('succeed', () => {
                            console.info('print state is succeed');
                        })
                        // ...
                    }).catch((error: BusinessError) => {
                        console.error(`Failed to print. Code: ${error.code}, message: ${error.message}`);
                    })
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}
```

## print.print11+

print(jobName: string, printAdapter: PrintDocumentAdapter, printAttributes: PrintAttributes, context: Context): Promise<PrintTask>

打印接口，传入文件进行打印，三方应用需要更新打印文件，使用Promise异步回调。当前支持的文件类型：".pdf"。当三方应用需要通过传文件描述符fd拉起系统打印预览界面进行打印时，可通过此接口传入自定义的PrintDocumentAdapter来更新待打印文件。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jobName | string | 是 | 表示待打印文件名称，例如：test.pdf。当前仅支持".pdf"文件类型。打印侧通过[onStartLayoutWrite](js-apis-print.md#onstartlayoutwrite11)接口将空的PDF文件的fd传给接口调用方；调用方使用新的打印参数更新待打印文件。 |
| printAdapter | [PrintDocumentAdapter](js-apis-print.md#printdocumentadapter11) | 是 | 表示三方应用实现的[PrintDocumentAdapter](js-apis-print.md#printdocumentadapter11)接口实例。 |
| printAttributes | [PrintAttributes](js-apis-print.md#printattributes11) | 是 | 表示打印参数。 |
| context | Context | 是 | 用于拉起系统打印界面的UIAbilityContext。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PrintTask](js-apis-print.md#printtask)> | Promise对象，返回[PrintTask](js-apis-print.md#printtask)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button('打印').width('90%').height(50).onClick(() => {
                    let jobName : string = 'jobName';
                    // printAdapter需要用户实现PrintDocumentAdapter接口，这里提供简单的示例供参考
                    let printAdapter : print.PrintDocumentAdapter = new MyPrintDocumentAdapter();
                    let printAttributes : print.PrintAttributes = {
                        copyNumber: 1,
                        pageRange: {
                            startPage: 0,
                            endPage: 5,
                            pages: []
                        },
                        pageSize: print.PrintPageType.PAGE_ISO_A3,
                        directionMode: print.PrintDirectionMode.DIRECTION_MODE_AUTO,
                        colorMode: print.PrintColorMode.COLOR_MODE_MONOCHROME,
                        duplexMode: print.PrintDuplexMode.DUPLEX_MODE_NONE
                    };
                    let context = this.getUIContext().getHostContext();

                    print.print(jobName, printAdapter, printAttributes, context).then((printTask: print.PrintTask) => {
                        printTask.on('succeed', () => {
                            console.info('print state is succeed');
                        })
                        // ...
                    }).catch((error: BusinessError) => {
                        console.error(`Failed to print. Code: ${error.code}, message: ${error.message}`);
                    })
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}

class MyPrintDocumentAdapter implements print.PrintDocumentAdapter {
    onStartLayoutWrite(jobId: string, oldAttrs: print.PrintAttributes, newAttrs: print.PrintAttributes, fd: number,
        writeResultCallback: (jobId: string, writeResult: print.PrintFileCreationState) => void) {
        writeResultCallback(jobId, print.PrintFileCreationState.PRINT_FILE_CREATED);
    }
    onJobStateChanged(jobId: string, state: print.PrintDocumentAdapterState) {
        if (state === print.PrintDocumentAdapterState.PREVIEW_DESTROY) {
            console.info('PREVIEW_DESTROY');
        } else if (state === print.PrintDocumentAdapterState.PRINT_TASK_SUCCEED) {
            console.info('PRINT_TASK_SUCCEED');
        } else if (state === print.PrintDocumentAdapterState.PRINT_TASK_FAIL) {
            console.info('PRINT_TASK_FAIL');
        } else if (state === print.PrintDocumentAdapterState.PRINT_TASK_CANCEL) {
            console.info('PRINT_TASK_CANCEL');
        } else if (state === print.PrintDocumentAdapterState.PRINT_TASK_BLOCK) {
            console.info('PRINT_TASK_BLOCK');
        }
    }
}
```

## PrintAttributes11+

定义打印参数的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| copyNumber | number | 否 | 是 | 表示文件打印份数。取值应为正整数。不传入时默认值为0。 |
| pageRange | [PrintPageRange](js-apis-print.md#printpagerange11) | 否 | 是 | 表示待打印文件的页面范围。不传入时默认值为空范围对象。 |
| pageSize | [PrintPageSize](js-apis-print.md#printpagesize11) | [PrintPageType](js-apis-print.md#printpagetype11) | 否 | 是 | 表示待打印文件的纸张尺寸。不传入时默认值为空纸张尺寸对象。 |
| directionMode | [PrintDirectionMode](js-apis-print.md#printdirectionmode11) | 否 | 是 | 表示待打印文件的方向。不传入时默认值为0。 |
| colorMode | [PrintColorMode](js-apis-print.md#printcolormode11) | 否 | 是 | 表示待打印文件的色彩模式。不传入时默认值为0。 |
| duplexMode | [PrintDuplexMode](js-apis-print.md#printduplexmode11) | 否 | 是 | 表示待打印文件的单双面模式。不传入时默认值为0。 |

## PrintPageRange11+

定义打印范围的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startPage | number | 否 | 是 | 表示起始页。取值应为正整数，默认值为1。 |
| endPage | number | 否 | 是 | 表示结束页。取值应为正整数，默认值为待打印文件的最大页数。 |
| pages | Array<number> | 否 | 是 | 表示待打印的页面范围的集合。默认值为空。 |

## PrintPageSize11+

定义打印页面尺寸的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 表示纸张类型ID。 |
| name | string | 否 | 否 | 表示纸张类型名称。 |
| width | number | 否 | 否 | 表示页面宽度，单位：密尔（千分之一英寸）。 |
| height | number | 否 | 否 | 表示页面高度，单位：密尔（千分之一英寸）。 |

## PrintDirectionMode11+

打印纸张方向的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DIRECTION\_MODE\_AUTO | 0 | 表示自动选择纸张方向。 |
| DIRECTION\_MODE\_PORTRAIT | 1 | 表示纵向打印。 |
| DIRECTION\_MODE\_LANDSCAPE | 2 | 表示横向打印。 |

## PrintColorMode11+

打印色彩模式的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COLOR\_MODE\_MONOCHROME | 0 | 表示黑白打印。 |
| COLOR\_MODE\_COLOR | 1 | 表示彩色打印。 |

## PrintDuplexMode11+

打印单双面模式的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DUPLEX\_MODE\_NONE | 0 | 表示单面打印。 |
| DUPLEX\_MODE\_LONG\_EDGE | 1 | 表示双面打印沿长边翻转。 |
| DUPLEX\_MODE\_SHORT\_EDGE | 2 | 表示双面打印沿短边翻转。 |

## PrintPageType11+

打印纸张类型的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
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

打印任务状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PREVIEW\_DESTROY | 0 | 表示打印预览界面销毁。 |
| PRINT\_TASK\_SUCCEED | 1 | 表示打印任务成功。 |
| PRINT\_TASK\_FAIL | 2 | 表示打印任务失败。 |
| PRINT\_TASK\_CANCEL | 3 | 表示打印任务取消。 |
| PRINT\_TASK\_BLOCK | 4 | 表示打印任务阻塞。 |

## PrintFileCreationState11+

打印文件创建状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRINT\_FILE\_CREATED | 0 | 表示打印文件创建成功。 |
| PRINT\_FILE\_CREATION\_FAILED | 1 | 表示打印文件创建失败。 |
| PRINT\_FILE\_CREATED\_UNRENDERED | 2 | 表示打印文件创建成功但未渲染。 |

## PrinterState14+

打印机状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRINTER\_ADDED | 0 | 表示新打印机到达。 |
| PRINTER\_REMOVED | 1 | 表示打印机丢失。 |
| PRINTER\_CAPABILITY\_UPDATED | 2 | 表示打印机能力更新。 |
| PRINTER\_CONNECTED | 3 | 表示打印机已连接。 |
| PRINTER\_DISCONNECTED | 4 | 表示打印机已断开连接。 |
| PRINTER\_RUNNING | 5 | 表示打印机正在运行。 |

## PrintJobState14+

打印任务状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRINT\_JOB\_PREPARE | 0 | 表示打印任务的初始状态。 |
| PRINT\_JOB\_QUEUED | 1 | 表示打印任务传送到打印机。 |
| PRINT\_JOB\_RUNNING | 2 | 表示执行打印任务。 |
| PRINT\_JOB\_BLOCKED | 3 | 表示打印任务已被阻止。 |
| PRINT\_JOB\_COMPLETED | 4 | 表示打印任务完成。 |

## PrintJobSubState14+

打印任务子状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
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

打印错误代码的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| E\_PRINT\_NONE | 0 | 表示没有错误。 |
| E\_PRINT\_NO\_PERMISSION | 201 | 表示无权限，请根据对应接口的权限要求申请所需权限，并在配置文件中声明。 |
| E\_PRINT\_INVALID\_PARAMETER | 401 | 表示无效的参数，请检查参数类型和取值范围。 |
| E\_PRINT\_GENERIC\_FAILURE | 13100001 | 表示一般打印失败，请检查打印服务运行状态并重试。 |
| E\_PRINT\_RPC\_FAILURE | 13100002 | 表示RPC失败，请检查RPC通信状态并重试。 |
| E\_PRINT\_SERVER\_FAILURE | 13100003 | 表示打印服务失败，请检查打印服务是否正常运行并重试。 |
| E\_PRINT\_INVALID\_EXTENSION | 13100004 | 表示打印扩展无效，请检查扩展能力实现是否正确。 |
| E\_PRINT\_INVALID\_PRINTER | 13100005 | 表示打印机无效，请确认打印机 ID 及打印机信息是否正确后重试。 |
| E\_PRINT\_INVALID\_PRINT\_JOB | 13100006 | 表示打印任务无效，请检查任务 ID 和状态是否正确。 |
| E\_PRINT\_FILE\_IO | 13100007 | 表示文件输入/输出错误，请检查文件路径、文件状态和操作是否正确。 |
| E\_PRINT\_TOO\_MANY\_FILES18+ | 13100010 | 表示文件数量超过上限，当前上限99个。 |
| E\_PRINT\_SMB\_LOGIN\_LOCKOUT24+ | 13100012 | 表示当前SMB协议共享打印机账号因多次登录失败而被锁定。请等待账号解锁后重试，或联系管理员处理。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| E\_PRINT\_SMB\_CONNECTION\_FAILURE24+ | 13100013 | 表示SMB协议共享打印机连接失败（发生网络错误、主机不可达或端口被阻止）。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| E\_PRINT\_SMB\_INVALID\_CREDENTIALS24+ | 13100014 | 表示SMB协议共享打印机账号/密码错误。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## ApplicationEvent14+

打印应用事件的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| APPLICATION\_CREATED | 0 | 表示打印应用被拉起的事件。 |
| APPLICATION\_CLOSED\_FOR\_STARTED | 1 | 表示由于点击打印而关闭打印应用的事件。 |
| APPLICATION\_CLOSED\_FOR\_CANCELED | 2 | 表示由于点击取消而关闭打印应用的事件。 |

## print.addPrinterToDiscovery14+

addPrinterToDiscovery(printerInformation: PrinterInformation): Promise<void>

添加打印机到系统打印机发现列表，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| printerInformation | [PrinterInformation](js-apis-print.md#printerinformation14) | 是 | 表示新发现的打印机。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果，用于异步操作。resolve表示操作成功，reject表示操作失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerInformation : print.PrinterInformation = {
    printerId : 'testPrinterId', // printerId可通过on('printerChange')回调获取
    printerName : 'testPrinterName',
    printerStatus : 0,
    description : 'testDesc',
    uri : 'testUri',
    printerMake : 'testPrinterMake',
    options : 'testOps'
};
print.addPrinterToDiscovery(printerInformation).then(() => {
    console.info('addPrinterToDiscovery success');
}).catch((error: BusinessError) => {
    console.error(`Failed to addPrinterToDiscovery. Code: ${error.code}, message: ${error.message}`);
})
```

## print.updatePrinterInDiscovery14+

updatePrinterInDiscovery(printerInformation: PrinterInformation): Promise<void>

更新打印机能力到系统打印机发现列表，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| printerInformation | [PrinterInformation](js-apis-print.md#printerinformation14) | 是 | 表示待更新能力的打印机。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果，用于异步操作。resolve表示操作成功，reject表示操作失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let testPageSize : print.PrintPageSize = {
    id : 'ISO_A4',
    name : 'iso_a4_210x297mm',
    width : 8268,
    height : 11692
};

let testCapability : print.PrinterCapabilities = {
    supportedPageSizes : [testPageSize],
    supportedColorModes : [print.PrintColorMode.COLOR_MODE_MONOCHROME],
    supportedDuplexModes : [print.PrintDuplexMode.DUPLEX_MODE_NONE],
    supportedMediaTypes : ['stationery'],
    supportedQualities : [print.PrintQuality.QUALITY_NORMAL],
    supportedOrientations : [print.PrintOrientationMode.ORIENTATION_MODE_PORTRAIT],
    options : 'testOptions'
};

let printerInformation : print.PrinterInformation = {
    printerId : 'testPrinterId', // printerId可通过on('printerChange')回调获取
    printerName : 'testPrinterName',
    printerStatus : 0,
    description : 'testDesc',
    capability : testCapability,
    uri : 'testUri',
    printerMake : 'testPrinterMake',
    options : 'testOptions'
};
print.updatePrinterInDiscovery(printerInformation).then(() => {
    console.info('updatePrinterInDiscovery success');
}).catch((error: BusinessError) => {
    console.error(`Failed to updatePrinterInDiscovery. Code: ${error.code}, message: ${error.message}`);
})
```

## print.removePrinterFromDiscovery14+

removePrinterFromDiscovery(printerId: string): Promise<void>

从系统打印机发现列表里移除打印机，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| printerId | string | 是 | 表示待移除的打印机ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果，用于异步操作。resolve表示操作成功，reject表示操作失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// printerId可通过on('printerChange')回调获取
let printerId : string = 'testPrinterId';
print.removePrinterFromDiscovery(printerId).then(() => {
    console.info('removePrinterFromDiscovery success');
}).catch((error: BusinessError) => {
    console.error(`Failed to removePrinterFromDiscovery. Code: ${error.code}, message: ${error.message}`);
})
```

## print.getPrinterInformationById14+

getPrinterInformationById(printerId: string): Promise<PrinterInformation>

根据打印机ID获取打印机信息，使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| printerId | string | 是 | 表示待获取信息的打印机ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PrinterInformation](js-apis-print.md#printerinformation14)> | Promise对象，返回打印机信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// printerId可通过on('printerChange')回调获取
let printerId : string = 'testPrinterId';
print.getPrinterInformationById(printerId).then((printerInformation : print.PrinterInformation) => {
    console.info('getPrinterInformationById data : ' + JSON.stringify(printerInformation));
}).catch((error: BusinessError) => {
    console.error(`Failed to getPrinterInformationById. Code: ${error.code}, message: ${error.message}`);
})
```

## PrinterInformation14+

定义打印机信息的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| printerId | string | 否 | 否 | 表示打印机ID。 |
| printerName | string | 否 | 否 | 表示打印机名称。 |
| printerStatus | [PrinterStatus](js-apis-print.md#printerstatus14) | 否 | 否 | 表示当前打印机状态。 |
| description | string | 否 | 是 | 表示打印机说明。不传入时默认值为空字符串。 |
| capability | [PrinterCapabilities](js-apis-print.md#printercapabilities14) | 否 | 是 | 表示打印机能力。 |
| uri | string | 否 | 是 | 表示打印机URI。不传入时默认值为空字符串。 |
| printerMake | string | 否 | 是 | 表示打印机型号。不传入时默认值为空字符串。 |
| preferences18+ | [PrinterPreferences](js-apis-print.md#printerpreferences18) | 否 | 是 | 表示打印机首选项。 |
| alias18+ | string | 否 | 是 | 表示打印机别名。不传入时默认值为空字符串。 |
| selectedDriver24+ | [PpdInfo](js-apis-print.md#ppdinfo24) | 否 | 是 | 表示添加打印机时选择的驱动的信息。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| selectedProtocol24+ | string | 否 | 是 | 表示添加打印机时选择的协议。不传入时默认值为空字符串。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| options | string | 否 | 是 | 表示打印机详细信息。不传入时默认值为空字符串。 |

## PrinterCapabilities14+

定义打印机能力的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| supportedPageSizes | Array<[PrintPageSize](js-apis-print.md#printpagesize11)> | 否 | 否 | 表示打印机支持的纸张尺寸列表。 |
| supportedColorModes | Array<[PrintColorMode](js-apis-print.md#printcolormode11)> | 否 | 否 | 表示打印机支持的色彩模式列表。 |
| supportedDuplexModes | Array<[PrintDuplexMode](js-apis-print.md#printduplexmode11)> | 否 | 否 | 表示打印机支持的单双面模式列表。 |
| supportedMediaTypes | Array<string> | 否 | 是 | 表示打印机支持的纸张类型列表。不传入时默认值为空列表。 |
| supportedQualities | Array<[PrintQuality](js-apis-print.md#printquality14)> | 否 | 是 | 表示打印机支持的打印质量列表。不传入时默认值为空列表。 |
| supportedOrientations | Array<[PrintOrientationMode](js-apis-print.md#printorientationmode14)> | 否 | 是 | 表示打印机支持的打印方向列表。不传入时默认值为空列表。 |
| options | string | 否 | 是 | 表示打印机能力详细信息。不传入时默认值为空字符串。 |
| vendorPrinterPrefAbility | string | 否 | 是 | 表示由打印机驱动厂商提供的打印机首选项设置界面。不传入时默认值为空字符串。  **模型约束：** 此接口仅可在Stage模型下使用。  **起始版本：** 26.0.0 |
| vendorJobAttrAbility | string | 否 | 是 | 表示由打印机驱动厂商提供的打印任务属性设置界面。不传入时默认值为空字符串。  **模型约束：** 此接口仅可在Stage模型下使用。  **起始版本：** 26.0.0 |

## PrintQuality14+

打印质量的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| QUALITY\_DRAFT | 3 | 表示经济的打印质量。 |
| QUALITY\_NORMAL | 4 | 表示标准的打印质量。 |
| QUALITY\_HIGH | 5 | 表示最佳的打印质量。 |

## PrintOrientationMode14+

打印方向的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ORIENTATION\_MODE\_PORTRAIT | 0 | 表示纵向打印。 |
| ORIENTATION\_MODE\_LANDSCAPE | 1 | 表示横向打印。 |
| ORIENTATION\_MODE\_REVERSE\_LANDSCAPE | 2 | 表示横向翻转打印。 |
| ORIENTATION\_MODE\_REVERSE\_PORTRAIT | 3 | 表示纵向翻转打印。 |
| ORIENTATION\_MODE\_NONE | 4 | 表示自适应方向打印。 |

## PrinterStatus14+

打印机状态的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRINTER\_IDLE | 0 | 表示打印机空闲状态。 |
| PRINTER\_BUSY | 1 | 表示打印机忙碌状态。 |
| PRINTER\_UNAVAILABLE | 2 | 表示打印机脱机状态。 |

## PrinterPreferences18+

定义打印机首选项的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| defaultDuplexMode | [PrintDuplexMode](js-apis-print.md#printduplexmode11) | 否 | 是 | 表示默认单双面模式。 |
| defaultPrintQuality | [PrintQuality](js-apis-print.md#printquality14) | 否 | 是 | 表示默认打印质量。 |
| defaultMediaType | string | 否 | 是 | 表示默认纸张类型。 |
| defaultPageSizeId | string | 否 | 是 | 表示默认纸张尺寸的ID，其范围包含国际标准化组织定义的标准纸张尺寸（如ISO\_A4）和系统中定义的非标准的纸张尺寸（如Custom.178x254mm，表示这种纸张尺寸为178毫米 x 254毫米）。 |
| defaultOrientation | [PrintOrientationMode](js-apis-print.md#printorientationmode14) | 否 | 是 | 表示默认打印方向。 |
| borderless | boolean | 否 | 是 | 表示是否无边距打印，true表示无边距，false表示有边距。默认值为false。 |
| defaultColorMode24+ | [PrintColorMode](js-apis-print.md#printcolormode11) | 否 | 是 | 表示默认色彩模式。默认值为黑白。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| defaultCollate24+ | boolean | 否 | 是 | 表示默认出纸顺序。true表示逐份打印，false表示逐页打印。默认值为逐份。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| defaultReverse24+ | boolean | 否 | 是 | 表示默认打印顺序。true表示逆序打印，false表示正序打印。默认值为正序打印。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| options | string | 否 | 是 | 表示打印机首选项中除以上字段外的其他字段，从打印机或打印机驱动获取，以JSON格式存储在string中。 |
| vendorOptions | string | 否 | 是 | 表示以JSON格式字符串化的打印机驱动的厂商打印机首选项。  **模型约束：** 此接口仅可在Stage模型下使用。  **起始版本：** 26.0.0 |

## PrinterEvent18+

打印机相关事件的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRINTER\_EVENT\_ADDED | 0 | 表示打印机添加事件。 |
| PRINTER\_EVENT\_DELETED | 1 | 表示打印机删除事件。 |
| PRINTER\_EVENT\_STATE\_CHANGED | 2 | 表示打印机状态变化事件。 |
| PRINTER\_EVENT\_INFO\_CHANGED | 3 | 表示打印机信息变化事件。 |
| PRINTER\_EVENT\_PREFERENCE\_CHANGED | 4 | 表示打印机首选项变化事件。 |
| PRINTER\_EVENT\_LAST\_USED\_PRINTER\_CHANGED | 5 | 表示上次使用的打印机的变化事件。 |

## DefaultPrinterType18+

默认打印机确定方式的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT\_PRINTER\_TYPE\_SET\_BY\_USER | 0 | 表示将用户手动设置的默认打印机作为当前默认打印机。 |
| DEFAULT\_PRINTER\_TYPE\_LAST\_USED\_PRINTER | 1 | 表示自动将上次使用的打印机作为当前默认打印机。 |

## print.getAddedPrinters18+

getAddedPrinters(): Promise<Array<string>>

获取系统中已添加的打印机列表，使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回包含所有已添加打印机的打印机ID的列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.getAddedPrinters().then((printers: string[]) => {
    console.info('getAddedPrinters success ' + JSON.stringify(printers));
    // ...
}).catch((error: BusinessError) => {
    console.error(`Failed to getAddedPrinters. Code: ${error.code}, message: ${error.message}`);
})
```

## PrinterChangeCallback18+

type PrinterChangeCallback = (event: PrinterEvent, printerInformation: PrinterInformation) => void

将打印机事件和打印机信息作为参数的回调方法。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [PrinterEvent](js-apis-print.md#printerevent18) | 是 | 表示打印机事件。 |
| printerInformation | [PrinterInformation](js-apis-print.md#printerinformation14) | 是 | 表示打印机信息。 |

## print.on18+

on(type: 'printerChange', callback: PrinterChangeCallback): void

注册打印机变动事件回调，使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'printerChange' | 是 | 表示打印机变动事件。 |
| callback | [PrinterChangeCallback](js-apis-print.md#printerchangecallback18) | 是 | 打印机变动之后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';

// Trigger this callback when a added printer is changed.
let onPrinterChange =
    (event: print.PrinterEvent, printerInformation: print.PrinterInformation) => {
        console.info('printerChange, event: ' + event + ', printerInformation: ' + JSON.stringify(printerInformation));
    };
print.on('printerChange', onPrinterChange);
```

## print.off18+

off(type: 'printerChange', callback?: PrinterChangeCallback): void

取消注册打印机变动事件回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'printerChange' | 是 | 表示打印机变动事件。 |
| callback | [PrinterChangeCallback](js-apis-print.md#printerchangecallback18) | 否 | 表示要取消注册的打印机变动事件回调。不传入时取消调用方所有已注册的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';

// Trigger this callback when a added printer is changed.
let onPrinterChange =
    (event: print.PrinterEvent, printerInformation: print.PrinterInformation) => {
        console.info('printerChange, event: ' + event + ', printerInformation: ' + JSON.stringify(printerInformation));
    };
print.on('printerChange', onPrinterChange);
print.off('printerChange');
```

## print.startDiscoverPrinter20+

startDiscoverPrinter(extensionList: Array<string>, callback: AsyncCallback<void>): void

通过指定“打印扩展能力列表”来发现打印机，发现的打印机具备指定的打印扩展能力。如果指定空的打印扩展能力列表，则表示加载所有扩展能力。使用callback异步回调。在不需要继续发现时，调用[stopDiscoverPrinter](js-apis-print.md#printstopdiscoverprinter20)停止发现，释放系统资源，否则会导致系统持续进行打印机发现，消耗系统资源。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extensionList | Array<string> | 是 | 要加载的[打印扩展能力](js-apis-app-ability-printextensionability.md)列表，列表成员为打印扩展能力的包名，空列表表示加载所有扩展能力。 |
| callback | AsyncCallback<void> | 是 | 异步开始发现打印机之后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 加载所有打印扩展能力
let extensionList: string[] = [];
// 通过指定自己应用的包名，在发现时加载自己的打印扩展能力
// let extensionList: string[] = ['com.myapplication.test'];
print.startDiscoverPrinter(extensionList, (error: BusinessError) => {
    if (error) {
        console.error(`Failed to startDiscoverPrinter. Code: ${error.code}, message: ${error.message}`);
    } else {
        console.info('start Discover Printer success');
    }
})
```

## print.startDiscoverPrinter20+

startDiscoverPrinter(extensionList: Array<string>): Promise<void>

通过指定“打印扩展能力列表”来发现打印机，发现的打印机具备指定的打印扩展能力。如果指定空的打印扩展能力列表，则表示加载所有扩展能力，使用Promise异步回调。在不需要继续发现时，调用[stopDiscoverPrinter](js-apis-print.md#printstopdiscoverprinter20)停止发现，释放系统资源，否则会导致系统持续进行打印机发现，消耗系统资源。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extensionList | Array<string> | 是 | 要加载的[打印扩展能力](js-apis-app-ability-printextensionability.md)列表，列表成员为打印扩展能力的包名，空列表表示加载所有扩展能力。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果，用于异步操作。resolve表示操作成功，reject表示操作失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 加载所有打印扩展能力
let extensionList: string[] = [];
// 通过指定自己应用的包名，在发现时加载自己的打印扩展能力
// let extensionList: string[] = ['com.myapplication.test'];
print.startDiscoverPrinter(extensionList).then(() => {
    console.info('start Discovery success');
}).catch((error: BusinessError) => {
    console.error(`Failed to startDiscoverPrinter. Code: ${error.code}, message: ${error.message}`);
})
```

## print.stopDiscoverPrinter20+

stopDiscoverPrinter(callback: AsyncCallback<void>): void

停止发现打印机，使用callback异步回调。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 停止发现打印机的异步回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.stopDiscoverPrinter((error: BusinessError) => {
    if (error) {
        console.error(`Failed to stopDiscoverPrinter. Code: ${error.code}, message: ${error.message}`);
    } else {
        console.info('stop Discover Printer success');
    }
})
```

## print.stopDiscoverPrinter20+

stopDiscoverPrinter(): Promise<void>

停止发现打印机，使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果，用于异步操作。resolve表示操作成功，reject表示操作失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.stopDiscoverPrinter().then(() => {
    console.info('stop Discovery success');
}).catch((error: BusinessError) => {
    console.error(`Failed to stopDiscoverPrinter. Code: ${error.code}, message: ${error.message}`);
})
```

## print.connectPrinter20+

connectPrinter(printerId: string, callback: AsyncCallback<void>): void

通过打印机ID连接打印机，使用callback异步回调。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| printerId | string | 是 | 表示打印机ID。 |
| callback | AsyncCallback<void> | 是 | 通过打印机ID异步连接打印机的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// printerId可通过on('printerChange')回调获取
let printerId: string = 'printerId_32';
print.connectPrinter(printerId, (error: BusinessError) => {
    if (error) {
        console.error(`Failed to connectPrinter. Code: ${error.code}, message: ${error.message}`);
    } else {
        console.info('start connect Printer success');
    }
})
```

## print.connectPrinter20+

connectPrinter(printerId: string): Promise<void>

通过打印机ID连接打印机，使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| printerId | string | 是 | 表示打印机ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果，用于异步操作。resolve表示操作成功，reject表示操作失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// printerId可通过on('printerChange')回调获取
let printerId: string = 'printerId_32';
print.connectPrinter(printerId).then(() => {
    console.info('start connect Printer success');
}).catch((error: BusinessError) => {
    console.error(`Failed to connectPrinter. Code: ${error.code}, message: ${error.message}`);
})
```

## print.startPrint23+

startPrint(job: PrintJobData): Promise<void>

打印接口，传入文件或者二进制数据进行打印，使用Promise异步回调。该接口直接通过PrintJobData指定目标打印机ID及打印参数创建打印任务；如需拉起系统打印预览界面，请使用print.print接口。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| job | [PrintJobData](js-apis-print.md#printjobdata23) | 是 | 表示打印任务数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果，用于异步操作。resolve表示操作成功，reject表示操作失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

let tempPath = '/data/storage/el2/base/haps/entry/files/note.jpg';
let file: fileIo.File;
file = fileIo.openSync(tempPath, 4);

let printJobData: print.PrintJobData = {
    printerId: 'printerId', // printerId可通过on('printerChange')回调获取
    jobName: 'jobName',
    documentFormat: print.PrintDocumentFormat.DOCUMENT_FORMAT_AUTO,
    docFlavor: print.DocFlavor.FILE_DESCRIPTOR,
    copyNumber: 1,
    isLandscape: false,
    colorMode: print.PrintColorMode.COLOR_MODE_MONOCHROME,
    duplexMode: print.PrintDuplexMode.DUPLEX_MODE_NONE,
    pageSize: {id: 'ISO_A4', name: 'ISO_A4', width: 8268, height: 11692},
    fdList: [file.fd],
};
print.startPrint(printJobData).then(() => {
    console.info('start print success');
}).catch((error: BusinessError) => {
    console.error(`Failed to startPrint. Code: ${error.code}, message: ${error.message}`);
})
```

## PrintDocumentFormat23+

打印数据格式的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DOCUMENT\_FORMAT\_AUTO | 0 | 表示自动检测格式。 |
| DOCUMENT\_FORMAT\_JPEG | 1 | 表示JPEG格式。 |
| DOCUMENT\_FORMAT\_PDF | 2 | 表示PDF格式。 |
| DOCUMENT\_FORMAT\_POSTSCRIPT | 3 | 表示PostScript格式。 |
| DOCUMENT\_FORMAT\_TEXT | 4 | 表示文本格式。 |
| DOCUMENT\_FORMAT\_RAW | 5 | 表示RAW格式。 |

## DocFlavor23+

打印数据来源形式的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FILE\_DESCRIPTOR | 0 | 表示文件描述符。 |
| BYTES | 1 | 表示二进制数据。 |

## PrintJobData23+

定义打印任务的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| printerId | string | 否 | 否 | 表示打印机ID。 |
| jobName | string | 否 | 否 | 表示打印任务名称。 |
| documentFormat | [PrintDocumentFormat](js-apis-print.md#printdocumentformat23) | 否 | 否 | 表示打印数据格式。 |
| docFlavor | [DocFlavor](js-apis-print.md#docflavor23) | 否 | 否 | 表示打印数据来源形式。当取值为FILE\_DESCRIPTOR时，需提供fdList参数；当取值为BYTES时，需提供binaryData参数。 |
| copyNumber | number | 否 | 否 | 表示文件打印份数。取值应为正整数，默认为1。 |
| isLandscape | boolean | 否 | 否 | 表示是否横向打印。true表示横向打印，false表示纵向打印。默认值为false。 |
| colorMode | [PrintColorMode](js-apis-print.md#printcolormode11) | 否 | 否 | 表示色彩模式。 |
| duplexMode | [PrintDuplexMode](js-apis-print.md#printduplexmode11) | 否 | 否 | 表示单双面打印模式。 |
| pageSize | [PrintPageSize](js-apis-print.md#printpagesize11) | 否 | 否 | 表示选定的页面尺寸。 |
| jobId | string | 否 | 是 | 表示打印任务的唯一标识符。 |
| fdList | number[] | 否 | 是 | 表示待打印文件fd列表。当docFlavor设置为FILE\_DESCRIPTOR时，需传入此参数。 |
| binaryData | Uint8Array | 否 | 是 | 表示待打印二进制数据。当docFlavor设置为BYTES时，需传入此参数。 |
| printQuality | [PrintQuality](js-apis-print.md#printquality14) | 否 | 是 | 表示打印质量。 |
| mediaType | string | 否 | 是 | 表示打印纸张类型。 |
| isBorderless | boolean | 否 | 是 | 表示是否无边距打印。true表示无边距打印，false表示有边距打印。默认值为true。 |
| isAutoRotate | boolean | 否 | 是 | 表示是否自动旋转页面。true表示自动旋转页面，false表示不自动旋转页面。默认值为true。 |
| isReverse | boolean | 否 | 是 | 表示是否逆序打印。true表示逆序打印，false表示顺序打印。默认值为false。 |
| isCollate | boolean | 否 | 是 | 表示打印顺序方式。true表示逐份打印，false表示逐页打印。默认值为true。 |
| isSequential | boolean | 否 | 是 | 表示是否连续打印。true表示连续打印，false表示不连续打印。默认值为false。 |
| options | string | 否 | 是 | 表示以JSON格式字符串化的打印任务附加信息。应包含printerUri、printerName、documentFormat三个字段，不传或格式不合法会导致CUPS任务创建失败。 |
| vendorOptions | string | 否 | 是 | 表示以JSON格式字符串化的打印机驱动的厂商打印任务属性。  **起始版本：** 26.0.0 |

## PrintMargin24+

定义打印页边距的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | number | 否 | 是 | 表示页面上边距。默认值为0。单位：毫米。 |
| bottom | number | 否 | 是 | 表示页面下边距。默认值为0。单位：毫米。 |
| left | number | 否 | 是 | 表示页面左边距。默认值为0。单位：毫米。 |
| right | number | 否 | 是 | 表示页面右边距。默认值为0。单位：毫米。 |

## PrinterRange24+

定义打印范围的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startPage | number | 否 | 是 | 表示起始页。取值应为正整数，默认值为1。 |
| endPage | number | 否 | 是 | 表示结束页。取值应为正整数，默认值为待打印文件的最大页数。 |
| pages | Array<number> | 否 | 是 | 表示待打印的页面范围的集合。默认值为空。 |

## PreviewAttribute24+

定义打印预览属性的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| previewRange | [PrinterRange](js-apis-print.md#printerrange24) | 否 | 否 | 表示预览页面范围。 |
| result | number | 否 | 是 | 表示预览文件生成结果，具体取值含义由开发者自行定义。 |

## PrintResolution24+

定义打印分辨率的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 表示分辨率ID。 |
| horizontalDpi | number | 否 | 否 | 表示水平DPI。单位：DPI。 |
| verticalDpi | number | 否 | 否 | 表示垂直DPI。单位：DPI。 |

## PrinterCapability24+

定义打印机能力的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colorMode | number | 否 | 否 | 表示色彩模式，取值参考[PrintColorMode](js-apis-print.md#printcolormode11)。 |
| duplexMode | number | 否 | 否 | 表示单双面打印模式，取值参考[PrintDuplexMode](js-apis-print.md#printduplexmode11)。 |
| pageSize | Array<[PrintPageSize](js-apis-print.md#printpagesize11)> | 否 | 否 | 表示打印机支持的页面尺寸列表。 |
| resolution | Array<[PrintResolution](js-apis-print.md#printresolution24)> | 否 | 是 | 表示打印机支持的分辨率列表。 |
| minMargin | [PrintMargin](js-apis-print.md#printmargin24) | 否 | 是 | 表示打印机最小边距。 |
| options | Object | 否 | 是 | 表示以JSON格式字符串化的打印机能力信息。 |

## PrinterInfo24+

定义打印机信息的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| printerId | string | 否 | 否 | 表示打印机ID。 |
| printerName | string | 否 | 否 | 表示打印机名称。 |
| printerState | [PrinterState](js-apis-print.md#printerstate14) | 否 | 否 | 表示当前打印机状态。 |
| printerIcon | number | 否 | 是 | 表示打印机图标的资源ID。默认值为-1。 |
| description | string | 否 | 是 | 表示打印机说明。 |
| capability | [PrinterCapability](js-apis-print.md#printercapability24) | 否 | 是 | 表示打印机能力。 |
| options | Object | 否 | 是 | 表示以JSON格式字符串化的打印机信息。 |

## PrintJob24+

定义打印任务的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fdList | Array<number> | 否 | 否 | 表示待打印文件fd列表。 |
| jobId | string | 否 | 否 | 表示打印任务ID。 |
| printerId | string | 否 | 否 | 表示负责打印的打印机ID。 |
| jobState | [PrintJobState](js-apis-print.md#printjobstate14) | 否 | 否 | 表示当前打印任务状态。 |
| jobSubstate | [PrintJobSubState](js-apis-print.md#printjobsubstate14) | 否 | 否 | 表示当前打印任务子状态。 |
| copyNumber | number | 否 | 否 | 表示文件打印份数。取值应为正整数，默认为1。 |
| pageRange | [PrinterRange](js-apis-print.md#printerrange24) | 否 | 否 | 表示打印页面范围。 |
| isSequential | boolean | 否 | 否 | 表示是否连续打印。true表示连续打印，false表示不连续打印。默认值为false。 |
| pageSize | [PrintPageSize](js-apis-print.md#printpagesize11) | 否 | 否 | 表示选定的页面尺寸。 |
| isLandscape | boolean | 否 | 否 | 表示是否横向打印。true表示横向打印，false表示纵向打印。默认值为false。 |
| colorMode | number | 否 | 否 | 表示色彩模式，取值参考[PrintColorMode](js-apis-print.md#printcolormode11)。 |
| duplexMode | number | 否 | 否 | 表示单双面打印模式，取值参考[PrintDuplexMode](js-apis-print.md#printduplexmode11)。 |
| margin | [PrintMargin](js-apis-print.md#printmargin24) | 否 | 是 | 表示当前页边距设置。 |
| preview | [PreviewAttribute](js-apis-print.md#previewattribute24) | 否 | 是 | 表示预览设置。 |
| options | Object | 否 | 是 | 表示以JSON格式字符串化的打印任务详细信息。 |
| vendorOptions | string | 否 | 是 | 表示以JSON格式字符串化的打印机驱动的厂商打印任务属性。  **模型约束：** 此接口仅可在Stage模型下使用。  **起始版本：** 26.0.0 |

## print.updatePrintJobState24+

updatePrintJobState(jobId: string, state: PrintJobState, subState: PrintJobSubState, callback: AsyncCallback<void>): void

更新打印任务状态，使用callback异步回调。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.ENTERPRISE\_MANAGE\_PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jobId | string | 是 | 表示打印任务ID。 |
| state | [PrintJobState](js-apis-print.md#printjobstate14) | 是 | 表示打印任务状态。 |
| subState | [PrintJobSubState](js-apis-print.md#printjobsubstate14) | 是 | 表示打印任务子状态。 |
| callback | AsyncCallback<void> | 是 | 异步更新打印任务状态之后的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// jobId可通过打印扩展能力PrintExtensionAbility的onStartPrintJob回调获得
let jobId : string = 'jobId';
let state : print.PrintJobState = print.PrintJobState.PRINT_JOB_PREPARE;
let subState : print.PrintJobSubState = print.PrintJobSubState.PRINT_JOB_COMPLETED_SUCCESS;
print.updatePrintJobState(jobId, state, subState, (error: BusinessError) => {
    if (error) {
        console.error(`Failed to updatePrintJobState. Code: ${error.code}, message: ${error.message}`);
    } else {
        console.info('updatePrintJobState success');
    }
})
```

## print.updatePrintJobState24+

updatePrintJobState(jobId: string, state: PrintJobState, subState: PrintJobSubState): Promise<void>

更新打印任务状态，使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.ENTERPRISE\_MANAGE\_PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jobId | string | 是 | 表示打印任务ID。 |
| state | [PrintJobState](js-apis-print.md#printjobstate14) | 是 | 表示打印任务状态。 |
| subState | [PrintJobSubState](js-apis-print.md#printjobsubstate14) | 是 | 表示打印任务子状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果，用于异步操作。resolve表示操作成功，reject表示操作失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// jobId可通过打印扩展能力PrintExtensionAbility的onStartPrintJob回调获得
let jobId : string = 'jobId';
let state : print.PrintJobState = print.PrintJobState.PRINT_JOB_PREPARE;
let subState : print.PrintJobSubState = print.PrintJobSubState.PRINT_JOB_COMPLETED_SUCCESS;
print.updatePrintJobState(jobId, state, subState).then(() => {
    console.info('update print job state success');
}).catch((error: BusinessError) => {
    console.error(`Failed to updatePrintJobState. Code: ${error.code}, message: ${error.message}`);
})
```

## print.updatePrinterInformation24+

updatePrinterInformation(printerInformation: PrinterInformation): Promise<void>

更新系统中打印机的部分信息，使用Promise异步回调。当前仅允许更新[PrinterInformation](js-apis-print.md#printerinformation14)的alias和options字段。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.ENTERPRISE\_MANAGE\_PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| printerInformation | [PrinterInformation](js-apis-print.md#printerinformation14) | 是 | 表示待更新信息的打印机，当前仅允许更新alias和options字段。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果，用于异步操作。resolve表示操作成功，reject表示操作失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let testPageSize : print.PrintPageSize = {
    id : 'ISO_A4',
    name : 'iso_a4_210x297mm',
    width : 8268,
    height : 11692
};

let testCapability : print.PrinterCapabilities = {
    supportedPageSizes : [testPageSize],
    supportedColorModes : [print.PrintColorMode.COLOR_MODE_MONOCHROME],
    supportedDuplexModes : [print.PrintDuplexMode.DUPLEX_MODE_NONE],
    supportedMediaTypes : ['stationery'],
    supportedQualities : [print.PrintQuality.QUALITY_NORMAL],
    supportedOrientations : [print.PrintOrientationMode.ORIENTATION_MODE_PORTRAIT],
    options : 'testOptions'
};

let printerInformation : print.PrinterInformation = {
    printerId : 'testPrinterId', // printerId可通过on('printerChange')回调获取
    printerName : 'testPrinterName',
    printerStatus : 0,
    description : 'testDesc',
    capability : testCapability,
    uri : 'testUri',
    printerMake : 'testPrinterMake',
    options : 'testOptions'
};
print.updatePrinterInformation(printerInformation).then(() => {
    console.info('updatePrinterInformation success');
}).catch((error: BusinessError) => {
    console.error(`Failed to updatePrinterInformation. Code: ${error.code}, message: ${error.message}`);
})
```

## PpdInfo24+

定义打印机所使用驱动的PPD文件信息的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**模型约束：** 此接口仅可在Stage模型下使用。

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| manufacturer | string | 否 | 否 | 表示当前PPD文件内的打印机厂商名称。 |
| nickName | string | 否 | 否 | 表示当前PPD文件内的打印机别名。 |
| ppdName | string | 否 | 否 | 表示当前PPD文件的名称。 |

## SharedHost24+

定义共享设备信息的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**模型约束：** 此接口仅可在Stage模型下使用。

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ip | string | 否 | 否 | 表示共享设备的IP地址。 |
| shareName | string | 否 | 否 | 表示共享设备的主机名称。 |
| workgroupName | string | 否 | 否 | 表示共享设备的工作组名称。 |

## print.addPrinter24+

addPrinter(printerName: string, uri: string, ppdName?: string, options?: string): Promise<boolean>

添加打印机到系统中，使用Promise异步回调。该接口面向打印驱动、打印管理软件、三方打印管理软件、云打印等需要管理打印机或扫描仪的场景。

**需要权限：** ohos.permission.MANAGE\_PRINT\_JOB 或 ohos.permission.PRINTER\_DRIVER

**系统能力：** SystemCapability.Print.PrintFramework

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| printerName | string | 是 | 表示打印机名称。 |
| uri | string | 是 | 表示打印机的URI。 |
| ppdName | string | 否 | 表示打印机PPD驱动文件在文件系统中的名称。该名称由设备安装厂商驱动后生成，命名格式为“包名\_模块名\_文件名”，具体名称需向驱动厂商获取。当需要指定特定PPD驱动文件时传入此参数，不传入时系统自动匹配。 |
| options | string | 否 | JSON对象字符串，表示打印机选项参数。预留字段，暂未启用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回添加打印机成功与否的结果。true表示添加成功，false表示添加失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 13100003 | Add the printer to system failed. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerName : string = 'printerName';
let uri : string = 'uri';
let ppdName : string = 'ppdName';
print.addPrinter(printerName, uri, ppdName).then(() => {
    console.info('add printer success');
}).catch((error: BusinessError) => {
    console.error(`Failed to addPrinter. Code: ${error.code}, message: ${error.message}`);
})
```

## WatermarkHandleResult24+

强制水印处理结果的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WATERMARK\_HANDLE\_SUCCESS | 0 | 表示强制水印处理成功。 |
| WATERMARK\_HANDLE\_FAILURE | 1 | 表示强制水印处理失败。 |

## print.WatermarkCallback24+

type WatermarkCallback = (jobId: string, fd: number) => void

注册强制水印处理的监听事件时使用的回调类型。

**系统能力：** SystemCapability.Print.PrintFramework

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jobId | string | 是 | 表示当前打印任务的ID。 |
| fd | number | 是 | 表示当前文件的文件描述符。 |

## print.registerWatermarkCallback24+

registerWatermarkCallback(callback: WatermarkCallback): void

注册强制水印处理的监听事件。强制水印是指由企业管控策略要求在打印文件上强制添加的水印内容。在企业管理场景中，当需要在打印文件上强制添加水印（如公司标识、机密等级标记）时，可通过此接口注册水印处理回调。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [WatermarkCallback](js-apis-print.md#printwatermarkcallback24) | 是 | 表示注册强制水印处理的监听事件时使用的回调类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';

let watermarkCallback: print.WatermarkCallback = (jobId: string, fd: number) => {
    console.info('Watermark callback triggered, jobId: ' + jobId + ', fd: ' + fd);
};

try {
    print.registerWatermarkCallback(watermarkCallback);
    console.info('registerWatermarkCallback success');
} catch (error) {
    console.error(`Failed to registerWatermarkCallback. Code: ${error.code}, message: ${error.message}`);
}
```

## print.unregisterWatermarkCallback24+

unregisterWatermarkCallback(callback?: WatermarkCallback): void

注销强制水印处理的监听事件。当企业管理应用不再需要在打印文件上强制添加水印时，可调用此接口注销之前注册的水印处理回调。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [WatermarkCallback](js-apis-print.md#printwatermarkcallback24) | 否 | 表示要注销的水印处理回调。不传入时取消调用方所有已注册的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';

let watermarkCallback: print.WatermarkCallback = (jobId: string, fd: number) => {
    console.info('Watermark callback triggered, jobId: ' + jobId + ', fd: ' + fd);
};

try {
    print.registerWatermarkCallback(watermarkCallback);
    console.info('registerWatermarkCallback success');
    // 取消注册指定的水印处理回调
    print.unregisterWatermarkCallback(watermarkCallback);
    console.info('unregisterWatermarkCallback success');
} catch (error) {
    console.error(`Failed to unregisterWatermarkCallback. Code: ${error.code}, message: ${error.message}`);
}
```

## print.notifyWatermarkComplete24+

notifyWatermarkComplete(jobId: string, result: WatermarkHandleResult): void

通知水印处理完成，以便继续执行后续打印流程。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jobId | string | 是 | 表示打印任务ID。 |
| result | [WatermarkHandleResult](js-apis-print.md#watermarkhandleresult24) | 是 | 表示水印处理结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |

**示例：**

```ts
import { print } from '@kit.BasicServicesKit';

let watermarkCallback: print.WatermarkCallback = (jobId: string, fd: number) => {
    console.info('Watermark callback triggered, jobId: ' + jobId + ', fd: ' + fd);

    try {
        // 处理水印后通知系统处理成功
        print.notifyWatermarkComplete(jobId, print.WatermarkHandleResult.WATERMARK_HANDLE_SUCCESS);
        console.info('notifyWatermarkComplete success');
    } catch (error) {
        console.error(`Failed to notifyWatermarkComplete. Code: ${error.code}, message: ${error.message}`);
    }
};

try {
    print.registerWatermarkCallback(watermarkCallback);
    console.info('registerWatermarkCallback success');
} catch (error) {
    console.error(`Failed to registerWatermarkCallback. Code: ${error.code}, message: ${error.message}`);
}
```
