---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-popup-and-menu-components-uicontext-menu
title: 不依赖UI组件的全局菜单 (openMenu)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 菜单 > 不依赖UI组件的全局菜单 (openMenu)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e02e43fdb6f443b9a9d16b94010f509628f7cf79fea33c7aed75613309d4af88
---

[菜单控制 (Menu)](arkts-popup-and-menu-components-menu.md)在使用时依赖绑定UI组件，否则无法使用。从API version 18开始，可以通过使用全局接口[openMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#openmenu18)的方式，在无UI组件的场景下直接或封装使用，例如在事件回调中使用或封装后对外提供能力。

## 弹出菜单

通过[openMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#openmenu18)可以弹出菜单。

```typescript
this.getUIContext().getPromptAction()
  .openMenu(this.contentNode, { id: targetId }, {
    enableArrow: true
  })
  .then(() => {
    hilog.info(0xFF00, 'globalOpenMenu', 'openMenu success');
  })
  .catch((err: BusinessError) => {
    hilog.error(0xFF00, 'globalOpenMenu', 'openMenu error: ' + err.code + ' ' + err.message);
  });
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/mWXJShf7Qeq6GhAY_PsuJA/zh-cn_image_0000002706673756.gif)

### 创建ComponentContent

通过调用openMenu接口弹出菜单，需要定义ComponentContent，以提供自定义弹出框的内容。详细规格可参考[ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md)说明。

```typescript
private contentNode: ComponentContent<Object> =
  new ComponentContent(this.getUIContext(), wrapBuilder(buildText), this.message, { nestingBuilderSupported: true });
```

如果在wrapBuilder中包含其他组件（例如：[Popup](../harmonyos-references/ohos-arkui-advanced-popup.md)、[Chip](../harmonyos-references/ohos-arkui-advanced-chip.md)组件），则应在创建ComponentContent时设置[nestingBuilderSupported](../harmonyos-references/js-apis-arkui-buildernode.md#buildoptions12)属性为true。

```typescript
@Builder
export function buildText(params: Params) {
  Popup({
    // 设置图标内容
    icon: {
      // 请将$r('app.media.app_icon')替换为实际资源文件
      image: $r('app.media.app_icon'),
      width: 32,
      height: 32,
      fillColor: Color.White,
      borderRadius: 10
    } as PopupIconOptions,
    // 设置文字内容
    title: {
      text: `This is a Popup title 1`,
      fontSize: 20,
      fontColor: Color.Black,
      fontWeight: FontWeight.Normal
    } as PopupTextOptions,
    // 设置消息内容
    message: {
      text: `This is a Popup message 1`,
      fontSize: 15,
      fontColor: Color.Black
    } as PopupTextOptions,
    // 设置按钮内容
    buttons: [{
      text: 'confirm',
      action: () => {
        hilog.info(0xFF00, 'globalOpenMenu', 'confirm button click');
      },
      fontSize: 15,
      fontColor: Color.Black,
    },
      {
        text: 'cancel',
        action: () => {
          hilog.info(0xFF00, 'globalOpenMenu', 'cancel button click');
        },
        fontSize: 15,
        fontColor: Color.Black
      },] as [PopupButtonOptions?, PopupButtonOptions?]
  })
}

let contentNode: ComponentContent<Object> =
  new ComponentContent(uiContext, wrapBuilder(buildText), message, { nestingBuilderSupported: true });
```

### 绑定组件信息

通过调用openMenu接口弹出菜单，需要提供绑定组件的信息[TargetInfo](../harmonyos-references/arkts-apis-uicontext-i.md#targetinfo18)。若未传入有效的target，菜单将无法弹出。

目前有两种设置target的方式。

* target的id属性设置为number类型，此时需要将id设置为对应组件的UniqueID，组件的UniqueID由系统保证唯一性。

  ```typescript
  let frameNode: FrameNode | null = this.getUIContext().getFrameNodeByUniqueId(this.getUniqueId());
  let targetId = frameNode?.getChild(0)?.getUniqueId();
  ```
* target的id属性设置为string类型，此时需要将id设置为对应组件的通用属性[id](../harmonyos-references/ts-universal-attributes-component-id.md#id)值。当无法保证id的唯一性时，如多团队开发或者复用自定义组件，可以通过设置componentId属性明确指定此id的范围来精确指定target，此时componentId属性可以设置为对应组件的父组件或者所在自定义组件的UniqueID。

  ```typescript
  build() {
    NavDestination() {
      Column() {
        Row() {
          Button('button1')
            .id(this.targetIdString)
        }

        Row() {
          Button('button2')
            .id(this.targetIdString)
        }

        Button('openMenu')
          .onClick(() => {
            let frameNode: FrameNode | null = this.uiContext.getFrameNodeByUniqueId(this.getUniqueId());
            let componentId = frameNode?.getChild(1)?.getChild(0)?.getChild(1)?.getUniqueId();
            if (componentId == undefined) {
              this.componentId = 0;
            } else {
              this.componentId = componentId;
            }
            this.promptAction.openMenu(this.contentNode, { id: this.targetIdString, componentId: this.componentId }, {
              enableArrow: true
            })
              .then(() => {
                hilog.info(0x0000, 'openMenuWithTargetIdString', 'openMenu success');
              })
              .catch((err: BusinessError) => {
                hilog.error(0x0000, 'openMenuWithTargetIdString', 'openMenu error: ' + err.code + ' ' + err.message);
              });
          })
      }
    }
  }
  ```

### 设置弹出菜单样式

通过调用openMenu接口弹出菜单，可以设置[MenuOptions](../harmonyos-references/ts-universal-attributes-menu.md#menuoptions10)中的属性调整菜单样式。title属性不生效。preview参数仅支持设置[MenuPreviewMode](../harmonyos-references/ts-universal-attributes-menu.md#menupreviewmode11)类型。

```typescript
private options: MenuOptions = { enableArrow: true, placement: Placement.Bottom };
```

## 更新菜单样式

从API version 18开始，通过[updateMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#updatemenu18)可以更新菜单的样式。支持全量更新和增量更新其菜单样式，不支持更新[MenuOptions](../harmonyos-references/ts-universal-attributes-menu.md#menuoptions10)中的showInSubWindow、preview、previewAnimationOptions、transition、onAppear、aboutToAppear、onDisappear、aboutToDisappear、onWillAppear、onDidAppear、onWillDisappear和onDidDisappear属性。

```typescript
this.getUIContext().getPromptAction()
  .updateMenu(this.contentNode, {
    enableArrow: false
  }, true)
  .then(() => {
    hilog.info(0xFF00, 'globalOpenMenu', 'updateMenu success');
  })
  .catch((err: BusinessError) => {
    hilog.error(0xFF00, 'globalOpenMenu', 'updateMenu error: ' + err.code + ' ' + err.message);
  });
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/Ldmh-MCrRFSITCi_C0TIZg/zh-cn_image_0000002706673756.gif)

## 关闭菜单

从API version 18开始，通过调用[closeMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#closemenu18)可以关闭菜单。

```typescript
this.getUIContext().getPromptAction()
  .closeMenu(this.contentNode)
  .then(() => {
    hilog.info(0xFF00, 'globalOpenMenu', 'closeMenu success');
  })
  .catch((err: BusinessError) => {
    hilog.error(0xFF00, 'globalOpenMenu', 'closeMenu error: ' + err.code + ' ' + err.message);
  });
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/KE-TAgUTR1Owvc6mURLyHQ/zh-cn_image_0000002706673756.gif)

**说明** 

由于[updateMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#updatemenu18)和[closeMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#closemenu18)依赖content来更新或者关闭指定的菜单，开发者需自行维护传入的content。

## 在HAR包中使用全局菜单

可以通过[HAR](har-package.md)包封装一个Menu，从而对外提供菜单的弹出、更新和关闭能力。

具体调用方式参考[在HAR包中使用全局气泡提示](arkts-popup-and-menu-components-uicontext-popup.md#在har包中使用全局气泡提示)。
