---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-27
title: 如何实现屏幕亮度自动调整或自定义调整
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何实现屏幕亮度自动调整或自定义调整
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:e3ca922c1946eb2991c05b4974637ef197d7b7d6d3b11ef265b57ba61b654649
---

## 问题现象

如何调整屏幕亮度，并且获取屏幕亮度值？是否有相关场景的示例代码，如：实现打开一个页面亮度最大，关闭页面时亮度恢复系统默认？

## 背景知识

* @system.brightness (屏幕亮度)模块已经停止维护，其替代接口在[@ohos.settings](../harmonyos-references/js-apis-settings.md)模块中实现，此模块大部分能力仅对系统应用开放。
* @ohos.settings提供了设置、读取数据项的接口，通过指定[display](../harmonyos-references/js-apis-settings.md#display)相关的数据项SCREEN\_BRIGHTNESS\_STATUS可以设置设备显示亮度，亮度取值范围为0到255。
  + [settings.setValue](../harmonyos-references/js-apis-settings.md#settingssetvalue10)可用来设置显示亮度。
  + [settings.getValueSync](../harmonyos-references/js-apis-settings.md#settingsgetvaluesync10)可以获取当前设备亮度值。
* [@ohos.window](../harmonyos-references/js-apis-window.md)模块提供管理窗口的一些基础能力，包括对**当前应用屏幕亮度**的调整（@ohos.settings是对整个设备亮度调整）。
  + [setWindowBrightness](../harmonyos-references/arkts-apis-window-window.md#setwindowbrightness9)可以设置屏幕亮度，屏幕亮度调节范围为[0.0,1.0]或-1.0。1.0表示最亮，-1.0表示跟随系统亮度。
  + [getWindowProperties](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)接口可获取当前窗口的属性，其中包含当前应用的屏幕亮度信息。
* [settings.registerKeyObserver](../harmonyos-references/js-apis-settings.md#settingsregisterkeyobserver11)用于在指定上下文中注册一个观察者，以便在指定域名中观察指定的数据项。当该数据项的值发生变化时，将调用注册的回调函数。成功注册返回true，否则返回false。可以监听系统亮度变化。

## 解决方案

定义Brightness类。

* 在**getScreenBrightness**方法中，使用window.getLastWindow获取当前窗口对象，通过currentWindow.getWindowProperties获取当前窗口的属性，最后返回窗口属性的brightness值，即可获取当前屏幕亮度。
* 在**setScreenBrightness**方法中，使用window.getLastWindow获取当前窗口对象，通过currentWindow.setWindowBrightness(brightness)即可设置当前窗口的亮度。BrightnessUtil.ets文件代码如下：

  ```ts
  import { window } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';

  export default class Brightness {
    static async getScreenBrightness(ctx: Context): Promise<number> {
      try {
        const currentWindow = await window.getLastWindow(ctx);
        let properties = currentWindow.getWindowProperties(); // 获取当前窗口属性
        return properties.brightness;
      } catch (exception) {
        console.error(`Failed to getScreenBrightness. Cause code: ${exception.code}, message: ${exception.message}`);
      }
      return -1;
    }

    static setScreenBrightness(ctx: Context, brightness: number) {
      window.getLastWindow(ctx).then(currentWindow => {
        currentWindow.setWindowBrightness(brightness).catch((err: BusinessError) => {
          console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
        });
      }).catch((err: BusinessError) => {
        console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
      });
    }
  };
  ```

* 在Brightness类中，封装获取亮度、设置亮度方法的作用是捕获亮度调节过程中可能出现的错误并进行异常处理，以及便于多个UI界面需要调节亮度时直接调用。

以下为两种常见屏幕亮度调节场景示例：

* 场景一：出示二维码时屏幕自动调整为最大亮度。

  具体实现为在PageA主页面中跟随系统亮度，跳转PageB页面后设备亮度调至最大（在aboutToAppear中设置最亮），关闭PageB后亮度恢复默认值（在aboutToDisappear中设置跟随系统亮度）。
  + PageA页面：导入Brightness类，用于获取屏幕亮度，在Button组件中使用Brightness.getScreenBrightness方法获取当前屏幕亮度。

    PageA.ets页面代码如下：@Entry页面需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

    ```ts
    // 导入定义Brightness类
    import Brightness from '../utils/BrightnessUtil';
    import { settings } from '@kit.BasicServicesKit';

    @Entry
    @Component
    struct PageA {
      @State screenBrightness: number = 0; // 屏幕亮度
      @State deviceBrightness: string = ''; // 设备亮度
      context: Context = this.getUIContext().getHostContext()!;

      onPageShow() {
        setTimeout(async () => {
          const context: Context = this.getUIContext().getHostContext()!;
          this.screenBrightness = await Brightness.getScreenBrightness(context);
          this.deviceBrightness = settings.getValueSync(context, settings.display.SCREEN_BRIGHTNESS_STATUS, '10');
        }, 500);
      }

      build() {
        Column({ space: 20 }) {
          Text(`当前屏幕亮度: ${this.screenBrightness}`);
          Text(`当前设备亮度: ${this.deviceBrightness}`);
          Button(`click to PageB.`)
            .onClick(() => this.getUIContext().getRouter().pushUrl({ url: 'pages/PageB' }));
          Button('click to get brightness')
            .onClick(async () => {
              this.screenBrightness = await Brightness.getScreenBrightness(this.context);
              this.deviceBrightness = settings.getValueSync(this.context, settings.display.SCREEN_BRIGHTNESS_STATUS, '10');
            });
        }.width('100%').height('100%')
        .alignItems(HorizontalAlign.Center);
      }
    }
    ```
  + PageB页面：在aboutToAppear和aboutToDisappear中设置屏幕亮度，即可实现出示和关闭二维码时亮度自动调节的功能。

    PageB.ets页面代码如下：@Entry页面需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

    ```ts
    // 导入定义Brightness类
    import Brightness from '../utils/BrightnessUtil';
    import { settings } from '@kit.BasicServicesKit';

    @Entry
    @Component
    struct PageB {
      @State screenBrightness: number = 0;
      @State deviceBrightness: string = ''; // 设备亮度
      context: Context = this.getUIContext().getHostContext()!;

      aboutToAppear(): void {
        Brightness.setScreenBrightness(this.context, 1); // 设置亮度最大
      }

      aboutToDisappear(): void {
        Brightness.setScreenBrightness(this.context, -1); // 跟随系统亮度
      }

      build() {
        Column({ space: 20 }) {
          Text(`当前屏幕亮度: ${this.screenBrightness}`);
          Text(`当前设备亮度: ${this.deviceBrightness}`);
          Button('返回PageA')
            .onClick(() => this.getUIContext().getRouter().back());
          Button('click to get brightness')
            .onClick(async () => {
              this.screenBrightness = await Brightness.getScreenBrightness(this.context);
              this.deviceBrightness = settings.getValueSync(this.context, settings.display.SCREEN_BRIGHTNESS_STATUS, '10');
            });
        }.width('100%').height('100%')
        .alignItems(HorizontalAlign.Center);
      }
    }
    ```
  + 效果预览：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/CGVCC7X0QmuDOGf3Vln7yA/zh-cn_image_0000002717627987.png "点击放大")
* 场景二：小说软件自定义调整阅读界面的亮度，并且在退出阅读界面后恢复系统设置的亮度。

  具体实现为滑动条控制屏幕亮度，并获取当前屏幕亮度。

  + 导入Brightness类，用于获取屏幕亮度，使用Slider组件，定义onChange事件处理函数。
  + 当滑块值改变时，更新inSetValueOne状态变量为当前滑块的值，之后调用Brightness.setScreenBrightness方法，设置屏幕亮度为当前值。
  + 调用Brightness.getScreenBrightness方法，获取当前屏幕亮度，并打印到控制台。

    ReaderPage.ets页面代码如下：@Entry页面需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

    ```ts
    // 导入定义Brightness类
    import Brightness from '../utils/BrightnessUtil';

    @Entry
    @Component
    struct ReaderPage {
      @State inSetValueOne: number = 0;
      context: Context = this.getUIContext().getHostContext()!;

      build() {
        Column({ space: 8 }) {
          Text('调整亮度').fontColor(0xCCCCCC).width('90%');
          Row() {
            Slider({
              value: $$this.inSetValueOne,
              min: 0.0,
              max: 1,
              step: 0.01,
              style: SliderStyle.InSet
            })
              .blockColor(Color.White)
              .trackColor('#F1F3F5')
              .selectedColor('#0A59F7')
              .showTips(true)
              .onChange(async (value: number) => {
                this.inSetValueOne = value;
                Brightness.setScreenBrightness(this.context, value);
                let tmp = await Brightness.getScreenBrightness(this.context);
                console.info(`Succeeded in obtaining brightness. Brightness value :${tmp}`);
              });
          }.width('80%');
        }
        .justifyContent(FlexAlign.End)
        .width('100%')
        .height('100%');
      }
    }
    ```
  + 效果预览：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/MHQAqwhGTk-Q27hQWoXTBw/zh-cn_image_0000002717788201.png "点击放大")

## 常见FAQ

Q：为什么设置亮度后，通过系统下拉框调整设备亮度无效？

A：通过setWindowBrightness自定义亮度后，调整设备亮度不会改变当前应用亮度，重新设置跟随系统亮度setWindowBrightness(-1)即可。

Q：在平板和折叠屏上通过setWindowBrightness设置窗口亮度后，下拉栏调整系统亮度无法改变应用亮度，手机上正常，如何处理？

A：对于非2in1设备（不包含TV设备），在HarmonyOS 6.1.0之前，当前窗口的窗口亮度生效时，控制中心调整系统屏幕亮度不生效。从HarmonyOS 6.1.0开始，当前窗口的窗口亮度生效时，控制中心可以调整系统屏幕亮度，同时会将当前窗口恢复为系统屏幕亮度。请检查设备系统版本，若低于HarmonyOS 6.1.0，需升级至6.1.0及以上版本。

## 总结

通过调整屏幕亮度的方法，实现了两种场景，但两种场景的具体实现的方法略有不同：

* 对于出示二维码的场景，侧重于在二维码页面的生命周期内调整系统亮度使屏幕最亮。
* 而对于小说阅读场景，侧重于能够在应用界面随意调整亮度。
