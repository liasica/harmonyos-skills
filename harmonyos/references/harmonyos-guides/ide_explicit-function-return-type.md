---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_explicit-function-return-type
title: "@typescript-eslint/explicit-function-return-type"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/explicit-function-return-type
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:11ab95b3ad5542f21463f15d51afa01ffb70a928ee28922cdaa4dbd00027f72c
---

函数和类方法需要显式的定义返回类型。

该规则仅支持对.ts文件进行检查。通过配置选项，可以支持对.ets文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/explicit-function-return-type": "error"
  }
}
```

## 选项

该规则支持配置以下选项：

```screen
type Options = [
  {
    // 是否忽略.ets文件的检查，默认为false，不检查.ets文件
    allowArkTS?: boolean
  }
]
```

配置示例：

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/explicit-function-return-type": ["error", { "allowArkTS": true }]
  }
}
```

其余配置详情请参考[@typescript-eslint/explicit-function-return-type选项](https://typescript-eslint.nodejs.cn/rules/explicit-function-return-type/#options)。

## 正例

```screen
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

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
