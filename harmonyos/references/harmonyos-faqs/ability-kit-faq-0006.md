---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ability-kit-faq-0006
title: 字体设置与效果常见问题
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 常见问题 > 字体设置与效果常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:24+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:14e84acf9bb7bec1a76b3cd0abc768c0f62b0e55cad3939f1293879a1ad0d72d
---

**Q：在系统【设置】中，可以调整字体大小、显示大小缩放、字体粗细的字体样式。如何设置应用配置，使应用内字体样式，具备是否跟随系统字体样式变化的能力。**

**A**：

| 实现场景 | 实现方式 | 适用场景 |
| --- | --- | --- |
| 方案一 | 1. 跟随：配置configuration标签fontSizeScale参数为followSystem 2. 不跟随：对应页面或者组件块的字体像素单位设置为非fp | 字体大小是否跟随系统 |
| 方案二 | 1. 跟随：设置setDefaultDensityEnabled为false 2. 不跟随：设置setDefaultDensityEnabled为true | 显示大小缩放是否跟随系统 |
| 方案三 | 1. 默认跟随系统 2. Text组件提供了设置文本字重的属性fontweight，可以通过配置enableVariableFontWeight为true，来达到调节组件级字体粗细的目的。 | 字体粗细是否跟随系统 |

1. 字体大小是否跟随系统实施方案：
   * 设置字体大小不随系统变化的功能：

     默认情况下，工程中不会配置configuration标签，因此应用内字体大小默认不跟随系统变化。如果工程中配置了configuration标签的fontSizeScale参数为followSystem，但是想实现特定页面或者组件块的字体大小不跟随系统变化，可以将对应页面或者组件块的字体像素单位设置为非fp，比如.fontSize('12vp')。
   * 设置字体大小跟随系统变化的功能：

     不改变应用默认字体像素单位，即fp，通过配置configuration标签fontSizeScale参数为followSystem，可实现应用字体大小跟随系统变化的能力。

     新建配置文件"AppScope/resources/base/profile/configuration.json"：

     ```json
     {
       "configuration": {
         "fontSizeScale": "followSystem",
         "fontSizeMaxScale": "3.2"
       }
     }
     ```

     在"AppScope/app.json5"文件中引用该配置：

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/SCN1ZC50SHekIKVjoOecKw/zh-cn_image_0000002795443137.png "点击放大")
2. 显示大小缩放是否跟随系统实施方案：
   * 设置应用显示大小缩放不跟随系统变化的功能：

     通过使用窗口方法，设置[setDefaultDensityEnabled](../harmonyos-references/arkts-apis-window-windowstage.md#setdefaultdensityenabled12)为true，使得窗口不跟随系统显示大小变化重新布局。
   * 设置应用显示大小缩放跟随系统变化的功能：

     应用显示大小缩放默认会跟随系统显示大小变化重新布局，如果使用了[setDefaultDensityEnabled](../harmonyos-references/arkts-apis-window-windowstage.md#setdefaultdensityenabled12)接口，设置setDefaultDensityEnabled为false即可。
3. 字体粗细是否跟随系统实施方案：

   应用内字体粗细默认跟随系统字体粗细变化，目前暂无应用级接口设置字体粗细不跟随系统变化。

   [Text](../harmonyos-references/ts-basic-components-text.md#接口)组件提供了设置文本字重的属性[fontweight](../harmonyos-references/ts-basic-components-text.md#fontweight12)，可以通过配置[enableVariableFontWeight](../harmonyos-references/ts-text-common.md#fontsettingoptions12对象说明)为true，来达到调节组件级字体粗细的目的。

**Q：设置字体大小跟随系统变化后，两个Text的字体分别设置成.fontSize(40)与.fontSize('40fp')，在系统设置中调整字体大小，为什么两个Text大小一致？**

**A**：字体像素fp大小默认情况下与vp相同，即默认情况下1fp=1vp。如果用户在设置中选择了更大的字体，字体的实际显示大小就会在vp的基础上乘以scale系数，即1fp=1vp\*scale。但fontSize为number类型时，使用的是fp单位，具体可参考[fontSize](../harmonyos-references/ts-basic-components-text.md#fontsize)。

**Q：系统的字体设置是否仅限于主题样式中进行？**

**A**：系统的字体设置仅可在"桌面与个性化"中的"字体样式"选项中进行调整。

**Q：如何通过开关来动态配置应用的字体大小是否与系统设置同步，当开关开启时，应用字体大小将根据系统设置进行缩放；当开关关闭时，应用将采用一个独立的全局字体缩放系数，并忽略系统设置的变化？**

**A**：通过configuration标签设置完成跟随系统后，无法通过API来修改不跟随系统变化，只能单独设置字体属性来实现不跟随系统，没有全局设置方式。如果想利用全局设置字体大小来覆盖跟随系统变化，则需要利用setFontSizeScale方法来实现，但是设置完成后应用字体将不跟随系统变化，不再支持订阅系统字体大小变化，所以无法继续打开开关来实现跟随系统变化。验证代码如下：

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

可通过[preferences](../harmonyos-references/js-apis-data-preferences.md)持久化用户选择的字体模式，[AppStorage](../harmonyos-guides/arkts-appstorage.md)全局同步当前缩放倍率，[@StorageProp](../harmonyos-guides/arkts-appstorage.md#storageprop)实现组件响应式更新，同时支持"跟随系统"和"自定义倍率"两种模式。实现步骤如下。

1. 定义字体缩放选项模型，包含默认（跟随系统）、极小（0.8）、小（0.9）、标准（1.0）、大（1.2）、极大（1.4）等选项：

   ```ts
   export enum FontScaleMode {
     DEFAULT = 'default',
     MIN = 'min',
     SMALL = 'small',
     STANDARD = 'standard',
     LARGE = 'large',
     MAX = 'max',
   }

   export interface FontScaleOption {
     mode: string;
     label: string;
     scale: number;
   }

   export const FontScaleOptions: FontScaleOption[] = [
     { mode: FontScaleMode.DEFAULT, label: '默认（跟随系统）', scale: 1.0 },
     { mode: FontScaleMode.MIN, label: '极小', scale: 0.8 },
     { mode: FontScaleMode.SMALL, label: '小', scale: 0.9 },
     { mode: FontScaleMode.STANDARD, label: '标准', scale: 1.0 },
     { mode: FontScaleMode.LARGE, label: '大', scale: 1.2 },
     { mode: FontScaleMode.MAX, label: '极大', scale: 1.4 },
   ];

   export function getScaleByMode(mode: string): number {
     const option = FontScaleOptions.find(o => o.mode === mode);
     return option ? option.scale : 1.0;
   }
   ```
2. 通过preferences持久化用户选择的字体模式，AppStorage全局同步当前缩放倍率和模式。当模式为"跟随系统"时使用系统倍率，当模式为"自定义倍率"时使用对应固定倍率：

   ```ts
   import { preferences } from '@kit.ArkData';
   import { FontScaleMode, getScaleByMode } from '../model/FontScaleModel';

   const PREF_NAME = 'font_settings';
   const PREF_KEY_MODE = 'font_scale_mode';
   const STORE_KEY_SCALE = 'currentFontScale';
   const STORE_KEY_MODE = 'fontScaleMode';
   const STORE_KEY_SYSTEM_SCALE = 'systemFontScale';

   export class FontPreferenceUtil {
     private static pref: preferences.Preferences | null = null;

     static async init(context: Context): Promise<void> {
       FontPreferenceUtil.pref = await preferences.getPreferences(context, PREF_NAME);
       const savedMode = await FontPreferenceUtil.pref.get(PREF_KEY_MODE, FontScaleMode.DEFAULT) as string;
       AppStorage.setOrCreate(STORE_KEY_MODE, savedMode);
       AppStorage.setOrCreate(STORE_KEY_SYSTEM_SCALE, 1.0);
       if (savedMode === FontScaleMode.DEFAULT) {
         AppStorage.setOrCreate(STORE_KEY_SCALE, 1.0);
       } else {
         AppStorage.setOrCreate(STORE_KEY_SCALE, getScaleByMode(savedMode));
       }
     }

     static async setMode(mode: string): Promise<void> {
       if (!FontPreferenceUtil.pref) {
         console.error('[FontPreferenceUtil] preferences not initialized');
         return;
       }
       await FontPreferenceUtil.pref.put(PREF_KEY_MODE, mode);
       await FontPreferenceUtil.pref.flush();
       AppStorage.setOrCreate(STORE_KEY_MODE, mode);
       if (mode === FontScaleMode.DEFAULT) {
         const systemScale = AppStorage.get(STORE_KEY_SYSTEM_SCALE) ?? 1.0;
         AppStorage.setOrCreate(STORE_KEY_SCALE, systemScale);
       } else {
         AppStorage.setOrCreate(STORE_KEY_SCALE, getScaleByMode(mode));
       }
     }

     static updateSystemScale(systemScale: number): void {
       AppStorage.setOrCreate(STORE_KEY_SYSTEM_SCALE, systemScale);
       const currentMode = AppStorage.get(STORE_KEY_MODE);
       if (currentMode === FontScaleMode.DEFAULT) {
         AppStorage.setOrCreate(STORE_KEY_SCALE, systemScale);
       }
     }
   }

   export const FONT_SCALE_STORE_KEY = STORE_KEY_SCALE;
   export const FONT_MODE_STORE_KEY = STORE_KEY_MODE;
   ```
3. 在UIAbility的onCreate中初始化字体设置，在onConfigurationUpdate中监听系统字体变化并更新倍率：

   ```ts
   import { UIAbility, AbilityConstant, Want, Configuration } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';
   import { FontPreferenceUtil } from '../utils/FontPreferenceUtil';

   export default class EntryAbility extends UIAbility {
     async onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): Promise<void> {
       await FontPreferenceUtil.init(this.context);
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           console.error(`Failed to load content. code: ${err.code}, message: ${err.message}`);
           return;
         }
         console.info('Succeeded in loading content.');
       });
     }

     onConfigurationUpdate(newConfig: Configuration): void {
       const systemFontScale = newConfig.fontSizeScale ?? 1.0;
       FontPreferenceUtil.updateSystemScale(systemFontScale);
     }
   };
   ```
4. 组件中使用@StorageProp绑定缩放倍率，将基础字号乘以缩放倍率实现字体大小调节：

   ```ts
   import { FONT_SCALE_STORE_KEY } from '../utils/FontPreferenceUtil';

   @Entry
   @Component
   struct Index {
     @StorageProp(FONT_SCALE_STORE_KEY) fontScale: number = 1.0;

     build() {
       Column() {
         Text('标题文字')
           .fontSize(20 * this.fontScale)
           .fontWeight(FontWeight.Bold);
         Text('正文内容')
           .fontSize(16 * this.fontScale)
           .lineHeight(24 * this.fontScale);
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

选择"默认"时，应用字体跟随系统设置变化；选择其他选项时，应用使用固定倍率，不受系统设置影响。

**Q：设置configuration标签fontSizeScale为nonFollowSystem后，字体大小不跟随系统变化了，但字体粗细和大小缩放仍然跟随系统变化，如何处理？**

A：设置configuration标签的fontSizeScale为nonFollowSystem仅控制字体大小不跟随系统变化，不影响字体粗细和显示大小缩放。具体原因及处理方式如下：

1. 字体粗细：应用内字体粗细默认跟随系统字体粗细变化，目前暂无应用级接口设置字体粗细不跟随系统变化。可通过[Text](../harmonyos-references/ts-basic-components-text.md#接口)组件的[fontweight](../harmonyos-references/ts-basic-components-text.md#fontweight12)属性，配置[enableVariableFontWeight](../harmonyos-references/ts-text-common.md#fontsettingoptions12对象说明)为true来调节组件级字体粗细。
2. 显示大小缩放：应用显示大小缩放默认跟随系统显示大小变化重新布局，需通过窗口方法设置[setDefaultDensityEnabled](../harmonyos-references/arkts-apis-window-windowstage.md#setdefaultdensityenabled12)为true，使窗口不跟随系统显示大小变化重新布局。

**Q：当通过linearGradient设置渐变时，默认是背景色的渐变，而非文字渐变的效果。应该如何实现文字渐变？**

**A**：由于linearGradient颜色渐变属于组件内容且绘制在背景上方，若仅对文本应用渐变，效果将作用于背景而非文字本身，其效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/0t1O_14oTcueQY4ALyDsVA/zh-cn_image_0000002766033142.png)

要实现作用在字体上，目前以下实现方式：

1. API20之前：
   * ArkTS侧可以结合blendMode将背景色裁掉。通过混合模式（BlendMode）可以指定当前像素如何与其下方的像素混合，可以用来实现裁切、蒙版、提亮等效果。关于BlendMode的具体使用可以参考：[BlendMode](../harmonyos-references/arkts-apis-graphics-drawing-e.md#blendmode)。

     实现文字渐变的示例如下：

     ```ts
     @Entry
     @Component
     struct Index {
       @State message: string = 'Hello World';

       build() {
         RelativeContainer() {
           Row() {
             Text(this.message)
               .fontSize(24)
               .fontWeight(FontWeight.Bold)
               .blendMode(BlendMode.DST_IN, BlendApplyType.OFFSCREEN)
           }
           .linearGradient({
             direction: GradientDirection.Right,
             colors:
     ```
   * C-API侧，使用方案同上，使用[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)的NODE\_BLEND\_MODE，以及NODE\_LINEAR\_GRADIENT进行设置；
2. API20及以上：
   * 采用ArkTS实现文字渐变，可以使用Text的[shaderStyle](../harmonyos-references/ts-basic-components-text.md#shaderstyle20)属性，直接设置字体的渐变，示例如下：

     ```screen
     @Entry
     @Component
     struct Index {
       @State message: string = 'Hello World';

       build() {
         RelativeContainer() {
           Text(this.message)
             .fontSize(24)
             .fontWeight(FontWeight.Bold)
             .shaderStyle({
               direction: GradientDirection.Right,
               colors: [['#ff0631f5', 0.0], ['#ff922626', 1]]
             })
         }
         .width('100%')
         .height('100%')
       }
     }
     ```
   * 对于使用C-API开发的应用，可以使用[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)的 NODE\_TEXT\_LINEAR\_GRADIENT属性，实现文字渐变。

更多文字效果请参考：[基于Text组件及通用属性实现文字特效](https://gitcode.com/harmonyos_samples/text-effects)。
