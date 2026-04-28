---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-28
title: 如何从一个二进制文件中读取其字节数组？通过fileIo.createStreamSync只能获取到ArrayBuffer，如何转成number[]
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何从一个二进制文件中读取其字节数组？通过fileIo.createStreamSync只能获取到ArrayBuffer，如何转成number[]
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:27+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:5ac39f89fce787d0210972ea692c33d5a6d42286c41c19e15e403e4678ab942d
---

```
1. @Component
2. export struct ArrayBufferConversionArray {
3. @State fileLength: number = 10;
4. private tempData: number[] = [];

6. aboutToAppear(): void {
7. // Convert ArrayBuffer to a number array
8. let arrayBuffer: ArrayBuffer = new ArrayBuffer(this.fileLength);
9. let dataView: DataView = new DataView(arrayBuffer);
10. for (let index = 0; index < this.fileLength; index++) {
11. this.tempData[index] = dataView.getInt8(index);
12. }
13. console.info(this.tempData.toString());
14. }

16. build() {
17. RelativeContainer() {
18. Text(this.tempData.toString())
19. .id('ArrayBufferHelloWorld')
20. .fontSize(50)
21. .fontWeight(FontWeight.Bold)
22. .alignRules({
23. center: { anchor: '__container__', align: VerticalAlign.Center },
24. middle: { anchor: '__container__', align: HorizontalAlign.Center }
25. })
26. }
27. .height('100%')
28. .width('100%')
29. }
30. }
```

[ReadByte.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/LocationKit/entry/src/main/ets/pages/ReadByte.ets#L21-L51)
