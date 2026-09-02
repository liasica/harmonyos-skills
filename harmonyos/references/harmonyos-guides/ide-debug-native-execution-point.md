---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-execution-point
title: 设置执行点
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 设置执行点
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:25+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0cbce1737e62e1b1e984004734583cc3aabf6c67ab4fb3f625c9c23eba55f6b1
---

开发者可以通过“设置执行点”在调试会话期间跳转到编辑器中的任意代码行，并在对应位置设置执行点，跳过当前位置到目标位置之间的所有代码。

此操作适用于线性和非线性执行路径，用于中断和跳过循环，或者在if-else子句表达式或switch-case语句中选择另一个分支。例如，如果要检查另一个分支而不重新启动调试会话，可使用该功能。

## 操作步骤

1. 将当前执行指针（代表当前运行位置的橙色箭头）拖动到所需的代码行。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/USX5xN0jQjKzUMmuO2ktRg/zh-cn_image_0000002701822654.png)
2. 在需要设置执行点的行，点击鼠标右键，在弹出菜单中选择“Set Execution Point to Cursor”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/Ll0MM9j_SuCBIXB73wseNw/zh-cn_image_0000002731381955.png)

**说明** 

使用“设置执行点”时，仅修改了程序计数器的值，未修改其他寄存器的值，这可能会导致不可预知的错误，例如：

* 如果跳过初始化变量的那一行，应用将从堆栈/寄存器中获取值，这可能会导致段错误。
* 如果可执行代码被编译器优化，可能会得到一个不可预知的结果，或者无法移动执行点。

此外，还有一些其他不符合预期的问题，例如变量值错乱、堆栈信息异常等。
