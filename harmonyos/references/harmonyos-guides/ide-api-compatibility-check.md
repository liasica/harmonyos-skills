---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-api-compatibility-check
title: @compatibility/api-compatibility-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 兼容性规则@compatibility > @compatibility/api-compatibility-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:32+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:644274382a6243c80dd07087b5e74cee671ccf4cac0daceeeace2d13baee0e8d
---

从DevEco Studio 6.0.1 Beta1开始，Code Linter新增版本兼容性规则扫描。

工程代码中调用的API版本比工程配置中的compatibleSdkVersion版本高，可能会导致兼容性问题。建议添加代码报错措施，消除兼容性问题。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@compatibility/api-compatibility-check": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

**示例一**：API调用前，增加SDK版本判断。

```
1. import { dataUriUtils } from '@kit.AbilityKit';
2. import { deviceInfo } from '@kit.BasicServicesKit';

4. @Component
5. struct Test {
6. build() {
7. Text('hello').onClick(() => {
8. // 使用接口前增加SDK版本的判断，SDK版本计算方式具体请参考应用升级targetSDKVersion兼容低版本指导
9. if (deviceInfo.distributionOSApiVersion >= 60000) {
10. dataUriUtils.getId('');
11. }

13. // 使用接口前增加SDK版本的判断
14. if (deviceInfo.sdkApiVersion >= 20) {
15. dataUriUtils.getId('');
16. }
17. })
18. }
19. }
```

**示例二**：API调用前，增加判空。

```
1. import { dataUriUtils } from '@kit.AbilityKit';

3. @Component
4. struct Test {
5. build() {
6. Text("hello").onClick(() => {
7. // 判空
8. if (dataUriUtils.getId !== undefined) {
9. dataUriUtils.getId('');
10. }
11. })
12. }
13. }
```

**示例三**：API调用前，使用try-catch异常处理。

```
1. import { dataUriUtils } from '@kit.AbilityKit'

3. @Component
4. struct Test {
5. build() {
6. Text('hello').onClick(() => {
7. // 使用try-catch语法
8. try {
9. dataUriUtils.getId('');
10. } catch (error) {
11. // 异常处理
12. }
13. })
14. }
15. }
```

## 反例

```
1. // 工程中compatibleSdkVersion配置为5.0.5(17)
2. import { ScrollEffectType } from '@kit.UIDesignKit';

4. @Component
5. struct Test {
6. build() {
7. Text('hello').onClick(() => {
8. // ScrollEffectType.COMMON_BLUR从5.1.0(18)开始支持，不可直接调用
9. const value = ScrollEffectType.COMMON_BLUR
10. console.info(value.toString())
11. })
12. }
13. }
```

## 规则集

```
1. plugin:@compatibility/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
