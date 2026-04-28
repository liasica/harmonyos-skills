---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-128
title: 如何指定对象某些属性参与序列化
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何指定对象某些属性参与序列化
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:15+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:3bb3c7ef8a0bd2feaa66eefdb79e7e1495f509a4f27242f9dd6c089dbf5add29
---

可以通过[JSON.stringify()](../harmonyos-references/js-apis-json.md#jsonstringify)方法实现，stringify(value: Object, replacer?: (number | string)[] | null, space?: string | number): string中，当replacer为数组时，只有包含在这个数组中的属性名才会被序列化到最终的JSON字符串中；当参数为null或者未提供时，则对象所有的属性都会被序列化。

示例代码参考如下：

```
1. import { JSON } from '@kit.ArkTS';

3. interface Person {
4. name: string;
5. age: number;
6. city: string;
7. }

9. let obj: Person = { name: 'John', age: 30, city: 'ChongQing' };

11. @Entry
12. @Component
13. struct JSONDemo {
14. @State str: string = 'to json';

16. build() {
17. Row() {
18. Column() {
19. Button(this.str)
20. .onClick(() => {
21. let jsonStr1 = JSON.stringify(obj); // All attributes are serialized
22. console.info('jsonStr1：', jsonStr1); // jsonStr1： {"name":"John","age":30,"city":"ChongQing"}
23. let jsonStr2 = JSON.stringify(obj, ['name']); // Specify the name attribute and serialize it
24. console.info('jsonStr2：', jsonStr2); // jsonStr2： {"name":"John"}
25. })
26. }
27. .width('100%')
28. }
29. .height('100%')
30. }
31. }
```

[SpecifyCertainProperties.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/SpecifyCertainProperties.ets#L21-L51)
