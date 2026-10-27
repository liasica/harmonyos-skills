---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-41
title: "编译时DevEco Studio报错App Launch: To run and debug the Harmony device, configure the HarmonyOS runtime"
breadcrumb: "FAQ > DevEco Studio > 编译构建 > 编译时DevEco Studio报错App Launch: To run and debug the Harmony device, configure the HarmonyOS runtime"
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:53+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:9123cc468591a1765eb9582ea3b391d9950d64e122386fe4845b50e96b20cc79
---

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/dIKuH-4iSpqWEHX0_XW0Ow/zh-cn_image_0000002624478510.png)

**解决措施**

修改build-profile.json5文件，登录个人华为账号，然后重新签名。

1. 将根目录下的build-profile.json5文件里的 "runtimeOS": "OpenHarmony" 改成 "runtimeOS": "HarmonyOS"；
2. 点击 File > Project Structure > Signing Configs 进行签名配置；
3. 勾选“Support HarmonyOS（支持HarmonyOS）”和“Automatically generate signature（自动签名）”；
4. 点击“Sign In”按钮；
5. 登录华为账号，按提示在弹出的登录页面输入手机号并使用验证码登录。
