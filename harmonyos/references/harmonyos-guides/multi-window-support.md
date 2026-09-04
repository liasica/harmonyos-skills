---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-support
title: 应用声明支持智慧多窗
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口模式 > 智慧多窗应用开发指导 > 应用声明支持智慧多窗
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:08+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:d2f4d3a8da4369e3588f5a0ef27e90f686016004715391bb154a235c9ade73a6
---

当应用需要智慧多窗的能力时，可以通过在[module.json5配置文件](module-configuration-file.md)中对应标签添加相关字段声明支持。

## 声明支持悬浮窗

开发者可以通过在module.json5配置文件中[abilities标签](module-configuration-file.md#abilities标签)下的**supportWindowMode**属性增加“**floating**”字段或使用缺省值以声明应用支持悬浮窗。

**说明** 

supportWindowMode缺省值为["fullscreen", "split", "floating"]。

**supportWindowMode**属性主要标识当前UIAbility所支持的窗口模式，支持的字段及含义如下表所示。

| 字段 | 说明 |
| --- | --- |
| fullscreen | 窗口支持全屏显示。 |
| split | 窗口支持分屏显示。 |
| floating | 窗口支持悬浮窗显示。 |

在应用声明支持智慧多窗后，还可根据业务场景的需要配置是否支持横向悬浮窗或上下分屏模式。

当应用需要支持横向悬浮窗时，开发者可以通过在module.json5配置文件中**abilities**标签下的**preferMultiWindowOrientation**属性增加“**landscape**”或者“**landscape\_auto**”配合API以声明应用支持横向悬浮窗或上下分屏模式。

**preferMultiWindowOrientation**属性主要标识当前UIAbility组件多窗布局方向，支持的字段及含义如下表所示。

| 配置值 | 说明 | 效果 |
| --- | --- | --- |
| portrait | 多窗布局方向为竖向。建议竖向游戏类应用配置。 | **手机**  手势触发悬浮窗：竖向悬浮窗  手势触发分屏：不支持  分屏样式切换：不涉及  **折叠屏手机展开态**  手势触发悬浮窗：竖向悬浮窗  手势触发分屏：形成左右分屏  分屏样式切换：不支持样式切换 |
| landscape | 多窗布局方向为横向，配置后支持横向悬浮窗和上下分屏。建议横向游戏类应用配置。 | **手机**  手势触发悬浮窗：横向悬浮窗  手势触发分屏：不支持  分屏样式切换：不涉及  **折叠屏手机展开态**  手势触发悬浮窗：横向悬浮窗  手势触发分屏：形成上下分屏  分屏样式切换：不支持样式切换 |
| landscape\_auto | 多窗布局动态可变为横向，需要配合API（[enableLandscapeMultiWindow](../harmonyos-references/arkts-apis-window-window.md#enablelandscapemultiwindow12) / [disableLandscapeMultiWindow](../harmonyos-references/arkts-apis-window-window.md#disablelandscapemultiwindow12)）使用。建议视频类应用配置。 | **系统识别应用为横向全屏播放：**  **手机**  手势触发悬浮窗：横向悬浮窗  手势触发分屏：形成上下分屏  分屏样式切换：不涉及  **折叠屏手机展开态**  手势触发悬浮窗：横向悬浮窗  手势触发分屏：形成上下分屏  分屏样式切换：支持样式切换  **系统识别应用为非横向全屏播放：** 同配置为default |
| default | 缺省值，参数不配置时默认为default。  建议其他应用类配置。 | **折叠屏手机折叠态 & 手机**  手势触发悬浮窗：竖向悬浮窗  手势触发分屏：形成上下分屏  分屏样式切换：不涉及  **折叠屏手机展开态**  手势触发悬浮窗：竖向悬浮窗  手势触发分屏：形成左右分屏  分屏样式切换：支持样式切换 |

## 声明支持分屏

开发者可以通过在module.json5配置文件中[abilities标签](module-configuration-file.md#abilities标签)下的**supportWindowMode**属性增加“**split**”字段或使用缺省值以声明应用支持分屏。

**说明** 

supportWindowMode缺省值为["fullscreen", "split", "floating"]。

**supportWindowMode**属性主要标识当前UIAbility所支持的窗口模式，支持的字段及含义如下表所示。

| 字段 | 说明 |
| --- | --- |
| fullscreen | 窗口支持全屏显示。 |
| split | 窗口支持分屏显示。 |
| floating | 窗口支持悬浮窗显示。 |

## 应用内分屏

应用内分屏功能允许[声明支持分屏](multi-window-support.md#声明支持分屏)的应用在全屏显示模式下，通过调用startAbility方法启动UIAbility并形成分屏。该功能能够增强应用的多任务处理能力，提升用户的操作体验。

仅在Tablet设备、PC/2in1设备，以及支持横屏桌面且处于展开状态的折叠屏设备上生效。

此处以点击按钮启动分屏为例，主要步骤和示例如下所示：

1. 在应用中获取UIAbilityContext 对象，这是启动分屏所必需的上下文对象，用于后续调用startAbility接口。

   ```ts
   this.hostContext = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
   ```
2. 调用startAbility接口启动UIAbility，形成分屏。调用startAbility接口时，设置StartOptions对象，需要指定窗口模式[windowMode](../harmonyos-references/js-apis-app-ability-startoptions.md#startoptions)，需设置为WINDOW\_MODE\_SPLIT\_PRIMARY或者WINDOW\_MODE\_SPLIT\_SECONDARY。并可根据需要设置其他StartOptions属性或startAbility参数，如Want对象。

   从API版本26.0.0开始，支持使用分屏比例字段[splitRatio](../harmonyos-references/js-apis-app-ability-startoptions.md#startoptions)（需设置为EQUAL、PRIMARY\_DOMINANT或者SECONDARY\_DOMINANT，默认为EQUAL）设置应用内分屏比例。

   ```ts
   // 创建StartOptions并设置为主窗口模式，以主窗口占较大比例，副窗口占较小比例的布局启动分屏。
   let option: StartOptions = { windowMode: AbilityConstant.WindowMode.WINDOW_MODE_SPLIT_PRIMARY, splitRatio: window.SplitRatioPreference.PRIMARY_DOMINANT };
   let want: Want = { bundleName: 'com.example.startsplitdemo', abilityName: 'EntryAbility1', moduleName: '' };
   this.hostContext?.startAbility(want, option);
   ```

   从API版本26.0.0开始，支持指定窗口模式[windowMode](../harmonyos-references/js-apis-app-ability-startoptions.md#startoptions)为WINDOW\_MODE\_SPLIT，可从全屏窗口拉起应用内分屏，形成二分屏。在支持三分屏的设备上，从二分屏拉起应用内分屏，形成三分屏。

   ```ts
   // 创建StartOptions并设置窗口模式为分屏模式WINDOW_MODE_SPLIT，右侧分屏
   let option: StartOptions = { windowMode: AbilityConstant.WindowMode.WINDOW_MODE_SPLIT };
   let want: Want = { bundleName: 'com.example.startsplitdemo', abilityName: 'EntryAbility1', moduleName: '' };
   this.hostContext?.startAbility(want, option);
   ```
3. 若继续执行上述步骤，可继续启动其他UIAbility窗口。分屏窗口数量未满时，支持拉起新的分屏窗口；分屏窗口数量已满时，支持分屏窗口替换。

完整示例如下：

使用DevEco Studio新建Ability，创建EntryAbility，EntryAbility1和EntryAbility2，对应文中组成分屏的三个窗口页面，加载页面都是默认页面Index.ets。

```ts
// Index.ets
import { AbilityConstant, common, StartOptions, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

interface AbilityActionItem {
  title: string;
  want: Want;
  startOption: StartOptions;
}
const ICON_BG_COLORS = ['#E8F0FE', '#FFF3E0', '#E8F5E9', '#FCE4EC', '#E0F2F1', '#EDE7F6', '#F9FBE7', '#F1F3F5'];
const DOMAIN: number = 0x0000;
const TAG: string = 'Index';
const ACTION_ITEMS: AbilityActionItem[] = [
  {
    title: 'Start EntryAbility1 in left split-screen',
    // 指定拉起的分屏窗口的应用信息
    want: { bundleName: 'com.example.startsplitdemo', abilityName: 'EntryAbility1', moduleName: '' },
    // 创建StartOptions并设置窗口模式为分屏模式，左侧分屏
    startOption: { windowMode: AbilityConstant.WindowMode.WINDOW_MODE_SPLIT_PRIMARY }
  },
  {
    title: 'Start EntryAbility2 in the right split-screen',
    want: { bundleName: 'com.example.startsplitdemo', abilityName: 'EntryAbility2', moduleName: '' },
    // 创建StartOptions并设置窗口模式为分屏模式，右侧分屏
    startOption: { windowMode: AbilityConstant.WindowMode.WINDOW_MODE_SPLIT_SECONDARY }
  },
  {
    title: 'Start EntryAbility1 in the left split screen at a larger aspect ratio.',
    want: { bundleName: 'com.example.startsplitdemo', abilityName: 'EntryAbility1', moduleName: '' },
    startOption: {
      windowMode: AbilityConstant.WindowMode.WINDOW_MODE_SPLIT_PRIMARY,
      // 将左分屏以较大比例，右分屏以较小比例启动应用内分屏
      splitRatio: window.SplitRatioPreference.PRIMARY_DOMINANT
    }
  },
  {
    title: 'Start EntryAbility2 in the right split screen at a larger aspect ratio.',
    want: { bundleName: 'com.example.startsplitdemo', abilityName: 'EntryAbility2', moduleName: '' },
    startOption: {
      windowMode: AbilityConstant.WindowMode.WINDOW_MODE_SPLIT_SECONDARY,
      // 将左分屏以较小比例，右分屏以较大比例启动应用内分屏
      splitRatio: window.SplitRatioPreference.SECONDARY_DOMINANT
    }
  },
  {
    title: 'Start EntryAbility1 with the WINDOW_MODE_SPLIT window mode',
    want: { bundleName: 'com.example.startsplitdemo', abilityName: 'EntryAbility1', moduleName: '' },
    // 创建StartOptions并设置窗口模式为分屏模式WINDOW_MODE_SPLIT，右侧分屏
    startOption: { windowMode: AbilityConstant.WindowMode.WINDOW_MODE_SPLIT }
  },
  {
    title: 'Start EntryAbility2 with the WINDOW_MODE_SPLIT window mode',
    want: { bundleName: 'com.example.startsplitdemo', abilityName: 'EntryAbility2', moduleName: '' },
    startOption: { windowMode: AbilityConstant.WindowMode.WINDOW_MODE_SPLIT }
  }
]

@Entry
@Component
struct Index {
  @State name: string = '';
  @State currentItem: AbilityActionItem | null = null;
  private items: AbilityActionItem[] = ACTION_ITEMS;
  private hostContext: common.UIAbilityContext | null = null;

  aboutToAppear(): void {
    this.hostContext = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
    this.name = this.hostContext?.abilityInfo.name ?? '';
  }

  onItemClick = (item: AbilityActionItem) => {
    this.currentItem = item;
    this.hostContext?.startAbility(item.want, item.startOption).then(() => {
      hilog.info(DOMAIN, TAG, '启动成功');
    }).catch((err: BusinessError) => {
      hilog.error(DOMAIN, TAG, err.message);
    });
  }

  build() {
    Column() {
      Column({ space: 5 }) {
        Text('Ability Name: ' + this.name).fontSize(20).fontWeight(FontWeight.Medium).fontColor('#1D2129');
        if (this.currentItem) {
          Text('Ability Want Info: ' + JSON.stringify(this.currentItem)).fontSize(14).fontColor('#86909C');
        }
      }
      .width('100%')
      .padding(20)
      .backgroundColor('#F7F8FA')
      .borderRadius(18)
      .margin({ bottom: 20 })

      Column({ space: 4 }) {
        List({ space: 4 }) {
          ForEach(this.items, (item: AbilityActionItem, index: number) => {
            if (item.want.abilityName !== this.name) {
              ListItem() {
                Row() {
                  this.iconBuilder(item, index)
                  this.buttonInfoBuilder(item, index)
                }
                .alignItems(VerticalAlign.Center)
                .justifyContent(FlexAlign.Start)
                .width('100%')
                .margin({ left: 16, right: 16, top: 16, bottom: 16 })
                .onClick(() => this.onItemClick(item))
              }
              .borderRadius(14)
              .backgroundColor(Color.White)
              .width('100%')
            }
          })
        }
        .borderRadius(14)
        .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true })
        .scrollBar(BarState.Auto)
        .height('100%')
      }
      .backgroundColor('#60d9e0dc')
      .borderRadius(18)
      .padding({ left: 4, right: 4, top: 4, bottom: 4 })
      .width('100%')
      .layoutWeight(1);
    }
    .width('100%').height('100%').padding(24).backgroundColor('#FFFFFF');
  }

  @Builder
  buttonInfoBuilder(item: AbilityActionItem, index: number) {
    Column() {
      Text(item.title)
        .fontWeight(FontWeight.Medium).fontSize(14)
      Text(`${AbilityConstant.WindowMode[item.startOption.windowMode ?? -1]}`)
        .fontSize(12).fontColor('#86909C');
      Text(`windowMode:${item.startOption.windowMode}`)
        .fontSize(12).fontColor('#86909C');
      if (item.startOption.splitRatio !== undefined) {
        Text(`splitRatio: ${item.startOption.splitRatio}`)
          .fontSize(12).fontColor('#86909C');
      }
    }
    .alignItems(HorizontalAlign.Start)
    .justifyContent(FlexAlign.Center)
    .constraintSize({ maxWidth: '75%' })
    .margin({ left: 10 })
  }

  @Builder
  iconBuilder(item: AbilityActionItem, index: number) {
    Button({ type: ButtonType.Circle }) {
      SymbolGlyph(item.startOption.windowMode === AbilityConstant.WindowMode.WINDOW_MODE_SPLIT ?
        $r('sys.symbol.rectangle_split_3x1') : $r('sys.symbol.rectangle_split_2x1'))
        .fontSize(26).fontColor(['#ffa1e6f8']);
    }
    .width(52).height(52)
    .backgroundColor(ICON_BG_COLORS[index % ICON_BG_COLORS.length])
    .borderRadius(26)
    .id('icon')
  }
}
```

图1 启动左侧分屏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/wx6kHgG5SL6jrUSx_7HitA/zh-cn_image_0000002742123179.gif)

图2 启动右侧分屏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/KHIZ1oKmSeqHF1xuBEZwyg/zh-cn_image_0000002712244266.gif)

图3 以左分屏占较大比例启动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/iOsaiao9TAyjsXWRGDvnPg/zh-cn_image_0000002742003219.gif)

图4 以右分屏占较大比例启动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/lFbya5t8T16O-NZgO5X-KA/zh-cn_image_0000002712404232.gif)

图5 从二分屏拉起应用内分屏，形成三分屏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/URCBBes4QNaDIF0OZI6hJg/zh-cn_image_0000002742123181.gif)

## 应用内多窗

从HarmonyOS 6.0.0版本开始，新增支持应用内多窗。应用内多窗功能支持应用拉起分屏或全景多窗，方便用户进行多任务处理。

当应用开发者需要使用应用内多窗图标时，可以使用高级组件[MultiWindowEntryInAPP](../harmonyos-references/ui-design-multiwindowentryinapp-api.md)实现该功能。
