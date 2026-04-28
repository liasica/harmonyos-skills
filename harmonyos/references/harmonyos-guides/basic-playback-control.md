---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/basic-playback-control
title: 基础播控
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 应用接入播控自检 > 应用接入播控检查项详细说明 > 基础播控
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7915493e179be97d1dc0968ac0c915751490eac5ad7a5a2b3a6d643e24644824
---

## 媒体封面

注意

**自验证关注点：** 播放过程中查看播控中心是否显示媒体封面，封面图是否清晰。

应用提供媒体内容的封面图片（[AVMetadata.mediaImage](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)），如音乐专辑封面、视频海报等。如果应用提供的媒体封面比例或分辨率不满足要求，将会被自动缩放、裁切到合适大小。这可能导致封面图片内的信息损失或模糊，体验下降。mediaImage设置PixelMap性能更优。

音乐类媒体内容应提供比例为 1:1 的方形封面图片，建议分辨率为 800px \* 800px（如果应用提供的图片分辨率更大，将被压缩到 800px \* 800px 显示），最小分辨率是 300px \* 300px。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/o4AsBOrAQRCr8z5txD7s9Q/zh-cn_image_0000002552798906.png?HW-CC-KV=V1&HW-CC-Date=20260427T234552Z&HW-CC-Expire=86400&HW-CC-Sign=44499EAA49D0DC0DABAF33B19DFD44C3D74149BA844EF783FEEE456DC82583FE)

视频及其他类型的媒体内容除了上述建议分辨率的方形模板外，还支持纵向及横向的矩形封面模板。

纵向矩形模板的宽高比为13:18，如小于此比例，将会被自动缩放、裁切到该比例。

横向矩形模板的宽高比为16:9，如大于此比例，将会被自动缩放、裁切到该比例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/yPkdWtIuRoOI9bU2wIZFVg/zh-cn_image_0000002583438601.png?HW-CC-KV=V1&HW-CC-Date=20260427T234552Z&HW-CC-Expire=86400&HW-CC-Sign=55C80315858BEB458905184365B63C36D7907CA925B3DC74202A6B0210924D7F)

## 主标题

注意

**自验证关注点：** 播放过程中查看播控中心是否显示主标题，显示是否正确。

主标题（[AVMetadata.title](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)）用于显示歌曲名、影片名等内容名称，直播应用也可设置直播间名等，用于向用户展示当前正在播放的媒体内容，建议采用简短的字符串。字符串超长时会从右向左滚动显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/2yfi6kGOTu-2CcTqXplG9Q/zh-cn_image_0000002552958556.png?HW-CC-KV=V1&HW-CC-Date=20260427T234552Z&HW-CC-Expire=86400&HW-CC-Sign=21AEC518F726707950B05E2523D83E9202816364697D2F5014D5E274933091CF)

## 进度与时间

注意

**自验证关注点：** 播放过程中查看播控中心进度条是否正常显示，是否支持拖拽，拖拽后是否正确响应，不出现进度条回弹、抖动等。

**进度的显示**

播控中心支持显示如下三种形式的进度条，为保证用户体验，应用需尽量支持第一种进度条。

1. 应用内本身支持进度调节，提供当前播放的媒体内容的播放时长（[AVMetadata.duration](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)），注册进度控制（[seek](../harmonyos-references/arkts-apis-avsession-avsession.md#onseek10)）。播控显示第一种可拖动进度条。
2. 应用内本身不支持进度调节，可提供当前播放的媒体内容播放时长，不注册进度控制。播控显示第二种不可拖动，但进度随时间自动前进的进度条。
3. 应用内本身不支持进度调节，且无法获取媒体内容播放时长（如直播），可不提供媒体播放时长，不注册进度控制。播控显示第三种进度条，告知用户当前进度条不可使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/NAoJ7qW3Q2ior_2gPeduVA/zh-cn_image_0000002583478557.png?HW-CC-KV=V1&HW-CC-Date=20260427T234552Z&HW-CC-Expire=86400&HW-CC-Sign=3DFEC83D49B1EDB3B801C3D75F1A82232D0BA888D6D2F016B242FD22F0F41456)

**进度的控制**

第一种可拖动进度条，表示用户可通过播控中心，调节应用媒体播放进度。为了达到进度调节的一致体验，请参考如下内容开发：

