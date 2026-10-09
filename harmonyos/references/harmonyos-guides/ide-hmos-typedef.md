---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-typedef
title: "@typescript-eslint/typedef"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/typedef
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:52f215447d3ceb79cf809e32f04357a124b257fd4fd210c2a9b0326085c81c93
---

在某些位置需要类型注释。

支持检查的范围从选项中查看。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/typedef": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/typedef选项](https://typescript-eslint.nodejs.cn/rules/typedef#options)。

## 正例

```ts
export const text = 'text';
```

## 反例

```ts
// 默认配置下，规则不会告警
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
