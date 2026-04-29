---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-aipp-parameters
title: AIPP参数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型转换 > AIPP > AIPP参数
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:87d2a4920bab7ca49afba259940a8a957641d5908d5f6c011eadf06d9eeff964
---

AIPP分为静态AIPP和动态AIPP，两者使用严格区分，静态AIPP模型不能接收模型推理时传入的AIPP参数，不兼容动态AIPP场景，静态与动态AIPP区别详见下表。

| AIPP | 设置AIPP参数方式 | 优点 |
| --- | --- | --- |
| 静态AIPP | 在模型生成时通过配置文件或者IR构图预置。 | 更高效率，模型加载阶段即可完成AIPP初始化。 |
| 动态AIPP | 仅标记该模型具备AIPP处理功能。 | 更灵活，每次推理可传入不同AIPP参数。 |

## AIPP支持的输入格式

AIPP可配置的图片格式如下：

* YUV420SP\_U8
* XRGB8888\_U8
* ARGB8888\_U8
* YUYV\_U8
* YUV422SP\_U8
* AYUV444\_U8
* YUV400\_U8
* RGB888\_U8

格式后缀U8表示图片像素点为Uint8类型，范围为0到255。当图片的输入为YUV类型时，无论是YUV420还是YUV422或者YUYV，AIPP自动将图片数据补齐为YUV444格式。

除以上列举的图片类型，AIPP还可以通过开启Channel Swap通道交换功能，支持更加丰富的图片输入格式。

说明

YUYV\_U8和AYUV444\_U8当前版本不支持。

## AIPP支持的功能

AIPP按照芯片的处理顺序，支持的功能如下：

