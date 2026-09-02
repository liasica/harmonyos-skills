---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-5
title: 如何修改沙箱路径下json文件的指定内容
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何修改沙箱路径下json文件的指定内容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b8d85911d52d57152bbf9d35db2c38b52a71fc2c5363b0a938d313c903614d51
---

可以通过以下步骤来完成：

```ts
import { fileIo } from '@kit.CoreFileKit';

// In the utility class, retrieve the Context from the Entry Ability and save it to AppStore, then use AppStore to retrieve it in the utility class
let context = AppStorage.get("context") as UIContext;
let filePath = context.getHostContext()!.filesDir + '/people.json';

class Student {
  name: string = 'zhangsan';
  age: number = 10;
}

let student = new Student();
// 1 Create a file and write its contents
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
fileIo.writeSync(file.fd, JSON.stringify(student))
fileIo.close(file);
// 2 Read the contents of the JSON file through fileIo.readSync.
let data = fileIo.readTextSync(filePath);
let obj: Student = JSON.parse(data);
// 3 Change the specified content name to lisi
obj.name = 'lisi';
// 4 Rewrite JSON file
let fileModify = fileIo.openSync(filePath, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.TRUNC);
fileIo.writeSync(fileModify.fd, JSON.stringify(obj));
fileIo.close(fileModify);
// 5 Read the latest content
let content = fileIo.readTextSync(filePath);
console.info(`ModifySanFileContent content is :${content}`);
```

**参考链接**

[文件管理](../harmonyos-references/js-apis-file-fs.md)
