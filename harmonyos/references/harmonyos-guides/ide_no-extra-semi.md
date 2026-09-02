---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-extra-semi
title: "@typescript-eslint/no-extra-semi"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-extra-semi
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ab5efa95089fb608854e85f4f609400d6176b312d6fbcf296b24669e5e78a2ca
---

禁止使用不必要的分号。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-extra-semi": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
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

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
