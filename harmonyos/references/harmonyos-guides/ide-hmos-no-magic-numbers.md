---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-magic-numbers
title: "@typescript-eslint/no-magic-numbers"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-magic-numbers
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:690318a50e9762f17a7ea781415a8f80c897e6db0bc49076c0e974047618c53e
---

禁止使用魔法数字。

“魔法数字”是在代码中多次出现但没有明确含义的数字，最好将它们替换为常量。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-magic-numbers": "warn"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-magic-numbers选项](https://typescript-eslint.nodejs.cn/rules/no-magic-numbers#选项)。

## 正例

```ts
const TAX = 0.25;
const dutyFreePrice = 100;
export const finalPrice = dutyFreePrice + dutyFreePrice * TAX;
```

## 反例

```ts
export const finalPrice = 100 + 100 * 0.25;

const data = ['foo', 'bar', 'baz'];
export const dataLast = data[2];
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
