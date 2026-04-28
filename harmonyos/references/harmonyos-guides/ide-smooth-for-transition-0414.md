---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smooth-for-transition-0414
title: 转场操作流畅
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 转场操作流畅
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b51849be08949369ee19f8ecfbbe4cdf5b4d9888d7620db9c3129ffb3aac3484
---

## 规则详情

应用的应用内转场过程卡顿率≤ 0ms/s；滑动过程卡顿率：动效时间内累计丢帧时间/动效时长。

## 检测逻辑

* 开始时间：以ABILITY\_OR\_PAGE\_SWITCH转场泳道为例，泳道的起点（如图标记1）。
* 结束时间：以ABILITY\_OR\_PAGE\_SWITCH转场泳道为例，泳道的终点（如图标记2）。

  其他转场泳道标记如下：

  H:APP\_TRANSITION\_FROM\_OTHER\_APP

  H:APP\_TRANSITION\_TO\_OTHER\_APP

  H:APP\_SWIPER\_NO\_ANIMATION\_SWITCH

  H:APP\_TABS\_NO\_ANIMATION\_SWITCH

  H:APP\_TABS\_FLING

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/1hY994AbQZmJ15riJP_CMA/zh-cn_image_0000002561832987.png?HW-CC-KV=V1&HW-CC-Date=20260427T235705Z&HW-CC-Expire=86400&HW-CC-Sign=061A502B7B5011B34DFC615D49E3325B7F100EA00DD1662D928C7652644F8A1C)

* 总时长(s)：【最后一个“H:Waiting for Present Fence xxxx” 时间（如图标记2）】 - 【第一个“H:Waiting for Present Fence xxxx” 时间（如图标记1）】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/8Hcz0J8eQoWxHvpGeEHsRA/zh-cn_image_0000002561832979.png?HW-CC-KV=V1&HW-CC-Date=20260427T235705Z&HW-CC-Expire=86400&HW-CC-Sign=804B6A51008C06C6DF9917B4264FBF438B8CACF81A7E5659600520490644CE2E)

* 每帧时长(ms)：1000ms / 刷新率。
* 刷新率：在泳道范围内查找关键词H:RSHardwareThread::CommitAndReleaseLayers rate，如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/QYGIGKoIRJ2I-iNwPRExmg/zh-cn_image_0000002530753064.png?HW-CC-KV=V1&HW-CC-Date=20260427T235705Z&HW-CC-Expire=86400&HW-CC-Sign=BC7C7017A27F0AE005819E683F30994214106E252117008530FD9723EA80E148)

* 每帧渲染实际耗时(ms)：【下一个H:Waiting for Present Fence xxxx的起始时间】 - 【当前H:Waiting for Present Fence xxxx的起始时间】如下图 【标记2 - 标记1】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/W8vD50eCSyaKfNmYlHqQPw/zh-cn_image_0000002561832985.png?HW-CC-KV=V1&HW-CC-Date=20260427T235705Z&HW-CC-Expire=86400&HW-CC-Sign=52D3904092D37D206905591E1FCCDD47EC40CC131C88F54A9AE242854E147E07)

* 每帧丢帧时间(ms)：max（【每帧渲染实际耗时(ms)】- 【每帧时长(ms)】 \* 1.5, 0）；即每帧耗时大于标准耗时1.5倍时则判定为丢帧。

## 计算逻辑

卡顿率=所有【每帧丢帧时间(ms)】/ 总时长(s)，卡顿率小于等于0ms/s。
