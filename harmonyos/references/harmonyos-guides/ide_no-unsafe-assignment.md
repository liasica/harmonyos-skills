---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-assignment
title: @typescript-eslint/no-unsafe-assignment
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unsafe-assignment
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:41+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:24c3c78956fa25dc3512b4006c0485170c60a0f98b00f8aefd4f46ac8cdda249
---

禁止将“any”类型的值赋值给变量和属性。

该规则仅支持对.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-unsafe-assignment": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. let [x] = ['1'];
2. [x] = ['1'] as [string];
3. console.info([x].toString());

5. // generic position examples
6. export const a1: Set<string> = new Set<string>();
7. export const a2: Map<string, string> = new Map<string, string>();
8. export const a3: Set<string[]> = new Set<string[]>();
9. export const a4: Set<Set<Set<string>>> = new Set<Set<Set<string>>>();
```

## 反例

```
1. let [x] = ['1'];
2. [x] = ['1'] as [any];
3. [x] = '1' as any;
4. console.info([x].toString());

6. // generic position examples
7. export const a1: Set<string> = new Set<any>();
8. export const a2: Map<string, string> = new Map<any, string>();
9. export const a3: Set<string[]> = new Set<any[]>();
10. export const a4: Set<Set<Set<string>>> = new Set<Set<Set<any>>>();
```

## 规则集

```
1. plugin:@typescript-eslint/recommended
2. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
