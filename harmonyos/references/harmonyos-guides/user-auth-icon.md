---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-auth-icon
title: 使用嵌入式用户身份认证控件
breadcrumb: 指南 > 系统 > 安全 > User Authentication Kit（用户认证服务） > 使用嵌入式用户身份认证控件
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:34+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:99e7f1b770cd6d59968cb64bd4c9397a5c7d5d556d3ac9778d3b0ebb89d6d52c
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/Gt0IiCgPQUSnsE-4Y7-ixA/zh-cn_image_0000002817506869.png?HW-CC-KV=V1&HW-CC-Date=20261114T004733Z&HW-CC-Expire=31536000000&HW-CC-Sign=74525EDFD6C23BA92361CD1B6B20F48E1B7C5BF1C2A915446A6AEFA176E0C5CA)

## 示例

具体参数、使用方式等信息，请参考对应的[@ohos.userIAM.userAuthIcon (嵌入式用户身份认证控件)](../harmonyos-references/ohos-useriam-userauthicon.md)。
