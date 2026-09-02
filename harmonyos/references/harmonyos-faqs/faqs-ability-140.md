---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-140
title: 在设置中修改字体大小和显示缩放大小后，应用页面布局异常
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 在设置中修改字体大小和显示缩放大小后，应用页面布局异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1bba8cfb46982ce4fa20e6d8932b295c1979c061fafb139b2b35cf84611adf9a
---

## 问题现象

在设备设置中，修改字体大小以及显示大小缩放后，页面中布局出现异常（如出现组件间遮挡、截断、布局错乱等问题）。

## 背景知识

* [订阅环境变量](../harmonyos-guides/subscribe-system-environment-variable-changes.md#订阅环境变量)：系统配置的变化通常由“设置”中的选项或“控制中心”中的图标触发。订阅环境变量变化，可以使应用程序更加智能地响应系统环境变化，从而提供更好的用户体验。
* [configuration标签](../harmonyos-guides/app-configuration-file.md#configuration标签)：可以在app.json5配置文件中通过configuration标签，配置应用字体大小是否跟随系统变更以及应用字体最大放大倍数。
* [Configuration](../harmonyos-references/js-apis-app-ability-configuration.md#configuration)：定义了应用运行时的环境变量，包含语言、深浅色、屏幕方向、字体等。其中fontSizeScale表示字体大小缩放比例，受设置中的字体大小影响；screenDensity表示屏幕像素密度，受设置中的显示大小缩放影响。
* [支持适老化](../harmonyos-guides/arkui-support-for-aging-adaptation.md)：系统字体被放大后，应用应确保整体布局不出现错乱，组件不出现重叠。可以根据业务需要限制跟随的字体最大档位、改变布局来更好的适配更大字体等。
* [maxFontScale](../harmonyos-references/ts-basic-components-text.md#maxfontscale12)：设置文本最大的字体缩放倍数。
* [densityUpdate](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#ondensityupdate12)监听事件：监听屏幕像素密度变化。当设置中的显示大小缩放变化后，[屏幕实例](../harmonyos-references/js-apis-display.md#display)中的densityDPI会随之变化。
* [onSizeChange](../harmonyos-references/ts-universal-component-size-change-event.md#onsizechange)：组件尺寸变化事件。组件区域变化时触发该回调。仅会响应由布局变化所导致的组件尺寸发生变化时的回调。

## 问题定位

* 排查是否订阅环境变量。排查使用[onConfigurationUpdate](../harmonyos-references/js-apis-app-ability-ability.md#abilityonconfigurationupdate)回调方法中，根据fontSizeScale、screenDensity属性全局调整应用页面布局（推荐应用采用响应式布局并在该方法中更新断点）。
* 排查是否限制字体大小，以及数值是否合理。排查app.json5文件中configuration字段指向的资源文件中，是否存在fontSizeMaxScale字段，并检查该值是否合适。排查组件是否设置maxFontScale属性以及其数值是否合适。
* 排查是否订阅环境变量、densityUpdate事件，并在调整页面布局。排查是否监听onSizeChange事件，并在其中调整页面布局。

## 分析结论

* 应用未订阅环境变量，并根据环境变量中字体缩放倍数和屏幕像素密度对页面布局进行调整适应，导致页面布局出现异常情况。
* 应用未限制显示的字体缩放倍数或者配置的字体最大或最小缩放倍数不合适，在改变了系统字体大小和显示缩放大小后，出现字体超出容器显示或者超出背景区域的情况，导致布局异常。
* 应用未监听屏幕像素密度变化并调整页面布局，也未对某个组件添加onSizeChange事件并调整组件大小布局。导致调整显示大小缩放后，页面组件布局不符合预期，布局异常。

## 修改建议

* 如果需要全局对该情况进行适配，推荐参考[应用适配适老化大字体](../harmonyos-guides/arkui-support-for-aging-adaptation.md#应用适配适老化大字体)、[响应式布局](../best-practices/bpta-multi-device-responsive-layout.md)以及[限定词目录](../harmonyos-guides/resource-categories-and-access.md#限定词目录)，使用适配不同屏幕DPI的资源文件管理页面布局，并在onConfigurationUpdate中调整断点和布局。

  ```ts
  onConfigurationUpdate(newConfig: Configuration): void {
    console.info(`[ConfigurationChange], config: ${JSON.stringify(newConfig)}`);
    AppStorage.setOrCreate('FontSizeScale', newConfig.fontSizeScale); // 字体缩放比例
    AppStorage.setOrCreate('ScreenDensity', newConfig.screenDensity); // 屏幕像素密度

    // 如果应用采用响应式布局，可以根据字体缩放比例和屏幕像素密度更新断点
    // 或者根据fontSizeScale、screenDensity的值直接调整页面布局（限制组件宽高、换行显示、超出省略等方案）
  }
  ```
* 限制字体缩放倍数，保证字体相关布局正常。
  + 如果仅仅是对特定某个组件中的字体大小进行限制，推荐采用maxFontScale属性，设置字体最大缩放倍数。保证页面布局正常。

    ```ts
    @Component
    export struct MaxScale {
      build() {
        Column() {
          // 只会限制字体大小，实际显示效果还是会受到显示缩放大小的影响
          Text('限制字体最大缩放倍数')
            .maxFontScale(1.15)
        }
      }
    }
    ```
  + 在app.json5文件中，修改configuration标签指向的资源文件，配置fontSizeMaxScale设置应用字体最大缩放倍数。示例配置如下，限制字体最大缩放倍数为1.45。

    ```json
    {
      "configuration": {
        "fontSizeScale": "followSystem",
        "fontSizeMaxScale": "1.45"
      }
    }
    ```
  + 如果有需要的话，可以配置应用字体不跟随系统设置变化，在应用内自行统一管理字体。可以参考[应用内字体大小调节功能](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-SetAppFontSize)。
* 订阅相关事件，并在其中限制组件大小、调整页面布局，如订阅环境变量关注屏幕显示密度、添加densityUpdate或onSizeChange监听事件。

  ```ts
  import { display, uiObserver, window } from '@kit.ArkUI';
  import { BusinessError } from '@ohos.base';

  @Component
  export struct DensityUpdateTest {
    parentPadding: number = 12; // 左右边距
    // 限制组件最大宽度
    @State maxWidth: number =
      (this.getUIContext().px2vp(display.getDefaultDisplaySync().width) / 2 - this.parentPadding) / 2;

    aboutToAppear(): void {
      this.getUIContext()
        .getUIObserver()
        .on('densityUpdate', (info: uiObserver.DensityInfo) => {
          // 如果采用了响应式布局，可以直接更新断点，根据断点调整布局
          console.info('[densityChange]', `current width breakpoint:`, this.getUIContext().getWindowWidthBreakpoint());

          // 也可以根据density数据计算组件大小，调整布局
          // vp和pv转换公式：`vp = px / (DPI/160)` 和`info.density`相关
          // 建议直接通过UIContext的px2vp或vp2px方法转换
          console.info('[densityChange]', `current density: ${info.density}`);

          // 此处仅为示例，可以根据实际需要选择合适布局调整方案
          // 获取窗口宽度，并调整组件的最大宽度
          window.getLastWindow(this.getUIContext().getHostContext(), (err: BusinessError, windowClass: window.Window) => {
            let windowWidth = this.getUIContext().px2vp(windowClass.getGlobalRect().width);
            // 设置组件最大宽度，为(窗口左半-边距)/2，左侧组件占一半，右侧组件的一半宽度也不能超过该值
            this.maxWidth = (windowWidth / 2 - this.parentPadding) / 2;
          });
        });
    }

    build() {
      Column() {
        Column() {
          Stack() {
            Row() {
              Text('布局测试-偏左')
                .backgroundColor('#ff92f1b0')
                .constraintSize({ maxWidth: this.maxWidth }) // 限制最大宽度
            }
            .width('100%')
            .onSizeChange((oldSize, newSize) => {
              // 也可以在onSizeChange事件中调整布局
              console.info('[CompSizeChange]', oldSize.width, newSize.width);
            })

            Row() {
              Text('布局测试-居中')
                .backgroundColor('#ffffcfcf')
                .constraintSize({ maxWidth: this.maxWidth * 2 }) // 限制最大宽度
            }
          }
          .padding({
            left: this.parentPadding,
            right: this.parentPadding
          })
        }
        .width('100%')
      }
      .width('100%')
      .padding({
        top: 50,
        bottom: 30
      })
    }
  }
  ```

完整示例参考如下：

* “ets/entryability/EntryAbility.ets”文件。

  ```ts
  import { AbilityConstant, Configuration, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { window } from '@kit.ArkUI';

  const DOMAIN = 0x0000;

  export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      try {
        this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
      } catch (err) {
        hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
      }
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
      hilog.info(DOMAIN, 'testTag', '%{public}s', JSON.stringify(launchParam));
    }

    onDestroy(): void {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
    }

    onWindowStageCreate(windowStage: window.WindowStage): void {
      // Main window is created, set main page for this ability
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

      windowStage.loadContent('pages/LayoutTest', (err) => {
        if (err.code) {
          hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
          return;
        }
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

    onConfigurationUpdate(newConfig: Configuration): void {
      console.info(`[ConfigurationChange], config: ${JSON.stringify(newConfig)}`);
      AppStorage.setOrCreate('FontSizeScale', newConfig.fontSizeScale); // 字体缩放比例
      AppStorage.setOrCreate('ScreenDensity', newConfig.screenDensity); // 屏幕像素密度

      // 如果应用采用响应式布局，可以根据字体缩放比例和屏幕像素密度更新断点
      // 或者根据fontSizeScale、screenDensity的值直接调整页面布局（限制组件宽高、换行显示、超出省略等方案）
    }
  }
  ```
* “ets/pages/LayoutTest.ets”文件。

  ```ts
  import { DensityUpdateTest } from '../component/DensityUpdateTest';
  import { MaxScale } from '../component/MaxScaleTest';

  @Entry
  @Component
  struct LayoutTest {
    build() {
      Column() {
        DensityUpdateTest()
        MaxScale()
      }
    }
  }
  ```
* “ets/component/DensityUpdateTest.ets”文件。

  ```ts
  import { display, uiObserver, window } from '@kit.ArkUI';
  import { BusinessError } from '@ohos.base';

  @Component
  export struct DensityUpdateTest {
    parentPadding: number = 12; // 左右边距
    // 限制组件最大宽度
    @State maxWidth: number =
      (this.getUIContext().px2vp(display.getDefaultDisplaySync().width) / 2 - this.parentPadding) / 2;

    aboutToAppear(): void {
      this.getUIContext()
        .getUIObserver()
        .on('densityUpdate', (info: uiObserver.DensityInfo) => {
          // 如果采用了响应式布局，可以直接更新断点，根据断点调整布局
          console.info('[densityChange]', `current width breakpoint:`, this.getUIContext().getWindowWidthBreakpoint());

          // 也可以根据density数据计算组件大小，调整布局
          // vp和pv转换公式：`vp = px / (DPI/160)` 和`info.density`相关
          // 建议直接通过UIContext的px2vp或vp2px方法转换
          console.info('[densityChange]', `current density: ${info.density}`);

          // 此处仅为示例，可以根据实际需要选择合适布局调整方案
          // 获取窗口宽度，并调整组件的最大宽度
          window.getLastWindow(this.getUIContext().getHostContext(), (err: BusinessError, windowClass: window.Window) => {
            let windowWidth = this.getUIContext().px2vp(windowClass.getGlobalRect().width);
            // 设置组件最大宽度，为(窗口左半-边距)/2，左侧组件占一半，右侧组件的一半宽度也不能超过该值
            this.maxWidth = (windowWidth / 2 - this.parentPadding) / 2;
          });
        });
    }

    build() {
      Column() {
        Column() {
          Stack() {
            Row() {
              Text('布局测试-偏左')
                .backgroundColor('#ff92f1b0')
                .constraintSize({ maxWidth: this.maxWidth }) // 限制最大宽度
            }
            .width('100%')
            .onSizeChange((oldSize, newSize) => {
              // 也可以在onSizeChange事件中调整布局
              console.info('[CompSizeChange]', oldSize.width, newSize.width);
            })

            Row() {
              Text('布局测试-居中')
                .backgroundColor('#ffffcfcf')
                .constraintSize({ maxWidth: this.maxWidth * 2 }) // 限制最大宽度
            }
          }
          .padding({
            left: this.parentPadding,
            right: this.parentPadding
          })
        }
        .width('100%')
      }
      .width('100%')
      .padding({
        top: 50,
        bottom: 30
      })
    }
  }
  ```
* “ets/component/MaxScaleTest.ets”文件。

  ```ts
  @Component
  export struct MaxScale {
    build() {
      Column() {
        // 只会限制字体大小，实际显示效果还是会受到显示缩放大小的影响
        Text('限制字体最大缩放倍数')
          .maxFontScale(1.15)
      }
    }
  }
  ```
