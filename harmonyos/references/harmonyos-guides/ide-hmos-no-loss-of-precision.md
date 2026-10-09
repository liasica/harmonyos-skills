---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-loss-of-precision
title: "@typescript-eslint/no-loss-of-precision"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-loss-of-precision
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e989a8e708140e1995fe4a13983f34bab3f62172f41582f5724d51293ac0e50b
---

禁止使用失去精度的字面数字。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-loss-of-precision": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
export const a = 12345;
export const b = 123.456;
export const c = 123e34;
export const d = 12300000000000000000000000;
export const e = 0x1FFFFFFFFFFFFF;
export const f = 9007199254740991;
export const g = 9007_1992547409_91;
```

## 反例

```ts
export const a = 9007199254740993;
export const b = 5123000000000000000000000000001;
export const c = 1230000000000000000000000.0;
export const d = .1230000000000000000000000;
export const e = 0X20000000000001;
export const f = 0X2_000000000_0001;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
