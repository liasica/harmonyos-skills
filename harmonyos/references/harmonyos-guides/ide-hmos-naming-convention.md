---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-naming-convention
title: "@typescript-eslint/naming-convention"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/naming-convention
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:32f7a24a0529d6fd208d53b94b2dbf7f11e0320a9c04d51a31ed96efe08f7c8c
---

强制标识符使用一致的命名风格。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/naming-convention": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/naming-convention选项](https://typescript-eslint.nodejs.cn/rules/naming-convention/#options)。

## 正例

```ts
// 默认类名为大驼峰的命名风格，函数名为小驼峰的命名风格
export class Bar {
  public meth() {
    console.info('method');
  }
}

export function foo() {
  console.info('function');
}
```

## 反例

```ts
// 默认类名为大驼峰的命名风格，函数名为小驼峰的命名风格
export class bar {
  public Meth() {
    console.info('method');
  }
}

export function Foo() {
  console.info('function');
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
