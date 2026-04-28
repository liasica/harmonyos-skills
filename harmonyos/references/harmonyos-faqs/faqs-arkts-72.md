---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-72
title: 如何使用AOP接口实现重复插桩或替换
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何使用AOP接口实现重复插桩或替换
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:04+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:7706440169f4ab0f4b431718673184296672cf93ab4f3b745774f3d7c9c1bfcb
---

AOP提供的接口支持方法插桩或替换。

采用addBefore（方法调用前插桩）作为参考例子，重复插桩时，后插入的代码段先执行。

```
1. import { util } from '@kit.ArkTS';

3. class Test {
4. static data: string = "initData";

6. static printData(): void {
7. console.log("execute original printData");
8. }
9. }

11. @Entry
12. @Component
13. struct Index {
14. @State message: string = 'Hello World';

16. build() {
17. Row() {
18. Column() {
19. Text(this.message)
20. .fontSize(50)
21. .fontWeight(FontWeight.Bold)
22. .onClick(() => {
23. Test.printData();
24. util.Aspect.addBefore(Test, "printData", true, (classObj: Test) => {
25. console.log("execute before 1");
26. });
27. Test.printData();
28. util.Aspect.addBefore(Test, "printData", true, (classObj: Test) => {
29. console.log("execute before 2");
30. });
31. util.Aspect.addBefore(Test, "printData", true, (classObj: Test) => {
32. console.log("execute before 3");
33. });
34. Test.printData();
35. })
36. }
37. .width('100%')
38. }
39. .height('100%')
40. }
41. }
```

[AddBefore.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/AddBefore.ets#L21-L61)
