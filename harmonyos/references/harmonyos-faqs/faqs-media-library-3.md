---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-3
title: base64字符串如何转为图片并保存
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > base64字符串如何转为图片并保存
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:847656c6b8aa9252d06d8f8ed49270cc8b664dc88fdb3403ca5b1934742403c6
---

可以通过[buffer.from](../harmonyos-references/js-apis-buffer.md#bufferfrom)的方法，将base64编码格式的字符串创建为新的Buffer对象，接着用[fileIo.writeSync](../harmonyos-references/js-apis-fileio.md#fileiowritesync)方法将转换好的Buffer对象写入文件。

参考代码如下：

```
1. import { buffer } from '@kit.ArkTS';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';
4. import { fileUri } from "@kit.CoreFileKit";
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. // In the utility class, retrieve the Context from the Entry Ability and save it to AppStore, then use AppStore to retrieve it in the utility class
8. let context = AppStorage.get("context") as UIContext;
9. let filesDir = context.getHostContext()!.filesDir;

11. // Data is the base64 string that needs to be converted, and returns the sandbox path URI
12. export async function writeFile(data: string): Promise<string> {
13. let uri = ''
14. try {
15. let filePath = filesDir + "/1.png";
16. uri = fileUri.getUriFromPath(filePath);
17. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
18. console.info("file fd: " + file.fd);
19. const reg = new RegExp("data:image/\\w+;base64,")
20. const base64 = data.replace(reg, "");
21. console.log("base64flag", base64)
22. const dataBuffer = buffer.from(base64, 'base64')
23. let writeLen = fileIo.writeSync(file.fd, dataBuffer.buffer);
24. hilog.info(0xA0c0d0,'uri',uri)
25. fileIo.closeSync(file);
26. }
27. catch (Error) {
28. hilog.error(0xA0c0d0,'Error',Error.code)
29. }
30. return uri;
31. }
```

[Base64ImageConverter.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/MediaLibraryKit/entry/src/main/ets/pages/Base64ImageConverter.ets#L21-L51)
