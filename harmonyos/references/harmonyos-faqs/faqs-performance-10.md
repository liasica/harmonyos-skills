---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-10
title: H5页面中的图片、视频加载缓慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > H5页面中的图片、视频加载缓慢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:16e6b3292812ca02daf23a8496a2af2a54f7deb504b4077996b0b14259bf3e49
---

## 问题现象

浏览应用内带有图片、视频的内容时，出现加载慢的现象。

## 背景知识

* [ArkWeb](../harmonyos-guides/web-component-overview.md)提供了Web组件，页面加载是Web组件的基本功能。可以在Web组件创建时指定默认加载的网络页面，后续需要变更页面，可以通过loadUrl()接口加载指定的网页。
* [图片资源加载优化](../best-practices/bpta-texture-compression-improve-performance.md)：在应用开发中，当图片资源数量或大小超过特定阈值时，由于图片资源的格式需要通过CPU解压缩为纹理格式才能直接被GPU读取，将增加CPU的处理时间，导致图片加载延迟，此时应采用图片资源加载优化方案优化图片资源的处理。
* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，开发者可以借助它预览真机或模拟器中的UI效果，快速定位布局层级问题，也可以观察组件属性、不同组件之间的关系等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/TbTjqBikQQGfgtK_RNnO_g/zh-cn_image_0000002628395078.png "点击放大")

* [ArkWeb分析](../harmonyos-guides/ide-profiler-arkweb.md)：DevEco Profiler提供的ArkWeb加载和丢帧等问题分析模板，可以结合ArkWeb执行流程的关键Trace点来定位问题发生的阶段。如果问题发生在渲染阶段，可以结合H:RosenWeb数据，线程运行状态以及帧渲染流程打点数据，进一步分析丢帧问题。

  Web页面加载流程Trace关键点：

  | Web网页加载流程拆解 | Trace关键字 |
  | --- | --- |
  | 应用收到点击事件 | DispatchTouchEvent |
  | Web组件初始化 | NWebImpl|CreateNWeb |
  | 导航 | H:LocalFrame::Navigate| url=https://xxx |
  | 创建URLLoader加载图片资源 | H:URLLoader::URLLoader | url=https://xxx |
  | 启动请求 | H:HttpCacheTransaction::Start | url=https://xxx |
  | 创建HttpStream | H:HttpNetworkTransaction::DoCreateStream |url=https://xxx |
  | 发送请求 | H:HttpNetworkTransaction::DoSendRequestComplete | url=https://xxx |
  | 接收到响应头 | H:HttpNetworkTransaction::DoReadHeadersComplete | url=https://xxx |
  | 开始接收响应体 | H:NavigationBodyLoader::StartLoadingBody |url=https://xxx |
  | 数据接收完成 | H:URLLoader::NotifyCompleted | responseCode | url=https://xxx |
  | 绘制 | H:SingleThreadProxy::ScheduledActionSendBeginMainFrame |
  | 渲染 | NotifyReadyToCommitOnImpl |
  | 完成时延结束 | SkiaOutputSurfaceImplOnGpu::SwapBuffers |
