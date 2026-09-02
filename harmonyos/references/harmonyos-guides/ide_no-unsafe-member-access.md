---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-member-access
title: "@typescript-eslint/no-unsafe-member-access"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unsafe-member-access
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8c6b73af28abe60176d20ffa6c4c8d8947836b3c5b8a3720c70e262b4b1f1894
---

禁止成员访问“any”类型的值。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unsafe-member-access": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
declare const properlyTyped: { prop: { a: string } };

export const v1 = properlyTyped.prop.a;

const key = 'a';
export const v2 = properlyTyped.prop[key];

const arr = ['1', '2', '3'];
let idx = 1;
export const v3 = arr[idx];
export const v4 = arr[idx++];
```

## 反例

```screen
declare const properlyTyped: { prop: { a: any } };

export const v1 = properlyTyped.prop.a;

const key = 'a' as any;
export const v2 = properlyTyped.prop[key];

const arr = ['1', '2', '3'];
let idx: any = 1;
export const v3 = arr[idx];
export const v4 = arr[idx++];
```

## 规则集

```screen
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
