---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-61
title: 如何合并两个对象
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何合并两个对象
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:03+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:057cbf562ebf4438192565f5f5c207a145d3201f31a56ddb1eeb7502ba93b9da
---

出于性能考虑，ArkTS限制了ES6的Object.assign()方法。若需在ArkTS文件中扩展对象属性或合并两个对象，可以自行实现assign方法。

1. 自定义assign方法

```
1. function assign(target: Record<string, Object>, ...source: Object[]): Record<string, Object> {
2. for (const items of source) {
3. for (const key of Object.keys(items)) {
4. target[key] = Reflect.get(items, key)
5. }
6. }
7. return target;
8. }
```

[Assign.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/Assign.ets#L21-L28)

2. 使用assign方法

```
1. interface IMergeSub {
2. testString: string,
3. testObject?: IMergeSub,
4. testArray?: Array<number>
5. }

8. interface IMerge {
9. a: IMergeSub,
10. b: IMergeSub[],
11. c: string[],
12. d: number
13. }

16. export function testAssign() {
17. let objectOne: IMerge =
18. {
19. a: {
20. testString: 'objectOne-a-testString',
21. testObject: {
22. testString: 'objectOne-a-testObject-testString'
23. },
24. testArray: [1]
25. },
26. b: [{
27. testString: 'objectOne-b-testString',
28. testObject: {
29. testString: 'objectOne-b-testObject-testString'
30. },
31. testArray: [2]
32. }],
33. c: ['objectOne-c'],
34. d: 3
35. }

38. let objectTwo: Record<string, Object> = {
39. 'a': 'objectTwo-a',
40. 'c': ['objectTwo-c'],
41. 'e': 1
42. }

45. let objectThree: Record<string, Object> = {
46. 'f': ['objectThree-f']
47. }

50. // Merge multiple objects, and the properties of both Object One and Object Two will be attached to Object Three. When the property names are the same, the properties of the object with the lower index will overwrite the properties of the previous object
51. const multiObjectMerged = assign(objectThree, objectTwo, objectOne);
52. console.log('multiObjectMerged is:' + JSON.stringify(multiObjectMerged));
53. console.log('objectThree is:' + JSON.stringify(objectThree));

56. // Merge the properties of Object One into Object Two, and the value of Object Two will change. When the property names are the same, Object One will overwrite the properties of Object Two
57. const objectMerged = assign(objectTwo, objectOne);
58. console.log('objectTwo is:' + JSON.stringify(objectTwo));
59. console.log('objectMerged is:' + JSON.stringify(objectMerged));
60. }
```

[Assign.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/Assign.ets#L32-L91)
