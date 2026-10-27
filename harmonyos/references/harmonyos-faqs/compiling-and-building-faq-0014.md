---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0014
title: 编译构建密钥库密码错误问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > 编译构建密钥库密码错误问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:51+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:eb27c7cb52ad386d84aaa8b07e09b2af30ed52ea4d6376a0eb7f45c4d2890512
---

**Q：编译报错“keystore password was incorrect”？**

**A**：问题现象：编译时出现错误，提示“ERROR - hap-sign-tool: error: ACCESS\_ERROR, code: 109. Details: Init keystore failed: keystore password was incorrect”。请检查密钥库密码是否正确。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/AGxLrXA8TvuYG-PlmTRVDQ/zh-cn_image_0000002771935442.png "点击放大")

报错原因：密钥库(p12)的密码错误。签名文件中的签名密码错误导致该问题出现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/oL-JPmc7TYGJseXhJiMgAQ/zh-cn_image_0000002772095400.png "点击放大")

**须知** 

密钥库密码和密钥密码在创建p12文件时由开发者输入，请牢记这些密码。build-profile.json5文件中记录了密码的密文，但签名工具需要输入密码明文，不能直接使用build-profile.json5中的值。

常见场景：

1. 密码输入错误。
2. 在命令行中输入了密文。
3. 密钥（keyAlias）密码和密钥库（p12）密码混淆。

解决措施：重新自动签名可以解决该问题。

1. 点击**File > Project Structure > Project > Signing Configs**，打开签名配置页面。
2. 勾选“Automatically generate signing”（如果是HarmonyOS工程，还需勾选“Support HarmonyOS”），等待重新签名，点击**OK**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/kpGnP5d6Q9KZZPFDiz2Yxw/zh-cn_image_0000002801215679.png "点击放大")
