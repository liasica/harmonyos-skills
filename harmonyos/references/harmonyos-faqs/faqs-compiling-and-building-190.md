---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-190
title: 历史问题报错：“hvigor ERROR: Error: EINVAL: invalid argument, mkdir ‘D:xxx\yyy\zzz\D:’/ 'C:xxx\yyy\zzz\C:at Object.mkdirSync (node:fs:1391:3)”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 历史问题报错：“hvigor ERROR: Error: EINVAL: invalid argument, mkdir ‘D:xxx\yyy\zzz\D:’/ 'C:xxx\yyy\zzz\C:at Object.mkdirSync (node:fs:1391:3)”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:05+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:4603868e83f6d20a6cde7e336acbc38aa0b42e912ab6c2ae6a10143e48afb1c6
---

**问题现象**

构建报错：“hvigor ERROR: Error: EINVAL: invalid argument, mkdir ‘D:xxx\yyy\zzz\D:’”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/Ui_eiyzST3WI7mUYQ1DDnQ/zh-cn_image_0000002433194024.png?HW-CC-KV=V1&HW-CC-Date=20260429T062103Z&HW-CC-Expire=86400&HW-CC-Sign=6352BD1356518C5854D593E4F798C0EC394959C428B02B420550CB31D589ABD9)

**常见错误场景**

工程A通过引用外部模块的方式使用了工程B中的har模块，在工程B中执行ohpm后，在工程A中没有重新执行ohpm install直接编译（或者调试），导致编译报错。

**问题原因**

ohpm远程第三方包安装后，软连接指向的路径为非本工程路径（是由于被其他工程篡改），编译时会出现预期之外的错误。注：能以非本工程路径存在的依赖仅为本地模块，参考官网工程外模块的使用方式）

**解决措施**

1.**在问题工程中重新执行ohpm install**，或者sync。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/P-0oou6RS42SHpS2G1mrQg/zh-cn_image_0000002433353864.png?HW-CC-KV=V1&HW-CC-Date=20260429T062103Z&HW-CC-Expire=86400&HW-CC-Sign=01BA1D6AC00902206887616C1F3837748A7A0477EE7ECC73F4F1B477BE6D54A4 "点击放大")

2.使用build菜单先进行构建，再调试运行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/-NtIbxJuSQqg6RMp9zJbCQ/zh-cn_image_0000002466912421.png?HW-CC-KV=V1&HW-CC-Date=20260429T062103Z&HW-CC-Expire=86400&HW-CC-Sign=07FE310D74FCD752E7B94D2A4FAF9CE15BD40A8B5468C849FC5159439C2D82F8 "点击放大")
