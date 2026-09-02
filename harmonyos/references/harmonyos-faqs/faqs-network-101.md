---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-101
title: 如何判断某个IP是否在某IP段范围内
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何判断某个IP是否在某IP段范围内
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b655e561a9681b2cb45cf666dfc8e0a570a606430bb4849032adf4de876beb28
---

## 问题现象

当前IP：192.168.9.230，如何判断该目标IP是否在10.101.10.210~255.201.255.1范围内？

## 背景知识

IPv4地址采用点分十进制表示法，每个点分部分称为一个"八位组"，范围是0-255。判断某个IP是否在某IP段范围内可以先将IP转换为32位无符号整数，转换原理是基于256进制（2^8）的位权计算。例如：192.168.1.1=192×256³ + 168×256² + 1×256 + 1。

## 解决方案

判断当前IP是否在某IP段范围内，可以参照以下步骤：

1. 将点分十进制格式的IP地址转换为长整型数字，便于比较大小。
2. 检查目标IP是否在指定的起始IP和结束IP范围内。

```screen
function ipToLong(ip: string): number {
  const parts = ip.split('.').map(part => parseInt(part));
  return parts[0] * Math.pow(256, 3) + parts[1] * Math.pow(256, 2) + parts[2] * 256 + parts[3];
}

function isIPInRange(ip: string, startIP: string, endIP: string): boolean {
  const ipNum = ipToLong(ip);
  const startIPNum = ipToLong(startIP);
  const endIPNum = ipToLong(endIP);

  return ipNum >= startIPNum && ipNum <= endIPNum;
}

@Entry
@Component
struct JudgeIp {
  judge() {
    const targetIP = '192.168.9.230';
    const startIP = '10.101.10.210';
    const endIP = '255.201.255.1';

    let res = isIPInRange(targetIP, startIP, endIP);
    try {
      this.getUIContext().getPromptAction().showToast({ message: `目标ip地址是否在范围内: ${res}` });
    } catch (error) {
      console.error(`Error code: ${error.code}, Message: ${error.message}`);
    }
  }

  build() {
    Column() {
      Button('查询').onClick(() => {
        this.judge();
      });
    }.width('100%').height('100%').justifyContent(FlexAlign.Center);
  }
}
```
