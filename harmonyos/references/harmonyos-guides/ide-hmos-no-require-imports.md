---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-require-imports
title: "@typescript-eslint/no-require-imports"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-require-imports
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:71beabf3fbc69f05b74546f80d34720d1e65852294b0db82341cb1861382313b
---

禁止使用“require()”语法导入依赖。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-require-imports": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
// lib1 lib2 lib3为ArkTS文件
import * as lib1 from './lib1';
import { lib2 } from './lib2';
import * as lib3 from './lib3';
```

## 反例

```ts
// lib3为ArkTS文件
import lib3 = require('./lib3');
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
