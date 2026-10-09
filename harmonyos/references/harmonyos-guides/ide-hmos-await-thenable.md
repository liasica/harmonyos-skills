---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-await-thenable
title: "@typescript-eslint/await-thenable"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/await-thenable
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c0630483ec4b5fc11128e473f73ae7c96ebd5bdd23786c574a08b8e136404b22
---

不允许对不是“Thenable”对象的值使用await关键字（“Thenable”表示某个对象拥有“then”方法，比如Promise）。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/await-thenable": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
async function test() {
  await Promise.resolve('value');
}

export { test };
```

## 反例

```ts
async function test() {
  await 'value';
}

export { test };
```

## 规则集

```screen
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[代码Code Linter检查](ide-hmos-code-linter.md)。
