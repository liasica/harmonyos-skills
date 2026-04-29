---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-realtime-check
title: 代码实时检查及快速修复
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > 代码实时检查及快速修复
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:17+08:00
doc_updated_at: 2026-03-24
content_hash: sha256:57a0e0425d1eb4ec6ed59c642ca445d94795e036e6a19c0a9ddf301aa4c9b472
---

## 实时检查

编辑器会实时地进行代码分析，如果输入的语法不符合编码规范，或者出现语义语法错误，将在代码中突出显示错误或警告，将鼠标放置在错误代码处，会提示详细的错误信息。

从DevEco Studio 4.0 Release版本开始，当compileSdkVersion≥10时，编辑器代码实时检查支持ArkTS性能语法规范检查。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/-0V7mZ0OT76nihGBbzlUUg/zh-cn_image_0000002561752973.png?HW-CC-KV=V1&HW-CC-Date=20260429T054515Z&HW-CC-Expire=86400&HW-CC-Sign=091B4001C580FCCF581E8F3DBD4EE576E065A869EE6CB4C235546291F770B519)

说明

当前compileSdkVersion≥10且arkTSVersion≥1.1（默认）时，ArkTS严格类型检查支持实时检查。

## 代码快速修复

DevEco Studio支持代码快速修复能力，辅助开发者快速修复ArkTS或C++代码问题。

**查看告警信息：**使用双击**Shift**快捷键打开文件查询框，输入**problems**打开问题工具面板；双击对应告警信息，可以查看告警的具体位置及原因。

**快速修复：**将光标放在错误告警的位置，可在弹出的悬浮窗中查看问题描述和对应修复方式；单击**M****ore actions**可查看更多修复方法。或是在页面出现灯泡图标时，可点击图标并根据相应建议，实现代码快速修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/C6Ux5Oo5QCOi9RyeqJLTFg/zh-cn_image_0000002561832975.png?HW-CC-KV=V1&HW-CC-Date=20260429T054515Z&HW-CC-Expire=86400&HW-CC-Sign=0951D69782B6D7D9C3805120E25D7D9A04F8C2F252F0AE057350F9D2663905AF)

## C++快速修复使用演示

下面通过示例展示C++代码中快速修复功能的使用方法。

### 填充switch语句

编辑器支持快速修复方式，对C++代码自动补齐switch条件表达式缺失的case条件，提升编码效率。

光标悬浮在switch表达式的条件变量处，点击灯泡图标，在下拉菜单中选择**Create missing switch cases**，完成缺失的case条件补充。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/ms2Z6-4pRW-DHaHGXTzhNw/zh-cn_image_0000002530753042.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054515Z&HW-CC-Expire=86400&HW-CC-Sign=3E188BA8674A221EBB71AD2FFB022292F8955911F719E4BEC6BD68FC187C04C0)

### 使用auto替换类型

编辑器中可以用 auto 替换 iterator，new expression，cast expression的声明类型。光标悬浮在类型名称处，点击灯泡图标，在下拉菜单中选择**Replace the type with 'auto****'**完成替换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/JU5k6b0MTNOVd3TzmJisig/zh-cn_image_0000002561752971.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054515Z&HW-CC-Expire=86400&HW-CC-Sign=5C1A30877D96E32CF8527FDABF1A24EAA42B32F6750A1DD156A51EF5D9DC8082)

### 用?:三元操作符替换if-else

编辑器中支持将if-else语句替换为?:三元操作符。光标放在if表达式的条件处，左侧出现黄色灯泡图标，点击灯泡图标，在下拉菜单中选择**Replace 'if else' with '?:'**完成替换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/ghjIM5_vTI-HZTEy8NVZWg/zh-cn_image_0000002561752981.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054515Z&HW-CC-Expire=86400&HW-CC-Sign=43D186A85E0A3B2E0AED6A09B3BE3A4AD2260346B79F5D10175A16BF5A165CE5)

### 从使用处生成构造函数

如使用了未定义的构造函数，可通过quickfix方式快速生成相应的构造函数定义。点击构造函数名称，左侧出现红色灯泡后，点击灯泡图标选择**Create new constructor 'xxx'**生成构造函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/_nxuU3y_Raq4s8uSRuGJGA/zh-cn_image_0000002561832967.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054515Z&HW-CC-Expire=86400&HW-CC-Sign=5FA28497FCF1AE37B0FB87A9718AEA9EC5005566B06D71D0FB56478BFA8B6078)

### 将变量拆分为声明和赋值

光标点击需要拆分的变量，左侧出现黄色灯泡后，点击灯泡图标选择**Split into declaration and assignment**，将变量的声明赋值语句拆分成声明语句和赋值语句。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/LS2pa3iJT7CZTTL92p57XA/zh-cn_image_0000002530913046.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054515Z&HW-CC-Expire=86400&HW-CC-Sign=AB049F2134F06FDCF598A60AFB384F02A05DD3D215C714866A49341A6F136EFF)
