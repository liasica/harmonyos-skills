---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-namespace-keyword
title: "@typescript-eslint/prefer-namespace-keyword"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-namespace-keyword
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5c53b27265c9ddb85e2b8f2202a3328358ea85035931b5a3e814f726a9c89860
---

推荐使用“namespace”关键字而不是“module”关键字来声明一个自定义的 TypeScript 模块。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-namespace-keyword": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export namespace Example {}
```

## 反例

```screen
export module Example {}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
