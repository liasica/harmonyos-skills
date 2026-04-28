---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-id-in-get-resource-sync-api
title: @performance/hp-arkui-use-id-in-get-resource-sync-api
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-id-in-get-resource-sync-api
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:09+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:7c01a0192306dc6da735cbdf5d04021abe85d27d1d887ce6f7a5a070dfd51a2e
---

在使用API getColorSync和getStringSync时建议带id版本。

高耗时函数处理场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-use-id-in-get-resource-sync-api": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { BusinessError } from '@ohos.base';

3. try {
4. // 本地resources中配置的color资源
5. this.context.resourceManager.getColorSync($r('app.color.test').id);
6. } catch (error) {
7. let code = (error as BusinessError).code;
8. let message = (error as BusinessError).message;
9. console.error(`getColorSync failed, error code: ${code}, message: ${message}.`);
10. }
```

## 反例

```
1. import { BusinessError } from '@ohos.base';

3. try {
4. // 本地resources中配置的color资源
5. this.context.resourceManager.getColorSync($r('app.color.test'));
6. } catch (error) {
7. let code = (error as BusinessError).code;
8. let message = (error as BusinessError).message;
9. console.error(`getColorSync failed, error code: ${code}, message: ${message}.`);
10. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
