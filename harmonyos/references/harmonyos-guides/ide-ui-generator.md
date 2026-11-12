---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-generator
title: 应用UI生成
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 应用UI生成
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:2d43dd6d2541596206af589a04c3dee2d9b19ddb7928bb6618cab57f1ea87a6d
---

UI Generator用于快速生成可编译、可运行的HarmonyOS UI工程，支持基于已有UI布局文件（XML），快速生成对应的HarmonyOS UI代码，其中包含HarmonyOS基础工程、页面布局、组件及属性和资源文件等。

## 使用约束

建议使用DevEco Studio 5.0.3.700及以上版本。

## 启用插件

1. 在DevEco Studio菜单栏，点击**File > Setting****s...**（macOS为**DevEco Studio > Preferences****/Settings**）**> Plugins**，在Installed列表中找到UI Generator插件，点击**Enable**启用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/fbqcNE6jR3eg5G34-QlKWg/zh-cn_image_0000002808767119.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E294CE5FFEE30DB82D972AE64210903105F8885E4A4CBEF967C5EA93786169F5)
2. 单击OK并关闭设置窗口，插件启用成功。

## 开始使用

1. 在DevEco Studio菜单栏点击**Tools > Generate Project From...**打开UI Generator工具，首次使用需要阅读并确认用户协议，确认后可继续使用。
2. 输入待配置项路径，点击**Next**进入下一步。

   | 待配置项 | 说明 |
   | --- | --- |
   | Installation package path | 待转换的APK应用包的路径，请提供未混淆的Debug版本应用包。 |
   | SDK path | 等于或高于编译应用包所使用版本的SDK路径。 |
   | Git Bash path | Git Bash工具存放路径。若本地已下载安装Git Bash，插件将自动获取其路径。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/luKf-Ek4RY2MSy8bIUF5Mw/zh-cn_image_0000002779407564.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=8157E9045BBBB1B404B6DB6D5728D067F3E96C6C980CEFE9D4777C2CF92D45BA)
3. 选择将要生成的XML页面（可在搜索框进行搜索），勾选后点击向右箭头将选中的XML导入至右侧。点击**Next**开始生成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/ozPCCi1rQJGIQuLFwY7dcw/zh-cn_image_0000002808767117.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=504A8216905D4BF4E27516A1045ABA819D6485848EB42230F04BA25AB416C173)
4. 配置输出工程待配置项，点击**Finish**进行生成。

   | 待配置项 | 说明 |
   | --- | --- |
   | Destination Path | 生成新工程的保存路径（默认生成到用户目录下UIGenerationProjects，用户可根据需要自行更改） |
   | Compatible SDK | 生成的新工程所使用的SDK版本 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/bV9-hQVoTb2StRFHGq8T_A/zh-cn_image_0000002779407566.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=EEF05C294F547AE4309EAA0CC9D8F5249B327055D5D2573AFAAC5E4549426C9B)
5. （可选）如果所选XML无有效根节点，需要选择根节点信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/kKFoj4dUTwW6wpIEysj3xA/zh-cn_image_0000002808887203.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C67CCABA81AC665B48CB58A9BF5398CA38B84A271F10365DF51446ACA4F412D)
6. 点击**Finish**，在弹窗中点击确认，打开新工程。

   生成的页面位于entry > src > main > ets > pages目录下，可以点击Previewer查看页面预览效果。不支持生成的组件、属性会以注释的形式给出，方便后续定位修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/gScFwcQ-SSSD7-SOiB1k2Q/zh-cn_image_0000002808887205.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B338743EB8F7B02DC48B240B52CCEAD9F5A1C25D8AD5B5C89C4574E2EF698EA)
7. 生成的新工程内的entry > src > main > resources目录包含文本、图像、颜色资源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/X1fWFmhKRTeHUc2Fpz2RVQ/zh-cn_image_0000002779567540.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=50741D6137310BEC7192224E1B66739D5E7E84D4ED00C29CE2D1D16284B1BA6A "点击放大")

   更多操作指导，请参考视频课程：[毕方HarmonyOS UI代码生成工具](https://developer.huawei.com/consumer/cn/training/course/live/C101731322888995220)。
