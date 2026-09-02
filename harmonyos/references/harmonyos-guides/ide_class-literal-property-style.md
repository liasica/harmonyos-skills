---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_class-literal-property-style
title: "@typescript-eslint/class-literal-property-style"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/class-literal-property-style
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:50+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:88ac9cc6d2b2526abd7b8e11e3d37bb0f7470c1498cff5c7b635122d99c9bee0
---

建议类中的字面量属性对外暴露时，保持一致的风格。

## 规则配置

```screen
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

```screen
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

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
