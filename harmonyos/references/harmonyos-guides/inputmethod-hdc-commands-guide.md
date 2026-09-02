---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/inputmethod-hdc-commands-guide
title: Ime工具
breadcrumb: 指南 > 应用框架 > IME Kit（输入法开发服务） > Ime工具
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:26+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:72be3a78ca12e1366c4f93ddbdf031d675612a6ba3ddf1d72759f6f6db0b5620
---

**说明** 

Ime工具从API version 20开始支持。

**工具用法**

hdc shell ime [选项] [参数]

**命令列表**

| 选项 | 参数 | 描述 |
| --- | --- | --- |
| -u | userId | 指定操作的用户ID（该值默认为主屏幕的前台用户ID）。可与其他选项配合使用，用于多用户环境下的输入法管理。 |
| -e | bundle [-b /-f] | 启用指定输入法到指定模式。未设置-b/-f选项时，默认-b为基础模式，-f为完整体验模式。  **注意：** 系统预置的默认输入法不支持通过此命令更改其使能状态。 |
| -d | bundle | 禁用指定输入法。  **注意：** 不允许禁用预置默认输入法。 |
| -s | bundle | 切换到指定输入法。  **注意：** 在锁屏或密码输入场景下，不允许切换到其他输入法。 |
| -g | NA | 获取当前输入法。 |
| -l | NA | 列出所有输入法。 |
| -h | NA | 显示本帮助信息。 |

## 通过Ime工具管理输入法示例代码

1. 启用输入法，支持启用三方输入法到基础模式或者完整体验模式。

   ```shell
    # 输入：hdc命令启用输入法。
    # 处理：检查为shell调用后，将调用系统输入法管理接口。
    # 输出：效果等同于启用API调用。
    # 基础模式
    hdc shell ime -e com.xxx.yyy
    # 完整体验模式
    hdc shell ime -e com.xxx.yyy -f
   ```
2. 禁用输入法，支持停用三方输入法应用。

   ```shell
    # 输入：hdc命令禁用输入法。
    # 处理：检查为shell调用后，将接到禁用输入法的接口。
    # 输出：效果等同于禁用API调用。
    hdc shell ime -d com.xxx.yyy
   ```
3. 切换到指定输入法。

   ```shell
    # 输入：hdc命令切换输入法。
    # 处理：检查为shell调用后，将接到切换输入法接口。
    # 输出：效果等同于切换输入法API调用。
    hdc shell ime -s com.xxx.yyy
   ```
4. 获取当前输入法。

   ```shell
    # 输入：hdc命令获取当前输入法。
    # 处理：检查为shell调用后，将接到获取当前输入法接口。
    # 输出：效果等同于获取当前输入法API调用。
    hdc shell ime -g
   ```
5. 列出所有输入法，预置默认输入法不显示使能状态。

   ```shell
    # 输入：hdc命令列出所有输入法。
    # 处理：检查为shell调用后，将接到列出所有输入法接口。
    # 输出：效果等同于列出所有输入法API调用。
    hdc shell ime -l
   ```
6. 显示本帮助信息。

   ```shell
    # 输入：hdc命令显示ime帮助信息。
    # 输出：显示ime帮助信息。
    hdc shell ime -h
   ```

## 多用户环境下的输入法管理

从API版本26.0.0开始：在多用户环境下，可以使用-u选项指定目标用户ID，对不同用户的输入法进行管理。

### 多用户命令示例

1. 获取指定用户的当前输入法。

   ```shell
    # 输入：获取用户100的当前输入法。
    # 处理：系统会查询用户100的当前输入法。
    # 输出：显示用户100的当前输入法信息。
    hdc shell ime -u 100 -g
   ```
2. 切换指定用户的输入法。

   ```shell
    # 输入：为用户100切换到指定输入法。
    # 处理：系统会为用户100切换到指定的输入法。
    # 输出：显示切换结果。
    hdc shell ime -u 100 -s com.example.ime
   ```
3. 为指定用户启用输入法。

   ```shell
    # 输入：为用户100启用指定输入法到基础模式。
    # 处理：系统会为用户100启用指定的输入法。
    # 输出：显示启用结果。
    hdc shell ime -u 100 -e com.example.ime

    # 启用到完整体验模式
    hdc shell ime -u 100 -e com.example.ime -f
   ```
4. 为指定用户禁用输入法。

   ```shell
    # 输入：为用户100禁用指定输入法。
    # 处理：系统会为用户100禁用指定的输入法。
    # 输出：显示禁用结果。
    hdc shell ime -u 100 -d com.example.ime
   ```
5. 列出指定用户的所有输入法。

   ```shell
    # 输入：列出用户100的所有输入法。
    # 处理：系统会查询用户100的所有输入法。
    # 输出：显示用户100的所有输入法列表。
    hdc shell ime -u 100 -l
   ```

**说明** 

* -u选项为可选项，如果不指定，默认操作当前用户。
* 用户ID必须为非负整数。
* 只有用户0的应用才能执行跨用户操作。
