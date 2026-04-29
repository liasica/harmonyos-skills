---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-environment
title: Environment：设备环境查询
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V1） > 管理应用拥有的状态 > Environment：设备环境查询
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:17+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:05f16a55089fe6b912dad1a3e9196e9be1352d88d274a83f1fef38168625a66f
---

如果开发者需要获取应用程序运行设备的环境参数（如多语言、深浅色模式等）以进行不同的场景判断，可以使用Environment设备环境查询。

Environment是ArkUI框架在应用程序启动时创建的单例对象，为[AppStorage](arkts-appstorage.md)提供应用程序运行状态的属性。所有属性都是不可变的简单类型。

Environment提供了读取系统环境变量并将其值写入AppStorage的功能。开发者需要通过AppStorage获取环境变量的值。详细信息请参阅 [Environment 内置参数](arkts-environment.md#environment内置参数)。

在阅读本文档前，建议提前阅读：[AppStorage](arkts-appstorage.md)。

## Environment内置参数

| 键 | 数据类型 | 描述 |
| --- | --- | --- |
| accessibilityEnabled | string | 是否启用获取无障碍屏幕阅读。'true'表示启用，'false'表示不启用。 |
| colorMode | [ColorMode](../harmonyos-references/ts-state-management-environment-variables.md#colormode) | 色彩模型类型。  - ColorMode.LIGHT：浅色。  - ColorMode.DARK：深色。 |
| fontScale | number | 字体大小比例。开发者需要配置configuration，设置fontSizeScale为"followSystem"，具体配置步骤可参考[configuration](app-configuration-file.md#configuration标签)使fontScale跟随系统变化。  默认值跟随系统默认参数。 |
| fontWeightScale | number | 字体粗细程度。在不同的系统或者机型中，fontWeightScale的取值范围可能会有所不同。  默认值跟随系统默认参数。 |
| layoutDirection | [LayoutDirection](../harmonyos-references/ts-state-management-environment-variables.md#layoutdirection) | 布局方向类型：  - LayoutDirection.LTR：从左到右。  - LayoutDirection.RTL：从右到左。 |
| languageCode | string | 当前系统语言值，取值必须为小写字母（例如：zh）。  默认值跟随系统默认参数。 |

## 限制条件

Environment和[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)相关联，需要在UIContext明确的时候才可以调用Environment的接口，可以通过在[runScopedTask](../harmonyos-references/arkts-apis-uicontext-uicontext.md#runscopedtask)里调用明确上下文。如果不是在UIContext明确的地方调用，将导致无法查询到设备环境数据。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage) {
6. windowStage.loadContent('pages/Index');
7. let window = windowStage.getMainWindow();
8. window.then(window => {
9. let uiContext = window.getUIContext();
10. // Environment在UIContext.runScopedTask里调用明确上下文
11. uiContext.runScopedTask(() => {
12. Environment.envProp('languageCode', 'en');
13. });
14. });
15. }
16. }
```

## 使用场景

### 从UI中访问Environment参数

* 使用Environment.[envProp](../harmonyos-references/ts-state-management.md#envprop10)将设备运行的环境变量存入AppStorage中。

  ```
  1. // 将设备的languageCode存入AppStorage，默认值为en
  2. Environment.envProp('languageCode', 'en');
  ```
* 在自定义组件中通过@StorageProp获取languageCode的值。

  ```
  1. @StorageProp('languageCode') lang: string = 'en';
  ```

设备环境到Component的更新链：Environment --> AppStorage --> Component。

说明

应用无法修改环境变量参数，因此使用@StorageProp获取。这样即使在组件内修改，也不会同步回AppStorage中，影响其他组件处获取环境变量的结果。

```
1. // 将设备languageCode存入AppStorage中
2. Environment.envProp('languageCode', 'en');

4. @Entry
5. @Component
6. struct UiEnvironment {
7. @StorageProp('languageCode') languageCode: string = 'en';

9. build() {
10. Row() {
11. Column() {
12. // 输出当前设备的languageCode
13. Text(this.languageCode)
14. }
15. }
16. }
17. }
```

### 应用逻辑使用Environment

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0001;
4. const TAG = 'environmentalProject';

6. // 使用Environment.envProp将设备运行languageCode存入AppStorage中
7. Environment.envProp('languageCode', 'en');
8. // 从AppStorage获取单向绑定的languageCode的变量
9. const lang: SubscribedAbstractProperty<string> = AppStorage.prop('languageCode');

11. if (lang.get() === 'zh') {
12. // 请将$r('app.string.AppliedLogic_Hello')替换为实际资源文件，在本示例中该资源文件的value值为"你好"
13. hilog.info(DOMAIN, TAG, `${$r('app.string.AppliedLogic_Hello')}`);
14. } else {
15. hilog.info(DOMAIN, TAG, 'Hello!');
16. }
```
