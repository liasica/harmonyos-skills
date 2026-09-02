---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-4
title: 页面发生卡死，无法响应点击或侧滑操作
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 页面发生卡死，无法响应点击或侧滑操作
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:41073f77828310c79d4b634d2c87fa1695a0ebf0b71a6d0f027fc7eb5e82cce6
---

## 问题现象

应用内跳转页面，一直显示加载中，或长时间停留未跳转，点击或侧滑操作都无响应。

## 背景知识

* 用户在使用应用时，如果出现点击无反应或应用无响应等情况，并且持续时间超过一定限制，就会被定义为应用无响应，详情参考[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)。
* AppFreeze日志规格说明可以参考[日志规格](../harmonyos-guides/appfreeze-guidelines.md#日志规格)。
* 应用冷启动流程大致可分为以下部分：
  1. 应用进程创建、初始化：该阶段主要是系统完成应用进程的创建以及初始化的过程，解码启动页图标。
  2. 启动应用、Ability：该阶段主要是加载资源，创建和初始化Application和Ability对象，加载依赖模块。
  3. Ability和AbilityStage生命周期：该阶段主要执行Ability和AbilityStage启动生命周期的回调。
  4. 加载绘制首页：该阶段主要是加载首页内容、测量布局、刷新组件并绘制显示。
* [Network Kit（网络服务）](../harmonyos-guides/network-kit.md)主要提供的功能有http数据请求、WebSocket连接、Socket连接、网络连接管理和MDNS管理。日志http\_exec相关字段说明：
  + size：上传或者下载的数据大小（单位：byte）。
  + dns：域名解析耗时（单位：ms）。
  + connect：TCP握手耗时（单位：ms）。
  + tls：tls握手耗时（单位：ms）。
  + firstSend：开始发送数据时与发起请求的时间间隔（单位：ms）。
  + firstRecv：第一次收到服务器回复与发起请求的时间间隔（单位：ms）。
  + total：总耗时（单位：ms）。
  + redirect：表示重定向操作所花费的时间（单位：ms）。
  + errCode：表示错误代码，通常用于标识请求或响应中出现的问题。
  + RespCode：表示http响应的状态码。
  + httpVer：表示使用的http协议版本。
  + method：表示http请求的方法。
* [HiSmartPerf](../AppGallery-connect-Guides/smartperf-tool-0000001873208929.md)：无需ROOT设备，即可准确、高效地采集到应用运行时的CPU、GPU等性能数据，了解应用的性能状况。

## 场景一

### 问题定位

1. 当faultlogger目录下没有卡死日志生成时，可以结合trace进行分析。
2. 使用HiSmartPerf工具抓取该过程的trace信息，查看应用主线程，排查卡死阶段有没有耗时特别长的函数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/v8iHgYN2T5G3pV-2nSvxYw/zh-cn_image_0000002628316232.png "点击放大")
3. 从trace日志中看出，OnBackground函数执行时间超过了20s。

### 分析结论

函数执行时间过长导致应用卡死。

### 修改建议

排查函数执行耗时长的原因。

## 场景二

### 问题定位

1. 当faultlogger目录下没有卡死日志生成时，结合trace分析，也没有耗时特别长的函数，需要排查是否是页面跳转逻辑问题导致页面卡在启动页。
2. 结合代码分析页面跳转逻辑。

### 分析结论

存在页面跳转逻辑问题导致应用卡死在启动页。

### 修改建议

修复页面跳转逻辑。

## 场景三

### 问题定位

1. 当faultlogger目录下没有卡死日志生成时，使用HiSmartPerf工具抓取该过程的trace信息，结合trace分析，查看应用主线程，可以看到部分时间段无内容加载，进一步发现http请求执行时间过长，持续时间36s。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/snDtRzyaRL2KomBj8vQeIQ/zh-cn_image_0000002658675469.png "点击放大")
2. 记下TaskId=-2147483648，在hilog日志中查找对应网络请求日志。

   发现http请求报错，错误码为2300028，查询文档[HTTP错误码](../harmonyos-references/errorcode-net-http.md)。

   2300028：操作超时，可能原因为TCP连接超时或读写超时。需要排查网络或服务器问题，例如网络是否稳定、信号强度是否较弱、服务器负载是否过高、处理速度是否正常等。

   ```txt
   03-17 16:24:20.846 13583 13773 E C015B0/com.hx.example/NETSTACK: [http_exec.cpp:312] CURLcode result 28
   03-17 16:24:20.846 13583 13773 I C015B0/com.hx.example/NETSTACK: [http_exec.cpp:418] taskid=-2147483648, size:0, dns:76179.535, connect:0.000, tls:0.000, firstSend:0.000, firstRecv:0.000, total:76179.699, redirect:0.000, errCode:2300028, RespCode:0, httpVer:0, method:POST, osErr:0
   ```

