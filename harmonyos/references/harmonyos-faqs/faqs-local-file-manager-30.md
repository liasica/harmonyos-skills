---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-30
title: 如何获取到resources下rawfile 的文件
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何获取到resources下rawfile 的文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:69b1928c9b622fd9e5e9bd3520f979703a43cc75625e646083330259d0b6ee50
---

可以通过[@ohos.resourceManager (资源管理)](../harmonyos-references/js-apis-resource-manager.md)模块中的[getRawFileContent](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontent9)接口来获取resources/rawfile目录下对应的rawfile文件内容。参考代码如下：

```ts
import { fileIo } from '@kit.CoreFileKit';

@Component
export struct GetRawfile {
  @State message: string = 'Hello World';

  aboutToAppear(): void {
    this.getUIContext().getHostContext()?.resourceManager.getRawFileContent('test.txt', (_err, value) => {
      if (_err) {
        console.error('Failed to get raw file:', _err);
        return;
      }
      let fileBuffer: ArrayBufferLike = value.buffer;
      let context = this.getUIContext()
        .getHostContext(); // Obtain the application sandbox path for storing temporary files, and perform null checking
      let filePath = context!.filesDir + '/test.txt';
      console.info('testTag-filePath:' + filePath);
      let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
      let writeLen = fileIo.writeSync(file.fd, fileBuffer);
      console.info('testTag-write data to file succeed and size is:' + writeLen);
      fileIo.closeSync(file);
    });
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('RawfileHelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
