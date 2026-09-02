---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_semi
title: "@typescript-eslint/semi"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/semi
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:1219603d2c1632024e01efcafdec2b7d37d73841774a28c7256cea73e11a88b9
---

要求或不允许使用分号。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/semi": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/semi选项](https://eslint.nodejs.cn/docs/rules/semi#选项)。

## 正例

```screen
export const name = 'ESLint';

export class Foo {
  public bar = '1';
}
```

## 反例

```screen
// 默认在语句末尾需要加分号
export const name = 'ESLint'

export class Foo {
  // 默认在语句末尾需要加分号
  public bar = '1'
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
