---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-lines-between-class-members
title: "@typescript-eslint/lines-between-class-members"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/lines-between-class-members
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:864460aebceca6a51fa843f66fa789be5c2704bf6ed6a2c679b031b2761f79d2
---

禁止或者要求类成员之间有空行分隔。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/lines-between-class-members": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/lines-between-class-members选项](https://typescript-eslint.nodejs.cn/rules/lines-between-class-members/#options)。

## 正例

```ts
// 默认要求类成员之间有空行分隔
export class Foo {
  public baz() {
    console.info('baz');
  }

  public qux() {
    console.info('qux');
  }
}
```

## 反例

```ts
// 默认要求类成员之间有空行分隔
export class Foo {
  public baz() {
    console.info('baz');
  }
  public qux() {
    console.info('qux');
  }
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
