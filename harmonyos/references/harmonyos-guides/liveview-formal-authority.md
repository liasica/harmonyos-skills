---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-formal-authority
title: 申请实况窗正式权限
breadcrumb: 指南 > 应用服务 > Live View Kit（实况窗服务） > 开发准备 > 申请实况窗正式权限
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:22+08:00
doc_updated_at: 2026-10-30
content_hash: sha256:c0b187b8b73a07c1f672bc1e6c48137afd8d6fc9c90541a568d5d5a02312d8f8
---

当开发者已对调测设备的实况窗业务进行了充分的[联调测试](liveview-joint-commission-test.md)，确认设计方案和功能体验均符合[《实况窗设计规范》](liveview-design-formula.md)，可提交申请正式权限。提交后实况窗将对开发者的方案设计、功能体验进行评审与验收。开发者将会在7个工作日内收到评审结果。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/4h3tS4KyQuaMr0nPfxXmNg/zh-cn_image_0000002788468046.png?HW-CC-KV=V1&HW-CC-Date=20261114T004822Z&HW-CC-Expire=31536000000&HW-CC-Sign=06DB082F4B7F3F1E194CD5DF9E86CBF6BA46BC726D1C7C4ABDDB1FAA3A866E5C)
2. 在项目列表中找到需要开通实况窗的项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/upb_LTxATAu0YfPomIb_FA/zh-cn_image_0000002817507535.png?HW-CC-KV=V1&HW-CC-Date=20261114T004822Z&HW-CC-Expire=31536000000&HW-CC-Sign=795AC9F0DCD55060A281B453EDB0A2D34386558028CCA39DB96181F151FCC31F)
3. 通过“增长 > 推送服务 > 配置”导航到“配置”页签，选择需要开通实况窗的应用，并点击“实况窗”的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/2DPh3KqcRkO32eNDkgdbrw/zh-cn_image_0000002817427471.png?HW-CC-KV=V1&HW-CC-Date=20261114T004822Z&HW-CC-Expire=31536000000&HW-CC-Sign=367F5E1581BEB246216EE20630A67BA5907A0FE8268B70E47CFDFA1D04FEB2D8)
4. 开发者可点击开通实况窗权限，进入实况窗介绍页面，点击“立即申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/s9ZApKfkRVy00c7gjkeIdg/zh-cn_image_0000002788468052.png?HW-CC-KV=V1&HW-CC-Date=20261114T004822Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF36BE3FC3554EB12560A41115FB68E983C02C15E6869F4E4CB78D328647C35E)
5. 点击“立即申请”后进入实况窗页面。可点击“应用场景”列表中各场景的“申请”按钮，按需申请开通实况窗权益。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/aqacac1HTCCsgkMmpIHdtA/zh-cn_image_0000002817507541.png?HW-CC-KV=V1&HW-CC-Date=20261114T004822Z&HW-CC-Expire=31536000000&HW-CC-Sign=50522F110F43AFDFA7847AB3BD8AC074D267BD9C874021A8628B2921A1D0CE84)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/iD3GZhAgTWmwb_W8HIoKrQ/zh-cn_image_0000002788308110.png?HW-CC-KV=V1&HW-CC-Date=20261114T004822Z&HW-CC-Expire=31536000000&HW-CC-Sign=2FD906F1C37B471EB8CF2330882C1A2519482FFDA9948369FB91CF9D8D29B28E)
6. 按要求填写场景的描述信息、场景接入方案和备注信息后提交申请，等待审批结果即可。可参见[实况窗权益申请填写要求](liveview-formal-authority.md#实况窗权益申请填写要求)进行申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/_tpuSpWQSzSrQUhM7VXtjw/zh-cn_image_0000002817427473.png?HW-CC-KV=V1&HW-CC-Date=20261114T004822Z&HW-CC-Expire=31536000000&HW-CC-Sign=53529EE384B1AB8A65E3CED0A627B69103E39563F5A3F5EAC0D187A7D8EDE318)

## 实况窗权益申请填写要求

### 场景描述

需包含：接入场景的描述、消息的展示时机基本说明、展示的主要节点。开发者填写的内容将用于客服答疑等场景，请尽可能详细地描述。

示例：

```
以打车场景接入为例，场景描述可按照如下字段描述提交
接入场景：用户打车后，通过实况窗通知展示接驾进展、行程进展等信息
展示时机：用户提交即时出行订单后，或预约订单开始前30分钟
展示节点：呼叫司机、司机赶来、司机到达上车点、前往目的地、到达目的地-待支付、到达目的地-已支付
```

**须知** 

若开发者的应用内支持使用其他应用的小程序，需明确说明本次申请的场景使用范围是否涉及到其他应用的小程序。若涉及，开发者需确保不会出现同一个任务多端推送实况窗的体验，在提交申请时需在附件中一并附上如下内容：

* 与小程序客户端的沟通对齐证明。需双方明确客户端对开发者应用内其小程序产生的任务的处理方式，如客户端不会对开发者应用内其小程序产生的任务进行实况窗通知等。
* 策略变更预案。若小程序客户端策略发生变更，针对继续保持上述体验的应对策略预案。

沟通证明和预案需按场景和小程序一对一制定。后续在该场景下若涉及新增其他小程序，需线下提交针对新增小程序的沟通对齐证明和对应预案。

### 接入方案

请将应用已验收通过的接入方案现网效果截图（含每个状态节点的卡片、胶囊、锁屏效果、展示时机说明）、主要特殊场景方案效果放在同一张图片中，图片大小需控制在3M内。

示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/wWWNotMyT1KTysXpwf6L7A/zh-cn_image_0000002788468054.png?HW-CC-KV=V1&HW-CC-Date=20261114T004822Z&HW-CC-Expire=31536000000&HW-CC-Sign=8E03EEACDB268A502B0FB7D6F7571165354C8304BF16095A8A0973A02BB78FB3)

实况窗接入方案请需满足《实况窗设计规范》中的要求，开发者可按照模板进行设计。

**申请前自验**

应用在申请实况窗权限时，需对应用当前实况窗的效果和体验进行自检验收，并在申请时将自检项结果通过备注说明，如某项内容已完成自检，可在“[ ]”中打√

* [ ]确认上传的截图满足实况窗设计规范要求。
* [ ]每个创建的实况窗活动均已添加结束事件。
* [ ]确认实况窗与应用内任务进度与信息一致。
* [ ]确认同一实时任务不存在多个实况窗。
* [ ]确认已考虑并提供主要特殊场景的方案。
* [ ]已经完成实况窗场景测试，满足上线要求。
* [ ]认可实况窗的管理规范，若出现不符合设计规范或者违背场景准入要求，同意华为对相关场景[场景名称]权限进行收回。

**须知** 

开通正式权益涉及方案评审与测试验收，方案评审阶段通过后，须开发者配合测试验收（如提供验收方式和验收版本）。整个流程周期约15个工作日，请留意[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台申请结果或邮箱。
