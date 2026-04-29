---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-buffer-power-optimization
title: Buffer低功耗优化
breadcrumb: 最佳实践 > 功耗 > 功耗场景优化案例 > Buffer低功耗优化
category: best-practices
scraped_at: 2026-04-29T14:13:58+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:ee549ba076d029cd10c1c19ee91860877a4729c79534e61ee2b580d21988b821
---

## 概述

在HarmonyOS中，Buffer是承载自绘制内容循环渲染的主要载体，有别于Vsync统一执行的思想，自绘制内容的生产不依赖于系统事件，而是由三方主导控制。Buffer在渲染过程中通过BufferQueue来进行轮转，采用了生产者与消费者的设计思想，应用将作为生产者将生产好的渲染内容准备好后，从BufferQueue中获取并Flush Buffer，而RS则作为消费者可以通过AcquireBuffer接口获取Buffer，让该Buffer作为自绘制Surface中的一帧在屏幕上显示，并将使用后的Buffer调用ReleaseBuffer释放进入轮转池。相关的流转逻辑可以参考下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/-3EH-_5yThKuTExfKaHflw/zh-cn_image_0000002427647038.png?HW-CC-KV=V1&HW-CC-Date=20260429T061354Z&HW-CC-Expire=86400&HW-CC-Sign=CE8A50BB1612B2B0A32921CABA5A7392ABE50FE3D0DE9A83B4662F111FA6A4FC)

开发者可以通过Profiler的Trace工具分析Buffer的流转过程，可按照下图所示的顺序将相关进程置顶排列。其中OS\_IPC中包含了render\_service的跨进程通信信息，开发者可参考下图虚线所示，根据binder找到对应的生产者进程，详细的Trace点含义如下：

1. “H:RequestBuffer name: xxx queueId: 6631429506443 queueSize: 5 reserveSlotNum: 0”：位于OS\_IPC线程泳道，表明Producer申请使用了一帧Buffer，通过binder与生产者的对应进程连接，由生产者执行后续业务。
2. “H:FlushBuffer name: xxx queueId: 6631429506443 sequence: 97784886”：位于OS\_IPC线程泳道，表明名称为xxx的Surface的Buffer在此时完成内容生产，已通过BufferQueue交给了消费者侧。其中queueId是Buffer序列的独立id，sequence是每个Buffer的独立id。与此同时，OS\_IPC中还可以搜到H:rs\_RequestNextVSync，表明下一帧Vsync中，rs会被拉起执行后续业务。
3. “H:AcquireBuffer with PresentTimestamp name: xxx queueId: 6631429506443”：位于render\_service线程泳道，表明名为xxx的Surface此时在rs收集该帧的绘制诉求时，rs作为消费者请求了这个Buffer，用于后续的帧绘制。如果成功获取到了该Buffer，会在子Trace中额外打印“H:acquire buffer sequence: 97784886”。
4. “H:ReleaseBuffer name: xxx queueId: 6631429506443 seq: 97784892”：位于RSHardware或RSUniRenderThrea线程泳道，该信息通常出现在RSHardwareThread一帧中的最末尾，表明消费者已成功使用该Buffer，并释放该Buffer块，交还给BufferQueue。反之，如果ReleaseBuffer在RSUniRender中出现，则表明此时Buffer无需渲染在屏幕上，属于Buffer空跑问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/ahhtCnxvSNCkySbfUsxgMw/zh-cn_image_0000002411919048.png?HW-CC-KV=V1&HW-CC-Date=20260429T061354Z&HW-CC-Expire=86400&HW-CC-Sign=CE72E8B9C1FED69ECB42EE27FBCDFF12CADE0EDD843951FE199877B439AD8464 "点击放大")

## 分析思路

在定位问题时，开发者可以按照以下步骤来确定Buffer使用是否无误：

* 在RSHardwareThread泳道中搜索“H:ReleaseBuffer”：如图所示，在选定的时间段内RosenWeb和DisplayNode均释放了一定次数，开发者可以根据右侧的Occurrence统计其出现次数。由于BufferQueue具有循环复用的机制，同一seq会多次复用，如图中RosenWeb由5个Buffer循环复用而成。DisplayNode是应用进程下发绘制指令并经渲染后得到的统一绘制图层，大部分ArkUI组件的刷新也在DisplayNode中体现。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/nLATAtHdQiazen9FJ2-ruw/zh-cn_image_0000002445438225.png?HW-CC-KV=V1&HW-CC-Date=20260429T061354Z&HW-CC-Expire=86400&HW-CC-Sign=1E4CDDA991F5EDB63DE493A7FBEB1BF2CFE4BB108DC79A2E5A64EADFBC8D9CC1 "点击放大")

