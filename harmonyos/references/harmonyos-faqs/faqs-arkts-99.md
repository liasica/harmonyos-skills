---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-99
title: 如何通过AOP统计方法执行时间
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何通过AOP统计方法执行时间
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:11+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5ef988cc30669ddb314e60b46f328ba795d29ddc620e4eca753db6f01c018331
---

为了统计执行时间，可以使用addBefore记录开始时间，使用addAfter记录结束时间。

示例如下：

```
1. import { util } from '@kit.ArkTS';
2. import { systemDateTime } from '@kit.BasicServicesKit';

4. class Utils {
5. Add(len: number): number {
6. let num = 0;
7. for (let index = 1; index <= len; index++) {
8. num += index;
9. }
10. return num;
11. }
12. }

14. let startTime = 0; // Initialization start time
15. let endTime = 0; // Initialization end time

17. util.Aspect.addBefore(Utils, 'Add', false, () => {
18. startTime = systemDateTime.getTime(true); // Return the start time in nanoseconds
19. })

21. util.Aspect.addAfter(Utils, 'Add', false, () => {
22. endTime = systemDateTime.getTime(true); // Return the end time in nanoseconds
23. })

25. let utilsObj = new Utils();
26. utilsObj.Add(1000);

28. @Entry
29. @Component
30. struct Index {
31. build() {
32. Row() {
33. Column() {
34. Button('get execution time')
35. .onClick(() => {
36. console.log('startTime:', startTime);
37. console.log('endTime:', endTime);
38. console.log('endTime - startTime = ', endTime - startTime);
39. })
40. }
41. .width('100%')
42. }.height('100%')
43. }
44. }
```

[AopUtils.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/AopUtils.ets#L21-L64)
