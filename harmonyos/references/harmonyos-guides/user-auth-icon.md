---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-auth-icon
title: 使用嵌入式用户身份认证控件
breadcrumb: 指南 > 系统 > 安全 > User Authentication Kit（用户认证服务） > 用户身份认证开发指导 > 使用嵌入式用户身份认证控件
category: harmonyos-guides
scraped_at: 2026-04-29T13:32:26+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:65b0bde3e9b3676a173d47398c98a532c57562f99445705d70b0ac6134c2dffb
---

提供应用界面上展示的人脸、指纹认证图标，功能包括：

1. 提供嵌入式人脸、指纹认证控件图标，应用可集成。
2. 支持自定义图片的颜色和大小，其余样式元素不可变更。
3. 点击控件图标后可拉起系统弹窗式人脸、指纹认证控件。

当前支持使用认证控件的认证类型包括：

* 人脸认证
* 指纹认证
* 人脸+锁屏口令认证
* 指纹+锁屏口令认证
* 人脸+指纹+锁屏口令认证

以指纹认证为例，控件使用效果如图所示。应用集成嵌入式用户身份认证控件后，用户点击左图中的指纹图标（即嵌入式用户身份认证控件），系统将自动拉起右图中的系统身份认证控件，完成身份认证。开发者无需通过接口发起身份认证请求，简化了认证流程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/RwIp2Y3aSqmSvJ1fikI5vg/zh-cn_image_0000002589324785.png)

## 示例

具体参数、使用方式等信息，请参考对应的[@ohos.userIAM.userAuthIcon (嵌入式用户身份认证控件)](../harmonyos-references/ohos-useriam-userauthicon.md)。
