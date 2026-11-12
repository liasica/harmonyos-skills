---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-troubleshooting-0010
title: ArkUI-Image组件图片显示异常问题定位
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 故障排查 > ArkUI-Image组件图片显示异常问题定位
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:9dd83f98bb7040a82076b7a6500bf1a663f2be1ef41df91ee604982cbdf0c498
---

## 使用Image组件加载图片，发现图片变为了正方形

### 问题现象

使用Image加载图片，发现图片被压缩，且打印图片大小时发现，图片大小并非图片原本尺寸，而是高宽均为512像素尺寸。

错误现象展示如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/s2qWEuISRQeQ5Zd4TbMyDQ/zh-cn_image_0000002801202855.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=C53CAC47E95E41E46179CC415072CF18E011807D50C8E93BD69665D77414D447 "点击放大")

正常现象展示如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/NRTAE2O2Szy74f82iROyGg/zh-cn_image_0000002801202857.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=616959FEF43038B12A46F928874BD3B2CBEA731DBF7F1BE4C1FB07807F07FB5A "点击放大")

### 定位过程

1. 同一张图片，新建项目展示查看确认正常。
2. 使用代码确认其尺寸，发现其尺寸被压缩到512像素尺寸。
3. 全局搜索图片资源，发现该图片资源也被用于在module.json5中的icon属性引用。
4. 修改module.json5的icon属性对该图片引用后，该图片应用内展示恢复正常。
5. 重新设置icon属性复现之后，发现是编译打包后的HAP包内，该图片大小被压缩到512像素大小的正方形。

### 分析结论

应该是因为该图片被设置为应用桌面图标后，IDE编译打包时将其压缩到512像素尺寸的正方形，而后续应用内使用也只能拿到压缩后的图片。

### 修改建议

修改module.json5的icon属性，不要使用可能会在应用内使用的图片作为桌面应用图标。

## 怎么解决Image组件加载图片被旋转90度的问题

### 问题现象

使用Image组件加载图片时，图片自动被旋转了90度，如何使图片显示方向正确。问题代码如下：

```ts
@Entry
@Component
struct ImageRotationProblem {
  build() {
    Column() {
      // 运行时请按需替换图片资源
      Image($r('app.media.startIcon'));
    };
  }
}
```

左图为正常显示效果，右图为Image加载显示效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/-hCvHcG4Sh2mq8q6laZZFg/zh-cn_image_0000002771763180.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=787BC93BB0C513064E3D0DE6783174584E70CC606558DDB2497F6F125E92A5D0 "点击放大")

### 定位过程

1. 使用Image组件加载其他图片，检查是否为组件问题。由于“新闻”图片正常显示，确认非组件问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/-gaMctBwQ7OQSk_N7SgICw/zh-cn_image_0000002801202983.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC1DE4933AEFBD04A1784EA74D81616D9888517F43E6AC71D9FDF6967D98D462 "点击放大")
2. 检查原图片Exif信息，定位其orientation属性。通过在线网站查看图片信息得知该图片的拍摄方向为逆时针旋转90度。由此，定位到图片被旋转的原因。

   | 属性 | 说明 | 值 |
   | --- | --- | --- |
   | ImageWidth | 像素宽度 | 4032 |
   | XResolution | X分辨率 | 72 |
   | YResolution | Y分辨率 | 72 |
   | Resolution | 分辨率单位 | 英寸 |
   | Orientation | 拍摄方向 | 6（逆时针旋转90°） |

### 分析结论

图片旋转是因为图像的拍摄方向属性固定为旋转90度导致的，需要旋转归位或者对图像进行其他处理。

### 修改建议

**方案一：通过组件旋转属性，使图片显示方向正常：**

直接给Image组件加上对应的旋转属性，使图片正常显示。因为图片的方向是逆时针90度，将Image组件顺时针旋转90度后，图片会正常显示。通过以下属性旋转：

```ts
@Entry
@Component
struct ImageRotationOne {
  build() {
    Column() {
      // 运行时请按需替换图片资源
      Image($r('app.media.startIcon'))
        .rotate({ angle: 90 });
    };
  }
}
```

**说明** 

这种方案只有在确定图片的方向信息时才能使用，如果是从网络加载的、不能确定方向的图片列表，该方案则不适用。

**方案二：通过orientation属性，设置图片的显示方向：**

