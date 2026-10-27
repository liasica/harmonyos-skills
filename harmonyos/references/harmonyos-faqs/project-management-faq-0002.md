---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/project-management-faq-0002
title: build-profile.json5工程检查报错问题排查
breadcrumb: FAQ > DevEco Studio > 工程管理 > 常见问题 > build-profile.json5工程检查报错问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:49+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:d94059d4a571e30d58d02bebf7d413e0ab075579dd7e6ac71f13de912e22e344
---

**Q：工程检查报错，提示“Incorrect settings found in the build-profile.json5 file”。**

**A**：解决措施如下：

1. 工程级build-profile.json5文件配置可能存在错误，请根据以下规范检查并修改配置。特别注意compatibleSdkVersion、targetSdkVersion和runtimeOS的位置和填写格式。

   ```json
       {
         "app": {
           "signingConfigs": [],
           "products": [
             {
               "name": "default",
               "signingConfig": "default",
               "compatibleSdkVersion": "5.0.0(12)", // Specify the minimum version compatible with HarmonyOS applications/services. The version number needs to be changed to "5.0.0 (12)", please use English carefully And ()
               "targetSdkVersion": "5.0.0(12)",     // Specify the target version for HarmonyOS applications/services. If not set, the default is compatibleSdkVersion
               "runtimeOS": "HarmonyOS",            // Designated as HarmonyOS/OpenHarmony
             }
           ],
           // ...
       }
   ```
2. 在工程级build-profile.json5的products下配置runtimeOS，请检查并删除模块级build-profile.json5文件中的runtimeOS字段。
