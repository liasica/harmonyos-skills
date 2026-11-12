---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-24
title: 打开工程时左侧目录树不显示
breadcrumb: FAQ > DevEco Studio > 工程管理 > 打开工程时左侧目录树不显示
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:571dba383dae76913acf96fcbd9ba0aff87db377fac00c71de259431ef6dcbfa
---

**问题现象**

左侧目录树不显示，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/wRJIqAL4RDWB3ds4Rs9rFA/zh-cn_image_0000002624478438.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=ABB5951C040760B276DFDC5C76F0598A5C02B09087502EA43012E1A897CCE135)

**问题原因**

**情况1：**

在 macOS上，系统对隐私权限的管理非常严格。如果没有获得访问特定目录（如“下载”或“桌面”）的权限，就会出现项目虽然打开了，但左侧目录树一片空白的情况。

**情况2：**

当用户删除工程目录下的.idea/modules文件夹或者.idea/modules文件夹不存在时，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/Czw9Jv92SJ2rNDwrIqX4RQ/zh-cn_image_0000002654797805.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=332D6449486D6C3562A5952985D38004CDD82204A3A1B16D093AA3CEE628C8D3)

由于modules文件夹下的iml文件定义了详细的工程模块结构信息，modules.xml定义了工程模块结构文件的位置。删除modules文件夹后根据modules.xml无法找到对应的iml文件。

**解决措施**

**情况1：**

如果缺少访问权限，设置项目文件夹访问权限就可以解决问题：系统设置->隐私与安全->文件和文件夹->允许访问（找到DevEco Studio，点击展开），重启IDE，工程目录树才可以恢复

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/SdUG0dc_RjeB-tGxfOL_2g/zh-cn_image_0000002624638346.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=AAC4015255469B0A748986590460EC943975A7B398C92D4BA0E07E420AD2701C)

**情况2：**

需要关闭工程，在文件管理器中删除工程的modules.xml，重新启动IDE打开工程，工程目录树才可以恢复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/H_xf8_LBShuEaYBsa4qnAA/zh-cn_image_0000002654837751.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F507E56011A72AE5726647D5899B4B2FF165185B42CB75C813CE842C6E0E33F)
