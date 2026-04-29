---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-181
title: 编译报错“Error: open 'xxx\libimage_transcoder_shared.dll' failed”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Error: open 'xxx\libimage_transcoder_shared.dll' failed”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a08fa8a3f8749943deffac7fbe22a24265132917523369640141ff5ea0e0d8c1
---

**问题现象**

Windows下编译工程出现错误，提示“Error: open 'xxx\deveco-studio\sdk\default\hms\toolchains\lib\libimage\_transcoder\_shared.dll' failed”，加载dll失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/2R0MlrhfRIKwgN1h1a78Cg/zh-cn_image_0000002194158948.png?HW-CC-KV=V1&HW-CC-Date=20260429T062100Z&HW-CC-Expire=86400&HW-CC-Sign=FB221E73F1E46AA53E1045E48A7C55E3C4A6C2C94EC95D9F4804F84DE00BA4F4)

**可能原因**

1、系统在环境变量中找不到libimage\_transcoder\_shared.dll及其依赖的第三方库路径。

2、用户环境变量或系统环境变量中的某些路径包含权限受限或损坏的文件，这些文件无法被正常访问。如果这些路径在环境变量中的顺序排在libimage\_transcoder\_shared.dll之前，系统在加载 DLL 时会按顺序搜索环境变量，并首先访问这些出错的文件。

例如，用户环境变量中包含%USERPROFILE%\AppData\Local\Microsoft\WindowsApps。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/40twT5KkT7SGZJoQ8kLaiQ/zh-cn_image_0000002229758829.png?HW-CC-KV=V1&HW-CC-Date=20260429T062100Z&HW-CC-Expire=86400&HW-CC-Sign=1538F46C5181E8C2BF50F9967F8E448526D17FEE5691384D30C5AFA7D5C8715B)

该路径的文件无法访问。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/fcjzXAC6S92_zDWAIWCbtg/zh-cn_image_0000002194158944.png?HW-CC-KV=V1&HW-CC-Date=20260429T062100Z&HW-CC-Expire=86400&HW-CC-Sign=07E58BE78B8F356E748D7E3BA70387E19F83DE9D32FEE4BD07B4C29C11599C93)

**解决措施**

1、将报错的路径xxx\deveco-studio\sdk\default\hms\toolchains\lib和xxx\deveco-studio\sdk\default\openharmony\previewer\common\bin手动添加到系统环境变量的最前面。

2、检查用户环境变量和系统环境变量中的所有路径，确保这些路径下的文件均可访问。可以通过尝试修改文件（如覆盖、压缩等）来观察是否有报错。将无法访问的路径从环境变量中删除。
