---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-4
title: 如何解决文件的中文乱码问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何解决文件的中文乱码问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f29c59bb00053602a189b32ed4dcdd7e5a7c5b216dfea596518e36ceca15fdb9
---

读取文件内容的buffer数据后，通过TextDecoder对文件内容进行解码。

```ts
import { util } from '@kit.ArkTS';
import { fileIo } from '@kit.CoreFileKit';

// In the utility class, retrieve the Context from the Entry Ability and save it to AppStore, then use AppStore to retrieve it in the utility class
let context = AppStorage.get("context") as UIContext;
// Create a file to write Chinese characters
let filePath = context.getHostContext()!.filesDir + "/test0.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
// Write a paragraph of content to a file
let writeLen = fileIo.writeSync(file.fd, "Hello, world");
fileIo.closeSync(file);
console.info(`GarbledCnCharacters The length of str is: ${writeLen}`);
let stream = fileIo.createStreamSync(filePath, "r+");
let buffer = new ArrayBuffer(4096);
stream.readSync(buffer);
// Set the encoding format to "utf-8"
let textDecoder = util.TextDecoder.create('utf-8', { ignoreBOM: true });
// Retrieve the corresponding text after decoding the input
let readString = textDecoder.decodeToString(new Uint8Array(buffer), { stream: false });
console.info(`GarbledCnCharacters read content is:${readString}`);
```

**参考链接**

[TextDecoder](../harmonyos-references/js-apis-util.md#textdecoder)
