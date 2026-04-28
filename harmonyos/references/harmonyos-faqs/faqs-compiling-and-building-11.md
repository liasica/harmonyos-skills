---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-11
title: 编译报错“Property xxx does not exist on type 'typeof BuildProfile'.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Property xxx does not exist on type 'typeof BuildProfile'.”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3dbf50de673d6f4df2db3f50e1716cf719182e62d97b02b0d3170bc0b4723968
---

**问题现象****1**

使用自定义参数BuildProfile时，编译过程中未出现异常，但编译构建失败，提示“Property xxx does not exist on type 'typeof BuildProfile'”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/f1WGJTeMQnmXxtFRmyxF1Q/zh-cn_image_0000002229604165.png?HW-CC-KV=V1&HW-CC-Date=20260428T002908Z&HW-CC-Expire=86400&HW-CC-Sign=8CCED2B4DCB3CA91644BECD2C34141BE01FCB9A27EB9010D470C36D8A0A0E6B9)

**解决措施**

检查当前模块下build-profile.json5文件中targets>buildProfileFields配置的自定义参数的key值是否一致。如果不一致，请将targets内所有buildProfileFields的key值统一。

以下为导致编译报错的配置示例：

```
1. "targets": [
2. {
3. "name": "default",
4. "config": {
5. "buildOption": {
6. "arkOptions": {
7. "buildProfileFields": {
8. "targetName": "default"
9. }
10. }
11. }
12. }
13. },
14. {
15. "name": "default1",
16. "config": {
17. "buildOption": {
18. "arkOptions": {
19. "buildProfileFields": {
20. "targetName1": "default1"
21. }
22. }
23. }
24. }
25. }
26. ]
```

将targets内所有buildProfileFields的key值修改为一致，例如都修改为targetName。

**问题现象2**

使用了自定义参数BuildProfile并且编译器标红且构建失败，提示“Property xxx does not exist on type 'typeof BuildProfile'.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/AlmsVrhVTAmIaJp94VIZ3g/zh-cn_image_0000002194318396.png?HW-CC-KV=V1&HW-CC-Date=20260428T002908Z&HW-CC-Expire=86400&HW-CC-Sign=5E8E6EBD1F0DAA3E379988AE4166BA7507E44E53E25A7CBE9FD711235B240549)

**解决措施**

检查当前模块下的 build-profile.json5文件，确保buildProfileFields中已添加所使用的自定义参数。
