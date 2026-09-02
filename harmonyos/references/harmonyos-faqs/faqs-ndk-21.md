---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-21
title: 如何在ArkTS侧引用其他三方so库
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在ArkTS侧引用其他三方so库
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:3815e83d9d05db2281d496d5492cae24e0b17b5bf71be40b9d5392fd01af2376
---

**解决措施**

在ArkTS中引用三方库so需要具备以下三个文件：xxx.so、Index.d.ts和oh-package.json5。其中，Index.d.ts和oh-package.json5在C++模板中自带，也可以手动创建。在需要调用的模块根目录下的oh-package.json5中声明so库的根目录路径。然后在代码中使用import语句引用oh-package.json5中声明的依赖名称。此方案仅适用于已经适配了Native的so库。因此，在编译生成so库时，需要实现功能函数并注册其Native侧接口，同时提供对应的Native侧接口声明文件Index.d.ts和配置文件oh-package.json5。

1. 将so文件移动到libs文件夹下对应架构的目录。如果在纯ArkTS工程中，还需将编译三方库时生成的libc++\\_xxx.so移动到该目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/Twi1AxOwROqrRIC-YRfYbg/zh-cn_image_0000002654835197.png "点击放大")
2. 在src/main/cpp/types目录下创建新目录，并将Index.d.ts和oh-package.json5文件移动到该目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/kl9vhsZsS92HUSmSWv5hpA/zh-cn_image_0000002654795263.png "点击放大")
3. 在模块级的oh-package.json5文件中声明该 so 库的根目录路径。

   ```json
   "dependencies": {
     "libimportthirdpartylibraries.so": "file:./src/main/cpp/types/libimportthirdpartylibraries",
     "libapplication.so": "file:./src/main/cpp/types/libapplication"
   },
   ```
4. 在代码中引用并调用oh-package.json5中声明的依赖。

   ```ts
   import testNapi from 'libimportthirdpartylibraries.so';
   import myNapi from 'libapplication.so';

   @Entry
   @Component
   struct Index {
     @State message: string = 'Hello World';

     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               console.info(`MyTest NAPI 2 + 3 = ${myNapi.add(2, 3)}`);
               console.info(`MyTest NAPI 2 - 3 = ${testNapi.sub(2, 3)}`);
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

运行结果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/ltB8_JZnQzy0LW9bENxnwQ/zh-cn_image_0000002624635798.png "点击放大")

**参考链接**

[在ArkTS侧引用三方so库](../harmonyos-guides/integrate-third-party-dlls.md#在arkts侧引用三方so库)
