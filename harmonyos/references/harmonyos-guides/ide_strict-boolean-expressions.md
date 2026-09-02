---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_strict-boolean-expressions
title: "@typescript-eslint/strict-boolean-expressions"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/strict-boolean-expressions
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:4d98cc93e4f0deba616fd98f38e5ccb412e83e51216ad8a111e7dca8f3651161
---

不允许在布尔表达式中使用非布尔类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/strict-boolean-expressions": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/strict-boolean-expressions选项](https://typescript-eslint.nodejs.cn/rules/strict-boolean-expressions/#options)。

## 正例

```screen
// nullable values should be checked explicitly against null or undefined
function getNum(): number | undefined {
  return undefined;
}

const num: number | undefined = getNum();
if (num !== undefined) {
  console.log('num is defined');
}

function getStr(): string | null {
  return 'null';
}

const str: string | null = getStr();
if (str !== null) {
  console.log('str is not empty');
}
```

## 反例

```screen
// nullable values should be checked explicitly against null or undefined
function getNum(): number | undefined {
  return undefined;
}

const num: number | undefined = getNum();
if (num) {
  console.log('num is defined');
}

function getStr(): string | null {
  return 'null';
}

const str: string | null = getStr();
if (str) {
  console.log('str is not empty');
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
