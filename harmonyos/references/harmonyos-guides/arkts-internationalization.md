---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-internationalization
title: UI国际化
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > UI国际化
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0b29d5413989a224036a202c17c0ed03c3a38dfc2af6e971b14f6143e5247f06
---

本文介绍如何实现应用程序UI界面的国际化，包含资源配置和镜像布局，关于应用适配国际化的详细参考，请参考[Localization Kit（本地化开发服务）](i18n-l10n.md)。

## 利用资源限定词配置国际化资源

在开发阶段，通过DevEco Studio，可以为应用在对应语言和地区的资源限定词目录下配置不同的资源，来实现UI国际化。详细介绍请参考[资源分类与访问](resource-categories-and-access.md)。

## 使用镜像能力

不同国家对文本对齐方式和读取顺序有所不同，例如英语采用从左到右的顺序，阿拉伯语和希腊语则采用从右到左（RTL）的顺序。为满足不同用户的阅读习惯，ArkUI提供了镜像能力。在特定情况下将显示内容在X轴上进行镜像反转，由从左到右显示变成从右到左显示。

| 镜像前 | 镜像后 |
| --- | --- |
|  |  |

当组件满足以下任意条件时，镜像能力生效：

1. 组件的direction属性设置为Direction.Rtl。
2. 组件的direction属性设置为Direction.Auto，且当前的系统语言（如维吾尔语）的阅读习惯是从右向左。

### 基本概念

* LTR：顺序为从左到右。
* RTL：顺序为从右到左。

### 使用约束

ArkUI 如下能力已默认适配镜像：

