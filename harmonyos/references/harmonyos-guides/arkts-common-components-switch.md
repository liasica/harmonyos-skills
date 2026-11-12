---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-switch
title: 切换按钮 (Toggle)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 按钮与选择 > 切换按钮 (Toggle)
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:9e467357bc71db0f30dc2b4bc33f3f6fd9f195e0ffc9d9a87d9ec952c961a31c
---

Toggle组件提供状态按钮样式、勾选框样式和开关样式，一般用于两种状态之间的切换。具体用法请参考[Toggle](../harmonyos-references/ts-basic-components-toggle.md)。

## 创建切换按钮

Toggle通过调用[ToggleOptions](../harmonyos-references/ts-basic-components-toggle.md#toggleoptions18对象说明)来创建，具体调用形式如下：

```ts
Toggle(options: { type: ToggleType, isOn?: boolean })
```

其中，ToggleType为切换类型，包括Button、Checkbox和Switch，isOn为切换按钮的状态。

API version 11开始，Checkbox默认样式由圆角方形变为圆形。

接口调用有以下两种形式：

* 创建不包含子组件的Toggle。

  当ToggleType为Checkbox或者Switch时，用于创建不包含子组件的Toggle：

  ```typescript
  Toggle({ type: ToggleType.Checkbox, isOn: false }).id('toggle1') // 请开发者替换为实际的id
  Toggle({ type: ToggleType.Checkbox, isOn: true }).id('toggle2') // 请开发者替换为实际的id
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/BeY8s26QQVe_tvaRdew1ew/zh-cn_image_0000002786518966.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE5FB01872D3CB2484AF9CBF313F7958C8F2460CBF1D8201B708096A133F8416)

  ```typescript
  Toggle({ type: ToggleType.Switch, isOn: false }).id('toggle3') // 请开发者替换为实际的id
  Toggle({ type: ToggleType.Switch, isOn: true }).id('toggle4') // 请开发者替换为实际的id
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/bK-V-IAvTmif_vAu1l3v7Q/zh-cn_image_0000002786359038.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D32100C947226A9EAA0E581749DCB50BAFD1236D4B45EF096316EF1557A91B8)
* 创建包含子组件的Toggle。

  当ToggleType为Button时，只能包含一个子组件，如果子组件有文本设置，则相应的文本内容会显示在按钮上。

  ```typescript
  Toggle({ type: ToggleType.Button, isOn: false }) {
    Text('status button')
      .fontColor('#182431')
      .fontSize(12)
  }.width(100).id('toggle5') // 请开发者替换为实际的id

  Toggle({ type: ToggleType.Button, isOn: true }) {
    Text('status button')
      .fontColor('#182431')
      .fontSize(12)
  }.width(100).id('toggle6') // 请开发者替换为实际的id
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/7ulvme74RfKgk2clBfWh6Q/zh-cn_image_0000002815558459.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=E81DE292D9267C80429665F6E5715BB05DD0859DB6F54B675D07A40C79F2436C)

## 自定义样式

* 通过selectedColor属性设置Toggle打开选中后的背景颜色。

  ```typescript
    Toggle({ type: ToggleType.Button, isOn: true }) {
      Text('status button')
        .fontColor('#182431')
        .fontSize(12)
    }.width(100)
    .selectedColor(Color.Pink)
  // ···

    Toggle({ type: ToggleType.Checkbox, isOn: true })
      .selectedColor(Color.Pink)
      // ···
    Toggle({ type: ToggleType.Switch, isOn: true })
      .selectedColor(Color.Pink)
      // ···
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/UcSBvWNRQ1CeA-6t52AH3Q/zh-cn_image_0000002815398543.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=53C243C540253154A31A8FF49EA7E50AA547E12D2F66F1CF0146346BAE251AC8)
* 通过switchPointColor属性设置Switch类型的圆形滑块颜色，仅对type为ToggleType.Switch生效。

  ```typescript
  Toggle({ type: ToggleType.Switch, isOn: false })
    .switchPointColor(Color.Pink)
    // ···
  Toggle({ type: ToggleType.Switch, isOn: true })
    .switchPointColor(Color.Pink)
    // ···
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/VPNL46_dQWW7-FdqtDMYuQ/zh-cn_image_0000002786518968.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BE8705BAC45B76443EC41EC81314CAA947BD95219A5F9A7AB7FA1A426E3017E)

## 添加事件

除支持[通用事件](../harmonyos-references/ts-component-general-events.md)外，Toggle还用于选中和取消选中后触发某些操作，可以绑定onChange事件来响应操作后的自定义行为。

```typescript
Toggle({ type: ToggleType.Switch, isOn: false })
  .onChange((isOn: boolean) => {
    if(isOn) {
      // 需要执行的操作
      // ···
    }
  })
```

## 场景示例

Toggle用于切换蓝牙开关状态。

```typescript
// xxx.ets
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
export struct ToggleSample {
  @State message: string = 'off';
  pathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column({ space: 8 }) {
        Column({ space: 8 }) {
          Text('Bluetooth Mode: ' + this.message)
            .id('message')
          Row() {
            Text('Bluetooth')
            Blank()
            Toggle({ type: ToggleType.Switch })
              .id('toggle') // 请开发者替换为实际的id
              .onChange((isOn: boolean) => {
                if (isOn) {
                  this.message = 'on';
                  promptAction.openToast({ 'message': 'Bluetooth is on.' });
                } else {
                  this.message = 'off';
                  promptAction.openToast({ 'message': 'Bluetooth is off.' });
                }
              })
          }.width('100%')
        }
        .alignItems(HorizontalAlign.Start)
        .backgroundColor('#fff')
        .borderRadius(12)
        .padding(12)
        .width('100%')
      }
      .width('100%')
      .height('100%')
      .padding({ left: 12, right: 12 })
    }
    .backgroundColor('#f1f2f3')
    // 请将$r('app.string.ToggleCaseExample_title')替换为实际资源文件，在本示例中该资源文件的value值为"toggle蓝牙示例"
    .title($r('app.string.ToggleCaseExample_title'))
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/0uSPHU3BSDmokZfGyAzWGg/zh-cn_image_0000002786359040.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=46957984862D367F9CD89DC5284E5C94346C32320DC05534E735FEB624348226)
