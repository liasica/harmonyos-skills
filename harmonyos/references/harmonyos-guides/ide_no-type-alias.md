---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-type-alias
title: "@typescript-eslint/no-type-alias"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-type-alias
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:6c09fae7c61e63f716c5c06d3f9dff92b67a894087cf305029bd8f0ce9ad9e98
---

禁止使用类型别名。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-type-alias": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-type-alias选项](https://typescript-eslint.nodejs.cn/rules/no-type-alias/#options)。

## 正例

```screen
interface Person {
  readonly firstName: string;
  readonly lastName: string;
  readonly age: number;
}

export function addPerson(person: Person): Person {
  return person;
}
```

## 反例

```screen
// 不允许使用类型别名，建议使用接口替代
type Person = {
  readonly firstName: string;
  readonly lastName: string;
  readonly age: number;
};

export function addPerson(person: Person): Person {
  return person;
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
