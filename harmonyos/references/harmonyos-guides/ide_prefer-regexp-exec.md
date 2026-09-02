---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-regexp-exec
title: "@typescript-eslint/prefer-regexp-exec"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-regexp-exec
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cde71d9ec3ed7a064489afb0b578744eb6d9a24879def29d25feda50d519e126
---

如果未提供全局标志（/g），推荐使用“RegExp#exec”，而不是“String#match”。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-regexp-exec": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
/thing/.exec('something');

'some things are just things'.match(/thing/g);

const text = 'something';
const search = /thing/;
search.exec(text);
```

## 反例

```screen
'something'.match(/thing/);

'some things are just things'.match(/thing/);

const text = 'something';
const search = /thing/;
text.match(search);
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
