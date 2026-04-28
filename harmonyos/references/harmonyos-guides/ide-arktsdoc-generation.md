---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-generation
title: 文档生成
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 生成ArkTSDoc文档 > 文档生成
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:939d83eb1932d13dd1884f83d77e91c338fdf1254805e81fa54899c9071fff9f
---

DevEco Studio支持通过Generate ArkTSDoc功能，将代码文件中变量、方法、接口、类等需要对外暴露的信息快速生成相应的参考文档。

从DevEco Studio 6.1.0 Beta1开始，ArkTSDoc功能支持多模块导出，以及导出时支持设置不需要被导出的目录。

说明

* 当前支持对工程或目录下.ets/.ts/.js/.md格式文件生成ArkTSDoc文档。
* 文件中export的变量、方法、接口、类等将生成相应的ArkTSDoc文档，未export的对象不支持生成。
* 若选择对工程/目录整体导出ArkTSDoc文档，生成后的ArkTSDoc文档目录和原目录结构一致。

## 生成步骤

1. 在菜单栏选择**Tools >** **Generate ArkTSDoc...**进入ArkTSDoc生成界面。
2. 设置生成ArkTSDoc的范围，可选择整个工程、单个模块或多个模块，某个目录或单个文件进行导出。

   点击**Modules**后的下拉箭头，会弹出所有模块，可以选择单个或多个模块作为导出范围。当模块数量较多时，可以使用检索功能，快速定位模块。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/okF5L7deQy-dpUTmieCyLg/zh-cn_image_0000002561833351.png?HW-CC-KV=V1&HW-CC-Date=20260427T235631Z&HW-CC-Expire=86400&HW-CC-Sign=2599C4A1AE2D262F77B3110BC951AA7A5A7C4C7BFB46D230B65ED849BD30D3F6)
3. 在导出时，可以在**Command line arguments**设置无需被导出的目录，使用"-e"子命令进行指定。多个目录使用英文";"分隔，使用"./"开头路径代表项目根路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/PaQwxHKYSHOe0c8uLimveQ/zh-cn_image_0000002530753438.png?HW-CC-KV=V1&HW-CC-Date=20260427T235631Z&HW-CC-Expire=86400&HW-CC-Sign=0A0AFA18B5DD8046B74FECC8289B5E5F1572E89FFC3D747135496E092F7E28B9)
4. 在**Output directory**中输入导出ArkTSDoc的存储路径后，点击**Generate**。
5. 若勾选**Open generated documentation in browser**选项，在生成ArkTSDoc后，将自动打开相应页面查看生成的文档。配置完毕后点击Generate，开始扫描并生成ArkTSDoc文档。

   生成的ArkTSDoc左侧文档目录和原工程目录结构一致，右侧可点击跳转到当前文件包含的某个变量、方法、接口或类的文档位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/J_OSh4WbSoi6rQm6q7rUAA/zh-cn_image_0000002561753369.png?HW-CC-KV=V1&HW-CC-Date=20260427T235631Z&HW-CC-Expire=86400&HW-CC-Sign=2DC787CFC7E6BB1448EA31E681949B340866D7FE263FBE7E6A5F88F7E7AE9844 "点击放大")

   若没有勾选**Open generated documentation in browser**选项，在生成ArkTSDoc后，DevEco Studio右下角弹出对应提示框，可以点击Go to Folder跳转到生成的ArkTSDoc文件夹，用浏览器打开文件夹中index.html文件即可查看ArkTSDoc文档。

## 生成效果示例

**注释格式要求：**当前仅支持“/\*\* \*/”文档注释格式；支持param等[标准标签](ide-arktsdocs-standard-label.md)和myTag等自定义标签生成相应文档。

```
1. /**
2. * Prints "log" logs.
3. *
4. * @param { string } message - Text to print.
5. * @myTag
6. * @since 11
7. */
```

**代码示例：**

```
1. /**
2. * Defines the demo class
3. *
4. * @since 11
5. */
6. export class Demo {
7. /**
8. * Prints "log" logs.
9. *
10. * @param { string } message - Text to print.
11. * @myTag
12. * @since 11
13. */
14. static log(message: string): void {

16. }
17. }
```

**ArkTSDoc文档生成结果：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/MFdTzCmnQa6EcR6TVcULWg/zh-cn_image_0000002530753436.png?HW-CC-KV=V1&HW-CC-Date=20260427T235631Z&HW-CC-Expire=86400&HW-CC-Sign=BF50C9594C270AED69D1690E2FFB23D28315F8F3F4F25B8B566FEB4C4B3436AA "点击放大")
