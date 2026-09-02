---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1241
title: 窗口旋转方向设置异常
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 窗口旋转方向设置异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-08-27
content_hash: sha256:1bbb8a659463d5cb471703a115cf3d313b4b01107c180f274eff327520ee4f78
---

## 问题现象

用户打开应用尝试切换横屏或竖屏时，切换失败。

## 背景知识

* 配置[module.json5](../harmonyos-guides/module-configuration-file.md)的"orientation"字段可以对应用启动时的旋转策略进行设置。
* 调用应用窗口的[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)可以设置进入应用后修改窗口的显示方向属性，该方法是对显示方向做持久化操作，因此在部分页面有特殊适配时，在进入页面进行相应的方向设置，退出页面需要恢复初始设置。
* [窗口方向](../best-practices/bpta-multi-device-window-direction.md)：窗口是运行在屏幕上的一个可交互的图形界面区域，属于软件层面，窗口方向代表的是窗口旋转策略。
* [Orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)：窗口显示方向类型枚举。

## 问题定位

1. 检查代码，在代码中全局搜索module.json5的orientation字段，看是否应用在启动时设置了横竖屏切换。
2. 代码全局中有setPreferredOrientation方法，检查方法设置的参数是否设置成了强制横屏或强制竖屏；或在日志中搜索关键字orientation，如果发现有setWindowOrientation: 1 Succeeded.或OnSetPreferredOrientation end, window [xxxx, xxxx] orientation=1信息。使用orientation的枚举值来判断，如为1时，表示竖屏显示模式，其他枚举值参考背景知识。
3. 代码中既没有在module.json5内配置orientation字段，也没有通过setPreferredOrientation方法设置屏幕方向。

## 分析结论

1. 应用module.json5文件的orientation配置项是固定方向，导致无法横竖屏切换。
2. 应用内配置了setPreferredOrientation(window.Orientation.PORTRAIT)或者setPreferredOrientation(window.Orientation.LANDSCAPE)，使得应用只能竖屏或者横屏展示，导致无法进行横竖屏切换。
3. 应用没有设置setPreferredOrientation方法或module.json5的orientation字段导致不能横竖屏切换。

## 修改建议

1. 将module.json5文件中"orientation"配置项改为可随屏幕重力方向旋转的字段，例如auto\_rotation。详见[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)。
2. 在代码中通过调用窗口window的setPreferredOrientation方法进行设置，例如设置为AUTO\_ROTATION\_RESTRICTED跟随传感器自动旋转且受控制中心的旋转开关控制。代码如下：

   ```ts
   import { common } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';

   @Entry
   @Component
   struct OrientationUsagePage {
     message: string = '横竖屏切换示例';

     aboutToAppear(): void {
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       let windowClass: window.Window = context.windowStage.getMainWindowSync();
       windowClass.setPreferredOrientation(window.Orientation.AUTO_ROTATION_RESTRICTED); // 设置屏幕方向为跟随传感器自动旋转且受控制中心的旋转开关控制。
       let systemBarProperties: window.SystemBarProperties = {
         statusBarColor: '#00000000',
       };
       windowClass.setWindowSystemBarProperties(systemBarProperties); // 设置状态栏背景色为透明
     }

     build() {
       Column() {
         Text(this.message)
           .fontSize(30)
           .fontWeight(FontWeight.Bold)
       }
       .height('100%')
       .width('100%')
       .justifyContent(FlexAlign.Center)
     }
   }
   ```

## 常见FAQ

Q：如何区分应用主动旋转屏幕与系统自动旋转？

A：筛选日志关键词SetRequestedOrientation，如果出现类似如下日志，则说明应用主动调用[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)方法旋转屏幕：

```txt
  C04202/应用包名/WMSMain                                  应用包名  I     [] SetRequestedOrientation(2865): id:94 lastReqOrientation:1 target:2 state:2
  C04200/com.ohos.sceneboard/SceneSession     com.ohos.sceneboard   I     (5194)SetRequestedOrientation: id: 94 orientation: 2
  C04202/应用包名/WMSMain                                  应用包名  I     [] SetRequestedOrientation(2865): id:94 lastReqOrientation:2 target:2 state:2
```

Q：进入页面，一直在横竖屏切换，该如何排查？

A：可以按照上一个FAQ确认应用是否主动切换横竖屏。如果是，则需要重点排查横竖屏切换后触发的监听事件（如媒体查询、窗口大小变化等），检查其中的业务逻辑，确认是否是触发了横竖屏切换-监听事件-横竖屏切换的死循环。
