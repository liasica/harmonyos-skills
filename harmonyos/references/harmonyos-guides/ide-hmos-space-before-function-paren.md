---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-space-before-function-paren
title: "@typescript-eslint/space-before-function-paren"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/space-before-function-paren
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:9e3f174b5e63339492b1ddf2e9bcff51eb96cdac7c16ebdfb864dbdab25b1a65
---

强制在函数名和括号之间保持一致的空格风格。

**说明** 

* 该规则默认要求函数名和括号间有空格。如需修改请参考[选项](ide-hmos-space-before-function-paren.md#section182418564158)。
* 该规则建议在对.ts文件进行检查时使用。如需检查.ets文件，建议使用[@hw-stylistic/space-before-function-paren](ide-hmos-space-before-function-paren-stylistic.md)。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/space-before-function-paren": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/space-before-function-paren选项](https://eslint.nodejs.cn/docs/rules/space-before-function-paren#选项)。

## 正例

```ts
// 默认foo和(之间需要一个空格
export function foo () {
  // ...
}
```

## 反例

```ts
// 默认foo和(之间需要一个空格
export function foo() {
  // ...
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
