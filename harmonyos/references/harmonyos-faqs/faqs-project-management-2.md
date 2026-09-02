---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-2
title: 工程检查报错，提示“Incorrect settings found in the build-profile.json5 file”
breadcrumb: FAQ > DevEco Studio > 工程管理 > 工程检查报错，提示“Incorrect settings found in the build-profile.json5 file”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a5b23da8e4680c191128bbc749fc512d3eedcb5330510b42661e0de6b10ad17f
---

**解决措施**

1. 工程级build-profile.json5文件配置可能存在错误，请根据以下规范检查并修改配置。特别注意compatibleSdkVersion、targetSdkVersion和runtimeOS的位置和填写格式。

   ```json
   {
     "app": {
       "signingConfigs": [],
       "products": [
         {
           "name": "default",
           "signingConfig": "default",
           "compatibleSdkVersion": "4.0.0(10)", // Specify the minimum version compatible with HarmonyOS applications/services. The version number needs to be changed to "4.0.0 (10)", please use English carefully And ()
           "targetSdkVersion": "4.0.0(10)",     // Specify the target version for HarmonyOS applications/services. If not set, the default is compatibleSdkVersion
           "runtimeOS": "HarmonyOS",            // Designated as HarmonyOS/OpenHarmony
         }
       ],
       // ...
   }
   ```
2. 在工程级build-profile.json5的products下配置runtimeOS，请检查并删除模块级build-profile.json5文件中的runtimeOS字段。
