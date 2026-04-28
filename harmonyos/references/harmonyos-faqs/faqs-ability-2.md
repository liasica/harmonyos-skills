---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-2
title: 如何使用AbilityStage的生命周期函数
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何使用AbilityStage的生命周期函数
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:74bfdca232e2f2f28b5eea1101f4a0761e1145add766e93a522f2ae44923886c
---

DevEco Studio默认工程未包含AbilityStage。若需使用AbilityStage功能，可手动创建AbilityStage文件。具体步骤如下：

1. 在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录，命名为myabilitystage。
2. 在myabilitystage目录中，右键选择“New > ArkTS File”，新建一个文件并命名为MyAbilityStage.ets。
3. 打开MyAbilityStage.ets文件，导入AbilityStage的依赖包，自定义类继承AbilityStage并添加所需的生命周期回调。示例中添加了onCreate()生命周期回调。

   ```
   1. import { AbilityStage, Want } from '@kit.AbilityKit';

   3. export default class MyAbilityStage extends AbilityStage {
   4. onCreate(): void {
   5. // When the HAP of the application is first loaded, initialize the operation for the module
   6. }

   8. onAcceptWant(want: Want): string {
   9. // Triggered only when UIAbility is configured in specified startup mode
   10. return 'MyAbilityStage';
   11. }
   12. }
   ```

   [MyAbilityStage.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/myabilitystage/MyAbilityStage.ets#L21-L32)
4. 在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中，通过配置 srcEntry 参数来指定模块对应的代码路径，以作为HAP加载的入口。

   ```
   1. {
   2. "module": {
   3. "name": "entry",
   4. "type": "entry",
   5. "srcEntry": "./ets/myabilitystage/MyAbilityStage.ets",
   6. // ...
   7. }
   8. }
   ```

   [module\_myability.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/module_myability.json5#L5-L59)

[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md)拥有[onCreate()](../harmonyos-references/js-apis-app-ability-abilitystage.md#oncreate)、[onDestroy()](../harmonyos-references/js-apis-app-ability-abilitystage.md#ondestroy12)生命周期回调和[onAcceptWant()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onacceptwant)、[onConfigurationUpdate()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onconfigurationupdate)、[onMemoryLevel()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onmemorylevel)事件回调等。
