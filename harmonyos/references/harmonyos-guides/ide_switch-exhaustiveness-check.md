---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_switch-exhaustiveness-check
title: @typescript-eslint/switch-exhaustiveness-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/switch-exhaustiveness-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:5d38c1d5b5bd82453d8cc6f4d9f9e5d587cc469a91037f8f618d7fedea2451cc
---

要求switch语句对于联合类型中值的判断是详尽无遗的。

当switch语句中的判断条件是字面量值的集合或者是一个枚举类型，如果case语句中缺少任何一个值的判断，并且没有default语句时，此规则会告警。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/switch-exhaustiveness-check": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/switch-exhaustiveness-check选项](https://typescript-eslint.nodejs.cn/rules/switch-exhaustiveness-check/#options)。

## 正例

```
1. type Day =
2. | 'Monday'
3. | 'Tuesday'
4. | 'Wednesday'
5. | 'Thursday'
6. | 'Friday'
7. | 'Saturday'
8. | 'Sunday';

10. declare const day1: Day;

12. let result = '0';

14. switch (day1) {
15. case 'Monday':
16. result = '1';
17. break;
18. case 'Tuesday':
19. result = '2';
20. break;
21. case 'Wednesday':
22. result = '3';
23. break;
24. case 'Thursday':
25. result = '4';
26. break;
27. case 'Friday':
28. result = '5';
29. break;
30. case 'Saturday':
31. result = '6';
32. break;
33. case 'Sunday':
34. result = '7';
35. break;
36. }

38. declare const day2: Day;

40. result = '0';

42. switch (day2) {
43. case 'Monday':
44. result = '1';
45. break;
46. default:
47. result = '42';
48. }
49. console.info(result);

51. enum Fruit {
52. apple = 'apple',
53. banana = 'banana',
54. cherry = 'cherry'
55. }

57. declare const fruit: Fruit;

59. switch (fruit) {
60. case Fruit.apple:
61. console.log('an apple');
62. break;

64. case Fruit.banana:
65. console.log('a banana');
66. break;

68. case Fruit.cherry:
69. console.log('a cherry');
70. break;
71. }
```

## 反例

```
1. type Day =
2. | 'Monday'
3. | 'Tuesday'
4. | 'Wednesday'
5. | 'Thursday'
6. | 'Friday'
7. | 'Saturday'
8. | 'Sunday';

10. declare const day: Day;
11. let result = '0';

13. switch (day) {
14. // 只处理了'Monday'，缺少其他值的判断，并且也没有default分支
15. case 'Monday':
16. result = '1';
17. break;
18. }
19. console.info(result);
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
