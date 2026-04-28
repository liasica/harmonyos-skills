---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/description-of-personal-data
title: 鲸鸿动能Ads Kit个人数据处理说明
breadcrumb: 指南 > 应用服务 > Ads Kit（广告服务） > 鲸鸿动能Ads Kit个人数据处理说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d6262183091c37a8effae6ac5498eb6e6406e673aca53e98166fa48430058107
---

此文档针对华为作为最终用户数据控制者，对用户的数据处理进行说明，包括：

* 华为处理的个人数据清单
* 指导用户行使数据主体权利

## **华为处理的个人数据清单**

鲸鸿动能Ads Kit处理的个人数据清单和存储期限如下：

| **个人数据清单** | **使用目的** | **存留期** |
| --- | --- | --- |
| 设备标识符、OAID、设备型号、设备硬件信息、操作系统、设备状态信息、系统设置信息、应用基本信息、应用使用信息、磁力计、加速度传感器、传感器信息、陀螺仪、网络信息、运营商信息、IP地址或IP归属地、WLAN信息（WiFi参数、WiFi状态）、BSSID、SSID、华为其他相关应用的数据、华为账号信息、举报内容、**联系方式（邮箱或手机号码）**、举证材料（图片或视频）、年龄、性别、个人偏好、应用设置信息、搜索记录、订阅信息、交易记录 | 用于向您提供广告服务、帮助识别和防范广告中的欺诈及其它恶意行为，以及广告转化行为的归因、用于本应用和华为其他应用中保障产品的稳定运行、根据法律法规的要求保障网络安全、完成统计结算、改善产品的运营策略、为您处理投诉举报请求、用于向您提供个性化广告。 | 保存至留存期到期，如涉及个性化推荐、个性化广告、营销、问题和建议、帮助和反馈、投诉举报，其相关个人信息通常保存不超过2年。如涉及产品运营与维护，其相关个人信息通常保存不超过5年。 |

## **指导用户行使数据主体权利**

### **隐私政策披露鲸鸿动能Ads Kit处理的个人信息**

在您接入、使用鲸鸿动能Ads Kit服务前，**我们要求您在隐私政策中向用户告知我们是如何处理其个人数据的，并获取用户同意或取得其他合法性基础**。您可以在隐私声明中显示链接，方便用户查阅当您使用鲸鸿动能广告平台的服务时，[鲸鸿动能广告平台如何使用相关数据](https://legal.cloud.huawei.com.cn/terms/scope/huawei/ads-hmos/privacy-statement.htm?&code=CN&language=zh-CN&branchid=0&contenttag=default)。

用户可参考[关于鲸鸿动能广告与隐私的声明](https://legal.cloud.huawei.com.cn/terms/scope/huawei/ads-hmos/privacy-statement.htm?&code=CN&language=zh-CN&branchid=0&contenttag=default)中的说明行使数据主体权利。如果用户对自己的数据主体权利有进一步要求或存在任何疑问、意见或建议，可通过鲸鸿动能广告隐私声明中的“如何联系我们”章节中所描述的方式与我们取得联系，我们会尽快答复并支持用户行使其相关权利。

### **个性化广告推荐功能的配置说明**

我们的鲸鸿动能Ads Kit针对个性化广告推荐的功能提供了配置能力，您可以基于业务诉求选择开启或关闭相关功能。

您可以通过请求参数设置接口[AdOptions.nonPersonalizedAd](../harmonyos-references/js-apis-advertising.md#adoptions)配置开启或关闭个性化广告，若关闭个性化广告，则正常返回非个性化广告。关闭个性化广告后，用户接收到的广告数量可能不会减少，但广告相关性会降低。
