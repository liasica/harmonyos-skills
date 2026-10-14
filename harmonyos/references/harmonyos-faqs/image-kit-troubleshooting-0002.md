---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/image-kit-troubleshooting-0002
title: 系统相册大图加载与解码报错问题定位
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 故障排查 > 系统相册大图加载与解码报错问题定位
category: harmonyos-faqs
scraped_at: 2026-10-15T07:15:35+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:6b746343253e9805435378ac48906c79632863c01fd16d6ffb8a26e44cb039e7
---

## 问题现象

应用侧保存分辨率40320x25200大图到系统相册无法正常加载，且无法正常使用图片解码，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/ND1MRglyQB2xWZfMC0_Q2Q/zh-cn_image_0000002789316857.png "点击放大")

## 定位过程

测试使用代码如下：

```ts
async createPixel() {
  const resourceManager = this.getUIContext().getHostContext()?.resourceManager;
  const imageData = await resourceManager!.getMediaContent($r('app.media.startIcon').id);
  let arrayBuffer = imageData.buffer;
  const imageSource = image.createImageSource(arrayBuffer);
  console.info('createImageSource success')
  let imageInfo = imageSource.getImageInfoSync(0);
  let width = imageInfo.size.width;
  let height = imageInfo.size.height;
  const opts: image.DecodingOptions = {
    editable: true,
    desiredSize:{width:width,height:height},
    desiredPixelFormat: image.PixelMapFormat.BGRA_8888
  };
  let pixel = await imageSource.createPixelMap(opts);
  console.info('createPixelMap success')
  const imagePackerApi: image.ImagePacker = image.createImagePacker()
  let packOpts: image.PackingOption = {
    format:'image/jpeg',
    quality:100
  }
  try{
    imagePackerApi.packToData(pixel,packOpts).then(()=>{
      console.info('imagePacking success')
    })
  }catch (err){
    console.error('imagePacking failed',err)
  }
  console.info('imagePacking complete')
}
```

如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/1ah8cf09Sayvmj3a-0YKkw/zh-cn_image_0000002759918096.png "点击放大")

可以看到使用超大图解码后，Heap存在明显上涨且长时间无回落。查询日志相关信息，通过日志发现尽管图片解码实例创建成功，但后续创建PixelMap以后的程序并未顺利执行，日志打印如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/krbAgKooRR6Lf5ugxsMLbQ/zh-cn_image_0000002759918110.png "点击放大")

## 分析结论

当图片分辨率过大（像素数超过4亿）时，此时解码占用内存高，触发严重的整机性能问题。图片分辨率降低后可以在图库中正常显示且解码正常。

## 修改建议

HarmonyOS的图片解码对图片分辨率及文件占用的空间有限制，单张图片的文件占用空间大小不能超过2G，单个应用运行内存占用达到4G会触发整机性能问题。建议在图片解码前[将图片压缩到指定大小](faqs-image-16.md)，既可展示图片，又可以保证系统的稳定运行。正常日志打印效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/FAGXBUGVQ9yUx9jU19H0eg/zh-cn_image_0000002789316945.png "点击放大")

针对大图加载、图片编辑及长图预览场景，参考[图片区域解码与下采样指导](../harmonyos-guides/image-region-and-downsampling.md)和[图片解码内存优化](../harmonyos-guides/image-allocator-type.md)。
