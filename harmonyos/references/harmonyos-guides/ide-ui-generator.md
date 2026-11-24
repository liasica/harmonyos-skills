---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-generator
title: 应用UI生成
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 应用UI生成
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:39+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:f758db704aa5779ee78e7c1981da667a91d7840c8983854a6e2c668915a9686c
---

UI Generator用于快速生成可编译、可运行的HarmonyOS UI工程，支持基于已有UI布局文件（XML），快速生成对应的HarmonyOS UI代码，其中包含HarmonyOS基础工程、页面布局、组件及属性和资源文件等。

## 使用约束

建议使用DevEco Studio 5.0.3.700及以上版本。

## 启用插件

1. 在DevEco Studio菜单栏，点击**File > Setting****s...**（macOS为**DevEco Studio > Preferences****/Settings**）**> Plugins**，在Installed列表中找到UI Generator插件，点击**Enable**启用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/PdB8wVu-TF-ng6cErjKTrw/zh-cn_image_0000002808767119.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=05CD51EB0B1FBAD2372DA531024F496AE685B0C4596DB5B917EC7DD23A8B8E57)
2. 单击OK并关闭设置窗口，插件启用成功。

## 开始使用

1. 在DevEco Studio菜单栏点击**Tools > Generate Project From...**打开UI Generator工具，首次使用需要阅读并确认用户协议，确认后可继续使用。
2. 输入待配置项路径，点击**Next**进入下一步。

   | 待配置项 | 说明 |
   | --- | --- |
   | Installation package path | 待转换的APK应用包的路径，请提供未混淆的Debug版本应用包。 |
   | SDK path | 等于或高于编译应用包所使用版本的SDK路径。 |
   | Git Bash path | Git Bash工具存放路径。若本地已下载安装Git Bash，插件将自动获取其路径。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/NsEPhNnqSHCa00Sr8eCOrQ/zh-cn_image_0000002779407564.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=26EABD6F82062C219B6E8CB746F893DA63B7A7F74B0C6327BF851055F7DBDE12)
3. 选择将要生成的XML页面（可在搜索框进行搜索），勾选后点击向右箭头将选中的XML导入至右侧。点击**Next**开始生成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/blDt44qwTFC0jYvbwYv35A/zh-cn_image_0000002808767117.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4E7D917215787D0BDB236D63B509A2B0B322C7184B548026683596D6B28750F)
4. 配置输出工程待配置项，点击**Finish**进行生成。

   | 待配置项 | 说明 |
   | --- | --- |
   | Destination Path | 生成新工程的保存路径（默认生成到用户目录下UIGenerationProjects，用户可根据需要自行更改） |
   | Compatible SDK | 生成的新工程所使用的SDK版本 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/97FAlO4USQerTEZR9dcfUA/zh-cn_image_0000002779407566.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA5F099AB5D5082664BEFE09C9644D5F9752F1ECF4A252A60DEB9E78E7884D40)
5. （可选）如果所选XML无有效根节点，需要选择根节点信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/7VE9ZR_oQ3iNVDMU7IfSlw/zh-cn_image_0000002808887203.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD96FF11E8F1ACDF5598D951F2878CACAC77901B65D692FCACC4B6B5AF07B0AE)
6. 点击**Finish**，在弹窗中点击确认，打开新工程。

   生成的页面位于entry > src > main > ets > pages目录下，可以点击Previewer查看页面预览效果。不支持生成的组件、属性会以注释的形式给出，方便后续定位修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/bUU9N1MXQWePVMywe-R9_Q/zh-cn_image_0000002808887205.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D97147FFB7FA026A7353823170BBC11D08C2FD81211972B58F7B84A99ABAD85)
7. 生成的新工程内的entry > src > main > resources目录包含文本、图像、颜色资源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/kj1ne51LQWOsfKwLYJDT7A/zh-cn_image_0000002779567540.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=4ADB8A5B07D02CC235ADF8AA2BBA279911EFB71A6791AA3CFED6E1E05D8E439C "点击放大")

   更多操作指导，请参考视频课程：[毕方HarmonyOS UI代码生成工具](https://developer.huawei.com/consumer/cn/training/course/live/C101731322888995220)。
