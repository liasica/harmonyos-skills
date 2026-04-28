---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-129
title: 对象反序列化时number类型丢失精度如何解决
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 对象反序列化时number类型丢失精度如何解决
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8237607451cedb899a21ac27f63b633b090e20ac60bb34f2277f58140ea07050
---

1. 通过[JSON.parse()](../harmonyos-references/js-apis-json.md#jsonparse)解析，可以通过传入options参数，指定options为bigIntMode: JSON.BigIntMode.PARSE\_AS\_BIGINT，来处理BigInt的模式。

   示例代码参考如下：

   ```
   1. import { JSON } from '@kit.ArkTS';

   3. let options: JSON.ParseOptions = {
   4. bigIntMode: JSON.BigIntMode.PARSE_AS_BIGINT,
   5. }
   6. let numberText = '{"largeNumber":1122333444455556666677777888889}';
   7. let numberObj = JSON.parse(numberText, (key: string, value: Object | undefined | null): Object | undefined | null => {
   8. if (key === "largeNumber") {
   9. return value;
   10. }
   11. return value;
   12. }, options) as Object;

   14. @Entry
   15. @Component
   16. struct BigIntDemo {
   17. @State str: string = 'bigint num';

   19. build() {
   20. Row() {
   21. Column() {
   22. Button(this.str)
   23. .onClick(() => {
   24. console.info((numberObj as object)?.["largeNumber"]); // 1122333444455556666677777888889
   25. })
   26. }
   27. .width('100%')
   28. }
   29. .height('100%')
   30. }
   31. }
   ```

   [NumberLosesAccuracy.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/NumberLosesAccuracy.ets#L21-L51)
2. 使用三方库[json-bigint](https://ohpm.openharmony.cn/#/cn/detail/@ohmos%2Fjson-bigint)处理。
