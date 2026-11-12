---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-45
title: DevEco Studio安装后使用过程中常见配置问题
breadcrumb: FAQ > DevEco Studio > 环境准备 > DevEco Studio安装后使用过程中常见配置问题
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9f3bd03abe48bb5de28607e9d9530b6455f84ff50d6f96b2b7958c84a19b6e4f
---

## 问题现象

问题一：当前代码不展示高亮，并且也不显示代码补全提示。

问题二：开发工具DevEco Studio安装后Tools下没有显示Device Manager选项，在设备预览下拉表中也没有Device Manager选项。

问题三：DevEco Studio开启后特别耗电，如何配置可以降低耗电。

问题四：使用DevEco Studio，新建工程、新建模块、Project Structure、Choose Process等页面显示空白。

## 解决方案

### 问题一

* 检查是否误操作关闭了该文件的语法检查，将OFF修改为All Problems查看代码是否恢复高亮，若未恢复高亮，则重启DevEco Studio重试：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/7AnTDrnXTzaSkKmspXsalw/zh-cn_image_0000002658804709.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=280CE28379781804E09232BFAA25A0436CFD79723C9970F553724854ACD3BBB1 "点击放大")

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/WpMAn_HCQLa28tbDjd1vFw/zh-cn_image_0000002628565342.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B2221F8C6D274D32012B070031128CC8EC8804101D9DEB1F59E001FD6BC1976 "点击放大")
* 检查是否开启了省电模式，取消省电模式：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/LTWMAppiSZSodopckLpv2Q/zh-cn_image_0000002628405440.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=83DCA05920F83AE8B030CCED7DF5AA3443614C4B136A7C95F32E6F6ED9095D80)
* 缓存问题，导致未正确索引该文件，清除缓存重新运行DevEco Studio：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/ZYKWHlXhSUeakpW1VLOTTA/zh-cn_image_0000002658924649.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=70FBF883283074A37D50712C89EF1528F9A6F8A8C156B03067053565E5C1A423)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/19yLwqTHTUu1qFZ-kMrNiA/zh-cn_image_0000002658804711.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=682C9554FA91C72AD378E3C82A0117CDD65325A2F23E265A67141CFDA591EE7C)

### 问题二

* 在DevEco Studio->Settings->OpenHarmony SDK检查是否安装SDK。没有SDK的话可以点击对应版本进行更新或者下载：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/0FPlZoMwTX2BQrkVwqcCJw/zh-cn_image_0000002628565344.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC45D0EA760BEE08031292F2FC01CCC79298DFE49BDBCA613ADA8050F27ADB2E "点击放大")
* 模拟器当前仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）使用，确认开发者账号是否满足，通过右上角图标登录或更换账号：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/b3-bmap_SVCChrerR4XCOw/zh-cn_image_0000002628405442.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=82EFF3852DF9F1B943E9DDFA08419618258CEAB4CCA3180DF12C8CE9DFEE8808)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/SaZhttxYTv2_eMNIWa81mg/zh-cn_image_0000002658924651.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=111365A745F5845B1101A44F3122152C19F4D34A275BB7FD4DE9099DD2C8AE28)
* 检查用户目录下国家码配置是否为CN。路径C:\Users\XXX\AppData\Roaming\Huawei\DevEcoStudio6.0\options\country.region.xml，手动修改为CN重启DevEco Studio：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/OGyFHNwbR9OZIckMn2P1gQ/zh-cn_image_0000002658804713.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=5EF9EB5E8EC47B659E80892824A8CC5C501E58C177C5BD9881D5F1E7BD0B6573 "点击放大")

### 问题三

