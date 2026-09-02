---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-support-for-aging-adaptation
title: 支持适老化
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 无障碍与适老化 > 支持适老化
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:51+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a73d7e69f6c83ea17ef20967d17762ec2f7a5a834ea581336b8cd82ea17d4fc2
---

系统字体被放大后，应用应确保整体布局不出现错乱，组件不出现重叠。可以根据业务需要限制跟随的字体最大档位、改变布局来更好的适配更大字体等。本文旨在指导应用如何跟随系统字体大小和跟随到的最大倍数。

## 应用适配规则

* 在系统使用1.75倍及以上的大字体时，页面布局不得错乱，组件不得叠加，文字不得截断。
* 图标及图片不会随着字体的变大而变化。
* 页面中不重要的内容字体，可采用不跟随系统字体变化或限制字体最大尺寸的方法进行布局。
* 若应用跟随系统字体增大后导致页面内容位置挤压或截断等问题，可采取将X轴扩展至Y轴的措施，例如将左右布局调整为上下布局。
* [系统组件](arkui-support-for-aging-adaptation.md#适配适老化的系统组件及触发方式)已针对适老化大字体进行了单独适配，尽可能在开发过程中使用系统组件。

## 应用适配适老化大字体

1. 开启路径

   在“设置-辅助功能-关怀模式-放大显示”中开启。

   各档位对应参数：

   | 档位 | 字体大小 | 字体粗细 |
   | --- | --- | --- |
   | 标准 | 1倍 | 1倍 |
   | 大1档 | 1.15倍 | 1倍 |
   | 大2档 | 1.3倍 | 1.1倍 |
   | 大3档 | 1.45倍 | 1.1倍 |
   | 大4档 | 1.75倍 | 1.25倍 |
   | 大5档 | 2.0倍 | 1.25倍 |
   | 大6档 | 3.2倍 | 1.25倍 |
2. 适配方法

   当前默认应用不跟随系统字体的变化。如需跟随系统字体变化，并设置最大跟随变化的倍数，请按以下步骤操作：

   * [app.json5配置文件](app-configuration-file.md)适配。

     通过配置"configuration": "$profile:configuration"，指向base/profile/configuration.json文件；

     ```screen
     {
       "app": {
         "bundleName": "com.example.myapplication",
         "vendor": "example",
         "versionCode": 1000000,
         "versionName": "1.0.0",
         "icon": "$media:app_icon",
         "label": "$string:app_name",
         "configuration": "$profile:configuration"
       }
     }
     ```
   * 在base文件目录下新增profile文件夹，并在此目录下新增 configuration.json 文件。

     配置"fontSizeScale": "followSystem"表示该应用的字体大小将根据系统设置进行缩放，"fontSizeMaxScale": "1.3"表示应用字体大小随系统变化的最大缩放比例为1.3倍。

     ```screen
     {
       "configuration": {
         "fontSizeScale": "followSystem",
         "fontSizeMaxScale": "1.3"
       }
     }
     ```
   * 若应用需适应系统字体大小的变化，最大应调整至1.75倍，但部分组件可调整至2倍。

     首先需要按照上述步骤配置"fontSizeMaxScale"为1.75。

     ```screen
     {
       "configuration": {
         "fontSizeScale": "followSystem",
         "fontSizeMaxScale": "1.75"
       }
     }
     ```

     然后，为Text添加maxFontScale属性，传递参数为2，表示该Text组件跟随系统字体大小变化的最大倍数为2倍。

     ```screen
     Text('hello world!')
       .fontSize($r('sys.float.Body_M'))
       .maxFontScale(2)
       .fontColor($r('sys.color.font_secondary'))
     ```

     当Text组件配置了maxFontScale属性时，将采用组件设置的最大放大倍数，而非系统默认的最大放大倍数。
   * 若应用不需要跟随系统字体大小变化，无需配置。
3. 获取字体大小和粗细。

   * 生命周期回调方法[onConfigurationUpdated](../harmonyos-references/js-apis-app-ability-environmentcallback.md#onconfigurationupdated)的config参数可接收字体大小（[fontSizeScale](../harmonyos-references/js-apis-app-ability-configuration.md#configuration)）与字体粗细（[fontWeightScale](../harmonyos-references/js-apis-app-ability-configuration.md#configuration)）。

     注册系统环境变化的监听后，在系统环境变化时可触发回调。
   * 应用冷启动查询系统字体大小档位。

     ```screen
     let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     let fontSizeScale: number = context.config?.fontSizeScale ?? 1;
     ```

## 适配适老化的系统组件及触发方式

适老化提供了一种通过鼠标或手指长按的方法来放大所选区域或组件，即如果系统字体大小大于1倍，当用户使用鼠标或手指长按装配了适老化方法的组件，需要从所选区域的组件中提取数据，并放入另一个弹窗组件中展示。该方法的目的在于使组件和组件内部数据（子组件）放大，同时将整体组件在屏幕中央显示，让用户能够更好的观察该组件。

* 适老化规则

  由于在系统字体大于1倍时，组件并没有默认放大，需要通过配置[configuration标签](app-configuration-file.md#configuration标签)，实现组件放大的适老化功能。
* 如何开启适老化

  进入手机设置，点击辅助功能，开启关怀模式。
* 适老化操作

  在已经支持适老化能力的组件上长按组件，能够触发弹窗，当用户释放时，适老化操作结束。当设置系统字体大于1倍时，组件自动放大，当系统字体恢复至1倍时组件恢复正常状态。
* 适老化对象

  触发适老化操作并提供数据的组件。
* 适老化弹窗目标

  可接收并处理适老化数据的组件。
* 弹窗限制

  当用户将系统字体设置为2倍以上时，弹窗内容包括icon和文字的放大倍数固定为2倍。
* 联合其他能力

  适老化能力可以适配其他能力（如：滑动拖拽）。底部页签（tabBar）组件在触发适老化时，如果用户滑动手指或鼠标可以触发底部页签其他子组件的适老化功能。

| 触发方式 | 组件名称 |
| --- | --- |
| 长按系统组件触发 | [SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)， [底部页签（tabBar）](../harmonyos-references/ts-container-tabcontent.md#tabbar9)，[Navigation](../harmonyos-references/ts-basic-components-navigation.md)，[NavDestination](../harmonyos-references/ts-basic-components-navigation.md#navdestination10)， [Tabs](../harmonyos-references/ts-container-tabs.md) |
| 设置系统字体默认放大 | [PickerDialog](../harmonyos-references/ts-methods-calendarpicker-dialog.md)， [Button](../harmonyos-references/ts-basic-components-button.md)， [Menu](../harmonyos-references/ts-basic-components-menu.md)， [Stepper](../harmonyos-references/ts-basic-components-stepper.md)， [BindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)，[TextInput](../harmonyos-references/ts-basic-components-textinput.md)，[TextArea](../harmonyos-references/ts-basic-components-textarea.md)，[Search](../harmonyos-references/ts-basic-components-search.md)，[SelectionMenu](../harmonyos-references/ohos-arkui-advanced-selectionmenu.md)，[Chip](../harmonyos-references/ohos-arkui-advanced-chip.md)，[Dialog](../harmonyos-references/ohos-arkui-advanced-dialog.md)，[Slider](../harmonyos-references/ts-basic-components-slider.md)， [Progress](../harmonyos-references/ts-basic-components-progress.md)， [Badge](../harmonyos-references/ts-container-badge.md) |

SideBarContainer组件通过长按控制按钮触发适老化弹窗。在系统字体为1倍的情况下，长按控制按钮不能弹窗。在系统字体大于1倍的情况下，长按控制按钮可以弹窗。

```ts
@Entry
@Component
struct SideBarContainerExample {
  @State currentFontSizeScale: number = 1
  normalIcon: Resource = $r("app.media.icon")
  selectedIcon: Resource = $r("app.media.icon")
  @State arr: number[] = [1, 2, 3]
  @State current: number = 1
  @State title: string = 'Index01';

  build() {
    SideBarContainer(SideBarContainerType.Embed) {
      Column() {
        ForEach(this.arr, (item: number) => {
          Column({ space: 5 }) {
            Image(this.current === item ? this.selectedIcon : this.normalIcon).width(64).height(64)
            Text("0" + item)
              .fontSize(25)
              .fontColor(this.current === item ? '#0A59F7' : '#999')
              .fontFamily('source-sans-pro,cursive,sans-serif')
          }
          .onClick(() => {
            this.current = item;
            this.title = "Index0" + item;
          })
        }, (item: string) => item)
      }.width('100%')
      .justifyContent(FlexAlign.SpaceEvenly)
      .backgroundColor($r('sys.color.mask_fifth'))
    }
    .controlButton({
      icons: {
        hidden: $r('sys.media.ohos_ic_public_drawer_open_filled'),
        shown: $r('sys.media.ohos_ic_public_drawer_close')
      }
    })
    .sideBarWidth(150)
    .minSideBarWidth(50)
    .maxSideBarWidth(300)
    .minContentWidth(0)
    .onChange((value: boolean) => {
      console.info('status:' + value)
    })
    .divider({ strokeWidth: '1vp', color: Color.Gray, startMargin: '4vp', endMargin: '4vp' })
  }
}
```

切换系统字体前后长按已经支持适老化能力的组件，有如下效果：

| 系统字体为一倍（适老化能力开启前） | 系统字体为1.75倍（适老化能力开启后） |
| --- | --- |
|  |  |

[TextPickerDialog](../harmonyos-references/ts-methods-textpicker-dialog.md)组件通过设置系统字体大小触发适老化弹窗。在系统字体为1倍的情况下，适老化不触发；在系统字体大于1倍的情况下，适老化触发。

```ts
@Entry
@Component
struct TextPickerExample {
  private select: number | number[] = 0;
  private cascade: TextCascadePickerRangeContent[] = [
    {
      text: '辽宁省',
      children: [{ text: '沈阳市', children: [{ text: '沈河区' }, { text: '和平区' }, { text: '浑南区' }] },
        { text: '大连市', children: [{ text: '中山区' }, { text: '金州区' }, { text: '长海县' }] }]
    },
    {
      text: '吉林省',
      children: [{ text: '长春市', children: [{ text: '南关区' }, { text: '宽城区' }, { text: '朝阳区' }] },
        { text: '四平市', children: [{ text: '铁西区' }, { text: '铁东区' }, { text: '梨树县' }] }]
    },
    {
      text: '黑龙江省',
      children: [{ text: '哈尔滨市', children: [{ text: '道里区' }, { text: '道外区' }, { text: '南岗区' }] },
        { text: '牡丹江市', children: [{ text: '东安区' }, { text: '西安区' }, { text: '爱民区' }] }]
    }
  ]
  @State v: string = '';
  @State showTriggered: string = '';
  private triggered: string = '';
  private maxLines: number = 3;

  linesNum(max: number): void {
    let items: string[] = this.triggered.split('').filter(item => item != '');
    if (items.length > max) {
      this.showTriggered = items.slice(-this.maxLines).join('');
    } else {
      this.showTriggered = this.triggered;
    }
  }

  build() {
    Column() {
      Button("TextPickerDialog.show:" + this.v)
        .onClick(() => {
          TextPickerDialog.show({
            range: this.cascade,
            selected: this.select,
            onAccept: (value: TextPickerResult) => {
              this.select = value.index
              console.log(this.select + '')
              this.v = value.value as string
              console.info("TextPickerDialog:onAccept()" + JSON.stringify(value))
              if (this.triggered != '') {
                this.triggered += `onAccept(${JSON.stringify(value)})`;
              } else {
                this.triggered = `onAccept(${JSON.stringify(value)})`;
              }
              this.linesNum(this.maxLines);
            },
            onCancel: () => {
              console.info("TextPickerDialog:onCancel()")
              if (this.triggered != '') {
                this.triggered += `onCancel()`;
              } else {
                this.triggered = `onCancel()`;
              }
              this.linesNum(this.maxLines);
            },
            onChange: (value: TextPickerResult) => {
              console.info("TextPickerDialog:onChange()" + JSON.stringify(value))
              if (this.triggered != '') {
                this.triggered += `onChange(${JSON.stringify(value)})`;
              } else {
                this.triggered = `onChange(${JSON.stringify(value)})`;
              }
              this.linesNum(this.maxLines);
            },
          })
        })
        .margin({ top: 60 })
    }
  }
}
```

| 系统字体为一倍（适老化能力开启前） | 系统字体为1.75倍（适老化能力开启后） |
| --- | --- |
|  |  |
