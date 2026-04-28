---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-execution-point
title: 设置执行点
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 设置执行点
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:2d6fa3118715b84819a5fbd1ff0119f070c19fa447be4492b678d5244e0a7523
---

开发者可以通过“设置执行点”在调试会话期间跳转到编辑器中的任意代码行，并在对应位置设置执行点，跳过当前位置到目标位置之间的所有代码。

此操作适用于线性和非线性执行路径，用于中断和跳过循环，或者在if-else子句表达式或switch-case语句中选择另一个分支。例如，如果要检查另一个分支而不重新启动调试会话，可使用该功能。

## 操作步骤

1. 将当前执行指针（代表当前运行位置的橙色箭头）拖动到所需的代码行。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/QbImsZ1URdKuCgLw-4fYPA/zh-cn_image_0000002530912830.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=3BC36AD94328612024D7A96880FFE5192D87EFED7B195AD0C000B082DE305FFC)
2. 在需要设置执行点的行，点击鼠标右键，在弹出菜单中选择“Set Execution Point to Cursor”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/sz_i8OKoTSKdZmPlAyafhg/zh-cn_image_0000002530912826.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=8D45046EA63A35BEF10AB2B2457FAE07FAA8C966E6715F96969717C040A0DA04)

说明

使用“设置执行点”时，仅修改了程序计数器的值，未修改其他寄存器的值，这可能会导致不可预知的错误，例如：

* 如果跳过初始化变量的那一行，应用将从堆栈/寄存器中获取值，这可能会导致段错误。
* 如果可执行代码被编译器优化，可能会得到一个不可预知的结果，或者无法移动执行点。

此外，还有一些其他不符合预期的问题，例如变量值错乱、堆栈信息异常等。
