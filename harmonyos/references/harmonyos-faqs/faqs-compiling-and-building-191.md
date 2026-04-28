---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-191
title: 新建工程/模块无法加载ets目录下的资源
breadcrumb: FAQ > DevEco Studio > 编译构建 > 新建工程/模块无法加载ets目录下的资源
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:49+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:bfae57e925e2afaeee0aaf03f101983d02018cdae367b79c87834b4a30247049
---

**问题现象**

新建工程，通过ImageBitmap或其他组件使用src/main/ets目录中的本地图片无法加载。

**可能原因**

若使用DevEco Studio 6.0.0 Beta2及之后的版本创建的新工程，会默认不打包模块src/main目录中的图片资源，具体参考**[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)**

**解决措施**

1. 将ets目录中的资源文件放置到resources目录中,通过$r的方式引用，参考:

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct VideoPlayer {
5. private controller: VideoController = new VideoController()
6. private previewUris: Resource = $r('app.media.preview')
7. private innerResource: Resource = $rawfile('videoTest.mp4')

9. build() {
10. Column() {
11. Video({
12. src: this.innerResource,
13. previewUri: this.previewUris,
14. controller: this.controller
15. })
16. .onUpdate((event) => { // Triggered when the playback progress changes.
17. console.info("Video update.");
18. })
19. .onPrepared((event) => { // Triggered when video preparation is complete.
20. console.info("Video prepared.");
21. })
22. .onError(() => { // Triggered when the video playback fails.
23. console.error("Video error.");
24. })
25. .onStop(() => { // Triggered when the video playback stops.
26. console.info("Video stopped.");
27. })
28. }
29. }
30. }
```

[GetResources.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetResources.ets#L21-L50)

2. 若使用的组件不支持直接使用$r的写法,可以通过resourceManager资源接口获取和使用resources资源目录中的资源，参考:

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ImageExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // Replace "common/images/example.jpg" with the image resource file you use.
8. // private img: ImageBitmap = new ImageBitmap("common/images/example.jpg"); // This relative path writing will make it impossible to record pictures in the new template
9. private img: ImageBitmap = new ImageBitmap(this.getUIContext().getHostContext()?.resourceManager
10. .getDrawableDescriptorByName("example")
11. .getPixelMap()); // You can refer to the interface for using resourceManager

13. build() {
14. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
15. Canvas(this.context)
16. .width('100%')
17. .height('100%')
18. .backgroundColor('#ffff00')
19. .onReady(() => {
20. this.context.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 200)
21. this.img.close()
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

[GetResourceManager.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetResourceManager.ets#L21-L47)
