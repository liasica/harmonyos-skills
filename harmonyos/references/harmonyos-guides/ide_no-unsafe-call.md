---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-call
title: @typescript-eslint/no-unsafe-call
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unsafe-call
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:41+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a8e13757422342bc17e5e8510872147537ca05ef208494a56d916c90935d21b1
---

禁止调用“any”类型的表达式。

该规则仅支持对.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-unsafe-call": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. declare const typedVar: () => void;
2. declare const typedNested: { prop: { a: () => void } };

4. typedVar();
5. typedNested.prop.a();

7. ((): void => {
8. console.info('hello');
9. })();

11. new Map();

13. export const raw = String.raw`foo`;
```

## 反例

```
1. declare const anyVar: any;
2. declare const nestedAny: { prop: any };
3. // anyVar为any类型，禁止调用
4. anyVar();
5. anyVar.a.b();
6. // nestedAny中的prop属性为any类型，禁止调用
7. nestedAny.prop();
```

## 规则集

```
1. plugin:@typescript-eslint/recommended
2. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
