---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-3
title: base64字符串如何转为图片并保存
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > base64字符串如何转为图片并保存
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fc43e2c818673c959f4def1d2aac1e20c0a9daf5b2e36424287754d5b634cd9f
---

可以通过[buffer.from](../harmonyos-references/js-apis-buffer.md#bufferfrom)的方法，将base64编码格式的字符串创建为新的Buffer对象，接着用[fileIo.writeSync](../harmonyos-references/js-apis-fileio.md#fileiowritesync)方法将转换好的Buffer对象写入文件。

参考代码如下：

```ts
import { buffer } from '@kit.ArkTS';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { fileUri } from "@kit.CoreFileKit";
import { hilog } from '@kit.PerformanceAnalysisKit';

// In the utility class, retrieve the Context from the Entry Ability and save it to AppStore, then use AppStore to retrieve it in the utility class
let context = AppStorage.get("context") as UIContext;
let filesDir = context.getHostContext()!.filesDir;

// Data is the base64 string that needs to be converted, and returns the sandbox path URI
export async function writeFile(data: string): Promise<string> {
  let uri = ''
  try {
    let filePath = filesDir + "/1.png";
    uri = fileUri.getUriFromPath(filePath);
    let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    console.info("file fd: " + file.fd);
    const reg = new RegExp("data:image/\\w+;base64,")
    const base64 = data.replace(reg, "");
    console.log("base64flag", base64)
    const dataBuffer = buffer.from(base64, 'base64')
    let writeLen = fileIo.writeSync(file.fd, dataBuffer.buffer);
    hilog.info(0xA0c0d0,'uri',uri)
    fileIo.closeSync(file);
  }
  catch (Error) {
    hilog.error(0xA0c0d0,'Error',Error.code)
  }
  return uri;
}
```
