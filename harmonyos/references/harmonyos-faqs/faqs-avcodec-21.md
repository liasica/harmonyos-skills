---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-21
title: 视频解码如何传入SPS，PPS数据
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 视频解码如何传入SPS，PPS数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:81a765c5c2ac155e7d476aee079a201abbc48857f14dc3c02a16cbc01d6e4829
---

## 问题现象

视频文件在解封装后得到H264裸流数据，然后使用编码器工具VideoDecoder组件时使用其硬解码功能，在创建解码器时，如何传入SPS，PPS数据给解码器？

## 背景知识

SPS和PPS都为H264编码中的重要数据信息。

* SPS：即Sequence Paramater Set，序列参数集。即原始视频的每一帧的像素数据经过编码之后的结构组成的序列。而每一帧的编码后数据所依赖的参数保存于图像参数集中。
* PPS：Picture Paramater Set，图像参数集。即图像的一些参数，宽、高等。

H264原始码流是由若干NALU组成的结构，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/7Rgl6J79RMmnom5Yji7RRw/zh-cn_image_0000002658791637.png)

* NALU（Network Abstraction Layer Units）：网络抽象层。

  每个NAL单元是一个有一定语法元素的可变长字节字符串，包括一个字节的NAL Header（用来表示数据类型），以及若干整数字节的原始字节序列负荷（RBSP）。在实际的H264数据帧中，往往帧前面带有00 00 00 01或00 00 01的分隔符，其后跟随NAL单元数据。一个NAL单元可以携带一个编码片，I帧、P帧、B帧、一个序列参数集（SPS）、或一个图像参数集（PPS）。

  H264采用NAL单元可以适用于多种网络，而且能进一步提高其抗误码能力。通过序列号的设置可以发现丢失的是哪一个VLC单元，冗余编码图像使得基本编码图像丢失仍可得到较粗糙的图像。

  NAL Header（1 byte）的组成为：forbidden\_zero\_bit(1bit)+nal\_ref\_idc(2bit)+nal\_unit\_type(5bit)

  forbidden\_zero\_bit：禁止位，初始为0，当网络发现NAL单元有比特错误时可设置该比特为1，以便接收方纠错或丢掉该单元。

  nal\_ref\_idc：nal重要性指示，标志该NAL单元的重要性，值越大，越重要，解码器在解码处理不过来的时候，可以丢掉重要性为0的NALU。

  nal\_unit\_type：用来识别不同NAL单元类型：

| nal\_unit\_type | NAL单元和RBSP语法结构的内容 |
| --- | --- |
| 0 | 未指定 |
| 1 | 一个非 IDR 图像的编码条带 |
| 2 | 编码条带数据分割块A |
| 3 | 编码条带数据分割块B |
| 4 | 编码条带数据分割块C |
| 5 | IDR图像的编码条带 |
| 6 | 辅助增强信息 （SEI） |
| 7 | 序列参数集 |
| 8 | 图像参数集 |
| 9 | 访问单元分隔符 |
| 10 | 序列结尾 |
| 11 | 流结尾 |
| 12 | 填充数据 |
| 13 | 序列参数集扩展 |
| 14~18 | 保留 |
| 19 | 未分割的辅助编码图像的编码条带 |
| 20~23 | 保留 |
| 24~31 | 未指定 |

其中值为7和8的nal\_unit\_type就为需要设置的SPS和PPS参数。

## 解决方案

使用AVCodec进行解码的流程中，给视频解码器传入SPS和PPS数据，都需要通过[OH\_VideoDecoder\_PushInputBuffer](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_pushinputbuffer)函数在传入首帧数据时传入SPS/PPS数据。

传入SPS、PPS数据也分为首次传入和重新传入两种情况，两种情况的操作流程有一些区别：

