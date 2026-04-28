---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-magic-numbers
title: @typescript-eslint/no-magic-numbers
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-magic-numbers
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:36+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:e3ef5d87ea075b0391cc68273130561ea1550a211a4170a0f438bbabb9d0993a
---

禁止使用魔法数字。

“魔法数字”是在代码中多次出现但没有明确含义的数字，最好将它们替换为常量。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-magic-numbers": "warn"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-magic-numbers选项](https://typescript-eslint.nodejs.cn/rules/no-magic-numbers#选项)。

## 正例

```
1. const TAX = 0.25;
2. const dutyFreePrice = 100;
3. export const finalPrice = dutyFreePrice + dutyFreePrice * TAX;
```

## 反例

```
1. export const finalPrice = 100 + 100 * 0.25;

3. const data = ['foo', 'bar', 'baz'];
4. export const dataLast = data[2];
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
