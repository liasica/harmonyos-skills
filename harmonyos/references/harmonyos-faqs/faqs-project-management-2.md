---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-2
title: 工程检查报错，提示“Incorrect settings found in the build-profile.json5 file”
breadcrumb: FAQ > DevEco Studio > 工程管理 > 工程检查报错，提示“Incorrect settings found in the build-profile.json5 file”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c1e8ba9b044617eddbbbf01d2497963a247ade2fd297ca7d2d865decb55ac900
---

**解决措施**

1. 工程级build-profile.json5文件配置可能存在错误，请根据以下规范检查并修改配置。特别注意compatibleSdkVersion、targetSdkVersion和runtimeOS的位置和填写格式。

   ```
   1. {
   2. "app": {
   3. "signingConfigs": [],
   4. "products": [
   5. {
   6. "name": "default",
   7. "signingConfig": "default",
   8. "compatibleSdkVersion": "4.0.0(10)", //Specify the minimum version compatible with HarmonyOS applications/services. The version number needs to be changed to "4.0.0 (10)", please use English carefully And ()
   9. "targetSdkVersion": "4.0.0(10)",     //Specify the target version for HarmonyOS applications/services. If not set, the default is compatibleSdkVersion
   10. "runtimeOS": "HarmonyOS",            //Designated as HarmonyOS/OpenHarmony
   11. }
   12. ],
   13. // ...
   14. }
   ```

   [build-profile.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ProjectManagement/build-profile.json5#L4-L41)
2. 在工程级build-profile.json5的products下配置runtimeOS，请检查并删除模块级build-profile.json5文件中的runtimeOS字段。
