---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-19
title: 编译报错“keystore password was incorrect”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“keystore password was incorrect”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:99eaf00a0e81b39bcc84d9083b1fe083506a84cf42ff443266debc1d65178306
---

**问题现象**

编译时出现错误，提示“ERROR - hap-sign-tool: error: ACCESS\_ERROR, code: 109. Details: Init keystore failed: keystore password was incorrect”。请检查密钥库密码是否正确。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/sH8jQwunRw2wPhx1CiLfRA/zh-cn_image_0000002229603737.png?HW-CC-KV=V1&HW-CC-Date=20260428T002910Z&HW-CC-Expire=86400&HW-CC-Sign=70F09561DE8D987ED981F3F51C150D60F260E5EECD9F94621E6A8A18C879DDAA)

**报错原因**

密钥库(p12)的密码错误。签名文件中的签名密码错误导致该问题出现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/lBBDbGA4SAOZyKW0S0oe3A/zh-cn_image_0000002436501498.png?HW-CC-KV=V1&HW-CC-Date=20260428T002910Z&HW-CC-Expire=86400&HW-CC-Sign=D616FBBABB3375B2EDBBD0E22E9FC715D405A63E940B864EBC9444A6A02E7E20)

注意

密钥库密码和密钥密码在创建p12文件时由开发者输入，请牢记这些密码。build-profile.json5文件中记录了密码的密文，但签名工具需要输入密码明文，不能直接使用build-profile.json5中的值。

**常见场景**

1. 密码输入错误。
2. 在命令行中输入了密文。
3. 密钥（keyAlias）密码和密钥库（p12）密码混淆。

**解决措施**

重新自动签名可以解决该问题：

1. 点击**File > Project Structure > Project > Signing Configs**，打开签名配置页面。

2. 勾选“Automatically generate signing”（如果是HarmonyOS工程，还需勾选“Support HarmonyOS”），等待重新签名，点击**OK**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/P1uGdP1DRWeNY2tlYvP6Ow/zh-cn_image_0000002229758209.png?HW-CC-KV=V1&HW-CC-Date=20260428T002910Z&HW-CC-Expire=86400&HW-CC-Sign=B729358C0A6554BCDA209D3CD842C0BBBF41AC2D85BAD73BD5895E4CAF4F0813)
