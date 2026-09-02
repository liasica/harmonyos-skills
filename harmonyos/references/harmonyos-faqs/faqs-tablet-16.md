---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-16
title: 分屏模式下组件卡片内大面积空白
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 分屏模式下组件卡片内大面积空白
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:09100ae5f37cb8791b4ba8d8e34b22041ef5296f0d8fbecbfb868ae3fafa8436
---

## 问题现象

在平板设置中的系统选项点击智慧多窗开启智慧多窗应用栏配置。打开应用，进入主界面，操作分屏展示，组件卡片内大面积空白。

## 背景知识

* [abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)：module.json5中的abilities标签中可以设置UIAbility组件所支持的窗口模式是否支持分屏。该标签可缺省，缺省默认支持。
* [on('windowStatusChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatuschange11)：开启窗口模式变化的监听，当窗口windowStatus发生变化时进行通知（此时窗口属性可能还没有更新）。
* [on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)：从全屏进入分屏模式后，窗口尺寸、宽高比例会发生变化。需要使用[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)实现对窗口尺寸大小变化的监听，再根据窗口的尺寸变化，更新调整自身应用布局以实现适配。
* [自适应布局](../best-practices/bpta-multi-device-adaptive-layout.md)：当外部容器大小发生变化时，元素可以根据相对关系自动变化以适应外部容器变化的布局能力。自适应布局能力可以实现界面显示随外部容器大小连续变化。
* [响应式布局](../best-practices/bpta-multi-device-responsive-layout.md)：当外部容器大小发生变化时，元素可以根据断点、栅格或特定的特征（如屏幕方向、窗口宽高等）自动变化以适应外部容器变化的布局能力。当前响应式布局能力有3种：
  + [断点](../best-practices/bpta-multi-device-responsive-layout.md#section1532120147301)：将窗口宽度划分为不同的范围（即断点），监听窗口尺寸变化，当断点改变时同步调整页面布局。
  + [媒体查询](../best-practices/bpta-multi-device-responsive-layout.md#section1950102518311)：媒体查询支持监听窗口宽度、横竖屏、深浅色、设备类型等多种媒体特征，当媒体特征发生改变时同步调整页面布局。
  + [栅格布局](../best-practices/bpta-multi-device-responsive-layout.md#section1061332817545)：栅格组件将其所在的区域划分为有规律的多列，通过调整不同断点下的栅格组件的参数以及其子组件占据的列数等，实现不同的布局效果。响应式布局可以实现界面随外部容器大小有不连续变化，通常不同特征下的界面显示会有较大的差异。

## 问题定位

* 排查应用module.json5文件的[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)中supportWindowMode属性是否缺省或者未设置为['split']。
* 排查应用是否监听[on('windowStatusChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatuschange11)和[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)事件，并且动态设置窗口布局。
* 排查页面是否采用[自适应布局](../best-practices/bpta-multi-device-adaptive-layout.md)或[响应式布局](../best-practices/bpta-multi-device-responsive-layout.md)来根据外部容器大小的变化更新调整自身应用布局以实现适配。

## 分析结论

* 应用module.json5文件的[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)中supportWindowMode属性没有缺省也没有设置为split。
* 应用的EntryAbility文件的onWindowStageCreate生命周期回调中，没有通过窗口对象获取启动时的应用窗口宽度并监听窗口尺寸变化。
* 应用没有采用自适应布局或响应式布局，从而导致窗口大小变化页面位置错乱、空白等问题。

## 修改建议

* 将module.json5中的abilities标签中supportWindowMode属性设置为split支持分屏模式或者缺省。
* 在EntryAbility文件中的onWindowStageCreate生命周期回调中通过[on('windowStatusChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatuschange11)和[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)事件来监听窗口布局的变化，并将窗口尺寸的长度单位由px换算为vp后，保存当前窗口的大小。示例代码如下：

  ```screen
  import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { display, window } from '@kit.ArkUI';

  const DOMAIN = 0x0000;

  export default class EntryAbility extends UIAbility {
    private curBp: string = '';

    onCreate(): void {
      try {
        this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
      } catch (err) {
        hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
      }
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
    }

    // 根据当前窗口尺寸更新断点
    private updateBreakpoint(windowWidth: number): void {
      // 将长度的单位由px换算为vp
      let windowWidthVp = windowWidth / display.getDefaultDisplaySync().densityPixels;
      let newBp: string = '';
      if (windowWidthVp < 320) {
        newBp = 'xs';
      } else if (windowWidthVp < 600) {
        newBp = 'sm';
      } else if (windowWidthVp < 840) {
        newBp = 'md';
      } else {
        newBp = 'lg';
      }
      if (this.curBp !== newBp) {
        this.curBp = newBp;
        // 使用状态变量记录当前断点值
        AppStorage.setOrCreate('currentBreakpoint', this.curBp);
      }
    }

    onDestroy(): void {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
    }

    onWindowStageCreate(windowStage: window.WindowStage): void {
      // Main window is created, set main page for this ability
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

      windowStage.getMainWindow().then((windowObj) => {
        // 获取应用启动时的窗口尺寸
        this.updateBreakpoint(windowObj.getWindowProperties().windowRect.width);
        // 注册回调函数，监听窗口尺寸变化
        windowObj.on('windowSizeChange', (windowSize) => {
          this.updateBreakpoint(windowSize.width);
        });
      });

      windowStage.loadContent('pages/Index', (err) => {
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
  };
  ```
* 在页面获取当前窗口的尺寸BreakPoint，并根据BreakPoint结合栅格布局来对页面中的组件进行适配。

  ```screen
  interface ElementType {
    index: number
    text: string
    color: ResourceColor
  }

  @Entry
  @Component
  struct GridRowSample3 {
    @StorageProp('currentBreakpoint') currentBreakpoint: string = 'sm';
    private controller: TextInputController = new TextInputController();
      private elements: ElementType[] = [
      {index: 1, text: '在售', color: $r('sys.color.ohos_id_color_palette_aux1')},
      {index: 2, text: '住宅', color: $r('sys.color.ohos_id_color_palette_aux2')},
      {index: 3, text: '江景', color: $r('sys.color.ohos_id_color_palette_aux3')},
      {index: 4, text: '品质楼盘', color: $r('sys.color.ohos_id_color_palette_aux4')},
      {index: 5, text: '地铁沿线', color: $r('sys.color.ohos_id_color_palette_aux5')},
    ];

    build() {
      Column() {
        TextInput({ text: '', placeholder: 'input your word...', controller: this.controller })
          .placeholderColor(Color.Grey)
          .placeholderFont({ size: 14, weight: 400 })
          .caretColor(Color.Blue)
          .width('95%')
          .height(40)
          .margin(20)
          .fontSize(14)
          .fontColor(Color.Black)
          .inputFilter('[a-z]', (e) => {
            console.info(JSON.stringify(e));
          })
        // 配置不同断点下columns和gutter的取值
        GridRow({columns: {sm: 4, md: 8, lg: 12},
          gutter: {x: {sm: 8, md: 16, lg: 24}, y: {sm: 8, md: 16, lg: 24}}}) {
          ForEach([1,2], ()=>{
            GridCol({span: {sm: 2, md: 4, lg: 6}}) {
              Column() {
                Image($r('app.media.startIcon'))
                  .width('100%')
                  .height(this.currentBreakpoint =='sm' ? '10%': this.currentBreakpoint == 'md' ? "15%": '20%')
                  .layoutWeight(1)
                Text('金顶学府').margin({top: 16, bottom: 8}).padding({left: 8, right: 8})
                Text('地点： 武汉/武昌').fontSize(12).margin({bottom: 8}).fontColor('#333').padding({left: 8})
                Flex({justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center}) {
                  ForEach(this.elements, (item: ElementType) => {
                    Text(item.text).backgroundColor(item.color)
                      .padding(2)
                      .margin({right: 12})
                      .fontSize(12)
                  })
                }.padding({left: 8})
                Text('24599/元m²起').fontSize(24).margin({top: 12}).fontColor(Color.Red).padding({left: 8})
              }
              .alignItems(HorizontalAlign.Start)
              .justifyContent(FlexAlign.Start)
              .border({radius: this.currentBreakpoint == 'sm' ? '4%' : '8%'})
              .height(this.currentBreakpoint == 'sm' ? '30%' : '50%')
              .width('100%')
              .backgroundColor(Color.White)
            }
          })
        }
        .height('100%')
        .width('100%')
      }.padding({left: 12, right: 12})
        .backgroundColor('#eee')
        .height('100%')
        .width('100%')
    }
  }
  ```

完整代码如下：

```screen
interface ElementType {
  index: number
  text: string
  color: ResourceColor
}

@Entry
@Component
struct GridRowSample3 {
  @StorageProp('currentBreakpoint') currentBreakpoint: string = 'sm';
  private controller: TextInputController = new TextInputController();
    private elements: ElementType[] = [
    {index: 1, text: '在售', color: $r('sys.color.ohos_id_color_palette_aux1')},
    {index: 2, text: '住宅', color: $r('sys.color.ohos_id_color_palette_aux2')},
    {index: 3, text: '江景', color: $r('sys.color.ohos_id_color_palette_aux3')},
    {index: 4, text: '品质楼盘', color: $r('sys.color.ohos_id_color_palette_aux4')},
    {index: 5, text: '地铁沿线', color: $r('sys.color.ohos_id_color_palette_aux5')},
  ];

  build() {
    Column() {
      TextInput({ text: '', placeholder: 'input your word...', controller: this.controller })
        .placeholderColor(Color.Grey)
        .placeholderFont({ size: 14, weight: 400 })
        .caretColor(Color.Blue)
        .width('95%')
        .height(40)
        .margin(20)
        .fontSize(14)
        .fontColor(Color.Black)
        .inputFilter('[a-z]', (e) => {
          console.info(JSON.stringify(e));
        })
      // 配置不同断点下columns和gutter的取值
      GridRow({columns: {sm: 4, md: 8, lg: 12},
        gutter: {x: {sm: 8, md: 16, lg: 24}, y: {sm: 8, md: 16, lg: 24}}}) {
        ForEach([1,2], ()=>{
          GridCol({span: {sm: 2, md: 4, lg: 6}}) {
            Column() {
              Image($r('app.media.startIcon'))
                .width('100%')
                .height(this.currentBreakpoint =='sm' ? '10%': this.currentBreakpoint == 'md' ? "15%": '20%')
                .layoutWeight(1)
              Text('金顶学府').margin({top: 16, bottom: 8}).padding({left: 8, right: 8})
              Text('地点： 武汉/武昌').fontSize(12).margin({bottom: 8}).fontColor('#333').padding({left: 8})
              Flex({justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center}) {
                ForEach(this.elements, (item: ElementType) => {
                  Text(item.text).backgroundColor(item.color)
                    .padding(2)
                    .margin({right: 12})
                    .fontSize(12)
                })
              }.padding({left: 8})
              Text('24599/元m²起').fontSize(24).margin({top: 12}).fontColor(Color.Red).padding({left: 8})
            }
            .alignItems(HorizontalAlign.Start)
            .justifyContent(FlexAlign.Start)
            .border({radius: this.currentBreakpoint == 'sm' ? '4%' : '8%'})
            .height(this.currentBreakpoint == 'sm' ? '30%' : '50%')
            .width('100%')
            .backgroundColor(Color.White)
          }
        })
      }
      .height('100%')
      .width('100%')
    }.padding({left: 12, right: 12})
      .backgroundColor('#eee')
      .height('100%')
      .width('100%')
  }
}
```
