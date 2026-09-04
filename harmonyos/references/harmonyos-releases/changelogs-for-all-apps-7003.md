---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-7003
title: 针对所有应用的变更
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > OS平台行为变更说明 > 26.0.0 Release引入的行为变更 > 针对所有应用的变更
category: harmonyos-releases
scraped_at: 2026-09-05T06:12:27+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:06cb8beaa7fc020229be53f5fd5fe0fbd9e333fa10fc3c7b311ed1a4a3b87b15
---

## Ability Kit

### 新增默认浏览器权限

**变更原因**

为避免非专业或低安全性应用引发的安全风险与体验割裂，系统引入默认浏览器权限管控机制。该机制围绕安全、隐私、用户体验三大维度设立严格准入标准，全面保障并提升网络浏览体验。

**变更影响**

此变更涉及应用适配。

变更前：

仅声明支持打开HTTP协议，应用即可展示在默认浏览器备选列表并且可以被设置为默认浏览器。

变更后：

1. 应用需要申请默认浏览器权限（ohos.permission.DEFAULT\_WEB\_BROWSER）才可以被展示在默认浏览器备选列表。
2. 具备默认浏览器权限的应用才可以被设置为默认浏览器。

**说明** 

默认浏览器权限管控将于HarmonyOS下一个正式发布版本生效。请有需要的开发者尽快申请该权限，以免影响功能。

**起始 API Level**

不涉及

**变更的接口/组件**

不涉及

**适配指导**

若设置默认浏览器，需要按照[受限权限申请指导](../harmonyos-guides/declare-permissions-in-acl.md)申请默认浏览器权限（ohos.permission.DEFAULT\_WEB\_BROWSER）。权限授权后，在配置文件中[声明权限](../harmonyos-guides/declare-permissions.md)。

可申请默认浏览器权限的特殊场景和功能：

* 默认浏览器权限面向浏览器类应用，用于将应用设置为系统默认浏览器，接管系统及第三方应用发出的网页链接打开请求，统一管理网页内容的跳转与展示。
* 仅满足浏览器品类标准，并通过安全、隐私、用户体验三项审核的应用方可申请此权限。

## Agent Framework Kit

### OnDataCallback接口变更

**变更原因**

