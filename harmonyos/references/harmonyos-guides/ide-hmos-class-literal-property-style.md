---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-class-literal-property-style
title: "@typescript-eslint/class-literal-property-style"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/class-literal-property-style
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:038f28b01e6aa2d770fb18876baaf3ecea4ffe84656a67c81f2531f68c95a21c
---

建议类中的字面量属性对外暴露时，保持一致的风格。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/class-literal-property-style": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/class-literal-property-style选项](https://typescript-eslint.nodejs.cn/rules/class-literal-property-style/#options)。

## 正例

```ts
class Mx {
  public readonly myField1 = 'hello';

  public readonly myField2 = ['a', 'b'];

  public readonly ['myField3'] = 'hello world';

  public get myField4() {
    return `hello ${this.myField1}`;
  }
}

export { Mx };
```

## 反例

```ts
class Mx {
  public static get myField1() {
    return '1';
  }

  public get ['myField2']() {
    return 'hello world';
  }
}

export { Mx };
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
