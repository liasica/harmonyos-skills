---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-21
title: 如何在ArkTS侧引用其他三方so库
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在ArkTS侧引用其他三方so库
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a9522209f5ffb0bb867217b7d199f5c2732366331d732e136b420ddd758ae00c
---

**解决措施**

在ArkTS中引用三方库so需要具备以下三个文件：xxx.so、Index.d.ts和oh-package.json5。其中，Index.d.ts和oh-package.json5在C++模板中自带，也可以手动创建。在需要调用的模块根目录下的oh-package.json5中声明so库的根目录路径。然后在代码中使用import语句引用oh-package.json5中声明的依赖名称。此方案仅适用于已经适配了Native的so库。因此，在编译生成so库时，需要实现功能函数并注册其Native侧接口，同时提供对应的Native侧接口声明文件Index.d.ts和配置文件oh-package.json5。

1. 将so文件移动到libs文件夹下对应架构的目录。如果在纯ArkTS工程中，还需将编译三方库时生成的libc++\\_xxx.so移动到该目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/xF2DoqUGRmOqYT0Nt_TC9Q/zh-cn_image_0000002194318516.png?HW-CC-KV=V1&HW-CC-Date=20260428T002431Z&HW-CC-Expire=86400&HW-CC-Sign=915D0286C4F9CA000994044BAF7168C2FDAA4EC03277F7E6354628E4A2F56949 "点击放大")
2. 在src/main/cpp/types目录下创建新目录，并将Index.d.ts和oh-package.json5文件移动到该目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/zApv2AXWR0CeIpUZ5OmM-g/zh-cn_image_0000002229604289.png?HW-CC-KV=V1&HW-CC-Date=20260428T002431Z&HW-CC-Expire=86400&HW-CC-Sign=318E420B227875D0A1D9EF0AB995D33CA72557515822454CFA368798EB9BA4D2 "点击放大")
3. 在模块级的oh-package.json5文件中声明该 so 库的根目录路径。

   ```
   1. "dependencies": {
   2. "libimportthirdpartylibraries.so": "file:./src/main/cpp/types/libimportthirdpartylibraries",
   3. "libapplication.so": "file:./src/main/cpp/types/libapplication"
   4. },
   ```

   [oh-package.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/ImportThirdPartyLibraries/oh-package.json5#L12-L15)
4. 在代码中引用并调用oh-package.json5中声明的依赖。

   ```
   1. import testNapi from 'libimportthirdpartylibraries.so';
   2. import myNapi from 'libapplication.so';

   4. @Entry
   5. @Component
   6. struct Index {
   7. @State message: string = 'Hello World';

   9. build() {
   10. Row() {
   11. Column() {
   12. Text(this.message)
   13. .fontSize(50)
   14. .fontWeight(FontWeight.Bold)
   15. .onClick(() => {
   16. console.info(`MyTest NAPI 2 + 3 = ${myNapi.add(2, 3)}`);
   17. console.info(`MyTest NAPI 2 - 3 = ${testNapi.sub(2, 3)}`);
   18. })
   19. }
   20. .width('100%')
   21. }
   22. .height('100%')
   23. }
   24. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/ImportThirdPartyLibraries/src/main/ets/pages/Index.ets#L19-L42)

运行结果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/3VvAKFIGRWWgnvrhW9rMnw/zh-cn_image_0000002229758785.png?HW-CC-KV=V1&HW-CC-Date=20260428T002431Z&HW-CC-Expire=86400&HW-CC-Sign=9E6068269B6E759A1D49EAAA7CCC6D398B1B2A32713EFEB85DE1BE3FFD0BA9CB "点击放大")

**参考链接**

[在ArkTS侧引用三方so库](../best-practices/bpta-dynamic-link-library.md#section166546365376)
