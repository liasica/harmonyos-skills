---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-prefer-readonly
title: "@typescript-eslint/prefer-readonly"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-readonly
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:18+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:c0ec966025c9d79c9b6c107c7af968ac2287ed0aa8d50b1d12c4b068edbf8561
---

如果私有成员从未在构造函数之外进行修改，则要求将其标记为“只读”。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-readonly": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/prefer-readonly选项](https://typescript-eslint.nodejs.cn/rules/prefer-readonly/#options)。

## 正例

```ts
export class Container {
  // Public members might be modified externally
  public publicMember: boolean = true;

  // Protected members might be modified by child classes
  protected protectedMember: number = Number.MAX_VALUE;

  // This is modified later on by the class
  private modifiedLater = 'unchanged';

  public mutate() {
    this.modifiedLater = 'mutated';
  }
}
```

## 反例

```ts
export class Container {
  // These member variables could be marked as readonly
  private neverModifiedMember = true;

  private onlyModifiedInConstructor: number;

  // Private parameter properties can also be marked as readonly
  private neverModifiedParameter: string;

  public constructor(
    onlyModifiedInConstructor: number,
    // Private parameter properties can also be marked as readonly
    neverModifiedParameter: string,
  ) {
    this.neverModifiedParameter = neverModifiedParameter;
    this.onlyModifiedInConstructor = onlyModifiedInConstructor;
  }
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
