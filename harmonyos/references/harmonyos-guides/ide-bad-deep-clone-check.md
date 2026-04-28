---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-bad-deep-clone-check
title: @performance/bad-deep-clone-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:01+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:8581ee04c6f2b9ca642045ca0257129b400570ec3ebb0d114800e1b1c778fc3a
---

避免使用不合理深拷贝，如JSON.parse(JSON.stringify(foo))和\_.cloneDeep(foo)。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/bad-deep-clone-check": "warn",
5. }
6. }
```

## 选项

```
1. "@performance/bad-deep-clone-check": [
2. 1,
3. {
4. "functions": [
5. "utils.clone"
6. ]
7. }
8. ]
```

## 正例

说明

正例的深拷贝实现仅作为示例，开发者需根据业务实际情况确认是否使用该实现。

* 该示例实现不支持函数和文档对象模型（Document Object Model）元素的拷贝。函数通常不需要深拷贝。
* 对于复杂的对象结构，使用该示例性能可能受到影响。
* 对于大型的自定义对象结构，可以使用结构化克隆算法（Structured Clone）或Web Worker。

```
1. // deepClone.ts
2. type Cloneable = object | Array<any> | Map<any, any> | Set<any> | Date | RegExp;

4. export function deepClone<T extends Cloneable>(source: T, weakMap = new WeakMap()): T {
5. // 处理原始类型和函数
6. if (typeof source !== 'object' || source === null) {
7. return source;
8. }
9. // 处理循环引用
10. if (weakMap.has(source)) {
11. return weakMap.get(source);
12. }
13. // 处理特殊对象类型
14. if (source instanceof Date) {
15. return new Date(source) as T;
16. }
17. if (source instanceof RegExp) {
18. return new RegExp(source.source, source.flags) as T;
19. }
20. // 处理数组
21. if (Array.isArray(source)) {
22. const cloneArr: any[] = [];
23. weakMap.set(source, cloneArr);
24. for (const item of source) {
25. cloneArr.push(deepClone(item, weakMap));
26. }
27. return cloneArr as T;
28. }
29. // 处理Map
30. if (source instanceof Map) {
31. const cloneMap = new Map();
32. weakMap.set(source, cloneMap);
33. for (const [key, value] of source) {
34. cloneMap.set(deepClone(key, weakMap), deepClone(value, weakMap));
35. }
36. return cloneMap as T;
37. }
38. // 处理Set
39. if (source instanceof Set) {
40. const cloneSet = new Set();
41. weakMap.set(source, cloneSet);
42. for (const value of source) {
43. cloneSet.add(deepClone(value, weakMap));
44. }
45. return cloneSet as T;
46. }
47. // 处理普通对象
48. const cloneObj = Object.create(Object.getPrototypeOf(source));
49. weakMap.set(source, cloneObj);
50. // 使用Object.getOwnPropertyDescriptors获取所有属性描述符
51. const descriptors = Object.getOwnPropertyDescriptors(source);

53. for (const [key, descriptor] of Object.entries(descriptors)) {
54. if (descriptor.value !== undefined) {
55. descriptor.value = deepClone(descriptor.value, weakMap);
56. }
57. Object.defineProperty(cloneObj, key, descriptor);
58. }
59. // 处理Symbol属性
60. const symbolKeys = Object.getOwnPropertySymbols(source);
61. for (const key of symbolKeys) {
62. cloneObj[key] = deepClone(source[key as any], weakMap);
63. }
64. return cloneObj;
65. }
```

```
1. //example.ts
2. import { deepClone } from './deepClone';

4. // 使用示例
5. const obj = {
6. a: 1,
7. b: [2, 3],
8. c: { d: 4 },
9. e: new Date(),
10. f: new Map([['key', 'value']]),
11. g: new Set([1, 2, 3]),
12. h: /regexp/gim
13. };
14. const cloned = deepClone(obj);
```

## 反例

```
1. import _ from 'lodash';
2. /**
3. * 下载lodash依赖：
4. * 1、ohpm install lodash
5. * 2、ohpm install @types/lodash --save-dev
6. */
7. interface Foo {
8. id: number;
9. name: string;
10. }
11. const foo:Foo = {
12. id:1,
13. name:"aa"
14. }
15. const clone1:Foo = JSON.parse(JSON.stringify(foo)) as Foo;
16. const clone2:Foo = _.cloneDeep(foo);
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
