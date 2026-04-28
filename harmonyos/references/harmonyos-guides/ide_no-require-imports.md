---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-require-imports
title: @typescript-eslint/no-require-imports
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-require-imports
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:38+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:f6c7dab7f534d6c7d991f57da2e6d9dc7e183618a18ef903fdeb6dfde63b8716
---

禁止使用“require()”语法导入依赖。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-require-imports": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // lib1 lib2 lib3为.js/.ts文件
2. import * as lib1 from './lib1';
3. import { lib2 } from './lib2';
4. import * as lib3 from './lib3';
```

## 反例

```
1. // lib3为.js/.ts文件
2. import lib3 = require('./lib3');
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
