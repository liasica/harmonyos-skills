---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-35
title: 如何将数据持续写入文件内
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何将数据持续写入文件内
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:29+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:d40fc6b4391356eef399c6cb23afae4f55ab2ccefaa58395f76a5203877338c7
---

fileIo.writeSync方法中的WriteOptions.offset表示期望的文件写入位置。可以通过[filelo.read](../harmonyos-references/js-apis-file-fs.md#fileioread)获取偏移量offset，然后在之前的数据位置继续写入数据。参考代码如下：

```
1. import { fileIo, WriteOptions } from '@kit.CoreFileKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Component
5. export struct ContinuousWrite {
6. @State message: string = 'Hello World';

8. aboutToAppear(): void {
9. let context = this.getUIContext().getHostContext(); // Sandbox Path
10. let filePath = context!.filesDir + '/test.txt';
11. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
12. let arrayBuffer = new ArrayBuffer(4096);
13. fileIo.read(file.fd, arrayBuffer).then((readLen: number) => {
14. console.info(readLen.toString());
15. let str: string = 'hello, world';
16. let options: WriteOptions = { offset: readLen };
17. let writeLen = fileIo.writeSync(file.fd, str, options);
18. console.info('write data to file succeed and size is:' + writeLen);
19. }).catch((err: BusinessError) => {
20. console.error('read file data failed with error message: ' + err.message + ', error code: ' + err.code);
21. }).finally(() => {
22. fileIo.closeSync(file);
23. });
24. }

26. build() {
27. RelativeContainer() {
28. Text(this.message)
29. .id('WriteHelloWorld')
30. .fontSize(50)
31. .fontWeight(FontWeight.Bold)
32. .alignRules({
33. center: { anchor: '__container__', align: VerticalAlign.Center },
34. middle: { anchor: '__container__', align: HorizontalAlign.Center }
35. })
36. }
37. .height('100%')
38. .width('100%')
39. }
40. }
```

[StreamDataToFile.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CoreFileKit/entry/src/main/ets/pages/StreamDataToFile.ets#L21-L61)
