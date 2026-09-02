---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_triple-slash-reference
title: "@typescript-eslint/triple-slash-reference"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/triple-slash-reference
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:3edf88e7fae2e7bc1a62277c625a35250dc9be38ee3cc6e55a7a7170f1999e28
---

不允许某些三斜杠引用，推荐使用ES6风格的导入声明。

支持以下三种三斜杠引用方式的检查。

```screen
/// <reference lib="..." />
/// <reference path="..." /> 
/// <reference types="..." />
```

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/triple-slash-reference": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/triple-slash-reference选项](https://typescript-eslint.nodejs.cn/rules/triple-slash-reference/#options)。

## 正例

```screen
import { value } from 'code';
export { value };
```

## 反例

```screen
/// <reference path="code" />

globalThis.value;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
