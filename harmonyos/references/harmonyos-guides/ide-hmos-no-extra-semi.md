---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-extra-semi
title: "@typescript-eslint/no-extra-semi"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-extra-semi
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:15f937c6ebe928afd163c9e76587b003fd1cb3956e25e54f62b18f909e84adec
---

禁止使用不必要的分号。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-extra-semi": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
export const x = 5;

export function foo() {
  // code
}

export const bar = () => {
  // code
};

export class C {
  public field: string = 'field';

  static {
    // code
  }

  public method() {
    // code
  }
}
```

## 反例

```ts
export const x = 5;;

export function foo() {
  // code
};

export const bar = () => {
  // code
};;

export class C {
  public field: string = 'field';;

  static {
    // code
  };

  public method() {
    // code
  };
};
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
