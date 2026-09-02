---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-20
title: 如何存储文件才不会跟随app卸载而删除
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何存储文件才不会跟随app卸载而删除
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e227ac991f6eca6a485c47dafe02ed74b68dbc4aa2427559876dec09c61bd5c7
---

**解决措施**

如果是用户文件，例如在应用内主动保存的文件，可以存储在媒体库公共目录/storage/media/100/local/files。公共目录下的文件不会在应用卸载时被删除。

**参考代码**

可以使用[@ohos.file.picker](../harmonyos-references/js-apis-file-picker.md)中提供的save方法在公共目录创建文件，方法可以参考以下代码：

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { picker, fileIo } from '@kit.CoreFileKit';

let uri: string = '';

// Save content to the public directory
export async function saveToUser(content: string) {
  try {
    let DocumentSaveOptions = new picker.DocumentSaveOptions();
    // New file name
    DocumentSaveOptions.newFileNames = ['test.txt'];
    let documentPicker = new picker.DocumentViewPicker();
    documentPicker.save(DocumentSaveOptions).then((DocumentSaveResult: Array<string>) => {
      console.info('DocumentViewPicker.save successfully, uri: ' + JSON.stringify(DocumentSaveResult));
      uri = DocumentSaveResult[0];
      // Write the content into the newly created file
      let file = fileIo.openSync(uri, fileIo.OpenMode.READ_WRITE);
      fileIo.writeSync(file.fd, content);
    }).catch((err: BusinessError) => {
      console.error('DocumentViewPicker.save failed with err: ' + JSON.stringify(err));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('DocumentViewPicker failed with err: ' + err.message);
  }
}
```
