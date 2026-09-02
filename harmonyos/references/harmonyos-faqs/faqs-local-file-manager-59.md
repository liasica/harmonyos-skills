---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-59
title: 沙箱目录/文件常见操作
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 沙箱目录/文件常见操作
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:2399a8d30d3a9d69027d62b69ff50b7de1216e42d9e9582c976fe6267b4677b1
---

## 问题现象

出于安全考虑，对系统文件夹访问权限被收回，想要访问系统文件夹里的文件，必须使用[DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)打开可视化交互页面，那么开发过程中涉及到的对各类文件的操作，就要依靠沙箱来实现，应该怎样访问沙箱中的文件呢？

## 背景知识

* [应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)是安全防护为目的的隔离机制，避免数据受到恶意路径穿越访问，开发者可以使用Device File Browser[访问设备文件](../harmonyos-guides/ide-device-file-explorer.md)。
* 应用沙箱路径下通过[@ohos.file.fs](../harmonyos-references/js-apis-file-fs.md)读写文件，经过映射转换，实际读写的是真实物理路径中的应用文件。

## 解决方案

* 查看正在调试的设备的沙箱文件：
  + 通过IDE的可视化工具Device File Browser中查看设备文件目录，该工具可以在IDE中通过View -> Tool Windows -> Device File Browser打开，Device File Browser对应沙箱目录如下：/data/app/el2/100/base/{应用包名}/haps/entry/files。
  + 通过命令行的方式访问debug应用的沙箱目录，API 15前后的系统版本访问方式不同，参考：[命令行方式访问应用沙箱](../harmonyos-guides/ide-device-file-explorer.md#section48216711204)。
* 获取沙箱路径下的文件列表：

  fs.listFile列出文件夹下所有文件名，支持递归列出所有文件名（包含子目录下），支持文件过滤，代码示例请参考：[fs.listFile](../harmonyos-references/js-apis-file-fs.md#fileiolistfile)。
* 读取沙箱路径下的文件：

  以读取json文件为例，首先通过[openSync](../harmonyos-references/js-apis-fileio.md#fileioopensync)打开沙箱文件路径，然后[fs.writeSync](../harmonyos-references/js-apis-file-fs.md#fileiowritesync)将数据写入文件，最后通过[fs.readTextSync](../harmonyos-references/js-apis-file-fs.md#fileioreadtextsync)直接读取文件的文本内容，代码示例如下：

  ```ts
  import { fileIo as fs } from '@kit.CoreFileKit';
  import { common } from '@kit.AbilityKit';

  @Entry
  @Component
  struct ReadFilePage {
    build() {
      Column() {
        Text('读取文件测试')
          .padding(40)
          .onClick(()=>{
            let context = this.getUIContext().getHostContext() as common.Context;
            let pathDir = context.filesDir;
            let filePath = pathDir + '/test.json';
            let json:ESObject = {key:1};
            let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
            fs.writeSync(file.fd, JSON.stringify(json));
            let json2 = fs.readTextSync(filePath);
            console.info(`读取的json: : ${json2}`);
            fs.closeSync(file);
          })
      }
    }
  }
  ```
* 删除沙箱路径文件：
  + [fs.unlink](../harmonyos-references/js-apis-file-fs.md#fileiounlink)：删除单个沙箱路径文件，使用promise异步回调。
  + [fs.rmdir](../harmonyos-references/js-apis-file-fs.md#fileiormdir)：删除目录及其所有子目录和文件，使用promise异步回调。该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlink接口删除单个文件。
* Native侧访问应用沙箱文件：[Native侧实现沙箱文件访问](faqs-local-file-manager-59.md)有ArkTS侧获取沙箱路径传递给Native侧访问文件和Native侧直接拼接沙箱路径访问文件两种方案。

## 常见FAQ

Q：Image组件可以直接使用传入沙箱路径进行显示吗？

A：Image组件不能直接传入应用沙箱路径，需要传入应用沙箱uri，拿到文件的沙箱路径后，通过调用@ohos.file.fileUri模块的[fileUri.getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)将沙箱路径转化为沙箱uri，传入之后即可正常显示。

Q：使用listFiles并传入过滤器filter来获取指定后缀名的文件名时，如何排除目录名，仅保留文件名？

A：[ListFileOptions](../harmonyos-references/js-apis-file-fs.md#listfileoptions11)中recursion为false时，返回当前目录下满足过滤要求的文件名及目录名，若不想返回目录名，可将recursion置为true，此时仅返回满足过滤要求的文件的相对路径（包含文件名）。

Q：如何将用户文件复制到应用的沙箱目录？

A：使用[fs.copy](../harmonyos-references/js-apis-file-fs.md#fileiocopy11)拷贝文件到沙箱即可，该API使用promise异步回调。