* [Crop](cannkit-aipp-parameters.md#crop)：图片裁剪。
* [Channel Swap](cannkit-aipp-parameters.md#channel-swap)：通道交换。
* [Color Space Conversion](cannkit-aipp-parameters.md#color-space-conversion)：色域转换。
* [Resize](cannkit-aipp-parameters.md#resize)：图片缩放。
* [Data Type Conversion](cannkit-aipp-parameters.md#data-type-conversion)：数据类型转换。
* [Rotation](cannkit-aipp-parameters.md#rotation)：图片旋转。
* [Padding](cannkit-aipp-parameters.md#padding)：图片补边。

### Crop

AIPP的Crop功能用于对输入图片进行裁剪，涉及参数如下：

| **名称** | **描述** | **取值范围** |
| --- | --- | --- |
| switch | 裁剪使能开关。 | false/true |
| load\_start\_pos\_w | 裁剪起始位置水平方向坐标。 | load\_start\_pos\_w < src\_image\_size\_w |
| load\_start\_pos\_h | 裁剪起始位置垂直方向坐标。 | load\_start\_pos\_h < src\_image\_size\_h |
| crop\_size\_w | 裁剪出的图像宽度。 | load\_start\_pos\_w + crop\_size\_w <= src\_image\_size\_w |
| crop\_size\_h | 裁剪出的图像高度。 | load\_start\_pos\_h + crop\_size\_h <= src\_image\_size\_h |

YUV类型的图片受图片自身类型的限制，当输入图片类型为YUV420SP、YUYV、YUV422SP和AYUV444时，裁剪的起始坐标和裁剪的宽高都应该是偶数，系统会进行校验。

### Channel Swap

AIPP支持两种类型的通道交换：RB/UV通道交换和AX通道交换。

RB/UV通道交换丰富了输入图片的格式，开启RB/UV通道交换后，AIPP支持的图片输入格式比可配置的输入类型丰富了一倍。

| 配置类型 | 可接受图片类型 |
| --- | --- |
| YUV420SP\_U8 | YUV420，YVU420 + rbuv\_swap\_switch |
| XRGB8888\_U8 | XRGB，XBGR + rbuv\_swap\_switch |
| ARGB8888\_U8 | ARGB，ABGR + rbuv\_swap\_switch |
| RGB888\_U8 | BGR + rbuv\_swap\_switch |
| YUYV\_U8 | YUYV，YVYU + rbuv\_swap\_switch |
| YUV422SP\_U8 | YUV422，YVU422 + rbuv\_swap\_switch |
| AYUV444\_U8 | AYUV + rbuv\_swap\_switch |

当配置的图片输入格式为XRGB、ARGB或AYUV时，支持开启AX通道交换。开启通道交换后，图片第一个通道的输入被搬移到第四个通道上，即当XRGB、ARGB和AYUV开启AX通道交换后，转变为RGBX、RGBA和YUVA。

当模型训练集为RGB格式的图片，而推理时的图片输入为XRGB或者ARGB时，可以通过使能AX通道交换，将RGB通道前移，实现兼容。

### Color Space Conversion

色域转换（Color Space Conversion，以下简称CSC），特指在YUV444和RGB888两种图片格式之间进行转换。涉及如下配置参数。

| **名称** | **描述** | **类型** | **取值范围** |
| --- | --- | --- | --- |
| csc\_switch | CSC开关。 | bool | true/false |
| matrix\_r0c0  matrix\_r0c1  matrix\_r0c2  matrix\_r1c0  matrix\_r1c1  matrix\_r1c2  matrix\_r2c0  matrix\_r2c1  matrix\_r2c2 | CSC矩阵元素。 | int16 | [-32677, 32676] |
| output\_bias\_0  output\_bias\_1  output\_bias\_2 | RGB转YUV时的输出偏移。 | uint8 | [0, 255] |
| input\_bias\_0  input\_bias\_1  input\_bias\_2 | YUV转RGB时的输入偏移。 | uint8 | [0, 255] |

参考1：YUV和BGR的转换公式。

* YUV转BGR

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/lQ8TuwWDQGuY2twEZSDAlg/zh-cn_image_0000002558765718.png?HW-CC-KV=V1&HW-CC-Date=20260429T054056Z&HW-CC-Expire=86400&HW-CC-Sign=379CD9DD33FC2B5A5CCA437F021C87FBCAF685280297E31140A76467FD893593)
* BGR转YUV

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/MnG3VcpWQNKNC1GA7CWUuQ/zh-cn_image_0000002558606062.png?HW-CC-KV=V1&HW-CC-Date=20260429T054056Z&HW-CC-Expire=86400&HW-CC-Sign=6A403783D11D73D79C7288E2F6AF265A9B7292866E629CEB7F5D2393C24D5B6D)

参考2：BT-601 narrow、JPEG和BT-709 narrow三种类型图片的转换公式。

* BT-601 narrow

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/qOT-CrQ6T82arTOVAM1aJw/zh-cn_image_0000002589325589.png?HW-CC-KV=V1&HW-CC-Date=20260429T054056Z&HW-CC-Expire=86400&HW-CC-Sign=E474CE3BA3E0AD117D248C8224E5E7C8B0683744DDC1BF46455E72A22C6F400A)
* JPEG

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/wywfXrh7R72kzKYswvFpxA/zh-cn_image_0000002589245527.png?HW-CC-KV=V1&HW-CC-Date=20260429T054056Z&HW-CC-Expire=86400&HW-CC-Sign=378FECB5FAFDFF93A9CEED8C4E4A66B6EFE0AA057CE277BA74562CA2C22A6B4D)
* BT-709 narrow

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/QUAeqF0jSwqF2_GQbOtVIQ/zh-cn_image_0000002558765720.png?HW-CC-KV=V1&HW-CC-Date=20260429T054056Z&HW-CC-Expire=86400&HW-CC-Sign=86F9EC1506274FE0358AEC6795E2BDC02466355F54F27D35ADDD054818919BD3)

使用配置文件生成静态AIPP模型时，需要根据以上的公式配置CSC矩阵以及"input\_bias"或者"output\_bias"的值。使用IR定义AIPP CSC功能算子，以及使用CANN Kit接口配置CSC参数时，支持传入目标类型，由系统来填充CSC配置参数。

以下为JPEG和BT-601NARROW两种图片类型下的CSC配置参考。

* 输入为YUV格式图片(YUV420/YUYV/YUV422SP/AYUV444)，模型训练集为RGB，不支持从YUV400到RGB的转换。

  | JPEG | BT-601NARROW | BT-601FULL | BT-709NARROW |
  | --- | --- | --- | --- |
  | matrix\_r0c0 : 256  matrix\_r0c1 : 0  matrix\_r0c2 : 359  matrix\_r1c0 : 256  matrix\_r1c1 : -88  matrix\_r1c2 : -183  matrix\_r2c0 : 256  matrix\_r2c1 : 454  matrix\_r2c2 : 0  input\_bias\_0 : 0  input\_bias\_1 : 128  input\_bias\_2 : 128 | matrix\_r0c0 : 298  matrix\_r0c1 : 0  matrix\_r0c2 : 409  matrix\_r1c0 : 298  matrix\_r1c1 : -100  matrix\_r1c2 : -208  matrix\_r2c0 : 298  matrix\_r2c1 : 516  matrix\_r2c2 : 0  input\_bias\_0 : 16  input\_bias\_1 : 128  input\_bias\_2 : 128 | matrix\_r0c0 : 256  matrix\_r0c1 : 0  matrix\_r0c2 : 359  matrix\_r1c0 : 256  matrix\_r1c1 : -88  matrix\_r1c2 : -183  matrix\_r2c0 : 256  matrix\_r2c1 : 454  matrix\_r2c2 : 0  input\_bias\_0 : 0  input\_bias\_1 : 128  input\_bias\_2 : 128 | matrix\_r0c0 : 298  matrix\_r0c1 : 0  matrix\_r0c2 : 460  matrix\_r1c0 : 298  matrix\_r1c1 : -55  matrix\_r1c2 : -137  matrix\_r2c0 : 298  matrix\_r2c1 : 541  matrix\_r2c2 : 0  input\_bias\_0 : 16  input\_bias\_1 : 128  input\_bias\_2 : 128 |
* 输入为YUV格式图片(YUV420/YUYV/YUV422SP/AYUV444)，模型训练集为BGR，不支持从YUV400到BGR的转换。

  | JPEG | BT-601NARROW | BT-601FULL | BT-709NARROW |
  | --- | --- | --- | --- |
  | matrix\_r0c0 : 256  matrix\_r0c1 : 454  matrix\_r0c2 : 0  matrix\_r1c0 : 256  matrix\_r1c1 : -88  matrix\_r1c2 : -183  matrix\_r2c0 : 256  matrix\_r2c1 : 0  matrix\_r2c2 : 359  input\_bias\_0 : 0  input\_bias\_1 : 128  input\_bias\_2 : 128 | matrix\_r0c0 : 298  matrix\_r0c1 : 516  matrix\_r0c2 : 0  matrix\_r1c0 : 298  matrix\_r1c1 : -100  matrix\_r1c2 : -208  matrix\_r2c0 : 298  matrix\_r2c1 : 0  matrix\_r2c2 : 409  input\_bias\_0 : 16  input\_bias\_1 : 128  input\_bias\_2 : 128 | matrix\_r0c0 : 256  matrix\_r0c1 : 454  matrix\_r0c2 : 0  matrix\_r1c0 : 256  matrix\_r1c1 : -88  matrix\_r1c2 : -183  matrix\_r2c0 : 256  matrix\_r2c1 : 0  matrix\_r2c2 : 359  input\_bias\_0 : 0  input\_bias\_1 : 128  input\_bias\_2 : 128 | matrix\_r0c0 : 298  matrix\_r0c1 : 541  matrix\_r0c2 : 0  matrix\_r1c0 : 298  matrix\_r1c1 : -55  matrix\_r1c2 : -137  matrix\_r2c0 : 298  matrix\_r2c1 : 0  matrix\_r2c2 : 460  input\_bias\_0 : 16  input\_bias\_1 : 128  input\_bias\_2 : 128 |
* 输入为YUV格式图片(YUV420/YUYV/YUV422SP/AYUV444)，模型训练集为灰度图（YUV400\_U8）。

  | JPEG | BT-601NARROW | BT-601FULL | BT-709NARROW |
  | --- | --- | --- | --- |
  | matrix\_r0c0 : 256  matrix\_r0c1 : 0  matrix\_r0c2 : 0  matrix\_r1c0 : 0  matrix\_r1c1 : 0  matrix\_r1c2 : 0  matrix\_r2c0 : 0  matrix\_r2c1 : 0  matrix\_r2c2 : 0 | N/A | N/A | N/A |
* 输入为RGB格式图片(XRGB8888/ARGB8888)，模型训练集为灰度图（YUV400\_U8）。

  | JPEG | BT-601NARROW | BT-601FULL | BT-709NARROW |
  | --- | --- | --- | --- |
  | matrix\_r0c0 : 76  matrix\_r0c1 : 150  matrix\_r0c2 : 30  matrix\_r1c0 : 0  matrix\_r1c1 : 0  matrix\_r1c2 : 0  matrix\_r2c0 : 0  matrix\_r2c1 : 0  matrix\_r2c2 : 0 | N/A | N/A | N/A |
* 输入为RGB格式图片(XRGB8888/ARGB8888)，模型训练集为YUV444SP。

  | JPEG | BT-601NARROW | BT-601FULL | BT-709NARROW |
  | --- | --- | --- | --- |
  | matrix\_r0c0 : 77  matrix\_r0c1 : 150  matrix\_r0c2 : 29  matrix\_r1c0 : -43  matrix\_r1c1 : -85  matrix\_r1c2 : 128  matrix\_r2c0 : 128  matrix\_r2c1 : -107  matrix\_r2c2 : -21  output\_bias\_0 : 0  output\_bias\_1 : 128  output\_bias\_2 : 128 | matrix\_r0c0 : 66  matrix\_r0c1 : 129  matrix\_r0c2 : 25  matrix\_r1c0 : -38  matrix\_r1c1 : -74  matrix\_r1c2 : 112  matrix\_r2c0 : 112  matrix\_r2c1 : -94  matrix\_r2c2 : -18  output\_bias\_0 : 16  output\_bias\_1 : 128  output\_bias\_2 : 128 | matrix\_r0c0 : 77  matrix\_r0c1 : 150  matrix\_r0c2 : 29  matrix\_r1c0 : -43  matrix\_r1c1 : -85  matrix\_r1c2 : 128  matrix\_r2c0 : 128  matrix\_r2c1 : -107  matrix\_r2c2 : -21  output\_bias\_0 : 0  output\_bias\_1 : 128  output\_bias\_2 : 128 | matrix\_r0c0 : 47  matrix\_r0c1 : 157  matrix\_r0c2 : 16  matrix\_r1c0 : -26  matrix\_r1c1 : -87  matrix\_r1c2 : 112  matrix\_r2c0 : 112  matrix\_r2c1 : -102  matrix\_r2c2 : -10  output\_bias\_0 : 16  output\_bias\_1 : 128  output\_bias\_2 : 128 |
* 输入为RGB格式图片(XRGB8888/ARGB8888)，模型训练集为YVU444SP。

  | JPEG | BT-601NARROW | BT-601FULL | BT-709NARROW |
  | --- | --- | --- | --- |
  | matrix\_r0c0 : 77  matrix\_r0c1 : 150  matrix\_r0c2 : 29  matrix\_r1c0 : 128  matrix\_r1c1 : -107  matrix\_r1c2 : -21  matrix\_r2c0 : -43  matrix\_r2c1 : -85  matrix\_r2c2 : 128  output\_bias\_0 : 0  output\_bias\_1 : 128  output\_bias\_2 : 128 | matrix\_r0c0 : 66  matrix\_r0c1 : 129  matrix\_r0c2 : 25  matrix\_r1c0 : 112  matrix\_r1c1 : -94  matrix\_r1c2 : -18  matrix\_r2c0 : -38  matrix\_r2c1 : -74  matrix\_r2c2 : 112  output\_bias\_0 : 16  output\_bias\_1 : 128  output\_bias\_2 : 128 | matrix\_r0c0 : 77  matrix\_r0c1 : 150  matrix\_r0c2 : 29  matrix\_r1c0 : 128  matrix\_r1c1 : -107  matrix\_r1c2 : -21  matrix\_r2c0 : -43  matrix\_r2c1 : -85  matrix\_r2c2 : 128  output\_bias\_0 : 0  output\_bias\_1 : 128  output\_bias\_2 : 128 | matrix\_r0c0 : 47  matrix\_r0c1 : 157  matrix\_r0c2 : 16  matrix\_r1c0 : 112  matrix\_r1c1 : -102  matrix\_r1c2 : -10  matrix\_r2c0 : -26  matrix\_r2c1 : -87  matrix\_r2c2 : 112  output\_bias\_0 : 16  output\_bias\_1 : 128  output\_bias\_2 : 128 |

说明

从使用的角度，将灰度图转成RGB没有意义，系统约束当输入格式配置为YUV400\_U8时，不支持CSC。

### Resize

图片缩放参数及约束如下：

| **名称** | **描述** | **取值范围（静态）** | **取值范围（动态）** |
| --- | --- | --- | --- |
| switch | 缩放使能开关 | false/true | false/true |
| resize\_input\_w | 缩放前图像宽度 | [16, 4096] | [16, 1280] |
| resize\_input\_h | 缩放前图像高度 | [16, 4096] | [16, 4096] |
| resize\_output\_w | 缩放后图像宽度 | [16, 1280] | [16, 448] |
| resize\_output\_h | 缩放后图像高度 | [16, 4096] | [16, 4096] |

图片缩放倍数约束如下：

| 名称 | 描述 | 范围（动态&静态） |
| --- | --- | --- |
| resize\_output\_w / resize\_input\_w | 图像宽度缩放倍数 | [1/16, 16] |
| resize\_output\_h / resize\_input\_h | 图像高度缩放倍数 | [1/16, 16] |

Resize类型为双线性插值。Resize子功能的"resize\_input\_w"和"resize\_input\_h"两个参数对开发者不可见。

* 当Crop功能关闭时，图片缩放前的大小取输入图片的大小。
* 当Crop功能打开时，因为AIPP的Resize处理总是在Crop之后，图片缩放前的大小取图片裁剪后的大小。配置时，只需要关心缩放后的大小即可。

通过配置文件转换静态AIPP模型时，Crop之后的大小crop\_size\_w和crop\_size\_h，以及Resize之后的大小resize\_output\_w和resize\_output\_h可以省去不配置，前提是这两个参数可以通过计算获取。省略resize\_output\_w和resize\_output\_h时，Resize功能这两个值取模型训练集的图片尺寸减去AIPP Padding之后的结果；当Resize不使用时，同理可省略Crop功能crop\_size\_w和crop\_size\_h。

### Data Type Conversion

数据类型转换（Data Type Conversion，以下简称DTC），DTC用于将输入图片中像素值转换为模型训练时的数据类型。AIPP允许开发者设置DTC参数，使得转换之后的数据在一个预期的范围，避免强制转换。

将Uint8类型的数据转换为Int8类型的数据，计算规则如下：

pixel\_out\_chx(i) = pixel\_in\_chx(i)-mean\_chn\_i

将Uint8类型的数据转换为Float16类型的数据，计算规则如下：

pixel\_out\_chx(i) = [pixel\_in\_chx(i)-mean\_chn\_i-min\_chn\_i] \* var\_reci\_chn

DTC涉及的配置参数如下表。

| **名称** | **描述** | **取值范围** |
| --- | --- | --- |
| switch | DTC使能开关。 | false/true |
| mean\_chn\_0 | 通道0均值。 | [0, 255] |
| mean\_chn\_1 | 通道1均值。 | [0, 255] |
| mean\_chn\_2 | 通道2均值。 | [0, 255] |
| mean\_chn\_3 | 通道3均值。 | [0, 255] |
| min\_chn\_0 | 通道0最小值。 | [-65504, 65504] |
| min\_chn\_1 | 通道1最小值。 | [-65504, 65504] |
| min\_chn\_2 | 通道2最小值。 | [-65504, 65504] |
| min\_chn\_3 | 通道3最小值。 | [-65504, 65504] |
| var\_reci\_chn\_0 | 通道0方差。 | [-65504, 65504] |
| var\_reci\_chn\_1 | 通道1方差。 | [-65504, 65504] |
| var\_reci\_chn\_2 | 通道2方差。 | [-65504, 65504] |
| var\_reci\_chn\_3 | 通道3方差。 | [-65504, 65504] |

说明

当DTC开关为false时，或者开发者调用CANN Kit接口未传入DTC参数时，系统默认对图片输入数据进行类型强转，效果同通道均值和最小值均为0，通道方差为1。

### Rotation

AIPP的Rotation功能用于对输入图片进行旋转，涉及的参数如下：

| **名称** | **描述** | **取值范围** |
| --- | --- | --- |
| switch | Rotation使能开关 | false/true |
| rotation\_angle | 图像旋转角度 | [0, 90, 180, 270] |

### Padding

AIPP的Padding功能用于对输入图片进行补边，涉及的参数如下。

| **名称** | **描述** | **取值范围** |
| --- | --- | --- |
| switch | Padding使能开关。 | false/true |
| left\_padding\_size | 图像左侧Padding像素数。 | N/A |
| right\_padding\_size | 图像右侧Padding像素数。 | N/A |
| top\_padding\_size | 图像上侧Padding像素数。 | N/A |
| bottom\_padding\_size | 图像下侧Padding像素数。 | N/A |
| padding\_value\_chn\_0 | 通道0 Padding的值。 | [-65504, 65504] |
| padding\_value\_chn\_1 | 通道1 Padding的值。 | [-65504, 65504] |
| padding\_value\_chn\_2 | 通道2 Padding的值。 | [-65504, 65504] |
| padding\_value\_chn\_3 | 通道3 Padding的值。 | [-65504, 65504] |

说明

* 上下左右的Padding值不要超过32，如果Padding值过大，AIPP将使用软件代码进行处理，效率低于硬件实现。
* padding\_value\_chn\_0~padding\_value\_chn\_3暂不支持。
