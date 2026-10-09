---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-prefer-includes
title: "@typescript-eslint/prefer-includes"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-includes
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:908162801672a8a9d89643efc85faf2e62f3c3b758f3882aef8a35b86b664686
---

强制使用“includes”方法而不是“indexOf”方法。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-includes": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
const str: string = 'hello';
const array: string[] = ['hello'];
const readonlyArray: readonly string[] = ['hello'];

str.includes('h');
array.includes('h');
readonlyArray.includes('h');
```

## 反例

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
