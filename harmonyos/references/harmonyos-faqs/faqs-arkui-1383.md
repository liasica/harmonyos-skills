---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1383
title: 基于单选框的深浅色模式切换失败
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 基于单选框的深浅色模式切换失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b6ac6d97c776a03a1e9d83d5c9981992a8fbf7f430b6f50b40ce223dfa636875
---

## 问题现象

在通过单选框交互实现深浅色主题实时切换的过程中，界面行为异常。具体操作和现象如下：从浅色模式时切换到深色模式时，浅色模式的Radio仍显示为选中状态，而深色模式的Radio无法选中，但实际已经切换成深色模式了。

问题代码如下：

```ts
import { hilog } from '@kit.PerformanceAnalysisKit';
import { ConfigurationConstant } from '@kit.AbilityKit';

@Entry
@Component
struct RadioButton {
  build() {
    Column() {
      List() {
        ListItem({ style: ListItemStyle.CARD }) {
          Row() {
            Column() {
              Text('使用浅色模式')
                .fontColor(Color.White);
            };

            Column() {
              Radio({ value: 'lightMode', group: 'colorModeRadioGroup' })
                .checked(true)
                .onChange((isChecked: boolean) => {
                  hilog.info(0x0002, '浅色模式Radio', 'isChecked:%{public}s', isChecked);
                  this.onColorModeCheckboxStateChange(!isChecked);
                });
            };
          };
        }.width('92%')
        .margin({ top: 16 })
        .backgroundColor('#0A59F7')
        .borderRadius(20);

        ListItem({ style: ListItemStyle.CARD }) {
          Row() {
            Column() {
              Text('使用深色模式')
                .fontColor(Color.White);
            };

            Column() {
              Radio({ value: 'darkMode', group: 'colorModeRadioGroup' })
                .checked(false)
                .onChange((isChecked: boolean) => {
                  hilog.info(0x0002, '深色模式Radio', 'isChecked:%{public}s', isChecked);
                });
            };
          };
        }
        .width('92%')
        .margin({ top: 16 })
        .backgroundColor('#0A59F7')
        .borderRadius(20);
      };
    }
    .height('100%')
    .width('100%');
  }

  onColorModeCheckboxStateChange(changedPropertyName: boolean) {
    hilog.info(0x0002, 'onColorModeCheckboxStateChange', '颜色模式即将改为:%{public}s', changedPropertyName);
    if (changedPropertyName) {
      this.getUIContext()
        .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT);
    } else {
      this.getUIContext()
        .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
    }
  }
}
```

问题现象如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/xzvUchScRqa9HAmODE6w_Q/zh-cn_image_0000002628602660.png "点击放大")

## 背景知识

[Radio](../harmonyos-guides/arkts-common-components-radio-button.md)是单选框组件，通常用于提供相应的用户交互选择项，同一组的Radio中只有一个可以被选中。

## 问题定位

通过分析问题代码可知：

* 当调用[setColorMode](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#setcolormode18)切换颜色模式时，组件重新渲染，通过属性[checked](../harmonyos-references/ts-basic-components-radio.md#checked)强制重置状态。
* [onChange](../harmonyos-references/ts-basic-components-radio.md#onchange)回调被频繁触发，但isChecked的值与实际颜色模式不一致。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/jTiRDiDoQgSkqCESwR_y2w/zh-cn_image_0000002658841931.png "点击放大")
* 切换到深色模式后，Radio.checked仍为true，状态冲突。

代码逻辑分析：

* 硬编码的checked属性：Radio.checked的值始终为固定值，未与颜色模式状态动态绑定。组件重新渲染时，checked被强制重置为硬编码值，导致状态冲突。

  ```ts
  Radio({ value: 'lightMode', group: 'colorModeRadioGroup' }).checked(true)
  Radio({ value: 'darkMode', group: 'colorModeRadioGroup' }).checked(false)
  ```
* onChange回调逻辑错误：!isChecked导致逻辑反转，用户点击浅色模式的Radio会切换到深色模式，但界面刷新后checked被重置为true，形成状态冲突。onChange回调被反复触发，导致无限循环。

  ```ts
  .onChange((isChecked: boolean) => {
    this.onColorModeCheckboxStateChange(!isChecked);
  })
  ```

## 分析结论

由于调用this.getUIContext().getHostContext()?.getApplicationContext().setColorMode()刷新界面深浅模式时，会触发组件重新渲染；而Radio组件的check()属性被硬编码为固定值，导致其选中状态在界面刷新后被强制重置，从而引发onChange回调频繁触发，切换深色模式后浅色模式的Radio组件状态同步异常。

## 修改建议

原始问题的核心是Radio的属性checked被硬编码，导致状态无法同步。可通过@State装饰器将isChecked与UI动态绑定，代码如下：

* this.isChecked控制浅色模式的选中状态。
* !this.isChecked控制深色模式的选中状态，两者互斥。
* 避免硬编码，确保Radio.checked始终与状态同步。

```ts
Radio({ value: 'lightMode', group: 'colorModeRadioGroup' })
  .checked(this.isChecked)
```

```ts
Radio({ value: 'darkMode', group: 'colorModeRadioGroup' })
  .checked(!this.isChecked)
```

完整代码如下：

```ts
import { hilog } from '@kit.PerformanceAnalysisKit';
import { ConfigurationConstant } from '@kit.AbilityKit';

@Entry
@Component
struct RadioButton {
  @State isChecked: boolean = true;

  onColorModeCheckboxStateChange(changedPropertyName: boolean) {
    hilog.info(0x0002, 'onColorModeCheckboxStateChange', '颜色模式即将改为:%{public}s', changedPropertyName);
    if (changedPropertyName) {
      this.getUIContext()
        .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT);
    } else {
      this.getUIContext()
        .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
    }
  }

  build() {
    RelativeContainer() {
      List() {
        ListItem({ style: ListItemStyle.CARD }) {
          Row() {
            Column() {
              Text('使用浅色模式')
                .fontColor(Color.White);
            };

            Column() {
              Radio({ value: 'lightMode', group: 'colorModeRadioGroup' })
                .checked(this.isChecked)
                .onChange((isChecked: boolean) => {
                  this.isChecked = isChecked;
                  hilog.info(0x0002, '浅色模式Radio', 'isChecked:%{public}s', isChecked);
                  this.onColorModeCheckboxStateChange(isChecked);
                });
            };
          };
        }
        .margin({ top: 16 })
        .width('92%')
        .backgroundColor(this.isChecked ? '#0A59F7' : '#317AF7')
        .borderRadius(35);

        ListItem({ style: ListItemStyle.CARD }) {
          Row() {
            Column() {
              Text('使用深色模式')
                .fontColor(Color.White);
            };

            Column() {
              Radio({ value: 'darkMode', group: 'colorModeRadioGroup' })
                .checked(!this.isChecked)
                .onChange((isChecked: boolean) => {
                  hilog.info(0x0002, '深色模式Radio', 'isChecked:%{public}s', isChecked);
                });
            };
          };
        }
        .width('92%')
        .margin({ top: 16 })
        .backgroundColor(this.isChecked ? '#0A59F7' : '#317AF7')
        .borderRadius(35);
      };
    }
    .height('100%')
    .width('100%');
  }
}
```

修正效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/DYNJIA24Spydl48hUWzWeQ/zh-cn_image_0000002628762562.png "点击放大")
