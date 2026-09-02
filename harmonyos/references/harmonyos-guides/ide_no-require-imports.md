---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-require-imports
title: "@typescript-eslint/no-require-imports"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-require-imports
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:37d064943f4288a5f4adef564fea391e2fa7f618dc8860643fb1df0714653084
---

禁止使用“require()”语法导入依赖。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-require-imports": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// lib1 lib2 lib3为.js/.ts文件
import * as lib1 from './lib1';
import { lib2 } from './lib2';
import * as lib3 from './lib3';
```

## 反例

```screen
// lib3为.js/.ts文件
import lib3 = require('./lib3');
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