* 在RSUniRenderThre中搜索“H:ReleaseBuffer”：RSUniRenderThre中也会出现Buffer释放的流程，如下图所示，有一块RosenWeb的BufferQueue在框选时间内循环了174次，该Buffer并未实际造成显示效果，造成了Buffer空跑问题。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/oDXCe_P_TtK2fCWH264ZlQ/zh-cn_image_0000002445518321.png?HW-CC-KV=V1&HW-CC-Date=20260429T061354Z&HW-CC-Expire=86400&HW-CC-Sign=E20B1E6BAA7DA6432990A59B4170E1CF8C022B1700A5AE1670AC510B21F4F51D "点击放大")

* 在render\_service泳道中搜索“seq = [空跑Buffer id]”：发现一个空跑的BufferQueue时，可以从中找到一个Buffer id，例如100151309，并在render\_service中进行搜索。搜索结果如下，在“H:RsDebug surfaceHandler(id:xxx)”中，开发者可以确认到该Buffer所对应的RS树node id。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/HXrSNypCQeK4VxoOiEfMOQ/zh-cn_image_0000002411759188.png?HW-CC-KV=V1&HW-CC-Date=20260429T061354Z&HW-CC-Expire=86400&HW-CC-Sign=CE97FC3510C07B6DF7C8C5D34F2C27996A8398B084FBB45E0C3EF5E8B4704C75 "点击放大")

开发者可使用HiSmartPerf工具，在“整机测试-RS树可视化展示”处展开RS树，通过id查找的方式找到此BufferQueue对应的rs节点位置，定位到导致空跑问题的自绘制内容。如下图，开发者在TabIndex为0的home页面抓取Trace发现了Buffer空跑问题，通过RsDebug找到问题node id后通过id搜索，在切换至yellow页面时，发现是此处的web buffer预渲染导致的空跑问题。

注意

能够造成空跑问题的Buffer通常并不会在屏幕上显示，所以往往并不会在当前页面被发现，开发者在使用该工具时可以结合页面逻辑，上下滚动、左右切换，以及根据问题复现的步骤依次回溯路径页面来寻找有问题的RS node。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/18W94DEiR-2rOa6FHHBZWQ/zh-cn_image_0000002411919056.png?HW-CC-KV=V1&HW-CC-Date=20260429T061354Z&HW-CC-Expire=86400&HW-CC-Sign=85BA91C08A5971C33E35B4B09EA30D6C4782CCEE4A0AFA6EACE6217113AC58A8 "点击放大")

## Web预渲染优化案例

### 问题现象

[Web的预渲染](bpta-web-develop-optimization.md#section172031338172719)是一种广泛使用的性能优化手段，让Web组件在挂载之前完成渲染可以有效减少Web初次加载时的时延表现，但处理不当也同样可能引起Buffer类空跑问题。在Web类应用中，对于预加载的离线Web节点，开发者需要确保这些后台的Web处于冻结状态，不会产生持续性的冗余Buffer影响正常场景的功能。下图展示了一个在非Web首页通过Tab预加载两个Web页面的Trace，分析Buffer的Release情况，发现Trace中RSUniRenderThre的帧率表现高于实际的显示帧率，表明空跑问题存在。进一步观察发现，RSUni中有两处ReleaseBuffer，来自两个不同的queueId，由此可以推断该页面可能存在两个离线的Web组件正在后台渲染，带来冗余负载。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/J1jtcfHATxCPLW7NH7z6sA/zh-cn_image_0000002445438233.png?HW-CC-KV=V1&HW-CC-Date=20260429T061354Z&HW-CC-Expire=86400&HW-CC-Sign=12C62304C9C8C9054E72C9873D5E7015E4FD89B8CF6B51E2C78875DA29DC59CA "点击放大")

开发者可以通过HiSmartPerf的RS树工具定位Buffer位置，除此之外，推荐开发者充分利用Web DevTools工具，参考[使用DevTools工具调试前端页面](../harmonyos-guides/web-debugging-with-devtools.md)，开发者可以通过端口投射的方式展示当前页面中所有的Web页面加载情况。如下图所示，端口投射成功后“1”处填写投射端口，“2”处将显示所有创建成功的web对象，点击其中的两个网页可查看其当前活跃状态，如“3”“4”则分别对应了处于冻结状态和活跃状态的页面，点击inspect观察表现情况。这种活跃/冻结状态可以调用WebController.onActive/onInactive来控制，原则上，并非在屏幕显示范围内的Web不应处于活跃状态，避免带来Buffer空跑问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/meVtVIcuSXahF3PGCP9COg/zh-cn_image_0000002445518329.png?HW-CC-KV=V1&HW-CC-Date=20260429T061354Z&HW-CC-Expire=86400&HW-CC-Sign=83A91A71D8497AF2447A11995BC7D01576B35F3849DEB4F9C733B74CA7089629 "点击放大")

