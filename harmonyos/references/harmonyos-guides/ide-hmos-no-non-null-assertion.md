---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-non-null-assertion
title: "@typescript-eslint/no-non-null-assertion"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-non-null-assertion
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c65eaafa8243d83d976c7454aab2f3d16cc8f47eec56f114702a1ffb9fb88288
---

禁止以感叹号作为后缀的方式使用非空断言。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-non-null-assertion": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
interface Example {
  property?: string;
}

declare const example: Example;
export const includesBaz = example.property?.includes('baz') ?? false;
```

## 反例

```ts
interface Example {
  property?: string;
}

declare const example: Example;
// 禁止使用"example.property!"的方式来进行非空断言
export const includesBaz = example.property!.includes('baz');
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
