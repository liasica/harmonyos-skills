---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-non-null-assertion
title: @typescript-eslint/no-non-null-assertion
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-non-null-assertion
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:37+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:e01c10f417fefbea721104f71dbf662e562614f3ee4c09abcf608596c4611e04
---

禁止以感叹号作为后缀的方式使用非空断言。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-non-null-assertion": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. interface Example {
2. property?: string;
3. }

5. declare const example: Example;
6. export const includesBaz = example.property?.includes('baz') ?? false;
```

## 反例

```
1. interface Example {
2. property?: string;
3. }

5. declare const example: Example;
6. // 禁止使用"example.property!"的方式来进行非空断言
7. export const includesBaz = example.property!.includes('baz');
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
