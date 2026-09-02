---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/list-item-combination-scenarios
title: 列表项组件整体聚焦
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 列表项组件整体聚焦
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:96e1b48955a3ec22b0d470f9b2f7bf0a26dd57fc25323b3660910cacac6ac2c4
---

## 设计场景

列表包含一系列相同宽度的列表项，列表项可能由显示文本和可操控组件组合而成。显示文本通常是对可操控组件的功能性描述，类似于可操控组件的标签，因此列表项中的显示文本和可操控组件适合作为一个整体进行聚焦和播报。应用可以在列表项上设置[accessibilityGroup](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitygroup)，并通过[accessibilityOptions](../harmonyos-references/ts-types.md#accessibilityoptions14对象说明)指定可操控组件，桥接可操控组件的无障碍状态和无障碍点击事件。

### accessibilityOptions说明

* [accessibilityPreferred](../harmonyos-references/ts-types.md#accessibilityoptions14对象说明)：指定是否优先使用无障碍文本进行拼接。若accessibilityPreferred设置为true，则深度遍历每个子节点时优先选择该子节点的无障碍文本accessibilityText。若无障碍文本为空，则选择本身Text文本，最终将拼接完成的文本设置给accessibilityText与Text都为空的父节点。默认值为false，表示不启用此功能。
* [stateControllerRoleType](../harmonyos-references/ts-types.md#accessibilityoptions14对象说明)：指定特定类型的子组件用于控制容器组件的状态播报。配置accessibilityGroup的容器组件进行无障碍聚合后，会将该特定类型的子组件的选中状态和状态播报文本作为聚合组件的状态和播报文本，避免需要对子组件单独进行聚焦。如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件作为控制组件。默认值为空，表示不指定任何子组件。
* [stateControllerId](../harmonyos-references/ts-types.md#accessibilityoptions14对象说明)：指定特定唯一标识ID的子组件用于控制容器组件的状态播报。配置accessibilityGroup的容器组件进行无障碍聚合后，会将该ID对应的子组件的选中状态和状态播报文本作为聚合组件的状态和播报文本，避免需要对子组件单独进行聚焦。如果聚合组件内有多个相同ID的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。如果与stateControllerRoleType同时配置，则优先匹配ID一致的组件。默认值为空，表示不指定任何子组件。
* [actionControllerRoleType](../harmonyos-references/ts-types.md#accessibilityoptions14对象说明)：指定特定类型的子组件用于控制容器组件的操作执行。配置accessibilityGroup的容器组件进行无障碍聚合后，如果触发无障碍的控制操作时，会将操作转发给该特定类型的子组件，避免需要对子组件单独进行聚焦。当前只支持无障碍点击操作。如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。默认值为空，表示不指定任何子组件。
* [actionControllerId](../harmonyos-references/ts-types.md#accessibilityoptions14对象说明)：指定特定唯一标识ID的子组件用于控制容器组件的操作执行。配置accessibilityGroup的容器组件进行无障碍聚合后，如果触发无障碍的控制操作时，会将操作转发给该ID对应的子组件，避免需要对子组件单独进行聚焦。当前只支持无障碍点击操作。如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。如果与actionControllerRoleType同时配置，则优先匹配ID一致的组件。默认值为空，表示不指定任何子组件。

## 开发流程

如下示例将开关、单选框、复选框和标签文本组合为一个整体进行聚焦和播报：

```typescript
@Entry
@Component
export struct Rule_2_1_13 {
  title: string = 'Rule 2.1.13';
  scroller: Scroller = new Scroller();
  @State isToggleSwitch: boolean = false;
  @State isChecked: boolean = false;
  @State isSelected: boolean = false;

  build() {
    NavDestination() {
      Column() {
        Scroll(this.scroller) {
          Column({ space: 30 }) {
            Column() {
              Text("按ID接管, state和action接管, 一个 toggle, 样式为开关")
              // 指定特定唯一标识ID为toggletest1的toggle子组件，样式为开关，桥接其无障碍状态和无障碍点击事件。
              Column() {
                Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
                  Text("是否开启功能")
                  Toggle({ type: ToggleType.Switch, isOn: true })
                    .selectedColor('#007DFF')
                    .switchPointColor('#FFFFFF')
                    .onChange((isOn: boolean) => {
                      console.info('Component status:' + isOn);
                    })
                    .id("toggletest1")
                }
              }.width('100%')
              .accessibilityGroup(true, {
                stateControllerId: "toggletest1",
                actionControllerId: "toggletest1"
              })
              .border({ color: Color.Black, width: 2 }).padding(10)
            }

            Column() {
              Text("按ID接管, state和action接管, 一个 toggle, 样式为按钮")
              // 指定特定唯一标识ID为toggletest1的toggle子组件，样式为按钮，桥接其无障碍状态和无障碍点击事件。
              Column() {
                Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
                  Text("是否改变状态")
                  Toggle({ type: ToggleType.Button, isOn: true }) {
                    Text('status button').fontColor('#182431').fontSize(12)
                  }.width(106)
                  .selectedColor('rgba(0,125,255,0.20)')
                  .onChange((isOn: boolean) => {
                    console.info('Component status:' + isOn);
                  })
                  .id("toggletest1")
                }
              }.width('100%')
              .accessibilityGroup(true, {
                stateControllerId: "toggletest1",
                actionControllerId: "toggletest1"
              })
              .border({ color: Color.Black, width: 2 }).padding(10)
            }

            Column() {
              Text("按ID接管, state和action接管, 一个 toggle, 样式为单选框")
              // 指定特定唯一标识ID为toggletest1的toggle子组件，样式为单选框，桥接其无障碍状态和无障碍点击事件。
              Column() {
                Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
                  Text("是否选中功能")
                  Toggle({ type: ToggleType.Checkbox, isOn: false })
                    .selectedColor('#007DFF')
                    .switchPointColor('#FFFFFF')
                    .onChange((isOn: boolean) => {
                      console.info('Component status:' + isOn);
                    })
                    .id("toggletest1")
                }
              }.width('100%')
              .accessibilityGroup(true, {
                stateControllerId: "toggletest1",
                actionControllerId: "toggletest1"
              })
              .border({ color: Color.Black, width: 2 }).padding(10)
            }

            Column() {
              Text("按ID接管, state和action接管, 一个 raido")
              // 指定特定唯一标识ID为radiotest1的radio子组件，桥接其无障碍状态和无障碍点击事件。
              Column() {
                Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
                  Text("是否改变单选框")
                  Radio({
                    value: 'Radio2.1', group: 'radioGroup2',
                    indicatorType: RadioIndicatorType.TICK
                  })
                    .radioStyle({
                      checkedBackgroundColor: Color.Pink
                    })
                    .checked(false)
                    .height(20)
                    .width(20)
                    .onChange((isChecked: boolean) => {
                      console.info('Radio1 status is ' + isChecked);

                    })
                    .id("radiotest1")
                }
              }.width('100%')
              .accessibilityGroup(true, {
                stateControllerId: "radiotest1",
                actionControllerId: "radiotest1"
              })
              .border({ color: Color.Black, width: 2 }).padding(10)

              Radio({ value: 'Radio2.2', group: 'radioGroup2' })
                .checked(false)
                .radioStyle({
                  checkedBackgroundColor: Color.Pink
                })
                .height(20)
                .width(20)
                .onChange((isChecked: boolean) => {
                  console.info('Radio2 status is ' + isChecked);
                })
            }

            Column() {
              Text("按ID接管, state和action接管, 一个 CheckBox")
              // 指定特定唯一标识ID为checkboxtest1的checkbox子组件，桥接其无障碍状态和无障碍点击事件。
              Column() {
                Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
                  Text("是否改变复选框")
                  Checkbox({ name: 'checkbox2', group: 'checkboxGroup2' })
                    .select(true)
                    .selectedColor(0xed6f21)
                    .shape(CheckBoxShape.CIRCLE)
                    .onChange((value: boolean) => {
                      console.info('Checkbox2 change is' + value);
                    })
                    .id("checkboxtest1")
                }
              }.width('100%')
              .accessibilityGroup(true, {
                stateControllerId: "checkboxtest1",
                actionControllerId: "checkboxtest1"
              })
              .border({ color: Color.Black, width: 2 }).padding(10)
            }
          }
        }
        .scrollable(ScrollDirection.Vertical)
        .scrollBar(BarState.On)
        .friction(0.6)
        .edgeEffect(EdgeEffect.None)
        .width("100%")
      }
      .width("100%")
      .height("100%")
    }
    .title(this.title)
  }
}
```
