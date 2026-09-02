---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-16
title: HarmonyOS中如何实现图片取色
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > HarmonyOS中如何实现图片取色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:300e38f66956d32b4786b49a7f9017f632e68fe3aae7e7e9c2b418679013b5c4
---

## 问题现象

如何获取图片的主要颜色，或是图片某个位置的像素值？

实现过程中的常见问题：

* 为什么提取出来的颜色不符合预期？
* 如何进行颜色格式转换？

## 背景知识

图片取色根据场景需求可以使用不同的方法实现：

* ColorPicker：使用[ColorPicker](../harmonyos-references/js-apis-effectkit.md#colorpicker)可以获取图片的主要颜色、占比最多的颜色、平均颜色等色值。其核心接口分类与适用场景如下：
* readPixels：使用[readPixels](../harmonyos-references/arkts-apis-image-pixelmap.md#readpixels7)固定按照BGRA\_8888格式，读取PixelMap指定区域内的图像像素数据，并写入PositionArea.pixels缓冲区中，该区域由PositionArea.region指定。使用Promise异步回调。
* ColorPicker取色类与readPixels方法的对比：

  | 取色方式 | 方法返回值 | 适用场景 |
  | --- | --- | --- |
  | ColorPicker | Promise对象（包含颜色信息），或Color实例，包含红、绿、蓝、透明度四个值 | 对整张图进行分析，通过取色类中的不同接口能获得不同颜色值。 |
  | readPixels | BGRA\_8888格式 | 获得给定坐标位置的颜色，如：取色笔 |

## 解决方案

下文将用下述示例图片举例阐述各个场景下的颜色提取：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/nWbIb1GdSdWgdkdlcFpAXw/zh-cn_image_0000002628393318.png "点击放大")

1. **图像整体取色**。
   * **方案一：主色提取**。
     + **适用场景：** getMainColor接口用于精确计算并预览图片；getMainColorSync接口用于主题色生成，详细示例请见：[基于ColorPicker实现自适应背景色功能](https://gitcode.com/harmonyos_samples/effect-kit#基于colorpicker实现自适应背景色功能)。图片主色不能与图片占比最大色混为一谈，主色接口会将图片涉及到的颜色混合后输出，与人眼分析出的所谓“占比最大主色”不同。
     + **核心代码：**

       ```ts
       // 同步主色获取
       const color = colorPicker.getMainColorSync();
       console.info('get main color =', '{red:', color.red, 'green:', color.green, 'blue:', color.blue, 'alpha:',
         color.alpha, '}');
       ```
     + **输出结果：**

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/D6A_vnegSiC-RRUsgP2E-w/zh-cn_image_0000002628553214.png "点击放大")

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/wcpwyUvjTxa5czYl7VPLTQ/zh-cn_image_0000002658912533.png "点击放大")

       通过与下述中占比最大颜色值进行比较，会发现与占比最大的色值有一定偏差。这是因为读取图片主色方法，是通过综合颜色分布、饱和度、亮度等权重计算得出。例如，一张包含蓝、白、黄混合的图片，主色可能输出浅绿色（混合结果）而非具体颜色值。图片主色的判断通常需要更复杂的算法，可能涉及到颜色空间的转换、色彩饱和度的计算等，以确保选择的主色能够准确反映图像的整体色彩特征，适合需要代表性颜色的场景。
     + **与相似接口区别：**

       getMainColor与getMainColorSync都用于提取图像主色，其核心区别在于**执行方式**和**适用场景**。

       |  | getMainColor | getMainColorSync |
       | --- | --- | --- |
       | 执行方式 | 异步（基于回调） | 同步 |
       | 返回值 | 通过回调函数返回Color对象 | 直接返回Color对象 |
       | 适用场景 | 适用于对主线程流畅性要求高的场景：①用于精确计算、复杂图像处理（如：医疗影像中的主色识别）；②大文件主色提取（如：4K壁纸的主色提取）。 | 适用于需要立即获取结果且对性能影响可控的场景：①动画切换时的实时背景色更新；②需要快速响应用户交互的主色提取（如：点击按钮后立即变色）。 |
   * **方案二：高频色统计**。
     + **适用场景：** getLargestProportionColor接口用于统计色彩区域占比而非单纯像素计数，通过区域占比识别大块连续颜色，**视觉占比最大的代表性颜色**。

       getTopProportionColors接口用于获取图像中占比前N的颜色值，其核心原理是通过**颜色频率统计与排序**算法实现。接口常用于商品主图品牌色提取（需结合面积占比过滤）。
     + **核心代码：**

       ```ts
       // 获取占比最大的颜色
       const largestColor = colorPicker.getLargestProportionColor();
       console.info('get largest proportion color =' + '{red:', largestColor.red, 'green:', largestColor.green,
         'blue:', largestColor.blue, 'alpha:', largestColor.alpha, '}');
       // 获取占比靠前的颜色值
       const topColors = colorPicker.getTopProportionColors(2);
       for (let index = 0; index < topColors.length; index++) {
         if (topColors[index]) {
           console.info('get top proportion colors: index ' + index + ', color ' + '{red:', topColors[index]?.red,
             'green:', topColors[index]?.green, 'blue:', topColors[index]?.blue, 'alpha:',
             topColors[index]?.alpha, '}');
         }
       }
       ```
     + **输出结果：**

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/7yGewf66QtaJcs1pGzyL3g/zh-cn_image_0000002658792593.png "点击放大")

       getLargestProportionColor接口输出颜色为黄色，与图片的背景色完全一致。对于RGB颜色模型，每个像素由红、绿、蓝三个通道的值组成，接口会记录所有像素中相同颜色组合的出现频率，最终输出频率最高的颜色组合。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/t-qPoFkORJmjPVEKgNYuBA/zh-cn_image_0000002628393338.png "点击放大")

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/-jypK_9cQYiytsnyzc-F9w/zh-cn_image_0000002628553222.png "点击放大")

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/VqAn-NV9ReW62MOscOHzJw/zh-cn_image_0000002658912541.png "点击放大")

       getTopProportionColors接口输出前两位的高频颜色。该接口原理与getLargestProportionColor类似。
     + **与相似接口区别：**

       在HarmonyOS中，getLargestProportionColor与getMainColor均用于提取图像颜色特征，但两者的算法逻辑和应用场景存在显著差异。

       |  | getTopProportionColors | getLargestProportionColor | getMainColorSync |
       | --- | --- | --- | --- |
       | 算法逻辑 | 统计占比前N的颜色，支持自定义数量 | 统计像素颜色频率，直接选取出现次数最多的颜色值（即**占比最高的单一颜色**）。 | **综合计算颜色权重**，可能结合亮度、饱和度或位置分布等因素，生成代表整体色调的主色。 |
       | 结果特性 | 返回占比前N的Color数组 | 返回单个Color对象 | 返回单个Color对象 |
       | 适用场景 | ①图像分类：通过颜色分布特征识别图片类型（如自然风景、人工制品）；②动态适配：根据主色生成配套UI元素（如按钮、图标颜色匹配）。 | 需要快速获取图像中**最突出的单一颜色**（如提取LOGO主色、检测明显色块）。 | 需要反映图像**整体色调**（如主题色适配）。 |
   * **方案三：平均色统计**。
     + **适用场景：** getAverageColor接口**适用于颜色分布均匀的图像**，但可能因互补色混合导致结果发灰，一般适用于渐变背景中间色的生成。
     + **核心代码：**

       ```ts
       // 获取平均色
       const averageColor = colorPicker.getAverageColor();
       console.info('get average color =' + '{red:', averageColor.red, 'green:', averageColor.green, 'blue:',
         averageColor.blue, 'alpha:', averageColor.alpha, '}');
       ```
     + **输出结果：**

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/UcTFm2cqT-K4FsDk1QbTNg/zh-cn_image_0000002658792603.png "点击放大")

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/xIdy7YfWTtOIBISWasJzxA/zh-cn_image_0000002628393348.png "点击放大")

       输出颜色为蓝色，是因为获取平均色接口会遍历图片中所有像素的RGBA值，分别累加红（R）、绿（G）、蓝（B）通道的总和，并统计有效像素数量（通常忽略透明度低于阈值的像素，如Alpha通道<10），再进行平均值的计算，图像中蓝色占大部分，且部分色块为深红、深蓝、白色等，因此最终平均色为蓝色。
     + **与相似接口区别：**

       getAverageColor侧重数学平均，而getMainColorSync和getLargestProportionColor分别侧重视觉感知和频率统计。
   * **方案四：图像饱和度分析**。
     + **适用场景：** getHighestSaturationColor接口用于提取图像中饱和度最高的颜色，其核心原理基于HSV/HSL颜色模型的饱和度（Saturation）通道分析。
     + **核心代码：**

       ```ts
       // 获取饱和度最高的颜色
       const highestSatColor = colorPicker.getHighestSaturationColor();
       console.info('get highest SatColor color =', '{red:', highestSatColor.red, 'green:', highestSatColor.green,
         'blue:', highestSatColor.blue, 'alpha:', highestSatColor.alpha, '}');
       ```
     + **与相似接口区别：**

       该接口与上述接口不同点在于，使用该接口时，会将图像中每个像素的RGB值转换为HSV（色相Hue、饱和度Saturation、明度Value）颜色空间进行分析。HSV模型中，**S通道（0-1或0-100%）直接表示颜色的鲜艳程度**，数值越高饱和度越强。遍历像素点，最后返回S值最高的颜色。
     + **输出结果：**

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/upribDvmTXeJ6XDGcU4lVQ/zh-cn_image_0000002628553230.png "点击放大")

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/VIoQq3IWRkiN8dBwPzPdBg/zh-cn_image_0000002658912549.png "点击放大")

       接口检测出饱和度最高的颜色为船身的深蓝色。
     + **与相似接口区别：**

       |  | getHighestSaturationColor | getLargestProportionColor | getMainColorSync |
       | --- | --- | --- | --- |
       | 算法逻辑 | 基于HSV模型筛选S值最高的颜色 | 统计像素频率最高颜色 | 综合亮度、位置等权重计算主色 |
       | 结果特性 | 鲜艳度最高的单一颜色（如亮红色） | 占比最大的颜色（可能低饱和） | 视觉显著色（可能非最高饱和） |
       | 适用场景 | ①识别图像中的强调色（如广告中的促销标识）；②为设计工具提供高饱和度配色方案（如海报设计、品牌色提取）。 | 提取LOGO主色、检测明显色块等。 | 主题色适配等。 |
   * **方案五：黑白灰属性分析**。
     + **适用场景：** isBlackOrWhiteOrGrayColor接口用于判断颜色是否为黑白灰（无彩色系），使用colorPicker获取颜色值时，需要转换为十六进制数据才能用于黑白灰判断。
     + **核心代码：**

       ```ts
       // 黑白灰检测
       const isNeutral = colorPicker.isBlackOrWhiteOrGrayColor(0xFFFF00FF);
       console.info('isBlackOrWhiteOrGrayColor', isNeutral);
       ```
     + **与相似接口区别：**

       |  | isBlackOrWhiteOrGrayColor | getHighestSaturationColor | getAverageColor |
       | --- | --- | --- | --- |
       | 算法逻辑 | 基于RGB通道差异或HSV饱和度判断 | 筛选饱和度最高的颜色 | 计算颜色均值 |
       | 结果特性 | 返回布尔值，仅标识是否为无彩色 | 返回具体颜色值（高饱和彩色） | 返回混合色（可能包含灰调） |
       | 适用场景 | ①深色模式适配：检测系统或UI元素颜色是否为黑白灰，避免与深色背景冲突；②图像分类：识别黑白照片或灰度界面截图；③无障碍设计：确保文字与背景颜色对比度符合无障碍标准 | 识别图像中的强调色等。 | 渐变背景色适配等。 |
