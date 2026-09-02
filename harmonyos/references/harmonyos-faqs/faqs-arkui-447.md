---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-447
title: 组件A通过bindContextMenu配置了长按菜单，点击菜单外区域，组件A响应了点击事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 组件A通过bindContextMenu配置了长按菜单，点击菜单外区域，组件A响应了点击事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9d0767c553a244785e54a77d5a65958e22eeed64fc0806a8171bf689aeaf9eee
---

**问题背景**

在组件A上通过bindContextMenu配置了长按菜单后，当用户点击菜单外区域时，会出现事件透传现象——组件A会响应点击事件。这种交互行为不符合某些场景下的设计需求，需要实现菜单弹出时完全阻断对下层组件的事件传递。

**解决措施**

当前菜单默认的模态行为是仅菜单自身区域可交互，菜单外区域保持事件穿透（点击会穿透到下层组件），默认模态模式对应的枚举值（如ModalMode.NONE）。从API 20版本开始，HarmonyOS开放了菜单模态模式的配置能力。通过将ModalMode参数设置为TARGET\_WINDOW即可实现。

**参考示例：**

```typescript
@Entry
@Component
struct ModalModeDemo {
  @State btnMessage: string = "Click To Trigger, longPress To Pop Up Menu"
  @State toastMessage: string = "The Click event was triggered."
  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ content: "MenuOptionOne" })
      MenuItem({ content: "MenuOptionTwo" })
    }
  }

  build() {
    Stack({ alignContent: Alignment.Center }) {
      Column() {
        Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
          Column() {
            Button(this.btnMessage)
              .bindContextMenu(this.MyMenu, ResponseType.LongPress, {
                modalMode: ModalMode.TARGET_WINDOW,
                placement: Placement.BottomLeft
              })
              .onClick(() => {
                this.getUIContext().getPromptAction().showToast({
                  message: this.toastMessage
                })
              })
          }
        }
      }
    }.width('100%').height('100%')
  }
}
```

**参考链接**

[菜单控制](../harmonyos-references/ts-universal-attributes-menu.md)
