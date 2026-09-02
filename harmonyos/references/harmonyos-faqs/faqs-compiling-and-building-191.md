---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-191
title: 新建工程/模块无法加载ets目录下的资源
breadcrumb: FAQ > DevEco Studio > 编译构建 > 新建工程/模块无法加载ets目录下的资源
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fb5b7e21bd8f0f35c68cfe9f5ab891def1757f6d3a609f9d0c07e30b7dc1e258
---

**问题现象**

新建工程，通过ImageBitmap或其他组件使用src/main/ets目录中的本地图片无法加载。

**可能原因**

若使用DevEco Studio 6.0.0 Beta2及之后的版本创建的新工程，会默认不打包模块src/main目录中的图片资源，具体参考**[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)**

**解决措施**

1. 将ets目录中的资源文件放置到resources目录中,通过$r的方式引用，参考：

   ```typescript
   // xxx.ets
   @Entry
   @Component
   struct VideoPlayer {
     private controller: VideoController = new VideoController()
     private previewUris: Resource = $r('app.media.preview')
     private innerResource: Resource = $rawfile('videoTest.mp4')

     build() {
       Column() {
         Video({
           src: this.innerResource,
           previewUri: this.previewUris,
           controller: this.controller
         })
           .onUpdate((event) => { // Triggered when the playback progress changes.
             console.info("Video update.");
           })
           .onPrepared((event) => { // Triggered when video preparation is complete.
             console.info("Video prepared.");
           })
           .onError(() => { // Triggered when the video playback fails.
             console.error("Video error.");
           })
           .onStop(() => { // Triggered when the video playback stops.
             console.info("Video stopped.");
           })
       }
     }
   }
   ```
2. 若使用的组件不支持直接使用$r的写法,可以通过resourceManager资源接口获取和使用resources资源目录中的资源，参考：

   ```typescript
   // xxx.ets
   @Entry
   @Component
   struct ImageExample {
     private settings: RenderingContextSettings = new RenderingContextSettings(true);
     private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
     // Replace "common/images/example.jpg" with the image resource file you use.
     // private img: ImageBitmap = new ImageBitmap("common/images/example.jpg"); // This relative path writing will make it impossible to record pictures in the new template
        private img: ImageBitmap = new ImageBitmap(this.getUIContext().getHostContext()?.resourceManager
       .getDrawableDescriptorByName("example")
       .getPixelMap()); // You can refer to the interface for using resourceManager

     build() {
       Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
         Canvas(this.context)
           .width('100%')
           .height('100%')
           .backgroundColor('#ffff00')
           .onReady(() => {
             this.context.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 200)
             this.img.close()
           })
       }
       .width('100%')
       .height('100%')
     }
   }
   ```
