---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/network-netcopilot
title: netcopilot工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > netcopilot工具
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:14a206de86e2ddfa074190b49b8ba75d02808c73b1fd2cc17c65e4d7abe49eb4
---

netcopilot是一款帮助开发者进行网络模拟的工具，通过hdc命令行直接调用网络领航员接口，执行网络领航员请求，目前已支持预置场景场景调用和自定义场景调用。

**说明** 

netcopilot工具从API version 20开始支持。

在使用本工具前，开发者需要先获取hdc工具。

## 使用方法

### 命令行说明

```shell
hdc shell netcopilot <命令行参数> <子参数>
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

```shell
> hdc shell netcopilot -h
netcopilot usage:
  -h : show help message
  -e <enable>: 0 for disable, 1 for enable
  -p : print all scenario info
  -s <scenario id>: simulate specified network scenario
  -c : cancel simulating scenario
  -P <scenario id>: print specified scenario details
  -a <custom scenario details>: add custom network scenario
  -d <scenario id>: delete custom network scenario
```

### 开启/关闭领航员

```shell
> hdc shell netcopilot -e 0
Disable netcopilot success

> hdc shell netcopilot -e 1
Enable netcopilot success
```

### 查看网络场景列表

```shell
> hdc shell netcopilot -p
  +------------+------------------------------+
  | ScenarioID | ScenarioName                 |
  +------------+------------------------------+
  1            | 进出电梯
  2            | 离家断开WLAN
  3            | 到家连上WLAN
  4            | 人员拥挤的饭堂
  5            | 信号弱的地库
  6            | 乘坐地铁
  7            | 乘坐高铁（多SIM切换）
  8            | 高速公路自驾
  +------------+------------------------------+
```

### 启动场景模拟

```shell
> hdc shell netcopilot -s 4
Success to simulate scenario 4
```

### 停止场景模拟

```shell
> hdc shell netcopilot -c 4
Clear active net scenario success
```

### 新增自定义场景

```shell
> hdc shell netcopilot -a "{\"scenarioName\":\"自定义场景1\",\"uplinkBandwidth\":100000,\"downlinkBandwidth\":500000,\"uplinkLatency\":200,\"downlinkLatency\":200,\"uplinkDropRate\":0.05,\"downlinkDropRate\":0.01}"
```

**注意** 

自定义场景子参数需要转成json字符串。

### 查看自定义场景详情

```shell
> hdc shell netcopilot -P 1000
Scenario Name: 自定义场景1
Uplink Bandwidth: 100000Kbps
Downlink Bandwidth: 500000Kbps
Uplink Latency: 200ms
Downlink Latency: 200ms
Uplink Drop Rate: 0.05%
Downlink Drop Rate: 0.01%
```

### 删除自定义场景

```shell
> hdc shell netcopilot -d 1000
Delete custom scenario success
```
