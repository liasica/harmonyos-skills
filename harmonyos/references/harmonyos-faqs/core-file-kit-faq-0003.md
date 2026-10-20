---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/core-file-kit-faq-0003
title: rawfile目录文件读取与访问常见问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 常见问题 > rawfile目录文件读取与访问常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:43+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:8918147d61d35574472fe042a03d23b9603912ea5b881ea47b3bc8e86b06517d
---

**Q：如何实现rawfile目录下文件夹复制到沙箱目录，并支持读写功能？**

**A**：假设rawfile目录下存在apps文件夹（路径：rawfile/apps），需将其复制到沙箱目录。

由于rawfile目录下的文件夹无法跟随应用安装解压到沙箱目录，若需要将整个文件夹拷贝到沙箱目录，需要进行递归遍历文件夹等操作，不推荐。因此目前有以下两种推荐方案：

方案一：rawfile目录下的文件夹直接复制到resfile目录下（resfile/apps），然后再复制到沙箱。

由于resfile下文件夹随应用安装解压到应用沙箱目录，但是仅能以只读方式访问，所以也需要将其文件复制到沙箱目录下进行读写。

1. 通过context.resourceDir获取resfile目录，context.filesDir获取沙箱目录。
2. 使用[fs.copyDirSync()](../harmonyos-references/js-apis-file-fs.md#fileiocopydirsync10)把resfile/apps直接复制到沙箱目录。

方案二：把需要复制的目录压缩成zip，复制zip并解压到沙箱目录。

1. 通过[getRawFd()](../harmonyos-references/js-apis-resource-manager.md#getrawfd9)获取rawfile/apps.zip所在hap包的descriptor信息（示例代码中的参数data）。
2. 使用buffer将rawfile/apps.zip文件内容复制到沙箱临时文件路径（示例代码中的参数filepath）。
3. 使用[zlib.decompressFile()](../harmonyos-references/js-apis-zlib.md#zlibdecompressfile9)解压zip文件至沙箱通用文件路径（示例代码中的参数sandboxPath）。

示例代码如下：

```ts
import { fileIo } from '@kit.CoreFileKit';
import { zlib } from '@kit.BasicServicesKit';
import type { common } from '@kit.AbilityKit';
import type { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct RawfileToSandbox {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Column() {
      // 方案一：rawfile目录下的文件夹直接复制到resfile目录下（resfile/apps），然后再复制到沙箱。
      Button('复制resFile目录下文件夹到沙箱目录')
        .height(100)
        .width('50%')
        .onClick(() => {
          try {
            let srcPath = this.context.resourceDir + '/apps/';
            let destPath = this.context.filesDir + '/apps/';
            // 判断文件夹是否存在
            if (!fileIo.accessSync(destPath)) {
              fileIo.mkdirSync(destPath);
            }
            fileIo.copyDirSync(srcPath, destPath, 0);
          } catch (error) {
            let err: BusinessError = error as BusinessError;
            console.error(`copy directory failed with error message: ${JSON.stringify(err)}`);
          }
        });

      // 方案二：把需要复制的目录压缩成zip，复制zip并解压到沙箱目录。
      Button('复制zip到沙箱，并解压zip')
        .height(100)
        .width('50%')
        .onClick(async () => {
          // 通过fd来进行拷贝，避免文件过大的内存占用问题
          // data.fd是hap包的fd，data.offset表示目标文件在hap包中的偏移，data.length表示目标文件的长度
          this.context.resourceManager.getRawFd('apps.zip', async (err, data) => {
            try {
              let sandboxPath = this.context.filesDir;
              console.info(`沙箱路径：${sandboxPath}`);
              let filePath = this.context.tempDir + '/bfapps.zip';
              console.info(`压缩文件路径：${filePath}`);
              let dest = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
              let bufsize = 4096;
              let buf = new ArrayBuffer(bufsize);
              let off = 0;
              let readLen = 0;

              // 把rawfile压缩包文件内容复制到沙箱路径
              let len = fileIo.readSync(data.fd, buf, { offset: data.offset + off, length: bufsize });
              while (len) {
                fileIo.writeSync(dest.fd, buf, { offset: off, length: len });
                readLen += len;
                if (readLen >= data.length) {
                  break;
                }
                off += len;
                if ((data.length - readLen) < bufsize) {
                  bufsize = data.length - readLen;
                }
                len = fileIo.readSync(data.fd, buf, { offset: data.offset + off, length: bufsize });
              }
              fileIo.closeSync(dest.fd);

              // 对沙箱路径下的压缩文件进行解压
              await zlib.decompressFile(filePath, sandboxPath);
              this.context.resourceManager.closeRawFd('apps.zip');
            } catch (e) {
              console.error(`failed, error = ${JSON.stringify(e)}`);
            }
          });
        });

    }
    .height(300)
    .width('100%')
    .justifyContent(FlexAlign.SpaceAround);
  }
}
```

**Q：zlib.decompressFile()的参数inFile和outFile可以取到项目内的路径吗？**

**A**：inFile和outFile文件路径必须为沙箱路径。

**Q：为什么context.getApplicationContext().resourceDir返回值是空字符串？**

**A**：通过ApplicationContext获取的是应用级别的应用文件路径，这其中不包括resourceDir，详情参考[获取应用文件路径](../harmonyos-guides/application-context-stage.md#获取应用文件路径)。

**Q：在APP开发中，需要使用JSON文件保存信息到本地或者服务器，如何在如下场景去读取JSON文件？**

* 场景一：读取放在工程rawfile目录下的JSON文件。
* 场景二：读取放在本地沙箱目录下的JSON文件。
* 场景三：读取网络接口返回的JSON文件。

**A**：读取JSON文件主要是读取文件二进制数据转为JSON字符串或者直接读取JSON字符串，然后解析对象数据。

模拟JSON文件，放在rawfile目录下或者沙箱filesDir目录下，定义数据类型，示例代码如下：

```json
{
  "CityCodeList":  [
    {
      "districtGeocode":"110100",
      "district":"北京"
    },
    {
      "districtGeocode":"110101",
      "district":"东城"
    },
    {
      "districtGeocode":"110102",
      "district":"朝阳"
    }
  ]
}
```

```ts
// 定义数据类
export class CityCode {
  cityCodeList: Array<CityCodeBean> = [];
}

export class CityCodeBean {
  districtGeocode: string = '';
  district: string = '';
}
```

* 场景一：读取放在工程rawfile目录下的JSON文件，并解析为对象。通过getRawFileContentSync读取文件，返回二进制数据。转字符串后，通过JSON.parse解析为对象。示例代码如下：

  ```ts
  getRawFileJsonData() {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let value: Uint8Array = context.resourceManager.getRawFileContentSync('testData.json');
      let citystr = buffer.from(value.buffer).toString();
      let cityObj: ESObject = JSON.parse(citystr);
      let cityInfoList: CityCode = cityObj;
      console.info('getRawFileJsonData：', JSON.stringify(cityInfoList));
    }
  ```
* 场景二：读取放在沙箱目录下的JSON文件，并解析为对象。通过[fs.readTextSync](../doccenter-references/api/js-apis-file-fs.md#fileioreadtextsync)读取文件，返回字符串文本数据，通过JSON.parse解析为对象。示例代码如下：

  ```ts
  getLocationFileJsonData() {
      // 读取文件，解析为对象
      let context = this.getUIContext().getHostContext() as common.Context;
      let pathDir = context.filesDir;
      let filePath = pathDir + '/testData.json';// 需要先把测试数据放入沙箱filesDir目录下
      try {
        let cityStr = fs.readTextSync(filePath);
        let cityObj: ESObject = JSON.parse(cityStr);
        let cityInfoList: CityCode = cityObj;
        console.info('getLocationFileJsonData：', JSON.stringify(cityInfoList));
      } catch (e) {
        console.error('fs.readTextSync failed error is : ', JSON.stringify(e));
      }
    }
  ```
* 场景三：读取通过网络接口返回的JSON文件。先使用[requestInStream](../harmonyos-references/js-apis-http.md#requestinstream10-1)获取文本，再通过httpRequest.on('dataReceive',()=>{})流式获取数据，httpRequest.on('dataEnd',()=>{})整合文本内容转化JSON数据。

  ```ts
  async httpGetJsonFile(): Promise<object> {
      return new Promise((resolve: Function) => {
        let res = new ArrayBuffer(0);
        let httpRequest = http.createHttp();
        httpRequest.on('dataReceive', (data: ArrayBuffer) => {
          const newRes = new ArrayBuffer(res.byteLength + data.byteLength);
          const resView = new Uint8Array(newRes);
          resView.set(new Uint8Array(res));
          resView.set(new Uint8Array(data), res.byteLength);
          res = newRes;
          console.info('res length: ', res.byteLength);
        });
        httpRequest.on('dataEnd', () => {
          try {
            let textDecoderOptions: util.TextDecoderOptions = {
              ignoreBOM: true
            };
            let decoder = util.TextDecoder.create('utf-8', textDecoderOptions);
            let str = decoder.decodeToString(new Uint8Array(res));
            console.info('test json read successful: ', str);
            let jsonStr = json.parse(str);
            resolve(jsonStr);
          } catch (err) {
            hilog.error(0x0000, 'testTag', `error: ${(err as BusinessError).code} ${(err as BusinessError).message}`);
          }
        });
        httpRequest.requestInStream('json文件的网络地址', // 后台服务器地址
          {
            method: http.RequestMethod.GET,
            header: {
              'Content-Type': 'application/json'
            },
            connectTimeout: 6000,
            readTimeout: 6000,
          }, (err, data) => {
            if (!err) {
              console.info('data: ', data);
            }
          }
        );
      });
    }
  ```

三个场景的完整代码示例如下：

```ts
import { buffer, util } from '@kit.ArkTS';
import { common } from '@kit.AbilityKit';
import json from '@ohos.util.json';
import { http } from '@kit.NetworkKit';
import fs from '@ohos.file.fs';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 定义数据类
export class CityCode {
  cityCodeList: Array<CityCodeBean> = [];
}

export class CityCodeBean {
  districtGeocode: string = '';
  district: string = '';
}
@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  // 读取文件，解析为对象
  aboutToAppear(): void {
    this.getRawFileJsonData();
    this.getLocationFileJsonData();
    this.httpGetJsonFile();
  }

  // 场景一：读取放在工程rawfile目录下的JSON文件，并解析为对象。
  getRawFileJsonData() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let value: Uint8Array = context.resourceManager.getRawFileContentSync('testData.json');
    let citystr = buffer.from(value.buffer).toString();
    let cityObj: ESObject = JSON.parse(citystr);
    let cityInfoList: CityCode = cityObj;
    console.info('getRawFileJsonData：', JSON.stringify(cityInfoList));
  }

  // 场景二：读取放在沙箱目录下的JSON文件，并解析为对象。
  getLocationFileJsonData() {
    // 读取文件，解析为对象
    let context = this.getUIContext().getHostContext() as common.Context;
    let pathDir = context.filesDir;
    let filePath = pathDir + '/testData.json';// 需要先把测试数据放入沙箱filesDir目录下
    try {
      let cityStr = fs.readTextSync(filePath);
      let cityObj: ESObject = JSON.parse(cityStr);
      let cityInfoList: CityCode = cityObj;
      console.info('getLocationFileJsonData：', JSON.stringify(cityInfoList));
    } catch (e) {
      console.error('fs.readTextSync failed error is : ', JSON.stringify(e));
    }
  }

  // 场景三：读取通过网络接口返回的JSON文件。
  async httpGetJsonFile(): Promise<object> {
    return new Promise((resolve: Function) => {
      let res = new ArrayBuffer(0);
      let httpRequest = http.createHttp();
      httpRequest.on('dataReceive', (data: ArrayBuffer) => {
        const newRes = new ArrayBuffer(res.byteLength + data.byteLength);
        const resView = new Uint8Array(newRes);
        resView.set(new Uint8Array(res));
        resView.set(new Uint8Array(data), res.byteLength);
        res = newRes;
        console.info('res length: ', res.byteLength);
      });
      httpRequest.on('dataEnd', () => {
        try {
          let textDecoderOptions: util.TextDecoderOptions = {
            ignoreBOM: true
          };
          let decoder = util.TextDecoder.create('utf-8', textDecoderOptions);
          let str = decoder.decodeToString(new Uint8Array(res));
          console.info('test json read successful: ', str);
          let jsonStr = json.parse(str);
          resolve(jsonStr);
        } catch (err) {
          hilog.error(0x0000, 'testTag', `error: ${(err as BusinessError).code} ${(err as BusinessError).message}`);
        }
      });
      httpRequest.requestInStream('json文件的网络地址', // 后台服务器地址
        {
          method: http.RequestMethod.GET,
          header: {
            'Content-Type': 'application/json'
          },
          connectTimeout: 6000,
          readTimeout: 6000,
        }, (err, data) => {
          if (!err) {
            console.info('data: ', data);
          }
        }
      );
    });
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

**Q：如何获取resource目录下的资源？**

A：可以使用以下两种方法获取资源文件：

1. 使用 r或*r*或rawfile 获取静态资源。程序运行时，资源路径不会改变。
2. 使用ResourceManager获取资源。适合动态获取，运行时可动态更改资源路径。

参考链接：[资源访问](../harmonyos-guides/resource-categories-and-access.md#资源访问)、[@ohos.resourceManager (资源管理)](../harmonyos-references/js-apis-resource-manager.md)。

**Q：rawfile目录会存放项目资源，那么如何读取rawfile目录下的文件？**

A：对于rawfile目录下面的文件一般分为两类：

* 资源文件（例如string、color、plural等json文件，通过$rawfile访问，返回Resource类型对象，适用于界面控件绑定资源文件情形等，通常不涉及写操作）：需要注意的是资源文件需要通过指定文件路径和文件名来访问。

  单Hap/Hsp包内访问：通过$rawfile('filename')形式访问，其中，filename为rawfile目录下文件的相对路径，文件名需要包含后缀，路径开头不可以"/"开头。格式示例如下：

  ```ts
  Image($rawfile('testPic.png')); // 需要替换为实际项目中的文件名
  ```

* 跨Hap/Hsp访问：（由于Har包是随模块编译的，直接对应的模块中引用即可，不涉及跨包访问，这里不再赘述。）需要先在entry中oh-package.json5中添加module依赖；使用格式为$rawfile('[Hsp].filename')，其中[Hsp]为Hsp模块名，filename仍为rawfile目录下文件的相对路径。除此之外，和其他目录下访问资源文件一致，详情请见[资源访问](../harmonyos-guides/resource-categories-and-access.md#资源访问)。
* 其他类型文件（例如，db文件、txt文件等，原始文件形式保存）：需要用到资源管理模块resourceManager的常见接口：

  |  | [getRawFileContent](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontent9) | [getRawFd](../harmonyos-references/js-apis-resource-manager.md#getrawfd9) |
  | --- | --- | --- |
  | 功能 | 用于获取resources/rawfile目录下对应的rawfile文件内容 | 用于获取resources/rawfile目录下rawfile文件所在Hap的descriptor信息 |
  | 常见适用场景 | 处理文件内容小的文件，直接将rawfile目录下的文件的二进制buffer读取到内存中进行读写 | 处理文件内容大的文件，需要获取rawfile目录下的文件的fd，将rawfile目录下的文件拷贝到应用沙箱下，再对沙箱文件进行读写 |

  文件内容小的文件，进行访问（以文本文件，举例说明）：

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

* 文件内容大的文件，进行访问（以数据库db文件，举例说明）：
  1. 先通过getRawFd获取rawfile目录下的文件描述符fd。
  2. 然后，在应用沙箱里创建对应的沙箱文件，获取到对应的文件描述符fd。
  3. 将rawfile目录下的文件通过buffer的方式拷贝到沙箱文件下。
  4. 最后，在应用沙箱下访问对应文件。

  代码示例如下：

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

  完整代码如下：

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

**Q：使用getRawFd读取rawfile中的文件中出现缺失问题如何解决？**

**A**：getRawFd获取的文件描述符为当前Hap的并不是resources/rawfile目录下rawfile文件的，因此使用getRawFileContent代替getRawFd获取当前文件内容。

**Q：官网对于getRawFd接口官网API说明是访问Hap包目录的下的文件（resourceManager.getRawFd('rawfilepath')可获取rawfile所在Hap包的descriptor信息），那么如何在entry下获取Hsp的rawfile资源？**

**A**：对于跨Hap/Hsp的模块需要createModuleContext接口，先获取对应模块的context，再使用该context调用getRawFd获取文件句柄。

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
