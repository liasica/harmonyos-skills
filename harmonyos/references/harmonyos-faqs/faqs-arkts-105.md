---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-105
title: 如何通过判断函数入参类型实现不同代码逻辑
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何通过判断函数入参类型实现不同代码逻辑
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:12+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ce64c601f2f4843cc53992a820e94857e56708b47e938110c61fb6666470f48f
---

可参考如下示例：

```
1. class Game {
2. }

5. function solve(message: number | string | boolean | Map<string, number> | Record<string, number> | Game) {
6. // Game：Type judgment
7. if (message instanceof Game) {
8. console.info('Game');
9. return;
10. }

13. // Retrieve the constructor corresponding to the parameter and convert it to a string, then extract the string
14. let typeStr: string = message.constructor.toString().substring(9, 12);
15. // Determine the type corresponding to typeStr
16. switch (typeStr) {
17. case 'Num':
18. console.info('number type');
19. break;
20. case 'Str':
21. console.info('string type');
22. break;
23. case 'Boo':
24. console.info('boolean type');
25. break;
26. case 'Map':
27. console.info('Map type');
28. break;
29. case 'Obj':
30. console.info('Record type');
31. break;
32. }
33. }

36. let gameVal: Game = '';
37. let mapVal = new Map<string, number>();
38. mapVal.set('width', 100);
39. mapVal.set('height', 100);
40. let recordVal: Record<string, number> = { 'wight': 100, 'score': 100 };

43. @Entry
44. @Component
45. struct ParamsType {
46. build() {
47. Row() {
48. Column() {
49. Button('get params type')
50. .onClick(() => {
51. solve(100);
52. solve('100');
53. solve(true);
54. solve(mapVal);
55. solve(recordVal);
56. solve(gameVal);
57. })
58. }
59. .width('100%')
60. }
61. .height('100%')
62. }
63. }
```

[ParamsType.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/ParamsType.ets#L21-L83)
