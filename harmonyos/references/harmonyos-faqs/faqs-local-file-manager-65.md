---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-65
title: 文件下载到本地后内容丢失
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 文件下载到本地后内容丢失
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:5724ce912a90d423af28eb5416d6cd96fb9ec46637281d181493201556d5209e
---

## 问题现象

文件内容下载到沙箱后，文件内容始终只有一部分。

## 背景知识

[文件管理](../harmonyos-references/js-apis-file-fs.md)：基础文件操作API，提供基础文件操作能力，包括文件基本管理、文件目录管理、文件信息统计、文件流式读写等常用功能。

[fs.createStreamSync](../harmonyos-references/js-apis-file-fs.md#fileiocreatestreamsync)：以同步方法基于文件路径创建文件流。需要配合Stream中的close()函数关闭文件流。

## 问题定位

问题代码如下：

```ts
/*文件保存到沙箱*/
try {
  request.downloadFile(this.context, {
    url: this.downloadUrl,
    filePath: this.filesDir + '/' + this.name
  }).then(async (downloadTask: request.DownloadTask) => {
    downloadTask.on('complete', async () => {
      console.info('download complete');
      let file =
        fs.openSync(this.filesDir + '/' + this.name, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
      let arrayBuffer = new ArrayBuffer(1024);
      let readLen = fs.readSync(file.fd, arrayBuffer);
      let buf = buffer.from(arrayBuffer, 0, readLen);
      console.info(`The content of file: ${buf.toString()}`);
      fs.closeSync(file);
      this.savePath(filePath, this.name, buf)
    })
  }).catch((err: BusinessError) => {
    console.error(`Invoke downloadTask failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Invoke downloadFile failed, code is ${err.code}, message is ${err.message}`);
}
```

文件能读取到内容，说明成功下载到沙箱里了。始终只有一部分很可能是文件较长，使用buffer时处理不当，导致只有开头部分的内容被存入了沙箱，因此着重排查这部分代码。

```ts
let arrayBuffer = new ArrayBuffer(1024);
let readLen = fs.readSync(file.fd, arrayBuffer);
let buf = buffer.from(arrayBuffer, 0, readLen);
```

很明显ArrayBuffer被写成了一个固定的值，也没有进行循环操作等处理，因此只有前1024位内容被存入了沙箱。

## 分析结论

下载时buffer值写成了固定值且无循环读取操作，只有开头的内容被存入沙箱。

## 修改建议

可以参考以下代码写法，在使用buffer时，将文件流存到一个buffer数组内，最后将这些buffer合并到一起，除了修正了原问题外，在文件较大时也可以避免单个bufSize过大导致的内容丢失等问题。

```ts
import fs from '@ohos.file.fs';
import { buffer } from '@kit.ArkTS';
import { BusinessError } from '@ohos.base';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  async readLocalFileWithStream() {
    try {
      let buffers: buffer.Buffer[] = [];
      let inputStream = fs.createStreamSync('文件沙箱路径', 'r+');
      let bufSize = 1024;
      let readSize = 0;
      let buf = new ArrayBuffer(bufSize);

      class Option {
        public offset: number = 0;
        public length: number = bufSize;
      }

      let option = new Option();
      option.offset = readSize;
      let readLen = await inputStream.read(buf, option);
      // 存入当前结果
      buffers.push(buffer.from(buf.slice(0, readLen)));
      readSize += readLen;
      while (readLen > 0) {
        option.offset = readSize;
        readLen = await inputStream.read(buf, option);
        buffers.push(buffer.from(buf.slice(0, readLen)));
        readSize += readLen;
      }
      inputStream.closeSync();
      // 合并内容
      let finalBuf: ArrayBuffer = buffer.concat(buffers).buffer;
      console.info(`final ArrayBuffer byteLength is ${finalBuf.byteLength}}`);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`readLocalFileWithStream failed, code is ${err.code},message is ${err.message}`);
    }
  }

  build() {
    RelativeContainer() {
      Text(this.message)
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
