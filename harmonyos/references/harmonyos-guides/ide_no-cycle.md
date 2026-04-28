---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-cycle
title: @security/no-cycle
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-cycle
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:53+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:06348416236299d3923a37f2263224e19ca8e993c38a683a2ebd6802cce2aa38
---

该规则禁止使用循环依赖。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-cycle": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // foo.ets
2. import {} from './bar';

4. // bar.ets
5. import {} from './index';
```

## 反例

```
1. // foo.ets
2. import {} from './bar';

4. // bar.ets
5. import {} from './foo';
```

说明

反例中foo.ets文件依赖了bar.ets文件，bar.ets文件同时依赖了foo.ets文件，造成了循环依赖。

## 规则集

```
1. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
