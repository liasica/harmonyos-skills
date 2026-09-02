---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-116
title: 如何获取手机当前网络连接的子网掩码
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何获取手机当前网络连接的子网掩码
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4972b721d737ba2d9b7e423968720076cb17ab39103d0cc6c981dbcd327f837a
---

## 问题现象

1. 如何获取手机当前网络连接的子网掩码？
2. 如何查看网络的路由信息？

## 背景知识

* [getConnectionPropertiesSync](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectionpropertiessync10)同步获取NetHandle对应的网络的连接信息。
* [网络连接管理](../harmonyos-references/js-apis-net-connection.md)提供管理网络一些基础能力，包括获取默认激活的数据网络、获取所有激活数据网络列表、开启关闭飞行模式、获取网络能力信息等功能。

## 解决方案

1. 系统并未提供直接获取子网掩码的接口，可通过获取网络的连接信息然后计算获得。
   * 在module.json5文件中配置"ohos.permission.GET\_NETWORK\_INFO"权限。
   * 获取子网掩码代码如下：

     ```ts
     import { connection } from '@kit.NetworkKit';

     @Entry
     @Component
     struct SubnetMask {
       @State subnetMaskStr: string = '获取子网掩码';
       /**
        * 计算子网掩码
        * @param prefixLength 前缀长度
        * @returns 子网掩码字符串
        */
       calculateSubnetMask(prefixLength: number): string {
         if (!Number.isInteger(prefixLength) || prefixLength > 32 || prefixLength < 0) {
           return '';
         }
         // 计算每个字节的子网掩码部分
         let subnetMask = '';
         for (let i = 0; i < 4; i++) {
           // 每个字节中的有效位数
           const bits = Math.min(prefixLength, 8);
           // 计算子网掩码字节的值并添加到结果字符串
           subnetMask += (256 - Math.pow(2, 8 - bits)) + '.';
           // 更新剩余的位数
           prefixLength -= bits;
         }
         // 去除末尾的点并返回子网掩码字符串
         return subnetMask.slice(0, -1);
       }

       build() {
         RelativeContainer() {
           Text(this.subnetMaskStr)
             .id('SubnetMaskHelloWorld')
             .fontSize($r('app.float.page_text_font_size'))
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
             .onClick(()=>{
               try {
                 // 1.获取默认网络
                 const netHandle = connection.getDefaultNetSync();
                 // 2.获取网络连接信息
                 const connectionProperties = connection.getConnectionPropertiesSync(netHandle);
                 // 3.提取链路信息
                 const linkAddress = connectionProperties.linkAddresses?.[0];
                 if (linkAddress) {
                   // 计算子网掩码，参数为链路地址前缀的长度
                   this.subnetMaskStr = this.calculateSubnetMask(linkAddress.prefixLength);
                 }
               } catch (err) {
                 console.error(`errCode is ${err.code}, message is ${err.message}`);
               }
             })

         }
         .height('100%')
         .width('100%');
       }
     }
     ```

     示例效果：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/V2HECaLjRg2ol4_1He527Q/zh-cn_image_0000002658970121.png "点击放大")
2. 可以通过[connection.getConnectionPropertiesSync](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectionpropertiessync10)接口获取[ConnectionProperties](../harmonyos-references/js-apis-net-connection.md#connectionproperties)网络连接信息，其中就包含routes路由信息。
