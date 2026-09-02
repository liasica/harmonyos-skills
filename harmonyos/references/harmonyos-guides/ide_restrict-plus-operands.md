---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_restrict-plus-operands
title: "@typescript-eslint/restrict-plus-operands"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/restrict-plus-operands
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:fa2cd8f50918641ad49ad6904faa9c813a4ccfbd5c95721d35b2bf177d38deaa
---

要求加法的两个操作数都是相同的类型，并且是“bigint”、“number”或“string”。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/restrict-plus-operands": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/restrict-plus-operands选项](https://typescript-eslint.nodejs.cn/rules/restrict-plus-operands/#options)。

## 正例

```screen
const num = 10;
const bigIntNum = 1n;
export const foo1 = parseInt('5.5', num) + num;
export const foo2 = bigIntNum + bigIntNum;
```

## 反例

```screen
const num = 10;
const bigIntNum = 1n;
export const foo2 = bigIntNum + num;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