1. 应用不需要通过[AVPlaybackState](../harmonyos-references/arkts-apis-avsession-i.md#avplaybackstate10)实时设置进度，播控中心会根据应用设置的信息自行进行播放进度的计算。只需要在应用播放状态、播放进度、倍速发生变化时，再更新AVPlaybackState。

   如：

   （1）应用播放、暂停时需要设置播放状态或暂停状态，及当前播放或暂停时的进度。

   （2）用户通过播控中心调节进度条，应用收到调节的回调，或在应用内调节进度条，应用都需要通知播控当前调节完毕的状态与进度。

   （3）应用在真实播放开始时，再设置起始进度；若播放存在缓冲状态，可以先上报播放状态为[PLAYBACK\_STATE\_BUFFERING](../harmonyos-references/arkts-apis-avsession-e.md#playbackstate10)，来通知播控显示为播放但不走进度。
2. VIP/广告进度处理。

   * 支持试听/试看

     a. 应用不需要设置完整的歌曲时长，则只需要设置歌曲的试听时长。当应用仅设置歌曲的试听时长而不是完整时长，用户在播控中心触发进度控制时，应用收到的时长也是VIP试听时长内的相对时间戳位置，而不是完整歌曲的绝对时间戳位置，应用需要重新计算歌曲从零开始的绝对时间戳进行实际响应处理。

     b. 如果应用设置完整歌曲时长，但需要系统支持试听片段，也可以在播放时上报起始进度position，当收到的seek指令超过试听片段时，上报试听截止position，系统播控的进度会跟随回弹。
   * 不支持试听/试看

     等同于不支持进度条，可按照第三种进度显示接入。
   * 支持广告

     + 播放广告时，单独设置广告的时长duration。
     + 当进入到正片播放的时候，则重新设置一次新的时长，以与广告进行区分。

## 副标题

注意

**自验证关注点：** 播放过程中查看播控中心是否显示副标题，显示是否正确。

副标题用于显示媒体内容的辅助信息，如歌曲的歌手名、影片的发布者信息、剧集/综艺节目的选集信息等。可通过[AVMetadata.subtitle](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)或者[AVMetadata.artist](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)，选其一设置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/gIL3HqTHS--q07FGrJoLVA/zh-cn_image_0000002552798908.png?HW-CC-KV=V1&HW-CC-Date=20260427T234552Z&HW-CC-Expire=86400&HW-CC-Sign=3795CFD55C0553B045FE136DF36544D4712E92B9CB5EBCEF42FFF62C2D774FC3)

## 滚动歌词

注意

**自验证关注点：** 播放过程中查看播控中心是否显示歌词，显示是否正确，是否随进度正确刷新显示。

歌曲类媒体内容如有歌词信息，可以选择在副标题区域显示歌词。将当前播放歌曲的全曲歌词内容，按照标准lyric格式拼接为字符串，如[00:25.44]xxx\r\n[00:26.44]xxx\r\n，通过[AVMetadata.lyric](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)设置给播控中心。播控中心会自动按照进度，在副标题位置刷新显示，应用不需要实现其余功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/t2HozN6NRi2fbX3Xl4aP6Q/zh-cn_image_0000002583438603.png?HW-CC-KV=V1&HW-CC-Date=20260427T234552Z&HW-CC-Expire=86400&HW-CC-Sign=93B6C0FCEBFB60489A92ADE609751FCC348A44DDCE65B92DD2F64773EB2DA10E)

## 媒体音源特殊标识

注意

**自验证关注点：** 播放过程中查看播控中心是否显示“AudioVivid”等标识。

应用可以提供当前播放的媒体内容的资源标签信息（[AVMetadata.displayTags](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)）。根据媒体资源的属性，应用可用提供标签信息以体现该媒体内容的特殊性，如：AudioVivid。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/izvXeoeVRnOKHZP-59x8yQ/zh-cn_image_0000002552958558.png?HW-CC-KV=V1&HW-CC-Date=20260427T234552Z&HW-CC-Expire=86400&HW-CC-Sign=771A56FB6B9386B6F97FEA964044A16855E360465D617BA6EC907A936E4F2D02)

## 播放/暂停

注意

**自验证关注点：** 播放过程中，进入播控中心，点击播放暂停查看是否生效，状态是否与应用内对应。

应用需支持播控中心播放暂停，在接收到播控的播放/暂停回调，或者用户在应用内播放暂停，需上报当前的播放状态与进度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/iehRuzGfTX6Xctn27XwlSA/zh-cn_image_0000002583478559.png?HW-CC-KV=V1&HW-CC-Date=20260427T234552Z&HW-CC-Expire=86400&HW-CC-Sign=3B323EF95C3D785339175DC6D78709E838ECB61598E8418AA8A0DA2B9E41FEF6)

## 上下一首/集

注意

**自验证关注点：** 播放过程中，进入播控中心，点击上一首、下一首查看是否生效，播放内容是否与应用内对应。

应用按照内部实现，接入上下一首/集，在接收到播控的上下一首/集回调，或者用户在应用切歌切集时，需上报切换后新的媒体信息，播放状态、进度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/RyXs2B_2TuqCozI41L_OtQ/zh-cn_image_0000002552798910.png?HW-CC-KV=V1&HW-CC-Date=20260427T234552Z&HW-CC-Expire=86400&HW-CC-Sign=AFE47311FD13CF2008A57F8E734C39851A57A51366841FEF7EA228704CC9153B)

## 按钮置灰