[OnDataCallback](../harmonyos-references/hmaf-a2a-protocol.md#ondatacallback)接口的method参数类型由枚举AgentOperation变更为string，简化了接口定义，提升了扩展性。开发者可直接使用字符串进行方法判断，无需依赖枚举类型。未知method字段值改为直接透传给Agent处理。

RequestContext参数类型中，RequestContext.getClientSessionId()方法仅在ClearContext请求中会返回非空值。ClearContext请求不再单独处理，改为按未知method流程处理。此方法将与ClearContext的处理流程一同删除。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更涉及的接口为26.0.0 Beta版本新增接口，因此仅在26.0.0 Beta版本上新建应用或已将应用升级至26.0.0 Beta版本的开发者需予以关注。

* 变更前：[OnDataCallback](../harmonyos-references/hmaf-a2a-protocol.md#ondatacallback)的method参数类型为AgentOperation枚举；RequestContext.getClientSessionId()方法可用。
* 变更后：[OnDataCallback](../harmonyos-references/hmaf-a2a-protocol.md#ondatacallback)的method参数类型为string；RequestContext.getClientSessionId()方法已删除。

**起始 API Level**

26.0.0

**变更的接口/组件**

@kit.AgentFrameworkKit：

* [OnDataCallback](../harmonyos-references/hmaf-a2a-protocol.md#ondatacallback)，method参数类型改为string。
* AgentOperation枚举类已删除。
* RequestContext.getClientSessionId()方法已删除。

**适配指导**

开发者需要修改[OnDataCallback](../harmonyos-references/hmaf-a2a-protocol.md#ondatacallback)接口的实现：

1. 从@kit.AgentFrameworkKit的import中删除AgentOperation。
2. 将method参数类型由AgentOperation改为string。
3. 将switch语句中的枚举值替换为字符串。

   | 变更前（枚举值） | 变更后（string） |
   | --- | --- |
   | AgentOperation.EXECUTE | 'Execute' |
   | AgentOperation.CANCEL | 'Cancel' |
   | AgentOperation.CLEAR\_CONTEXT | ClearContext请求不再单独提供处理流程，建议删除此分支或移动到默认分支处理 |
   | AgentOperation.PERCEPTION\_SUGGEST | 'PerceptionSuggest' |
4. 删除RequestContext.getClientSessionId()的调用。

适配示例，变更前：

```ts
import { RequestContext, AgentOperation } from '@kit.AgentFrameworkKit';
const TAG = 'A2A-Server';
let agentOnData = (method: AgentOperation, context: RequestContext) => {
  const taskId: string = context.getTaskId() ?? '';
  switch (method) {
    case AgentOperation.EXECUTE:
      // 执行A2A服务端的请求处理流程
      hilog.info(0x0000, TAG, 'Execute called');
      break;
    case AgentOperation.CANCEL:
      hilog.info(0x0000, TAG, 'Cancel called');
      break;
    case AgentOperation.CLEAR_CONTEXT:
      const clientSessionId: string = context.getClientSessionId() ?? "";
      hilog.info(0x0000, TAG, `Clear context called, session id: ${clientSessionId}`);
      break;
    case AgentOperation.PERCEPTION_SUGGEST:
      hilog.info(0x0000, TAG, 'Perception suggest called');
      break;
    default:
      break;
  }
};
```

变更后：

```ts
import { RequestContext } from '@kit.AgentFrameworkKit';
const TAG = 'A2A-Server';
let agentOnData = (method: string, context: RequestContext) => {
  const taskId: string = context.getTaskId() ?? '';
  switch (method) {
    case 'Execute':
      // 执行A2A服务端的请求处理流程
      hilog.info(0x0000, TAG, 'Execute called');
      break;
    case 'Cancel':
      hilog.info(0x0000, TAG, 'Cancel called');
      break;
    case 'PerceptionSuggest':
      hilog.info(0x0000, TAG, 'Perception suggest called');
      break;
    default:
      break;
  }
};
```

## ArkUI

### Image组件autoResize属性默认行为变更

**变更原因**

图片解码后的宽×高像素乘积超过5000万时，按原图尺寸解码会占用大量内存，内存压力大甚至存在稳定性问题。为控制内存占用，该场景下[autoResize](../harmonyos-references/ts-basic-components-image.md#autoresize)属性默认值变更为true，即图片解码过程中开启降采样解码。该判断仅与图片像素尺寸相关，与图片文件大小及图片格式无关。

**变更影响**

此变更涉及应用适配。

* 变更前：未设置[autoResize](../harmonyos-references/ts-basic-components-image.md#autoresize)时，Image组件的autoResize属性默认为false，即图片解码过程中不自动缩放，按原图尺寸解码。
* 变更后：未设置autoResize时，如果图片解码后的宽×高像素乘积超过5000万，Image组件的autoResize默认设置为true，此时图片解码过程中会自动缩放，根据显示区域尺寸降采样解码。

**起始 API Level**

7

**变更的接口/组件**

Image的autoResize属性。

**适配指导**

默认行为变更。如果应用加载宽×高像素乘积大于5000万的图片且需要保留原图显示质量（例如需要对大图进行放大查看细节），可设置autoResize为false，按原图尺寸解码。

```ts
Image($r('app.media.large_image'))
  .autoResize(false)
```

### 沉浸光感新增生效约束

**变更原因**

为确保性能和功耗体验最优，规范沉浸光感组件使用，沉浸光感对部分组件新增生效范围的约束。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更涉及的接口为26.0.0 Beta版本新增接口，因此仅在26.0.0 Beta版本上新建应用或已将应用升级至26.0.0 Beta版本的开发者需予以关注。

* 变更前：针对支持开启沉浸光感的所有组件，沉浸光感开启后，沉浸光感效果生效。
* 变更后：

  + 弹窗类组件（AlertDialog、ActionSheet、CustomDialog、CalendarPickerDialog、DatePickerDialog、TimePickerDialog、TextPickerDialog、SelectionMenu、AlphabetIndexer弹窗、Text设置copyOption后长按或双击触发的文本菜单）和弹窗类接口（PromptAction、ArkUI\_NativeDialog、@ohos.promptAction (弹窗)、Popup控制、Tips控制、菜单控制、半模态转场）以及按钮与选择类组件（Slider、Toggle、Select）仍可在页面内全部区域生效，与变更前无变化。
  + 其他组件仅在Navigation/NavDestination标题栏或横向Tab中barPosition为BarPosition.End的底部TabBar中生效。在其他区域中设置沉浸光感效果不生效。

以下示例展示了，其他组件（如Column）不在Navigation/NavDestination标题栏或底部TabBar区域中设置沉浸光感，在变更前后的效果变化：

```ts
import { uiMaterial } from '@kit.ArkUI';

@Entry
@Component
struct MaterialScopeExample {
  build() {
    Stack() {
      Column()
        .width('100%')
        .height('100%')
        .linearGradient({
          angle: 0, // 渐变角度，0度是从左到右。
          colors: [
            ['#004AAF', 0.0], // 起始颜色及位置（0.0表示起点）。
            ['#2787D9', 0.5], // 中间颜色及位置。
            ['#F0FAFF', 1.0] // 结束颜色及位置（1.0表示终点）。
          ]
        })
      Column() {
        // 标题栏/底部TabBar范围外的普通组件
        Column() {
          Text('普通组件')
            .fontSize(32)
            .fontWeight(FontWeight.Bold)
        }
        .width(328)
        .height(56)
        .borderRadius(28)
        .justifyContent(FlexAlign.Center)
        .systemMaterial(new uiMaterial.ImmersiveMaterial({
          style: uiMaterial.ImmersiveStyle.THIN,
        }))
      }
    }
  }
}
```

变更前，Column组件通过systemMaterial设置了沉浸光感，沉浸光感效果生效。示例图片如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/2-0G8f8STzuVcfw4JGvubg/zh-cn_image_0000002744123695.jpg)

变更后，Column组件通过systemMaterial设置了沉浸光感，由于不处于生效范围内，沉浸光感效果不生效。示例图片如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/CYesaLCUSWye2CiapRcRDQ/zh-cn_image_0000002714364828.jpg)

**起始 API Level**

26.0.0

**变更的接口/组件**

除以下清单以外的所有ArkUI组件：

* 弹窗类组件（[AlertDialog](../harmonyos-references/ts-methods-alert-dialog-box.md)、[ActionSheet](../harmonyos-references/ts-methods-action-sheet.md)、[CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)、[CalendarPickerDialog](../harmonyos-references/ts-methods-calendarpicker-dialog.md)、[DatePickerDialog](../harmonyos-references/ts-methods-datepicker-dialog.md)、[TimePickerDialog](../harmonyos-references/ts-methods-timepicker-dialog.md)、[TextPickerDialog](../harmonyos-references/ts-methods-textpicker-dialog.md)、[SelectionMenu](../harmonyos-references/ohos-arkui-advanced-selectionmenu.md)、[AlphabetIndexer](../harmonyos-references/ts-container-alphabet-indexer.md)弹窗、[Text](../harmonyos-references/ts-basic-components-text.md)设置copyOption后长按或双击触发的文本菜单）。
* 弹窗类接口（[PromptAction](../harmonyos-references/arkts-apis-uicontext-promptaction.md)、[ArkUI\_NativeDialog](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog.md)、[@ohos.promptAction](../harmonyos-references/js-apis-promptaction.md) (弹窗)、[Popup控制](../harmonyos-references/ts-universal-attributes-popup.md)、[Tips控制](../harmonyos-references/ts-universal-attributes-tips.md)、[菜单控制](../harmonyos-references/ts-universal-attributes-menu.md)、[半模态转场](../harmonyos-references/ts-universal-attributes-sheet-transition.md)）。
* 按钮与选择类组件（[Slider](../harmonyos-references/ts-basic-components-slider.md)、[Toggle](../harmonyos-references/ts-basic-components-toggle.md)、[Select](../harmonyos-references/ts-basic-components-select.md)）。

**适配指导**

变更后，如果组件需要沉浸光感效果，需要将该组件放置于Navigation/NavDestination标题栏或Tabs的底部TabBar。

下面提供三个示例，分别介绍如何将组件放置于Navigation标题栏、横向Tabs中barPosition为BarPosition.End的底部TabBar中，开启沉浸光感效果，以及弹窗类组件开启沉浸光感的使用示例。

* Navigation标题栏适配指导

  以下示例展示了通过Navigation标题栏，使得通过systemMaterial设置Column组件的沉浸光感效果生效。

  ```ts
  import { CircleShape, uiMaterial } from '@kit.ArkUI';

  @Entry
  @Component
  struct MaterialScopeAdaptExample {
    private titleHeight: number = 140

    @Builder
    customTitle() {
      Row() {
        Text('标题栏')
          .fontColor('#182431')
          .fontSize(30)
          .lineHeight(41)
          .fontWeight(700)
        Blank()
        Column() {
          SymbolGlyph($r('sys.symbol.a_3d_square_fill'))
            .fontSize(24)
        }
        .width(50)
        .height(50)
        .clipShape(new CircleShape({
          width: 50,
          height: 50
        }))
        .justifyContent(FlexAlign.Center)
        .backgroundColor(Color.Transparent)
        // 在Navigation标题栏区域中设置Column的沉浸光感效果，处于生效范围内，沉浸光感效果生效。
        .systemMaterial(new uiMaterial.ImmersiveMaterial({
          style: uiMaterial.ImmersiveStyle.THIN,
        }))
      }
      .alignItems(VerticalAlign.Center)
      .width('100%')
      .height(this.titleHeight)
      .padding(16)
    }

    build() {
      Column() {
        Navigation() {
          Column() {
            // 内容
          }
          .width('100%')
          .height('100%')
          .padding(16)
          .backgroundColor('#FFFFFF')
          .linearGradient({
            angle: 0,
            colors: [
              ['#004AAF', 0.0],
              ['#2787D9', 0.5],
              ['#F0FAFF', 1.0]
            ]
          })
          .justifyContent(FlexAlign.Center)
          .alignItems(HorizontalAlign.Center)
        }
        .title({ builder: this.customTitle, height: this.titleHeight },   { barStyle: BarStyle.STACK })
        .titleMode(NavigationTitleMode.Full)

        // 在沉浸光感生效范围外，通过systemMaterial设置Column组件的沉浸光感效果，沉浸光感效果不生效。
        // this.customTitle()
      }.width('100%').height('100%').backgroundColor('#F1F3F5')
    }
  }
  ```

  在自定义组件中，为Column组件设置了沉浸光感，处于生效范围外，沉浸光感效果不生效。示例图片如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/pE6TKFW6Qbqw0uLGHecz1Q/zh-cn_image_0000002743963725.jpg)

  在Navigation标题栏中，为Column组件设置了沉浸光感，处于生效范围内，沉浸光感效果生效。示例图片如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/iQdqd9f3QoSG01S3BfL0-g/zh-cn_image_0000002714524792.jpg)
* 底部TabBar适配指导

  以下示例展示了使用底部TabBar，使得通过systemMaterial设置Column组件的沉浸光感效果生效。

  ```ts
  import { CircleShape, uiMaterial } from '@kit.ArkUI';

  @Entry
  @Component
  struct TabsCustomTabBarExample {
    @Builder
    tabItem(icon: Resource) {
      Column() {
        Column() {
          SymbolGlyph(icon)
            .fontSize(24)
        }
        .width(48)
        .height(48)
        .clipShape(new CircleShape({
          width: 48,
          height: 48
        }))
        .justifyContent(FlexAlign.Center)
        .backgroundColor(Color.Transparent)
        // 在Tabs的底部TabBar区域中设置Column的沉浸光感，处于生效范围内，沉浸光感效果生效。
        .systemMaterial(new uiMaterial.ImmersiveMaterial({
          style: uiMaterial.ImmersiveStyle.THIN,
        }))
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center)
    }

    @Builder
    customTabBar() {
      Row() {
        this.tabItem($r('sys.symbol.house_fill'))
        this.tabItem($r('sys.symbol.search_things'))
        this.tabItem($r('sys.symbol.person_fill'))
      }
      .alignItems(VerticalAlign.Center)
      .justifyContent(FlexAlign.SpaceEvenly)
      .height(96)
      .padding({ left: 16, right: 16, bottom: 16 })
    }

    build() {
      Column() {
        Tabs({ barPosition: BarPosition.End }) {
          TabContent() {
            Column()
              .width('100%')
              .height('100%')
              .backgroundColor('#FFFFFF')
              .linearGradient({
                angle: 0,
                colors: [
                  ['#004AAF', 0.0],
                  ['#2787D9', 0.5],
                  ['#F0FAFF', 1.0]
                ]
              })
          }
          .tabBar(this.tabItem($r('sys.symbol.house_fill')))
          TabContent() {
            Column()
              .width('100%')
              .height('100%')
              .backgroundColor('#FFFFFF')
          }
          .tabBar(this.tabItem($r('sys.symbol.search_things')))
          TabContent() {
            Column()
              .width('100%')
              .height('100%')
              .backgroundColor('#FFFFFF')
          }
          .tabBar(this.tabItem($r('sys.symbol.person_fill')))
        }
        .barFloatingStyle({
          adaptToHandedness: true,
          systemMaterial: new uiMaterial.ImmersiveMaterial({ style: uiMaterial.ImmersiveStyle.THIN,   colorInvert: false })
        })
        .barOverlap(true)
        .width('100%')
        .height('100%')

        // 在沉浸光感生效范围外，通过systemMaterial设置Column组件的沉浸光感效果，沉浸光感效果不生效。
        // this.customTabBar()
      }.width('100%').height('100%').backgroundColor('#F1F3F5')
    }
  }
  ```

  在自定义组件中，为Column组件设置了沉浸光感，处于生效范围外，沉浸光感效果不生效。示例图片如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/7PH1Vp4tS-q_YHInhpuTzg/zh-cn_image_0000002744123697.jpg)

  在底部TabBar中，为Column组件设置了沉浸光感，处于生效范围内，沉浸光感效果生效。示例图片如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/lLjvejzAS8KkI0IxQAC8JQ/zh-cn_image_0000002714364830.jpg)
* 弹窗类组件沉浸光感使用示例

  由于不处于Navigation/NavDestination标题栏或Tabs的底部TabBar的区域内，因此以下两个场景，设置于背板的沉浸光感效果不会生效：

  + 使用Stack组件堆叠的形式配合组件可见性实现的类弹窗效果。
  + 设置于自定义弹窗外层容器组件上的沉浸光感效果。

  上述两种场景，若想生效沉浸光感效果，建议使用弹窗类组件和弹窗类接口配合沉浸光感属性进行改造。以下示例展示了通过[CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)的systemMaterial属性开启沉浸光感。

  ```ts
  import { uiMaterial } from '@kit.ArkUI';

  @CustomDialog
  struct CustomDialogExample {
    controller?: CustomDialogController;

    build() {
      Column() {
        Text('这是自定义弹窗')
          .fontSize(30)
          .height(100)
        Button('点我关闭弹窗')
          .onClick(() => {
            if (this.controller != undefined) {
              this.controller.close();
            }
          })
          .margin(20)
      }
      // 在自定义弹窗外层容器上设置沉浸光感效果，不处于沉浸光感的生效区域中，沉浸光感效果不生效
      // .systemMaterial(new uiMaterial.ImmersiveMaterial({
      //   style: uiMaterial.ImmersiveStyle.ULTRA_THIN,
      // }))
    }
  }

  @Entry
  @Component
  struct CustomDialogUser {
    dialogController: CustomDialogController | null = new CustomDialogController({
      builder: CustomDialogExample(),
      systemMaterial: new uiMaterial.ImmersiveMaterial({ style: uiMaterial.ImmersiveStyle.ULTRA_THIN })
    })

    build() {
      Stack({ alignContent: Alignment.Top }) {
        Column() {
          Button('CustomDialog')
            .margin(20)
            .onClick(() => {
              if (this.dialogController != null) {
                this.dialogController.open();
              }
            })
        }
        .height('100%')
        .width('100%')
        .linearGradient({
          angle: 0,
          colors: [
            ['#004AAF', 0.0],
            ['#2787D9', 0.5],
            ['#F0FAFF', 1.0]
          ]
        })
      }
    }
  }
  ```

  使用CustomDialog的systemMaterial属性开启弹窗的沉浸光感效果，示例图片如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/3aZJ6UbfTvy1QevEmulnPw/zh-cn_image_0000002743963727.jpg)

