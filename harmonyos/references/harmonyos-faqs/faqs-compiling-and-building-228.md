---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-228
title: 自定义Hvigor插件是否能进行断点调试
breadcrumb: FAQ > DevEco Studio > 编译构建 > 自定义Hvigor插件是否能进行断点调试
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1f09f28224eba151dd57539800052ad5d8c753339d998c0e5f08cbc4d7885395
---

## 问题现象

自定义Hvigor插件如何调试？

## 背景知识

* Hvigor允许开发者实现自己的插件，开发者可以定义自己的构建逻辑，并与他人共享，参考[开发Hvigor插件](../harmonyos-guides/ide-hvigor-plugin.md)。
* Node.js的Inspector模块是用于启用和管理V8 Inspector的内置模块，它允许开发者通过Chrome DevTools远程调试和检查运行中的Node.js应用程序。

## 解决方案

* hvigorfile.ts文件暂时不支持在DevEco Studio调试。
* 可借助Node.js的Inspector模块通过Chrome DevTools进行断点调试，具体步骤如下：
  1. 在hvigorfile.ts通过open启动调试器并等待连接：

     ```screen
     import { hapTasks } from '@ohos/hvigor-ohos-plugin';
     import { HvigorPlugin, HvigorNode } from '@ohos/hvigor';
     import { open } from 'inspector';

     /**
      * open(port?: number, host?: string, wait?: boolean): void
      * port：用于监听检查器连接的端口。
      * host：用于监听检查器连接的主机。
      * wait：阻塞直到有客户端连接。
      */
     open(9229, undefined, true);

     // 自定义插件
     function customPlugin(): HvigorPlugin {
       return {
         pluginId: 'customPlugin',
         apply(node: HvigorNode): void {
           debugger
           console.info("hello customPlugin");
         }
       }
     }

     export default {
       system: hapTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
       plugins: [
         customPlugin()
       ]       /* Custom plugin to extend the functionality of Hvigor. */
     }
     ```
  2. 打开Chrome调试页面：chrome://inspect/#devices：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/YbdCc0FdQlOBlwJmnoDt3Q/zh-cn_image_0000002658928587.png "点击放大")
  3. 勾选“Discover network targets”，点击Configure按钮：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/N1jgr0UITEeqKidK_LeAjw/zh-cn_image_0000002658808637.png "点击放大")
  4. 配置监听接口，勾选“Enable port forwarding”，点击Done：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/VdA7sXxeTNqD-xRuiVEC2w/zh-cn_image_0000002628569272.png "点击放大")
  5. 回到DevEco Studio界面，执行构建：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/rYfBcWX3TGKcY-EWhQfNxg/zh-cn_image_0000002628409366.png "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/D3dmiQ4cQkenhUp07JQCgQ/zh-cn_image_0000002658928589.png "点击放大")
  6. 切换至Chrome调试页面，点击“inspect”，即可开始调试：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/ysts6cKdTFqyHMtx6hr6zA/zh-cn_image_0000002658808639.png "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/w1svjcfETAW0OLcaTUHxYg/zh-cn_image_0000002628569274.png "点击放大")
  7. 调试如果开启了[守护进程](../harmonyos-guides/ide-hvigor-daemon.md)，二次构建时会因守护进程还在出现以下报错，[关闭当前工程的守护进程](../harmonyos-guides/ide-hvigor-daemon.md#section298519112359)重新执行步骤5即可：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/D_zMFb2hQweuKgTCi9-MFQ/zh-cn_image_0000002628409368.png "点击放大")
