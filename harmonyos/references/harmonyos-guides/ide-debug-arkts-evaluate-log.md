---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-evaluate-log
title: 打印表达式
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 打印表达式
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:43dbd87399863271b0a55a45b43cde2ff5f716f6115be8e77391a7ed926c9b61
---

开发者可以通过Evaluate and log能力在代码执行到断点行时打印开发者指定的表达式。

1. 在需要打印表达式结果的地方设置断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/qGDO5FHBRV-9R194Kq8e5g/zh-cn_image_0000002561832883.png?HW-CC-KV=V1&HW-CC-Date=20260427T235647Z&HW-CC-Expire=86400&HW-CC-Sign=B3AB23BA910CF8DED4347E72C774C3F52726EF5C3CE073E955C7AC5DD89E1E67)
2. 右键断点，然后点击**More**按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/5vJwQb9kRlKM7B5cHU-M_g/zh-cn_image_0000002561752901.png?HW-CC-KV=V1&HW-CC-Date=20260427T235647Z&HW-CC-Expire=86400&HW-CC-Sign=FF8F8146E4097AABD4715C8ECA347880896EE41A4652C1712E37289545893B06)
3. 勾选**Evaluate and log**复选框，并在下方输入框输入要打印的表达式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/q0oCEI0nRXuBDl5aUf9Bdg/zh-cn_image_0000002530912956.png?HW-CC-KV=V1&HW-CC-Date=20260427T235647Z&HW-CC-Expire=86400&HW-CC-Sign=888B27EE93355912E0840EAD8F90D51A9C04D9EA6665A0BE1F8420365189EBAC)
4. 启动调试，程序运行到断点时，切换到调试的Console窗口，表达式的打印结果将在这里展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/UmlQRuJ0S326C3u9J9YWjg/zh-cn_image_0000002561832879.png?HW-CC-KV=V1&HW-CC-Date=20260427T235647Z&HW-CC-Expire=86400&HW-CC-Sign=91ABBDAC38FBB8A6250DE930762F74CFA9D9B5344EA5EE9A7AC20410DE78E48D)
