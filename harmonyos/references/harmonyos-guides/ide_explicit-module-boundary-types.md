---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_explicit-module-boundary-types
title: "@typescript-eslint/explicit-module-boundary-types"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/explicit-module-boundary-types
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:40eb1904c283a0008f71c3c59df7bbcc6c401eace7a757f01712cc3accc3726d
---

导出到外部的函数和公共类方法，需要显式的定义返回类型和参数类型。

该规则仅支持对.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/explicit-module-boundary-types": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/explicit-module-boundary-types选项](https://typescript-eslint.nodejs.cn/rules/explicit-module-boundary-types/#options)。

## 正例

```screen
// A function with no return value (void)
export function test1(): void {
  return;
}

// A return value of type string
export const arrowFn1 = (): string => 'test';

// All arguments should be typed
export const arrowFn2 = (arg: string): string => `test ${arg}`;

export class Test {
  // A class method with no return value (void)
  public method(): void {
    return;
  }
}

// The function does not apply because it is not an exported function.
function test2() {
  return;
}

test2();
```

## 反例

```screen
// Should indicate that no value is returned (void)
export function test() {
  return;
}

// Should indicate that a string is returned
export const arrowFn1 = () => 'test';

// All arguments should be typed
export const arrowFn2 = (arg): string => `test ${arg}`;
export const arrowFn3 = (arg: any): string => `test ${arg}`;

export class Test {
  // Should indicate that no value is returned (void)
  public method() {
    return;
  }
}
```

## 规则集

```screen
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