* 可以通过以下方案解决IDE高耗电:
  1. 开启IDE省电模式：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/7r3aACuIQHWpIJ8qhTUPBQ/zh-cn_image_0000002628565346.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9FC1D9E9951FE1E7C465DE73DED0EEA5AA6E555DD68398C19D51A549894D583)
  2. 禁用CodeGlance（缩略图）等非必需插件，减少图形渲染负担：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/ccJ9Z20NSMyOarvs009cLQ/zh-cn_image_0000002628405444.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=91A3A98D86CAE4FA0645D404903577487BEF2A3633613DD252D324F6863DE632 "点击放大")
  3. 禁用GPU渲染:在idea.properties文件中添加sun.java2d.opengl=false，idea.properties位于DevEco Studio安装目录的bin目录下。

### 问题四

* 关闭jcef的GPU渲染：
  1. 点击右上角的放大镜图标，搜索配置项：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/J-FZESr_Rgq7jK08tgg3pQ/zh-cn_image_0000002658924653.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C44A36DB6C5635A1CC3A01CB1310A9A1885AE555374D6781CBAC80460E7E766)
  2. 输入registry，点击下面的Registry...选项：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/ztXbvFsqSjqsSgPlFf6X8A/zh-cn_image_0000002658804715.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=96CEB345AB48E33CE51BADE1CDA422762EC8A8DF53E92C32C8A61953523B3EBC)
  3. 直接输入gpu进行查找，勾选ide.browser.jcef.gpu.disable这一项，重启IDE：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/fQQefYEVTGKksxthqhW_Yw/zh-cn_image_0000002628565348.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=42D7AA879A1AF600A3C56FFC01E172A1DA929C871304A7F60A5EDF21CE9E4C8E)
* 可能是DevEco Studio权限不足导致，以管理员身份启动DevEco Studio：
  1. 在DevEco Studio安装目录的bin目录找到DevEco Studio的启动图标：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/Ga50mKhaTsSDznXT9ag0iQ/zh-cn_image_0000002628405446.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D3920B8FD6BB4D9A5A91A2820D147B1353DADB72B4ED1498E75A85916B865CD)
  2. 选中启动图标右键->属性->兼容性->以管理员身份运行此程序->确定，启动DevEco Studio：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/CLzSpcK9TsmVpJgKVTDPBA/zh-cn_image_0000002658924655.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2B92F8E59515FF88EE7B481A50481E767E8BAFDBAAAEB33BC2DD50DC41BD496)
* jcef文件缺失导致：

  检查jbr/bin/server/jvm.dll及jbr/bin/chrome\_elf.dll是否存在，jcef文件缺失，导致jcef进程无法拉起，如果不存在，则需要重新安装DevEco Studio：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/oDA6ZErtTFqswoBqvVqXMA/zh-cn_image_0000002658804717.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BD27908614A619ABC4E7936D05C3F9FCF1877A11AE09E9913DF9E3CA29B8A74)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/qDYhhAOESuK47f_PWQnxBg/zh-cn_image_0000002628565350.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=FED78EF2EC13D10DF94D5A6596FD78A7BB4E44E0B3348E567D0AFE3231DE6DCB "点击放大")
* jcef沙箱环境与当前电脑环境冲突，导致jcef无法正常工作，关闭jcef沙盒功能：
  1. 点击右上角的放大镜图标，搜索配置项：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/unkoOM1kT_u36CGSIMw5uw/zh-cn_image_0000002628405448.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=055EA74EAF918EAE357A245C96424D040B555F05182FA71EB3BFAB04D8C67749)
  2. 输入registry，点击下面的Registry...选项：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/m0voCZLnRtyLF0UDenK1GQ/zh-cn_image_0000002658924673.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C081A270C42B0F527E4737310C73EA9A32A137626660081FD419A02E08411E2)
  3. 直接输入sandbox进行查找，取消勾选ide.browser.jcef.sandbox.enable这一项，重启IDE：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/DLcvy3FITUan6X2qP501Vw/zh-cn_image_0000002658804735.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=1826E22E6D53F513B5901A90859A7E54075CC57325D562088969B213B03E4E30)
