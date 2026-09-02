---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_unbound-method
title: "@typescript-eslint/unbound-method"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/unbound-method
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b2d630d682fb32d749b0b372a61f263e5f36bf34ccb9d5e11ac503a681855feb
---

强制类作用域中的方法在预期范围内调用。

类方法作为独立变量传递时，不会保留类作用域，“this”不再指代当前类。解决方法是定义为“this: void”或者使用箭头函数。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/unbound-method": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/unbound-method选项](https://typescript-eslint.nodejs.cn/rules/unbound-method/#options)。

## 正例

```screen
class MyClass {
  public logUnbound(): void {
    this.logUnbound();
  }

  public logBound = () => {
    this.logUnbound();
  };
}

const instance = new MyClass();

// logBound will always be bound with the correct scope
const logBound = instance.logBound;
logBound();
```

## 反例

```screen
class MyClass {
  public logUnbound(): void {
    this.logUnbound();
  }

  public logBound = () => {
    this.logUnbound();
  };
}

const instance = new MyClass();

// logBound will always be bound with the correct scope
const logUnbound = instance.logUnbound;
logUnbound();
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