3. 在应用没有freeze的情况下，网络请求超时是不会阻塞手势事件的，需要继续排查为什么点击或侧滑操作无响应，查看hilog中关于手势的日志，搜索OnInputEvent。观察到Touch test result is empty，说明触碰测试结果为空，应用前端组件未绑定事件。

   ```txt
   03-17 16:23:21.369 13583 13747 I C02805/com.hx.example/InputKeyFlow: [P:D:22511][OnPointerEvent:508] id:22511 recv
   03-17 16:23:21.369 13583 13747 I C04213/com.hx.example/InputKeyFlow: [] OnInputEvent(86): eid:4,InputId:22511,wid:77,action:2
   03-17 16:23:21.370 13583 13747 W C04219/com.hx.example/WMSDecor:  [invalidDomain][] GetDecorHeight(2212): Get app window decor height failed
   03-17 16:23:21.370  3529  3533 I C04200/com.ohos.sceneboard/Session: (2120)TransferPointerEvent: Session TransferPointEvent, eventId:22511, action:down, persistentId:77, bundleName:, pid:13583
   03-17 16:23:21.370 13583 13747 I C0420C/com.hx.example/WMSEvent: [] NotifyPointerEvent(3782): Input id:22511
   03-17 16:23:21.370 13583 13747 I C0420C/com.hx.example/WMSEvent: [] NotifyPointerEvent(3784): Start to process pointerEvent, id: 22511
   03-17 16:23:21.370 13583 13747 I C03919/com.hx.example/AceInputTracking: [(-1:100000:singleton)] pointdown windowId: 77
   03-17 16:23:21.370 13583 13747 I C04213/com.hx.example/InputKeyFlow: [] ConsumePointerEventInner(818): InputId:22511,wid:77,pointId:0,srcType:2,rect:[0,0,1320,2120],notify:1
   03-17 16:23:21.371 13583 13747 I C02805/com.hx.example/InputKeyFlow: [][OnPointerEvent:215] ac: move: 22512
   03-17 16:23:21.371 13583 13747 I C0420C/com.hx.example/WMSEvent: [] NotifyPointerEvent(3784): Start to process pointerEvent, id: 22512
   03-17 16:23:21.371 13583 13583 I C03951/com.hx.example/InputKeyFlow: [(100000:100000:scope)] InputTracking id:22511, fingerId:0, type=0, inject=0, isPrivacyMode=0
   03-17 16:23:21.371 13583 13747 I C0420C/com.hx.example/WMSEvent: [] NotifyPointerEvent(3784): Start to process pointerEvent, id: 22513
   03-17 16:23:21.371 13583 13583 I C03951/com.hx.example/InputKeyFlow: [(100000:100000:scope)] InputTracking id:22511, touch test hitted node info: fingerId: 0
   03-17 16:23:21.371 13583 13583 W C03951/com.hx.example/InputKeyFlow: [(100000:100000:scope)] Touch test result is empty.
   03-17 16:23:21.371 13583 13583 I C03951/com.hx.example/InputKeyFlow: [(100000:100000:scope)] InputTracking id:22511, touch test hitted recognizer type info: 
   03-17 16:23:21.371 13583 13583 I C03919/com.hx.example/AceInputTracking: [(100000:100000:scope)] Hitted recognizer info is empty.
   03-17 16:23:21.372 13583 13747 I C0420C/com.hx.example/WMSEvent: [] NotifyPointerEvent(3784): Start to process pointerEvent, id: 22514
   03-17 16:23:21.372 13583 13583 I C03919/com.hx.example/AceInputTracking: [(100000:100000:scope)] Consumed new event id=22511 in ace_container, lastEventInfo: id:22509
   ```

### 分析结论

网络超时导致页面一直加载，组件未绑定事件导致无响应。

### 修改建议

检查设备网络是否稳定，检查服务器是否能正常建立连接并传输数据。