* Web页资源加载全流程：

  不同于HarmonyOS ArkUI页面，Web页面的所有信息均是通过URL链接获取，在本地解析成DOM结构后渲染为适配当前设备屏幕比例、可操控的页面。全流程分为三大部分：浏览器控制流程，资源下载流程，渲染送显流程。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/i5hdUGHfTR-I-ZSWZcPNqg/zh-cn_image_0000002658914299.png "点击放大")
  + 浏览器控制流程主要负责处理用户输入、创建Web组件、管控资源下载流程和渲染送显流程：
    1. 接收并处理用户输入：

       接收用户点击跳转Web页的指令，根据相应的触摸事件逻辑或指定跳转命令，获得目的URL地址、渲染坐标等信息，初始化Web组件。
    2. 创建资源下载流程和渲染送显流程：

       调用相关接口，将所需数据打包，用于初始化资源下载流程和渲染送显流程。
    3. 传递资源：

       在网络进程将页面资源下载后，打包传递给渲染进程。
    4. 关闭本次加载并释放相应资源：

       在渲染进程完成后，检查各进程状态并释放相应资源，关闭本次加载。
  + 资源下载流程：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/BSX9dQJZQ4qQg8sfjVXu2Q/zh-cn_image_0000002658794353.png "点击放大")
    1. 启动请求，创建URLRequest：

       网页加载管理器URLLoader将初始化一个含有当前网络参数的URLRequest，它将驱动一次完整的网络请求任务。
    2. 检查缓存项：

       URLRequest将从网络请求中拿到cookies并检查是否存在缓存项，如果不存在则会新建。
    3. 通过HttpStream建立网络连接：

       URLRequest请求一个已匹配缓存项的数据传输流进程HttpStream，并生成一个包含主机名、端口号等信息的socket。

       根据DNS域名服务器返回的重定向路径，发送socket，完成与接收方的TCP连接。
    4. 发送请求，读取响应头head：

       URLRequest通过传输接口格式化请求头和请求体后，发送到接收方。接收方会等待并接收响应头，向上传递给接收方的URLRequest并保存cookies。
    5. 读取响应体：

       发送方URLRequest会创建一个数据管道，并将一端传递给接收方。发送方每次会先从管道获取一个新的共享内存，再通过URLRequest写入数据，直到数据全部发送完毕。

       服务器端会接收到共享内存的读取请求并依次读取，直到读取完毕全部数据。
    6. 断开连接并销毁URLRequest：

       读取完成后，将关闭TCP连接及与这个请求相关的进程，并保存可复用的socket，最后销毁URLRequest。
  + 渲染流程：
    1. 将html转换为树形结构DOM树：

       通过html解析器，分析并拆解html页面信息，将其重构为元素相互独立的DOM树结构。再根据元素在html页面中的分布位置和形态，分析出对应ArkUI组件及其具体属性值、坐标信息。
    2. 绘制准备：

       通过图层树，实现层叠上下文，保证DOM重叠时可以用正确的顺序合成页面。再将每个图层的绘制拆分成很多小的绘制指令，组成待绘制列表。提交给合成器后会将图层划分为图块（大图层和小图层以相同大小的图块进行管理、缓存和渲染）。
    3. 渲染送显：

       将图块信息转换为带有颜色透明度信息的位图（光栅化）。之后合成器会通过viz线程向GPU\_task插入送显任务，将像素点输出到屏幕上。

## 问题定位

1. 使用Ark Inspector查看应用布局，该页面布局为Web页面。在右侧搜索框输入content确认该网页地址。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/SCK24p7WSSK2mDVuvMnKew/zh-cn_image_0000002628554986.png "点击放大")

   在浏览器中输入该网页地址，然后打开网络(Ctrl+U)，可以看到图片/视频资源地址为"https://xxx"。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/M1ft7_1lQpCGdznXwTSZGA/zh-cn_image_0000002628395092.png "点击放大")
2. 使用DevEco Studio Profiler的ArkWeb分析抓取该图片/视频资源加载过程的Trace，再根据加载流程中的Trace关键字表拆分该图片/视频资源加载过程，可找到其加载过程及耗时。

   以图片举例，具体步骤如下所示（对应图中红点标识）：

   首先将Trace关键字表中的对应关键字放入搜索框，例如“发送请求”：H:HttpNetworkTransaction::DoSendRequestComplete| url=https://xxx （改为对应的图片URL）。

   然后在搜索结果中筛选目标，找出任意一次成功复现的节点。

   最后放大该时间轴比例，直至可以清晰显示该线程的运行时长及其具体运行时间点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/n7Ks7lEqTe2aogNngF6zew/zh-cn_image_0000002658914313.png "点击放大")

   重复以上步骤，依次搜索“应用收到点击事件”、“发起请求”、“开始接收资源下载数据”、“资源下载完成”、“绘制”、“渲染完成”的Trace关键字，获知以下加载流程全景图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/b4OUHHN_QW2VZoct7XQpAQ/zh-cn_image_0000002658794361.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/zIs0GhX7Q9eyApEx8QvJuQ/zh-cn_image_0000002628554996.png "点击放大")

   选中A点时间坐标，拖向B点的时间坐标，即可标记该时间段，并显示其时长。依次标记所需时间段，可知：总时长2s，应用收到点击事件到开始接收响应体耗时137ms，下载全程耗时1.5s，渲染流程单独耗时337ms。由此可知，总时长过长的主要原因是过长的下载耗时。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/4eZ-KdXbQvCaNQds4PxrOw/zh-cn_image_0000002628395096.png "点击放大")

   复制URL到浏览器，可打开下载该图片资源，发现该图片大小为3.2M，明显超出该场景表现所需的图片资源大小，在未经充分加载优化的情况下会导致加载耗时过长。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/WgVhj-pNSfCS1NPA0Fx39Q/zh-cn_image_0000002658914315.png "点击放大")

## 分析结论

由于该图片/视频资源较大、未经过充分加载优化，导致出现加载缓慢的现象。

## 修改建议

可采取[预下载优化](../best-practices/bpta-web-develop-optimization.md#section11708113212514)和[图片资源加载优化](../best-practices/bpta-texture-compression-improve-performance.md)方案，优化图片/视频加载速度。