### 优化思路

说明

当前系统对Web组件接入了[可见性回调](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareaapproximatechange17)来方便开发者规避大部分Web空跑问题，该接口可以保证当Web挂载到ArkUI树上之后，跟随Web组件的可见性来控制Controller，当组件不可见时设置Web为冻结，可见时设置为活跃。但可见性接口对于离线组件不会返回结果，依赖三方开发者进行控制。

开发者可通过[WebviewController](../harmonyos-references/arkts-apis-webview-webviewcontroller.md)的onActive()和onInactive()来控制Web的活跃与冻结，冻结态的Web处于后台不会生产Buffer，可保证功耗收益。当开发者[使用离线Web组件](../harmonyos-guides/web-offline-mode.md#预渲染web页面)或主动调用了preloaditems()等方法时，建议在Web容器中添加onFirstMeaningfulPaint()回调，确保Web离线加载时，在完成第一次页面渲染之后进入冻结状态，既能保证进入预渲染Web时能够快速打开第一帧内容，也能保证其后台不产生冗余Buffer。

```
1. @Component
2. struct MyWebComponent {
3. private src: string = ""
4. private controller1: webview.WebviewController = new webview.WebviewController();
5. shouldDraw: boolean = true;
6. build() {
7. Web({ src: this.src, controller: this.controller1 })
8. .onPageBegin(() => {
9. console.log(this.src, "webpage is onActive")
10. this.controller1.onActive();
11. })

13. .onFirstMeaningfulPaint(() => {
14. if (!this.shouldDraw) {
15. return;
16. }
17. console.log(this.src, "webpage is onInactive")
18. this.controller1.onInactive()
19. this.shouldDraw = false
20. })
21. }
22. }
```

[buffer\_power\_example.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/PowerAnalysis/LowerPowerSample/entry/src/main/ets/pages/buffer_power_example.ets#L24-L45)

注意

Tab是一种较为特殊的加载结构，Tab默认的切换动效会将路径中的TabContent进行构建，此时位于路径TabContent中的Web组件，会由于隐式动效的特性无法响应可见性回调。对于使用了Tab+Web的开发者，推荐在接入onFirstMeaningfulPaint()首帧冻结的基础上，主动调用[preloadItems](../harmonyos-references/ts-container-tabs.md#preloaditems12)()方法对Tabs进行预加载。若不进行预加载，需确保onPageBegin()中，不将controller设置为活跃状态。

## 自绘制组件空跑优化案例

### 问题现象

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/MfPbPua9SKuioVyQCQBDIQ/zh-cn_image_0000002411759192.png?HW-CC-KV=V1&HW-CC-Date=20260429T061354Z&HW-CC-Expire=86400&HW-CC-Sign=314EEADA6CD3E5DDF78A664D4DFF6FB133A56A467F4BE921D6A41F22EEA43342 "点击放大")

上图展示了一个位于可滑动列表中的Video组件从屏幕外滑动至屏幕内的应用场景。其中“1”处的信息代表页面滑动的时机，“2”处的信息表明，视频的硬解码进程一直持续着产生。观察“3”“4”两处的差异可以发现，当Video组件位于屏幕外时，由于Buffer的持续生产造成了RSUni持续ReleaseBuffer，引发空跑问题。原则上，开发者所使用的自绘制图层需要对其ArkUI载体（如Video、XComponent等）添加充分的事件监听，确保其不再需要显示时，从Buffer生产的源头上停止。

### 优化思路

```
1. @Component
2. export struct MyVideoComponent {
3. @State videoSrc: Resource | string = $r('app.media.test_video');
4. private controller: VideoController = new VideoController();

7. build() {
8. Column() {
9. Video({
10. src: this.videoSrc,
11. controller: this.controller,

13. })
14. .width(300)
15. .height(200)
16. .onPrepared(() => {
17. this.controller.start();
18. })
19. // 确保视频组件完全可见时播放，完全不可见时停止
20. .onVisibleAreaChange([0.0], (isExpanding: boolean, currentRatio: number) => {
21. if (isExpanding && currentRatio >= 1.0) {
22. console.info('Component is completely visiable.');
23. if (this.controller) {
24. this.controller.start();
25. }
26. }
27. if (!isExpanding && currentRatio <= 0.0) {
28. console.info('Component is completely invisible.');
29. if (this.controller) {
30. this.controller.pause();
31. }
32. }
33. })
34. }
35. }
36. }
```

[buffer\_power\_example.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/PowerAnalysis/LowerPowerSample/entry/src/main/ets/pages/buffer_power_example.ets#L49-L84)

如上代码所示，开发者可利用可见性监听，判断当前呈现自绘制内容的ArkUI组件是否位于显示范围，通过控制Video.controller，控制视频在可见时播放，不可见时停止。

## 自绘制图层GPU重绘问题低功耗建议

### 问题现象

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/GUc1aGEaSzCXtqblR39uxQ/zh-cn_image_0000002411919060.png?HW-CC-KV=V1&HW-CC-Date=20260429T061354Z&HW-CC-Expire=86400&HW-CC-Sign=F9EDBC7EA9D80227AA344238BD1932F9002FC435BDEE2989C2CA59C131A80BF9 "点击放大")

对于使用了自绘制图层的应用页面而言，开发者还需要考虑该自绘制图层与当前页面中已有的图层如DisplayNode之间的交叠关系。理想情况下，自绘制图层完成生产后，如果无需与其他图层产生更多叠加计算时，无需交由RSUniRender线程重新处理，可直接交由RSHardware显示，这种显示方式可称之为“直通”。反之，如果开发者对承载自绘制组件的容器设定了一些图形绘制效果，例如模糊、透明、提亮等，那么RSUniRender需要将已经渲染好的Buffer，与作为背景的DisplayNode进行交叠计算。在这种情况下，自绘制图层不得不在RSUniRender中提前释放Buffer，将自绘制图层的内容由GPU进行重绘，并重新作为DisplayNode的一部分，再交由RSHardware进行显示，这种现象可称之为“GPU重绘”问题。

警告

GPU重绘问题对功耗的影响巨大，且多数情况下，开发者所设置的背景色、透明度等属性实际带来的显示效果在自绘制图层的覆盖下，效果并不明显。由于自绘制图层的生产本身也会消耗较多CPU和GPU的计算资源，持续性的GPU重绘将会占据更高的计算资源，引起明显发热。特别地，对于Web、XComponent等容器，不建议开发者主动设置背景色与透明度。

以下是一些常见的“GPU重绘”问题的根因。

* filter效果：自绘制图层本身或与之相交叠的组件具有filter效果，包括模糊、提亮、blendMode等效果，导致图层需要重新GPU计算
* 背景颜色：图层背景颜色带透明度，导致合成时不得不与其他图层做叠加计算
* 图层格式：当前系统的直通绘制，不支持非HEBC格式且旋转的buffer直接在线合成，对于视频播放、通话、会议场景，建议开发者[主动关闭CPU访问窗口缓冲区](../harmonyos-faqs/faqs-arkgraphics-2d-14.md)（适配HEBC格式）。HEBC格式的图层本身在绘制时对CPU更加友好，可以带来更好的功耗表现，减少发热风险。

### 问题定位

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/f9bi0au2RoSe8pnhsTw6hw/zh-cn_image_0000002445438237.png?HW-CC-KV=V1&HW-CC-Date=20260429T061354Z&HW-CC-Expire=86400&HW-CC-Sign=7A936D6C42DF22F3A86DAD9AD358B7C30FA6AC2C8D152CC2B89BA0A409E54C95 "点击放大")

开发者可以搜索“DrawImage”判断有无GPU重绘问题产生，如上图，给一个纯净的适配播放图层设置了一个透明度，进而引发GPU重绘问题发生，开发者可根据以下几个Trace点定位问题：

1. H:AcquireBuffer name: Surface queueId: 6605659702100：对应自绘制图层Buffer获取时机
2. H:RSBaseRenderEngine::DrawImage(GPU) targetColorGamut=4：“DrawImage(GPU)”表明存在GPU重绘现象，targetColorGamut=4表明该Surface在合成时，有四个buffer的内容，其中固定存在的三个Buffer分别是Display和两个固定圆角图层，当该值大于3时，表明有其他来源的Buffer进行了重绘进入了DisplayNode
3. H:ReleaseBuffer name: Surface queueId: 6605659702100 seq: 100801225：Buffer在RSUni中释放，此时Buffer的内容已经在DisplayNode中，Buffer重新流入BufferQueue
4. H:ReleaseBuffer name: DisplayNode queueId: 6605659701285 seq: 100798111：DisplayNode在RSHardware中释放

说明

在上图所示的案例中，观察发现render\_service里既没有ProcessCommandUni、也没有Animate的有效信息，表明此时DisplayNode并无实际刷新任务执行。但由于GPU重绘问题的存在，DisplayNode也会全程参与Buffer轮转过程，并产生图层计算功耗。

### 优化思路

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/cge4XyCOTG-Evn9tYB1Krw/zh-cn_image_0000002445518333.png?HW-CC-KV=V1&HW-CC-Date=20260429T061354Z&HW-CC-Expire=86400&HW-CC-Sign=F69D6946A2E902A523926371B6E0770C1DD39C78656428B12D5119FA2F37D513 "点击放大")

