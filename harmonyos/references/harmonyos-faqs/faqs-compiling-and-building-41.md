---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-41
title: 编译时DevEco Studio报错App Launch: To run and debug the Harmony device, configure the HarmonyOS runtime
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译时DevEco Studio报错App Launch: To run and debug the Harmony device, configure the HarmonyOS runtime
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:727f1688c958257abded7307e94440e55f1b8d79537803dbf797201229b3f250
---

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/sG9UYE1gSvelFqXDRthy7Q/zh-cn_image_0000002229604181.png?HW-CC-KV=V1&HW-CC-Date=20260428T002915Z&HW-CC-Expire=86400&HW-CC-Sign=9BED88B8549AF9539D470A72F26668DF0F682A829A501D1B313F1337EDF7FEAC)

**解决措施**

修改build-profile.json5文件，登录个人华为账号，然后重新签名。

1. 将根目录下的build-profile.json5文件里的 "runtimeOS": "OpenHarmony" 改成 "runtimeOS": "HarmonyOS"；
2. 点击 File > Project Structure > Signing Configs 进行签名配置；
3. 勾选“Support HarmonyOS（支持HarmonyOS）”和“Automatically generate signature（自动签名）”；
4. 点击“Sign In”按钮；
5. 登录华为账号，按提示在弹出的登录页面输入手机号并使用验证码登录。
