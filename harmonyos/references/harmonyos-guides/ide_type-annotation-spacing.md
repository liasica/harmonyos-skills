---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_type-annotation-spacing
title: "@typescript-eslint/type-annotation-spacing"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/type-annotation-spacing
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:22+08:00
doc_updated_at: 2026-02-09
content_hash: sha256:b356dfa878de807adbb4eee2090c7d16dd9116cae9b3eb096940a9da90bdec75
---

类型注解前后需要一致的空格风格。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/type-annotation-spacing": "error"
  }
}
```

## 选项

支持配置以下选项：

```screen
type Options = {
  before: boolean;
  after: boolean;
  overrides: {
    colon: {
      before: boolean;
      after: boolean;
    };
    arrow: {
      before: boolean;
      after: boolean;
    };
    variable: {
      before: boolean;
      after: boolean;
    };
    parameter: {
      before: boolean;
      after: boolean;
    };
    property: {
      before: boolean;
      after: boolean;
    };
    returnType: {
      before: boolean;
      after: boolean;
    };
  }
}
```

* before/after：布尔类型，可以设置为true或者false。true表示类型注解中的冒号（:）和箭头（=>）之前/之后需要加空格，false表示类型注解中的冒号（:）和箭头（=>）之前/之后不需要加空格。
* overrides：对象类型，可以对不同的语法场景进行差异化配置，支持以下属性：
  + colon：对象类型，可以对类型注解中的冒号（:）进行差异化配置，支持以下属性：
    - before：布尔类型，可以设置为true或者false。默认值为false，表示类型注解中的冒号（:）之前不需要加空格；true表示类型注解中的冒号（:）之前需要加空格。
    - after：布尔类型，可以设置为true或者false。默认值为false，表示类型注解中的冒号（:）之后不需要加空格；true表示类型注解中的冒号（:）之后需要加空格。
  + arrow：对象类型，可以对类型注解中的箭头（=>）进行差异化配置，支持以下属性：
    - before：布尔类型，可以设置为true或者false。默认值为true，表示类型注解中的箭头（=>）之前需要加空格；false表示类型注解中的箭头（=>）之前不需要加空格。
    - after：布尔类型，可以设置为true或者false。默认值为true，表示类型注解中的箭头（=>）之后需要加空格；false表示类型注解中的箭头（=>）之后不需要加空格。
  + variable：对象类型，可以对变量中类型注解的冒号（:）进行差异化配置，支持配置为before/after：
    - before/after：布尔类型，可以设置为true或者false，true表示类型注解中的冒号（:）之前/之后需要加空格。
  + parameter：对象类型，可以对参数中类型注解的冒号（:）进行差异化配置，支持配置为before/after：
    - before/after：布尔类型，可以设置为true或者false，true表示类型注解中的冒号（:）之前/之后需要加空格。
  + property：对象类型，可以对类/接口成员中类型注解的冒号（:）进行差异化配置，支持配置为before/after：
    - before/after：布尔类型，可以设置为true或者false，true表示类型注解中的冒号（:）之前/之后需要加空格。
  + returnType：对象类型，可以对函数返回类型中类型注解的冒号（:）进行差异化配置，支持配置为before/after：
    - before/after：布尔类型，可以设置为true或者false，true表示类型注解中的冒号（:）之前/之后需要加空格。

示例：

```screen
"@typescript-eslint/type-annotation-spacing": [
  "error",
  {
    "before": true,
    "after": true,
    "overrides": {
      "colon": {
        "before": false,
        "after": true
      },
      "arrow": {
        "before": true,
        "after": true
      },
      "variable": {
        "before": true,
        "after": false
      },
      "parameter": {
        "before": false,
        "after": true
      },
      "property": {
        "before": true,
        "after": false
      },
      "returnType": {
        "before": true,
        "after": false
      }
    }
  }
]
```

**说明** 

选项存在优先级，overrides下的配置会覆盖overrides之外的配置：overrides.variable/parameter/property/returnType > overrides.colon/arrow > before/after。

## 正例

```screen
// 默认冒号前无空格，冒号后有空格
export const foo1: string = 'bar';

export declare function foo2(): string;

export class Foo3 {
  public name: string = 'hello';
}
// 默认箭头前后都有空格
export declare type Foo4 = () => void;
```

## 反例

```screen
// 默认冒号前无空格，冒号后有空格
export const foo1 :string = 'bar';

export declare function foo2() :string;

export class Foo3 {
  public name :string = 'hello';
}
// 默认箭头前后都有空格
export declare type Foo4 = ()=>void;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
