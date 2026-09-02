---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_member-delimiter-style
title: "@typescript-eslint/member-delimiter-style"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/member-delimiter-style
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:133a9789bdfeb1fb7a4806a70b31c08e57c764abeed1c0284f78424c1e163aa9
---

要求接口和类型别名中的成员之间使用特定的分隔符。

支持定义的分隔符有三种：分号、逗号、无分隔符。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/member-delimiter-style": "error"
  }
}
```

## 选项

支持配置以下选项：

```screen
type BaseOption = {
  multiline: {
    delimiter: 'none' | 'semi' | 'comma';
    requireLast: boolean;
  };
  singleline: {
    delimiter: 'semi' | 'comma';
    requireLast: boolean;
  };
}

type Options = {
  multiline: {
    delimiter: 'none' | 'semi' | 'comma';
    requireLast: boolean;
  };
  singleline: {
    delimiter: 'semi' | 'comma';
    requireLast: boolean;
  };
  overrides: {
    interface: BaseOption;
    typeLiteral: BaseOption;
  };
  multilineDetection: 'brackets' | 'last-member';
}
```

* multiline/singleline：对象类型，分别定义多行/单行的interface/type alias成员之间分隔符风格，支持以下两种属性：
  + delimiter：枚举类型，定义分隔符风格，取值范围如下：
    - none：表示不需要加分隔符。
    - semi：表示建议使用分号作为分隔符。
    - comma：表示建议使用逗号作为分隔符。
  + requireLast：布尔类型，可以设置为true或者false，true表示最后一个成员的末尾需要加分隔符，false表示最后一个成员的末尾不加分隔符。

* multilineDetection：枚举类型，判断多行的依据，可取值如下：
  + brackets：默认值，表示interface/type alias中存在换行，即视为多行。
  + last-member：表示interface/type alias的最后一个成员与右括号（}）处于同一行，则视为单行。
* overrides：对象类型，可以针对interface/type alias进行差异化配置，支持以下两种属性：
  + interface：对象类型，可以对interface进行差异化配置，配置方式同multiline/singleline。
  + typeLiteral：对象类型，可以对type alias进行差异化配置，配置方式同multiline/singleline。

示例：

```screen
"@typescript-eslint/member-delimiter-style": [
  "error",
  {
    // 多行interface/type alias使用逗号作为分隔符，最后一个成员末尾不加分隔符
    "multiline": {
      "delimiter": "comma",
      "requireLast": false
    },
    // 单行interface/type alias使用分号作为分隔符，最后一个成员末尾需要加分隔符
    "singleline": {
      "delimiter": "semi",
      "requireLast": true
    },
    // 分别对interface和type alias进行差异化配置
    overrides: {
      interface: {
        "multiline": {
          "delimiter": "comma",
          "requireLast": false
        },
        "singleline": {
          "delimiter": "semi",
          "requireLast": true
        }
      },
      typeLiteral: {
        "multiline": {
          "delimiter": "comma",
          "requireLast": false
        },
        "singleline": {
          "delimiter": "semi",
          "requireLast": true
        }
      }
    },
    multilineDetection: "brackets",
  },
]
```

## 正例

```screen
// 默认接口/类型别名定义为多行的场景下，每个成员应以分号 (;) 分隔。 最后一个成员必须有一个分隔符。
// 默认接口/类型别名定义为单行的场景下，每个成员应以分号 (;) 分隔。最后一个成员不能有分隔符。
// 接口/类型别名中的任何换行符都会使其成为多行。
export interface Foo1 {
  name: string;

  greet(): string;
}

export interface Foo2 { name: string }
```

## 反例

```screen
// missing semicolon delimiter
export interface Foo {
  name: string
  greet(): string
}

// using incorrect delimiter
export interface Bar {
  name: string,
  greet(): string,
}

// missing last member delimiter
export interface Baz {
  name: string;
  greet(): string
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
