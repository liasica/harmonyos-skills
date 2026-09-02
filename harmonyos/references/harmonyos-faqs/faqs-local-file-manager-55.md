---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-55
title: rawfile目录下文件夹如何复制到沙箱目录并读写
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > rawfile目录下文件夹如何复制到沙箱目录并读写
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:8451e66bccaea455b4ff410a341ee993da3d8bfa0ac54fea9ed1e0f8a0659137
---

## 问题现象

如何实现rawfile目录下文件夹复制到沙箱目录，并支持读写功能？

## 背景知识

应用资源文件目录分为在base目录、限定词目录、rawfile目录、resfile目录。而rawfile目录、resfile目录通常存放其他类型文件（例如txt文件、db文件等等），原始文件形式保存。rawfile目录和resfile目录同在[资源目录](../harmonyos-guides/resource-categories-and-access.md#资源目录)下，目录中的资源文件会被直接打包进应用，不经过编译，也不会分配资源ID。二者的主要不同之处在于访问方式：

* resfile目录：应用安装后，resfile资源会被解压到应用沙箱路径，通过Context属性resourceDir获取到resfile资源目录后，可通过文件路径以只读权限访问。
* rawfile目录：通过文件路径和文件名进行访问（"$rawfile('filename')"）；或者通过Context获取[resourceManager](../harmonyos-references/js-apis-resource-manager.md)后，调用资源管理接口访问。

应用沙箱是一种以安全防护为目的的隔离机制，避免数据受到恶意路径穿越访问。在这种沙箱的保护机制下，应用可见的目录范围即为“[沙箱目录](../harmonyos-guides/app-sandbox-directory.md)”。通常rawfile/resfile目录下文件/文件夹无法直接在应用中读写，需要复制到应用沙箱下才可以读写。

## 解决方案

假设rawfile目录下存在apps文件夹（路径：rawfile/apps），需将其复制到沙箱目录。由于rawfile目录下的文件夹无法跟随应用安装解压到沙箱目录，若需要将整个文件夹拷贝到沙箱目录，需要进行递归遍历文件夹等操作，不推荐。因此目前有以下两种推荐方案：

* **方案一：rawfile目录下的文件夹直接复制到resfile目录下（resfile/apps），然后再复制到沙箱。**由于resfile下文件夹随应用安装解压到应用沙箱目录，但是仅能以只读方式访问，所以也需要将其文件复制到沙箱目录下进行读写。
  1. 通过context.resourceDir获取resfile目录，context.filesDir获取沙箱目录。
  2. 使用[fs.copyDirSync()](../harmonyos-references/js-apis-file-fs.md#fileiocopydirsync10)把resfile/apps直接复制到沙箱目录。
* **方案二：把需要复制的目录压缩成zip，复制zip并解压到沙箱目录。**
  1. 通过[getRawFd()](../harmonyos-references/js-apis-resource-manager.md#getrawfd9)获取rawfile/apps.zip所在hap包的descriptor信息（示例代码中的参数data）。
  2. 使用buffer将rawfile/apps.zip文件内容复制到沙箱临时文件路径（示例代码中的参数filepath）。
  3. 使用[zlib.decompressFile()](../harmonyos-references/js-apis-zlib.md#zlibdecompressfile9)解压zip文件至沙箱通用文件路径（示例代码中的参数sandboxPath）。

完整示例参考如下：

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

## 常见FAQ

Q：zlib.decompressFile()的参数inFile和outFile可以取到项目内的路径吗？

A：inFile和outFile文件路径必须为沙箱路径。

Q：为什么context.getApplicationContext().resourceDir返回值是空字符串？

A：通过ApplicationContext获取的是应用级别的应用文件路径，这其中不包括resourceDir，详情参考[获取应用文件路径](../harmonyos-guides/application-context-stage.md#获取应用文件路径)。

## 总结

|  | 方案一 | 方案二 |
| --- | --- | --- |
| 关键接口 | fs.mkdirSync、 fs.copyDirSync | resourceManager.getRawFd、 fs.openSync、fs.readSync、fs.writeSync、zlib.decompressFile |
| 使用场景 | 适用于文件夹下嵌套层级少，子目录、子文件小的情况，因为copyDirSync直接拷贝文件夹会造成应用开销大，占用运行内存 | 适用于文件夹下嵌套层级多，子目录、子文件大的情况，该方案利用了压缩、解压，buffer循环读取可以减少应用开销、占用内存较少 |

综上所述，需要读写rawfile文件夹需要先复制到应用沙箱，两种方案需要根据开发者具体场景进行选择。
