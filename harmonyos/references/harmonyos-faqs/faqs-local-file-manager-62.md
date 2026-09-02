---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-62
title: rawfile下文件拷贝到沙箱后大小和内容错误如何解决
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > rawfile下文件拷贝到沙箱后大小和内容错误如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:02097474456cd7fa9d808c0ff1c03f9e73b0b17f3c4104ad30c63bf046558b69
---

## 问题现象

使用resourceManager.getRawFd获取rawfile目录下资源文件描述符fd，再使用fileIo.copyfile拷贝到沙箱目录后，文件大小及内容都异常。

问题代码示例参考如下：

```screen
import { common } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

function copyRawFileToSdcard(context: common.Context) {
  let destRoot = context.filesDir;
  // rawfile下的文件名
  let srcFileName = 'test_1.txt'
  let destFilePath = destRoot + '/test/copy_' + srcFileName;
  // 创建文件目录
  fileIo.mkdir(destRoot + '/test').catch((error: BusinessError) => {
    // 可能目录已存在或者没有权限
    console.error(`copyRawFileToSdcard mkdir fail: ${error.code}, ${error.code}`)
  }).then(async () => {
    // 创建目录成功
    console.info('copyRawFileToSdcard mkdir success')
    // 获取rawfile的fd
    let data: resourceManager.RawFileDescriptor = await context.resourceManager.getRawFd(srcFileName);
    fileIo.copyFile(data.fd, destFilePath, 0).then(() => {
      // 文件拷贝成功
      console.info('copyRawFileToSdcard write success')
    }).catch((error: BusinessError) => {
      // 文件拷贝失败
      console.error(`copyRawFileToSdcard write exception : ${error.code}, ${error.code}`)
    })
  })
}
```

原始文件与拷贝后文件对比如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/KDR9wT8ESTuca_yLDGxbVg/zh-cn_image_0000002659138375.png "点击放大")

## 背景知识

* [rawfile目录](../harmonyos-guides/resource-categories-and-access.md#资源目录)属于应用工程的资源目录，该目录下的文件目录中的资源文件会被直接打包进应用，不经过编译，也不会被赋予资源文件ID。可以通过指定文件路径和文件名访问。
* 可以通过[resourceManager.getRawFileContent](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontent9)获取rawfile目录下的文件内容。

## 问题定位

rawfile目录下文件属于应用工程的[资源文件](../harmonyos-guides/resource-categories-and-access.md#资源目录)，获取的resourceManager.RawFileDescriptor中的资源fd并非文件系统的文件描述符fd，不能直接通过[@ohos.file.fs (文件管理)](../harmonyos-references/js-apis-file-fs.md)去访问和管理，需要通过[@ohos.resourceManager (资源管理)](../harmonyos-references/js-apis-resource-manager.md#resourcemanager)模块访问。

## 分析结论

rawfile目录下文件不能直接使用[@ohos.file.fs (文件管理)](../harmonyos-references/js-apis-file-fs.md)去访问和管理。

## 解决方案

1. 使用resourceManager.getRawFileContent获取rawfile目录下文件内容。
2. 使用fileIo.createStreamSync获取目标文件流fileStream，再使用fileStream.writeSync写入。

完整示例参考如下：

```screen
import { common } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  copyRawFileToSdcard(context: common.Context) {
    let destRoot = context.filesDir;
    // rawfile下的文件名
    let srcFileName = 'test_1.txt';
    let destFilePath = destRoot + '/test/copy_' + srcFileName;
    // 创建文件目录
    fileIo.mkdir(destRoot + '/test').then(async () => {
      // 创建目录成功
      console.info('copyRawFileToSdcard mkdir success');
      context.resourceManager.getRawFileContent(srcFileName, (error: BusinessError, data: Uint8Array) => {
        if (error != null) {
          promptAction.openToast({ message: '拷贝失败' });
          console.error(`error.code is ${error.code},error.message is ${error.message},`);
        } else {
          let fileStream = fileIo.createStreamSync(destFilePath, 'w+');
          fileStream.writeSync(data.buffer);
          fileStream.close();
          // 文件拷贝成功
          promptAction.openToast({ message: '拷贝成功' });
          console.info('copyRawFileToSdcard write success');
        }
      });
    }).catch((error: BusinessError) => {
      // 可能目录已存在或者没有权限
      promptAction.openToast({ message: '拷贝失败' });
      console.error(`copyRawFileToSdcard mkdir fail: ${error.code}, ${error.code}`);
    });
  }

  build() {
    Column() {
      Button('开始拷贝')
        .width(200)
        .height(40)
        .onClick(() => {
          this.copyRawFileToSdcard(this.context);
        })
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```

## 总结

1. 使用resourceManager.getRawFd获取rawfile目录下资源文件描述符fd，并非文件管理系统中的文件描述符fd，两者指向的并非同一文件。
2. rawfile目录下的文件拷贝需要使用resourceManager.getRawFileContent获取其文件内容，再写入到对应文件中。

## 常见FAQ

Q：使用[getRawFileContent](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontent9)方法，path是否可以传入文件夹路径？

A：不能。因为getRawFileContent方法是用于获取resources/rawfile目录下对应的rawfile文件内容，传入文件夹路径，无法确保文件夹下是否有多个文件，所以getRawFileContent()中path传参不能传入resources/rawfile目录下的文件夹路径，只能传入resources/rawfile目录下的文件路径，比如：context.resourceManager.getRawFileContent('OA/index.html') 。

Q：getRawFileContent('BannerData.json')读取不到rawfile的对应json文件。

A：需要修改路径，把filename换成"rawfile/BannerData.json"即可。
