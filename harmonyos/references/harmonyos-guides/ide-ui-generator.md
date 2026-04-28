---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-generator
title: 应用UI生成
breadcrumb: 指南 > 使用AI智能辅助编程 > 应用UI生成
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:16+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:74e02eea2329453e90985999e9863baa771c26d844a0853a886b9592ac7fbf52
---

UI Generator用于快速生成可编译、可运行的HarmonyOS UI工程，支持基于已有UI布局文件（XML），快速生成对应的HarmonyOS UI代码，其中包含HarmonyOS基础工程、页面布局、组件及属性和资源文件等。

## 使用约束

建议使用DevEco Studio 5.0.3.700及以上版本。

## 启用插件

1. 在DevEco Studio菜单栏，点击**File > Setting****s...**（macOS为**DevEco Studio > Preferences****/Settings**）**> Plugins**，在Installed列表中找到UI Generator插件，点击**Enable**启用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/eaA8k9x5RTOZK0BA1hirXw/zh-cn_image_0000002530913614.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=34D7EF8022644EBA5FD1AD5C610C3DCE738601B0AD22EE449C501D09B00C6FE2)
2. 单击OK并关闭设置窗口，插件启用成功。

## 开始使用

1. 在DevEco Studio菜单栏点击**Tools > Generate Project From...**打开UI Generator工具，首次使用需要阅读并确认用户协议，确认后可继续使用。
2. 输入待配置项路径，点击**Next**进入下一步。

   | 待配置项 | 说明 |
   | --- | --- |
   | Installation package path | 待转换的APK应用包的路径，请提供未混淆的Debug版本应用包。 |
   | SDK path | 等于或高于编译应用包所使用版本的SDK路径。 |
   | Git Bash path | Git Bash工具存放路径。若本地已下载安装Git Bash，插件将自动获取其路径。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Z57lvVQ1Q9C9Gn5QWYR9eQ/zh-cn_image_0000002561833533.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=2964662A118F76238FD6862C7EBCB79BDBAD7D8AF6C75D07347E2C3E7886D3EB)
3. 选择将要生成的XML页面（可在搜索框进行搜索），勾选后点击向右箭头将选中的XML导入至右侧。点击**Next**开始生成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/NOGweWjvRu6kIC9XLYZtqA/zh-cn_image_0000002530753612.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=466D005D06F08EEE34D99D8AC06E1B6997F5D27D79F8A3E13D05E943247BE5B1)
4. 配置输出工程待配置项，点击**Finish**进行生成。

   | 待配置项 | 说明 |
   | --- | --- |
   | Destination Path | 生成新工程的保存路径（默认生成到用户目录下UIGenerationProjects，用户可根据需要自行更改） |
   | Compatible SDK | 生成的新工程所使用的SDK版本 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/mgHnHyUiT0muSWDojmmNeQ/zh-cn_image_0000002561833541.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=DE6685F4615CBB233407094466803F813D4913242A049D2F79D98E90135836CD)
5. （可选）如果所选XML无有效根节点，需要选择根节点信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/kEtMvf3WQhC1JzqC1FGH-w/zh-cn_image_0000002561833535.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=64FFF0FB4E48448D0C11CC018774A9122DAB47D36E21F49A99D80E54C3302EC2)
6. 点击**Finish**，在弹窗中点击确认，打开新工程。

   生成的页面位于entry > src > main > ets > pages目录下，可以点击Previewer查看页面预览效果。不支持生成的组件、属性会以注释的形式给出，方便后续定位修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/QiH6G2kQRG2Wgft8q_7NBw/zh-cn_image_0000002561833543.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=18D4A26D56881ED53CA8B191592044280C3543BA5A5333D8B4CEE8A4E111BDAA)
7. 生成的新工程内的entry > src > main > resources目录包含文本、图像、颜色资源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/QUWabogQQpSHr88N47--dA/zh-cn_image_0000002561753559.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=25D95A529E6841D68F217656B453A864184013C0E2C3E16C00CA2CF1110940A7 "点击放大")

   更多操作指导，请参考视频课程：[毕方HarmonyOS UI代码生成工具](https://developer.huawei.com/consumer/cn/training/course/live/C101731322888995220)。
