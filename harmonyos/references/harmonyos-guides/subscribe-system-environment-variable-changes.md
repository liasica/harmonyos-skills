---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/subscribe-system-environment-variable-changes
title: 获取/设置环境变量
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 应用模型 > 应用组件 > 获取/设置环境变量
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1c052b22282e20e249483d26201ba46292d5d6498a20abcff6c179984de8c7b6
---

环境变量涵盖了所有可能影响应用运行时的环境配置信息，包括应用可指定的内部环境变量（字体大小、外观、语言等）和应用可感知的外部环境变量（屏幕方向等）。

通常条件下，环境变量会跟随系统设置变化。

## 使用场景

| 场景 | 说明 | 约束限制 | 场景举例 |
| --- | --- | --- | --- |
| [获取环境变量](subscribe-system-environment-variable-changes.md#获取环境变量) | 开发者可以使用[getConfigurationSync](../harmonyos-references/js-apis-resource-manager.md#getconfigurationsync10)主动获取当前环境变量，包括深浅色模式、屏幕方向、语言地区、屏幕密度、设备类型等。 | 当前仅支持同步获取，使用方式参考[ResourceManager.getConfigurationSync](../harmonyos-references/js-apis-resource-manager.md#getconfigurationsync10)。 | 应用运行过程中，可以主动获取当前应用深浅色模式，以更新用户界面显示。 |
| [设置环境变量](subscribe-system-environment-variable-changes.md#设置环境变量) | 当前仅支持应用自定义字体大小、深浅色、语言。  - [设置字体大小](subscribe-system-environment-variable-changes.md#设置字体大小)  - [设置深浅色模式](subscribe-system-environment-variable-changes.md#设置深浅色模式)  - [设置应用语言](subscribe-system-environment-variable-changes.md#设置应用语言) | 当应用设置环境变量后，应用将无法通过订阅感知到对应的环境变量在系统中的变化。 | 应用自定义字体大小，以提升用户体验。 |
| [订阅环境变量](subscribe-system-environment-variable-changes.md#订阅环境变量) | 通过订阅环境变量，及时感知系统环境变化。支持订阅的环境变量包括语言、深浅色、屏幕方向等，详见[Configuration](../harmonyos-references/js-apis-app-ability-configuration.md)。 | - 如果开发者将环境变量配置为不跟随系统变化（即[configuration标签](app-configuration-file.md#configuration标签)中的对应字段取值为“nonFollowSystem”），应用将无法通过订阅感知对应的环境变量在系统中的变化。  - 应用订阅环境变量后，当应用处于后台时，环境变量发生变更，应用将无法实时收到订阅通知。相关通知推送会被延迟处理，待应用切换回前台时，才会收到订阅通知。 | 当用户旋转设备屏幕时，应用可以通过订阅环境变量感知环境变化重新布局用户界面，以适应屏幕方向和尺寸。 |

## 获取环境变量

开发者可以使用[getConfigurationSync](../harmonyos-references/js-apis-resource-manager.md#getconfigurationsync10)主动获取当前[环境变量](../harmonyos-references/js-apis-resource-manager.md#configuration)，包括深浅色模式、屏幕方向、语言地区、屏幕密度、设备类型等，对应用程序作出相应处理，提供更好的用户体验。

```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN_NUMBER = 0xF811;
const TAG = '[EnvAbility0]';

export default class EnvAbility0 extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let value = this.context.resourceManager.getConfigurationSync();
      // 屏幕方向
      let direction = value.direction;
      // 语言文字国家地区
      let locale = value.locale;
    } catch (error) {
      hilog.error(DOMAIN_NUMBER, TAG, 'getConfigurationSync error is ' + error);
    }
  }
}
```

## 设置环境变量

支持应用自定义的环境变量包括[字体大小](subscribe-system-environment-variable-changes.md#设置字体大小)、[深浅色模式](subscribe-system-environment-variable-changes.md#设置深浅色模式)、[应用语言](subscribe-system-environment-variable-changes.md#设置应用语言)，其他环境变量（例如屏幕方向等）均不支持直接设置。

### 设置字体大小

应用字体大小默认不跟随系统变化，开发者可以通过将[configuration标签](app-configuration-file.md#configuration标签)中fontSizeScale的值配置为followSystem，使得应用字体大小跟随系统变化。

开发者可以使用[setFontSizeScale](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextsetfontsizescale13)设置应用字体大小。设置后，应用字体将不跟随系统变化，不再支持订阅系统字体大小变化。

```typescript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EnvAbility1 extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        return;
      }
    });
    let applicationContext = this.context.getApplicationContext();
    applicationContext.setFontSizeScale(2);
  }
}
```

### 设置深浅色模式

应用深浅色模式默认跟随系统。开发者可以设置应用或组件的深浅色模式。设置后，不再支持订阅系统的深浅色模式变化。

配置生效的优先级为：UIAbility/UIExtensionAbility的深浅色模式 > 应用的深浅色模式 > 系统的深浅色模式。

* **设置应用的深浅色模式：** 使用ApplicationContext的[setColorMode](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextsetcolormode11)接口，可以设置应用深浅色模式。

  ```typescript
  import { UIAbility, ConfigurationConstant } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { window } from '@kit.ArkUI';

  export default class EnvAbility2 extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
      windowStage.loadContent('pages/Index', (err, data) => {
        if (err.code) {
          hilog.error(0x0000, 'testTag', 'Failed to load the content.');
          return;
        }
        let applicationContext = this.context.getApplicationContext();
        applicationContext.setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
      });
    }
  }
  ```
* **设置UIAbility的深浅色模式：** 使用UIAbilityContext的[setColorMode](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#setcolormode18)，可以设置UIAbility的深浅色模式。

  ```typescript
  import { UIAbility, ConfigurationConstant } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { window } from '@kit.ArkUI';

  export default class EnvAbility3 extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
      windowStage.loadContent('pages/Index', (err, data) => {
        if (err.code) {
          hilog.error(0x0000, 'testTag', 'Failed to load the content.');
          return;
        }
        let uiAbilityContext = this.context;
        uiAbilityContext.setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
      });
    }
  }
  ```
* **设置UIExtensionAbility的深浅色模式：** 使用UIExtensionContext的[setColorMode](../harmonyos-references/js-apis-inner-application-uiextensioncontext.md#setcolormode18)，可以设置UIExtensionAbility的深浅色模式。

  ```typescript
  // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
  import { ShareExtensionAbility, ConfigurationConstant } from '@kit.AbilityKit';

  export default class EnvAbility4 extends ShareExtensionAbility {
    onForeground() {
      let uiExtensionContext = this.context;
      uiExtensionContext.setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
    }
  }
  ```

### 设置应用语言

应用语言默认跟随系统语言变化。开发者可以使用[setLanguage](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextsetlanguage11)设置应用语言。设置后，不再支持订阅系统语言变化。

```typescript
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

export default class EnvAbility5 extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content.');
        return;
      }
      let applicationContext = this.context.getApplicationContext();
      applicationContext.setLanguage('zh-cn');
    });
  }
}
```

## 订阅环境变量

系统配置的变化通常由“设置”中的选项或“控制中心”中的图标触发。订阅环境变量变化，可以使应用程序更加智能地响应系统环境变化，从而提供更好的用户体验。查看当前支持订阅变化的环境变量，参见[Configuration](../harmonyos-references/js-apis-app-ability-configuration.md)。

基于当前的应用模型，可以通过以下几种方式来实现订阅环境变量的变化。

* [使用ApplicationContext订阅回调](subscribe-system-environment-variable-changes.md#使用applicationcontext订阅回调)
* [在AbilityStage组件管理器中订阅回调](subscribe-system-environment-variable-changes.md#在abilitystage组件管理器中订阅回调)
* [在UIAbility组件中订阅回调](subscribe-system-environment-variable-changes.md#在uiability组件中订阅回调)
* [在ExtensionAbility组件中订阅回调](subscribe-system-environment-variable-changes.md#在extensionability组件中订阅回调)

### 使用ApplicationContext订阅回调

[ApplicationContext](../harmonyos-references/js-apis-inner-application-applicationcontext.md)提供了注册回调函数以订阅环境变量的变化，并且可以通过调用相应的方法来撤销该回调。这有助于在资源不再需要时释放相关资源，从而提高系统的可靠性和性能。

1. 使用[on](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextonenvironment)方法，应用程序可以通过在非应用组件模块中订阅环境变量的变化来动态响应这些变化。例如，使用该方法在页面中监测系统语言的变化。

   ```typescript
   import { common, EnvironmentCallback, Configuration } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   const TAG: string = '[EnvAbilityPage6]';
   const DOMAIN_NUMBER: number = 0xFF00;

   @Entry
   @Component
   struct EnvAbilityPage6 {
     private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     private callbackId: number = 0; // 注册订阅系统环境变化的ID

     subscribeConfigurationUpdate(): void {
       let systemLanguage: string | undefined = this.context.config.language; // 获取系统当前语言

       // 1.获取ApplicationContext
       let applicationContext = this.context.getApplicationContext();

       // 2.通过applicationContext订阅环境变量变化
       let environmentCallback: EnvironmentCallback = {
         onConfigurationUpdated(newConfig: Configuration) {
           hilog.info(DOMAIN_NUMBER, TAG, `onConfigurationUpdated systemLanguage is ${systemLanguage}, newConfig: ${JSON.stringify(newConfig)}`);
           if (systemLanguage !== newConfig.language) {
             hilog.info(DOMAIN_NUMBER, TAG, `systemLanguage from ${systemLanguage} changed to ${newConfig.language}`);
             systemLanguage = newConfig.language; // 将变化之后的系统语言保存，作为下一次变化前的系统语言
           }
         },
         onMemoryLevel(level) {
           hilog.info(DOMAIN_NUMBER, TAG, `onMemoryLevel level: ${level}`);
         }
       }
       try {
         this.callbackId = applicationContext.on('environment', environmentCallback);
       } catch (err) {
         let code = (err as BusinessError).code;
         let message = (err as BusinessError).message;
         hilog.error(DOMAIN_NUMBER, TAG, `Failed to register applicationContext. Code is ${code}, message is ${message}`);
       }
     }

     // 页面展示
     build() {
       // ...
     }
   }
   ```
2. 在资源使用完成之后，可以通过调用[off](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextoffenvironment-1)方法释放相关资源。

   ```typescript
   import { common } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   const TAG: string = '[EnvAbilityPage7]';
   const DOMAIN_NUMBER: number = 0xFF00;

   @Entry
   @Component
   struct EnvAbilityPage7 {
     private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     private callbackId: number = 0; // 注册订阅系统环境变化的ID

     unsubscribeConfigurationUpdate() {
       let applicationContext = this.context.getApplicationContext();
       try {
         applicationContext.off('environment', this.callbackId);
       } catch (err) {
         let code = (err as BusinessError).code;
         let message = (err as BusinessError).message;
         hilog.error(DOMAIN_NUMBER, TAG, `Failed to unregister applicationContext. Code is ${code}, message is ${message}`);
       }
     }

     // 页面展示
     build() {
       // ...
     }
   }
   ```

### 在AbilityStage组件管理器中订阅回调

使用[AbilityStage.onConfigurationUpdate()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onconfigurationupdate)回调方法订阅环境变量的变化。当环境变量发生变化时，会调用该回调方法。在该方法中，通过[Configuration](../harmonyos-references/js-apis-app-ability-configuration.md)对象获取最新的环境变量信息。可以进行相应的界面适配等操作，从而提高系统的灵活性和可维护性。

**说明** 

* DevEco Studio默认工程中未自动生成[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md)，AbilityStage文件的创建参见[AbilityStage开发步骤](abilitystage.md#开发步骤)。
* 当使用回调方法订阅系统环境变量的变化时，该回调方法会随着AbilityStage的生命周期而存在，在Module销毁时一并销毁。

例如，在[AbilityStage.onConfigurationUpdate()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onconfigurationupdate)回调方法中实现监测系统语言的变化。

```typescript
import { AbilityStage, Configuration } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[EnvAbilityStage]';
const DOMAIN_NUMBER: number = 0xFF00;

let systemLanguage: string | undefined; // 系统当前语言

export default class EnvAbilityStage extends AbilityStage {
  onCreate(): void {
    systemLanguage = this.context.config.language; // Module首次加载时，获取系统当前语言
    hilog.info(DOMAIN_NUMBER, TAG, `systemLanguage is ${systemLanguage}`);
  }

  onConfigurationUpdate(newConfig: Configuration): void {
    hilog.info(DOMAIN_NUMBER, TAG, `onConfigurationUpdate, language: ${newConfig.language}`);
    hilog.info(DOMAIN_NUMBER, TAG, `onConfigurationUpdated systemLanguage is ${systemLanguage}, newConfig: ${JSON.stringify(newConfig)}`);

    if (systemLanguage !== newConfig.language) {
      hilog.info(DOMAIN_NUMBER, TAG, `systemLanguage from ${systemLanguage} changed to ${newConfig.language}`);
      systemLanguage = newConfig.language; // 将变化之后的系统语言保存，作为下一次变化前的系统语言
    }
  }
}
```

### 在UIAbility组件中订阅回调

[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)组件提供了[UIAbility.onConfigurationUpdate()](../harmonyos-references/js-apis-app-ability-ability.md#abilityonconfigurationupdate)回调方法用于订阅环境变量的变化。当环境变量发生变化时，会调用该回调方法。在该方法中，通过[Configuration](../harmonyos-references/js-apis-app-ability-configuration.md)对象获取最新的环境变量信息，而无需重启UIAbility。

**说明** 

* 当应用通过回调方法订阅环境变量变化时，该订阅会随着所在UIAbility的生命周期持续有效。一旦UIAbility被销毁，之前注册的所有回调订阅将自动失效，同时应用将不会再收到订阅的回调信息。
* 如果使用该接口监听屏幕方向变化，需要在module.json5配置文件的[abilities标签](module-configuration-file.md#abilities标签)中将orientation字段配置为auto\_rotation。

例如，在[onConfigurationUpdate()](../harmonyos-references/js-apis-app-ability-ability.md#abilityonconfigurationupdate)回调方法中实现监测系统语言的变化。

```typescript
import { AbilityConstant, Configuration, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[EnvAbility9]';
const DOMAIN_NUMBER: number = 0xFF00;

let systemLanguage: string | undefined; // 系统当前语言

export default class EnvAbility9 extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    systemLanguage = this.context.config.language; // UIAbility实例首次加载时，获取系统当前语言
    hilog.info(DOMAIN_NUMBER, TAG, `systemLanguage is ${systemLanguage}`);
  }

  onConfigurationUpdate(newConfig: Configuration): void {
    hilog.info(DOMAIN_NUMBER, TAG, `onConfigurationUpdated systemLanguage is ${systemLanguage}, newConfig: ${JSON.stringify(newConfig)}`);

    if (systemLanguage !== newConfig.language) {
      hilog.info(DOMAIN_NUMBER, TAG, `systemLanguage from ${systemLanguage} changed to ${newConfig.language}`);
      systemLanguage = newConfig.language; // 将变化之后的系统语言保存，作为下一次变化前的系统语言
    }
  }
}
```

### 在ExtensionAbility组件中订阅回调

[ExtensionAbility](../harmonyos-references/js-apis-app-ability-extensionability.md)组件提供了[onConfigurationUpdate()](../harmonyos-references/js-apis-app-ability-ability.md#abilityonconfigurationupdate)回调方法用于订阅环境变量的变化。当环境变量发生变化时，会调用该回调方法。在该方法中，通过[Configuration](../harmonyos-references/js-apis-app-ability-configuration.md)对象获取最新的环境变量信息。

**说明** 

当应用通过回调方法订阅环境变量变化时，该订阅会随着所在ExtensionAbility的生命周期持续有效。一旦ExtensionAbility被销毁，之前注册的所有回调订阅将自动失效，同时应用将不会再收到订阅的回调信息。

以[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)为例说明。例如，在[onConfigurationUpdate()](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonconfigurationupdate)回调方法中实现环境变量的变化。

```typescript
import { FormExtensionAbility } from '@kit.FormKit';
import { Configuration } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[EnvFormExtensionAbility]';
const DOMAIN_NUMBER: number = 0xFF00;

export default class EnvFormExtensionAbility extends FormExtensionAbility {
  onConfigurationUpdate(newConfig: Configuration) {
    hilog.info(DOMAIN_NUMBER, TAG, 'onConfigurationUpdate: ' + JSON.stringify(newConfig));
  }
}
```
