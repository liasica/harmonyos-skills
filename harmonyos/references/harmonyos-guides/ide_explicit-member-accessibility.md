---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_explicit-member-accessibility
title: "@typescript-eslint/explicit-member-accessibility"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/explicit-member-accessibility
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d5a8fdfb04924bb95c22c88c49347fbf7da1afdbb07f8f495e93134750e54fac
---

在类属性和方法上需要显式定义访问修饰符。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/explicit-member-accessibility": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/explicit-member-accessibility选项](https://typescript-eslint.nodejs.cn/rules/explicit-member-accessibility)。

## 正例

```screen
export class Animal {
  private animalName: string; // Property

  public constructor(name: string) {
    // Parameter property and constructor
    this.animalName = name;
  }

  public get name(): string {
    // get accessor
    return this.animalName;
  }

  public set name(value: string) {
    // set accessor
    this.animalName = value;
  }

  public walk() {
    // method
  }
}
```

## 反例

```screen
export class Animal {
  private animalName: string; // Property

  constructor(name: string) {
    // Parameter property and constructor
    this.animalName = name;
  }

  get name(): string {
    // get accessor
    return this.animalName;
  }

  set name(value: string) {
    // set accessor
    this.animalName = value;
  }

  walk() {
    // method
  }
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
