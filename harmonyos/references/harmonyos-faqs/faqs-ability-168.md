---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-168
title: 控制应用退至后台或直接销毁
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 控制应用退至后台或直接销毁
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-08-20
content_hash: sha256:28b6cfb3be96f813d3c5abed86da778e00c5eb644f3bd78e559efc9208ec2270
---

## 问题现象

如何通过API控制应用退至后台或者直接销毁应用？

## 背景知识

* [Window](../harmonyos-references/arkts-apis-window-window.md)是用于管理窗口的模块，主要用于构建支持多窗口场景的应用。它提供了窗口创建、生命周期管理、布局适配、多窗口切换等功能，帮助开发者高效处理复杂窗口场景。
* [terminateSelf](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself-1)销毁UIAbility自身。使用Promise异步回调。仅支持在主线程调用。

## 解决方案

* 实现将应用退至后台，可以通过@ohos.window (窗口)提供的[minimize](../harmonyos-references/js-apis-uitest.md#minimize9)方法实现。
* 实现将应用销毁，可使用terminateSelf接口停止UIAbility，默认情况下应用会在最近任务列表中保留快照，若要清理任务中心的相关任务（即不保留最近任务列表中的快照），需要在module.json5配置文件中将removeMissionAfterTerminate字段取值配置为true。示例代码如下：

Index.ets：实现应用退至后台及销毁应用逻辑。

```ts
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  build() {
    Column({ space: 16 }) {
      Button('退至后台')
        .onClick(() => {
          // 获取Context
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          // 通过Context获取windowStage
          let windowStage = context.windowStage;
          // 通过windowStage获取主窗口
          let mainWindow = windowStage.getMainWindowSync();
          // 将主窗口最小化
          mainWindow.minimize();
        });
      Button('销毁应用')
        .onClick(() => {
          // 获取Context
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          // 通过Context获取销毁应用
          context.terminateSelf()
            .then(() => {
              // 执行正常业务
              console.info('terminateSelf succeed');
            })
            .catch((err: BusinessError) => {
              // 处理业务逻辑错误
              console.error(`terminateSelf failed, code is ${err.code}, message is ${err.message}`);
            });
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

module.json5：将removeMissionAfterTerminate字段取值配置为true。

```json
"abilities": [
  {
    // 清除销毁应用快照
    "removeMissionAfterTerminate": true,
    "name": "EntryAbility",
    "srcEntry": "./ets/entryability/EntryAbility.ets",
    "description": "$string:EntryAbility_desc",
    "icon": "$media:layered_image",
    "label": "$string:EntryAbility_label",
    "startWindowIcon": "$media:startIcon",
    "startWindowBackground": "$color:start_window_background",
    "exported": true,
    "skills": [
      {
        "entities": [
          "entity.system.home"
        ],
        "actions": [
          "ohos.want.action.home"
        ]
      }
    ]
  }
],
```

## 常见FAQ

Q：锁屏的时候应用会收到minimize设计目的是什么？

A：锁屏后应用退后台会降低设备功耗问题，应用在后台CPU不会调度，可以延长设备续航时间。
