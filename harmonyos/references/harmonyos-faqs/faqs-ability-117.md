---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-117
title: HarmonyOS Next系统属于大端还是小端
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > HarmonyOS Next系统属于大端还是小端
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:53+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ea9f39569c79ea4bd8fe5b6b1aee5e1ca78e860004008a3952363e7b2b773a92
---

属于小端序，可以通过以下代码验证：

```
1. @Entry
2. @Component
3. struct IndexTest {
4. @State message: string = 'Hello World';

6. isLittleEndian(): boolean {
7. const buffer = new ArrayBuffer(2);
8. const uint8Array = new Uint8Array(buffer);
9. const uint16Array = new Uint16Array(buffer);
10. // Write 0xAA and 0xBB into the buffer
11. uint8Array[0] = 0xAA;
12. uint8Array[1] = 0xBB;
13. // If read in small order, 0xBBAA will be interpreted as 48042
14. // If read in big endian order, 0xAABB will be interpreted as 43707
15. return uint16Array[0] === 0xBBAA;
16. }

19. aboutToAppear() {
20. if (this.isLittleEndian()) {
21. console.log('Small end');
22. } else {
23. console.log('Big end');
24. }
25. }

28. build() {
29. RelativeContainer() {
30. Text(this.message)
31. .id('IndexTest')
32. .fontSize(50)
33. .fontWeight(FontWeight.Bold)
34. .alignRules({
35. center: { anchor: '__container__', align: VerticalAlign.Center },
36. middle: { anchor: '__container__', align: HorizontalAlign.Center }
37. })
38. }
39. .height('100%')
40. .width('100%')
41. }
42. }
```

[LittleEndianPage.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/LittleEndianPage.ets#L21-L62)
