---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-144
title: 如何设置应用内字体是否跟随系统变化
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何设置应用内字体是否跟随系统变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:10c8f98a43af87d60c1b3acb61dc7a64fb425b32b0aa49f98cc9e4c555de9fe4
---

## 问题现象

在系统【设置】中，可以调整字体大小、显示大小缩放、字体粗细的字体样式。如何设置应用配置，使应用内字体样式，具备是否跟随系统字体样式变化的能力。

## 背景知识

* [configuration标签](../harmonyos-guides/app-configuration-file.md#configuration标签)：该标签是一个profile文件资源，用于指定描述应用字体大小跟随系统变更的配置文件。在开发视图的“AppScope/resources/base/profile”下面定义配置文件configuration.json。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/JeSUMZ-IQ9uH3gvoxMPADw/zh-cn_image_0000002628789244.png "点击放大")

  同时需要在[AppScope/app.json5](../harmonyos-guides/app-configuration-file.md)中配置configuration标签后，该标签才能生效。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/YDRMzKrUR4ixXYuqNtX-qA/zh-cn_image_0000002628629344.png)
* 影响字体大小的另一个重要因素就是像素单位，ArkUI支持如下[四种像素单位](../harmonyos-references/ts-pixel-units.md)。
  + 应用字体默认像素单位为fp，配置过configuration标签之后，应用字体大小就会跟随系统变化。
  + 当应用字体像素为其它非fp单位时，应用字体大小不随configuration标签配置而变化。此时，可以[在UIAbility组件中订阅回调](../harmonyos-guides/subscribe-system-environment-variable-changes.md#在uiability组件中订阅回调)，使应用字体跟随系统变化。
* [@ohos.window（窗口）](../harmonyos-references/js-apis-window.md)中提供的[setDefaultDensityEnabled](../harmonyos-references/arkts-apis-window-windowstage.md#setdefaultdensityenabled12)方法可以设置应用显示大小缩放是否跟随系统变化。不调用此接口进行设置，则表示不使用系统默认Density，即应用显示大小缩放默认会跟随系统显示大小变化重新布局。

## 解决方案

| 实现场景 | 实现方式 | 适用场景 |
| --- | --- | --- |
| 方案一 | 1. 跟随：配置configuration标签fontSizeScale参数为followSystem 2. 不跟随：对应页面或者组件块的字体像素单位设置为非fp | 字体大小是否跟随系统 |
| 方案二 | 1. 跟随：设置setDefaultDensityEnabled为false 2. 不跟随：设置setDefaultDensityEnabled为true | 显示大小缩放是否跟随系统 |
| 方案三 | 1. 默认跟随系统 2. Text组件提供了设置文本字重的属性fontweight，可以通过配置enableVariableFontWeight为true，来达到调节组件级字体粗细的目的。 | 字体粗细是否跟随系统 |

1. 字体大小是否跟随系统实施方案。
   * 设置字体大小不随系统变化的功能。

     默认情况下，工程中不会配置configuration标签，因此应用内字体大小默认不跟随系统变化。如果工程中配置了configuration标签的fontSizeScale参数为followSystem，但是想实现特定页面或者组件块的字体大小不跟随系统变化，可以将对应页面或者组件块的字体像素单位设置为非fp，比如.fontSize('12vp')。
   * 设置字体大小跟随系统变化的功能。

     不改变应用默认字体像素单位，即fp，通过配置configuration标签fontSizeScale参数为followSystem，可实现应用字体大小跟随系统变化的能力。

   新建配置文件“AppScope/resources/base/profile/configuration.json”。

   ```json
   {
     "configuration": {
       "fontSizeScale": "followSystem",
       "fontSizeMaxScale": "3.2"
     }
   }
   ```

   在“AppScope/app.json5”文件中引用该配置。

   ```json
   {
     "app": {
       "bundleName": "com.example.q202410164817582",
       "vendor": "example",
       "versionCode": 1000000,
       "versionName": "1.0.0",
       "icon": "$media:layered_image",
       "label": "$string:app_name",
       // 在此处引用
       "configuration": "$profile:configuration"
     }
   }
   ```

   注意：如需要监听系统缩放比例系数来修改应用内字体大小，参考：[如何获取系统缩放比例系数来修改应用内字体大小](../best-practices/bpta-custom-font-settings.md#section1079883442818)。

   效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/2n3lEYexQaWlMGpk4e_ixw/zh-cn_image_0000002658988567.gif "点击放大")
2. 显示大小缩放是否跟随系统实施方案。
   * 设置应用显示大小缩放不跟随系统变化的功能。

     通过使用窗口方法，设置[setDefaultDensityEnabled](../harmonyos-references/arkts-apis-window-windowstage.md#setdefaultdensityenabled12)为true，使得窗口不跟随系统显示大小变化重新布局。
   * 设置应用显示大小缩放跟随系统变化的功能。

     应用显示大小缩放默认会跟随系统显示大小变化重新布局，如果使用了[setDefaultDensityEnabled](../harmonyos-references/arkts-apis-window-windowstage.md#setdefaultdensityenabled12)接口，设置setDefaultDensityEnabled为false即可。
3. 字体粗细是否跟随系统实施方案。

   应用内字体粗细默认跟随系统字体粗细变化，目前暂无应用级接口设置字体粗细不跟随系统变化。

   [Text](../harmonyos-references/ts-basic-components-text.md#接口)组件提供了设置文本字重的属性[fontweight](../harmonyos-references/ts-basic-components-text.md#fontweight12)，可以通过配置[enableVariableFontWeight](../harmonyos-references/ts-text-common.md#fontsettingoptions12对象说明)为true，来达到调节组件级字体粗细的目的。

## 常见FAQ

Q：设置字体大小跟随系统变化后，两个Text的字体分别设置成.fontSize(40)与.fontSize('40fp')，在系统设置中调整字体大小，为什么两个Text大小一致？

A：字体像素fp大小默认情况下与vp相同，即默认情况下1fp=1vp。如果用户在设置中选择了更大的字体，字体的实际显示大小就会在vp的基础上乘以scale系数，即1fp=1vp\*scale。但fontSize为number类型时，使用的是fp单位，具体可参考[fontSize](../harmonyos-references/ts-basic-components-text.md#fontsize)。

Q：系统的字体设置是否仅限于主题样式中进行？

A：系统的字体设置仅可在“桌面与个性化”中的“字体样式”选项中进行调整。

Q：如何通过开关来动态配置应用的字体大小是否与系统设置同步，当开关开启时，应用字体大小将根据系统设置进行缩放；当开关关闭时，应用将采用一个独立的全局字体缩放系数，并忽略系统设置的变化？

A：通过configuration标签设置完成跟随系统后，无法通过API来修改不跟随系统变化，只能单独设置字体属性来实现不跟随系统，没有全局设置方式。如果想利用全局设置字体大小来覆盖跟随系统变化，则需要利用setFontSizeScale方法来实现，但是设置完成后应用字体将不跟随系统变化，不再支持订阅系统字体大小变化，所以无法继续打开开关来实现跟随系统变化。验证代码如下：

```ts
import { EnvironmentCallback, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    let envCallback: EnvironmentCallback = {
      onConfigurationUpdated(config) {
        let systemFontSize = config.fontSizeScale;
        // 系统字体大小存储到AppStorage
        AppStorage.setOrCreate('systemFontSize', systemFontSize);
        console.info(`systemFontSize: ${systemFontSize}`);
      },
      onMemoryLevel(level) {
        console.info(`onMemoryLevel level: ${level}`);
      }
    };
    try {
      let applicationContext = this.context.getApplicationContext();
      let callbackId = applicationContext.on('environment', envCallback);
      console.info(`callbackId: ${callbackId}`);
    } catch (paramError) {
      console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
    }
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      AppStorage.setOrCreate('context', this.context);
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
};
```

```ts
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @StorageLink('systemFontSize') systemFontSize: number = 0;
  @StorageLink('isFollow') isFollow: boolean = true;
  @StorageLink('context') context: common.Context | undefined = undefined;

  build() {
    Column() {
      Button('切换跟随全局字体大小')
        .onClick(() => {
          if (this.isFollow) {
            // 切换成不跟随
            this.context?.getApplicationContext().setFontSizeScale(2);
            AppStorage.setOrCreate('isFollow', false);
          } else {
            // 切换成跟随
            // 设置setFontSizeScale以后就无法监听到系统字体变化了，所以这里设置失败
            this.context?.getApplicationContext().setFontSizeScale(this.systemFontSize);
            AppStorage.setOrCreate('isFollow', true);
          }
        });
      Text('Hello World');
      Text('Hello World').fontSize('50vp');
      Text('跟随系统倍数：' + this.systemFontSize);
    }
    .padding({
      top: 100,
    })
    .size({ width: '100%', height: '100%' })
    .backgroundColor('#0d000000');
  }
}
```
