---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_await-thenable
title: "@typescript-eslint/await-thenable"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/await-thenable
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:55fbebcd9e827f4ad070a99b6702fedd519616b3dc39cebe2eea789688309ab4
---

不允许对不是“Thenable”对象的值使用await关键字（“Thenable”表示某个对象拥有“then”方法，比如Promise）。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/await-thenable": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
async function test() {
  await Promise.resolve('value');
}

export { test };
```

## 反例

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
