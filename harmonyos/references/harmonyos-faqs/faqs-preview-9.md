---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-preview-9
title: 如何使用ohos.file.fs打开gbk编码文档
breadcrumb: FAQ > 应用服务开发 > 通用文件预览服务（Preview Kit） > 如何使用ohos.file.fs打开gbk编码文档
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:81885f93347338ee1992f3560f8d750b63ce37b62cc7dd66ab311912adc4ab9a
---

## 问题现象

开发过程中遇到有文档的编码类型不为utf-8，而ohos.file.fs中readTextSync，参数options-encoding仅支持utf-8，不支持其他编码类型，使用该方法打开文档会出现乱码。

## 背景知识

* [Core File Kit简介](../harmonyos-guides/core-file-kit-intro.md#core-file-kit概述)：Core File Kit（文件基础服务）为开发者提供一套访问和管理应用文件和用户文件的能力。帮助用户更高效地管理、查找和备份各类文件，使用户能够轻松应对各种文件管理的需求。
* [fs.readTextSync](../harmonyos-references/js-apis-file-fs.md#fileioreadtextsync)：以同步方法基于文本方式读取文件（即直接读取文件的文本内容）。
* [fs.openSync](../harmonyos-references/js-apis-file-fs.md#fileioopensync)：以同步方法打开文件或目录。支持使用URI打开文件。
* [fs.readSync](../harmonyos-references/js-apis-file-fs.md#fileioreadsync)：以同步方法从文件读取数据。
* [TextDecoder](../harmonyos-references/js-apis-util.md#textdecoder)：TextDecoder用于将字节数组解码为字符串。

## 解决方案

下方代码中readGbkStr方法为解决方案。

使用openSync方法打开文件后，使用readSync方法读取数据到Uint8Array，最后使用TextDecoder用于将字节数组解码为字符串。

```ts
import type { common } from '@kit.AbilityKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { util } from '@kit.ArkTS';

// demo展示使用utf8\gbk编码打开gbk编码文档的页面
// writeGbkStr方法用于生成gbk编码文档用于展示
// readGbkStr方法为使用gbk编码打开文档的实现

@Entry
@Component
struct Index {
  private ctx = this.getUIContext().getHostContext() as common.UIAbilityContext;
  // 写入文档的内容，用于展示
  private text = 'Text是文本组件，用于展示用户视图，如显示文章的文字内容。该组件支持绑定自定义文本选择菜单，用户可根据需要选择不同功能。';
  // 用于测试生成的临时文件名
  private fileName = 'test0.txt';
  // 文件地址请按实际填写
  private filesDir = this.ctx.filesDir + "/" + this.fileName;

  aboutToAppear(): void {
    writeGbkStr(this.filesDir, this.text);
  }

  build() {
    Column() {
      Text('read utf8:').fontWeight(600).fontSize(30).textAlign(TextAlign.Start).width("95%")
      Text(fs.readTextSync(this.filesDir)).textAlign(TextAlign.Start).width("95%")

      Text('read gbk:').fontWeight(600).fontSize(30).textAlign(TextAlign.Start).width("95%")
      Text(readGbkStr(this.filesDir)).textAlign(TextAlign.Start).width("95%")
    }
    .height("100%")
    .width("100%")
  }
}

// 生成gbk编码的文档
function writeGbkStr(filesDir: string, content: string) {
  let file = fs.openSync(filesDir, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
  try {
    let textEncoder = new util.TextEncoder('gbk');
    let buffer = new ArrayBuffer(118);
    let uint8 = new Uint8Array(buffer);
    textEncoder.encodeIntoUint8Array(content, uint8);
    fs.writeSync(file.fd, uint8.buffer);
  } finally {
    fs.close(file.fd);
  }
}

function readGbkStr(filesDir: string) {
  let file = fs.openSync(filesDir, fs.OpenMode.READ_ONLY);
  try {
    // 读取数据到Uint8Array
    let buf = new ArrayBuffer(118);
    fs.readSync(file.fd, buf);
    let decoder = util.TextDecoder.create('gbk');
    return decoder.decodeToString(new Uint8Array(buf));
  } finally {
    fs.close(file.fd);
  }
}
```
