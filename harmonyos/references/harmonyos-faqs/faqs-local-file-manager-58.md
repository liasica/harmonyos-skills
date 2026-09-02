---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-58
title: 如何读取rawfile目录下的文件
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何读取rawfile目录下的文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:748821bbb1d62a210baac698e601c4640fac2147532baeb67bfa5cf804ed9198
---

## 问题现象

rawfile目录会存放项目资源，那么如何读取rawfile目录下的文件？

## 背景知识

* [rawfile目录](../harmonyos-guides/resource-categories-and-access.md#资源目录)是项目的资源目录。支持创建多层子目录，文件夹允许放置各种类型的资源文件。需要注意的是：rawfile目录下的资源文件会被直接打包进入应用包体内，不经过编译，所以不会分配资源ID，需要通过指定文件路径和文件名访问。
* [资源管理模块resourceManager](../harmonyos-references/js-apis-resource-manager.md)：根据当前[Configuration](../harmonyos-references/js-apis-resource-manager.md#configuration)配置包括语言、区域、横竖屏、Mcc（移动国家码）和Mnc（移动网络码）、Device capability（设备类型）、Density（分辨率）获取最匹配的应用资源或系统资源。
* [resourceManager.getRawFileContentSync](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontentsync10)：获取resources/rawfile目录下对应的rawfile文件内容，使用同步形式返回。

## 解决方案

对于rawfile目录下面的文件一般分为两类：

* 资源文件（例如string、color、plural等json文件，通过$rawfile访问，返回Resource类型对象，适用于界面控件绑定资源文件情形等，通常不涉及写操作）：需要注意的是资源文件需要通过指定文件路径和文件名来访问。
  + 单Hap/Hsp包内访问：通过$rawfile('filename')形式访问，其中，filename为rawfile目录下文件的相对路径，文件名需要包含后缀，路径开头不可以“/”开头。格式示例如下：

    ```ts
    Image($rawfile('testPic.png')); // 需要替换为实际项目中的文件名
    ```
  + 跨Hap/Hsp访问：（由于Har包是随模块编译的，直接对应的模块中引用即可，不涉及跨包访问，这里不再赘述。）需要先在entry中oh-package.json5中添加module依赖；使用格式为$rawfile('[Hsp].filename')，其中[Hsp]为Hsp模块名，filename仍为rawfile目录下文件的相对路径。除此之外，和其他目录下访问资源文件一致，详情请见[资源访问](../harmonyos-guides/resource-categories-and-access.md#资源访问)。

* 其他类型文件（例如，db文件、txt文件等，原始文件形式保存）：需要用到资源管理模块resourceManager的常见接口：

  |  | [getRawFileContent](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontent9) | [getRawFd](../harmonyos-references/js-apis-resource-manager.md#getrawfd9) |
  | --- | --- | --- |
  | 功能 | 用于获取resources/rawfile目录下对应的rawfile文件内容。 | 用于获取resources/rawfile目录下rawfile文件所在Hap的descriptor信息。 |
  | 常见适用场景 | 处理文件内容小的文件，直接将rawfile目录下的文件的二进制buffer读取到内存中进行读写。 | 处理文件内容大的文件，需要获取rawfile目录下的文件的fd，将rawfile目录下的文件拷贝到应用沙箱下，再对沙箱文件进行读写。 |

  + 文件内容小的文件，进行访问（以文本文件，举例说明）：

    ```ts
    // 小文件读取
    Button('读取小文件').onClick(() => {
      let context = this.getUIContext().getHostContext();
      let fileName: string = 'testTxt.txt'; // 需要替换为实际项目中的文件名
      // 获取文件内容
      // 确保在工程目录src/main/resources/rawfile里存在需要读取的文件
      context?.resourceManager.getRawFileContent(fileName, (error, value) => {
        if (error) {
          hilog.error(LogDomain, 'TestShow-', `error Code: ${error.code} error Msg: ${error.message}`);
          return;
        }
        // 这里读取到文件内容可以进行下一步操作
        let myBuffer: ArrayBufferLike = value.buffer;
        hilog.info(LogDomain, 'TestShow-', `buffer length: ${myBuffer.byteLength}`);
      });
    });
    ```
  + 文件内容大的文件，进行访问（以数据库db文件，举例说明）：
    1. 先通过getRawFd获取rawfile目录下的文件描述符fd。
    2. 然后，在应用沙箱里创建对应的沙箱文件，获取到对应的文件描述符fd。
    3. 将rawfile目录下的文件通过buffer的方式拷贝到沙箱文件下。
    4. 最后，在应用沙箱下访问对应文件。

    ```ts
    // 大文件读取，以数据库db文件为例
    Button('读取大文件').onClick(() => {
      let context = this.getUIContext().getHostContext();
      try {
        let dirPath = context?.getApplicationContext().databaseDir + '/entry';
        fs.mkdirSync(dirPath);
        let filePath: string = '/rdb'; //待创建的沙箱目录名 需要替换为项目中的实际待创建的沙箱目录名
        dirPath = dirPath + filePath;
        fs.mkdirSync(dirPath);
      } catch (error) {
        hilog.error(LogDomain, 'TestShow-', 'initDataBaseDir err');
      }
      let dbFileName: string = 'test.db'; // 项目中实际的db文件名
      try {
        let dbFilePath = 'rdb/'; // 替换为项目中实际文件路径
        context?.resourceManager.getRawFd(dbFilePath + dbFileName, (error, value) => {
          if (error != null) {
            hilog.error(LogDomain, 'TestShow-', `error Code: ${error.code} error Msg: ${error.message}`);
          } else {
            hilog.info(LogDomain, 'TestShow-', value.length.toString());
            this.saveFileToSandbox(value, dbFileName);
          }
        });
      } catch (err) {
        let error: BusinessError = err as BusinessError;
        hilog.error(LogDomain, 'TestShow-', `error Code: ${error.code} error Msg: ${error.message}`);
      }
    });
    ```

    其中saveFileToSandbox方法如下：

    ```ts
    /**
     * 保存文件到沙箱里
     * @param file 文件的信息
     * @param dbFileName 文件名
     */
    saveFileToSandbox(file: resourceManager.RawFileDescriptor, dbFileName: string) {
      let context = this.getUIContext().getHostContext();
      if (!context) {
        hilog.error(LogDomain, 'TestShow-', `error: context 为空`);
        return;
      }
      // 创建缓存文件(当前是覆盖式创建)
      let filePath: string =
        context.getApplicationContext().databaseDir + '/entry/rdb/' + dbFileName; // 引号中的内容需要替换为待读取文件在项目中的实际路径
      let cacheFile = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
      // 读取缓冲区大小
      let bufferSize = 30000;
      let buffer = new ArrayBuffer(bufferSize); // 创建buffer缓冲区
      // 要copy的文件的offset和length
      let currentOffset = file.offset;
      let readOption: ReadOptions = {
        offset: currentOffset, // 期望读取文件的位置。可选，默认从当前位置开始读
        length: bufferSize // 每次期望读取数据的长度。可选，默认缓冲区长度
      };
      // 后面len会一直减，直到没有
      while (true) {
        // 读取buffer容量的内容
        let readLength = fs.readSync(file.fd, buffer, readOption);
        // 写入buffer容量的内容
        // 写到cacheFile里
        fs.writeSync(cacheFile.fd, buffer, { length: readLength });
        // 判断后续内容，修改读文件的参数
        // buffer没读满代表文件读完了
        if (readLength < bufferSize) {
          break;
        }
        if (readOption.offset != undefined) {
          readOption.offset += readLength;
        }
      }
      hilog.info(LogDomain, 'TestShow-', 'Copy Success!');
      fs.close(cacheFile);
    }
    ```

  完整示例参考如下：

  ```ts
  import fs, { ReadOptions } from '@ohos.file.fs';
  import { resourceManager } from '@kit.LocalizationKit';
  import { application, common } from '@kit.AbilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  const LogDomain = 0x0000;

  @Entry
  @Component
  struct rwRawFile {
    build() {
      Column() {
        Image($rawfile('testPic.png')); // 需要替换为实际项目中的文件名

        Button('读取文件').onClick(() => {
          let context = this.getUIContext().getHostContext();
          let fileName: string = 'testTxt.txt'; // 需要替换为实际项目中的文件名
          context?.resourceManager.getRawFileContent(fileName, (error, readRes) => {
            if (error) {
              hilog.error(LogDomain, 'TestShow-', `error code: ${error.code} , error msg: ${error.message}`);
              return;
            }
            // 这里可以对读取结果进行后续处理。
            hilog.info(LogDomain, 'TestShow-', `readRes length: ${readRes.byteLength}`);
          });
        });

        // 小文件读取
        Button('读取小文件').onClick(() => {
          let context = this.getUIContext().getHostContext();
          let fileName: string = 'testTxt.txt'; // 需要替换为实际项目中的文件名
          // 获取文件内容
          // 确保在工程目录src/main/resources/rawfile里存在需要读取的文件
          context?.resourceManager.getRawFileContent(fileName, (error, value) => {
            if (error) {
              hilog.error(LogDomain, 'TestShow-', `error Code: ${error.code} error Msg: ${error.message}`);
              return;
            }
            // 这里读取到文件内容可以进行下一步操作
            let myBuffer: ArrayBufferLike = value.buffer;
            hilog.info(LogDomain, 'TestShow-', `buffer length: ${myBuffer.byteLength}`);
          });
        });

        // 大文件读取，以数据库db文件为例
        Button('读取大文件').onClick(() => {
          let context = this.getUIContext().getHostContext();
          try {
            let dirPath = context?.getApplicationContext().databaseDir + '/entry';
            fs.mkdirSync(dirPath);
            let filePath: string = '/rdb'; //待创建的沙箱目录名 需要替换为项目中的实际待创建的沙箱目录名
            dirPath = dirPath + filePath;
            fs.mkdirSync(dirPath);
          } catch (error) {
            hilog.error(LogDomain, 'TestShow-', 'initDataBaseDir err');
          }
          let dbFileName: string = 'test.db'; // 项目中实际的db文件名
          try {
            let dbFilePath = 'rdb/'; // 替换为项目中实际文件路径
            context?.resourceManager.getRawFd(dbFilePath + dbFileName, (error, value) => {
              if (error != null) {
                hilog.error(LogDomain, 'TestShow-', `error Code: ${error.code} error Msg: ${error.message}`);
              } else {
                hilog.info(LogDomain, 'TestShow-', value.length.toString());
                this.saveFileToSandbox(value, dbFileName);
              }
            });
          } catch (err) {
            let error: BusinessError = err as BusinessError;
            hilog.error(LogDomain, 'TestShow-', `error Code: ${error.code} error Msg: ${error.message}`);
          }
        });
      };
    }

    /**
     * 保存文件到沙箱里
     * @param file 文件的信息
     * @param dbFileName 文件名
     */
    saveFileToSandbox(file: resourceManager.RawFileDescriptor, dbFileName: string) {
      let context = this.getUIContext().getHostContext();
      if (!context) {
        hilog.error(LogDomain, 'TestShow-', `error: context 为空`);
        return;
      }
      // 创建缓存文件(当前是覆盖式创建)
      let filePath: string =
        context.getApplicationContext().databaseDir + '/entry/rdb/' + dbFileName; // 引号中的内容需要替换为待读取文件在项目中的实际路径
      let cacheFile = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
      // 读取缓冲区大小
      let bufferSize = 30000;
      let buffer = new ArrayBuffer(bufferSize); // 创建buffer缓冲区
      // 要copy的文件的offset和length
      let currentOffset = file.offset;
      let readOption: ReadOptions = {
        offset: currentOffset, // 期望读取文件的位置。可选，默认从当前位置开始读
        length: bufferSize // 每次期望读取数据的长度。可选，默认缓冲区长度
      };
      // 后面len会一直减，直到没有
      while (true) {
        // 读取buffer容量的内容
        let readLength = fs.readSync(file.fd, buffer, readOption);
        // 写入buffer容量的内容
        // 写到cacheFile里
        fs.writeSync(cacheFile.fd, buffer, { length: readLength });
        // 判断后续内容，修改读文件的参数
        // buffer没读满代表文件读完了
        if (readLength < bufferSize) {
          break;
        }
        if (readOption.offset != undefined) {
          readOption.offset += readLength;
        }
      }
      hilog.info(LogDomain, 'TestShow-', 'Copy Success!');
      fs.close(cacheFile);
    }

    /**
     * 读取Hap/Hsp包内文件
     * @param packageName 包名
     * @param fileName 文件名
     */
    readPackageFile(packageName: string, fileName: string) {
      let moduleContext: common.Context;
      let context = this.getUIContext().getHostContext();
      application.createModuleContext(context, packageName).then((data: Context) => {
        // 文件读取
        moduleContext = data;
        moduleContext.resourceManager.getRawFd(fileName).then((res) => {
          // 对读取结果进行其他处理
          hilog.info(LogDomain, 'TestShow-', `show file fd: ${res.fd}`);
        }).catch((error: BusinessError) => {
          hilog.error(LogDomain, 'TestShow-', `error Code: ${error.code} error Msg: ${error.message}`);
        });
      }).catch((error: BusinessError) => {
        let code: number = (error as BusinessError).code;
        let message: string = (error as BusinessError).message;
        hilog.error(LogDomain, 'TestShow-', `createModuleContext failed, error.code: ${code}, error.message: ${message}`);
      });
    }

  }
  ```

## 常见FAQ

Q：使用getRawFd读取rawfile中的文件中出现缺失问题如何解决？

A：getRawFd获取的文件描述符为当前Hap的并不是resources/rawfile目录下rawfile文件的，因此使用getRawFileContent代替getRawFd获取当前文件内容。

Q：官网对于getRawFd接口官网API说明是访问Hap包目录的下的文件（resourceManager.getRawFd('rawfilepath')可获取rawfile所在Hap包的descriptor信息），那么如何在entry下获取Hsp的rawfile资源？

A：对于跨Hap/Hsp的模块需要createModuleContext接口，先获取对应模块的context，再使用该context调用getRawFd获取文件句柄。

```ts
/**
 * 读取Hap/Hsp包内文件
 * @param packageName 包名
 * @param fileName 文件名
 */
readPackageFile(packageName: string, fileName: string) {
  let moduleContext: common.Context;
  let context = this.getUIContext().getHostContext();
  application.createModuleContext(context, packageName).then((data: Context) => {
    // 文件读取
    moduleContext = data;
    moduleContext.resourceManager.getRawFd(fileName).then((res) => {
      // 对读取结果进行其他处理
      hilog.info(LogDomain, 'TestShow-', `show file fd: ${res.fd}`);
    }).catch((error: BusinessError) => {
      hilog.error(LogDomain, 'TestShow-', `error Code: ${error.code} error Msg: ${error.message}`);
    });
  }).catch((error: BusinessError) => {
    let code: number = (error as BusinessError).code;
    let message: string = (error as BusinessError).message;
    hilog.error(LogDomain, 'TestShow-', `createModuleContext failed, error.code: ${code}, error.message: ${message}`);
  });
}
```
