---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-2
title: 如何使用AbilityStage的生命周期函数
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何使用AbilityStage的生命周期函数
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ae6681177ff0b42d94f7413cbc6d4b2165011f9cb28d65c681a87dd8b4efc976
---

DevEco Studio默认工程未包含AbilityStage。若需使用AbilityStage功能，可手动创建AbilityStage文件。具体步骤如下：

1. 在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录，命名为myabilitystage。
2. 在myabilitystage目录中，右键选择“New > ArkTS File”，新建一个文件并命名为MyAbilityStage.ets。
3. 打开MyAbilityStage.ets文件，导入AbilityStage的依赖包，自定义类继承AbilityStage并添加所需的生命周期回调。示例中添加了onCreate()生命周期回调。

   ```typescript
   import { AbilityStage, Want } from '@kit.AbilityKit';

   export default class MyAbilityStage extends AbilityStage {
     onCreate(): void {
       // When the HAP of the application is first loaded, initialize the operation for the module
     }

     onAcceptWant(want: Want): string {
       // Triggered only when UIAbility is configured in specified startup mode
       return 'MyAbilityStage';
     }
   }
   ```
4. 在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中，通过配置 srcEntry 参数来指定模块对应的代码路径，以作为HAP加载的入口。

   ```json
   {
     "module": {
       "name": "entry",
       "type": "entry",
       "srcEntry": "./ets/myabilitystage/MyAbilityStage.ets",
       // ...
     }
   }
   ```

[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md)拥有[onCreate()](../harmonyos-references/js-apis-app-ability-abilitystage.md#oncreate)、[onDestroy()](../harmonyos-references/js-apis-app-ability-abilitystage.md#ondestroy12)生命周期回调和[onAcceptWant()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onacceptwant)、[onConfigurationUpdate()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onconfigurationupdate)、[onMemoryLevel()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onmemorylevel)事件回调等。