利用orientation属性，[设置图像内容的显示方向](../harmonyos-references/ts-basic-components-image.md#示例21设置图像内容的显示方向)。如果需要显示携带旋转角度信息或翻转信息的图片建议使用ImageRotateOrientation.AUTO进行设置。示例代码如下：

```ts
// 运行时请按需替换图片资源
@Entry
@Component
struct ImageRotationTwo {
  build() {
    Column() {
      // 运行时请按需替换图片资源
      Image($r('app.media.startIcon'))
        .orientation(ImageRotateOrientation.AUTO);
    };
  }
}
```

**说明** 

这种方案不支持gif和svg类型的图片。

**方案三：将图片转成ImageSource对象后读取旋转信息：**

**思路**：读取每张图片的方向orientation信息，根据其方向，设置图片的显示方向。

1. 使用Image Kit的createImageSource接口，将图片转换成image.ImageSource对象。
2. 使用ImageSource的getImageProperty接口获取图片的image.PropertyKey.ORIENTATION旋转信息。
3. 根据图片的EXIF方向信息设置orientation属性值进行旋转，使图片正常显示。

详细代码可以参考：[获取图片的Exif信息并设置图像内容的显示方向](../harmonyos-references/ts-basic-components-image.md#示例22获取图片的exif信息并设置图像内容的显示方向)。

## 长图渐变色效果未正常显示

### 问题现象

页面展示图片时通常先是展示缩略图，点击后才会显示原图。长图以缩略图样式展示时通常添加渐变色以提高用户体验。

图一：无渐变色的缩略图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/nEaXovJaSHiyXcAGb5qm0g/zh-cn_image_0000002771763344.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBD2420AC4C8BC1B513211ABEC06CA67B45A80F4021EA0FAD07F21579DA421A5 "点击放大")

图二：有渐变色的缩略图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/HCRRSDj9RN6vp59R94PwcQ/zh-cn_image_0000002801083191.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=51CDB713D563523A3B71CD33AC469D9F8A02751418257D76AC08240F5EAC27B2 "点击放大")

### 定位过程

1. 通过DevEco Testing查看问题组件，发现是Image组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/9TvNo3BlQTGODT4Nvp_GNQ/zh-cn_image_0000002771923506.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C2A5FEC1AD39A11F570A859FAFC2304ECE82AD5000D820899F36A262C88268B "点击放大")
2. 排查该Image组件的同层组件的设置，发现没有使用linearGradient设置颜色渐变的同层组件。

   ```ts
   @Entry
   @Component
   struct ImgExample {

     build() {
       Stack() {
         Image($r('app.media.long')) // $r('app.media.long')需要替换为开发者需要的图片资源文件
           .width(200)
           .height(300)
           .objectFit(ImageFit.Auto)
           // 没有使用linearGradient设置颜色渐变的同层组件
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

### 分析结论

Image组件没有使用linearGradient设置颜色渐变的同层组件，导致长图没有渐变色效果。

### 修改建议

添加使用linearGradient设置颜色渐变的同层组件。

```ts
@Entry
@Component
struct ImgExample {
  build() {
    Stack() {
      Stack() {
        Image($r('app.media.long')) // $r('app.media.long')需要替换为开发者需要的图片资源文件
          .width('100%')
          .height('100%')
          .objectFit(ImageFit.Auto);

        // 使用linearGradient设置颜色渐变的同层组件
        Row()
          .width('100%')
          .height('40')
          .linearGradient({
            direction: GradientDirection.Bottom,
            colors: [['#00000000', 0.0], ['#ff000000', 1.0]]
          });
      }
      .width(200)
      .height(300)
      .alignContent(Alignment.Bottom);
    }
    .width('100%')
    .height('100%');
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/4d3uQlWDTnqapl5zB2OldA/zh-cn_image_0000002801203363.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=7F28A3418ED4BF35CAB4C51422A2346A8BEB6A0AE0D4CE9D3B02DBA352E5E44B "点击放大")

## 页面上图片展示不完整

### 问题现象

加载应用内的图片时，图片显示不完整。

图一：完整显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/O8iHMUJaQsSOw3xyN07FBA/zh-cn_image_0000002771763596.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=D651CD9E980D426DDA638C71FC9DBB3909512C5020BC350EC5D5A83C4526FFD2 "点击放大")

图二：显示不完整。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/jaOn5IYfTH65lRWFbyjjTw/zh-cn_image_0000002801203375.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=31E725205CC1183E93D1B78044CDE4C12071A3BA8F0EC5D0C2D868845DAA57F9 "点击放大")

### 定位过程

