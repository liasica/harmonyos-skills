---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-configuration
title: @ohos.application.Configuration (Configuration)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 已停止维护的接口 > @ohos.application.Configuration (Configuration)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:50+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ec323ab0ab539d19ed5cc2714e9888a83323c99c914949791003a04141aa09a1
---

定义环境变化信息。Configuration是接口定义，仅做字段声明。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块从API version 9废弃，替换模块为[@ohos.app.ability.Configuration (Configuration)](js-apis-app-ability-configuration.md)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import Configuration from '@ohos.application.Configuration';
```

## Configuration

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| language8+ | string | 否 | 是 | 表示应用程序的当前语言。例如：zh。 |
| colorMode8+ | [ConfigurationConstant.ColorMode](js-apis-application-configurationconstant.md#colormode) | 否 | 是 | 表示深浅色模式，取值范围：浅色模式（COLOR\_MODE\_LIGHT），深色模式（COLOR\_MODE\_DARK）。默认为浅色。 |

具体字段描述参考ohos.application.Configuration.d.ts文件

**示例：**

```
1. import UIAbility from '@ohos.app.ability.UIAbility';
2. import AbilityConstant from '@ohos.app.ability.AbilityConstant';
3. import EnvironmentCallback from '@ohos.app.ability.EnvironmentCallback';
4. import Want from '@ohos.app.ability.Want';
5. import Window from '@ohos.window';
6. import { BusinessError } from '@ohos.base';

8. export default class EntryAbility extends UIAbility {
9. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
10. }

12. onDestroy() {
13. }

15. onWindowStageCreate(windowStage: Window.WindowStage) {
16. let envCallback: EnvironmentCallback = {
17. onConfigurationUpdated(config) {
18. console.info(`envCallback onConfigurationUpdated success: ${JSON.stringify(config)}`);
19. let language = config.language;
20. let colorMode = config.colorMode;
21. },
22. onMemoryLevel(level) {
23. console.info(`onMemoryLevel level: ${JSON.stringify(level)}`);
24. }
25. };

27. let applicationContext = this.context.getApplicationContext();
28. try {
29. applicationContext.on('environment', envCallback);
30. } catch (paramError) {
31. console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
32. }

34. windowStage.loadContent('pages/index', (err, data) => {
35. if (err.code) {
36. console.error(`failed to load the content, error: ${JSON.stringify(err)}`);
37. return;
38. }
39. console.info(`Succeeded in loading the content, data: ${JSON.stringify(data)}`);
40. });
41. }
42. }
```
