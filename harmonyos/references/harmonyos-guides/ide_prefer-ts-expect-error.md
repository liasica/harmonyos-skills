---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-ts-expect-error
title: @typescript-eslint/prefer-ts-expect-error
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-ts-expect-error
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:47+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0e1abbbdde299dbb749d34ecd5c30f2992b057d2e68d1cef55146bbb3c4a96e1
---

强制使用“@ts-expect-error”而不是“@ts-ignore”。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/prefer-ts-expect-error": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // @ts-expect-error: with description
2. export const str: string = 1;

4. /**
5. * Explaining comment
6. *
7. * @ts-expect-error: with description */
8. export const multiLine: number = 'value';

10. /** @ts-expect-error: with description */
11. export const block: string = 1;
```

## 反例

```
1. // @ts-ignore
2. const str: string = 1;

4. /**
5. * Explaining comment
6. *
7. * @ts-ignore */
8. const multiLine: number = 'value';

10. /** @ts-ignore */
11. const block: string = 1;

13. const isOptionEnabled = (key: string): boolean => {
14. // @ts-ignore: if key isn't in globalOptions it'll be undefined which is false
15. return !!globalOptions[key];
16. };
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