2. **像素级操作取色**。
   * **适用场景：** readPixels适合后台分析、批量处理、自动化操作，多用于系统自动分析颜色类。提供直观操作，适合设计类应用。该接口可以**快速获取特定区域的颜色值**，进行如二维码扫描、颜色采样、取色笔等图像分析相关操作。
   * **坐标系定义：**
     + 原点位置：左上角基准，坐标原点(0,0)位于图像左上角。
     + 轴向规则：
       - X轴：水平向右递增（宽度方向）；
       - Y轴：垂直向下递增（高度方向）。
   * **核心代码：**

     ```ts
     const area: image.PositionArea = {
       pixels: new ArrayBuffer(4),
       offset: 0,
       stride: 4,
       region: { size: { height: 1, width: 1 }, x: 0, y: 0 },
     };
     if (pixelMap !== undefined) {
       pixelMap.readPixels(area).then(() => {
         console.info('Succeeded in reading the image data in the area.'); // 符合条件则进入。
         console.info('BGRA data is ', new Uint8Array(area.pixels));
       }).catch((error: BusinessError) => {
         console.error(`Failed to read the image data in the area. code is ${error.code}, message is ${error.message}`); // 不符合条件则进入。
       });
     }
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/VMaFyYv8QYe81QKCKJghuQ/zh-cn_image_0000002658792607.png "点击放大")

     坐标选取了样图的左上角（浅蓝色区域），输出颜色值：BGRA(255,223,175,255)，符合预期。

     完整代码如下所示：

     ```ts
     import { BusinessError } from '@kit.BasicServicesKit';
     import { image } from '@kit.ImageKit';
     import { common } from '@kit.AbilityKit';
     import { effectKit } from '@kit.ArkGraphics2D';
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import { resourceManager } from '@kit.LocalizationKit';

     @Entry
     @Component
     struct Index {
       async colorPicker() {
         try {
           let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
           const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
           const fileData: Uint8Array = await resourceMgr.getMediaContent($r('app.media.ColorPicker').id);
           const buffer = fileData.buffer as ArrayBuffer;
           const imageSource: image.ImageSource = image.createImageSource(buffer);
           const pixelMap: image.PixelMap = await imageSource.createPixelMap();
           const area: image.PositionArea = {
             pixels: new ArrayBuffer(4),
             offset: 0,
             stride: 4,
             region: { size: { height: 1, width: 1 }, x: 0, y: 0 },
           };
           if (pixelMap !== undefined) {
             pixelMap.readPixels(area).then(() => {
               console.info('Succeeded in reading the image data in the area.'); // 符合条件则进入。
               console.info('BGRA data is ', new Uint8Array(area.pixels));
             }).catch((error: BusinessError) => {
               console.error(`Failed to read the image data in the area. code is ${error.code}, message is ${error.message}`); // 不符合条件则进入。
             });
           }
           effectKit.createColorPicker(pixelMap, (err, colorPicker) => {
             if (err) {
               console.error(`failed to create color picker.`);
             }
             // 同步主色获取
             const color = colorPicker.getMainColorSync();
             console.info('get main color =', '{red:', color.red, 'green:', color.green, 'blue:', color.blue, 'alpha:',
               color.alpha, '}');
             // 获取占比最大的颜色
             const largestColor = colorPicker.getLargestProportionColor();
             console.info('get largest proportion color =' + '{red:', largestColor.red, 'green:', largestColor.green,
               'blue:', largestColor.blue, 'alpha:', largestColor.alpha, '}');
             // 获取占比靠前的颜色值
             const topColors = colorPicker.getTopProportionColors(2);
             for (let index = 0; index < topColors.length; index++) {
               if (topColors[index]) {
                 console.info('get top proportion colors: index ' + index + ', color ' + '{red:', topColors[index]?.red,
                   'green:', topColors[index]?.green, 'blue:', topColors[index]?.blue, 'alpha:',
                   topColors[index]?.alpha, '}');
               }
             }
             // 获取平均色
             const averageColor = colorPicker.getAverageColor();
             console.info('get average color =' + '{red:', averageColor.red, 'green:', averageColor.green, 'blue:',
               averageColor.blue, 'alpha:', averageColor.alpha, '}');
             // 获取饱和度最高的颜色
             const highestSatColor = colorPicker.getHighestSaturationColor();
             console.info('get highest SatColor color =', '{red:', highestSatColor.red, 'green:', highestSatColor.green,
               'blue:', highestSatColor.blue, 'alpha:', highestSatColor.alpha, '}');
             // 黑白灰检测
             const isNeutral = colorPicker.isBlackOrWhiteOrGrayColor(0xFFFF00FF);
             console.info('isBlackOrWhiteOrGrayColor', isNeutral);
           });
         } catch (e) {
           hilog.error(0x0000, 'TestTag', 'Failed error.code is %{public}d,error.message is %{public}s', e.code,
             e.message);
         }
       }

       build() {
         Row() {
           Column() {
             Image($r('app.media.ColorPicker'))
               .width(200);
             Button('获取图片像素值')
               .onClick(() => {
                 this.colorPicker();
               });
           };
         };
       }
     }
     ```

## 常见FAQ

Q：十进制的(r,g,b)值，如何才能转化为十六进制颜色代码（如："#0A59F7"）？

A：分为两步，先获取需要转换的各十进制颜色，再将其通过toString(16)方法转换为十六进制数。具体过程如下：

* 首先直接获取需要的十进制颜色值，分别获取各个颜色值。
* 将十进制转化成十六进制。核心参考代码如下（完整代码参考解决方案）：

  ```ts
  // 将十进制的bgra_8888像素值转换为十六进制的颜色值
  export function color2hex(color: effectKit.Color): string {
    const b = color.blue;
    const g = color.green;
    const r = color.red;
    const a = color.alpha;
    let rightColor =
      `#${a.toString(16)}${r.toString(16).padStart(2, '0')}${g.toString(16).padStart(2, '0')}${b.toString(16)
        .padStart(2, '0')}`;
    return rightColor;
  }
  ```

Q：十六进制的颜色（如："#0A59F7"），如何才能转化为十进制颜色(r,g,b)？

A：不包含透明度的十六进制颜色可能是6位数，也可能是3位数，因此首先需要扩展简写形式，将十六进制字符串统一处理为6位格式（如#FFF→#FFFFFF），再将6位颜色进行解析，最终得到十进制颜色，具体操作步骤如下：

* 扩展简写形式（无需扩展则省略），核心参考代码如下：
* 再将如"#0A59F7"的颜色值进行解析，2个字符代表1个颜色通道，因此对于该颜色字符串，红色需要使用slice(1, 3)方法，代表截取子串“0A”；绿色需要使用slice(3, 5)方法用于截取子串“59”；蓝色需要使用slice(5, 7)方法，代表截取子串“F7”；再使用parseInt方法将十六进制字符串转换为十进制数值，如：parseInt("FF", 16)→255。核心参考代码如下（完整代码参考解决方案）：

  ```ts
  export function hex2rgb(hex: string): Array<number> {
    if (hex.length === 4) {
      hex = '#' + hex[1] + hex[1] + hex[2] + hex[2] + hex[3] + hex[3];
    }
    const r = parseInt(hex.slice(1, 3), 16);
    const g = parseInt(hex.slice(3, 5), 16);
    const b = parseInt(hex.slice(5, 7), 16);
    return [r, g, b];
  }
  ```

最终返回一个数组[r,g,b]，分别对应红、绿、蓝通道的十进制值。

Q：能否直接获取网络图片的主色？

A：目前暂不支持直接获取网络图片的主色。需要将图片下载至本地沙箱转换为PixelMap后才可以进行获取主色操作，具体实现可参考：[多媒体像素图](../harmonyos-guides/arkts-graphics-display.md#多媒体像素图)。

## 总结

当前支持的图片取色接口及使用场景如下：

| 接口分类 | 接口 | 使用场景 |
| --- | --- | --- |
| 主色提取 | [getMainColor()](../harmonyos-references/js-apis-effectkit.md#getmaincolor) | 非阻塞式调用，后台线程执行计算，用于精确计算、复杂图像处理（如医疗影像中的主色识别）或大文件主色提取（如4K壁纸的主色提取）。 |
| 主色提取 | [getMainColorSync()](../harmonyos-references/js-apis-effectkit.md#getmaincolorsync) | 阻塞式调用，用于快速获取图像主色、实时反馈（如按钮点击即时变色）等。 |
| 高频颜色 | [getLargestProportionColor()](../harmonyos-references/js-apis-effectkit.md#getlargestproportioncolor10) | 统计像素频率最高颜色（适用于LOGO等高纯度场景）。 |
| Top N颜色 | [getTopProportionColors(n)](../harmonyos-references/js-apis-effectkit.md#gettopproportioncolors12) | 返回出现频率最高的前N个颜色。取值范围[1,10]。案例：根据照片生成5色配色方案。 |
| 饱和度分析 | [getHighestSaturationColor()](../harmonyos-references/js-apis-effectkit.md#gethighestsaturationcolor10) | 读取图片中最鲜艳的颜色，饱和度最高的颜色，只关注 HSV 中的 S（饱和度）。强调色提取（适用于视觉焦点检测）。案例：从风景照中提取最鲜艳的花朵色。 |
| 平均色计算 | [getAverageColor()](../harmonyos-references/js-apis-effectkit.md#getaveragecolor10) | 计算所有像素RGB均值（适用于渐变背景生成）。 |
| 黑白灰检测 | [isBlackOrWhiteOrGrayColor()](../harmonyos-references/js-apis-effectkit.md#isblackorwhiteorgraycolor10) | 判断颜色是否为中性色（阈值可配置）。 |
| 像素级读取 | [readPixelsSync(x, y)](../harmonyos-references/arkts-apis-image-pixelmap.md#readpixelssync12) | 直接读取指定坐标像素值。案例：取色笔。 |
