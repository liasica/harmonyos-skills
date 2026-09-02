---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-deveco-studio-arkts-1
title: DevEco Studio频繁出现卡顿或卡死
breadcrumb: FAQ > DevEco Studio > ArkTS语言 > 方舟编程语言（ArkTS） > DevEco Studio频繁出现卡顿或卡死
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:30cc613631deb7ffaf27fd39c1b77fbe9efa9462078fb44b222c12056910b0db
---

## 问题现象

### 场景一

* DevEco Studio内编写代码移动光标有明显卡顿。
* DevEco Studio频繁出现卡死，特别是复制完粘贴后，编写代码就会出现卡死。

### 场景二

开发者在使用DevEco Studio开发过程中，debug操作出现卡顿现象，一次debug操作需要约10分钟甚至更长时间，尝试清理缓存、重启电脑，尝试修改虚拟机可使用的最大内存等常规方法后，问题仍未解决。

## 背景知识

根据[工具简介](../harmonyos-guides/ide-tools-overview.md)可知，HUAWEI DevEco Studio是基于IntelliJ IDEA Community开源版本打造。对DevEco Studio卡顿的处理，可参考IntelliJ IDEA Community处理方式。

## 问题定位

### 场景一

1. 检查DevEco Studio卡顿或停止响应，是否显示“Low Memory”告警。
2. 检查是否已禁用metal渲染（metal为macOS的底层图形加速技术）。点击“help->Edit Custom VM Options...”，是否有如下配置：-Dsun.java2d.metal=false。
3. JavaScript实时检查项目是否开启。
4. 检查是否关闭并行模式。

### 场景二

1. 具体日志获取，通过“Help->Show Log in Explorer”,点开之后打开idea.log文件；分析idea.log无异常发现；
2. 使用抓取dump命令“jmap -dump:format=b,file=202104012.hprof 6666” 6666是DevEco Studio的pid，通过分析dump日志，发现YTRouteUtil这个文件里有很多断点；
3. 初步分析YTRouteUtil这个文件在不断的重复加载导致不断地索引sourceMap发送断点信息；
4. 通过排查代码发现Git能把断点提交上去，才会那么多断点，问题定位到是DevEco Studio断点太多引发卡顿了；
5. 经过进一步排查开发者把.idea目录提交上去了，其中.idea目录中的workspace.xml会保存断点信息。

## 分析结论

### 场景一

1. 内存不足。
2. 没有禁用metal渲染。
3. 编辑时的JavaScript实时检查动作导致CPU负载高。
4. 未关闭并行模式。

### 场景二

问题是由开发者加入过多断点引起的。由于多人协作，通过Git提交了调试断点，导致断点数量激增。建议开发者清理不必要的调试断点，避免提交.idea资源上库。

## 修改建议

### 场景一

1. 在DevEco Studio的配置文件中[手动修改虚拟机可使用的最大内存](faqs-profiler-3.md)。
2. 禁用metal渲染框架，禁用该框架会提升IDE的响应速度和整体性能，点击“help->Edit Custom VM Options...”，在打开的文件中新增以下配置：-Dsun.java2d.metal=false。
3. 关闭JavaScript相关的设置，可以减少不必要的计算和内存消耗，提高IDE工具的性能和响应速度：
   * Settings(设置)-(Editor)编辑器-(Intentions)意图下的JavaScript相关的设置取消勾选。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/OkF_529nQ6COGVYAlzg5cw/zh-cn_image_0000002658928955.png "点击放大")
   * 关闭native相关设置，通过File—>Settings—>Editor—>Inspection—>JavaScript TypeScript ArkTS—>Unregister function in native declaration file，取消Unregister function in native declaration file勾选，保存。
4. 关闭并行模式：

   打开菜单栏：File->Settings->Build, Execution, Deployment->Build Tools->Hvigor，取消勾选Execute tasks in parallel mode。

### 场景二

1. Git端处理方法：提交代码阶段避免提交.idea资源上库；
2. 本地清理非必要的调试断点方法：可以通过[断点管理](../harmonyos-guides/ide-debug-arkts-breakpoint.md#section168791742202819)工具删除不必要的断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/6b8zoS9WQM29G6T073eMsA/zh-cn_image_0000002658808999.png "点击放大")

## 常见FAQ

Q：DevEco Studio打开项目就卡在SyncData上，无法编译如何解决？

A：先尝试重启DevEco Studio，若未解决再重启电脑。