1. 使用DevEco Testing查看问题组件，该组件为Image组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/dqM29wRmSG6Q_3AydqArNw/zh-cn_image_0000002771763600.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=B3A00A12D4CFCFB0AD00C2F7E59F62A28D62ADF813E409883DD2E0C0533A986F "点击放大")
2. 查看Image组件的objectFit属性是否正确，图片的缩放模式选用不当可能造成图片显示不完整，如果图片缩放模式设置为cover，图片会保持宽高比，并填满容器，超出部分会被裁剪。

   ```ts
   @Entry
   @Component
   struct ImgEmpty {

     build() {
       Stack() {
         Image($r('app.media.product')) // $r('app.media.product')需要替换为开发者需要的图片资源文件
           .width(300)
           .height(200)
           .objectFit(ImageFit.Cover) // 图片保持宽高比并填满容器，超出部分会被裁剪
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

### 分析结论

图片使用了不合适的缩放模式，造成超出容器的部分被裁剪，导致图片显示不完整。

### 修改建议

objectFit属性设置为Contain，该缩放模式会保持宽高比，完整显示图片。

```ts
@Entry
@Component
struct ImgTruncation {
  build() {
    Stack() {
      Image($r('app.media.product')) // $r('app.media.product')需要替换为开发者需要的图片资源文件
        .width(300)
        .height(200)
        .objectFit(ImageFit.Contain) // 保持宽高比，完整显示图片
    }
    .width('100%')
    .height('100%');
  }
}
```

## 页面中的图片资源无法正常显示

### 问题现象

页面图片显示空白。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/suIfxMwgRBqBCFCgAicAPQ/zh-cn_image_0000002801083537.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=45AE0FBDAC626F1DADB41FE38E87FA98EE341CBE1EE1931F9CBFED8704E56CD2 "点击放大")

### 定位过程

1. 使用DevEco Testing查看问题组件，问题所在位置缺少Image组件，而正常显示图片组件的相同位置使用了Image组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/e57nHhNyQamzKS4aVXFfKg/zh-cn_image_0000002771923676.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1CF03DACC391267A1FFDD9A7753793262A54D0D8168CF6F829CF10D4BD6D057 "点击放大")
2. 排查Image组件的设置，发现添加了判断图片资源是否存在的逻辑。

   ```ts
   @Entry
   @Component
   struct ImgEmpty {
     imgSrcs: ResourceStr[] = ['', $r('app.media.myposter2')];

     build() {
       Stack() {
         List() {
           ForEach(this.imgSrcs, (img: ResourceStr, index: number) => {
             ListItem() {
               Row() {
                 Text('图片' + (index + 1))
                   .fontSize(20)
                   .height('100%')
                   .width(100)
                   .textAlign(TextAlign.Center)
                   .borderRadius(10);

                 // 图片资源为空时不显示图片组件
                 if (img !== '') {
                   Image(img)
                     .width(150)
                     .objectFit(ImageFit.Contain);
                 }
               }
               .width('100%')
               .height(120)
               .justifyContent(FlexAlign.Start)
               .borderRadius(10)
               .backgroundColor('#f1f3f5');
             }
             .margin({ top: 5, bottom: 5 });
           }, (item: string) => item);
         }
         .nestedScroll({
           scrollForward: NestedScrollMode.PARENT_FIRST,
           scrollBackward: NestedScrollMode.SELF_FIRST
         })
         .scrollBar(BarState.Off)
         .width('80%');
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

### 分析结论

该图片资源不存在，导致无法显示图片。

### 修改建议

无图片资源时通过alt属性使用占位图片替代。

```ts
@Entry
@Component
struct ImgEmpty {
  imgSrcs: ResourceStr[] = ['', $r('app.media.startIcon')]; // $r('app.media.startIcon')需要替换为开发者需要的图片资源文件

  build() {
    Stack() {
      List() {
        ForEach(this.imgSrcs, (img: ResourceStr, index: number) => {
          ListItem() {
            Row() {
              Text('图片' + (index + 1))
                .fontSize(20)
                .height('100%')
                .width(100)
                .textAlign(TextAlign.Center)
                .borderRadius(10);

              Image(img)
                .width(100)
                // $r('app.media.empty')需要替换为开发者需要的图片资源文件
                .alt($r('app.media.empty')) // 图片资源为空时显示占位图片
                .objectFit(ImageFit.Contain);
            }
            .width('100%')
            .height(120)
            .justifyContent(FlexAlign.Start)
            .borderRadius(10)
            .backgroundColor('#f1f3f5');
          }
          .margin({ top: 5, bottom: 5 });
        }, (item: string) => item);
      }
      .nestedScroll({
        scrollForward: NestedScrollMode.PARENT_FIRST,
        scrollBackward: NestedScrollMode.SELF_FIRST
      })
      .scrollBar(BarState.Off)
      .width('80%');
    }
    .width('100%')
    .height('100%');
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/cZnlH-ydQQKDN4QiG62mNA/zh-cn_image_0000002771763862.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE3B39E3204EC8EE6EEE88ECAB2190DC59D988B59BC61BB3ABD54EEC70A5CD20 "点击放大")
