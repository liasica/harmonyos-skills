---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-regexp-exec
title: @typescript-eslint/prefer-regexp-exec
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-regexp-exec
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:47+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3def49cb3c7dc9aa9acc87f5dcbd3a8f39f59153e12f0e288fea68ee0f6b0212
---

如果未提供全局标志（/g），推荐使用“RegExp#exec”，而不是“String#match”。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/prefer-regexp-exec": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. /thing/.exec('something');

3. 'some things are just things'.match(/thing/g);

5. const text = 'something';
6. const search = /thing/;
7. search.exec(text);
```

## 反例

```
1. 'something'.match(/thing/);

3. 'some things are just things'.match(/thing/);

5. const text = 'something';
6. const search = /thing/;
7. text.match(search);
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
