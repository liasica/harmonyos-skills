---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-constant-property-check-in-loops
title: @performance/constant-property-referencing-check-in-loops
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/constant-property-referencing-check-in-loops
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:01+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:1d572b0fa9a7ced3343d588fd0a093706dbf20b7201cf7fc0a000c67870365ea
---

在循环如需频繁访问某个常量，且该属性引用常量在循环中不会改变，建议提取到循环外部，减少属性访问的次数。

根据[ArkTS高性能编程实践](arkts-high-performance-programming.md)，建议修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/constant-property-referencing-check-in-loops": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. class Time {
2. static start: number = 0;
3. static info: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
4. }
5. function getNum(num: number): number {
6. /* Year has (12 * 29 =) 348 days at least */
7. let total: number = 348;
8. const info = Time.info[num- Time.start];
9. for (let index: number = 0x8000; index > 0x8; index >>= 1) {
10. if ((info & index) != 0) {
11. total++;
12. }
13. }
14. return total;
15. }
```

## 反例

```
1. class Time {
2. static start: number = 0;
3. static info: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
4. }
5. function getNum(num: number): number {
6. /* Year has (12 * 29 =) 348 days at least */
7. let total: number = 348;
8. for (let index: number = 0x8000; index > 0x8; index >>= 1) {
9. // warning
10. total += ((Time.info[num - Time.start] & index) !== 0) ? 1 : 0;
11. }
12. return total;
13. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
