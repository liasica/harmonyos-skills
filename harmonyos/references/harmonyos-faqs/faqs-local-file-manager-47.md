---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-47
title: 如何创建临时文件
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何创建临时文件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:31+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:0871eca68a1ac69a1e6a035f501f0529e2cc0b697cbe4f9bee80cecd9a2c5a99
---

可以参考如下示例：

```
1. import { fileIo, ReadOptions } from '@kit.CoreFileKit';
2. import { common } from '@kit.AbilityKit';
3. import { buffer } from '@kit.ArkTS';

5. @Entry
6. @Component
7. struct CreateFileDemo {
8. @State message: string = 'Hello World';
9. @State writeStr: string = 'write content';
10. @State readStr: string = 'read content';

12. build() {
13. Column() {
14. Text(this.message)
15. Button(this.writeStr)
16. .margin({ top: 15, bottom: 15 })
17. .onClick(() => {
18. let context = this.getUIContext().getHostContext();
19. let filesDir = context!.tempDir;
20. let file = fileIo.openSync(filesDir + 'test.txt', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
21. // Write a paragraph of content to a file
22. fileIo.writeSync(file.fd, 'Try to write str.');
23. console.info('str has been written');
24. // close file
25. fileIo.closeSync(file);
26. })
27. Button(this.readStr)
28. .onClick(() => {
29. let context = this.getUIContext().getHostContext();
30. let filesDir = context!.tempDir;
31. let file = fileIo.openSync(filesDir + 'test.txt', fileIo.OpenMode.READ_WRITE);
32. // Read a section of content from a file
33. let arrayBuffer = new ArrayBuffer(1024);
34. let readOptions: ReadOptions = {
35. offset: 0,
36. length: arrayBuffer.byteLength
37. };
38. let readLen = fileIo.readSync(file.fd, arrayBuffer, readOptions);
39. let buf = buffer.from(arrayBuffer, 0, readLen);
40. this.message = buf.toString();
41. // close file
42. fileIo.closeSync(file);
43. })
44. }
45. .height('100%')
46. .width('100%')
47. }
48. }
```

[CreateTempFile.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CoreFileKit/entry/src/main/ets/pages/CreateTempFile.ets#L21-L68)
