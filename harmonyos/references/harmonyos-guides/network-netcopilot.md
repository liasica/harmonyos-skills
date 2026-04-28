---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/network-netcopilot
title: netcopilot工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > netcopilot工具
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a7d2d9bb99397f6853c920467d1c25798b433676c0b24274774c47ad419f2653
---

netcopilot是一款帮助开发者进行网络模拟的工具，通过hdc命令行直接调用网络领航员接口，执行网络领航员请求，目前已支持预置场景场景调用和自定义场景调用。

说明

netcopilot工具从API version 20开始支持。

在使用本工具前，开发者需要先获取hdc工具。

## 使用方法

### 命令行说明

```
1. hdc shell netcopilot <命令行参数> <子参数>
```

命令行参数和子参数可参考下述参数列表，用户也可先输入hdc shell命令，再执行网络领航员请求。

### 参数列表

| 命令行参数 | 子参数 | 功能 | 说明 |
| --- | --- | --- | --- |
| -h | NA | 输出帮助信息 | NA |
| -e | 0关闭，1开启 | 开启/关闭领航员 | 关闭时其他接口不可用。 |
| -p | NA | 打印网络场景列表 | 默认会打印预置场景列表：  进出电梯  离家断开WLAN  到家连接WLAN  人员拥挤的饭堂  弱信号的地库  乘坐地铁  乘坐高铁（多SIM切换）  高速公路自驾 |
| -s | 场景id | 启动场景模拟 | 允许在不同场景间直接切换；  场景模拟需要满足对应网卡要求，进出电梯、离家断开WLAN、到家连接WLAN场景需要同时连接WLAN和蜂窝网络；其他场景需要连接WLAN或蜂窝网络。 |
| -c | 场景id | 取消场景模拟 | NA |
| -P | 场景id | 打印自定义场景详情 | 仅支持自定义场景。 |
| -a | 自定义场景详情 | 新增自定义场景 | 通过json字符串增加自定义场景，格式示例：  {  "scenarioName": "自定义场景",  "uplinkBandwidth": 1000000,  "downlinkBandwidth": 5000000,  "uplinkLatency": 200,  "downlinkLatency": 200,  "uplinkDropRate": 0.05,  "downlinkDropRate": 0.01  } |
| -d | 自定义场景id | 删除自定义场景 | 自定义场景id由网络领航员后端生成，通过-p查询列表获取id后，可以通过-d删除。 |

## 使用示例

### 使用帮助

```
1. > hdc shell netcopilot -h
2. netcopilot usage:
3. -h : show help message
4. -e <enable>: 0 for disable, 1 for enable
5. -p : print all scenario info
6. -s <scenario id>: simulate specified network scenario
7. -c : cancel simulating scenario
8. -P <scenario id>: print specified scenario details
9. -a <custom scenario details>: add custom network scenario
10. -d <scenario id>: delete custom network scenario
```

### 开启/关闭领航员

```
1. > hdc shell netcopilot -e 0
2. Disable netcopilot success

4. > hdc shell netcopilot -e 1
5. Enable netcopilot success
```

### 查看网络场景列表

```
1. > hdc shell netcopilot -p
2. +------------+------------------------------+
3. | ScenarioID | ScenarioName                 |
4. +------------+------------------------------+
5. 1            | 进出电梯
6. 2            | 离家断开WLAN
7. 3            | 到家连上WLAN
8. 4            | 人员拥挤的饭堂
9. 5            | 信号弱的地库
10. 6            | 乘坐地铁
11. 7            | 乘坐高铁（多SIM切换）
12. 8            | 高速公路自驾
13. +------------+------------------------------+
```

### 启动场景模拟

```
1. > hdc shell netcopilot -s 4
2. Success to simulate scenario 4
```

### 停止场景模拟

```
1. > hdc shell netcopilot -c 4
2. Clear active net scenario success
```

### 新增自定义场景

```
1. > hdc shell netcopilot -a "{\"scenarioName\":\"自定义场景1\",\"uplinkBandwidth\":100000,\"downlinkBandwidth\":500000,\"uplinkLatency\":200,\"downlinkLatency\":200,\"uplinkDropRate\":0.05,\"downlinkDropRate\":0.01}"
```

注意

自定义场景子参数需要转成json字符串。

### 查看自定义场景详情

```
1. > hdc shell netcopilot -P 1000
2. Scenario Name: 自定义场景1
3. Uplink Bandwidth: 100000Kbps
4. Downlink Bandwidth: 500000Kbps
5. Uplink Latency: 200ms
6. Downlink Latency: 200ms
7. Uplink Drop Rate: 0.05%
8. Downlink Drop Rate: 0.01%
```

### 删除自定义场景

```
1. > hdc shell netcopilot -d 1000
2. Delete custom scenario success
```