## Core File Kit

### 沙箱路径/storage/Users/currentUser/appdata下无权限目录的stat和access行为变更

**变更原因**

为强化沙箱路径下的安全机制，应用对/storage/Users/currentUser/appdata下的目录进行stat和access时，需严格遵循权限管控设计，确保仅可访问有权限的目录及文件。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

* 变更前：应用对沙箱路径/storage/Users/currentUser/appdata下没有权限的目录执行stat和access时，可以成功。
* 变更后：应用对沙箱路径/storage/Users/currentUser/appdata下没有权限的目录执行stat和access时，无法成功。

**起始 API Level**

9

**变更的接口/组件**

musl/sys/stat.h中stat、fstat、fstat64、fstatat等接口。

musl/unistd.h中access、faccessat等接口。

**适配指导**

排查及适配步骤如下：

1. 检查是否有硬编码访问：/storage/Users/currentUser/appdata/el2/{本应用包名}/files/路径。

   适配建议：删除硬编码逻辑，访问本应用路径可以转化为沙箱路径/data/storage/el2/base/files/。
2. 检查是否有硬编码访问：/storage/Users/currentUser/appdata/el2/{其他应用包名}/files/路径。

   适配建议：

   * 如果其他应用未对本应用授权，先获取授权再进行访问。
   * 如果其他应用已对本应用授权，无需整改。

