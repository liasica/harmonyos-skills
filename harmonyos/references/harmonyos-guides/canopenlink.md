---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canopenlink
title: （可选）使用canOpenLink判断应用是否可访问
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:49+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4dfcf0ecbdb805c219be6ed9a07d1b7c7a5d3e5738aab28ae98c3a095687625b
---

## 使用场景

在应用A想要拉起应用B的场景中，应用A可先调用canOpenLink接口判断应用B是否可访问，如果可访问，再拉起应用B。

说明

canOpenLink接口不支持判断以App Linking方式跳转的目标应用是否可访问。

## 约束限制

在entry模块的module.json5文件中的[querySchemes](module-configuration-file.md)字段中，从API version 21开始，最多允许配置200个URL scheme。API version 20及之前的版本，最多允许配置50个URL scheme。

## 接口说明

canOpenLink是[bundleManager](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagercanopenlink12)提供的支持判断目标应用是否可访问的接口。

匹配规则请参考[显式Want与隐式Want匹配规则](explicit-implicit-want-mappings.md)。

## 操作步骤

### 调用方操作步骤

1. 在entry模块的module.json5文件中配置[querySchemes](module-configuration-file.md)属性，声明想要查询的URL scheme。

   ```
   1. {
   2. "module": {
   3. //...
   4. "querySchemes": [
   5. "app1Scheme"
   6. ]
   7. }
   8. }
   ```
2. 导入ohos.bundle.bundleManager模块。
3. 调用canOpenLink接口。

   ```
   1. import { bundleManager } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. try {
   6. let link = 'app1Scheme://test.example.com/home';
   7. let canOpen = bundleManager.canOpenLink(link);
   8. hilog.info(0x0000, 'testTag', 'canOpenLink successfully: %{public}s', JSON.stringify(canOpen));
   9. } catch (err) {
   10. let message = (err as BusinessError).message;
   11. hilog.error(0x0000, 'testTag', 'canOpenLink failed: %{public}s', message);
   12. }
   ```

### 目标方操作步骤

在module.json5文件中配置[uris](module-configuration-file.md#skills标签)属性。

```
1. {
2. "module": {
3. //...
4. "abilities": [
5. {
6. //...
7. "skills": [
8. {
9. // actions不能为空，actions为空会造成目标方匹配失败
10. "actions": [
11. "ohos.want.action.home"
12. ],
13. "uris": [
14. {
15. "scheme": "app1Scheme",
16. "host": "test.example.com",
17. "pathStartWith": "home"
18. }
19. ]
20. }
21. ]
22. }
23. ]
24. }
25. }
```

## FAQ

1. 为什么限制querySchemes中配置的URL scheme个数？

   canOpenLink()接口提供了判断应用是否可以访问的能力。通过该能力，应用可以间接获取到指定应用是否安装等信息。

   为了保护系统安全和用户隐私，避免恶意应用扫描应用安装列表等行为，要求开发者在使用canOpenLink()接口时必须配置querySchemes属性，从API version 21开始，最多允许配置200个URL scheme。API version 20及之前的版本，最多允许配置50个URL scheme。
