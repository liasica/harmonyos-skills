---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-explicit-any
title: "@typescript-eslint/no-explicit-any"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-explicit-any
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:bc6da51faa20bfa6bcbd2e59991ae3965b85c8345069d1377badc196b8df7a47
---

不允许使用“any”类型。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-explicit-any": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-explicit-any选项](https://typescript-eslint.nodejs.cn/rules/no-explicit-any#options)。

## 正例

```screen
export const age1 = 17;
export const age2 = [age1];
export const age3 = [age1];

export function greet1(): string {
  return 'greet';
}

export function greet2(): string[] {
  return ['greet'];
}

export function greet4(): string[][] {
  return [['greet']];
}

export function greet5(param: readonly string[]): string {
  return param[age1];
}

export function greet6(param: readonly string[]): string[] {
  return [...param];
}
```

## 反例

```screen
export const age1: any = 17;
export const age2: any = [age1];
export const age3: any = [age1];

export function greet1(): any {
  return 'greet';
}

export function greet2(): any[] {
  return ['greet'];
}

export function greet4(): any[][] {
  return [['greet']];
}

export function greet5(param: readonly any[]): any {
  return param[age1];
}

export function greet6(param: readonly any[]): any[] {
  return [...param];
}
```

## 规则集

```screen
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