| 类别 | 名称 |
| --- | --- |
| 基础组件 | [Swiper](../harmonyos-references/ts-container-swiper.md)、[Tabs](../harmonyos-references/ts-container-tabs.md)、[TabContent](../harmonyos-references/ts-container-tabcontent.md)、[List](../harmonyos-references/ts-container-list.md)、[Progress](../harmonyos-references/ts-basic-components-progress.md)、[CalendarPicker](../harmonyos-references/ts-basic-components-calendarpicker.md)、[CalendarPickerDialog](../harmonyos-references/ts-methods-calendarpicker-dialog.md)、[TextPicker](../harmonyos-references/ts-basic-components-textpicker.md)、[TextPickerDialog](../harmonyos-references/ts-methods-textpicker-dialog.md)、[DatePicker](../harmonyos-references/ts-basic-components-datepicker.md)、[DatePickerDialog](../harmonyos-references/ts-methods-datepicker-dialog.md)、[Grid](../harmonyos-references/ts-container-grid.md)、[WaterFlow](../harmonyos-references/ts-container-waterflow.md)、[Scroll](../harmonyos-references/ts-container-scroll.md)、[ScrollBar](../harmonyos-references/ts-basic-components-scrollbar.md)、[AlphabetIndexer](../harmonyos-references/ts-container-alphabet-indexer.md)、[Stepper](../harmonyos-references/ts-basic-components-stepper.md)、[SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)、[Navigation](../harmonyos-references/ts-basic-components-navigation.md)、[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)、[Rating](../harmonyos-references/ts-basic-components-rating.md)、[Slider](../harmonyos-references/ts-basic-components-slider.md)、[Toggle](../harmonyos-references/ts-basic-components-toggle.md)、[Badge](../harmonyos-references/ts-container-badge.md)、[Counter](../harmonyos-references/ts-container-counter.md)、[Chip](../harmonyos-references/ohos-arkui-advanced-chip.md)、[SegmentButton](../harmonyos-references/ohos-arkui-advanced-segmentbutton.md)、[bindMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindmenu)、[bindContextMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu8)、[TextInput](../harmonyos-references/ts-basic-components-textinput.md)、[TextArea](../harmonyos-references/ts-basic-components-textarea.md)、[Search](../harmonyos-references/ts-basic-components-search.md)、[Stack](../harmonyos-references/ts-container-stack.md)、[GridRow](../harmonyos-references/ts-container-gridrow.md)、[Text](../harmonyos-references/ts-basic-components-text.md)、[Select](../harmonyos-references/ts-basic-components-select.md)、[Marquee](../harmonyos-references/ts-basic-components-marquee.md)、[Row](../harmonyos-references/ts-container-row.md)、[Column](../harmonyos-references/ts-container-column.md)、[Flex](../harmonyos-references/ts-container-flex.md)、[RelativeContainer](../harmonyos-references/ts-container-relativecontainer.md)、[ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md) |
| 高级组件 | [SelectionMenu](../harmonyos-references/ohos-arkui-advanced-selectionmenu.md) 、[TreeView](../harmonyos-references/ohos-arkui-advanced-treeview.md) 、[Filter](../harmonyos-references/ohos-arkui-advanced-filter.md)、[SplitLayout](../harmonyos-references/ohos-arkui-advanced-splitlayout.md)、[ToolBar](../harmonyos-references/ohos-arkui-advanced-toolbar.md)、[ComposeListItem](../harmonyos-references/ohos-arkui-advanced-composelistitem.md)、[EditableTitleBar](../harmonyos-references/ohos-arkui-advanced-editabletitlebar.md)、[ProgressButton](../harmonyos-references/ohos-arkui-advanced-progressbutton.md)、[SubHeader](../harmonyos-references/ohos-arkui-advanced-subheader.md) 、[Popup](../harmonyos-references/ohos-arkui-advanced-popup.md)、[Dialog](../harmonyos-references/ohos-arkui-advanced-dialog.md)、[SwipeRefresher](../harmonyos-references/ohos-arkui-advanced-swiperefresher.md) |
| 通用属性 | [position](../harmonyos-references/ts-universal-attributes-location.md#position)、[markAnchor](../harmonyos-references/ts-universal-attributes-location.md#markanchor)、[offset](../harmonyos-references/ts-universal-attributes-location.md#offset)、[alignRules](../harmonyos-references/ts-universal-attributes-location.md#alignrules12)、[borderWidth](../harmonyos-references/ts-universal-attributes-border.md#borderwidth)、[borderColor](../harmonyos-references/ts-universal-attributes-border.md#bordercolor)、[borderRadius](../harmonyos-references/ts-universal-attributes-border.md#borderradius)、[padding](../harmonyos-references/ts-universal-attributes-size.md#padding)、[margin](../harmonyos-references/ts-universal-attributes-size.md#margin) |
| 接口 | [AlertDialog](../harmonyos-references/ts-methods-alert-dialog-box.md)、[ActionSheet](../harmonyos-references/ts-methods-action-sheet.md)、[promptAction.showDialog](../harmonyos-references/js-apis-promptaction.md#promptactionshowdialogdeprecated)、[promptAction.showToast](../harmonyos-references/js-apis-promptaction.md#promptactionshowtoastdeprecated) |

但如下三种场景还需要进行适配：

1. 界面布局、边框设置：关于方向类的通用属性，如果需要支持镜像能力，使用泛化的方向指示词 start/end入参类型替换 left/right、x/y等绝对方向指示词的入参类型，来表示自适应镜像能力。
2. [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)组件只有限支持文本绘制的镜像能力。
3. [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件不支持组件镜像能力。

### 界面布局和边框设置

目前，以下三类通用属性需要使用新入参类型适配：

位置设置：[position](../harmonyos-references/ts-universal-attributes-location.md#position)、[markAnchor](../harmonyos-references/ts-universal-attributes-location.md#markanchor)、[offset](../harmonyos-references/ts-universal-attributes-location.md#offset)、[alignRules](../harmonyos-references/ts-universal-attributes-location.md#alignrules12)

边框设置：[borderWidth](../harmonyos-references/ts-universal-attributes-border.md#borderwidth)、[borderColor](../harmonyos-references/ts-universal-attributes-border.md#bordercolor)、[borderRadius](../harmonyos-references/ts-universal-attributes-border.md#borderradius)

尺寸设置：[padding](../harmonyos-references/ts-universal-attributes-size.md#padding)、[margin](../harmonyos-references/ts-universal-attributes-size.md#margin)

以position为例，需要把绝对方向x、y描述改为新入参类型start、end的描述，其他属性类似。

```typescript
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct InterfaceLayoutBorderSettings {
  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Stack({ alignContent: Alignment.TopStart }) {
        Column()
          .width(100)
          .height(100)
          .backgroundColor(Color.Red)
          .position({
            start: LengthMetrics.px(200),
            top: LengthMetrics.px(200)
          }) // 需要同时支持LTR和RTL时使用API12新增的LocalizedEdges入参类型,
        // 仅支持LTR时等同于.position({ x: '200px', y: '200px' })

      }.backgroundColor(Color.Blue)
    }.width('100%').height('100%').border({ color: '#880606' })
  }
}
```

### 自定义绘制Canvas组件

Canvas组件的绘制内容和坐标均不支持镜像能力。已绘制到Canvas组件上的内容并不会跟随系统语言的切换自动做镜像效果。

[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)的文本绘制支持镜像能力，在使用时需要与Canvas组件的通用属性direction（组件显示方向）和CanvasRenderingContext2D的属性direction（文本绘制方向）协同使用。具体规格如下：

1. 优先级：CanvasRenderingContext2D的direction属性 > Canvas组件通用属性direction > 系统语言决定的水平显示方向。
2. Canvas组件本身不会自动跟随系统语言切换镜像效果，需要应用监听到系统语言切换后自行重新绘制。
3. CanvasRenderingContext2D绘制文本时，只有符号等文本会对绘制方向生效，英文字母和数字不响应绘制方向的变化。

```typescript
import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';

@Entry
@Component
struct CustomizeCanvasComponentDrawing {
  @State message: string = 'Hello world';
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  aboutToAppear(): void {
    // 监听系统语言切换
    let subscriber: commonEventManager.CommonEventSubscriber | null = null;
    let subscribeInfo2: commonEventManager.CommonEventSubscribeInfo = {
      events: ['usual.event.LOCALE_CHANGED'],
    }
    commonEventManager.createSubscriber(subscribeInfo2,
      (err: BusinessError, data: commonEventManager.CommonEventSubscriber) => {
        if (err) {
          console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
          return;
        }

        subscriber = data;
        if (subscriber !== null) {
          commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
            if (err) {
              return;
            }
            // 监听到语言切换后，需要重新绘制Canvas内容
            this.drawText();
          })
        } else {
            console.error(`Need create subscriber`);
        }
      })
  }

  drawText(): void {
    console.error('drawText')
    this.context.reset()
    this.context.direction = 'inherit'
    this.context.font = '30px sans-serif'
    this.context.fillText('ab%123&*@', 50, 50)
  }

  build() {
    Row() {
      Canvas(this.context)
        .direction(Direction.Auto)
        .width('100%')
        .height('100%')
        .onReady(() =>{
          this.drawText()
        })
    }
    .height('100%')
  }

}
```

| 镜像前 | 镜像后 |
| --- | --- |
|  |  |

### 镜像状态字符对齐

[Direction](../harmonyos-references/ts-appendix-enums.md#direction)是指文字的方向，即文本在屏幕上呈现时字符的顺序。在从左到右（LTR）文本中，显示顺序是从左向右；在从右到左（RTL）文本中，显示顺序是从右到左。

[TextAlign](../harmonyos-references/ts-appendix-enums.md#textalign)是将文本作为一个整体，在布局上的影响，具体位置会受Direction影响，以TextAlign为start为例，当Direction为LTR时，布局位置靠左；当Direction为RTL时，布局位置靠右。

在LTR与RTL文本混排时，如一个英文句子中包含阿拉伯语的单词或短语，显示顺序将变得复杂。下图为数字和维吾尔语混合时对应的字符逻辑顺序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/p0tQL-V4RyqTB3uRty5Kkg/zh-cn_image_0000002736312963.png)

此时，文本渲染引擎会采用名为“双向算法”或“Unicode双向算法”（Unicode Bidirectional Algorithm）的方法来确定字符的显示顺序。下图展示了LTR与RTL文本混合时对应的字符显示顺序，确定字符方向的基本原则如下：

1. 强字符的方向性：强字符具有明确的方向性，例如，中文为LTR，阿拉伯语为RTL，这类字符的方向性会影响其周围的中性字符。
2. 弱字符的方向性：弱字符不具备明确的方向性，这些字符不会影响其周围中性字符的方向。
3. 中性字符的方向性：中性字符无固定方向性，它们会继承其最近的强字符的方向；若附近无强字符，则采用全局方向。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/aoCyMJHmTN-i4HuX60Mxrg/zh-cn_image_0000002706673922.png)
