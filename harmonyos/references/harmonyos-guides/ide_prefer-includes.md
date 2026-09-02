---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-includes
title: "@typescript-eslint/prefer-includes"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-includes
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ae67b47f0f11406be0ac384f2516e0c93cdf35555327a68af1bafd6b50a0a54d
---

强制使用“includes”方法而不是“indexOf”方法。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-includes": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
const str: string = 'hello';
const array: string[] = ['hello'];
const readonlyArray: readonly string[] = ['hello'];

str.includes('h');
array.includes('h');
readonlyArray.includes('h');
```

## 反例

```screen
const str: string = 'hello';
const array: string[] = ['hello'];
const readonlyArray: readonly string[] = ['hello'];

const num = -1;
let vv = str.indexOf('h') !== num;
vv = vv && array.indexOf('h') !== num;
vv = vv && readonlyArray.indexOf('h') !== num;
export { vv };
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
