---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-taro
title: Taro框架+H5接入智能填充
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > 三方框架+H5接入智能填充 > Taro框架+H5接入智能填充
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:01+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:ad5ee7c75d48c5a3ad90ccd15ee8d6cfa0d04b5d4b3340186530a3137a3a3eb1
---

**说明** 

目前仅支持已适配HarmonyOS的三方框架应用使用。

Taro及HarmonyOS版工程的搭建请参考官方文档[Harmony Hybrid | Taro 文档](https://docs.taro.zone/docs/harmony-hybrid/)。

## 前提条件

* 基于Web开发HarmonyOS应用。
* 设备智能填充开关必须处于打开状态，请前往“设置 > 隐私和安全 > 智能填充”页面开启开关。
* 设备已连接互联网并且登录华为账号。
* 该应用需已接入[智能填充服务](scenario-fusion-introduction-to-smart-fill.md#申请接入智能填充服务)。

## 开发准备

配置Taro已适配HarmonyOS的开发环境。

## 效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/9idy_rHZT5qWQ43_421ySw/zh-cn_image_0000002706835186.png)

## 示例代码

示例代码仅展示接入智能填充相关部分，请按照实际场景修改后使用。在Taro的Input组件（Form表单的子节点）中添加nativeProps属性，并配置nativeProps中[autocomplete](scenario-fusion-mappingrelationship.md#h5-autocomplete和harmonyos的contenttype的映射关系)属性来支持智能填充，Form表单提交后，当页面导航发生变化时，满足历史表单输入保存的条件时会触发对应弹窗（建议使用HTML <button> 标签进行Form表单提交）。代码如下：

```tsx
import React from 'react';
import { View, Text, Input, Form } from '@tarojs/components';
import Taro, { useLoad  } from '@tarojs/taro';
import './index.scss';

export default function Demo() : React.ReactNode {
  useLoad(() => {
    console.info('Page loaded.');
  });
  function handleSubmit(e) : void {
    Taro.request({
      // 将URL设置为实际的接口路径。
      url: '',
      method: 'POST',
    });
  }
  return (
    <Form onSubmit={handleSubmit}>
      <View className="native-form">
        <View className="form-item">
          <Text className="col-md-4">昵称：</Text>
          <View className="col-md-6">
            <Input
              className="form-value"
              name="nickname"
              type="text"
              nativeProps={{ autocomplete: 'nickname' }}
            ></Input>
          </View>
        </View>
        <View className="form-item">
          <Text className="col-md-4">姓名：</Text>
          <View className="col-md-6">
            <Input
              className="form-value"
              name="name"
              type="text"
              nativeProps={{ autocomplete: 'name' }}
            ></Input>
          </View>
        </View>
        <View className="form-item">
          <Text className="col-md-4">手机号：</Text>
          <View className="col-md-6">
            <Input
              className="form-value"
              name="tel"
              type="text"
              nativeProps={{ autocomplete: 'tel-national' }}
            ></Input>
          </View>
        </View>
        <View className="form-item">
          <Text className="col-md-4">邮箱：</Text>
          <View className="col-md-6">
            <Input
              className="form-value"
              name="email"
              type="text"
              nativeProps={{ autocomplete: 'email' }}
            ></Input>
          </View>
        </View>
        <View className="form-item">
          <Text className="col-md-4">身份证：</Text>
          <View className="col-md-6">
            <Input
              className="form-value"
              name="idcard"
              type="text"
              nativeProps={{ autocomplete: 'id-card-number' }}
            ></Input>
          </View>
        </View>
        <View className="form-item">
          <Text className="col-md-4">带街道地址：</Text>
          <View className="col-md-6">
            <Input
              className="form-value"
              name="street-address"
              type="text"
              nativeProps={{ autocomplete: 'street-address' }}
            ></Input>
          </View>
        </View>
      </View>
      <View>
        <button className="button">提交</button>
      </View>
    </Form>
  );
}
```

index.scss如下：

```scss
.form-item {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  margin-top: 20px;
  .col-md-4 {
    width: 30%;
    text-align: right;
    font-size: 32px;
  }
  .col-md-6 {
    width: 50%;
    .form-value {
      width: 100%;
      border-style: solid;
      border-width: 1px;
      border-color: #333333;
      font-size: 32px;
    }
  }
}
.button {
  width: 20%;
  background-color: #4caf50;
  border: none;
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 24px;
  margin-left: 30%;
  margin-top: 20px;
}
```
