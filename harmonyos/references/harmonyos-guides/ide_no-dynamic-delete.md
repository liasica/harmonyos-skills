---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-dynamic-delete
title: @typescript-eslint/no-dynamic-delete
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-dynamic-delete
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:30+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:2176c3d73c46384300cea605fbfa166792f20747de9f28cce3a8d221b77338ec
---

不允许在computed key表达式上使用“delete”运算符。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-dynamic-delete": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. const container: Record<string, number> = {
2. /* ... */
3. };

5. // Constant runtime lookups by string index
6. delete container.aaa;

8. // Constants that must be accessed by []
9. delete container['7'];
10. // '-Infinity' is number.
11. delete container['-Infinity'];
```

## 反例

```
1. const container: Record<string, number> = {
2. /* ... */
3. };

5. // Can be replaced with the constant equivalents, such as container.aaa
6. delete container['aaa'];
7. // 'Infinity' may be a string constant
8. delete container['Infinity'];

10. // Dynamic, difficult-to-reason-about lookups
11. const name = 'name';
12. delete container[name];
13. delete container[name.toUpperCase()];
```

## 规则集

```
1. plugin:@typescript-eslint/recommended
2. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