1. 首次传入SPS/PPS数据：

   在创建解码器并首次配置完回调函数和参数后，调用[OH\_VideoDecoder\_Start](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_start)函数让解码器开始工作。然后通过调用OH\_VideoDecoder\_PushInputBuffer函数在首帧传入SPS/PPS帧和I帧的拼接帧或者仅传入SPS/PPS帧，即可首次传入SPS、PPS数据给解码器。

   具体代码实现可以参考：[视频解码Surface模式](../harmonyos-guides/video-decoding.md#surface模式)中调用OH\_VideoDecoder\_Start的步骤和调用OH\_VideoDecoder\_PushInputBuffer步骤。
2. 重新传入SPS/PPS数据：

   在解码器创建之后，需要重新传入SPS/PPS数据或者分批次传入SPS/PPS的数据时，可以[使用OH\_VideoDecoder\_Flush](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_flush)函数刷新解码器，在刷新解码器后，解码器仍处于运行态，但会清除解码器中缓存的输入和输出数据及参数集如H.264格式的PPS/SPS，此时调用OH\_VideoDecoder\_Start接口重新让解码器开始工作，再调用OH\_VideoDecoder\_PushInputBuffer函数传入SPS/PPS帧和I帧的拼接帧或者仅传入SPS/PPS帧，即可重新传入SPS、PPS数据给解码器。

   具体代码实现可以参考：[视频解码Surface模式](../harmonyos-guides/video-decoding.md#surface模式)中调用OH\_VideoDecoder\_Flush的步骤。

## 常见FAQ

Q：如果在配置视频解码器时，已经通过OH\_MD\_KEY\_CODEC\_CONFIG设置了SPS/PPS，后续在输入解码帧时，是否需要继续输入SPS/PPS帧？

A：即使在调用[OH\_VideoDecoder\_Configure](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_configure)配置解码器时通过OH\_MD\_KEY\_CODEC\_CONFIG参数配置了SPS/PPS，后续写入解码数据时也必须传入SPS/PPS帧到输入缓冲区。解码时如果不传入SPS/PPS帧到视频解码器的缓冲区，将无法得到解码数据。

Q：AVCodec官方示例代码中解封装视频文件后输入视频解码器的首帧为SPS/PPS帧与I帧的拼接帧（Flags为AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA|AVCODEC\_BUFFER\_FLAGS\_SYNC\_FRAME）。是否要求输入视频解码器的首帧必须是SPS/PPS帧和I帧的拼接帧？

A：输入AVCodec视频解码器的首帧不一定要是SPS/PPS帧和I帧的拼接帧。可以首帧直接输入SPS/PPS帧和I帧的拼接帧（Flags为AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA|AVCODEC\_BUFFER\_FLAGS\_SYNC\_FRAME）；也可以先输入SPS/PPS帧（Flags为AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA）然后输入I帧（Flags为AVCODEC\_BUFFER\_FLAGS\_SYNC\_FRAME）。

Q：视频解码Flush后，如何重新获取SPS/PPS数据？

A：解码的首帧输入同时包含了SPS和PPS数据，可以将首帧buffer转换为16进制，buffer中以分隔符+x7（x为任意16进制数）开头到下一次分隔符的内容为SPS信息；以分隔符+x8（x为任意16进制数）开头到下一次分隔符的内容为PPS信息。将数据提取即可重新传入。

Q：OH\_VideoDecoder解码器输入的h264和h265的码流是AnnexB还是Avcc或者Hvcc？

A：视频解码输入码流仅支持AnnexB格式，且支持的AnnexB格式支持多slice，要求同一帧的多个slice一次送入解码器。详细可参考：视频解码的[限制约束](../harmonyos-guides/video-decoding.md#注意事项)。

Q：输入EOS packet，再调用视频解码器OH\_VideoDecoder\_Flush，然后调用OH\_VideoDecoder\_Start，此时概率性收到解码器的EOS output回调，按照预期，OH\_VideoDecoder\_Flush之后会失效所有input & output buffer，这是不是OH\_VideoDecoder\_Flush接口的bug?

A：OH\_VideoDecoder\_Flush只负责清除队列里的数据，不影响已发出的数据接收，不是bug。

Q：使用AVCodec Kit视频解码，如何判断手机是否支持H265？

A：目前手机已都支持H265，也可以通过[获取支持的编解码能力](../harmonyos-guides/obtain-supported-codecs.md)判断指定类别中的编解码器能力。
