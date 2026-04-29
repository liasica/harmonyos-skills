---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smooth-for-transition-0414
title: 转场操作流畅
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 转场操作流畅
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f35694c4b3a3acf59fd92cbbbf119e2641b54a253edfc1fdc691158575a2e7e6
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/1nfcuIf4ShuUwtqFFW2Fig/zh-cn_image_0000002561832987.png?HW-CC-KV=V1&HW-CC-Date=20260429T054704Z&HW-CC-Expire=86400&HW-CC-Sign=709C23FCFFD3D4882AD694DC1DC28994AA543D9148D605D56EC8882CF396E93C)

* 总时长(s)：【最后一个“H:Waiting for Present Fence xxxx” 时间（如图标记2）】 - 【第一个“H:Waiting for Present Fence xxxx” 时间（如图标记1）】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/nmg6GEzzRYiuElQHC1nytQ/zh-cn_image_0000002561832979.png?HW-CC-KV=V1&HW-CC-Date=20260429T054704Z&HW-CC-Expire=86400&HW-CC-Sign=9F2CA05126495DAB8ED1B7C8135C9EEEE2F5DBE48EA27D7DBF319EBD7BC221F7)

* 每帧时长(ms)：1000ms / 刷新率。
* 刷新率：在泳道范围内查找关键词H:RSHardwareThread::CommitAndReleaseLayers rate，如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/_9YC7cOiTtG1nXVrVWoTvg/zh-cn_image_0000002530753064.png?HW-CC-KV=V1&HW-CC-Date=20260429T054704Z&HW-CC-Expire=86400&HW-CC-Sign=D8F2D967AF2DC599C52E708F8444B73694679939D52E8669B2AD2872480EBEBA)

* 每帧渲染实际耗时(ms)：【下一个H:Waiting for Present Fence xxxx的起始时间】 - 【当前H:Waiting for Present Fence xxxx的起始时间】如下图 【标记2 - 标记1】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/yddfByB5RwOyOmCLiVS9vw/zh-cn_image_0000002561832985.png?HW-CC-KV=V1&HW-CC-Date=20260429T054704Z&HW-CC-Expire=86400&HW-CC-Sign=1E88592279AC6CFBC376F2A7994049B913B9A7B58C4173898311A683FA0EE37D)

* 每帧丢帧时间(ms)：max（【每帧渲染实际耗时(ms)】- 【每帧时长(ms)】 \* 1.5, 0）；即每帧耗时大于标准耗时1.5倍时则判定为丢帧。

## 计算逻辑

卡顿率=所有【每帧丢帧时间(ms)】/ 总时长(s)，卡顿率小于等于0ms/s。
