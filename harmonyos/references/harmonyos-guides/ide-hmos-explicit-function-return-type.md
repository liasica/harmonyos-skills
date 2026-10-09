---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-explicit-function-return-type
title: "@typescript-eslint/explicit-function-return-type"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/explicit-function-return-type
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:4ab3d218614429e8930b308b1f7f991b6ee7e1d6bc80bef14b7fb4adca55949c
---

函数和类方法需要显式的定义返回类型。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/explicit-function-return-type": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/explicit-function-return-type选项](https://typescript-eslint.nodejs.cn/rules/explicit-function-return-type/#options)。

## 正例

```ts
// No return value should be expected (void)
function test(): void {
  return;
}

// A return value of type number
const fn = function (): number {
  return Number.MAX_VALUE;
};

// A return value of type string
const arrowFn = (): string => 'test';

class Test {
  // No return value should be expected (void)
  public method(): void {
    return;
  }
}

export { test, fn, arrowFn, Test };
```

## 反例

```ts
// Should indicate that no value is returned (void)
function test() {
  return;
}

// Should indicate that a number is returned
const fn = function () {
  return Number.MAX_VALUE;
};

// Should indicate that a string is returned
const arrowFn = () => 'test';

class Test {
  // Should indicate that no value is returned (void)
  public method() {
    return;
  }
}

export { test, fn, arrowFn, Test };
```

## 规则集

```screen
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
