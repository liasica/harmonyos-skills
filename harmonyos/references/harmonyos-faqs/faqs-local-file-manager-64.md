---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-64
title: fs.writeSync写文件时如何在文件末尾追加内容
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > fs.writeSync写文件时如何在文件末尾追加内容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:820616545123a881a6753a2b68d1e2997d4e2d3f401caa78a798253850cde8f4
---

## 问题现象

如何使用fs.writeSync实现在文件末尾追加内容？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/Vjq81w2pQAWvmWT0sXtRnQ/zh-cn_image_0000002629059024.gif "点击放大")

## 解决方案

[fs.writeSync](../harmonyos-references/js-apis-file-fs.md#fileiowritesync)写文件时需要先使用[fs.openSync](../harmonyos-references/js-apis-file-fs.md#fileioopensync)打开文件，打开文件时可设置模式为“OpenMode.APPEND”，以追加方式打开。

```ts
import { systemDateTime } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
  @State message: string = '';

  build() {
    Column({ space: 30 }) {
      Text(`当前test.txt为文件的内容是：${this.message}`) // 展示文件内容
        .fontSize(30)
      Button('追加文本')
        .onClick(() => {
          let context = this.getUIContext().getHostContext() as Context;
          let filePath = context.cacheDir + '/test.txt'; // 获取文件路径
          let file =
            fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.APPEND | fs.OpenMode.CREATE); // 设置以追加方式打开文件
          let str = systemDateTime.getTime().toString() + ','; // 获取当前时间作为写入文件的内容
          let writeLen = fs.writeSync(file.fd, str); // 向文件内写入内容，返回值为写入内容的长度
          console.log(`writeLen：${writeLen}`);
          fs.closeSync(file); // 关闭文件
          this.message = fs.readTextSync(filePath); // 读取文件内容
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
