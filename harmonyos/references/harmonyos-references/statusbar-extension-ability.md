---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/statusbar-extension-ability
title: StatusBarViewExtensionAbility（状态栏扩展Ability）
breadcrumb: API参考 > 系统 > 基础功能 > Desktop Extension Kit（桌面拓展服务） > ArkTS API > StatusBarViewExtensionAbility（状态栏扩展Ability）
category: harmonyos-references
scraped_at: 2026-09-02T15:02:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:08b6c16ebb99cadb54ff03d8cb2af4eeca2a7958fa0ae1e95295fb5e481d7477
---

StatusBarViewExtensionAbility为状态栏扩展Ability，继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md#uiextensionability)，用于给应用提供接入状态栏图标左键业务弹窗的能力。

**说明** 

本模块接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { StatusBarViewExtensionAbility } from '@kit.DeskTopExtensionKit';
```

**示例：**

```typescript
import { StatusBarViewExtensionAbility } from '@kit.DeskTopExtensionKit';
import { UIExtensionContentSession, Want } from '@kit.AbilityKit';

let TAG = 'MyStatusBarViewAbility';

export default class MyStatusBarViewAbility extends StatusBarViewExtensionAbility {
  // 当StatusBarViewExtensionAbility组件实例完成创建时，系统会触发该回调。
  onCreate() {
    console.info(TAG, 'onCreate');
  }

  // 当UIExtensionContentSession实例创建完成后，系统会触发该回调。
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    console.info(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);
    session.loadContent('pages/StatusBarPage');
  }

  // 当StatusBarViewExtensionAbility组件首次启动到前台或者从后台转入到前台时，系统触发该回调。
  onForeground() {
    console.info(TAG, 'onForeground');
  }

  // 当StatusBarViewExtensionAbility组件从前台转入到后台时，系统触发该回调。
  onBackground() {
    console.info(TAG, 'onBackground');
  }

  // 当UIExtensionContentSession实例销毁后，系统触发该回调。
  onSessionDestroy(session: UIExtensionContentSession) {
    console.info(TAG, 'onSessionDestroy');
  }

  // 当StatusBarViewExtensionAbility组件被销毁时，系统触发该回调。
  onDestroy() {
    console.info(TAG, 'onDestroy');
  }
}
```
