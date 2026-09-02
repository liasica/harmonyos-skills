---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-31
title: 如何使用打印服务
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何使用打印服务
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:817afbacbeac781107b32cbd2d8fc321b1c48e98e35d21fcf377f8caee18ac24
---

## 问题现象

调用文件打印服务时，传入数据，跳转到打印页面显示文件格式不支持，但是API上显示是支持图片（.jpg, .png）和文件（.pdf）的，请问如何正确使用打印服务。

## 背景知识

系统提供调用基础打印功能的API，参考文档：[打印](../harmonyos-references/js-apis-print.md)。

## 解决方案

* 打印图片参考示例代码的步骤如下：
  1. 通过getContext接口获取Context上下文。
  2. 获取“resources/rawfile”目录下对应的rawfile文件内容，使用callback异步回调。
  3. 获取资源路径下的数据。
  4. 获取沙箱路径。
  5. 以同步方法打开文件并将数据写入文件。
  6. 调用系统打印接口。

* 打印PDF文件参考示例代码的步骤如下：
  1. 通过getContext接口获取Context上下文。
  2. 获取“resources/rawfile”目录下对应的rawfile文件内容，使用callback异步回调。
  3. 获取资源路径下的数据。
  4. 获取沙箱路径。
  5. 以同步方法打开文件并将数据写入文件。
  6. 设置待打印文件名称jobName。
  7. 创建三方应用实现的PrintDocumentAdapter接口实例printAdapter。
  8. 创建打印参数[printAttributes](../harmonyos-references/js-apis-print.md#printattributes11)。
  9. 调用系统打印接口，并传入以上三个参数。

打印图片、打印PDF文件完整示例参考如下：

```ts
import { BusinessError, print } from '@kit.BasicServicesKit';
import fs, { ReadOptions, WriteOptions } from '@ohos.file.fs';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('打印图片').onClick(() => {
        // 通过getContext接口获取Context上下文。
        let context: Context = this.getUIContext().getHostContext() as Context;
        // 获取resources/rawfile目录下对应的rawfile文件内容，使用callback异步回调。
        context.resourceManager.getRawFileContent("xx.jpg", (error: BusinessError, value: Uint8Array) => {
          if (error != null) {
            console.error("error code: %u, msg: %s", error.code, error.message);
          } else {
            // 获取资源路径下的数据。
            let myBuffer:ArrayBufferLike = value.buffer;
            // 获取沙箱路径。
            let filePath = context.cacheDir + "/xx.jpg";
            // 以同步方法打开文件并将数据写入文件。
            let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
            fs.writeSync(file.fd, myBuffer);
            let fileFd = 'fd://' + file.fd;

            // 调用系统打印接口。
            print.print([fileFd], context).then((printTask: print.PrintTask) => {
              printTask.on('succeed', () => {
                console.info(`result ==> 调用打印服务成功`);
              });
              printTask.on('fail', () => {
                console.info(`result ==> 调用打印服务失败`);
              });
            }).catch((err: BusinessError) => {
              console.error(`result ==> ${JSON.stringify(err)}`);
            });
          };
        });
      })
      Button('打印PDF文件').onClick(() => {
        // 通过getContext接口获取Context上下文。
        let context: Context = this.getUIContext().getHostContext() as Context;
        // 获取resources/rawfile目录下对应的rawfile文件内容，使用callback异步回调。
        context.resourceManager.getRawFileContent("test.pdf", (error: BusinessError, value: Uint8Array) => {

          if (error != null) {
            console.error("error code: %u, msg: %s", error.code, error.message);
          } else {
            // 获取资源路径下的数据。
            let myBuffer: ArrayBufferLike = value.buffer;
            // 以同步方法打开文件并将数据写入文件。
            let filePath = context.cacheDir + "/test.pdf";
            let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
            fs.writeSync(file.fd, myBuffer);
            // 设置待打印文件名称`jobName`。
            let jobName: string = 'test';
            // 创建三方应用实现的PrintDocumentAdapter接口实例`printAdapter`。
            let printAdapter: print.PrintDocumentAdapter = {
              onStartLayoutWrite(jobId: string,
                oldAttrs: print.PrintAttributes,
                newAttrs: print.PrintAttributes,
                fd: number,
                writeResultCallback: (jobId: string, writeResult: print.PrintFileCreationState) => void): void {
                console.info('printxxx', 'jobId:', jobId, 'oldAttrs:', JSON.stringify(oldAttrs), 'newAttrs:',
                  JSON.stringify(newAttrs), 'fd:', fd.toString());
                let bufSize = 4096;
                let readSize = 0;
                let buf = new ArrayBuffer(bufSize);
                let readOptions: ReadOptions = {
                  offset: readSize,
                  length: bufSize
                };
                let readLen = fs.readSync(file.fd, buf, readOptions);
                while (readLen > 0) {
                  readSize += readLen;
                  let writeOptions: WriteOptions = {
                    length: readLen
                  };
                  fs.writeSync(fd, buf, writeOptions);
                  readOptions.offset = readSize;
                  readLen = fs.readSync(file.fd, buf, readOptions);
                }

                writeResultCallback(jobId, print.PrintFileCreationState.PRINT_FILE_CREATED);
              },
              onJobStateChanged(): void {
              }
            };
            // 创建打印参数`printAttributes`。
            let printAttributes: print.PrintAttributes = {
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
            // 调用系统打印接口，并传入以上三个参数。
            print.print(jobName, printAdapter, printAttributes, context).then((printTask: print.PrintTask) => {
              printTask.on('succeed', () => {
                console.info('print state is succeed');
              });
            }).catch((err: BusinessError) => {
              console.error('print err ' + JSON.stringify(err));
            });
          };
        });
      })
    }
  }
}
```

## 常见FAQ

Q：使用系统打印API如何不拉起预览界面？

A：ArkTS API中的打印API需要拉起预览界面，不拉起预览界面请使用C API，参考：[OH\_Print](../harmonyos-references/capi-oh-print.md)。
