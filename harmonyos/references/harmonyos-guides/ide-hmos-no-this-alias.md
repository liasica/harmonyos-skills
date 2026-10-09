---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-this-alias
title: "@typescript-eslint/no-this-alias"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-this-alias
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:9299cf75b8b8452dd91f0a7b1b3b6a30ecf0d7bcee3da0da7677c1be130a8ef3
---

禁止将“this”赋值给一个变量。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-this-alias": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-this-alias选项](https://typescript-eslint.nodejs.cn/rules/no-this-alias/#options)。

## 正例

```ts
const time = 1000;
export class CC {
  public doWork(): void {
    console.info('work');
  }

  public init(): void {
    setTimeout(() => {
      this.doWork();
    }, time);
  }
}
```

## 反例

```ts
// 禁止将this赋值给一个变量
const self = this;

setTimeout(function () {
  self.doWork();
});
```

## 规则集

```screen
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
