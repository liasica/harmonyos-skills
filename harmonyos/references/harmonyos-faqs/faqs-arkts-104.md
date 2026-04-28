---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-104
title: 如何处理大整数
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何处理大整数
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:927fd92cc8e8d675c10414e901ea4a6461dc95b4fdcb5d8245a3666afb53fbf6
---

使用BigInt来处理大整数。

BigInt可以表示任意大小的整数。使用BigInt时，在整数字面量后面添加n后缀或使用BigInt()构造函数。

示例如下：

```
1. @Entry
2. @Component
3. struct BigIntNum {
4. build() {
5. Row() {
6. Column() {
7. Button('BigInt num')
8. .onClick(() => {
9. let bigIntNum: bigint = 12345678901234567890n; // Add n suffix after integer
10. let anotherBigInt: bigint = BigInt(9007199254740992); // Use BigInt() constructor
11. let sumBigInt: bigint = bigIntNum + anotherBigInt;
12. console.info('bigIntNum:' + bigIntNum);
13. console.info('anotherBigInt:' + anotherBigInt);
14. console.info('bigIntNum + anotherBigInt:' + sumBigInt);
15. })
16. }
17. .width('100%')
18. }
19. .height('100%')
20. }
21. }
```

[BigIntNum.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/BigIntNum.ets#L21-L41)
