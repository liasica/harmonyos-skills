---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-performance-no-closures
title: @performance/hp-performance-no-closures
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-performance-no-closures
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:12+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0270c96e6c20892a79b51a6230dc49ee1720fd3f0b5a72127f5a838b4f55dd60
---

建议函数内部变量尽量使用参数传递。

根据[ArkTS编程规范](arkts-high-performance-programming.md)，建议修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-performance-no-closures": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. let arr = [0, 1, 2];
2. function foo(array: Array<number>): number {
3. // arr 尽量通过参数传递
4. return array[0] + array[1];
5. }
6. foo(arr);
```

## 反例

```
1. let arr = [0, 1, 2];
2. function foo() {
3. // arr 尽量通过参数传递
4. return arr[0] + arr[1];
5. }
6. foo();
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