注意

**自验证关注点：** 播放过程中，进入播控中心，查看不支持的功能按钮是否已置灰。请按照自检表按应用类型接入必需的控制指令，以保障用户的体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/nF9nGVWjTCO82fzYRL_QaA/zh-cn_image_0000002583438605.png?HW-CC-KV=V1&HW-CC-Date=20260427T234552Z&HW-CC-Expire=86400&HW-CC-Sign=B2FFD5B3E9DD673D16C1073CDE1891279DF6F3AEB60BDEB0174BCE68AB693ED9)

应用按照内部实现，按需注册支持的播放控制指令。对于未注册的播放控制指令，在播控中心会显示为上图置灰样式，明确告知用户当前指令该应用不支持。具体实现可参考[应用接入AVSession-不支持命令的处理](avsession-access-scene.md#不支持命令的处理)。

## 点击播控卡片跳转应用指定页面

注意

**自验证关注点：** 播放过程中，进入播控中心，点击封面大图查看是否跳转至应用当前播放页面。

用户通过点击播控卡片，应跳转到应用的具体业务页，如：音乐/听书/视频的播放详情页，直播间页，新闻阅读播放页，浏览器具体tab页。具体实现可参考[媒体会话提供方-开发步骤](using-avsession-developer.md#开发步骤)的第3步。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/Lxm-zsFcSM6xOEa5T3Tiog/zh-cn_image_0000002552958560.png?HW-CC-KV=V1&HW-CC-Date=20260427T234552Z&HW-CC-Expire=86400&HW-CC-Sign=735F1BB61546EDE10BAC240E7707B7E106F81DDD9632B1F83D911812363A3A0F)

## 收藏

注意

**自验证关注点：** 播放过程中，进入播控中心，点击收藏按钮，查看是否生效，是否与应用内同功能按钮状态一致。

音乐/听书类应用，如应用内支持收藏/喜欢功能，可按需适配播控的收藏功能，用户播放过程中可以通过播控中心点击收藏/取消收藏。应用适配收藏功能，接收到播控的收藏/取消收藏的回调，或者用户在应用内点击收藏/取消收藏，均需上报当前播放内容的收藏状态，保证应用与播控的显示一致。具体实现可参考[应用接入AVSession-收藏](avsession-access-scene.md#收藏)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/xVNkouWwQcyv3HvNoakZWQ/zh-cn_image_0000002583478561.png?HW-CC-KV=V1&HW-CC-Date=20260427T234552Z&HW-CC-Expire=86400&HW-CC-Sign=EB067421738EDCD00B58C54DF0DA2DA43E770A6153E418E2F216151F8F7D11A8)

## 循环模式

注意

**自验证关注点：** 播放过程中，进入播控中心，点击切换循环模式，查看是否生效。

音乐/听书类应用，如应用内支持播放模式的切换，可按需适配播控的循环模式切换功能。

播控可支持的播放模式有：顺序播放、列表循环、单曲循环、随机播放。

应用适配循环模式切换功能，收到播控中心循环模式切换的回调后，或用户在应用内切换循环模式时，按照应用内定义的顺序，向播控上报切换后的循环模式。

例：收到播控切换循环模式回调参数为列表循环，表示当前的循环模式，应用内下一个循环模式为随机播放，就切换到随机播放，并设置AVPlaybackState的LoopMode为随机播放。

若应用内支持的循环模式不在系统固定的四个循环模式内，需要选择四个固定循环模式其一向系统上报，由应用自定。

例：收到播控切换循环模式回调参数为列表循环，表示当前的循环模式，应用内下一个循环模式为心动模式，可上报为随机播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/9avbDun8T7ivIy_k23GHXw/zh-cn_image_0000002552798912.png?HW-CC-KV=V1&HW-CC-Date=20260427T234552Z&HW-CC-Expire=86400&HW-CC-Sign=FFEA14FA21EF3B45520FA1DA0A939E473D57A0616EF489705033AD9E6AB85DC3)

## 快进/快退

注意

**自验证关注点：** 播放过程中，进入播控中心，点击快进、快退查看是否正常响应，播控中心进度是否显示正确。

对于需要频繁调节播放进度的媒体内容（如播客、听书等长音频媒体，或长视频媒体），应用可以适配快进快退功能。

可选择快进快退的时间长度：[10s、15s、30s](../harmonyos-references/arkts-apis-avsession-e.md#skipintervals11)。如下图显示。用户通过播控中心快进/快退，或在应用内快进快退，应用都需要通知播控当前调节完毕的状态与进度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/mjD81QveSLW27oP62Xz4YQ/zh-cn_image_0000002583438607.png?HW-CC-KV=V1&HW-CC-Date=20260427T234552Z&HW-CC-Expire=86400&HW-CC-Sign=39638B8064165073B4A9C3A63AE2EC15CEC672CBE861163E416FEBBEEF0CCF7C)
