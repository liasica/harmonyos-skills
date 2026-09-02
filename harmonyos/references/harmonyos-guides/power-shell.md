---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/power-shell
title: power-shell工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > power-shell工具
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9a6a49cead3424823080afb133adc572dd1a8eea6a79c8b6992a0e6108a5c03e
---

power-shell是实现设备电源状态转换等功能的工具，为开发者提供基本的设备电源状态调试能力，例如：熄屏、唤醒、设置电源模式等。

## 环境要求

开发者在使用本工具前需开启开发者模式，且需要获取[hdc工具](hdc.md)，执行hdc shell。

## power-shell命令工具列表

| 命令 | 描述 |
| --- | --- |
| help | 帮助命令，显示power-shell支持的命令信息。 |
| setmode | 设置电源模式命令，用来设置当前设备的电源模式。 |
| wakeup | 亮屏命令，用来唤醒系统并亮屏。 |
| suspend | 熄屏命令，用来暂停系统并熄屏。 |
| timeout | 自动熄屏命令，用来覆盖或恢复系统设置中自动熄屏时间。 |

## 帮助命令

```bash
# 显示帮助信息
power-shell help
```

## 设置电源模式命令

```bash
power-shell setmode
```

**设置电源模式命令列表**

| 命令 | 描述 |
| --- | --- |
| power-shell setmode -h | 显示setmode支持的命令信息。 |
| power-shell setmode 600 | 正常模式。 |
| power-shell setmode 601 | 省电模式。 |
| power-shell setmode 602 | 性能模式。 |
| power-shell setmode 603 | 超级省电模式。 |

示例：

```bash
# 设置设备电源状态为正常模式
power-shell setmode 600
# 设置设备电源状态为省电模式
power-shell setmode 601
# 设置设备电源状态为性能模式
power-shell setmode 602
# 设置设备电源状态为超级省电模式
power-shell setmode 603
```

## 亮屏命令

```bash
power-shell wakeup
```

**亮屏命令列表**

| 命令 | 描述 |
| --- | --- |
| power-shell wakeup | 亮屏。 |

示例：

```bash
# shell命令亮屏
power-shell wakeup
```

## 熄屏命令

```bash
power-shell suspend
```

**熄屏命令列表**

| 命令 | 描述 |
| --- | --- |
| power-shell suspend | 熄屏。 |

示例：

```bash
# shell命令熄屏
power-shell suspend
```

## 自动熄屏命令

```bash
power-shell timeout
```

**自动熄屏命令参数列表**

| 参数 | 参数说明 |
| --- | --- |
| -o <time> | 必选参数，设置自动熄屏时间。[time]单位为毫秒。 |
| -r | 必选参数，恢复到当前系统设置中的自动熄屏时间。 |

示例：

```bash
# 当前系统设置中自动熄屏时间为30秒
# shell命令设置自动熄屏时间为15000毫秒
power-shell timeout -o 15000
# 恢复系统设置的自动熄屏时间，此时自动熄屏时间为30秒
power-shell timeout -r
```
