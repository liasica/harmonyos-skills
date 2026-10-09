---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-file-naming-convention
title: "@hw-stylistic/file-naming-convention"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/file-naming-convention
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:cbf6201a89cf3ce7c1e32ac564ce07a0308ff8fd4a2043a250ab25f9010250aa
---

强制代码文件和资源文件保持一致的命名风格。

* .js文件建议使用小驼峰，.ets/.ts建议使用大驼峰；
* 资源文件建议使用小驼峰或者小写字母加下划线的风格命名。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/file-naming-convention": "error"
  }
}
```

## 选项

该规则默认检查代码文件和资源文件的命名风格，也可以接受一个对象作为参数{selector: string}，来指定只检查代码文件或者资源文件。"selector"支持配置为"resources"或者"code"。

示例：

1.以下配置只检查代码文件命名风格：

```json
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/file-naming-convention": ["error", { "selector": "code" }]
  }
}
```

2.以下配置只检查资源文件命名风格：

```json
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/file-naming-convention": ["error", { "selector": "resources" }]
  }
}
```

## 正例

```ts
// 代码文件名：Index.ets、EntryAbility.ets、index.js
// 资源文件名：color.json、background.png、main_pages.json
```

## 反例

```ts
// 代码文件名：index.ets、ability.ets、Index.js
// 资源文件名：String.json、BackGround.png
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
