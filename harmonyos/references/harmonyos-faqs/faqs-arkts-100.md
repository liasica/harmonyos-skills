---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-100
title: 如何对异步方法进行插桩/替换
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 如何对异步方法进行插桩/替换
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:26+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:a015a3ddb77503b91027fb13bc296338f87e82e0c5cc832f7a9218e28eebc95c
---

开发者可通过Aspect类封装提供切面能力的接口，用于对类方法进行前后插桩或替换实现，其中[addBefore()](../harmonyos-references/js-apis-util.md#addbefore11)方法可在指定的类对象的原方法执行前插入一个函数，[replace()](../harmonyos-references/js-apis-util.md#replace11)方法可将指定类的原方法替换为另一个函数。

参考如下示例：

```
1. import { util } from '@kit.ArkTS';

3. class Test1 {
4. static data: string = 'initData';

6. static async printData(arg: string) { // asynchronous method
7. console.log('execute original printData');
8. console.log('Test.data is' + Test1.data);
9. console.log('arg', arg);
10. return 0;
11. }
12. }

14. // Pile insertion
15. util.Aspect.addBefore(Test1, 'printData', true,
16. (classObj: Object, arg: string): void => {
17. console.log('execute before');
18. Reflect.set(classObj, 'data', 'dataChangedByBefore');
19. console.log('arg is ' + arg);
20. }
21. );

23. Test1.printData('m1').then((res) => {
24. console.log('res = ' + res.toString());
25. console.log('Test.data = ' + Test1.data);
26. });

28. class Test2 {
29. static data: string = 'initData';

31. static async printData(arg: string) { // asynchronous method
32. console.log('execute original printData');
33. console.log('Test.data is' + Test2.data);
34. console.log('arg', arg);
35. return 0;
36. }
37. }

39. // replace
40. util.Aspect.replace(Test2, 'printData', true,
41. // Replace with another asynchronous function
42. async (classObj: Object, arg: string): Promise<number> => {
43. console.log('execute instead');
44. Reflect.set(classObj, 'data', 'dataChangedByInstead');
45. console.log('arg is ' + arg);
46. return Promise.resolve(100);
47. });

49. Test2.printData('m1').then((res) => {
50. console.log('res = ' + res.toString());
51. console.log('Test.data = ' + Test2.data);
52. });
```

[AddBeforeAndReplace.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/AddBeforeAndReplace.ets#L21-L72)
