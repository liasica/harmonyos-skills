---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-92
title: 如何进行base64编码
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何进行base64编码
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b829ae770388d644892d0843705bc698e0c934abf99bae30cc378c508f0cf7d4
---

可使用util中的Base64Helper()方法进行base64编码，参考代码如下：

```
1. import { util } from '@kit.ArkTS';

3. @Entry
4. @Component
5. struct Base64Encode {
6. @State message: string = 'Base64 encoding';

8. build() {
9. Row() {
10. Column() {
11. Text(this.message)
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. .onClick(() => {
15. let base64 = new util.Base64Helper();
16. let arr = new Uint8Array([48, 49, 2, 1, 1, 4, 32, 115, 56]);
17. let base64Str = base64.encodeToStringSync(arr); // Uint8Array to base64
18. console.log('encodeToStringSync',base64Str);
19. // base64.decodeSync(''); // base64 to Uint8Array
20. // console.log('decodeSync',base64.decodeSync(''));
21. })
22. }
23. .width('100%')
24. }
25. .height('100%')
26. }
27. }
```

[Base64Encode.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/Base64Encode.ets#L21-L47)
