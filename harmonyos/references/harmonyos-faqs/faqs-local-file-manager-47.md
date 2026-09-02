---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-47
title: 如何创建临时文件
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何创建临时文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a0627ab5efc929f1df35167b51620fb15f5386bf63c2048be467bf312385e3ec
---

可以参考如下示例：

```ts
import { fileIo, ReadOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { buffer } from '@kit.ArkTS';

@Entry
@Component
struct CreateFileDemo {
  @State message: string = 'Hello World';
  @State writeStr: string = 'write content';
  @State readStr: string = 'read content';

  build() {
    Column() {
      Text(this.message)
      Button(this.writeStr)
        .margin({ top: 15, bottom: 15 })
        .onClick(() => {
          let context = this.getUIContext().getHostContext();
          let filesDir = context!.tempDir;
          let file = fileIo.openSync(filesDir + '/test.txt', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
          // Write a paragraph of content to a file
          fileIo.writeSync(file.fd, 'Try to write str.');
          console.info('str has been written');
          // close file
          fileIo.closeSync(file);
        })
      Button(this.readStr)
        .onClick(() => {
          let context = this.getUIContext().getHostContext();
          let filesDir = context!.tempDir;
          let file = fileIo.openSync(filesDir + '/test.txt', fileIo.OpenMode.READ_WRITE);
          // Read a section of content from a file
          let arrayBuffer = new ArrayBuffer(1024);
          let readOptions: ReadOptions = {
            offset: 0,
            length: arrayBuffer.byteLength
          };
          let readLen = fileIo.readSync(file.fd, arrayBuffer, readOptions);
          let buf = buffer.from(arrayBuffer, 0, readLen);
          this.message = buf.toString();
          // close file
          fileIo.closeSync(file);
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
