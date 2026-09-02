---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-string-starts-ends-with
title: "@typescript-eslint/prefer-string-starts-ends-with"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-string-starts-ends-with
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:051f950c45f5ced27850b323c44055efd89b4db179cb0e888849d0b29608f8d5
---

强制使用“String#startsWith”和“String#endsWith”而不是其他检查子字符串的等效方法。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-string-starts-ends-with": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
declare const foo: string;

// starts with
foo.startsWith('bar');

// ends with
foo.endsWith('bar');
```

## 反例

```screen
declare const foo: string;
declare const index: number;
// starts with
foo[index] === 'b';
foo.charAt(index) === 'b';
foo.indexOf('bar') === index;
foo.slice(index) === 'bar';
foo.substring(index) === 'bar';
foo.match(/^bar/) !== null;
/^bar/.test(foo);

// ends with
foo[foo.length - index] === 'b';
foo.charAt(foo.length - index) === 'b';
foo.lastIndexOf('bar') === foo.length - index;
foo.slice(-index) === 'bar';
foo.substring(foo.length - index) === 'bar';
foo.match(/bar$/) !== null;
/bar$/.test(foo);
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
