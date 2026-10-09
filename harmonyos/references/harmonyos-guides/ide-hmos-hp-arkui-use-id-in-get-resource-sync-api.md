---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hp-arkui-use-id-in-get-resource-sync-api
title: "@performance/hp-arkui-use-id-in-get-resource-sync-api"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-id-in-get-resource-sync-api
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:d0565f6bda7a932881145bace7b7d6961cda8c3d26eb67a7ad6e6c0fabbf9f70
---

在使用API getColorSync和getStringSync时建议带id版本。

高耗时函数处理场景下，建议优先修改。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-use-id-in-get-resource-sync-api": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```ts
import { BusinessError } from '@ohos.base';

try {
  // 本地resources中配置的color资源
  this.context.resourceManager.getColorSync($r('app.color.test').id);
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(`getColorSync failed, error code: ${code}, message: ${message}.`);
}
```

## 反例

```ts
import { BusinessError } from '@ohos.base';

try {
  // 本地resources中配置的color资源
  this.context.resourceManager.getColorSync($r('app.color.test'));
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(`getColorSync failed, error code: ${code}, message: ${message}.`);
}
```

## 规则集

```json
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