如上图，开发者可以使用HiSmartPerf的RS树工具查看可疑节点，在OtherModifier位置可以查看到来自pid进程58867，为该节点添加了一个0.4的Alpha透明度，结合该信息可进一步定位到对应的代码片段，如下图代码，注释掉透明度效果后问题不复现。

```
1. @Component
2. export struct MyVideoComponent_opacity {
3. @State videoSrc: Resource | string = $r('app.media.test_video');
4. private controller: VideoController = new VideoController();

7. build() {
8. Column() {
9. Video({
10. src: this.videoSrc,
11. controller: this.controller,

13. })
14. .width(300)
15. .height(200)
16. // .opacity(0.4) 注释掉此段代码，可规避GPU重绘
17. .onPrepared(() => {
18. this.controller.start();
19. })
20. }
21. }
22. }
```

[buffer\_power\_example.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/PowerAnalysis/LowerPowerSample/entry/src/main/ets/pages/buffer_power_example.ets#L89-L110)

修改好的Trace表现如下图所示，在直通情况下，自绘制图层在图中“1”处获取Buffer，“2”处释放Buffer，无需交由RSUniRender进行重绘计算，也没有DisplayNode的刷新显示，达到预期的低功耗效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/y1tdOLxhRTOL6l1DgnPImw/zh-cn_image_0000002411759196.png?HW-CC-KV=V1&HW-CC-Date=20260429T061354Z&HW-CC-Expire=86400&HW-CC-Sign=B2B99608593B62F224C4D6E7F91FEB1653BF61B384A5715EE9555BD15019AD91 "点击放大")

说明

以下效果会导致自绘制图层GPU重绘，非必要显示效果，不建议开发者接入：

* 使用[opacity](../harmonyos-references/ts-universal-attributes-opacity.md#opacity18)属性，给自绘制组件设置透明度
* 使用[foregroundEffect](../harmonyos-references/ts-universal-attributes-foreground-effect.md#foregroundeffect)实现前景模糊，[blur](../harmonyos-references/ts-universal-attributes-image-effect.md#blur)实现背景模糊
* 使用[grayscale](../harmonyos-references/ts-universal-attributes-image-effect.md#grayscale)，实现灰阶效果
* 使用[lightUpEffect](../harmonyos-references/ts-universal-attributes-image-effect.md#lightupeffect12)，强行对图层进行压暗提亮
* 特别地，对于Web、XComponent组件，建议设置背景色为黑色不透明，或不主动设置[backgroundColor](../harmonyos-references/ts-universal-attributes-background.md#backgroundcolor)属性
