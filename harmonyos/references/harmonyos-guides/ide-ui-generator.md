---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-generator
title: 应用UI生成
breadcrumb: 指南 > 使用AI智能辅助编程 > 应用UI生成
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:14+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:2b5b69c59f3e3c65a52c15f9750bbbfb01a601491f518cc074d2597e372771e4
---

UI Generator用于快速生成可编译、可运行的HarmonyOS UI工程，支持基于已有UI布局文件（XML），快速生成对应的HarmonyOS UI代码，其中包含HarmonyOS基础工程、页面布局、组件及属性和资源文件等。

## 使用约束

建议使用DevEco Studio 5.0.3.700及以上版本。

## 启用插件

1. 在DevEco Studio菜单栏，点击**File > Setting****s...**（macOS为**DevEco Studio > Preferences****/Settings**）**> Plugins**，在Installed列表中找到UI Generator插件，点击**Enable**启用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/tEhHegTCRDuU2MNgKkWJ7Q/zh-cn_image_0000002530913614.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=9485BDDA74EC64000A83C1008679E06491653E280F55D355BD51509475F6B79E)
2. 单击OK并关闭设置窗口，插件启用成功。

## 开始使用

1. 在DevEco Studio菜单栏点击**Tools > Generate Project From...**打开UI Generator工具，首次使用需要阅读并确认用户协议，确认后可继续使用。
2. 输入待配置项路径，点击**Next**进入下一步。

   | 待配置项 | 说明 |
   | --- | --- |
   | Installation package path | 待转换的APK应用包的路径，请提供未混淆的Debug版本应用包。 |
   | SDK path | 等于或高于编译应用包所使用版本的SDK路径。 |
   | Git Bash path | Git Bash工具存放路径。若本地已下载安装Git Bash，插件将自动获取其路径。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/tfdvdknvQBGvQb94IevWjg/zh-cn_image_0000002561833533.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=62A07284057DBD41F3A8ADBB40BE14C6D7B3CA0303BE276B71758874B731986F)
3. 选择将要生成的XML页面（可在搜索框进行搜索），勾选后点击向右箭头将选中的XML导入至右侧。点击**Next**开始生成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/qUBohwdvQ-aPsL4lzku3FQ/zh-cn_image_0000002530753612.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=EB80DC721BEA421FA9D8C5DE33A5085E5E0115C6DDB99D6B6331EDCF9CA7F73E)
4. 配置输出工程待配置项，点击**Finish**进行生成。

   | 待配置项 | 说明 |
   | --- | --- |
   | Destination Path | 生成新工程的保存路径（默认生成到用户目录下UIGenerationProjects，用户可根据需要自行更改） |
   | Compatible SDK | 生成的新工程所使用的SDK版本 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/ImBGhRMFRX6s_viLhT8xtw/zh-cn_image_0000002561833541.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=BD3481D01D9DDC226B1CBB9D566378D701E9EA17A1CC2E6CCF7D59A2AC3C84C7)
5. （可选）如果所选XML无有效根节点，需要选择根节点信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/E6_FJXkAQ2WVs2s911LSPg/zh-cn_image_0000002561833535.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=56FAF5D7D719C5D709ADC31DE893E059EC705997C7839E6C11F3A5A73C6DB55E)
6. 点击**Finish**，在弹窗中点击确认，打开新工程。

   生成的页面位于entry > src > main > ets > pages目录下，可以点击Previewer查看页面预览效果。不支持生成的组件、属性会以注释的形式给出，方便后续定位修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/raA46enYSfWU-LCJ8MdQZw/zh-cn_image_0000002561833543.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=A82C20CD9C85AABC482E8A520D0B4FEA96124AA69BB99CC5117FEB25BCEFFE47)
7. 生成的新工程内的entry > src > main > resources目录包含文本、图像、颜色资源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/mF6wL7QORgCK2V-P0y_PiQ/zh-cn_image_0000002561753559.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=B8EA1742B57D7B28CC2235958803C691672969D091A415F6700CE02AF0F45B79 "点击放大")

   更多操作指导，请参考视频课程：[毕方HarmonyOS UI代码生成工具](https://developer.huawei.com/consumer/cn/training/course/live/C101731322888995220)。