## Localization Kit

### 国际化-I18n模块部分新增接口错误码的类型从string变更为number

**变更原因**

系统错误码类型默认为number类型，Localization Kit接口的实现一直使用string类型。从API版本26.0.0开始，Localization Kit新增接口的错误码类型变更为number类型。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更涉及的接口为26.0.0 Beta版本新增接口，因此仅在26.0.0 Beta版本上新建应用或已将应用升级至26.0.0 Beta版本的开发者需予以关注。

从API版本26.0.0开始，新增接口的错误码类型为number类型，此前版本接口的错误码类型仍为string类型。

**起始API Level**

26.0.0

**变更的接口/组件**

* i18n.ChineseCalendar.setChineseCalendarTime
* i18n.ChineseCalendar.checkLeapMonth
* i18n.TimeZone.setAppDefaultTimeZoneById
* i18n.Unicode.detectEncoding
* i18n.I18NUtil.setUnicodeWrappedBidiDirection
* i18n.I18NUtil.convertCanonicalLocaleIdentifier
* i18n.SymbolDateTimeFormat.constructor
* i18n.SymbolDateTimeFormat.format
* i18n.SymbolDateTimeFormat.formatToParts
* i18n.SymbolDateTimeFormat.formatRange
* i18n.SymbolDateTimeFormat.formatRangeToParts
* i18n.SymbolDateTimeFormat.parse
* i18n.SymbolNumberFormat.constructor
* i18n.SymbolNumberFormat.format
* i18n.SymbolNumberFormat.formatToParts
* i18n.SymbolNumberFormat.formatRange
* i18n.SymbolNumberFormat.formatRangeToParts
* i18n.SymbolNumberFormat.parse

