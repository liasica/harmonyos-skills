---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-889
title: 使用restore时出现801和1300004错误码时如何处理
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 使用restore时出现801和1300004错误码时如何处理
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:63dc54b920097388cbea8db81c6a2364318dfc4de37bca71a2ec138276268721
---

## 问题现象

使用平板和PC设备运行官网[restore()](../harmonyos-references/arkts-apis-window-window.md#restore14)示例代码，分别出现801错误码和1300004错误码。

使用平板出现错误码801：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/QOTu5SXCSduHjaH8wRYdoQ/zh-cn_image_0000002658918855.png "点击放大")

使用PC设备出现错误码1300004：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/QiuaMdsuRPafD46alrm7ag/zh-cn_image_0000002628399640.png "点击放大")

## 背景知识

* [minimize](../harmonyos-references/arkts-apis-window-window.md#minimize11)：调用对象不同，实现不同的功能：
  + 当调用对象为主窗口时，实现最小化功能，可在Dock栏中还原，2in1设备上可以使用[restore()](../harmonyos-references/arkts-apis-window-window.md#restore14)进行还原。
  + 当调用对象为子窗口或悬浮窗时，实现隐藏功能，不可在Dock栏中还原，可以使用[showWindow()](../harmonyos-references/arkts-apis-window-window.md#showwindow9)进行还原。
* restore：将主窗口从最小化状态，恢复到前台显示，并恢复到进入该模式之前的大小和位置。常见使用场景如下：
  + 窗口从后台恢复到前台时（如从最小化状态恢复）。
  + 多窗口分屏模式下恢复窗口布局。
  + 配合minimize()实现自定义窗口动画效果。
* [deviceTypes](../harmonyos-guides/module-configuration-file.md#devicetypes标签)：标识当前Module可以运行在哪类设备上（当存在多个模块时，各模块的配置可以不同，但都必须包含将要安装的设备类型，以确保正常运行）。

  **说明** 

  + restore()仅在多窗层叠布局效果下生效，仅在主窗口为最小化状态且UIAbility生命周期为onForeground时生效。
  + restore()仅可在2in1设备或平板设备的自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下使用。

## 问题定位

```screen
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    try {
      let windowClass = windowStage.getMainWindowSync();
      // 调用minimize,使主窗最小化
      setTimeout(() => {
        windowClass.minimize();
        console.info('窗口最小化');
      }, 3000);
      // 设置延时函数延时5秒钟后对主窗进行恢复。
      setTimeout(() => {
        console.info('定时器运行');
        // 调用restore()函数对主窗进行恢复。
        let promise = windowClass.restore();
        promise.then(() => {
          console.info('Succeeded in restoring the window.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to restore the window. Cause code: ${err.code}, message: ${err.message}`);
        });
      }, 6000);
    } catch (exception) {
      console.error(`Failed to restore the window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }
};
```

* 在平板运行过后会发现应用一闪而逝，日志上查看可以看见窗口最小化成功，但是等待后发现定时器并未运行，日志也没有打印出来。在点击应用启动后出现错误码801，官网可查[801](../harmonyos-references/errorcode-universal.md#section801-该设备不支持此api)报错，该设备不支持此API因此无法调用。
* 在PC上运行后出现错误码1300004，官网可查[1300004](../harmonyos-references/errorcode-window.md#section1300004-无权限操作)报错，对误操作权限的对象进行操作时，会报此错。

## 分析结论

官网明确规定restore()在2in1设备或平板设备的自由多窗模式下使用，出现不支持此API和没有操作权限的报错，说明存在不支持的设备。

## 修改建议

可以查看下module.json5文件下deviceTypes下的有没有phone这个字段。

```screen
"deviceTypes": [
  "phone",
  "tablet"
],
```

有的话把phone这个字段移除即可。
