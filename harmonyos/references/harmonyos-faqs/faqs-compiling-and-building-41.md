---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-41
title: 编译时DevEco Studio报错App Launch: To run and debug the Harmony device, configure the HarmonyOS runtime
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译时DevEco Studio报错App Launch: To run and debug the Harmony device, configure the HarmonyOS runtime
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:68d9a8368f8d00a0235674c6dda9fde876aae1edf7b3be57dfa25acbe774909d
---

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/sG9UYE1gSvelFqXDRthy7Q/zh-cn_image_0000002229604181.png?HW-CC-KV=V1&HW-CC-Date=20260429T062028Z&HW-CC-Expire=86400&HW-CC-Sign=FAD4592AD39F35706365EA63E09881D6A5BBBD5B447124898F23F0BE31E17B38)

**解决措施**

修改build-profile.json5文件，登录个人华为账号，然后重新签名。

1. 将根目录下的build-profile.json5文件里的 "runtimeOS": "OpenHarmony" 改成 "runtimeOS": "HarmonyOS"；
2. 点击 File > Project Structure > Signing Configs 进行签名配置；
3. 勾选“Support HarmonyOS（支持HarmonyOS）”和“Automatically generate signature（自动签名）”；
4. 点击“Sign In”按钮；
5. 登录华为账号，按提示在弹出的登录页面输入手机号并使用验证码登录。
