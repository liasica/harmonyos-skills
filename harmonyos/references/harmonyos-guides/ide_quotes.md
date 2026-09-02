---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_quotes
title: "@typescript-eslint/quotes"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/quotes
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:22+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:001fcea6a6529f261c2774343fc5039f77fc6b378549efd10a60d05896360c3e
---

强制使用一致的反引号、双引号或单引号风格。

**说明** 

* 该规则默认检查字符串是否正确使用双引号。如需修改请参考[选项](ide_quotes.md#section182418564158)。
* 该规则建议在对.ts文件进行检查时使用。如需检查.ets文件，建议使用[@hw-stylistic/quotes](ide-quotes-stylistic.md)。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/quotes": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/quotes选项](https://eslint.nodejs.cn/docs/latest/rules/quotes#选项)。

## 正例

```screen
export const double = "double";
export const foo = `back
tick`;  // backticks are allowed due to newline
```

## 反例

```screen
// 默认推荐使用双引号
export const single = 'single';
export const unescaped = 'a string containing "double" quotes';
export const backtick = `back\ntick`; // you can use \n in single or double quoted strings
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
