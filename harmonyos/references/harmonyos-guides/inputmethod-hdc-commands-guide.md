---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/inputmethod-hdc-commands-guide
title: Ime工具
breadcrumb: 指南 > 应用框架 > IME Kit（输入法开发服务） > Ime工具
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a225e817b34463278e0696bf5b57c2d54afc7edd7529206af97183aab7f2921e
---

说明

Ime工具从API version 20开始支持。

**工具用法**

hdc shell ime [选项] [参数]

**命令列表**

| 选项 | 参数 | 描述 |
| --- | --- | --- |
| -e | bundle [-b /-f] | 启用指定输入法到指定模式。未设置-b/-f选项时，默认-b为基础模式，-f为完整体验模式。  **注意：** 预置默认输入法不支持调用此命令改变使能状态。 |
| -d | bundle | 禁用指定输入法。  **注意：** 不允许禁用预置默认输入法。 |
| -s | bundle | 切换到指定输入法。  **注意：** 在锁屏或密码输入场景下，不允许切换到其他输入法。 |
| -g | NA | 获取当前输入法。 |
| -l | NA | 列出所有输入法。 |
| -h | NA | 显示本帮助信息。 |

## 通过Ime工具管理输入法示例代码

1. 启用输入法，支持启用三方输入法到基础模式或者完整体验模式。

   ```
   1. # 输入：hdc命令启用输入法。
   2. # 处理：检查为shell调用后，将调用系统输入法管理接口。
   3. # 输出：效果等同于启用API调用。
   4. # 基础模式
   5. hdc shell ime -e com.xxx.yyy
   6. # 完整体验模式
   7. hdc shell ime -e com.xxx.yyy -f
   ```
2. 禁用输入法，支持停用三方输入法应用。

   ```
   1. # 输入：hdc命令禁用输入法。
   2. # 处理：检查为shell调用后，将接到禁用输入法的接口。
   3. # 输出：效果等同于禁用API调用。
   4. hdc shell ime -d com.xxx.yyy
   ```
3. 切换到指定输入法。

   ```
   1. # 输入：hdc命令切换输入法。
   2. # 处理：检查为shell调用后，将接到切换输入法接口。
   3. # 输出：效果等同于切换输入法API调用。
   4. hdc shell ime -s com.xxx.yyy
   ```
4. 获取当前输入法。

   ```
   1. # 输入：hdc命令获取当前输入法。
   2. # 处理：检查为shell调用后，将接到获取当前输入法接口。
   3. # 输出：效果等同于获取当前输入法API调用。
   4. hdc shell ime -g
   ```
5. 列出所有输入法，预置默认输入法不显示使能状态。

   ```
   1. # 输入：hdc命令列出所有输入法。
   2. # 处理：检查为shell调用后，将接到列出所有输入法接口。
   3. # 输出：效果等同于列出所有输入法API调用。
   4. hdc shell ime -l
   ```
6. 显示本帮助信息。

   ```
   1. # 输入：hdc命令显示ime帮助信息。
   2. # 输出：显示ime帮助信息。
   3. hdc shell ime -h
   ```
