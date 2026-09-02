---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_lines-between-class-members
title: "@typescript-eslint/lines-between-class-members"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/lines-between-class-members
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:890b73947de87196f193875faa36161842dd9670a7d5f6c487d9be00ea0f3d92
---

禁止或者要求类成员之间有空行分隔。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/lines-between-class-members": "error"
  }
}
```

## 选项

该规则有两个选项配置，第一个选项可以是字符串或者对象，第二个选项是对象。详情请参考[eslint/lines-between-class-members选项](https://eslint.nodejs.cn/docs/latest/rules/lines-between-class-members#选项)。

此外，第二个选项支持配置exceptAfterOverload属性，表示是否需要跳过重载类成员后空行的检查。exceptAfterOverload的值为布尔类型，配置为true时表示跳过不检查，配置为false时表示不跳过检查。默认为true。

示例：

```screen
"@typescript-eslint/lines-between-class-members": [
  "error",
  "always",
  {
    "exceptAfterOverload": true
  },
]
```

## 正例

```screen
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

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