**适配指导**

接口默认行为变更。请开发者确认此变更是否影响业务逻辑（如错误码类型判断），如有影响需进行适配。

## MDM Kit

### 企业设备管理服务部分接口错误码的类型从string变更为number

**变更原因**

系统错误码类型应为number类型，而企业设备管理服务接口的实现一直使用string类型。为规范数据类型，从API版本26.0.0开始，企业设备管理服务新增接口的错误码类型变更为number类型。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更涉及的接口为26.0.0 Beta版本新增接口，因此仅在26.0.0 Beta版本上新建应用或已将应用升级至26.0.0 Beta版本的开发者需予以关注。

* 变更前：企业设备管理服务接口错误码类型为string类型。
* 变更后：企业设备管理服务接口错误码类型为number类型。

```ts
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
 
let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
 
let bundleNames: Array<string> = ['com.example.notificationapp'];
 
try {
  applicationManager.addAllowedNotificationBundles(wantTemp, bundleNames, 100);
  console.info('Succeeded in adding allowed notification bundles.');
} catch (err) {
  console.error(`Code type is ${typeof(err.code)}`);
  // 变更前打印：Code type is string
  // 变更后打印：Code type is number
}
```

**起始API Level**

26.0.0

**变更的接口/组件**

* adminManager.enableSelfDeviceAdmin
* applicationManager.addAllowedNotificationBundles
* applicationManager.removeAllowedNotificationBundles
* applicationManager.getAllowedNotificationBundles
* applicationManager.queryBundleStatsInfos
* applicationManager.queryTrafficStats
* bundleManager.installForResult
* bundleManager.getInstalledBundleStorageStats
* deviceControl.operateDevice
* deviceSettings.setSwitchStatus
* securityManager.setScreenLockDisabledForAccount
* securityManager.isScreenLockDisabledForAccount
* securityManager.setScreenWatermarkImage
* securityManager.cancelScreenWatermarkImage
* telephonyManager.activeSim
* telephonyManager.deactiveSim
* telephonyManager.setDefaultData
* telephonyManager.getDefaultData

**适配指导**

接口默认行为变更。使用上述接口的开发者，如果业务代码使用了错误码类型判断，则需要适配。

以 applicationManager.addAllowedNotificationBundles为例，适配方法如下：

```ts
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
 
let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
 
let bundleNames: Array<string> = ['com.example.notificationapp'];
 
try {
  applicationManager.addAllowedNotificationBundles(wantTemp, bundleNames, 100);
  console.info('Succeeded in adding allowed notification bundles.');
} catch (err) {
  // 必须使用 number 类型进行判断
  if (err.code === 9200001) {
    // 相关业务操作
  }
}
```
