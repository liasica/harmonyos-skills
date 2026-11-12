---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_one-var-declaration-per-line
title: "@hw-stylistic/one-var-declaration-per-line"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/one-var-declaration-per-line
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:eab423cecda3c206f1de58a3a1ce0caa1b3af5cbcdc2d2818470e26bf239252d
---

变量声明时，要求一次仅声明一个变量。该规则仅检查.ets文件类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/one-var-declaration-per-line": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```screen
let a: string = 'hello';
let b: string = 'world';
a += 'my';
b += 'my';

const c: string = 'hello';
const d: string = 'world';

console.info(`a: ${a}, b: ${b}, c: ${c}, d: ${d}`);
```

## 反例

```screen
// Split 'const' declarations into multiple statements.
const a: string = 'hello', b: string = 'world';
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
