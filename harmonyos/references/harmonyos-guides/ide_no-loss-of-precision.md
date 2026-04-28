---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-loss-of-precision
title: @typescript-eslint/no-loss-of-precision
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-loss-of-precision
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:35+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:08e3b9461d5bb7d5135d76edfdcac2f0292b0b690d6405fa896cde05ca3dbd05
---

禁止使用失去精度的字面数字。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-loss-of-precision": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export const a = 12345;
2. export const b = 123.456;
3. export const c = 123e34;
4. export const d = 12300000000000000000000000;
5. export const e = 0x1FFFFFFFFFFFFF;
6. export const f = 9007199254740991;
7. export const g = 9007_1992547409_91;
```

## 反例

```
1. export const a = 9007199254740993;
2. export const b = 5123000000000000000000000000001;
3. export const c = 1230000000000000000000000.0;
4. export const d = .1230000000000000000000000;
5. export const e = 0X20000000000001;
6. export const f = 0X2_000000000_0001;
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
